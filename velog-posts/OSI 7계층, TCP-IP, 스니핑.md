<hr />
<h1 id="1-osi-7계층">1. OSI 7계층</h1>
<ul>
<li>OSI 7계층 모델<ul>
<li>네트워크의 동작 과정을 설명하는 가장 대표적인 모델</li>
<li>국제표준화기구인 ISO(International Organization for Standardization)에서 제정</li>
<li>실제 구현된 시스템이 아니라, 일종의 개념적 모델<ul>
<li>TCP/IP는 실제 구현이 되어 실질적인 표준처럼 사용되는 네트워크 모델</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="-통신-프로토콜protocol">• 통신 프로토콜(Protocol)</h2>
<p>• 네트워크를 통해 데이터를 주고받는 과정에 대한 약속
• OSI 7계층 모델은 통신 프로토콜을 7개의 세부 프로토콜로 나누어 설명</p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7a39d699-be7d-4c4e-8f84-cedb7381d1fb/image.png" /></p>
<hr />
<h2 id="-7계층-응용-계층">• 7계층: 응용 계층</h2>
<ul>
<li>응용 계층(Application Layer)<ul>
<li>사용자에게 인터페이스(UI: User Interface)를 제공하는 계층<ul>
<li>예1) 메일을 보내고 받는 MS사의 아웃룩(Outlook) 프로그램</li>
<li>예2) 웹 브라우저, FTP 프로그램 등</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="6계층-표현-계층presentation-layer">6계층: 표현 계층(Presentation Layer)</h2>
<ul>
<li>응용 계층(7계층)에서 다루는 데이터의 형식을 변환(Format Conversion)하는 계층<ul>
<li>암호화·복호화 혹은 인코딩·디코딩 등의 데이터 형식의 변환을 수행하는 계층<ul>
<li>예) 이메일 메시지: MIME(Multipurpose Internet Mail Extensions) 포맷으로 인코딩 (Encoding) 되어
있음 → 일반 텍스트 포맷으로 변환</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ef08746e-68cd-45d6-ba13-691e6fa60d06/image.png" /></p>
<hr />
<h2 id="-5계층-세션-계층session-layer">• 5계층: 세션 계층(Session Layer)</h2>
<p>• 두 개의 응용 프로세스 사이에 통신(세션)을 관리하는 계층</p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/316c0218-667c-4a30-90e4-830bd71947e6/image.png" /></p>
<hr />
<h2 id="-4계층-전송-계층transport-layer">• 4계층: 전송 계층(Transport Layer)</h2>
<ul>
<li>데이터를 주고받을 때 데이터의 유실(Loss)이 없도록 보 장해주는 계층</li>
<li>흐름 제어(Flow control)<ul>
<li>양 끝단(End-to-end)에서 전달받은 데이터의 오류를 검출<ul>
<li>만약 오류가 있다고 판단되면 재전송을 요청 → 데이터의 유실 방지</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ff938c7d-0d82-4ce8-bfe3-71c391e3d066/image.png" /></p>
<hr />
<h2 id="-전송-계층의-상하-관계의-특성">• 전송 계층의 상하 관계의 특성</h2>
<ul>
<li>상위 계층 (5계층, L5)은 하위 계층 (4계층, L4)이 하는 일에 관여하지 않음<ul>
<li>전송 계층의 상하 관계</li>
</ul>
</li>
<li>5계층(L5)의 1개 메시지 → 2개의 4계층(L4) 세그먼트(Segment)로 쪼개짐<ul>
<li>세그먼트: 4계층에서 다루는 데이터의 단위<ul>
<li>네트워크 전송에 적절한 크기로 쪼갠 것 + 헤더(Header) 정보<ul>
<li>페이로드(Payload): 상위 계층의 데이터</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>캡슐화(Encapsulation): 하위 계층에서 상위 계층의 페이로드에 헤더 정보를 붙이는 것<ul>
<li>E.g. 상위 계층- 5계층, 하위 계층- 4계층</li>
<li>4계층의 헤더: 흐름 제어를 위한 정보 포함<ul>
<li>데이터의 오류 검출, 만약 오류가 있다고 판단되면 재전송 요청</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ac8020e7-4b75-439a-8944-063b7c3d006d/image.png" /></p>
<hr />
<h2 id="-전송-계층의-대표적인-예-tcp-vs-udp">• 전송 계층의 대표적인 예: TCP vs. UDP</h2>
<ul>
<li>TCP(Transmission Control Protocol)</li>
<li>UDP(User Datagram Protocol)</li>
<li>전송 계층에서 하는 역할인 흐름 제어를 TCP만 하고 UDP에서는 하지 않음<ul>
<li>UDP는 신뢰성이 떨어지는 약점이 있지만 속도가 상대적으로 빠름<ul>
<li>예) 인터넷 실시간 영상 중계 등</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bcfb5134-bdb8-42db-9b9d-b10f770fb88f/image.png" /></p>
<hr />
<h2 id="-3계층-네트워크-계층network-layer">• 3계층: 네트워크 계층(Network Layer)</h2>
<ul>
<li>라우팅(Routing)을 처리하는 계층<ul>
<li>라우팅: 데이터를 전달할 때 어떤 경로로 데이터를 보낼지 경로를 선택하는 것
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c51ba78e-1d03-4f9b-a895-e5ebd408ceee/image.png" /></li>
</ul>
</li>
</ul>
<ul>
<li>여러 개의 노드가 복잡하게 연결된 네트워크에서 최적의 전달 경로가 정해질 수 있도록 여러 가지 기능을 제공</li>
</ul>
<hr />
<h2 id="-3계층-네트워크-계층-계속">• 3계층: 네트워크 계층 (계속)</h2>
<ul>
<li>3계층의 캡슐화<ul>
<li>세그먼트(4계층의 데이터)에 라우팅과 관련된 헤더 정  보가 추가</li>
<li>패킷(Packet): 3계층의 데이터 단위</li>
</ul>
</li>
<li>패킷의 헤더: 최적의 경로 선택를 위한 기초 자료 저장<ul>
<li>각 노드 사이의 전송 속도를 저장: 노드 사이의 전송 비용에 대한 추정치</li>
</ul>
</li>
<li>기존에 구해진 경로 상의 노드가 고장이 발생 → 대체 경로를 찾아서 전송<ul>
<li>네트워크 계층의 대표적인 예: IP(Internet Protocol) 프로토콜</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e1602ff4-49ea-4853-8306-60d44fb545ee/image.png" /></p>
<hr />
<h2 id="-2계층-데이터-링크-계층data-link-layer">• 2계층: 데이터 링크 계층(Data Link Layer)</h2>
<ul>
<li>단말 사이의 신뢰성 있는 전송을 보장하는 계층</li>
<li>포인트 투 포인트(Point-to-Point) 간 신뢰성을 보장하는 계층<ul>
<li>1계층인 물리 계층에서 발생할 수 있는 오류를 찾아내고 이를 수정</li>
</ul>
</li>
<li>에러를 검출하는 기법: 패리티 검사 (Parity Check) 등의 기법이 사용</li>
<li>2계층(L2)에서의 데이터 캡슐화<ul>
<li>프레임(Frame): 2계층에서 전달하는 데이터의 단위<ul>
<li>3계층의 페이로드인 패킷 앞·뒤에 헤더와 테일을 덧붙임</li>
</ul>
</li>
</ul>
</li>
<li>2계층의 예: 이더넷(Ethernet), 토큰 링(Token Ring) 등</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ad088891-3d10-4f7e-a7a6-15dcbf56d36f/image.png" /></p>
<hr />
<h2 id="1계층-물리-계층physical-layer">1계층: 물리 계층(Physical Layer)</h2>
<ul>
<li>단말과 단말 사이를 실제 물리적으로 연결<ul>
<li>예) 광케이블, 구리 케이블 또는 무선 등</li>
</ul>
</li>
<li>단말(Terminal)<ul>
<li>네트워크 사이를 연결해주는 관문 역할을 하는 노드(3계층) + 네트워크에 참여한 모든 단말을 포함</li>
<li>예) PC 또는 스마트폰 등</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d5f090ba-e2a9-4413-9745-a3f7f53ab39b/image.png" /></p>
<hr />
<h1 id="2-tcpip-프로토콜">2. TCP/IP 프로토콜</h1>
<h2 id="-tcpip-개요">• TCP/IP 개요</h2>
<ul>
<li>인터넷을 움직이게 하는 핵심 통신 프로토콜</li>
<li>TCP/IP와 OSI 7계층 모델의 관계</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/28750bfc-5b31-4abe-b0b0-231b172dfa8f/image.png" /></p>
<hr />
<h2 id="-ip-프로토콜의-이해">• IP 프로토콜의 이해</h2>
<ul>
<li>IP: 네트워크 계층에 해당하는 통신 프로토콜, 라우팅(Routing) 담당</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4cb7c089-2ede-43a8-aef0-92b4157da3bd/image.png" /></p>
<ul>
<li>각 노드(라우터)의 주소: 3계층의 IP 주소</li>
<li>라우팅 테이블(Routing Table): 각 노드 사이의 연결 정보를 저장한 테이블<ul>
<li>두 연결 사이의 전송 비용(Cost) 저장</li>
<li>전송 속도 or 단순히 거쳐야 하는 라우터 개수(Hop Count)<ul>
<li>윈도우 CMD에서 ‘route PRINT’로 확인</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="-ip-주소internet-protocol-address-네트워크상에서-유일한-주소">• IP 주소(Internet Protocol Address): 네트워크상에서 유일한 주소</h2>
<ul>
<li><p>IP 버전 4(IPv4, IP Version 4) 주소</p>
<ul>
<li>특별한 언급 없이 IP 주소라고 하면 IPv4</li>
<li>IP 주소의 크기 및 범위: 32비트(4바이트)</li>
<li>8비트씩 온점(.)을 찍어 끊어서 표시: 0.0.0.0부터 255.255.255.255</li>
<li>약 42억 개의 주소 할당이 ‘11년 2월 4일 종료 → 신규 주소 할당 중지</li>
</ul>
</li>
<li><p>IP 버전 6(IPv6, IP Version 6) 주소</p>
<ul>
<li><p>IP 주소의 크기: 128비트(16바이트) → IPv4 주소 개수의 296배의 크기</p>
</li>
<li><p>유비쿼터스 환경에서 사물마다 주소를 부여할 수 있는 수준</p>
</li>
<li><p>16진수 여덟 개를 쓰고 각각 쌍점( : ) 기호로 구분</p>
<ul>
<li>예) 2001:0db8:85a3:08d3:1319:8a2e:0370:7334</li>
</ul>
</li>
<li><p>IPv4와 IPv6는 호환이 되지 않음: IPv6 교체 비용이 높아서 적용이 더딘 상황</p>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="-ip-주소-계속">• IP 주소 (계속)</h2>
<ul>
<li>IP 주소의 클래스(Class)<ul>
<li>A부터 E까지 모두 5개</li>
<li>일반적으로 사용되는 클래스: A, B, C</li>
<li>특수 목적 클래스 D와 E<ul>
<li>D: 멀티 캐스팅(Multi-casting)용</li>
<li>E: 주로 연구용</li>
</ul>
</li>
</ul>
</li>
<li>IP주소 클래스에 따른 값의 범위</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e0077da5-d624-40e0-966c-0d01d98f48b7/image.png" /></p>
<hr />
<h2 id="-ip-주소-계속-1">• IP 주소 (계속)</h2>
<ul>
<li>IP 주소 = 네트워크 주소 + 호스트 주소<ul>
<li>IP 주소의 요청</li>
<li>TCP/IP를 관리하는 국제표준기구 IANA(Internet Assigned Numbers Authority)에 요청<ul>
<li>IP 주소의 ‘네트워크 주소’에 해당하는 부분만을 할당 받음</li>
<li>나머지 ‘호스트 주소’ 범위는 신청자가 자율적으로 관리하는 부분</li>
</ul>
</li>
</ul>
</li>
</ul>
<p> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/aa094b71-b2c2-4298-aa5d-8719eb8d541c/image.png" /></p>
<hr />
<h2 id="-ip-주소-계속-2">• IP 주소 (계속)</h2>
<ul>
<li>클래스 별 IP주소의 구성<ul>
<li>클래스 A: 네트워크 주소 개수 자체는 적지만, 포함하는 호스트 개수 많음<ul>
<li>A의 네트워크 개수: 128개</li>
<li>A의 호스트 개수: 2563개 (16,777,216개)</li>
</ul>
</li>
<li>클래스 B와 C: 네트워크 주소가 많지만, 포함할 수 있는 호스트 개수 적음<ul>
<li>C의 네트워크 개수: 25×256×256개 (2,097,152개)</li>
<li>C의 호스트 개수: 256개</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9b502add-a144-4898-97ad-f96f04280e52/image.png" /></p>
<hr />
<h2 id="-ip-주소-계속-3">• IP 주소 (계속)</h2>
<ul>
<li>공인 IP 주소(Public IP Address) vs. 사설 IP 주소(Private IP Address)</li>
<li>공인 IP 주소: IANA에 의해 할당받은 IP 주소</li>
<li>사설 IP 주소: 사내 네트워크에서만 사용될 수 있는 IP 주소<blockquote>
<p>클래스 A 10.0.0.0 ~ 10.255.255.255
클래스 B 172.16.0.0 ~ 172.31.255.255
클래스 C 192.168.0.0 ~ 192.168.255.255</p>
</blockquote>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f5d043ed-0650-457b-b338-43ccc430bc1e/image.png" /></p>
<hr />
<h2 id="-tcp-프로토콜의-이해">• TCP 프로토콜의 이해</h2>
<ul>
<li>TCP는 연결 지향적(Connection-oriented) 인 프로토콜<ul>
<li>송신자와 수신자가 통신을 시작되면 둘 사이에 연결 (Connection)이 맺어지고 통신이 끝날 때까지 연결이
지속됨</li>
</ul>
</li>
<li>TCP의 시작 과정: 3-way Handshaking<ul>
<li>(1) 송신자: 연결을 맺자고 요청하는 SYN(Synchronize, 동기화) 패킷 보냄</li>
<li>(2) 수신자: 송신자 요청을 승인하는 SYN+ACK(Acknowledge, 수락) 패킷 보냄</li>
<li>(3) 송신자: 수신자의 승인 패킷을 확인했다는 의미로 ACK 패킷 보냄<ul>
<li>이러한 3단계를 거치면 연결 생성(Established) 상태가 됨</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/52948eb7-4b89-48a9-b5b1-175cbd1b6356/image.png" /></p>
<hr />
<h2 id="-tcp-프로토콜의-이해-1">• TCP 프로토콜의 이해</h2>
<ul>
<li>실제 메시지가 오고 가는 과정: 2-way 방식<ul>
<li>흐름 제어(Flow Control) : 수신자의 ACK 패킷을 송신자가 일정 시간 못 받은 경우<ul>
<li>송신자는 수신자에게 다시 메시지를 재전송</li>
<li>TCP 헤더 정보를 이용, 슬라이딩 윈도우(Sliding Window) 기법으로 처리</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/505a5dc5-46d8-4c7e-963f-5b8595f01758/image.png" /></p>
<hr />
<h2 id="-tcp-프로토콜의-이해-2">• TCP 프로토콜의 이해</h2>
<ul>
<li>TCP 헤더 정보<ul>
<li>순서 번호(Sequence Number)</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/27f78cfe-daba-49a6-9c30-e145aa6e475f/image.png" /></p>
<hr />
<h2 id="-tcp-프로토콜의-이해-3">• TCP 프로토콜의 이해</h2>
<ul>
<li>TCP의 종료 과정: 4-way</li>
<li>(1) 송신자 : 수신자에게 연결을 끊고자 FIN(Finish, 종료) 패킷 보냄</li>
<li>(2)(3) 수신자 : ACK 패킷과 FIN 패킷을 각각 보냄<ul>
<li>종료 요청에 대한 확인과 동시에 자신도 연결 종료를 요청하는 것</li>
</ul>
</li>
<li>(4) 송신자 : 수신자의 종료 패킷에 대한 확인으로 ACK 패킷 보냄<ul>
<li>이렇게 연결이 끊어지게 되면 연결이 닫힘 상태(Closed)로 변경됨</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/233d0a56-9fe5-4b31-a48f-f6ed1f97045f/image.png" /></p>
<hr />
<h2 id="-tcp의-포트port">• TCP의 포트(Port)</h2>
<ul>
<li><p>포트(Port): 각 단말기 내에서 사용되는 주소</p>
<ul>
<li>수신자의 시스템 내에서 어떤 프로그램으로 메시지를 올려 보내줄지 결정</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5f538927-2286-46ed-86c0-47384c5aa183/image.png" /></p>
</li>
</ul>
<hr />
<h2 id="-tcp의-포트port-1">• TCP의 포트(Port)</h2>
<ul>
<li>대표적으로 많이 사용되는 TCP 포트<ul>
<li>20, 21 – FTP, 원격 파일 전송을 위한 목적</li>
<li>22 – SSH, 암호화된 원격 접속을 위한 목적</li>
<li>23 – 텔넷(Telnet), 원격 접속을 위한 목적</li>
<li>53 - DNS(Domain Name System), URL의 도메인 주소에서 IP 주소를 얻어올 때</li>
<li>80 - HTTP, 웹 접속을 위한 목적</li>
<li>110 - POP3(Post Office Protocol), 이메일 서버로부터 메일을 읽어올 때 사용</li>
<li>443 – HTTPS, 암호화된 웹 접속을 위한 목적</li>
</ul>
</li>
<li>TCP 포트 번호 범위</li>
</ul>
<table>
<thead>
<tr>
<th><strong>범위</strong></th>
<th><strong>구분</strong></th>
</tr>
</thead>
<tbody><tr>
<td>0 ~ 1,023번</td>
<td>잘 알려진 포트 (well-known port)</td>
</tr>
<tr>
<td>1,024 ~ 49,151번</td>
<td>등록된 포트 (registered port)</td>
</tr>
<tr>
<td>49,152 ~ 65,535번</td>
<td>동적 포트 (dynamic port)</td>
</tr>
</tbody></table>
<hr />
<h1 id="보안-공격의-유형">보안 공격의 유형</h1>
<ul>
<li>기준: 직접적인 피해가 발생하는지에 여부<ul>
<li>능동적 공격(Active Attack)</li>
<li>수동적 공격(Passive Attack)</li>
</ul>
</li>
</ul>
<table>
<thead>
<tr>
<th><strong>구분</strong></th>
<th><strong>수동적 공격</strong></th>
<th><strong>능동적 공격</strong></th>
</tr>
</thead>
<tbody><tr>
<td><strong>특징</strong></td>
<td>직접적인 피해 없음</td>
<td>직접적인 피해 있음</td>
</tr>
<tr>
<td><strong>탐지 가능성</strong></td>
<td>어려움</td>
<td>쉬움</td>
</tr>
<tr>
<td><strong>대표적인 예</strong></td>
<td>스니핑(Sniffing) 혹은 도청(Eavesdrop)</td>
<td>사회 공학(Social Engineering) <br /> 재사용 공격(Replay Attack) <br /> 변조 <br /> DoS / DDoS <br /> 세션 하이재킹(Session Hijacking)</td>
</tr>
</tbody></table>
<ul>
<li>수동적 공격 탐지의 중요성<ul>
<li>수동적 공격을 통해서 보안 취약점 정보의 획득 → 능동적 공격을 실행</li>
<li>능동적 공격 발생: 이미 수동적 공격도 상당 기간 동안 받았음을 의미</li>
</ul>
</li>
</ul>
<hr />
<h1 id="3-스니핑">3. 스니핑</h1>
<ul>
<li>개요<ul>
<li>스니핑(Sniffing)<ul>
<li>sniff는 ‘냄새를 맡다’ 혹은 ‘코를 킁킁거리다’라는 뜻</li>
<li>네트워크 보안에서는 송신자와 수신자가 주고받는 데이터를 중간에서 도청하는 것</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fb58df33-9b61-438b-bc1f-9dc9b3ae086b/image.png" /></p>
<hr />
<h2 id="-스니핑-기법-1-허브-환경에서의-스니핑">• 스니핑 기법 1: 허브 환경에서의 스니핑</h2>
<ul>
<li>허브: 더미 허브(Dummy Hub) 또는 수동 허브<ul>
<li>일종의 리피터(Repeater) 장비<ul>
<li>입력으로 전달받은 패킷을 나머지 모든 포트로 단순히 전달</li>
</ul>
</li>
<li>운영체제상 ‘다른 PC로 전달되는 패킷’을 무시<ul>
<li>네트워크 카드 (NIC, Network Interface Card) 의 셋팅<ul>
<li>자신의 MAC 주소가 아닌 패킷들은 필터링</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>네트워크 카드: 무차별 모드(Promiscuous Mode)로 설정<ul>
<li>나의 MAC 주소가 아닌 패킷도 전달받는 모드
→ 허브 환경에서 스니핑 가능</li>
</ul>
</li>
</ul>
<hr />
<h2 id="-스니핑-기법-2-스위치-환경에서의-스니핑">• 스니핑 기법 2: 스위치 환경에서의 스니핑</h2>
<ul>
<li>스위치(Switch)<ul>
<li>MAC 주소 정보를 이용하여 패킷을 해당 목적지로만 전달 → 무차별 모드로 셋팅해도 스니핑이 불가능</li>
</ul>
</li>
<li>모니터링 포트 (Monitoring Port) 를 이용한 스니핑<ul>
<li>모니터링 포트: 스위치를 통과하는 모든 패킷의 내용을 전달하는 포트<ul>
<li>정상적인 관리 목적으로 사용하기 위해 네트워크 장비 자체가 제공</li>
</ul>
</li>
<li>물리적으로 스위치에 접근 가능 → 모니터링 포트를 통해 스니핑 가능</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0e581c07-542e-4bb6-b831-e6d96f333ba1/image.png" /></p>
<hr />
<h2 id="-스니핑-기법-2-스위치-환경에서의-스니핑계속">• 스니핑 기법 2: 스위치 환경에서의 스니핑(계속)</h2>
<ul>
<li>스위치 재밍을 이용한 스니핑<ul>
<li>재밍(Jamming): 전파 방해</li>
<li>매핑 테이블의 최대 저장 개수보다 더 많은 정보가 추가 → 브로드캐스팅(Broadcasting) 모드로 동작<ul>
<li>매핑 테이블(Mapping Table): IP 주소를 MAC 주소로 변환하기 위해 내부적으로 관리하는 테이블 (arp /a 로 확인)</li>
<li>브로드캐스팅 모드: 자신이 전달받은 모든 패킷을 연결된 모든 단말기에 전달</li>
</ul>
</li>
<li>스위치 재밍 공격을 통해 스위치가 마치 더미 허브처럼 동작하게 되기 때문에 통신 속도가 느려짐</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/54c36540-9923-41aa-ae1c-f3cd030a8975/image.png" /></p>
<hr />
<h2 id="-스니핑-기법-2-스위치-환경에서의-스니핑-계속">• 스니핑 기법 2: 스위치 환경에서의 스니핑 (계속)</h2>
<ul>
<li>스푸핑 공격 기법을 이용<ul>
<li>스푸핑(Spoofing) 기법: 공격자가 마치 자신이 수신자인 것처럼 ‘위장’<ul>
<li>능동적 공격의 한 가지 방법</li>
</ul>
</li>
<li>예) ARP 스푸핑 등</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/84071316-bec5-4983-b5fc-7eec54ae6e89/image.png" /></p>
<hr />
<h2 id="-스니핑-방지-대책">• 스니핑 방지 대책</h2>
<ul>
<li>암호화: 스니핑에 대한 가장 효과적인 대처 방안</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d8a9ba22-69ff-4a7d-a636-8c1960ea7bed/image.png" /></p>
<hr />
<h2 id="-스니핑-방지-대책-1">• 스니핑 방지 대책</h2>
<ul>
<li>웹 환경의 HTTPS (Hypertext Transfer Protocol over Secure Socket Layer)<ul>
<li>암호화된 통신 프로토콜: HTTP 웹 표준 프로토콜 + SSL/TLS(Secure Sockets Layer/Transport Layer Security)
암호화 통신 프로토콜</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e655130d-01dd-4148-913b-cfb99dd1bf70/image.png" /></p>
<hr />
<h2 id="-스니핑-방지-대책-2">• 스니핑 방지 대책</h2>
<ul>
<li>이메일 환경의 PGP와 S/MIME(이메일 암호화)<ul>
<li>PGP(Pretty Good Privacy): 사용하기 편하고 사용된 알고리즘의 안전성이 높기 때문에 대중적으로 널리 사용     (<a href="https://www.openpgp.org/">https://www.openpgp.org/</a>)<ul>
<li>1991년 필립 짐머만(Phil Zimmermann)에 의해 개발</li>
</ul>
</li>
<li>S/MIME(Secure MIME): 이메일의 내용을 저장하는 방식인 MIME(Multipurpose Internet Mail Extension)에 암호화기법을 추가<ul>
<li>이메일에 암호화 관련 보안성을 제공하는 가장 대표적인 방식 중 하나</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/17dcecfb-bed1-43cf-9d5d-09eb0ed16381/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/466e7990-ade6-4fc6-baa6-d2473e2935be/image.png" /></p>
<hr />
<h2 id="-스니핑-방지-대책-3">• 스니핑 방지 대책</h2>
<ul>
<li>원격 접속을 위한 SSH<ul>
<li>SSH(Secure Shell): 암호화된 원격 접근 방식의 대표적인 예</li>
<li>원격에서 텔넷이나 FTP 등을 이용 → 스니핑을 통해 사용자 ID와 암호가 유출될 수 있음</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6d94707b-b9ed-4a70-8ea3-0f3174855849/image.png" /></p>
<hr />
<h2 id="-스니핑-방지-대책-4">• 스니핑 방지 대책</h2>
<ul>
<li>VPN(Virtual Private Networks) : 사설망 혹은 사설 가상망<ul>
<li>일종의 네트워크 시스템 자체를 의미<ul>
<li>전용망과 VPN으로 구성된 회사 네트워크의 예</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/daf1fefc-52e2-4e04-9e8f-ac5392dbfa44/image.png" /></p>
<ul>
<li>VPN 이용: 공개망을 사용하면서도 전용망을 사용하는 효과<ul>
<li>논리적으로는 전용선을 이용, 물리적으로는 인터넷을 이용</li>
<li>터널링(Tunneling) 기술: 두 종단 사이(End-to-end)에 가상적인 터널 만듦</li>
</ul>
</li>
</ul>
<hr />
<h2 id="-스니핑-방지-대책-5">• 스니핑 방지 대책</h2>
<ul>
<li><p>VPN을 이용한 접근</p>
<ul>
<li>내부망 VPN(Intranet VPN): 두 종단 각각에서 VPN 장비로 접속</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d3d2cb8a-736f-441d-94b5-635c47511585/image.png" /></p>
<ul>
<li>외부접속 VPN Remote Access VPN : 인터넷에서 직접 VPN 장비로 접속하는 경우(=Dial-up VPN)</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/761be1ec-9353-467a-8804-6c4a98437c35/image.png" /></p>
</li>
<li><p>VPN 통신 프로토콜: PPTP/L2F/L2TP, IPSec, SOCKS V5 등</p>
</li>
</ul>
<hr />
<h2 id="-스니핑-방지-대책-6">• 스니핑 방지 대책</h2>
<ul>
<li>스위치의 정적 매핑 테이블 사용<ul>
<li>스위치의 매핑 테이블을 정적(Static)으로 설정<ul>
<li>연결된 PC의 MAC 주소를 미리 조사 → IP 주솟값 등을 고정(Static 혹은 Permanent)</li>
</ul>
</li>
<li>재밍 공격, 스푸핑 공격을 당하더라도 MAC/IP 주솟값이 바뀌지 않아 안전</li>
<li>네트워크 관리자가 일일이 관리해야 하므로 높은 유지보수 비용 발생</li>
</ul>
</li>
</ul>
<table>
<thead>
<tr>
<th><strong>포트</strong></th>
<th><strong>MAC 주소</strong></th>
<th><strong>IP 주소</strong></th>
</tr>
</thead>
<tbody><tr>
<td>1</td>
<td>00:23:69:62:26:09</td>
<td>192.168.1.1</td>
</tr>
<tr>
<td>5</td>
<td>00:00:00:00:cc:10</td>
<td>192.168.1.162</td>
</tr>
<tr>
<td>6</td>
<td>22:22:22:00:cc:01</td>
<td>192.168.1.164</td>
</tr>
</tbody></table>
<hr />
<h2 id="-스니핑-탐지-방법">• 스니핑 탐지 방법</h2>
<ul>
<li>명령어 ping을 이용하는 방법<ul>
<li>존재하지 않는 IP 주소에 대한 요청에도 응답이 오는지 확인<ul>
<li>무차별 모드가 켜져 있는 호스트가 있는 경우<ul>
<li>예) ping 172.16.115.133 → 응답이 없어야 하는데도, 응답이 온다면?</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>ping: 네트워크를 통해 특정한 호스트(Host)까지 접속 가능한지를 테스트하는 명령어</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6198a3c1-d4b4-4b26-a515-83b4b9ca6410/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/30e09151-ccff-4053-9e8f-25d721942eb2/image.png" /></p>
<hr />
<h2 id="-스니핑-탐지-방법-1">• 스니핑 탐지 방법</h2>
<ul>
<li>ARP를 이용하는 방법<ul>
<li>ping을 이용한 방법과 유사한 방법</li>
<li>존재하지 않는 IP 주소를 이용하여 ARP 요청을 보냄
→ 응답 여부를 통해 스니핑 중인지를 판단</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2b52e2ae-2e1d-4504-9a46-66c54583f51d/image.png" /></p>
<hr />
<h2 id="-스니핑-탐지-방법-2">• 스니핑 탐지 방법</h2>
<ul>
<li>DNS 방법<ul>
<li>존재하지 않는 IP를 대상으로 ping을 먼저 보낸 다음, 해당 IP에 대한 도메인 이름을 물어보는 요청(InverseDNS Lookup)이 오는지 확인</li>
<li>원격 네트워크에서도 사용될 수 있음 ( vs. ping을 이용한 방법 – 로컬 네트워크 )</li>
</ul>
</li>
<li>테스트 대상 네트워크로부터 도메인 이름을 물어보는 요청이 오는가?</li>
<li>유인 방법<ul>
<li>일부러 가짜 사용자 ID와 패스워드를 유출<ul>
<li>공격자가 이러한 ID와 패스워드를 사용하게 함</li>
</ul>
</li>
<li>이후 네트워크 감시 프로그램을 이용하여 유출된 ID가 사용되는지를 분석</li>
</ul>
</li>
</ul>
<hr />
<h2 id="-스니핑-탐지-방법-3">• 스니핑 탐지 방법</h2>
<ul>
<li>호스트 기반 탐지</li>
<li>의심이 되는 PC 또는 서버에서 실제 명령을 실행</li>
<li>리눅스나 유닉스에서 ifconfig 명령을 실행</li>
<li>&quot;PROMISC&quot;: 현재 호스트가 무차별 모드로 설정되어 있고 스니핑 가능성 매우 큼</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fc68013b-c2de-4134-b29a-0507f33fa5ae/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/36195726-a82c-4594-9bd3-cdf79d24d6fc/image.png" /></p>
<hr />
<h2 id="-스니핑-탐지-방법-4">• 스니핑 탐지 방법</h2>
<ul>
<li>호스트 기반 탐지</li>
<li>윈도우에서 promiscdetect로 확인(전용 프로그램)</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/10c96cc5-4a57-4395-87df-843957933e5c/image.png" /></p>
<hr />
<h2 id="-스니핑-탐지-방법-5">• 스니핑 탐지 방법</h2>
<ul>
<li>네트워크 기반 탐지 도구: ARP watch<ul>
<li>현재 네트워크의 MAC 주소와 IP 주소에 대한 매핑 정보를 생성</li>
<li>변경이 발생했는지 모니터링 → 변경 시 관리자에게 알림 메일 발송</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/70964285-b1d1-492e-bea0-2bcb58a2b015/image.png" /></p>