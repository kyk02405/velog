<hr />
<h1 id="스푸핑">스푸핑</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f3a2b1df-1c8a-4b39-ab39-6452f34c1c3b/image.png" /></p>
<ul>
<li>스푸핑(Spoofing)<ul>
<li>원래 의미 : 다른 사람을 흉내 내는 것 혹은 따라하는 짓궂은 장난<ul>
<li>공격자는 마치 자신이 수신자인 것처럼 행세하여 송신자가 보낸 메시지를 강탈(수신자 역할)</li>
<li>공격자가 마치 공격 대상자인 것처럼 행세하는 것(송신자 역할)</li>
</ul>
</li>
</ul>
</li>
<li>스니핑 vs 스푸핑<ul>
<li>송·수신자 간의 메시지 전달 여부에 차이가 있음<ul>
<li>스니핑 : 수동적 공격</li>
<li>스푸핑 : 능동적 공격</li>
</ul>
</li>
<li>스니핑은 송·수신자 간의 메시지 전달 잘 됨(엿듣기)</li>
<li>스푸핑은 공격 대상자(송신자 or 수신자)인 것처럼
행세하므로 메시지 전달이 불완전</li>
</ul>
</li>
</ul>
<hr />
<h1 id="스푸핑-1">스푸핑</h1>
<ul>
<li>다양한 스푸핑 기법의 종류들<ul>
<li>2계층 공격 : 공격자가 같은 스위치 내에 존재</li>
<li>3계층 or 7계층 공격 : 공격자가 내부 네트워크 및 외부 네트워크에서도 공격 가능</li>
<li>네트워크 환경의 예</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cedc5e0c-c047-48b3-9861-17cd22a2f787/image.png" /></p>
<hr />
<h1 id="arp의-개념">ARP의 개념</h1>
<ul>
<li>ARP(Address Resolution Protocol)<ul>
<li>MAC 주소를 결정(Resolution)하기 위한 통신 프로토콜</li>
<li>IP주소를 MAC 주소(하드웨어 주소)로 변환하는 역할<ul>
<li>하드웨어 주소 : 네트워크 카드별로 부여되는 고유한 번호</li>
</ul>
</li>
</ul>
</li>
<li>공격자가 공격 대상자의 MAC 주소를 가로채는 공격<ul>
<li>IP 주소(3계층)로 보내더라도 내부적으로는 MAC주소(2계층)로 변환되어 전송됨</li>
</ul>
</li>
</ul>
<hr />
<h1 id="arp의-개념-1">ARP의 개념</h1>
<ul>
<li>ARP의 동작 원리(같은 로컬 네트워크에 단말이 있는 경우)<ul>
<li>ARP 요청의 예: IP 주소 IPB에 대한 MAC 주소가 없는 경우
(1) 단말 A : 단말 B의 MAC 주소를 모르기 때문에 스위치로 ARP 요청(ARP Request)을 보냄
(2) 스위치 : ARP 요청을 전달받게 되면, 자신에게 접속된 모든 단말에게 ARP 요청을 브로드캐스트(Broadcast)
방식으로 전송
(3) 단말 B : ARP 요청을 전달받은 단말 중에서 실제 요청한 IP 주소를 가진 단말이 있다면 이 단말은 ARP
응답(ARP Reply)을 보냄
(4) 단말 A : ARP 응답을 전달 받아 자신의 ARP 테이블에 B의 MAC 주소를 추가</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/96cda106-d101-4068-bf87-2bf159129eed/image.png" /></p>
<hr />
<h1 id="arp의-개념-2">ARP의 개념</h1>
<p>• ARP의 동작 원리(같은 로컬 네트워크에 단말이 있는 경우)
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7811868e-99f4-4813-9150-9ab9e41970bc/image.png" /></p>
<hr />
<h1 id="arp의-개념-3">ARP의 개념</h1>
<ul>
<li>ARP의 동작 원리(외부 네트워크에 단말이 있는 경우)<ul>
<li>외부의 네트워크에 있기 때문에 외부 네트워크의 통로가 되는 게이트웨이(Gateway)의 MAC 주소가
해당 IP의 MAC 주소로 설정</li>
<li>ARP 응답의 예 : 외부 망에 있는 단말 C에 대한 MAC 주소 추가</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/88db6c32-3eea-4484-b4ba-c88167f66184/image.png" /></p>
<hr />
<h1 id="arp-스푸핑">ARP 스푸핑</h1>
<ul>
<li>핵심<ul>
<li>공격자가 스위치 내의 다른 단말에 가짜 ARP 응답을 보내는 것</li>
<li>(ARP 요청이 오지 않았는데도 불구하고) ARP 응답을 스위치 내의 다른 단말에 지속적으로 보냄
→ 가짜 MAC 주소를 자신의 ARP 테이블에 반영</li>
</ul>
</li>
</ul>
<hr />
<h1 id="arp-스푸핑-1">ARP 스푸핑</h1>
<ul>
<li>Step-1: B의 MAC 주소를 가짜 MAC 주소로 변경<ul>
<li>공격자 I: 스위치에 연결된 다른 단말 A에 ARP 응답을 보냄<ul>
<li>가짜 ARP 응답에 의해 A의 ARP 테이블에 B의 MAC 주소가 MACI로 변경</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/797c2f6e-90b5-41e1-b851-7ba4454bdd69/image.png" /></p>
<hr />
<h1 id="arp-스푸핑-2">ARP 스푸핑</h1>
<ul>
<li>Step-2: B로 가야 하는 메시지가 공격자 I에게 전송됨<ul>
<li>A가 B에게 네트워크로 메시지 전송</li>
<li>A는 B의 IP 주소인 IPB로 메시지 전송</li>
<li>IPB에 해당하는 MAC 주소는 MACI로 변경</li>
<li>실제로는 공격자 I에게 메시지가 전달됨</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a84eb412-599a-4d96-8e67-ae84b57573b1/image.png" /></p>
<hr />
<h1 id="arp-스푸핑-3">ARP 스푸핑</h1>
<ul>
<li>ARP 스푸핑을 이용한 스니핑 공격<ul>
<li>Step-1: 스위치 내의 모든 단말의 MAC 주소를 공격자의 MAC 주소로 변경</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5d16e46e-e23e-4dbf-bfc3-5c236fc3e091/image.png" /></p>
<hr />
<h1 id="arp-스푸핑-4">ARP 스푸핑</h1>
<ul>
<li>ARP 스푸핑을 이용한 스니핑 공격<ul>
<li>Step-2: 공격자에게로 전달된 메시지를 원래의 수신자에게 재전송함</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3c6ba6b2-7d7c-48cf-8836-89995cab8a61/image.png" /></p>
<hr />
<h1 id="arp-스푸핑-5">ARP 스푸핑</h1>
<ul>
<li>ARP 스푸핑의 현상과 탐지<ul>
<li>(1) 지속적인 ARP 응답 발생<ul>
<li>ARP 스푸핑을 성공하고자 ARP 응답 혹은 ARP 요청을 주기적으로 보냄</li>
<li>와이어샤크(Wireshark) 같은 패킷 분석 프로그램을 이용하여 확인</li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li>예) ARP 응답으로 IP 주소 192.168.2.1에 해당하는 기존 MAC 주소 70:f3:95:8f:92:3a와 다른 새로운 MAC 주소
00:0e:2e:60:b7:22가 전달</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/05f43b8a-26f5-460a-baa3-18030ac746c1/image.png" /></p>
<hr />
<h1 id="arp-스푸핑-6">ARP 스푸핑</h1>
<ul>
<li>ARP 스푸핑의 현상과 탐지<ul>
<li>(2) ARP 테이블에서 중복된 MAC 주소 확인<ul>
<li>명령어 실행: arp –a</li>
<li>예) IP 주소(172.30.1.1)와 다른 IP 주소들(172.30.78.188, 172.30.78.38)<ul>
<li>같은 MAC 주소인 b8-03-05-6c-a0-bb 사용</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a91cdfc3-cec8-4ef8-b479-c20fd818bf1b/image.png" /></p>
<hr />
<h1 id="arp-스푸핑-7">ARP 스푸핑</h1>
<ul>
<li><p>ARP 스푸핑의 현상과 탐지</p>
<ul>
<li>(3) ARP 테이블 감시 프로그램 활용<ul>
<li>ARP 테이블을 직접확인 어려움 → 도구 이용(xarp, arpwatch 등)</li>
<li>xarp의 실행 예</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fabcd6e3-3de8-4904-9e49-acb8b3f2d284/image.png" /></p>
<ul>
<li>(4) 네트워크 속도 저하<ul>
<li>송신자가 보낸 메시지가 공격자를 한번 거쳐 재전송</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="arp-스푸핑-8">ARP 스푸핑</h1>
<ul>
<li><p>ARP 스푸핑 방지 대책</p>
<ul>
<li><p>a. 정적인 ARP 테이블 관리</p>
<ul>
<li><p>공격자가 보낸 arp 응답에 대해 MAC 주소가  변하지 않도록 정적 주소 설정</p>
</li>
<li><p>현실적 어려움 : 관리 비용 증가</p>
</li>
<li><p>단말의 추가나 변경이 발생할 때 게이트웨이의 ARP 테이블을 수정해야 됨</p>
</li>
<li><p>웹 서버와 같이 중요 단말만을 묶어서 별도의 서브 네트워크 (Sub-network)를 구성하고, 이들에 대해서만 정적인 ARP 테이블을 관리</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c4148d0a-fb19-4e52-98ce-6bcc4f8355ad/image.png" /></p>
<ul>
<li><p>B. PC와 서버의 보안 수준 강화</p>
<ul>
<li>보안 취약점이 있는 PC 혹은 서버로부터 공격이 시작되므로, 정기적인 보안 업데이트 및 최신화</li>
</ul>
</li>
</ul>
<hr />
<h1 id="ip-스푸핑">IP 스푸핑</h1>
<ul>
<li>IP 스푸핑(IP Address Spoofing)<ul>
<li>공격자의 IP 주소를 다른 IP 주소로 속이는 공격 방법</li>
<li>자신이 보내는 메시지 안의 IP 주소를 변조</li>
<li>IP 헤더 정보에 저장된 출발 IP 주소(Source IP Address) 변조</li>
</ul>
</li>
</ul>
<p> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9af5ce30-68ab-4071-957c-4e4252fb1a70/image.png" /></p>
<hr />
<h1 id="ip-스푸핑-1">IP 스푸핑</h1>
<ul>
<li><p>IP 스푸핑을 이용한 보안 공격</p>
<ul>
<li><p>IP 스푸핑 자체가 위협적일 수 있는 상황</p>
<ul>
<li><p>IP 주소가 인증(Authentication)의 수단이 될 때 예) A 서버와 B 서버가 IP 주소 기반의 트러스트(Trust) 관계</p>
</li>
<li><p>B는 IP 주소가 IPA인 모든 요청에 대해서 인증 절차 없이 허용 → 출발 IP가 신뢰하는 서버인 A의 주소 IPA</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ef6fad1b-4955-4355-91ce-2e17efc6ab01/image.png" /></p>
<hr />
<h1 id="ip-스푸핑-2">IP 스푸핑</h1>
<ul>
<li>IP 스푸핑을 이용한 보안 공격<ul>
<li>공격자는 먼저 B와 트러스트 관계인 서버 A를 공격<ul>
<li>서비스 거부 공격(DoS: Denial of Service) 등으로 공격<ul>
<li>서버 A를 동작 불능 상태로 만듦</li>
</ul>
</li>
</ul>
</li>
<li>출발 IP 주소를 IPA로 변조한 메시지를 서버 B로 보냄<ul>
<li>서버 B는 출발 IP가 IPA인 공격자의 메시지를 인증 절차 없이 허용함</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cee64c37-cf99-49aa-8709-a3ac95a7bb29/image.png" /></p>
<hr />
<h1 id="ip-스푸핑-3">IP 스푸핑</h1>
<ul>
<li>IP 스푸핑의 방지 방법<ul>
<li>IP 주소 기반의 트러스트 관계를 맺지 않음<ul>
<li>서버 클러스터링(Clustering)이 꼭 필요한 경우 : 트러스트 관계에 있는 서버들의 보안 수준 강화</li>
<li>정기적인 보안 업데이트 &amp; 보안 취약점 분석 &amp; 모니터링</li>
</ul>
</li>
<li>패킷 필터링(Packet Filtering)<ul>
<li>게이트웨이 밖에서 시도되는 IP 스푸핑 공격에 대한 방지 수단</li>
<li>게이트웨이 : 외부에서 내부 네트워크로 전달되는 메시지가 거쳐 가는 중간 관문</li>
<li>외부에서 내부로 전달되는 메시지 중에서 출발 IP가 내부 IP로 설정된 메시지를 필터링 (차단)</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ef59547a-4156-4da6-992e-ce9a5e31d8fb/image.png" /></p>
<hr />
<h1 id="웹-성능-프로그램">웹 성능 프로그램</h1>
<ul>
<li>IP 스푸핑의 합법적인 사용: 웹 성능 테스트 프로그램<ul>
<li>웹 사이트 성능 테스트 프로그램<ul>
<li>내부적으로 IP 변조 기능 사용</li>
<li>대량의 가상 사용자를 생성하여 마치 이들이 실제 사용자인 것처럼 시뮬레이션</li>
<li>가상 사용자별로 서로 다른 IP 주소를 할당</li>
<li>동시에 여러 사용자가 웹 사이트를 정상적으로 이용하는 것을 확인</li>
<li>예) HP LoadRunner, Apache JMeter 등</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bee8cad0-444a-46d7-b3c7-ca4ba379037a/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/61d28f5e-3c7e-4e9d-97f8-8476c3ce62d0/image.png" /></p>
<hr />
<h1 id="icmp">ICMP</h1>
<ul>
<li>ICMP(The Internet Control Message Protocol)<ul>
<li>네트워크 상에 현재 오류가 없는지 진단하거나 제어하는 목적으로 사용되는 프로토콜</li>
<li>IP 프로토콜의 약점 보완 목적으로 사용</li>
</ul>
</li>
<li>ICMP의 사용 목적 1: 네트워크 진단<ul>
<li>네트워크 연결 여부 확인: ping 또는 traceroute</li>
<li>네트워크가 끊어져 있다면 응답을 받을 수 없고, 이것을 통해 네트워크 연결이 정상인지 판단</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e318599e-9217-40cf-88ec-71d0f3b38035/image.png" /></p>
<hr />
<h1 id="icmp-1">ICMP</h1>
<ul>
<li>ICMP의 사용 목적 2: 네트워크 흐름 통제<ul>
<li>게이트웨이가 2개인 네트워크 환경에서 게이트웨이의 IP 메시지 재전송<ul>
<li>게이트웨이 1이 default gateway 역할을 할 경우, A가 C로 메시지 전송할 경우 게이트웨이 1로 전송</li>
<li>IP를 확인하고 내부망에 해당되면, 게이트웨이2로 재전송</li>
<li>ICMP는 네트워크 흐름 통제를 위해 다음부터 게이트웨이 2로 보내라는 의미로 ICMP 리다이렉트 메시지 보냄</li>
</ul>
</li>
<li>그 밖에 부하조절의 목적으로 활용<ul>
<li>특정 게이트웨이로 트래픽이 몰릴 경우, ICMP 리다이렉트 메시지를 이용해 다른 여러 게이트웨이로 분산 가능</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/226539be-d1e4-4143-8bcc-91913de2b033/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/72f143bd-247c-44a2-b8db-b3bd92abb04f/image.png" /></p>
<hr />
<h1 id="icmp-스푸핑">ICMP 스푸핑</h1>
<ul>
<li><p>Step-1: ICMP 리다이렉트 보내기 재전송</p>
<ul>
<li>공격자가 게이트웨이인 것처럼 속여 A가
메시지 전송하도록 함
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6144c102-d719-4e85-b802-e93f6c244dd6/image.png" /></li>
</ul>
</li>
<li><p>Step-2: 단말 A에서 보낸 메시지는 먼저
공격자 I에게로 전송됨
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1bf8f614-0cef-42aa-a5a4-fd5b86568400/image.png" /></p>
</li>
<li><p>Step-3: 스니핑 성공을 위해 기존 게이트웨이로 재전송</p>
<ul>
<li>아무 일도 없는 것처럼 하기 위해 공격자는 원래 게이트웨이를 통해 메시지를 전송<ul>
<li>A와 게이트웨이 사이에서 공격자가 위치</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/711f6f3f-7cde-49ab-92eb-ae28b654de13/image.png" /></p>
<ul>
<li>주의할 점<ul>
<li>ICMP는 3계층 공격이므로 스위치 외부 뿐만 아니라 게이트웨이 바깥에서도 공격 가능</li>
<li>최근의 게이트웨이는 ICMP 스푸핑을 막기 위해 방화벽 등을 이용해 ICMP 차단!</li>
</ul>
</li>
</ul>
<hr />
<h1 id="dns">DNS</h1>
<ul>
<li>DNS(Domain Name Service, 도메인 네임 서비스)<ul>
<li>접속하려는 URL 주소 이름으로 IP 주소를 구하는 서비스</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0b46da0a-3822-4130-a80a-e662ca8313c6/image.png" /></p>
<hr />
<h1 id="dns-스푸핑">DNS 스푸핑</h1>
<ul>
<li>DNS 스푸핑의 개념<ul>
<li>공격 대상에게 전달되는 IP 주소를 변조하거나, DNS 서버에 변조된 IP 주소가 저장되게 하여 공격
대상이 의도하지 않은 주소로 접속하게 하는 공격 방법</li>
<li>가짜 은행 사이트의 예</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/85f4355b-b8dd-4272-bb14-db0798e1a258/image.png" /></p>
<hr />
<h1 id="dns-스푸핑-1">DNS 스푸핑</h1>
<ul>
<li>DNS 스푸핑<ul>
<li>일반 사용자가 자신이 공격을 당했는지를 판단하기 쉽지 않음</li>
<li>‘보안 관련 인증 절차’라는 가짜 메시지 내용을 통해 사용자의 PC에 악성코드 설치 유도
→ 향후 2차, 3차의 추가적인 보안 사고 발생 가능</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5a381bac-2562-46c7-ad9e-7a2c8093db87/image.png" /></p>
<hr />
<h1 id="dns-스푸핑-2">DNS 스푸핑</h1>
<ul>
<li>스니핑을 이용한 공격<ul>
<li>Step-1: DNS 질의를 스니핑</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ee2ae07a-edb5-4e9a-b053-83086dc0db4f/image.png" /></p>
<ul>
<li>Step-2: 변조된 DNS 응답의 선택<ul>
<li>UDP 방식으로 DNS 응답이 전달되기 때문에 DNS 응답 중에서 먼저 도착한 메시지만 선택되고, 이후에 도착한 메시지는 무시<ul>
<li>공격자가 DNS 서버보다 공격 대상자에 좀 더 가까운 곳(같은 스위치에 연결)에 있음 
→ 공격자의 DNS 응답이 먼저 도착해서 공격자가 보낸 변조된 IP 주소를 선택하게 됨</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="dns-스푸핑-3">DNS 스푸핑</h1>
<ul>
<li>DNS 서버의 IP 주소 변조<ul>
<li>DNS 서버의 동작 방식: 순환 질의(Recursive Query) 방식<ul>
<li>계층적으로 도메인의 주소를 질의하는 방식</li>
</ul>
</li>
<li>구해진 IP 주소는 DNS 서버에 캐시(Cache)로 저장</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5467a714-8051-4a56-8ac1-575e04218153/image.png" /></p>
<hr />
<h1 id="dns-스푸핑-4">DNS 스푸핑</h1>
<ul>
<li>DNS 캐시 포이즈닝 - DNS 서버의 IP 주소 변조<ul>
<li>DNS서버에 대한 스푸핑 공격<ul>
<li>공격자가 위조된 IP를 DNS 서버에 전달</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ebed4332-94e1-498a-adbb-ee91e32c8b7d/image.png" /></p>
<hr />
<h1 id="dns-스푸핑-5">DNS 스푸핑</h1>
<ul>
<li>랜덤 ID 생성 기반의 DNS 캐시 포이즈닝<ul>
<li>Step-1: 대규모 DNS 질의를 보냄<ul>
<li>DNS 서버는 공인 네임 서버의 DNS 응답이 자신이 보낸 요청에 대한 응답인지 확인하기 위해 ID 생성</li>
<li>스니핑 혹은 스푸핑 등으로 ID를 알아내야 함 → 하지 만 쉬운 방법으로 랜덤 ID 생성해 여러 번 시도</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/81424de4-5b0b-4591-ba31-4bdf9565a54a/image.png" /></p>
<hr />
<h1 id="dns-스푸핑-6">DNS 스푸핑</h1>
<ul>
<li>랜덤 ID 생성 기반의 DNS 캐시 포이즈닝<ul>
<li>Step-2: 대규모 DNS 응답을 보냄</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/63084382-1b31-4292-9498-ecd2481f5d98/image.png" /></p>
<ul>
<li>여러 개의 서로 다른 ID 값을 랜덤(Random)하게 생성하여, DNS 응답을 동시에 보냄→ DNS 서버와 공인 네임 서버가 공유하는 ID 값을 우연히 알아 맞춤</li>
<li>일단 ID 값이 같다면 공격자가 보낸 DNS 응답이 공인 네임 서버에서 보내는 DNS 응답 대신에 선택됨</li>
<li>대부분 공격자가 공인 네임 서버보다 DNS 서버에 가까워, 먼저 도착함</li>
</ul>
<hr />
<h1 id="dns-스푸핑-7">DNS 스푸핑</h1>
<ul>
<li>DNS 캐시 포이즈닝 - DNS 서버의 IP 주소 변조<ul>
<li>생일 공격(Birthday Attack) 기법<ul>
<li>생일 역설(Birthday Paradox) : 한 반에 동시에 23명의 사람이 모여 있을 때 그 중에 생일이 같은 사람이 있을 확률이 50% 이상. 우리가 예상하는 확률보다 실제 확률이 뜻밖에 높다</li>
<li>DNS 질의에서 사용되는 ID는 크기 : 2바이트(16비트)</li>
<li>모두 65,536개의 값을 가질 수 있음 : 0 ~ 65,535</li>
<li>만약, 임의로 728이란 값을 선택하면, 약 750번의 랜덤 값을 생성시키면 728이라는 같은 값을 얻을 수 있음</li>
<li>공격자가 랜덤하게 750개 이상의 DNS 응답 ID를 생성 → 그 중 1개는 성공</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bbf89075-845f-44ba-8423-57efd2948392/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c16862a9-7448-45f1-99ec-86e94fcf712a/image.png" /></p>
<hr />
<h1 id="dns-스푸핑-8">DNS 스푸핑</h1>
<ul>
<li>DNS 캐시 포이즈닝 공격의 대비책<ul>
<li>DNS 서버의 소프트웨어(예를 들어 bind)의 최신 버전으로 업데이트<ul>
<li>BIND(Berkeley Internet Name Domain) : DNS를 를 운용하기 위한 데몬 프로그램</li>
</ul>
</li>
<li>외부에서 요청되는 DNS 질의에 대해서는 DNS 서버가 순환 질의를 하지 않도록 설정</li>
<li>DNSSEC(Domain Name System Security Extensions) 사용<ul>
<li>암호화하여 DNS 질의 및 응답 전달</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="서비스-거부-공격">서비스 거부 공격</h1>
<ul>
<li>서비스 거부 (DoS: Denial Of Service) 공격<ul>
<li>서비스가 정상적으로 제공되지 못하도록 방해하는 공격</li>
<li>도스 공격 or 디오에스 공격</li>
<li>공격의 목적 : 가용성(Availability)을 떨어트리는 것<ul>
<li>대규모의 가짜 요청을 만들어서 공격 대상자의 시스템에 과부하를 일으켜 정상적인 서비스 불능 상태 만듦</li>
<li>스니핑 &amp; 스푸핑은 원래의 정보를 변조하려는 목적이나 서비스 거부 공격은 공격 대상자를 망가뜨림(파급효과 큼)</li>
</ul>
</li>
</ul>
</li>
<li>분산 서비스 거부(DDoS: Distributed Denial Of Service) 공격<ul>
<li>공격자가 여러 곳에서 동시에 서비스 거부 공격을 하는 방법</li>
<li>악성코드 등을 이용해 좀비 PC 만들어 활용</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9ef46445-1392-4c88-9c47-9d6576e78b2e/image.png" /></p>
<hr />
<h1 id="서비스-거부-공격-1">서비스 거부 공격</h1>
<ul>
<li>DoS 공격과 DDoS 공격 유형</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6f86db28-0e26-46c2-ba3a-667fd1d82008/image.png" /></p>
<ul>
<li>서비스 거부 공격은 명백한 범법 행위</li>
<li>왜 서비스 거부 공격을 할까?<ul>
<li>공격자가 자신의 능력을 자랑하기 위해서</li>
<li>경쟁사의 서비스를 방해하기 위해서 : 반사 이익이 목적</li>
<li>서비스 중단을 빌미로 서비스 제공자를 협박하여 돈을 갈취</li>
</ul>
</li>
</ul>
<hr />
<h1 id="서비스-거부-공격-2">서비스 거부 공격</h1>
<ul>
<li>TCP SYN 플러딩<ul>
<li>SYN 패킷을 대량으로 보내어 웹 서버의 네트워크 대역폭을 낭비해서 일반 사용자들이 아예 웹 서버로 접속을 못 하게 만드는 공격 방법<ul>
<li>SYN 패킷을 넘치게 하는 공격, 신 플러딩(SYN Flooding)이라고도 함</li>
</ul>
</li>
</ul>
</li>
<li>TCP의 3-웨이 핸드셰이킹(3-way Handshaking)의 특징을 악용하는 방법<ul>
<li>처음의 두 단계가 이루어진 다음에 송신자가 세 번째 단계인 ACK 패킷을 보내지 않음
→ 수신자는 송신자가 ACK 패킷을 보낼 때까지 계속 기다림<ul>
<li>운영체제에서 설정된 최대 시간까지 기다리는데 보통 10초에서 1분 정도</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6586a952-a665-4b3c-8a00-480eb171b2e3/image.png" /></p>
<hr />
<h1 id="서비스-거부-공격-3">서비스 거부 공격</h1>
<ul>
<li>TCP SYN 플러딩(예시)<ul>
<li>최대 1,000명의 사용자에게 서비스할 수 있는 웹 서버로 공격자가 1,000개 혹은 그 이상의 SYN
패킷을 동시에 전송</li>
<li>대기 큐에서 지워지는 속도보다 채워지는 속도가 더 빠르도록 만듦</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1e514d1c-ab7a-40c1-8ac0-ceea0fd69e33/image.png" /></p>
<hr />
<h1 id="서비스-거부-공격-4">서비스 거부 공격</h1>
<ul>
<li>TCP SYN 플러딩 대응 방안<ul>
<li>대기 큐의 크기 증가( 서버의 가용성 증가) : 자원 증가의 한계 있음</li>
<li>최대 접속 대기 시간 감소 : ACK 패킷이 2초 내에 오지 않을 때에 강제 접속 종료</li>
<li>보안 솔루션 적용 : 침입 방지 시스템(IPS: Intrusion Prevention Systems) 등</li>
</ul>
</li>
</ul>
<hr />
<h1 id="서비스-거부-공격-5">서비스 거부 공격</h1>
<ul>
<li>ICMP 플러딩 : 스머프 공격<ul>
<li>대량의 ICMP echo 응답을 만들어 공격</li>
<li>브로드캐스팅 방식으로 동작하는 ICMP 프로토콜의 특성을 악용</li>
<li>ICMP echo의 출발 IP 변조</li>
<li>스머프(Smurf) 공격이라고도 부름</li>
<li>서비스 거부 공격의 수단으로 사용되는 단말 : 에이전트(Agent), 슬레이브(Slave), 봇 (Bot), 좀비(Zombie)</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/da442cd2-c191-487b-bc8f-9a852866b645/image.png" /></p>
<hr />
<h1 id="서비스-거부-공격-6">서비스 거부 공격</h1>
<ul>
<li>ICMP 플러딩: 스머프 공격<ul>
<li>Step-1: 공격자에 의한 브로드캐스트<ul>
<li>브로드캐스트를 이용해 에이전트가 동시에 공격</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/de8c9699-4efb-47a3-9b7f-cad86189f476/image.png" /></p>
<hr />
<h1 id="서비스-거부-공격-7">서비스 거부 공격</h1>
<ul>
<li>ICMP 플러딩: 스머프 공격<ul>
<li>Step-2: 에이전트에 의한 공격 실행<ul>
<li>변조된 ICMP echo 요청을 받은 에이전트들이 동시에 ICMP echo 응답을 공격 대상자에게 보냄</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0853d042-0bcc-4534-887c-6684a0b80954/image.png" /></p>
<hr />
<h1 id="서비스-거부-공격-8">서비스 거부 공격</h1>
<ul>
<li>분산 서비스 거부 공격의 구조<ul>
<li>4가지 구성요소 : 공격자, 공격 대상자, 에이전트, 마스터<ul>
<li>에이전트 : 공격 대상자에게 실제 공격을 하는 주체 (슬레이브, 봇, 좀비)</li>
<li>마스터 : 중간 증폭기 역할 (전달 공격자로부터 공격 명령을 받아 에이전트로 전달</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e6e183a8-5e59-4344-8b72-0e17e935df90/image.png" /></p>
<hr />
<h1 id="서비스-거부-공격-9">서비스 거부 공격</h1>
<ul>
<li>분산 서비스 거부 공격의 구조<ul>
<li>악성코드에 의한 DDoS</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/53090b67-bdfc-46ef-a83e-595c8d2e2101/image.png" /></p>
<hr />
<h1 id="서비스-거부-공격-10">서비스 거부 공격</h1>
<ul>
<li>IP 플러딩<ul>
<li>서비스 거부 공격을 하기 위해 공격자가 IP 관련 내용을 변조하는 공격 방식<ul>
<li>랜드(LAND) 공격 : 출발지 IP 주소를 변조하는 공격</li>
<li>티어드랍(Teardrop) 공격 : IP 패킷의 순서를 변조하는 공격</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="서비스-거부-공격---ip-플러딩">서비스 거부 공격 - IP 플러딩</h1>
<ul>
<li>랜드(LAND: Local Area Network Denial) 공격<ul>
<li>1997년 처음 발견, 패킷을 보낼 때 출발지 IP 주소와 도착지 IP주소를 같게 하여 보냄
→ 내보낸 메시지가 다시 자기 자신으로 돌아와서 무한 루프(Infinite Loop)에 빠짐</li>
<li>대처 방안<ul>
<li>윈도우 서버 2003, 윈도우 XP SP2 이후 버전의 운영체제는 패치가 적용되어 있음</li>
<li>방화벽 및 기타 네트워크 보안 솔루션 : 출발지와 도착지 IP가 같은 경우에 대한 예외처리 제공</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/57383270-48a9-47bb-ace9-edd6b490d62d/image.png" /></p>
<hr />
<h1 id="서비스-거부-공격---ip-플러딩-1">서비스 거부 공격 - IP 플러딩</h1>
<ul>
<li>티어드랍(Teardrop)<ul>
<li>IP 패킷(IP Fragments)의 헤더를 서로 중첩되도록 조작해서, IP 패킷을 재조합 과정에서 오류를
발생시키도록 하는 공격</li>
<li>네트워크 연결이 끊어지거나 혹은 블루 스크린(Blue screen) 등의 시스템 자체가 중단되기도 함</li>
<li>정상적인 IP 패킷 vs. 비정상적인 IP 패킷</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/31b009e5-ac96-453f-91eb-41b9357da9ca/image.png" /></p>
<ul>
<li>대처 방안<ul>
<li>윈도우 XP 이상의 운영체제에서는 이러한 티어드랍 공격에 대한 패치가 포함</li>
<li>시퀀스 번호에 오류가 있는 IP 패킷은 무시</li>
</ul>
</li>
</ul>
<hr />
<h1 id="서비스-거부-공격---http-get-플러딩">서비스 거부 공격 - HTTP GET 플러딩</h1>
<ul>
<li>HTTP GET 플러딩<ul>
<li>특정 웹페이지를 동시에 여러 에이전트가 요청하여 웹 서버가 이를 감당하지 못하게 만들어 서비스
거부를 일으키는 공격 방법</li>
<li>특정 서버를 대상으로 하여 특정 서버가 제공하는 서비스만을 중단</li>
<li>대처가 어려움 : 정상적인 HTTP 요청 → 단순히 요청 자체를 거부해서는 안 됨</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fe2b9a53-447b-4bed-acec-0ff16d6e1a69/image.png" /></p>
<ul>
<li>대응 방안 : 임계치 기반의 방어 기법<ul>
<li>특정 IP에서 임계치 값을 넘어서 대량의 HTTP GET 요청이 지속 
→ 해당 IP에서 전달되는 HTTP GET 요청 무시</li>
</ul>
</li>
</ul>
<hr />
<h1 id="서비스-거부-공격---http-get-플러딩-1">서비스 거부 공격 - HTTP GET 플러딩</h1>
<ul>
<li>HTTP GET 플러딩(변종 공격)<ul>
<li>HTTP CC 공격과 동적 HTTP 요청 공격</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bd0cfddb-455b-4758-afd8-0484ec78f2ae/image.png" /></p>
<hr />
<h1 id="서비스-거부-공격---http-get-플러딩-2">서비스 거부 공격 - HTTP GET 플러딩</h1>
<ul>
<li>HTTP CC 공격<ul>
<li>더 많은 부하를 발생시키기 위해 (HTTP 1.1 표준에 정의된) HTTP 헤더의 CC(Cache-Control) 옵션 값 사용<ul>
<li>웹 서버에서 캐시(Cache) 기능을 사용하지 않게 만듦 
→ 캐시를 사용하지 않아 항상 새로운 응답 메시지를 만들어야 하므로 웹 서비스 부하 증가</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0681b154-0173-4282-ba79-4b4c25d94b35/image.png" /></p>
<ul>
<li>방어 방법 : 임계치 기반의 방어 기법</li>
<li>같은 IP에서 보낸 대량의 HTTP GET 요청을 무시</li>
</ul>
<hr />
<h1 id="서비스-거부-공격---http-get-플러딩-3">서비스 거부 공격 - HTTP GET 플러딩</h1>
<ul>
<li>HTTP GET 플러딩<ul>
<li>동적 HTTP 요청 공격<ul>
<li>요청되는 웹 페이지 주소가 동적으로 바뀌는 공격</li>
<li>매번 요청되는 웹 페이지의 URL 주소가 변경 → DDoS 공격인지 판단이 어려움<ul>
<li>예) view.jsp?id=101, 102, 103, ...<ul>
<li>특정 게시판의 글 내용을 요청하는 경우 뒤의 글 번호 ID 값이 변경</li>
</ul>
</li>
</ul>
</li>
<li>웹 페이지 주소를 기반으로 임계치를 적용하는 것이 어려움<ul>
<li>단, 출발지 IP 주소는 동일</li>
<li>출발지 IP 주소 기반의 임계치 기반의 차단 정책<ul>
<li>특정 IP가 짧은 시간 내에 많은 요청을 할 경우 이를 차단</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>