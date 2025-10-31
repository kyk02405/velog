# Cloud DX - 20 Network(네트워크)

- 📅 Published: Thu, 23 Oct 2025 09:21:37 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-20-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%ACNetwork)

<hr />
<h1 id="네트워크">네트워크</h1>
<h2 id="네트워크-종류">네트워크 종류</h2>
<h2 id="lan">LAN</h2>
<ul>
<li>외부와 통신이 안되는 구역, 강의실 안
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/aa6b0e60-920e-4bc1-8ac1-41eedf573860/image.png" /></li>
</ul>
<h2 id="wan">WAN</h2>
<ul>
<li>외부와 통신이 되는 구역, 강의실 밖
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c5f0c7ad-e773-4128-9ae6-5c247363f45e/image.png" /></li>
</ul>
<hr />
<h2 id="ispinternet-service-provider">ISP(Internet Service Provider)</h2>
<ul>
<li>회선 제공 업체</li>
<li><code>KT</code>, <code>SKB</code>, <code>LGU++</code></li>
</ul>
<hr />
<h2 id="osi-7-layer">OSI 7 Layer</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/274498c2-0f3e-4947-8f3f-68481805a836/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/dae58f67-8b96-4c9d-a9de-0af334958994/image.png" /></p>
<h3 id="span-style--colorredospanpen-span-style--colorredsspanystems-span-style--colorredispannterconnection개방형-시스템-상호-연결"><span style="color: red;">O</span>pen <span style="color: red;">S</span>ystems <span style="color: red;">I</span>nterconnection(개방형 시스템 상호 연결)</h3>
<ul>
<li><code>Protocol</code>(프로토콜, 통신규악)을 이용한 통신을 계층별로 구분해 놓은 것을 말한다.<h3 id="protocol">Protocol</h3>
</li>
<li>컴퓨터나 네트워크 장비가 서로 통신하기 위해서 미리 정해놓은 약속</li>
</ul>
<hr />
<h1 id="span-style--colorskyblue🌐-layer-1-physical-layer-1계층-물리-계층-장비span"><span style="color: skyblue;">🌐 <strong>Layer 1. Physical Layer (1계층, 물리 계층, 장비)</strong></span></h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b967665f-d902-47bf-ae2d-1e0bf1c003f7/image.png" /></p>
<h2 id="📘-개요">📘 개요</h2>
<ul>
<li><strong>데이터 링크 계층(2계층)</strong> 으로부터 전달받은 <strong>프레임(Frame)</strong> 을
<strong>전송 매체(구리선, 광섬유, 무선 등)</strong> 를 통해 실제로 전송 가능한 <strong>전기적/광학적 신호</strong>로 변환(Encapsulation)합니다.</li>
<li>수신 측에서는 반대로 신호를 다시 데이터 형태로 복원(De-encapsulation)하여
<strong>데이터 링크 계층으로 전달</strong>합니다.</li>
</ul>
<blockquote>
<ul>
<li>MOdulation (변조)</li>
</ul>
</blockquote>
<ul>
<li>DEModulation (복조)</li>
<li><code>MODEM</code> (MOdulation DEModulation)을 생각하면 된다.</li>
</ul>
<hr />
<h2 id="⚙️-주요-기능">⚙️ 주요 기능</h2>
<table>
<thead>
<tr>
<th>기능</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>신호 변환</strong></td>
<td>데이터를 전기, 광, 무선 신호로 변환</td>
</tr>
<tr>
<td><strong>비트 전송 (Bit Transmission)</strong></td>
<td>0과 1의 물리적 전송 단위인 비트 스트림 전달</td>
</tr>
<tr>
<td><strong>전송 매체 정의</strong></td>
<td>케이블 종류, 커넥터, 핀 배열, 주파수 대역 등</td>
</tr>
<tr>
<td><strong>전송 방식 결정</strong></td>
<td>단방향(Simplex), 반이중(Half-duplex), 전이중(Full-duplex) 통신 모드 설정</td>
</tr>
</tbody></table>
<hr />
<h2 id="🔌-주요-장비">🔌 주요 장비</h2>
<table>
<thead>
<tr>
<th>장비</th>
<th>역할</th>
</tr>
</thead>
<tbody><tr>
<td><strong>허브 (Hub)</strong></td>
<td>신호를 단순히 재생/전달하는 장비</td>
</tr>
<tr>
<td><strong>리피터 (Repeater)</strong></td>
<td>감쇠된 신호를 재생하여 전송 거리 연장</td>
</tr>
<tr>
<td><strong>케이블 / 커넥터</strong></td>
<td>UTP, STP, 동축, 광케이블 등 전송 매체</td>
</tr>
<tr>
<td><strong>NIC (Network Interface Card)</strong></td>
<td>컴퓨터를 물리적 네트워크에 연결</td>
</tr>
</tbody></table>
<hr />
<h2 id="📡-전송-매체의-종류">📡 전송 매체의 종류</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th>예시</th>
<th>특징</th>
</tr>
</thead>
<tbody><tr>
<td><strong>유선 매체</strong></td>
<td>UTP, STP, Coaxial, Optical Fiber</td>
<td>전송속도 안정적, 외부 간섭 적음</td>
</tr>
<tr>
<td><strong>무선 매체</strong></td>
<td>Wi-Fi, Bluetooth, 5G</td>
<td>이동성 우수, 간섭 가능성 있음</td>
</tr>
</tbody></table>
<hr />
<h2 id="💬-핵심-포인트">💬 핵심 포인트</h2>
<blockquote>
<p>물리 계층은 <strong>“비트를 신호로 바꿔주는 층”</strong> 이며,
데이터의 <strong>형태나 의미를 알지 못하고</strong> 단순히 신호의 전달만 담당합니다.</p>
</blockquote>
<hr />
<h2 id="기본-장비-및-기타">기본 장비 및 기타</h2>
<ul>
<li><p>Cable, Connector, bit</p>
</li>
<li><p>Unshielded (UTP)</p>
</li>
<li><p>Shielded (STP)</p>
</li>
</ul>
<hr />
<h2 id="케이블-타입">케이블 타입</h2>
<hr />
<h2 id="ethernet-타입">Ethernet 타입</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5a6a9ccb-7372-4758-af07-a962abbb92ea/image.png" /></p>
<h3 id="ethernet">Ethernet</h3>
<ul>
<li>통신을 할 때 사용되는 모든 <code>Interface</code> 통칭한다.</li>
<li><code>WAN</code> [I/F] Card, <code>LAN</code> [I/F] Card, ...</li>
</ul>
<h3 id="10base-5">10Base-5</h3>
<ul>
<li><code>10</code> (10Mbps, 초당 전송 속도, bit per second)</li>
<li><code>Base</code> (Baseband Signal, 기저 대역)</li>
<li><code>5</code> (케이블 타입)</li>
</ul>
<hr />
<h2 id="케이블-연결">케이블 연결</h2>
<h3 id="straight-through-cable">Straight-Through Cable</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/03494312-90e4-4e7e-801c-0b43c55afc44/image.png" /></p>
<ul>
<li>다이렉트 연결 (1:1 연결)</li>
<li>서르 다른 장비간의 연결</li>
</ul>
<hr />
<h3 id="crossover-cable">Crossover Cable</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/37504290-2e48-4fe0-a3fd-69a7b9949849/image.png" /></p>
<ul>
<li><p>크로스 연결</p>
</li>
<li><p>서로 같은 장비간의 연결</p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/29a0e8cd-d959-42a2-a47a-52fe400d6294/image.png" /></p>
</li>
</ul>
<hr />
<h3 id="fiber-optical-connector">Fiber Optical Connector</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/65c351f6-719c-496f-ba66-3bf58d75358d/image.png" /></p>
<hr />
<h1 id="span-style--colorskybluelayer-2-data-link-layer2계층-데이터링크-계층-mac-addressspan"><span style="color: skyblue;">Layer 2. Data-Link Layer(2계층, 데이터링크 계층, MAC Address)</span></h1>
<hr />
<h2 id="개요">개요</h2>
<ul>
<li><code>LAN</code> 구간에서만 사용된다. 즉, 내부망에서만 사용된다.</li>
</ul>
<h2 id="기본-장비-및-기타-1">기본 장비 및 기타</h2>
<ul>
<li><code>Switch</code>(2계층의 대표적인 장비)</li>
<li><span style="color: red;">(핵심)</span><code>MAC Address</code> : <code>(Media Access Control)</code><ul>
<li>데이터를 송수신할 떄 Ehernet이 기억하고 있는 주소를 말한다.</li>
<li><code>MAC Address</code>는 절대 중복될 수가 없고
전세계적으로 유일무이하다.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="span-style--colororangemac-address-구조-eui-48--eui-64-span"><span style="color: orange;">MAC Address 구조 (EUI-48 &amp; EUI-64 )</span></h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cd5550d9-8a80-4bfa-8161-52835b5627b8/image.png" /></p>
<h3 id="개요-1">개요</h3>
<ul>
<li>16진수 구조로 되어 있다.</li>
<li>일반적으로 <code>LAN Card</code>라고 부르는 <code>NIC</code>(Netwrok Interface Card)의 일련번호를 <code>Ethernet</code>의 물리적 주소로 사용한다.</li>
</ul>
<h3 id="ehernet에서-사용되고-있는-mac-address주소">Ehernet에서 사용되고 있는 MAC Address주소</h3>
<ul>
<li><code>EUI-48</code> (48-bit Extended Unique Identifier)</li>
<li><code>EUI-64</code> (64-bit Extended Unique Identifier) </li>
</ul>
<h3 id="분석">분석</h3>
<ul>
<li><h2 id="16진수에-숫자-부여">16진수에 숫자 부여</h2>
</li>
<li><p>16진수를 표현하기 위해 사용되는 bit 갯수는?</p>
</li>
<li><p><code>MAC Address(00-0E-35-05-80-6F)</code></p>
<ul>
<li><code>0000 0000</code> - <code>0000 1110</code> - <code>0011 0101</code> </li>
<li><code>0000 0101</code> - <code>1000 0000</code> - <code>0110 1111</code></li>
</ul>
</li>
<li><p><code>MAC Address</code> 주소 확인</p>
<ul>
<li><code>arp-a (같은 공간 즉, LAN 구간에 있는 PC들의 MAC Address를 확인)</code></li>
<li><code>ipconfig /all (PC의 IP주소 및 MAC Address 확인)</code></li>
<li><code>Linux</code>에서는 <code>ifconfig &lt;이더넷&gt;</code>을 통해 확인 가능</li>
</ul>
</li>
</ul>
<hr />
<h1 id="span-style--colorskybluelayer-3-network-layer3계층-네트워크인터넷-계층-ip-address-span"><span style="color: skyblue;">Layer 3. Network Layer(3계층, 네트워크(인터넷) 계층, IP Address) </span></h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/138640d1-d17e-4d0e-841f-2984cb0eb3dc/image.png" /></p>
<h2 id="개요-2">개요</h2>
<ul>
<li><code>PC</code>에 <code>IP</code>를 부여하기 위한 <code>IP Table</code>을 구성한다.</li>
<li>즉, PC에 <code>IP</code>를 부여하고 인터넷을 할 수 있게 해준다.</li>
<li><span style="color: red;">(핵심)</span>라우터는 <code>내부망(LAN)</code>과 <code>외부망(WAN)</code>이 공존하는 장비이다.</li>
</ul>
<hr />
<h2 id="기본-장비-및-기타-2">기본 장비 및 기타</h2>
<ul>
<li><code>Router</code>(3계층의 대표적인 장비)</li>
<li><code>IP Address</code>, <code>ICMP</code>, <code>IGMP</code>, <code>ARP</code>, <code>RARP</code></li>
</ul>
<hr />
<h2 id="ip-class-scope-class-별-분석">IP Class Scope (Class 별 분석)</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a85e8b47-933e-4eb5-83d4-1573eb75145b/image.png" /></p>
<h3 id="span-style--colororangeipv4internet-protocl-version-4span"><span style="color: orange;">IPv4(Internet Protocl version 4)</span></h3>
<ul>
<li><code>8bit</code>(octect,옥텟) x 4자리 = <code>32bit</code> 주소체계</li>
<li>각 옥텟은 <code>.</code>으로 구분</li>
</ul>
<h3 id="span-style--colororangeipv6internet-protocl-version-6span"><span style="color: orange;">IPv6(Internet Protocl version 6)</span></h3>
<ul>
<li><code>16bit</code> x 8자리 = <code>128bit</code> 주소체계</li>
<li>각 영역은 <code>:</code> 으로 구분</li>
</ul>
<hr />
<h2 id="class별-subnet-mask">Class별 Subnet Mask</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6692e444-06c4-4399-83f3-2bd126cb34d4/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/067b6d47-bc94-49af-917c-685b6ca58070/image.png" /></p>
<h3 id="개요-3">개요</h3>
<ul>
<li><code>Network ID</code>영역과 <code>Host ID</code>영역을 구분하는 역할</li>
<li><code>Network ID</code>영역<ul>
<li>대역을 구분한다</li>
</ul>
</li>
<li><code>Host ID</code>영역<ul>
<li><code>PC(호스트)</code>에 부여할 IP주소의 갯수를 구분한다.</li>
</ul>
</li>
</ul>
<h3 id="각-대역별-subnet-mask">각 대역별 Subnet Mask</h3>
<ul>
<li><code>Class A (255.0.0.0)</code></li>
<li><code>Class B (255.255.0.0)</code></li>
<li><code>Class C (255.255.255.0)</code></li>
</ul>
<hr />
<h1 id="span-style--colorskybluelayer-4-transport-layer4계층-전송-계층-tcpipspan"><span style="color: skyblue;">Layer 4. Transport Layer(4계층, 전송 계층, TCP/IP)</span></h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6521dbc5-4f6f-4371-b7e3-d99d145dd50f/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/368b5447-a991-4503-8bc6-fc0e3dc01f98/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/34dd4acb-85f3-471d-92e7-e425b1089055/image.png" /></p>
<h2 id="개요-4">개요</h2>
<ul>
<li>사용자 간 데이터의 투명한(신뢰성을 기반으로 한) 전송을 제공(TCP)하고 상위 계층에 신뢰성 있는 데이터를 전송하는 서비스를 제공한다.</li>
</ul>
<h2 id="기본-장비-및-기타-3">기본 장비 및 기타</h2>
<h3 id="udp">UDP</h3>
<ul>
<li>데이터 전송 시 빠른 전송 서비스를 요구하는 음성, 영상 데이터의 전송에 적합한 통신 프로토콜이다.</li>
</ul>
<h3 id="tcp">TCP</h3>
<hr />
<h1 id="span-style--colorskybluelayer-5--7-sessionpresentation-application-layer-5계층연결-6계층표현-7계층응용span"><span style="color: skyblue;">Layer 5 ~ 7. Session/Presentation/ Application Layer (5계층(연결), 6계층(표현), 7계층(응용))</span></h1>
<h2 id="개요-5">개요</h2>
<ul>
<li>대부분 <code>서비스(서버에서의 서비스)</code>에 관련된 계층</li>
</ul>
<hr />
<h1 id="span-style--colorskybluesubnetingspan"><span style="color: skyblue;">Subneting</span></h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c752ca45-42b3-44d0-b1d2-3c2eb5d30202/image.png" /></p>
<h2 id="개요-6">개요</h2>
<ul>
<li><p><code>Broadcast Domain</code>에 많은 호스트가 연결된 경우 호스트에 발생한 <code>Broadcast traffic</code>이 모든 호스트에 전달되어 많은 Broadcast Traffic이 발생하며 하나의 Broadcast Domain에서는 보안이 취약하기 때문에 Firewall이나 ACL과 같은 정책을 구현하기 위해서는 Network Segment를 나누는 것이 효율적이다. </p>
</li>
<li><p>ISP업체에서는 회선을 임대한 기업들에 <code>IP</code>를 할당하기 위하여 <code>Subnetting</code>을 한 후에 <code>IP</code>를 할당하여 주소를 절약한다.</p>
</li>
<li><p>하나의 네트워크를 필요한 만큼의 IP대역으로분할, 배포하는 기술을 말한다.</p>
</li>
<li><p>남아 도는(잉여) 또는 사용하지 않는 <code>IP</code>를 필요한 곳에서 사용할 수 있도록 재배포하는 기술을 말한다.</p>
</li>
</ul>
<h2 id="pdf-module-0-42p--43p">PDF Module 0. 42p ~ 43p</h2>
<h3 id="초기-확인-작업">초기 확인 작업</h3>
<ul>
<li><p>Step 1. 주어진 대역<code>(218.128.32.0/24)</code></p>
</li>
<li><p>Step 2. 주어진 대역의 Class (Class C) </p>
</li>
<li><p>Step 3. 확인된 Class에 맞는 Subnet Mask (255.255.255.0)</p>
</li>
<li><p>Step 4. 한 대역당 사용하고자 하는 Host수 (25개)</p>
</li>
</ul>
<h3 id="분석-1">분석</h3>
<h3 id="계산-요령">계산 요령</h3>
<ul>
<li>각 대역별 Subnet Mask<ul>
<li>기본 SM(변하지 않는 옥텟).<code>서브넷 갯수</code>의 각 bit에 할당된 값의 합</li>
<li><code>255</code>.<code>255</code>.<code>255</code>.(<code>224</code>=128+64+32)</li>
</ul>
</li>
<li>CIDR 표기 <ul>
<li>&lt;각 대역별 첫 번째 주소&gt;/&lt;사용하지 않는 옥텟의 bit합)+<code>서브넷 갯수</code>에 할당된 bit수&gt;</li>
<li>218.128.32.0/(8+8+8+3)27</li>
</ul>
</li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bb62cf12-f49e-4a74-8169-bc93a0911ae1/image.png" /></p>
<h2 id="실습-1-21812832024-네트워크를-각-네트워크-당-25개의-host가-사용할-수-있도록-subneting-하시오">실습 1. 218.128.32.0/24 네트워크를 각 네트워크 당 25개의 Host가 사용할 수 있도록 Subneting 하시오</h2>
<ul>
<li>각 대역별 Subnet Mask는? 255.255.255.224</li>
<li>Subnet의 갯수 8개 </li>
<li>한 대역당 실제 사용 가능한 Host의 개수 ? 30개 (32-2)<ul>
<li>Network ID (각 대역별 첫 번째 주소)</li>
<li>Broadcast (각 대역별 마지막 주소)</li>
</ul>
</li>
<li>마지막 Subnet의 Network-ID는 218.128.32.224</li>
<li>첫번째 Subnet의 Broadcast는 218.128.32.31</li>
<li>두번째 Subnet의 사용 가능한 IP 범위는?  218.128.32.33 ~ 218.128.32.62</li>
</ul>
<hr />
<h2 id="실습-2-19516812024-네트워크를-8개의-네트워크로-사용할-수-있도록-subneting-하시오">실습 2. '195.168.12.0/24' 네트워크를 '8개'의 네트워크로 사용할 수 있도록 Subneting 하시오.</h2>
<ul>
<li>각 대역별 Subnet Mask는? 255.255.255.224</li>
<li>Subnet의 갯수 8개 </li>
<li>한 대역당 실제 사용 가능한 Host의 개수 ? 30개 (32-2)<ul>
<li>Network ID (각 대역별 첫 번째 주소)</li>
<li>Broadcast (각 대역별 마지막 주소)</li>
</ul>
</li>
<li>마지막 Subnet의 Network-ID는 195.168.12.224</li>
<li>첫번째 Subnet의 Broadcast는 195.168.12.0</li>
<li>두번째 Subnet의 사용 가능한 IP 범위는?  195.168.12.33 ~ 195.168.12.62</li>
</ul>
<hr />
<h2 id="실습-3-2058110024-네트워크를-7개의-네트워크로-사용할-수-있도록-subneting-하시오">실습 3. '205.81.10.0/24' 네트워크를 '7개'의 네트워크로 사용할 수 있도록 Subneting 하시오.</h2>
<ul>
<li>각 대역별 Subnet Mask는? 255.255.255.224</li>
<li>Subnet의 갯수 8개 </li>
<li>한 대역당 실제 사용 가능한 Host의 개수 ? 30개 (32-2)<ul>
<li>Network ID (각 대역별 첫 번째 주소)</li>
<li>Broadcast (각 대역별 마지막 주소)</li>
</ul>
</li>
<li>마지막 Subnet의 Network-ID는 205.81.10.224</li>
<li>첫번째 Subnet의 Broadcast는 195.168.12.0</li>
<li>두번째 Subnet의 사용 가능한 IP 범위는?  205.81.10.33 ~ 205.81.10.62</li>
</ul>
<hr />
<h2 id="실습-4-21110010024-네트워크를-각-네트워크-당-60개의-host가-사용할-수-있도록-subneting-하시오">실습 4. '211.100.10.0/24' 네트워크를 각 네트워크 당 '60개'의 Host가 사용할 수 있도록 Subneting 하시오.</h2>
<h3 id="확인-작업">확인 작업</h3>
<ul>
<li>C Class / 255.255.255.0 / 60개</li>
</ul>
<h3 id="분석-2">분석</h3>
<pre><code> \&lt;서브넷 갯수\&gt; &lt;호스트 갯수&gt;</code></pre><p>8+8+8 128 64 32 16 8 4 2 1
        0 0 </p>
<ul>
<li>각 대역별 Subnet Mask는? 255.255.255.224</li>
<li>Subnet의 갯수 3개 </li>
<li>한 대역당 실제 사용 가능한 Host의 개수 ? 62 (64-2)<ul>
<li>Network ID (각 대역별 첫 번째 주소)</li>
<li>Broadcast (각 대역별 마지막 주소)</li>
</ul>
</li>
<li>마지막 Subnet의 Network-ID는 211.100.10.224</li>
<li>첫번째 Subnet의 Broadcast는 211.100.10.0</li>
<li>두번째 Subnet의 사용 가능한 IP 범위는?  211.100.10.33 ~ 211.100.10.62</li>
</ul>
<hr />
<h2 id="실습-5-152061024-네트워크를-각-네트워크-당-100개의-host가-사용할-수-있도록-subneting-하시오">실습 5. '152.0.61.0/24' 네트워크를 각 네트워크 당 '100개'의 Host가 사용할 수 있도록 Subneting 하시오.</h2>
<ul>
<li>각 대역별 Subnet Mask는? 255.255.255.128 /25</li>
<li>Subnet의 갯수 2개 </li>
<li>한 대역당 실제 사용 가능한 Host의 개수 ? 126개 (128-2)<ul>
<li>Network ID (각 대역별 첫 번째 주소)</li>
<li>Broadcast (각 대역별 마지막 주소)</li>
</ul>
</li>
<li>마지막 Subnet의 Network-ID는 152.0.61.128</li>
<li>첫번째 Subnet의 Broadcast 주소는 152.0.61.127</li>
<li>두번째 Subnet의 사용 가능한 IP 범위는?  152.0.61.129 ~ 152.0.61.254</li>
</ul>
<hr />
<h2 id="실습-6-1891017024-네트워크를-각-네트워크-당-50개의-host가-사용할-수-있도록-subneting-하시오">실습 6. '189.101.7.0/24' 네트워크를 각 네트워크 당 '50개'의 Host가 사용할 수 있도록 Subneting 하시오.</h2>
<ul>
<li>각 대역별 Subnet Mask는? 255.255.255.192 /26</li>
<li>Subnet의 갯수 4개 </li>
<li>한 대역당 실제 사용 가능한 Host의 개수 ? 62 (64-2)<ul>
<li>Network ID (각 대역별 첫 번째 주소)</li>
<li>Broadcast (각 대역별 마지막 주소)</li>
</ul>
</li>
<li>마지막 Subnet의 Network-ID는 189.101.7.192</li>
<li>첫번째 Subnet의 Broadcast 주소는 </li>
</ul>
<p>189.101.7.63</p>
<ul>
<li>두번째 Subnet의 사용 가능한 IP 범위는?  189.101.7.65 ~ 189.101.7.126</li>
</ul>
<hr />
<h2 id="실습-7-151920016-네트워크를-각-네트워크-당-6500개의-host가-사용할-수-있도로-subneting-하시오">실습 7. '151.92.0.0/16' 네트워크를 각 네트워크 당 '6500개'의 Host가 사용할 수 있도로 Subneting 하시오.</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7992d08b-70c4-42d8-81e1-ab65eacdf18e/image.png" /></p>
<ul>
<li>각 대역별 Subnet Mask는? 255.255.224.0 /19</li>
<li>Subnet의 갯수 8개 </li>
<li>한 대역당 실제 사용 가능한 Host의 개수 ? 8190(8192-2)<ul>
<li>Network ID (각 대역별 첫 번째 주소)</li>
<li>Broadcast (각 대역별 마지막 주소)</li>
</ul>
</li>
<li>마지막 Subnet의 Network-ID는 151.92.224.0</li>
<li>첫번째 Subnet의 Broadcast 주소는 </li>
</ul>
<p>151.92.63.255</p>
<ul>
<li>두번째 Subnet의 사용 가능한 IP 범위는?  151.92.32.1 ~ 151.92.63.254</li>
</ul>
<p>128 64 32 16 8 4 2 </p>
<hr />
<h2 id="실습-8-152061016-네트워크를-각-네트워크-당-200개의-host가-사용할-수-있도록-subneting-하시오">실습 8. '152.0.61.0/16' 네트워크를 각 네트워크 당 '200개'의 Host가 사용할 수 있도록 Subneting 하시오.</h2>
<pre><code class="language-bash">   ; 분석

                       &lt;SN갯수&gt;            &lt;호스트갯수&gt;
     8+8+   128  64  32(8192)  16(4096)  8(2048)  4(1024)  2(512)  1(256)  |  128  64  32  16  8  4  2  1

   00000000   00000000 ~ 11111111   152.0.0.0 ~ 152.0.0.255      255.255.255.0   /24
   00000001            152.0.1.0 ~ 152.0.1.255
   00000010            152.0.2.0 ~ 152.0.2.255
   00000011            152.0.3.0 ~ 152.0.3.255
   ...
   11111110            152.0.254.0 ~ 152.0.254.255
   11111111            152.0.255.0 ~ 152.0.255.255</code></pre>
<ul>
<li>각 대역별 Subnet Mask는? 255.255.255.0 /24</li>
<li>Subnet의 갯수 256개 </li>
<li>한 대역당 실제 사용 가능한 Host의 개수 ? 254(256-2)<ul>
<li>Network ID (각 대역별 첫 번째 주소)</li>
<li>Broadcast (각 대역별 마지막 주소)</li>
</ul>
</li>
<li>마지막 Subnet의 Network-ID는 152.0.255.0</li>
<li>첫번째 Subnet의 Broadcast 주소는 </li>
</ul>
<p>152.0.0.255</p>
<ul>
<li>두번째 Subnet의 사용 가능한 IP 범위는?  152.0.1.1 ~ 152.0.1.254</li>
</ul>
<hr />
<h2 id="실습-9-152061016-네트워크를-각-네트워크-당-100개의-host가-사용할-수-있도록-subneting-하시오">실습 9. '152.0.61.0/16' 네트워크를 각 네트워크 당 '100개'의 Host가 사용할 수 있도록 Subneting 하시오.</h2>
<pre><code class="language-bash">   ; 분석

                       &lt;SN갯수&gt;            &lt;호스트갯수&gt;
     8+8+   128  64  32(8192)  16(4096)  8(2048)  4(1024)  2(512)  1(256)  .  128 | 64  32  16  8  4  2  1

   00000000 0    0000000 ~ 1111111   152.0.0.0 ~ 152.0.0.127      255.255.255.128   /25
   00000000 1            152.0.0.128 ~ 152.0.0.255
   00000001 0            152.0.1.0 ~ 152.0.1.127
   00000001 1            152.0.1.128 ~ 152.0.1.255
   00000010 0            152.0.2.0 ~ 152.0.0.127
   ...
   11111111 0            152.0.255.0 ~ 152.0.255.127
   11111111 1            152.0.255.128 ~ 152.0.255.255</code></pre>
<ul>
<li>각 대역별 Subnet Mask는? 255.255.255.128 /25</li>
<li>Subnet의 갯수 512개 </li>
<li>한 대역당 실제 사용 가능한 Host의 개수 ? 126(128-2)<ul>
<li>Network ID (각 대역별 첫 번째 주소)</li>
<li>Broadcast (각 대역별 마지막 주소)</li>
</ul>
</li>
<li>마지막 Subnet의 Network-ID는 152.0.255.128</li>
<li>첫번째 Subnet의 Broadcast 주소는 </li>
</ul>
<p>152.0.0.127</p>
<ul>
<li>두번째 Subnet의 사용 가능한 IP 범위는?  152.0.0.129 ~ 152.0.0.254</li>
</ul>
<hr />
<h2 id="실습-10-1891017016-네트워크를-각-네트워크-당-50의-host가-사용할-수-있도록-subneting-하시오">실습 10. '189.101.7.0/16' 네트워크를 각 네트워크 당 '50'의 Host가 사용할 수 있도록 Subneting 하시오.</h2>
<ul>
<li>각 대역별 Subnet Mask는? 255.255.255.192 /26</li>
<li>Subnet의 갯수 1024개 </li>
<li>한 대역당 실제 사용 가능한 Host의 개수 ? 62(64-2)<ul>
<li>Network ID (각 대역별 첫 번째 주소)</li>
<li>Broadcast (각 대역별 마지막 주소)</li>
</ul>
</li>
<li>마지막 Subnet의 Network-ID는 189.101.255.1</li>
<li>첫번째 Subnet의 Broadcast 주소는 </li>
</ul>
<p>189.101.0.63</p>
<ul>
<li>두번째 Subnet의 사용 가능한 IP 범위는?  189.101.0.65 ~ 189.101.0.126</li>
</ul>
<hr />
<h1 id="실습-11-154062016-네트워크를-각-네트워크-당-1300개의-host가-사용할-수-있도록-subneting-하시오">실습 11. '154.0.62.0/16' 네트워크를 각 네트워크 당 '1300개'의 Host가 사용할 수 있도록 Subneting 하시오.</h1>
<pre><code class="language-bash">   ; 분석

                       &lt;SN갯수&gt;            &lt;호스트갯수&gt;
     8+8+   128  64  32(8192)  16(4096)  8(2048)  | 4(1024)  2(512)  1(256)  .  128  64  32  16  8  4  2  1</code></pre>
<ul>
<li>각 대역별 Subnet Mask는? 255.255.255.192 /26</li>
<li>Subnet의 갯수 32개 </li>
<li>한 대역당 실제 사용 가능한 Host의 개수 ? 2046(2048-2)<ul>
<li>Network ID (각 대역별 첫 번째 주소)</li>
<li>Broadcast (각 대역별 마지막 주소)</li>
</ul>
</li>
<li>마지막 Subnet의 Network-ID는 154.0.248.0</li>
<li>첫번째 Subnet의 Broadcast 주소는 </li>
</ul>
<p>154.0.7.255</p>
<ul>
<li>두번째 Subnet의 사용 가능한 IP 범위는?  154.0.8.1 ~ 154.0.15.254</li>
</ul>
<hr />
<h1 id="vlsm-variable-length-subnet-mask">VLSM (Variable Length Subnet Mask)</h1>
<h2 id="개요-7">개요</h2>
<ul>
<li>VLSM variable-length subnet mask(가변 길이 서브넷 마스크)의 약어. </li>
<li>서로 다른 서브넷에서 동일한 네트워크 번호로 다른 서브넷 마스크를 지정할 수 있는 특성.  </li>
<li>VLSM은 가용 주소 공간을 최적화하는데 도움이 된다.</li>
<li>서브네팅 한 임의의 한 개 대역을 또 한 번 서브넷팅 하는 것을 말한다.</li>
</ul>
<hr />
<h2 id="실습-1-46페이지">실습 1. 46페이지</h2>
<h3 id="step-1-원래-대역-찾기">Step 1. 원래 대역 찾기</h3>
<ul>
<li><p><code>192.168.20.192/27</code>을 이용하면 어떤 대역을 서브넷팅 했는지 알 수가 있다.</p>
</li>
<li><p><code>/27</code>은 <code>서브넷 갯수</code>를 알 수 있고 또한 <code>32-27=5</code> 이기 때문에 
<code>호스트 갯수</code>는 <code>5bit</code>가 된다.</p>
</li>
<li><p>따라서 <code>128 64 32 | 16 8 4 2 1</code>과 같이 원대역을 유추할 수 있기 때문에 
원대역은 <code>192.168.20.20/24</code>이고 8개 대역으로 서브넷팅한 것을 알 수 있다.</p>
</li>
</ul>
<hr />
<h3 id="step-2-1921682019227-vlsm-구성">Step 2. <code>192.168.20.192/27</code> VLSM 구성</h3>
<pre><code class="language-bash">                        255.255.255.252   /30
   8+8+8+   128  64  32  ||  16  8  4  |  2  1
      110   000   00 ~ 11      192.168.20.192 ~ 192.168.20.195
      110   001         192.168.20.196 ~ 192.168.20.199
      110   010         192.168.20.200 ~ 192.168.20.203
      110   011         192.168.20.204 ~ 192.168.20.207
      110   100         192.168.20.208 ~ 192.168.20.211
      110   101         192.168.20.212 ~ 192.168.20.215
      110   110         192.168.20.216 ~ 192.168.20.219
      110   111         192.168.20.220 ~ 192.168.20.223</code></pre>
<hr />