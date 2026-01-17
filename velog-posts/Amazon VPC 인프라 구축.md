# Amazon VPC 인프라 구축

- 📅 Published: Sat, 17 Jan 2026 06:36:04 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Amazon-VPC-%EC%9D%B8%ED%94%84%EB%9D%BC-%EA%B5%AC%EC%B6%95)

<hr />
<h1 id="aws-실습-amazon-vpc-인프라-구축-및-ec2-배포">[AWS 실습] Amazon VPC 인프라 구축 및 EC2 배포</h1>
<p>이 포스팅은 AWS 네트워킹의 핵심 구성 요소인 VPC, 서브넷(Public/Private), 라우팅 테이블, 게이트웨이(IGW/NAT)를 직접 구축하고 EC2 인스턴스를 배치해보는 실습 과정을 정리한 것입니다.</p>
<h2 id="1-실습-목표">1. 실습 목표</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cf7a1975-b7a7-48db-8069-0c012df2049a/image.png" /></p>
<ul>
<li>Amazon VPC 생성 및 설정</li>
<li>퍼블릭(Public) 및 프라이빗(Private) 서브넷 구성</li>
<li>인터넷 게이트웨이(IGW) 및 NAT 게이트웨이 설정</li>
<li>라우팅 테이블 구성 및 서브넷 연결</li>
<li>보안 그룹(Security Group) 설정 및 EC2 인스턴스 배포</li>
<li>Session Manager를 통한 연결 테스트</li>
</ul>
<hr />
<h2 id="2-vpc-생성-virtual-private-cloud">2. VPC 생성 (Virtual Private Cloud)</h2>
<p>가장 먼저 논리적으로 격리된 가상 네트워크인 VPC를 생성합니다.</p>
<ol>
<li><strong>VPC 생성</strong><ul>
<li><strong>이름:</strong> <code>Lab VPC</code></li>
<li><strong>IPv4 CIDR:</strong> <code>10.0.0.0/16</code></li>
</ul>
</li>
<li><strong>DNS 호스트 이름 활성화</strong><ul>
<li>VPC 설정 편집에서 <strong>Enable DNS hostnames</strong> 체크 후 저장.</li>
<li><em>이 설정은 VPC 내 인스턴스에 퍼블릭 DNS 호스트 이름을 할당하기 위해 필요합니다.</em></li>
</ul>
</li>
</ol>
<hr />
<h2 id="3-서브넷subnet-생성">3. 서브넷(Subnet) 생성</h2>
<p>VPC의 IP 주소 범위를 나누어 퍼블릭과 프라이빗 용도의 서브넷을 생성합니다.</p>
<h3 id="31-퍼블릭-서브넷-public-subnet">3.1 퍼블릭 서브넷 (Public Subnet)</h3>
<p>인터넷과 직접 통신이 가능한 서브넷입니다.</p>
<ul>
<li><strong>VPC:</strong> Lab VPC</li>
<li><strong>이름:</strong> <code>Public Subnet</code></li>
<li><strong>가용 영역(AZ):</strong> 첫 번째 가용 영역 선택</li>
<li><strong>CIDR 블록:</strong> <code>10.0.0.0/24</code></li>
<li><strong>설정 변경:</strong> 서브넷 생성 후 <code>Enable auto-assign public IPv4 address</code> 활성화.</li>
</ul>
<h3 id="32-프라이빗-서브넷-private-subnet">3.2 프라이빗 서브넷 (Private Subnet)</h3>
<p>인터넷과 직접 연결되지 않고 격리된 서브넷입니다.</p>
<ul>
<li><strong>VPC:</strong> Lab VPC</li>
<li><strong>이름:</strong> <code>Private Subnet</code></li>
<li><strong>가용 영역(AZ):</strong> 첫 번째 가용 영역 선택 (퍼블릭과 동일하게 설정)</li>
<li><strong>CIDR 블록:</strong> <code>10.0.2.0/23</code><blockquote>
<p><strong>참고:</strong> CIDR <code>10.0.2.0/23</code>은 <code>10.0.2.x</code>와 <code>10.0.3.x</code> 대역을 모두 포함하므로 퍼블릭 서브넷보다 크기가 2배 큽니다.</p>
</blockquote>
</li>
</ul>
<hr />
<h2 id="4-인터넷-게이트웨이-igw-구성">4. 인터넷 게이트웨이 (IGW) 구성</h2>
<p>퍼블릭 서브넷이 인터넷과 통신할 수 있도록 게이트웨이를 연결합니다.</p>
<ol>
<li><strong>생성:</strong> 이름 <code>Lab IGW</code>로 생성.</li>
<li><strong>VPC 연결:</strong> 생성한 IGW를 <code>Lab VPC</code>에 연결(Attach).</li>
<li><strong>퍼블릭 라우팅 테이블 생성 및 연결</strong><ul>
<li><strong>이름:</strong> <code>Public Route Table</code></li>
<li><strong>라우팅 추가:</strong> <code>0.0.0.0/0</code> (모든 트래픽) → 타겟을 <code>Internet Gateway</code>로 설정.</li>
<li><strong>서브넷 연결:</strong> <code>Public Subnet</code>을 이 라우팅 테이블에 연결.</li>
</ul>
</li>
</ol>
<hr />
<h2 id="5-퍼블릭-보안-그룹-및-인스턴스-시작">5. 퍼블릭 보안 그룹 및 인스턴스 시작</h2>
<h3 id="51-보안-그룹-security-group-생성">5.1 보안 그룹 (Security Group) 생성</h3>
<ul>
<li><strong>이름:</strong> <code>Public SG</code></li>
<li><strong>인바운드 규칙:</strong> <code>HTTP</code> (포트 80) 허용, 소스는 <code>Anywhere-IPv4</code>.</li>
</ul>
<h3 id="52-퍼블릭-ec2-인스턴스-생성">5.2 퍼블릭 EC2 인스턴스 생성</h3>
<p>퍼블릭 서브넷에 웹 서버 역할을 할 인스턴스를 배포합니다.</p>
<ul>
<li><strong>이름:</strong> <code>Public Instance</code></li>
<li><strong>AMI:</strong> Amazon Linux 2023 AMI</li>
<li><strong>인스턴스 유형:</strong> <code>t3.micro</code></li>
<li><strong>네트워크:</strong> <code>Lab VPC</code> &gt; <code>Public Subnet</code> &gt; 퍼블릭 IP 자동 할당 <code>Enable</code></li>
<li><strong>보안 그룹:</strong> <code>Public SG</code> 선택</li>
<li><strong>IAM 역할:</strong> <code>EC2InstProfile</code> (Session Manager 사용 권한)</li>
<li><strong>사용자 데이터 (User Data):</strong> Apache 웹 서버 설치 스크립트 입력</li>
</ul>
<pre><code class="language-bash">#!/bin/bash
# Apache 웹 서버 및 PHP 설치
yum update -y
yum install -y httpd php8.1
systemctl enable httpd.service
systemctl start httpd
cd /var/www/html
wget https://us-west-2-tcprod.s3.amazonaws.com/courses/ILT-TF-200-ARCHIT/v7.10.4.prod-6bb65e0f/lab-2-VPC/scripts/instanceData.zip
unzip instanceData.zip</code></pre>
<hr />
<h2 id="6-nat-게이트웨이-및-프라이빗-라우팅-구성">6. NAT 게이트웨이 및 프라이빗 라우팅 구성</h2>
<p>프라이빗 서브넷의 인스턴스가 인터넷으로 나가는 트래픽(예: 업데이트)은 허용하되, 외부에서 직접 접근하는 것은 차단하기 위해 NAT 게이트웨이를 사용합니다.</p>
<ol>
<li><strong>NAT 게이트웨이 생성</strong><ul>
<li><strong>서브넷:</strong> 반드시 <strong><code>Public Subnet</code></strong>을 선택해야 함.</li>
<li><strong>Elastic IP:</strong> 새로 할당하여 연결.</li>
</ul>
</li>
<li><strong>프라이빗 라우팅 테이블 생성 및 연결</strong><ul>
<li><strong>이름:</strong> <code>Private Route Table</code>.</li>
<li><strong>라우팅 추가:</strong> <code>0.0.0.0/0</code> → 타겟을 <strong><code>NAT Gateway</code></strong>로 설정.</li>
<li><strong>서브넷 연결:</strong> <code>Private Subnet</code>을 이 라우팅 테이블에 연결.</li>
</ul>
</li>
</ol>
<hr />
<h2 id="7-프라이빗-보안-그룹-및-인스턴스-시작">7. 프라이빗 보안 그룹 및 인스턴스 시작</h2>
<h3 id="71-프라이빗-보안-그룹-생성">7.1 프라이빗 보안 그룹 생성</h3>
<p>프라이빗 인스턴스는 퍼블릭 인스턴스를 통해서만 접근을 허용하도록 설정합니다.</p>
<ul>
<li><strong>이름:</strong> <code>Private SG</code></li>
<li><strong>인바운드 규칙:</strong><ul>
<li><strong>유형:</strong> HTTP</li>
<li><strong>소스:</strong> <strong><code>Public SG</code></strong> (보안 그룹 ID 참조).</li>
<li><em>설명: IP 주소 대신 보안 그룹을 소스로 지정하면 해당 보안 그룹에 속한 리소스에서의 접근만 허용됩니다.</em></li>
</ul>
</li>
</ul>
<h3 id="72-프라이빗-ec2-인스턴스-생성">7.2 프라이빗 EC2 인스턴스 생성</h3>
<ul>
<li><strong>이름:</strong> <code>Private Instance</code></li>
<li><strong>네트워크:</strong> <code>Lab VPC</code> &gt; <strong><code>Private Subnet</code></strong> &gt; 퍼블릭 IP 자동 할당 <strong><code>Disable</code></strong></li>
<li><strong>보안 그룹:</strong> <code>Private SG</code> 선택</li>
<li><strong>IAM 역할:</strong> <code>EC2InstProfile</code></li>
<li><strong>사용자 데이터:</strong> 퍼블릭 인스턴스와 동일한 스크립트 사용.</li>
</ul>
<hr />
<h2 id="8-연결-확인-및-테스트">8. 연결 확인 및 테스트</h2>
<h3 id="81-퍼블릭-인스턴스-확인">8.1 퍼블릭 인스턴스 확인</h3>
<ul>
<li>브라우저 주소창에 <code>Public Instance</code>의 퍼블릭 DNS 주소를 입력하여 웹 페이지가 뜨는지 확인합니다.</li>
<li>AWS 콘솔의 <strong>Session Manager</strong>를 통해 접속한 뒤 <code>curl</code> 명령어로 외부 인터넷 연결을 확인합니다.</li>
</ul>
<h3 id="82-프라이빗-인스턴스-확인">8.2 프라이빗 인스턴스 확인</h3>
<ul>
<li>프라이빗 인스턴스는 퍼블릭 IP가 없으므로 <strong>Session Manager</strong>를 통해 접속합니다.</li>
<li><code>curl</code> 명령어로 외부 통신(NAT 게이트웨이 경유)이 되는지 확인합니다.</li>
<li>(선택 사항) 퍼블릭 인스턴스에서 프라이빗 인스턴스의 프라이빗 IP로 <code>curl</code>을 날려 내부 통신을 확인할 수 있습니다.</li>
</ul>
<h3 id="tip-ping-테스트를-위한-보안-그룹-수정">(Tip) Ping 테스트를 위한 보안 그룹 수정</h3>
<p>기본적으로 보안 그룹은 Ping(ICMP)을 허용하지 않습니다. 핑 테스트가 필요하다면 <code>Private SG</code>의 인바운드 규칙에 <strong>ICMP - IPv4</strong>를 추가하고 소스를 <code>Public SG</code>로 설정해야 합니다.</p>
<blockquote>
<h3 id="span-stylecolorred만약-private-보안-그룹에서-아웃바운드-트래픽을-막아놨으면-핑-응답이-안가는가span"><span style="color: red;">만약 private 보안 그룹에서 아웃바운드 트래픽을 막아놨으면 핑 응답이 안가는가?</span></h3>
<p>결론부터 말씀드리면, <strong>핑 응답(ICMP Echo Reply)은 문제없이 전달됩니다.</strong>
AWS의 <strong>보안 그룹(Security Group)</strong>은 <strong>상태 저장(Stateful)</strong> 방식으로 동작하기 때문입니다. 이 개념은 우리 프로젝트처럼 보안이 중요한 금융/트레이딩 플랫폼 아키텍처에서 매우 중요한 포인트입니다. </p>
</blockquote>
<h3 id="🛡️-왜-아웃바운드-규칙과-상관없이-응답이-가능할까">🛡️ 왜 아웃바운드 규칙과 상관없이 응답이 가능할까?</h3>
<p>AWS 보안 그룹의 <span style="color: red;"><strong>Stateful</strong></span> 특성 때문입니다.</p>
<ol>
<li><strong>상태 기억</strong>: 보안 그룹은 인바운드로 들어온 요청이 '허용'되면, 그 요청에 대한 <strong>응답(Return Traffic)을 기억</strong>합니다.</li>
<li><strong>자동 허용</strong>: 일단 인바운드 규칙을 통과한 트래픽의 응답은 아웃바운드 규칙을 확인하지 않고 <strong>자동으로 통과</strong>시킵니다.</li>
<li><strong>반대의 경우도 동일</strong>: 만약 우리 인스턴스에서 외부로 먼저 요청(Outbound)을 보냈다면, 그에 대한 응답(Inbound) 역시 인바운드 규칙과 상관없이 자동으로 허용됩니다.<h3 id="즉-인바운드에서-핑icmp을-허용했다면-아웃바운드가-모두-막혀있더라도-핑에-대한-응답은-나갈-수-있습니다"><strong>즉, 인바운드에서 핑(ICMP)을 허용했다면, 아웃바운드가 모두 막혀있더라도 '핑에 대한 응답'은 나갈 수 있습니다.</strong></h3>
</li>
</ol>
<hr />
<h3 id="⚠️-주의해야-할-점-네트워크-acl-nacl">⚠️ 주의해야 할 점: 네트워크 ACL (NACL)</h3>
<p>만약 보안 그룹이 아니라 <strong>네트워크 ACL(Network ACL)</strong>에서 아웃바운드를 막았다면 이야기가 달라집니다.</p>
<ul>
<li><strong>NACL은 Stateless(상태 비저장)</strong>입니다. </li>
<li>NACL에서 트래픽을 제어한다면 요청(Inbound)과 응답(Outbound) 규칙을 <strong>각각</strong> 만들어줘야 합니다.</li>
<li>우리 아키텍처에서 서브넷 단위의 추가 보안을 위해 NACL을 건드렸다면, 아웃바운드 0.0.0.0/0 허용 여부를 반드시 확인해야 합니다. </li>
</ul>
<hr />
<h2 id="📝-요약">📝 요약</h2>
<p>이 실습을 통해 다음과 같은 아키텍처를 완성했습니다.</p>
<ol>
<li><strong>VPC</strong> 내에 <strong>Public/Private 서브넷</strong> 분리</li>
<li><strong>IGW</strong>를 통해 퍼블릭 서브넷의 인터넷 접근 허용</li>
<li><strong>NAT Gateway</strong>를 통해 프라이빗 서브넷의 아웃바운드 인터넷 접근 허용</li>
<li><strong>Route Table</strong> 조작을 통해 트래픽 흐름 제어</li>
<li><strong>Security Group</strong>을 통해 계층 간(Tier) 접근 제어 구현</li>
</ol>