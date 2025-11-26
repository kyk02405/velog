# Cloud DX - 50 VPC(Virtual Private Cloud)

- 📅 Published: Wed, 26 Nov 2025 12:05:39 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-50-VPCVirtual-Private-Cloud)

<hr />
<h1 id="01-vpcvirtual-private-cloud">01. VPC(Virtual Private Cloud)</h1>
<h2 id="11-인프라-구축subnet--routing--internet-gateway">1.1 인프라 구축(Subnet / Routing / Internet Gateway)</h2>
<h3 id="개요">개요</h3>
<ul>
<li><p>VPC(Virtual Private Cloud)</p>
</li>
<li><p>사용자는 자기가 원하는대로 <code>IP 주소 범위 선택</code>, <code>서브넷 생성</code>, <code>라우팅 테이블</code>, <code>인터넷 게이트웨이</code> 구성 등 가상 네트워크 환경을 구성해 <code>VPC</code>를 생성할 수 있다.
한마디로 <code>AWS용 나만의 개인 네트워크 망 데이터센터</code>라고 이해하면 된다.</p>
</li>
<li><p><code>Public Cloud</code> 환경에서 사용할 수 있는 고객 전용 사설 네트워크를 말한다.</p>
</li>
<li><p><code>Public Cloud</code> 환경에서 사용할 수 있는 고객 전용 사설 네트워크를 말한다.</p>
</li>
<li><p><code>VPC</code> 사용이 의무화된 데다 대부분의 <code>AWS 서비스가 VPC에 의존적</code>이기 때문에 VPC에 대한 이해는 필수적이다.</p>
</li>
<li><p><code>VPC</code> 도입</p>
</li>
<li><p>사용자에 의해 생성되는 VPC 종류</p>
</li>
<li><p>사용자는 직접 VPC를 생성해서 사용할 수도 있고</p>
</li>
<li><p>계정을 생성 시 <code>Region</code>별로 <code>Default</code>로 생성되는 VPC를 사용할 수도 있다.</p>
</li>
<li><p>다른 네트워크와 논리적으로 분리되어 있기 때문에 IT 인프라를 안전하게 구축하고 간편하게 관리할 수 있는 장점이 있다.</p>
</li>
</ul>
<hr />
<ul>
<li><p>도입 전 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9181a34d-cebd-4380-b17a-df957e711185/image.png" /></p>
<ul>
<li>예전에는, 아래와 같이 <code>VPC</code> 이전 <code>EC2-클래식 네트워크</code>는 여러 사용자의 인스턴스들이 거미줄처럼 얽혀있어 복잡도가 높았다. &lt;&lt;001.png&gt;&gt;</li>
</ul>
</li>
<li><p>도임 후 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bb71a447-932e-41b0-975e-3753b9c7d0e5/image.png" /></p>
<ul>
<li><code>Amazon VPC</code>가 도입된 이후로 아래와 같이 인스턴스가 <code>VPC</code>에 속함으로써 네트워크를 구분할 수 있게 되었다. &lt;&lt;002.png&gt;&gt;</li>
<li><code>VPC</code> 별로 필요한 설정을 통해 인스턴스에 네트워크 설정을 적용할 수 있게 되었다.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="vpc의-이해">VPC의 이해</h3>
<ul>
<li><p>003.png <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/507d62fc-3ca1-445c-87b8-3cdd0c291ad1/image.png" /></p>
</li>
<li><p><code>VPC</code>에는 리전의 각 <code>가용성 영역</code>에 <code>하나의 서브넷</code>이 있다.</p>
</li>
<li><p>각 서브넷에는 <code>EC2 Instance (인스턴스)</code>가 있고, <code>VPC</code>의 리소스와 인터넷 간의 통신을 허용하는 <code>Internet Gateway (인터넷 게이트웨이)</code>가 있다.</p>
</li>
<li><p>Subnet Mask</p>
<ul>
<li><p><code>Network ID</code>와 <code>Host ID</code>를 구분하는 역할을 한다.</p>
<ul>
<li><p><code>Network ID</code></p>
<ul>
<li><code>대역</code>을 구분한다.</li>
</ul>
</li>
<li><p><code>Host ID</code></p>
<ul>
<li>대역 안에서 사용하는 호스트(PC)에게 IP를 부여한다.</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li><p>이 그림의 <code>네트워크 트래픽</code>은 <code>각 리전 내 2개의 VPC</code> 간에 공유되고 있는 것을 알 수 있다.(004.png)
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/798d50d2-250b-4644-a76c-843ce94a35d5/image.png" /></p>
</li>
<li><p><code>리소스 배치</code>, <code>연결 및 보안</code>을 포함하여 <code>가상 네트워킹 환경을 완전히 제어</code>할 수 있다.</p>
<ul>
<li>1st. AWS 서비스 콘솔에서 VPC를 설정하여 시작한다.</li>
<li>2nd. <code>EC2</code> (Amazon Elastic Compute Cloud) 및 <code>RDS</code> (Amazon Relational Database Service) 인스턴스와 같은 리소스를 VPC에 추가한다.</li>
<li>3rd. 마지막으로 VPC가 계정, 가용 영역 또는 AWS 리전에서 서로 통신하는 방법을 정의한다.</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li><p>이 그림은 <code>VPC</code>를 <code>/16</code>으로 생성하고 난 후 <code>Subnet</code>을 생성한 예이다. (005.png)
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/62e74986-1837-4461-a108-dc36718b00d2/image.png" /></p>
</li>
<li><p>서브넷을 최대 크기인 <code>/16</code>으로 <code>설정(B Class)</code>하고 있다.</p>
</li>
<li><p><code>AWS Cloud</code> 내에는 IDC의 집합인 <code>Region</code>이 존재하며 <code>Region</code>은 IDC인 다수의 <code>Availability Zone(AZ)</code>로 이루어지고 있다.</p>
</li>
<li><p>이 중에서 <code>VPC</code>는 <code>Region</code>에 상응하는 규모의 네트워크를 뜻한다는 것을 알 수 있다.</p>
</li>
</ul>
<hr />
<h2 id="12-vpc를-알아보기-위한-사전-지식필수">1.2 VPC를 알아보기 위한 사전 지식(필수)</h2>
<h3 id="121-amazon-ec2-vpc와-amazon-vpc-비교">1.2.1 Amazon EC2-VPC와 Amazon VPC 비교</h3>
<ul>
<li><code>Amazon EC2-VPC</code><ul>
<li>자동 생성<ul>
<li><code>기본값(Default)</code>으로 생성되어 있는 <code>VPC</code>는 절대 삭제해서는 안된다.    </li>
</ul>
</li>
<li><ul>
<li>Amazon에서는 기본값으로 제공하고 있다.</li>
</ul>
</li>
</ul>
</li>
<li><code>Amazon VPC</code>(수동생성)<ul>
<li>AWS의 확장 가능한 인프라를 사용한다는 이점과 함께 고객의 자체 데이터 센터에서 운영하는 기존 네트워크와 매우 유사하다.</li>
<li>AWS Cloud에서 다른 가상 네트워크와 논리적으로 분리되어 있다.</li>
<li>(핵심) IP 주소 범위와 VPC 범위를 설정하고 서브넷을 추가하고 보안 그룹을 연결한 다음 라우팅 테이블을 구성한다.</li>
<li>이 블로그에서는 임의적으로 AWS에서 디폴트로 지원하는 EC2-VPC가 아닌 Amazon VPC를 중점적으로 다루고 있다.</li>
<li>VPC는 Amazon 콘솔에서 생성된다.</li>
<li>하나의 VPC는 하나의 Region내에서만 생성이 가능하고 두 개 이상의 리전에 걸치는 것은 불가능하다.</li>
<li>그러나 하나의 VPC는 여러개의 Amazon Availability Zone (AZ) 에 걸쳐서 생성될 수 있다.</li>
<li>또한 가질 수 있는 IP 주소의 Range는 2^16 = 65535로 제한된다.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="122-public-subnet--private-subnet">1.2.2 Public Subnet &amp; Private Subnet</h3>
<ul>
<li><p>VPC 내에는 보통 Public Subnet과 Private Subnet으로 구성되어 있다.</p>
</li>
<li><p>Public Subnet</p>
<ul>
<li>Internet Gateway, ELB, 그리고 Public IP/Elastic IP를 가진 인스턴스를 내부에 가지고 있다.</li>
<li>특히, Public Subnet 내에 있는 Nat Instance를 통하여 Private Subnet 내에 있는 instances이 인터넷을 가능하게 해준다.</li>
</ul>
</li>
<li><p>Private Subnet</p>
<ul>
<li>기본적으로 외부와 차단되어 있다.</li>
<li>Private Subnet 내의 인스턴스들은 private ip만을 가지고 있으며 internet inbound/outbound가 불가능 하고 오직 다른 서브넷과의 연결만이 가능하다.</li>
</ul>
</li>
<li><p>006.png <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f253b77e-9001-4459-9cd1-8b0bc38bffa9/image.png" /></p>
</li>
<li><p>이 아키텍처는 <code>2개의 가용 영역</code>에 <code>2개의 public subnet</code>과 <code>4개의 private subnet</code>으로 구성되어 있다.</p>
</li>
<li><p><code>Private subnet 1, 2</code>에는 <code>Web 인스턴스</code>가, <code>private subnet 3,4</code>에는 <code>DB 인스턴스</code>가 위치하게 된다.</p>
</li>
<li><p>(핵심) 논리적으로 분리된 두 가용 영역에 각 두 개의 서브넷들과 인스턴스를 배치함으로써 <code>HA(High Availability, 고가용성)</code>을 높일 수 있다.</p>
</li>
<li><p>여기 사용되는 <code>VPC 대역대</code>는 <code>172.16.0.0/24</code> 이다.</p>
</li>
<li><p>서브네팅은 <code>public/private</code> 모두 6개의 서브넷으로 나뉘어 있다. 즉, <code>public subnet 2개</code>, <code>private subnet 4개</code>로 구성되어 있다.</p>
</li>
<li><p>각 Subnet당 <code>27개</code>의 네트워크 ip를 할당하였다.</p>
</li>
<li><p>(중요) AWS의 subnet에서는 앞 4개, 뒤 1개의 IP는 관리 용도로 사용할 수 없다는 것을 참고하도록 한다.</p>
<ul>
<li>VPC 대역대      → <code>172.16.0.0/24</code></li>
<li>public subnet1   → <code>172.16.0.0/27</code></li>
<li>public subnet2   → <code>172.16.0.32/27</code></li>
<li>private subnet1   → <code>172.16.0.64/27</code></li>
<li>private subnet2   → <code>172.16.0.96/27</code></li>
<li>private subnet3   → <code>172.16.0.128/27</code></li>
<li>private subnet4   → <code>172.16.0.160/27</code></li>
<li>x                           → <code>172.16.0.192/27</code></li>
<li>x                           → <code>172.16.0.224/27</code></li>
<li>VPC 대역대를 8개의 서브넷으로 나누었고 이중 <code>6개</code>만 사용하는 서브넷은 27개의 네트워크 ip를 가지고 있다.</li>
</ul>
</li>
</ul>
<h3 id="123-region-리전">1.2.3 Region (리전)</h3>
<ul>
<li><p>AWS 글로벌 인프라 구성을 위한 4가지 요소 (007.png) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/af8e88fd-ce4f-488d-b329-f6a13e6ec097/image.png" /> </p>
</li>
<li><p>리전 (Region)</p>
</li>
<li><p>가용영역 (AZ, Availability Zones)</p>
</li>
<li><p>엣지 로케이션 (Edge Location)</p>
</li>
<li><p>리전 엣지 캐시 (Regional Edge Cache)</p>
<ul>
<li><p>리전을 선택할때 고려할 점</p>
<ul>
<li><ol>
<li><p><code>지연 속도, 서비스 속도(접속 속도)</code></p>
<ul>
<li><p>리전은 AWS의 서비스들이 제공되는 서버의 물리적인 국가/도시 단위의 위치을 의미한다. (008.png ~ 009.png) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/eb190817-81f0-44c6-91e0-d877e757e0b2/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fade1944-7c36-4203-8456-1a2e92e836c6/image.png" /></p>
</li>
<li><p>위의 세계지도를 보면 AWS의 리전 분포를 알 수 있는데, 이렇게 여러 개의 리전을 각 지역마다 두는 이유는 네트워크 속도가 가장 큰 이유이다.</p>
</li>
</ul>
</li>
</ol>
<ul>
<li>우리나라 서버에 있는 서비스를 미국에서 접속하면 아무래도 속도가 느려질 수 밖에 없는데, 미국쪽 리전에 서버를 생성하여 서비스하면 이 문제를 해결 할 수 있다.</li>
<li>참고로, 어떤 리전에서는 사용할 수 있고, 다른 리전에서는 사용할 수 없는 서비스들이 있음</li>
</ul>
</li>
<li><ol start="2">
<li><p><code>각종 재해에 대한 대비</code></p>
<ul>
<li>미국 본사에 재해가 발생해 문제가 생겨도 각 세계에 뿌린 리전이 대신 서비스를 유지해줄 수 있다.</li>
</ul>
</li>
</ol>
</li>
<li><ol start="3">
<li><p><code>데이터 지역성 보장과 같은 법률 규제를 준수</code></p>
<ul>
<li>애플리케이션에서 카드 거래 내역 등의 데이터를 국외에 있는 서버로 반출하지 못하는 법률이 존재하는 경우, 국내 리전(서울 Region)의 클라우드 서비스를 이용하도록 해 규제를 준수하도록 하기 위함이다.</li>
<li>우리나라에서 서비스하는 데이터는 우리나라 서버에서만 저장해야 한다는 법률 등을 말한다.</li>
</ul>
</li>
</ol>
</li>
<li><p>리전별 속도 비교</p>
<ul>
<li><p><strong><u><a href="https://www.cloudping.info/">https://www.cloudping.info/</a></u></strong> 에 접속한 후 상단에 있는 <code>HTTP Ping</code>를 클릭하면 <code>한국을 기준</code>으로 한 각 리전별 서비스 속도를 알 수 있다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/57775fe7-574d-4d3b-a866-4a29d602cbcb/image.png" /></p>
</li>
<li><p>위 사이트를 보면  <code>ap-northeast-2 (Seoul)</code>이 가장 빠르다는 것을 알 수 있다. </p>
</li>
<li><p>따라서 리전을 선택할때 가장 우선적으로 <code>Latency(지연속도)</code>가 작은 곳을 우선적으로 고른다.</p>
</li>
<li><p>다만, 같은 AWS 서비스를 이용하더라도, <code>리전마다 가격이 다를 수 있다</code>는 점은 유의해야 한다. 이는 <code>각 국가의 경제적 특징</code>을 기준으로 한다는 점을 고려하기 때문이다.</p>
<ul>
<li>상파울로 (제일 비싸다 / 브라질의 도시 / 개발 도상국 / 전력 수급사정이 좋지 않다)</li>
<li>버지니아 (제일 싸다 / 제일 많이 사용 / 수익이 나기 때문에 저렴 / 일단 전반적으로 미국지역이 싼 편이다)</li>
</ul>
</li>
<li><p>결론</p>
<ul>
<li>리전마다 사용 가능한 서비스가 제한 될 수 있으니 <code>리전을 선택할때 고려할 점 3가지</code>를 모두 고려하여 리전을 설정해야 한다.</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="124-az-availability-zone-가용-영역">1.2.4 AZ (Availability Zone, 가용 영역)</h3>
<ul>
<li><p>각 리전별 2개 이상의 가용 영역을 가지고 있다 (010.png) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f41bd678-8d48-4883-9b59-d2b9a4885408/image.png" /></p>
<ul>
<li><code>리전</code>이 <code>국가/도시 단위의 지리적 위치</code>라면, <code>가용영역(AZ)</code>은 <code>각 리전(국가/도시) 안의 데이터센터</code>를 말한다. 즉, aws 서버 컴퓨터들이 모여있는 건물이라고 이해하면 된다.</li>
<li>기본적으로 AWS의 각 리전 안에는 <code>2개 이상의 가용 영역</code>을 가지고 있다.</li>
<li>위 사진에서 볼 수 있듯이 서울은 2개의 가용영역(AZ)이 있고 도쿄는 4개, 런던은 3개가 있는 것을 알 수 있다.</li>
</ul>
</li>
<li><p>가용 영역은 일정한 거리로 떨어져 있다 (011.png) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/91e99f2b-151b-42e1-b4e9-4b15a8986ad2/image.png" /></p>
<ul>
<li><p>각 리전의 AZ 건물들은 위 사진처럼 물리적으로 일정 거리(몇 KM 이상) 떨어져 있다.</p>
</li>
<li><p>앞서 설명한 리전과 같이 하나의 가용 영역이 각종 재해, 정전, 화재 등 다양한 이유로 작동불능이 되더라도 다른 가용 영역에서 서비스를 재개하여 유지할 수 있기 때문이다.</p>
</li>
<li><p>다만 모든 AZ는 서로 <code>100km 이내</code>의 거리에 위치해 있어야 한다. 그 이유는 각 데이터센터는 광통신 전용망(고속 프라이빗 네트워크)로 연결되어 있는데 서로 너무 멀리 떨어져 있으면 속도가 떨어질 수 있기 때문이다.</p>
</li>
<li><p>이렇게 데이터센터를 여러 개로 나누면 보안적인 측면에서도 이점으로 작용하는 특징도 있다.</p>
</li>
<li><p>AZ의 특징 중 하나가 각 계정 별로 부여된 AZ의 코드와 실제 위치가 다르다는 점이다.</p>
<ul>
<li>예를 들면 서울 리전에 강남 AZ, 용산 AZ, 송파 AZ가 있다고 가정하자.</li>
<li>각기 다른 <code>user A</code>와 <code>user B</code> 두 사용자가 서울 리전에 서비스를 구축하였다.</li>
<li>aws에서 각 계정들에게 가용영역(AZ)를 첫 번째는 강남, 두 번째는 용산, 세 번째는 송파 이렇게 바로 고정적으로 배치해 주는 것이 아니라 <code>AZ-A</code>, <code>AZ-B</code>, <code>AZ-C</code> 이런 식으로 가용영역을 매핑해서 중간 단계로 배치해 주는데, 이는 보안이나 한 AZ로 트래픽 몰림을 방지하기 위함이다.</li>
</ul>
</li>
</ul>
</li>
<li><p>보안과 트래픽 분산 (012.png) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a1f63844-2e93-430f-9ac9-63b3e4446aa3/image.png" /></p>
<ul>
<li>사진에서 보면 <code>user A</code>의 <code>AZ-A</code>는 <code>Data Center 2</code>에 연결되어 있고 <code>user B</code>의 <code>AZ-A</code>는 <code>Data Center 1</code>에 연결되어 있다.</li>
<li>이렇게 각 계정마다 가용영역을 랜덤으로 매핑함으로서 <code>user A</code>와 <code>user B</code>간의 저장소를 랜덤으로 배치하게 하여, <code>user A</code>가 민감한 데이터를 저장해도 어떤 데이터 센터에 저장되는지 추측할 수 없게 되어 보안적인 효과를 얻을 수 있다. 즉, 나의 계정의 가용영역 A는 다른 계정의 가용영역 A와 데이터센터 저장 위치가 다르다고 이해하면 된다.</li>
<li>또한 각 계정의 유저들이 데이터를 저장할 때, 하나의 데이터 센터에만 저장을 하지 않게 하고, 각 센터에 이리저리 분산함으로서 트래픽 몰림을 방지할 수 있다. (사진처럼 각 계정마다 데이터센터 연결선이 다르니까)</li>
<li>따라서 여러 개의 가용영역에 서버를 올려 사용하여 로드 밸런싱을 통하여 트래픽을 분산시켜 한쪽 가용영역이 작동을 안 하더라도 무중단 서비스를 제공할 수 있는 것이다.</li>
<li>결론적으로 각 계정의 개인적인 데이터를 보호할 수 있는 <code>보안 효과</code>를 얻을 수 있고, <code>트래픽을 분산</code>하는 일석이조의 효과가 있는 셈이다.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="125-edge-location">1.2.5 Edge Location</h3>
<ul>
<li><p>개요</p>
<ul>
<li><code>Edge (가장자리, 모서리, 만나는 지점)</code> + <code>Location (위치)</code>를 먼저 생각하고 아래 내용을 이해하면 된다.</li>
<li>aws의 CDN들의 여러 서비스들을 가장 빠른 속도로 제공(캐싱)하기 위한 거점을 말하는데 전 세계 여러 장소에 흩어져 있다.</li>
<li>보다 정확히 말하자면 리전과 가용영역과 별개로 AWS의 CDN 서비스인 <code>CloudFront</code>와 AWS의 DNS 서비스인 <code>Route53</code>의 캐시 서버를 의미한다.</li>
</ul>
</li>
<li><p><code>CDN</code> (Contents Delivery Network)</p>
<ul>
<li><p><code>CloudFront</code>란 AWS에서 제공하는 CDN 서비스를 의미한다.</p>
</li>
<li><p>CDN 서비스는 콘텐츠를 보다 빠르게 전송하는 기술로, 속도 개선과 회선 비용 절감에 용이하다.</p>
</li>
<li><p>최초 요청 시에는 서버로부터 콘텐츠를 가져와 고객에게 전송하며, 동시에 CDN 캐싱 장비에 저장한다.</p>
</li>
<li><p>이후에는 CDN 캐싱 장비에 저장된 콘텐츠를 바로 전송하는 방식이다.</p>
</li>
<li><p>CDN 업체에서 지정하는 콘텐츠 만료 지점까지 호출이 없으면 주기적으로 삭제한다.</p>
</li>
<li><p>CloudFront는 EC2나 S3 같은 서비스에서 사용할 경우, 가장 가까운 엣지로 라우팅되어 콘텐츠 전송 속도를 향상할 수 있다. 이를 통해 데이터, 동영상, 애플리케이션 및 API까지 전송 가능하다.</p>
</li>
<li><p>Static 캐싱</p>
<ul>
<li>운영자가 콘텐츠를 미리 캐시 서버에 복사해서 요청 시 무조건 캐시 서버 이용 가능</li>
</ul>
</li>
<li><p>Dynamic 캐싱</p>
<ul>
<li>운영자가 미리 복사하지 않아 콘텐츠가 없을 때 Origin 서버로부터 다운받아 전달하는 방식</li>
</ul>
</li>
</ul>
</li>
<li><p>실제 적용 사례</p>
<ul>
<li>한 번쯤은 제이쿼리 같은 라이브러리를 사용하기 위해 cdn 링크를 html에 삽입해본 경험이 있을 것이다.</li>
<li>당연히 소스를 빠르게 다운받아 이용하기 위해 속도가 중요하다는 것쯤은 알고 있을 것이다.</li>
<li>즉, 이와 같이 CDN과 DNS 같은 서비스들의 서버들은 리전과 별개로 여러 개의 엣지 로케이션에 적용되어 서비스되고 있기 때문에 저 멀리 미국 영화나 드라마를 지연 없이 바로바로 다운받아 볼 수 있는 것이다.</li>
</ul>
</li>
<li><p>엣지 로케이션 미 사용 (014.png) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/90872f4b-da88-436e-8b78-cfcf2f15a839/image.png" /></p>
<ul>
<li>우리나라의 대표적인 스트리밍 서비스는 아프리카 TV가 있다.</li>
<li>만일 미국과 남아프리카, 호주에서 우리나라 서비스 아프리카TV의 방송이나 영상을 보고 싶다면, 당연히 아프리카TV 본사가 위치하고 있는 한반도 리전에 접속해서 다운로드 해야 한다.</li>
<li>사진에서 볼수 있듯이 길게 설명안해도 속도가 엄청나게 느릴것 같아 보인다. 거기다 오늘 보고 끄고, 내일 또 방송을 보고싶을때 그 멀리까지 다시 연결해 다운받아야 할 것이다.</li>
<li>이러한 단점을 극복하기위해 엣지 로케이션 이라는 개념과 시설을 사용 하는 것이다.</li>
</ul>
</li>
<li><p>엣지로케이션 사용 (015.png ~ 016.png) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c0feecf2-4813-4069-9324-42783be7e822/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/881fbc9b-8d63-4654-9fd2-c3176b003e3c/image.png" /></p>
<ul>
<li>각 거점마다 가깝고 적당한 곳에 엣지 로케이션(임시 데이터 저장소 센터)을 배치한다. 하늘색 바둑알이 엣지 로케이션이다.</li>
<li>그러면 각 대륙의 사람들(검은색 바둑알)은 가까이 위치한 지역내의 엣지 로케이션에 접속해 스트리밍 서비스를 이용할 수 있게 된다.</li>
<li>당연히 훨씬 속도 면에서 유리하고, 또한 일정 기간 동안 요청한 데이터를 저장하는 기능(캐시, 콘텐츠 복사)도 갖춰 있어서 오늘 보고 내일 또 보고싶을때 저 멀리 까지 재연결 하는 일 없이 바로바로 볼 수 있는 장점도 있다.</li>
<li>결론적으로 엣지 로케이션이라함은 CDN 서비스와 사용자가 만나는 곳을 Edge라고 하며, 그 Edge가 어느 지역에 위치한 시설을 일컫는다.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="13-실습">1.3 실습</h2>
<h3 id="실습-1">실습 1.</h3>
<ul>
<li>019.png <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/64cd7903-0335-4c2a-9fed-f7ccdaef6575/image.png" /></li>
</ul>
<h3 id="작업순서">작업순서</h3>
<ul>
<li><p>Step 1. <code>VPC</code> 생성 및 설정</p>
<ul>
<li><p><code>VPC</code> 상태 확인</p>
<ul>
<li>기본 VPC가 1개 있다.
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d417435e-3e37-44e9-9b7a-601336760745/image.png" /></li>
</ul>
</li>
<li><p>생성할 VPC의 이름과 IPv4 CIDR 설정</p>
<ul>
<li><code>Region</code>을 <code>아시아 태평양(서울)</code>인 <code>ap-northeast-2</code>로 변경한다.</li>
<li>루트 유저가 아닌 사용자(<code>user1</code>)에서 작업을 해야 한다.
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d4fb8eac-be14-4dcc-8948-dd5fb48160c7/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c82db9ab-fd18-48d7-86b7-936cebf432c0/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b7478d3e-d90c-4787-9264-c1fc4d44828e/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li><p>Step 2. <code>Public Subnet</code> 및 <code>Private Subnet</code> 생성 및 설정</p>
<ul>
<li><p><code>VPC 대시보드</code>의 하단에 있는 <code>서브넷</code>을 클릭하면 우측에 기본값으로 생성되어 있는 것을 확인할 수 있다. (024.png)
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f985c7e5-335b-43ec-96e5-45e63d5107d6/image.png" /></p>
</li>
<li><p>우측에 있는 <code>서브넷 생성</code> 클릭</p>
<ul>
<li><code>myVPC</code> 선택
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3f4b5e60-89ee-4418-a01b-36e8318d7065/image.png" /></li>
</ul>
</li>
<li><p><code>public-subnet</code> 생성
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4e2c9a12-a4e9-4ee5-8495-9ad53455de17/image.png" /></p>
</li>
<li><p><code>private-subnet</code> 생성
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/67ce6628-07f6-47ee-9258-bc8258690481/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d8552f43-0e66-4832-9bd6-a781e5de3fb8/image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li><p>Step 3. <code>Internet Gateway</code> 생성 및 <code>VPC</code>와의 연결</p>
<ul>
<li><p><code>VPC 대시보드</code> 하단의 <code>인터넷 게이트웨이</code>를 클릭하면 우측에 <strong>기본값으로 1개 생성되어 있는 것</strong>을 확인할 수 있다.</p>
</li>
<li><p><code>NAT 게이트웨이</code>는 <strong>비용이 추가</strong>되므로 여기서는 알고만 넘어간다.</p>
</li>
<li><p>우측의 <code>인터넷 게이트웨이 생성</code> 클릭
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a06e1d4b-205f-4bb7-8c2e-b11166f3dd7e/image.png" /></p>
</li>
<li><p><code>이름 태그</code>에 <code>myIGW</code> 입력 후 <code>인터넷 게이트웨이 생성</code> 클릭
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8536a9ce-9a3b-48e6-a70f-aef672a38f54/image.png" /></p>
</li>
<li><p>생성 직후 우측 상단의 <code>VPC에 연결</code> 클릭
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7b64b5a1-afeb-4948-86a2-fe872181eb6e/image.png" /></p>
</li>
<li><p><code>사용 가능한 VPC</code> 항목에서 <code>vpc-0a4e63f46901119aa (myVPC)</code> 선택 → <code>인터넷 게이트웨이 연결</code> 클릭
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/36c5b01a-6f50-4546-b435-c718aefd4295/image.png" /></p>
</li>
<li><p>IGW가 정상적으로 생성되고 VPC에 연결된 상태 확인
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/be33b604-fe2d-482a-bf77-a3426dbbe52b/image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li><p>Step 4. 라우팅 테이블 생성과 서브넷 연결</p>
<ul>
<li><p>서브넷을 생성하고 라우팅 테이블을 따로 설정하지 않았기 때문에 서브넷은 모두 기본 라우팅 테이블에 연결이 되어 있다. (명시적 연결이 없는 서브넷으로 분류됨)</p>
<ul>
<li>서비스 유형이 변경될 수 있으므로 기본적으로 연결되어 있지 않을 가능성도 있다.</li>
</ul>
</li>
<li><p><code>VPC 대시보드</code> 하단의 <code>라우팅 테이블</code>을 클릭하면 기본 라우팅 테이블이 1개 생성되어 있는 것을 확인할 수 있다.</p>
<ul>
<li>하지만 앞에서 생성한 서브넷에 맞는 라우팅 테이블을 <strong>각각 별도로 생성</strong>해야 한다.</li>
</ul>
</li>
<li><p>우측 상단의 <code>라우팅 테이블 생성</code> 클릭</p>
<ul>
<li>이름: <code>public-rtb</code></li>
<li>VPC: <code>vpc-0a4e63f46901119aa (myVPC)</code></li>
<li>하단의 <code>라우팅 테이블 생성</code> 클릭
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/273eab9e-9c04-4753-9c89-fc8777deec22/image.png" /></li>
</ul>
</li>
<li><p>같은 방식으로 <code>private-rtb</code> 생성
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/050c5a98-d5d6-43c3-9348-00759028d623/image.png" /></p>
</li>
<li><p>라우팅 테이블 목록을 확인한다.</p>
</li>
<li><p>이제 <code>public-rtb</code>에 <code>public-subnet</code>을 연결한다.</p>
<ul>
<li><code>public-rtb</code> 선택 → 하단 <code>서브넷 연결</code> 탭</li>
<li>우측 하단 <code>서브넷 연결 편집</code> 클릭
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a764b343-b577-43a0-8ff9-96907cf74e96/image.png" /></li>
<li><code>public-subnet</code> 체크 후 <code>연결 저장</code>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5644e3c3-4e12-489f-a888-f0180aa0f77f/image.png" /></li>
<li><code>명시적 서브넷 연결</code> 영역에 내용이 추가된 것을 확인
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ea421bfb-8083-4ed9-a9e7-13a6dbfa65e8/image.png" /></li>
</ul>
</li>
<li><p>같은 방법으로 <code>private-rtb</code>에 <code>private-subnet</code> 연결
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d6f68c71-a98f-4f36-bbaa-66a028fafb21/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b7134004-4d01-4ae2-9ceb-9820be9cbf5e/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a18221e8-3e05-4dd5-a499-4d19d1fd9f41/image.png" /></p>
</li>
<li><p>라우팅 테이블과 서브넷이 정상적으로 연결된 것을 확인한다.</p>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 5. 라우팅 규칙 설정<ul>
<li><code>라우팅 테이블</code>에 있는 <code>public-rtb</code>를 체크한 후 하단에 있는 <code>라우팅</code> 탭을 클릭하고 우측에 있는 '라우팅 편집'을 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4d622766-cf0d-486e-8917-e406bf5c0a96/image.png" /></li>
<li>기존에 있는 '값(10.0.0.0/16, local)'은 절대 손대지 말고 '라우팅 추가'를 클릭하면서 다음과 같이 '2개의 규칙을 추가'하도록 한다.<ul>
<li>'0.0.0.0/0'      '인터넷 게이트웨이'      'myIGW'</li>
<li>'::/0'         '인터넷 게이트웨이'      'myIGW’ <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/054e5782-ecf4-4f11-9854-71d0a76be8de/image.png" /></li>
</ul>
</li>
<li><code>private-rtb</code>는 별도로 작업할 내용이 없다. 그냥 확인만 하도록 한다.</li>
<li>작업한 내용을 확인한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6cfdae25-d849-437d-9245-16f6662f5fe3/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 6. 작업 확인<ul>
<li><code>Public Subnet</code>과 <code>Private Subnet</code>은 AWS에서 리소스로 구분하는 것이 아니라</li>
<li>사용자가 설정한 라우팅 테이블에서 인터넷 게이트웨이로의 라우팅 규칙이 있는지 없는지에 따라 <code>public/private</code>으로 나뉜다는 것을 알 수 있다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/abb6e5e4-a2fc-469d-a223-1c59fa6af412/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e02c0e2e-4f58-47b8-97f5-468141fb0b80/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 7. (매우 중요)<ul>
<li>모든 작업이 완료되면 <code>사용자(user1)</code>와 <code>VPN</code> 모두 제거하도록 한다.</li>
<li><code>VRC</code> 제거<ul>
<li>Step 1. <code>VPC</code>에 연결된 ‘인터넷 게이트웨이’ 연결 분리 후 삭제 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6b63586d-0313-4528-bca0-0c6b49bcf10e/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/521c96ef-9a1b-4aea-8eb1-ac7b99cc7d24/image.png" /></li>
<li>Step 2. <code>서브넷</code>을 삭제한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c648b354-6bfa-4ec0-af68-731808f57efd/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/18041d94-17df-4600-bc83-733b1ed998ef/image.png" /></li>
<li>Step 3. <code>라우팅 테이블</code>을 삭제한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8abb46f0-b930-4f3a-8d83-285ead98e6a1/image.png" /></li>
<li>Step 4. <code>VPC</code>를 삭제한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6e27bcca-fb04-4738-9619-16f3282fabca/image.png" /><ul>
<li><code>사용자(user1)</code> 제거</li>
</ul>
</li>
</ul>
</li>
<li>Step 1. 사용자는 로그아웃하고 관리자로 로그인한다.</li>
<li>Step 2. <code>IAM</code> 서비스로 들어간다.</li>
<li>Step 3. <code>IAM 대시보드</code> 내용을 확인한다.</li>
<li>Step 4. 좌측의 <code>액세스 관리</code> 하단에 있는 <code>사용자</code>를 클릭한다.</li>
<li>Step 5. <code>사용자</code>를 체크한 후 <code>작업</code>에서 우측 상단에 있는 <code>삭제</code>를 클릭한다.<br /><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ecd674b7-8c5b-4837-892a-033b11411f8a/image.png" /></li>
<li>Step 6. 이 때 사용자 생성 시 <code>액세스 키</code>를 함께 만들었기 때문에 삭제가 불가하다고 나오는데 중간에 <code>액세스 키 비활성화</code>를 클릭하면 된다.<br /><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bed1f0b9-670c-4ec1-9fd0-e592977b40eb/image.png" /></li>
<li>Step 7. <code>액세스 키</code>가 <code>비활성화</code>되면 사용자를 삭제할 수가 있는데 하단에 <code>confirm</code>을 입력한 후 <code>사용자 삭제</code>를 클릭한다.<br /><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5d597584-7644-425a-a7bd-dd9970f63e71/image.png" /></li>
<li>Step 8. 왼쪽의 <code>액세스 관리</code> 하단에 있는 <code>사용자 그룹</code>을 클릭한다.</li>
<li>Step 9. <code>clouddxusergroup</code>을 체크한 후 우측 상단에 있는 <code>삭제</code>를 클릭한다.</li>
<li>Step 10. <code>clouddxusergroup</code>을 입력한 후 삭제하면 된다.<br /><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7375c841-547b-48f1-aae0-99dbbbfc85d4/image.png" /></li>
<li>Step 11. 왼쪽의 <code>액세스 관리</code> 하단에 있는 <code>정책</code>을 클릭한다.</li>
<li>Step 12. <code>clouddxaccess</code>를 체크한 후 우측 상단에 있는 <code>삭제</code>를 클릭한다.</li>
<li>Step 13. <code>clouddxaccess</code>를 입력한 후 삭제를 클릭한다.<br /><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/047e97fb-0122-4caa-b5b4-84d360d435e7/image.png" /></li>
<li>Step 14. <code>IAM 대시보드</code> 내용에 있는 <code>IAM 리소스</code> 내용을 확인한다.</li>
<li><code>역할</code>을 제외하고 모든 항목에 있는 값들이 <code>0</code>인 것을 확인한다.<br /><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d4537163-cee4-458a-a2fe-638abeb12f59/image.png" /></li>
</ul>
</li>
</ul>