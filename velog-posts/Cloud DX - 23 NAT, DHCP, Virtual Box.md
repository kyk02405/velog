# Cloud DX - 23 NAT, DHCP, Virtual Box

- 📅 Published: Thu, 30 Oct 2025 08:53:42 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-23-NAT-DHCP-Virtual-Box)

<hr />
<h1 id="span-style--colorskybluenatspannetwork-address-translation--patport-address-translation"><span style="color: skyblue;">NAT</span>(Network Address Translation) &amp; PAT(Port Address Translation)</h1>
<h2 id="개요">개요</h2>
<ul>
<li><code>NAT</code>는 <code>Routing Protocol</code> 3단계 (기본설정, 라우팅 테이블, 라우팅 프로토콜) 중에서 <code>3단계인 라우팅 프로토콜</code>이 없다.</li>
<li><code>Dynamic NAT</code>는 <code>공유기</code>와 동일하고 <code>Static NAT</code>는 <code>NAS</code>와 동일한 기능을 한다.</li>
<li>외부망으로의 통신을 위해 <code>사설IP</code>를 <code>공인IP</code>로 또는 <code>공인IP</code>를 <code>사설IP</code>로 변환할 때 사용한다.</li>
</ul>
<h2 id="nat와-pat-비교">NAT와 PAT 비교</h2>
<ul>
<li><code>NAT</code><ul>
<li><code>IP</code> 헤더의 주소를 다른 주소로 바꾸는 기술</li>
</ul>
</li>
<li><code>PAT</code><ul>
<li><code>NAT</code>와 동일한 기능을 가지고 있다.</li>
<li>사용자들마다 서로 다른 포트 번호만 다르게 해서 외부망으로 나가게 해주는 기술</li>
</ul>
</li>
</ul>
<h2 id="동적-nat와-정적-nat">동적 NAT와 정적 NAT</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d636a29b-a5a5-416e-a6c1-89e729e16809/image.png" /></p>
<ul>
<li>동적 NAT는 호스트가 요구하는 Traffic을 받으면 IP 주소내에서 사설 IP를 라우터에 설정된 주소풀에 있는 공인 IP로 변환한 후 외부로 전달한다. 외부에서 응답 신호가 라우터로 돌아오면 
NAT라우터는 NAT Table에 있는 이전 정보로 목적지로 들어온 주소를 사설 IP로 변환해서 내부망으로 전달한다 </li>
<li>정적 NAT는 외부주소로 들어온 요청을 내부 서버로 전달 될 수 있도록 목적지 주소를 변환하는 
기능이다. 이 방법으로 사설망 서버를 구현하고 외부 주소로 들어오는 연결을 내부 서버로 전달
할 수 있다</li>
</ul>
<hr />
<h2 id="dynamic-nat-설정">Dynamic NAT 설정</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8c3313fa-303f-4574-9d37-3b56b75fa3ca/image.png" /></p>
<h3 id="단계별-설정">단계별 설정</h3>
<ul>
<li><p>Step 1. <code>(외부망)</code> <code>IP</code>변환에 사용할 전역 주소풀을 설정한다.</p>
<ul>
<li><code>NAT</code>변환에 사용할 <code>공인IP</code>와 <code>Subnet Mask</code>를 지정한다.</li>
</ul>
</li>
<li><p>Step 2. <code>(내부망)</code>내부에서 <code>IP</code>변환을 허용할 주소를 <code>공인IP</code>와 <code>Standard Access-list</code>로 정의한다</p>
<ul>
<li><code>NAT</code> 변환에 사용할 <code>내부IP</code> 지정하는데 <code>ACL</code>을 사용한다.</li>
<li>사용되는 대역의 범위는 <code>Wildcard Mask</code>이다.</li>
</ul>
</li>
<li><p>Step 3.동적 변환을 수립하기 위한 <code>NAT</code> 설정을 한다</p>
<ul>
<li><code>Step 2</code>에서 지정한 <code>내부IP</code>를 <code>Step 1</code>에서 지정한 <code>공인IP</code>로 변환한다. </li>
<li>맨 뒤에 <code>overload</code>를 입력하면 <code>NAT</code>가 아닌 <code>PAT</code>로 동작한다.</li>
</ul>
</li>
<li><p>Step 4.각 인터페이스로 이동 후 내부와 외부를 각각 설정한다 </p>
</li>
<li><p>Step 5. </p>
</li>
</ul>
<hr />
<h2 id="01pkt">01.pkt</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f478ceaf-0537-4bf6-a6d8-4446f1453bc8/image.png" /></p>
<h2 id="r1">R1</h2>
<h3 id="1단계">1단계</h3>
<h3 id="2단계">2단계</h3>
<h3 id="nat">NAT</h3>
<blockquote>
<pre><code class="language-bash">R1(config)# ip nat pool R1N 210.128.62.1 210.128.62.1 netmask 255.255.255.252
R1(config)# access-list 1 permit 172.16.0.0 0.0.0.255
R1(config)# ip nat inside source list 1 pool R1N
R1(config)# int f0/0
R1(config-if)# ip nat inside 
R1(config-if)# exit
R1(config)# int s0/0
R1(config-if)# ip nat oustside </code></pre>
</blockquote>
<pre><code>- `R2`도 설정
- 여기까지 한다고 해서 `R2` 하단에 있는 `PC`들과 통신이 되는 것은 아니다.
`NAT` 외부와의 연결을 위한 기능을 하는 것이 아니고 외부에서 `IP`를 받은 후 `내부망`으로 사설 `IP`를 부여하기 위한 기능만을 제공할 뿐이다.
따라서 외부에 있는 임의의 라우터와 연결을 위해서는 3단계인 라우팅 프로토콜을 설정해야 한다.

### 3단계
### NAT 테이블 테스트 및 확인
- `R1`, `R2` 콘솔 화면을 출력해 놓는다
- `sh ip nat translation` 명령만 입력한다
- `PC0`에서 `PC5`로 `ping`을 때린다
- 통신이 잘 되는지 확인이 되면 앞에서 입력만 했던 명령을 때린다.
  - ![](https://velog.velcdn.com/images/kyk02405/post/d3707bce-9ba2-4d5e-9e5e-8d6fe820e7d5/image.png)

---
# DHCP(Dynamic Host Configuration Protocol)

## 개요
- `IP`를 자동으로 호스트에 부여하기 위한 프로토콜이다.
- `공유기`는 `DHCP` 기능을 하는 라우터가 내장되어 있는 장비이다.

## 실습
&gt;### 라우팅 테이블 설정
```bash
Router(config)#hostname DHCP-Server
DHCP-Server(config)#int f0/0
DHCP-Server(config-if)#ip address 192.168.0.254 255.255.255.0
DHCP-Server(config-if)#no sh
DHCP-Server(config-if)#no shutdown </code></pre><blockquote>
<h3 id="dhcp-server">DHCP Server</h3>
</blockquote>
<ul>
<li>Step 1. 할당된 <code>IP Pool</code>(영역) 정의<pre><code class="language-bash">DHCP-Server(config)# ip dhcp pool cisco</code></pre>
</li>
<li>Step 2. 할당될 <code>IP 대역</code>들 정의<pre><code class="language-bash">DHCP-Server(dhcp-config)# network 192.168.0.0 255.255.255.0</code></pre>
</li>
<li>Step 3. Default-Router 설정(default-gateway)<pre><code class="language-bash">DHCP-Server(dhcp-config)# default-router 192.168.0.254
DHCP-Server(dhcp-config)# exit
DHCP-Server(config)#</code></pre>
</li>
<li>Step 4. 할당되면 안되는 IP 주소(192.168.0.254) 설정 <ul>
<li>Gateway로 이미 할당되어 있기 때문에 Client에게 부여해서는 안된다.<pre><code class="language-bash">DHCP-Server(config)# ip dhcp excluded-address 192.168.0.254
DHCP-Server(config)# exit</code></pre>
<blockquote>
<ul>
<li>Step 5. DHCP로 IP 할당</li>
</ul>
</blockquote>
</li>
</ul>
</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/eb60c40a-83b9-4a4d-8d41-26cd8a11caa7/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/644a4d82-da09-4477-af14-feab64a0e3e0/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ea60617b-358d-46b9-aeb5-e159a7b1270c/image.png" /></li>
</ul>
<hr />
<h2 id="oracle-virtual-box">Oracle Virtual Box</h2>
<h3 id="다운로드">다운로드</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/706f3e65-b7f6-4ad4-8f01-9efeeca56e02/image.png" /></p>
<h3 id="설치">설치</h3>
<h3 id="기본-환경설정">기본 환경설정</h3>
<h3 id="모든-vmvirtual-machine에-적용되는-환경설정">모든 <code>VM(Virtual Machine)</code>에 적용되는 환경설정</h3>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e91848e1-1008-4fbc-81ae-19f891d73ea3/image.png" /></li>
<li>호스트키 조합</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/31ed1653-b8cf-4549-9b5d-164bba17850c/image.png" /></li>
<li>이 때 하단에 보면 <code>확인</code>이 <code>비활성 상태</code>로 나타난다.</li>
<li>그리고 <code>잘못된 설정 감지됨</code>이 보이는데 마우스를 가져가면 <code>Default machine folder is missing</code>이 출력된다.</li>
<li><code>일반</code>의 우측에 있는 <code>Default Machine Folder</code> 영역을 확인한다.<ul>
<li><code>C:\Users\CloudDX\VirtualBox VMs</code></li>
</ul>
</li>
<li>옆에 있는 화살표를 클릭한 후 <code>기타</code>를 클릭한다.</li>
<li>그리고 <code>C:\Users\CloudDX\.VirtualBox</code>로 경로를 변경<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fd3f35ac-e42a-4c59-8d8d-0a6d363ad1c6/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="작업-대상인-해당-vmvirtual-machine에-적용되는-환경설정">작업 대상인 해당 <code>VM(Virtual Machine)</code>에 적용되는 환경설정</h3>
<ul>
<li>이 설정을 하기 위해서는 <code>가상 머신</code>을 먼저 동작이 되어야 한다.</li>
<li>따라서 현재 <code>가상 머신</code>이 없기 때문에 설치를 먼저 진행하도록 한다.</li>
<li>여기서는 <code>Rocky Linux 9.6</code>을 이용한 <code>가상 머신</code>을 설치한다.<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/76c26f62-a8d8-4109-81d6-4026e03c9299/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5e504521-a99b-4a0e-8b4a-71298ef20935/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c8550c0a-bafc-49b7-9fbc-db1f1b6aeed9/image.png" /></li>
</ul>
</li>
</ul>
<h3 id="가상-머신">가상 머신</h3>
<ul>
<li>구성</li>
</ul>
<h3 id="확장팩-설치">확장팩 설치</h3>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/eb7473a1-50bc-4024-aa91-b8b4041dc4d6/image.png" /></li>
</ul>
<h3 id="방법-1-한대의-시스템만-사용할-때">방법 1. 한대의 시스템만 사용할 때</h3>
<ul>
<li><p>테스트 1. <code>Google DNS</code>인 8.8.8.8로 <code>ping</code> 테스트를 진행한다</p>
<ul>
<li>통신이 잘된다</li>
</ul>
</li>
<li><p><code>Host OS</code>의 <code>IP</code> 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1855f719-1d18-4201-a154-afad181a1773/image.png" /></li>
</ul>
</li>
<li><p><code>Guest OS</code>의 <code>IP</code> 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8fce5af9-00c8-4017-b30f-375c51ffdc00/image.png" /></li>
</ul>
</li>
<li><p>어뎁터 설정</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a353889b-fe3b-4a4a-ab5f-d3d579e61b5e/image.png" /></li>
</ul>
</li>
<li><p><code>Guest OS(Rocky86)</code>의 네트워크 설정</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/850f279e-a586-4a55-8763-1b57f8bac5bc/image.png" /></li>
<li>네트워크 데몬을 재실행해도 <code>IP</code>변화는 없음</li>
</ul>
</li>
<li><p><code>Putty</code> 접속</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/67478bbe-4542-4307-b487-a70ed191a12c/image.png" /></li>
<li>현재 설치만 진행했기 때문에 관리자 접속은<code>SSH</code> 환경설정에서 변경해 주면 된다.</li>
<li><code>vi /etc/ssh/sshd_config</code> 설정</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e585533b-a63a-4984-a313-cb0a35d49e00/image.png" /></li>
</ul>
</li>
</ul>
<blockquote>
<p> ctrl + alt + f = 전체화면
  ctrl + alt + home = 메뉴 </p>
</blockquote>
<hr />
<h3 id="방법-2-여러-대의-시스템을-사용할-때">방법 2. 여러 대의 시스템을 사용할 때</h3>
<ul>
<li>어뎁터 설정<ul>
<li>시스템이 동작중일 때는</li>
</ul>
</li>
<li><code>Guest OS(Rocky96)</code> 의 네트워크 설정을 변경할 수가 없다.</li>
</ul>