# Cloud DX - 39 패킷분석, 네트워크 해킹 절차 및 호스트 식별, Port Scanning

- 📅 Published: Wed, 19 Nov 2025 04:11:09 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-39-%ED%8C%A8%ED%82%B7%EB%B6%84%EC%84%9D-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%ED%95%B4%ED%82%B9-%EC%A0%88%EC%B0%A8-%EB%B0%8F-%ED%98%B8%EC%8A%A4%ED%8A%B8-%EC%8B%9D%EB%B3%84-Port-Scanning)

<hr />
<h1 id="span-style--colorskyblue02-패킷-분석-with-wiresharkspan"><span style="color: skyblue;">02. 패킷 분석 (with WireShark)</span></h1>
<h2 id="wireshark를-이용한-패킷-분석">WireShark를 이용한 패킷 분석</h2>
<h2 id="실습-1-데이터-링크2계층-패킷-분석">실습 1. 데이터 링크(2계층) 패킷 분석</h2>
<h3 id="실습-환경">실습 환경</h3>
<ul>
<li><p>Windows 10</p>
<ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
<li><p>Windows Server 2002 with IIS 웹서버</p>
<ul>
<li><code>192.168.10.132</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
<li><p><code>IIS</code> 다운 후에 <code>Host-only</code>로 변경</p>
<h3 id="통신-테스트">통신 테스트</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b7039d87-3553-41f8-b26d-dfa6c5dec279/image.png" /></p>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a783942d-1886-42eb-b629-239c4abce07f/image.png" /></p>
<h3 id="패킷-캡쳐-준비">패킷 캡쳐 준비</h3>
<ul>
<li><code>Windows Server 2022</code>에서 <code>IIS 웹서버</code> 추가 후 활성화</li>
<li>각 시스템에서 웹 브라우저를 통한 사이트 출력(IIS Test Page)
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ca088a48-56f7-4601-986f-1f041241a923/image.png" /></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e562c2ed-1a64-4ed0-9775-8a2b617ce1a2/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b97647b2-8727-4f92-b360-844da9d4ad8f/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d1536b82-e76e-46db-95de-70c5969e1b8f/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ad3fae71-1209-4b73-80a8-4e7e13edf6da/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0ed6f45a-a97e-4216-a4a4-9bf5139c162e/image.png" /></p>
<ul>
<li><p><code>Wireshark</code> 설치 및 실행</p>
</li>
<li><p>패킷 캡처</p>
<ul>
<li><p>각 시스템 별 <code>MAC Address</code> 확인</p>
<ul>
<li><code>Server</code> <code>00-0C-29-48-1A-CC</code></li>
<li><code>Client</code> <code>00-0C-29-B9-16-EA</code></li>
</ul>
</li>
<li><p>각 시스템에서 샥스핀을 실행</p>
<ul>
<li><code>Ethernet</code> 접속 후 중지</li>
<li>이 창 띄우고 대기<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d4c7384a-0e69-4e72-833e-b8e08005a933/image.png" /></li>
</ul>
</li>
<li><p><code>Client</code>에서 웹브라우저를 통해서 <code>Server</code>의 주소로 접속 시도</p>
<ul>
<li><code>Clinet</code> , <code>Server</code> 에서 <code>저장하지 않고 계속</code> 클릭 후 웹 접속</li>
<li>이후 <code>패킷 수집</code> 중지</li>
</ul>
</li>
</ul>
</li>
<li><p>패킷 분석</p>
<ul>
<li><p>일반 분석</p>
<ul>
<li><p>캡처</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/80200f7c-d9e3-41fe-aee8-3e07600fe6ad/image.png" /></li>
</ul>
</li>
<li><p>라인별 분석</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/abdcdd7d-bd5a-41cf-ba72-b623fcb5b71c/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="실습-2-네트워크-계층3계층-ip-address-패킷-분석">실습 2. 네트워크 계층(3계층, IP Address) 패킷 분석</h2>
<h3 id="실습-환경-1">실습 환경</h3>
<ul>
<li>Windows Server 시스템 4대 로딩</li>
<li>로딩 후 <code>Client100</code>과 <code>Client200</code>끼리 통신되는지 확인</li>
<li>패킷 분석은 라우터 역할을 하는 <code>SRV100</code>과 <code>SRV200</code>에서만 하면된다.</li>
</ul>
<h3 id="작업-순서">작업 순서</h3>
<ul>
<li><code>SRV100</code>과 <code>SRV200</code>을 <code>wireshark</code> 실행할 때 <code>I/F</code> <code>외부망</code>으로 </li>
<li><code>Clinet100</code>에서 <code>Client200</code>으로 <code>ping</code> 테스트 (with <code>-t</code> 옵션)</li>
</ul>
<hr />
<h1 id="span-style--colorskyblue03-네트워크-해킹-절차-및-호스트-식별span"><span style="color: skyblue;">03. 네트워크 해킹 절차 및 호스트 식별</span></h1>
<h2 id="31-활성화비활성화-된-호스트-식별">3.1 활성화/비활성화 된 호스트 식별</h2>
<h3 id="네트워크-환경위치에-따른-식별-유형">네트워크 환경(위치)에 따른 식별 유형</h3>
<ul>
<li><p>같은 네트워크 안에 있는 경우</p>
<ul>
<li>같은 MAC Address로 ARP를 보낸 경우에 확인 가능</li>
</ul>
</li>
<li><p>다른 네트워크 안에 있는 경우</p>
<ul>
<li>라우터 밖에 있는 경우</li>
</ul>
</li>
<li><p>ICMP로 확인 가능 (외부망 WAN)</p>
<ul>
<li>라우터 안에 있는 경우</li>
</ul>
</li>
<li><p>ARP로 확인 가능 (내부망 LAN)</p>
</li>
</ul>
<h3 id="실습-환경-구성">실습 환경 구성</h3>
<h3 id="실습">실습</h3>
<ul>
<li><p>실습 1. 로컬 테스트</p>
<ul>
<li><p>테스트 1. LAN 구간에서의 통신</p>
</li>
<li><p>명령</p>
<ul>
<li><p>SRV100 내부망에서 Client100으로 ping 명령을 때린 후 Client100에서 샥스핀으로 확인</p>
</li>
<li><p>결과</p>
<ul>
<li><p>ICMP 필터링 결과</p>
<ul>
<li><code>192.168.100.10    192.168.100.20    ICMP    74    Echo (ping) request  id=0x0001, seq=48/12288, ttl=128 (reply in 2)</code></li>
<li><code>192.168.100.20    192.168.100.10    ICMP    74    Echo (ping) reply    id=0x0001, seq=48/12288, ttl=64 (request in 1)</code></li>
</ul>
</li>
<li><p>출발지가 <code>Windows</code>면 <code>TTL</code>이 128 <code>Linux</code>면 <code>TTL</code>이 64</p>
</li>
</ul>
</li>
<li><p>ARP 필터링 결과</p>
<ul>
<li><code>Vmware_b0:8f:47    Vmware_5f:25:13    ARP    42    Who has 192.168.100.10?  Tell 192.168.100.20</code></li>
<li><code>Vmware_5f:25:13    Vmware_b0:8f:47    ARP    60    192.168.100.10 is at 00:0c:29:5f:25:13</code></li>
</ul>
</li>
</ul>
</li>
<li><p>테스트 2. WAN 구간에서의 통신</p>
</li>
<li><p>명령
 <code>Client200</code>에서 <code>Client100</code>으로 ping 명령을 때린 후 `Client100'에서 샥스핀으로 확인</p>
</li>
<li><p><code>Client200</code>에서 <code>MAC Address</code>를 확인하고 `Client100'에서의 샥스핀에 올라온 것과 비교</p>
<ul>
<li><p>결과</p>
</li>
<li><p>ICMP 필터링 결과</p>
<ul>
<li><p><code>1    0.000000000    192.168.200.20    192.168.100.20    ICMP    74    Echo (ping) request  id=0x0001, seq=7/1792, ttl=128</code></p>
</li>
<li><p><code>2    0.000320984    192.168.200.20    192.168.100.20    ICMP    74    Echo (ping) request  id=0x0001, seq=7/1792, ttl=126 (reply in 3)</code></p>
</li>
<li><p><code>3    0.000357193    192.168.100.20    192.168.200.20    ICMP    74    Echo (ping) reply    id=0x0001, seq=7/1792, ttl=64 (request in 2)</code></p>
</li>
<li><p><code>4    0.000683448    192.168.100.20    192.168.200.20    ICMP    74    Echo (ping) reply    id=0x0001, seq=7/1792, ttl=62</code></p>
</li>
<li><p><code>ARP</code>는 내부망만 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c5c7c0f0-f8bb-4626-ac3e-342869d5edfa/image.png" /></p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="결론">결론</h3>
<ul>
<li><p>각 <code>Client</code>에서 <code>ping</code>을 때린 후 <code>SRV/xxx</code>의 내부망과 하단에 있는 <code>Client</code>의 화면에만 MAC <code>Address</code>를 확인할 수가 있다.</p>
</li>
<li><p>외부 = <code>ICMP</code></p>
</li>
<li><p>내부 = <code>ARP</code></p>
</li>
</ul>
<hr />
<h2 id="32-네트워크-해킹-절차-및-정보수집을-위한-명령어-tool">3.2 네트워크 해킹 절차 및 정보수집을 위한 명령어 Tool</h2>
<h2 id="ping">ping</h2>
<h3 id="개요">개요</h3>
<ul>
<li>침투 테스트 범위에 있는 IP주소를 목록화하고 현재 동작중인 시스템을 확인한다.</li>
<li><span style="color: red;">(권장)</span> 보안상 문제(신뢰성)가 있고 IP로의 공격 범위를 제공하기 때문에 <code>차단</code>하는 것이 좋다.</li>
<li><span style="color: red;">(핵심)</span> 가장 큰 문제점으로는, 시스템의 네트워크에 과부하를 초래할 수 있다.</li>
</ul>
<h3 id="사용되는-패킷">사용되는 패킷</h3>
<ul>
<li><code>ICMP</code> <code>(TTL)</code></li>
<li><code>echo Request Packet</code> <code>(TTL)</code><ul>
<li><code>Linux/Unix</code> (64byte)</li>
<li><code>Windows</code> (32byte / 128byte)</li>
</ul>
</li>
<li><code>echo Response(Reply) Packet</code> <code>(TTL)</code><ul>
<li><code>Linux/Unix</code> (64byte)</li>
<li><code>Windows</code> (128byte)</li>
<li>그 밖에 (256byte)</li>
</ul>
</li>
<li><code>ping</code> 명령을 실행한 후 출력되는 내용은 모두 <code>Response(응답)</code> 내용을 보여주고 있다.</li>
<li>출력되는 내용 중에 <code>TTL</code>이 <code>echo Response(응답) Packet (TTL)</code>에서 언급한 내용과 다른 값을 보여주는데</li>
<li>이는 해당 대역에 있는 <code>Gateway</code>주소가 빠진 값을 보여주고 있는 것이다.</li>
</ul>
<h3 id="실습-1-개요-및-특징의-항목에-대한-대응방안">실습 1. 개요 및 특징의 항목에 대한 대응방안</h3>
<ul>
<li><p><code>테스트 1.</code> <code>Host OS</code>에서의 대응방안</p>
<ul>
<li>IP로의 공격 범위를 제공하기 때문에 차단하는 것이 좋다. </li>
<li><code>Host OS</code>에서 작업한다.<ul>
<li>(wf.msc에서 다음의 2가지 사항을 조치하면 된다.)</li>
<li>인바운드 규칙의 <code>파일 및 프린터 공유</code>의 규칙 사용을 해제한다.</li>
<li>ICMPv4의 <code>반향 요청</code>이 있다면 체크를 해제한다. 기본적으로 이 기능은 비활성 상태이다. </li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/96bd5f88-f0d0-4385-bbe5-21aceb5240ae/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5299e6f3-7104-420f-b0cf-8cfd1ed23c69/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/314c2caa-f8c9-4d79-a239-d8ea7bde53b0/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p><code>테스트 2.</code> <code>시스템의 네트워크에 과부하를 초래할 수 있다.</code></p>
<ul>
<li><p>실습 환경<code>(Host-only)</code></p>
<ul>
<li>실제 <code>공인 IP</code>를 이용해서 설정한 상태일 때<ul>
<li><code>Host OS(Windows 10)</code>에서 <code>외부의 시스템(www.samadal.com)</code>으로의 테스트를 시도한다.</li>
</ul>
</li>
<li><code>가상 머신</code>을 이용해서 설정한 상태일 때<ul>
<li><code>CentOS 7.9.2209</code> / <code>Rocky 9.6</code> with DNS Server (gusiya.com)<ul>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li><code>Windows 10</code><ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.131</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li><code>Network Adapter</code>는 모두 <code>Host-only</code>로 구성한다. </li>
<li>테스트 1. <code>Windows 10</code>에서 <code>ping</code> 요청 시 <code>응답 가능</code></li>
</ul>
</li>
<li><code>(rocky96)# echo 0 &gt; /proc/sys/net/ipv4/icmp_echo_ignore_all</code></li>
<li><code>(win10) ping www.gusiya.com</code></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/dc516ad5-41d9-46d1-9404-dc6996c76506/image.png" /></li>
</ul>
<ul>
<li>테스트 2. 'Windows 10'에서 'ping' 요청 시 '응답 불가능'<ul>
<li><code>(rocky96)# echo 1 &gt; /proc/sys/net/ipv4/icmp_echo_ignore_all</code></li>
<li><code>(win10) ping www.gusiya.com</code></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/18313904-b4ec-40f3-893e-32ecb848b378/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="실습-2-echo-packet">실습 2. Echo Packet</h3>
<h4 id="실습-환경-2">실습 환경</h4>
<ul>
<li><p><code>Kali</code></p>
<ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
<li><p><code>Windows 10</code></p>
<ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
</ul>
<h4 id="테스트-1-echo-request-패킷과-echo-response-패킷">테스트 1. echo Request 패킷과 echo Response 패킷</h4>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/626d9666-ce39-4e7a-a23c-dbacb933c2d1/image.png" /></p>
</li>
<li><p>앞에서 언급한 <code>사용되는 패킷</code>을 참고하면 된다.</p>
</li>
<li><p>샥스핀의 하단에 있는 송수신 패킷들을 한 개씩 클릭한 상태에서 하단에 있는 <code>세부항목</code>을 확인해보면</p>
</li>
<li><p><code>Linux (kali)</code>이기에 <code>64</code>가, <code>수신부</code>는 <code>Windows</code>이기에 <code>128</code>이 출력되는 것을 알 수 있다.</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b938f5f5-cdac-4839-a1d6-5004d53c46a0/image.png" /></li>
</ul>
</li>
</ul>
<h4 id="테스트-2-echo-request-패킷과-echo-response-패킷">테스트 2. echo Request 패킷과 echo Response 패킷</h4>
<ul>
<li><code>Kail</code>에서 <code>Windows</code>로 <code>ping</code>을 때린다.<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/30389172-9d0a-40c6-853e-863ab52806c0/image.png" /></li>
</ul>
</li>
</ul>
<ul>
<li>앞에서 언급한 <code>사용되는 패킷</code>을 참고하면 된다.</li>
<li>샥스핀의 하단에 있는 송수신 패킷들을 한 개씩 클릭한 상태에서 하단에 있는 <code>세부항목</code>을 확인해보면</li>
<li><code>Windows 10</code>이기에 <code>128</code>이, <code>송신부</code>는 <code>Windows</code>이기에 <code>128</code>이 출력되는 것을 알 수 있다.<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bf6f8c1e-de88-48d6-9ec0-ccb8f0033e99/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h2 id="nslookup">nslookup</h2>
<h3 id="개요-1">개요</h3>
<ul>
<li><code>DNS Lookup(네임서버 조회)</code>을 통해 FQDN을 검색할 수 있다.</li>
<li><code>DNS</code>의 호스트와 매핑되어 있는 <code>IP주소</code>를 확인할 수 있다.</li>
</ul>
<hr />
<h2 id="traceroute">traceroute</h2>
<h3 id="개요-2">개요</h3>
<ul>
<li>네트워크 정보를 확인하는 명령어이다</li>
<li>목적지로 가는 동안에 거치는 라우터를 기록한다.</li>
<li><code>Windows</code> 에서는 <code>tracert</code>를 사용한다.<h3 id="실습환경">실습환경</h3>
</li>
<li><code>Kali</code><ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li><code>CentOS</code><ul>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>x</code> / <code>x</code></li>
</ul>
</li>
<li><code>Windows 10</code><ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li><code>Network Adapter는 Host-only</code></li>
</ul>
<hr />
<h2 id="arping">arping</h2>
<ul>
<li>'ARP 패킷'을 이용한 '살아있는 호스트(Live)'를 식별한다.</li>
<li>'OSI 7 layer'의 '3계층 이하(2계층, Data-Link Layer)'에서만 동작한다.</li>
<li>로컬 네트워크에 있는 시스템끼리만 통신이 가능하다.</li>
</ul>
<hr />
<h2 id="netenum">netenum</h2>
<h3 id="개요-3">개요</h3>
<ul>
<li>특정 IP 주소의 대역(범위) 안에 있는 모든 시스템(장비 등 IP를 사용하는 모든 시스템)에 ping 패킷을 보낸 후 활성화 된 시스템을 확인한다.</li>
<li>'ICMP echo Request' 패킷을 보낸 후 'ICMP echo Reponse' 패킷을 받아서 IP주소들을 출력해 준다.</li>
<li>실제 도메인 등을 이용하는 것이 아니기 때문에 IP가 부여된 시스템이 여러 개 있으면 좋다.</li>
</ul>
<h3 id="실습환경-1">실습환경</h3>
<ul>
<li><code>Kali</code><ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li><code>CentOS</code><ul>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>x</code> / <code>x</code></li>
</ul>
</li>
<li><code>Windows 10</code><ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li><code>Network Adapter는 Host-only</code></li>
<li>패키지 다운<pre><code class="language-bash">[samadal@kali ~]$ sudo apt install irpas</code></pre>
</li>
</ul>
<h3 id="wireshark로-분석">wireshark로 분석</h3>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/27da0c72-8b92-4a45-846c-05e2e5ab52e8/image.png" /></li>
<li>netenum이 “192.168.10.1 ~ 192.168.10.254” 전부에게 ARP 요청을 보내는 모습</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b9203764-a450-4ba7-a376-14f30dd8dac4/image.png" /></li>
</ul>
<hr />
<h2 id="33-dns-zone-transfer-네임서버-영역-전송">3.3 DNS Zone Transfer (네임서버 영역 전송)</h2>
<h3 id="개요-4">개요</h3>
<ul>
<li>'외부'에서 'DNS 정보'를 조회할 때 설정한다.</li>
<li><code>정방향 조회영역</code>, '역방향 조회영역'들의 '내용 노출로 인한 피해를 최소화'한다.</li>
<li>(핵심) 네임서버조회가 안될 경우 에는 제대로 된 내용을 조회할 수가 없다.<h3 id="실습환경-2">실습환경</h3>
</li>
<li><code>Kali</code><ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li><code>CentOS</code><ul>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>x</code> / <code>x</code></li>
</ul>
</li>
<li><code>Windows 10</code><ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.128</code></li>
</ul>
</li>
</ul>
<h3 id="dig-domain-information-groper">dig (Domain Information Groper)</h3>
<ul>
<li><p>개요</p>
<ul>
<li>'Domain Information Groper(웅덩이, 구덩이)'의 약자이다.</li>
<li>DNS로부터 정보를 가져올 수 있는 도구를 말한다.</li>
<li>DNS 정보와 그에 매핑되어 있는 호스트의 유무를 조사할 수 있다.</li>
<li>'Windows Server 제품군'에서 실습했던 'Root Hint'와 동일한 기능을 가지고 있다.</li>
<li>'네트워크 어뎁터'가 'NAT'로 되어 있을 때 네임서버를 입력하지 않을 경우 '/etc/resolv.conf'의 내용을 참고로 'Root Server'를 조회한다.  즉, NAT는 외부와의 통신이 되기 때문이다.</li>
</ul>
</li>
<li><p>사용법</p>
<pre><code class="language-bash">dig [@Server] [Domain] [Query Type]</code></pre>
</li>
<li><p>실습 1. <code>dig</code> 단일 명령</p>
<ul>
<li><p>개요</p>
<ul>
<li><code>Root Server</code>의 목록들만 출력</li>
</ul>
</li>
<li><p>명령 실행 1. <code>Network Adapter</code> <code>NAT</code>로 되어 있는 경우</p>
<ul>
<li><code>Kali</code>의 <code>IP</code>를 <code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code>로 변경한다</li>
<li><code>Network Adapter</code>를 <code>NAT</code>로 변경한다.</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2691d47c-fe3d-4e1a-a5a7-a15e9db489f7/image.png" /></li>
</ul>
</li>
<li><p>명령 실행 2. <code>Network Adapter</code> <code>Host-only</code>로 되어 있는 경우</p>
<ul>
<li><code>Kali</code>의 <code>IP</code>를 <code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code>로 변경한다</li>
<li><code>Network Adapter</code>를 <code>Host-only</code>로 변경한다.</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2a9977b3-d012-4811-8050-01c2582542a0/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p>실습 2. 특정 네임서버로 <code>DNS</code> 정보를 조회</p>
<ul>
<li>개요<ul>
<li>특정 네임서버의 레코드 정보를 가져온다.</li>
<li>이 경우에 <code>/etc/resolv.conf</code>의 IP는 <code>Gateway</code>의 IP(192.168.10.2)를 입력해야 출력된다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li><table>
<thead>
<tr>
<th>네트워크 모드</th>
<th>인터넷</th>
<th>dig root server 조회</th>
<th>이유</th>
</tr>
</thead>
<tbody><tr>
<td><strong>NAT</strong></td>
<td>가능</td>
<td>가능</td>
<td>NAT 게이트웨이가 인터넷 DNS에 연결</td>
</tr>
<tr>
<td><strong>Host-only</strong></td>
<td>불가</td>
<td>불가</td>
<td>DNS·게이트웨이가 내부망에 없음</td>
</tr>
</tbody></table>
</li>
</ul>
<ul>
<li><code>[samadal@kali ~]$ sudo dig @210.102.55.92 samadal.com</code></li>
</ul>
<h3 id="dns-zone-transfer">DNS Zone Transfer</h3>
<ul>
<li><p>실습 1. </p>
<ul>
<li><p>DNS(CentOS)에서 영역 전송 허용 여부(allow-transfer)를 <code>any</code>로 변경했을 때</p>
<ul>
<li><p><code>kali</code>에서 <code>[samadal@kali ~]$ sudo dig @192.168.10.128 axfr gusiya.com</code> 실행</p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7999c9b1-31b4-4ef2-b7a0-885a07ea3297/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/beb954a1-7d45-4721-977b-215711b042fb/image.png" /></p>
</li>
</ul>
</li>
<li><p>DNS(CentOS)에서 영역 전송 허용 여부(allow-transfer)를 <code>none</code>로 변경했을 때</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/710bf9a2-ba33-4718-a084-703891884bba/image.png" /></li>
</ul>
</li>
<li><p>내부 도메인 구조, 서버 IP, 웹/DB/Mail 서버 위치, 서브도메인 전체 목록이 모든 정보가 해커에게 그대로 털림
→ 그래서 any는 절대 사용하면 안 되는 위험 설정</p>
</li>
<li><p><span style="color: orange;"><code>영역 전송 허용 여부(allow-transfer)</code>를 <code>none</code>으로 하는 것이 가장 확실한 대응법이다.</span></p>
</li>
</ul>
</li>
<li><p>실습 2. <code>Brute Forcing (무차별 대입 공격)</code>을 이용한 <code>DNS Zone Transfer</code></p>
<ul>
<li><p>개요</p>
<ul>
<li>동일한 IP에서 쿼리에 대한 질의(Query)를 계속 물어본다면 '불순한 의도'로 간주할 수 있는데 이러한 것들 모니터링 하는 것을 말한다.</li>
<li>가능한 모든 암호 조합을 무차별적으로 시도하는 기초적인 해킹 기법을 말한다.</li>
<li>대부분의 암호는 시간이 걸릴 뿐이지 결국에는 알게 되는데 이 때 사용되는 해킹 기법인 '사전 공격'을 이용한다.</li>
</ul>
</li>
<li><p>환경 설정</p>
<ul>
<li><code>Kali</code><ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li><code>CentOS</code><ul>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>x</code> / <code>x</code></li>
</ul>
</li>
<li><code>Windows 10</code><ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.128</code></li>
</ul>
</li>
</ul>
</li>
<li><p>사용되는 명령어 (DNS Server를 분석하고 관련 정보를 수집)</p>
<ul>
<li><p><code>DNS Server</code>의 하위 도메인 정보 출력</p>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d4aafe14-288e-4889-b7c6-3bc60032619f/image.png" /></p>
</li>
<li><p><code>sudo dnsmap gusiya.com</code></p>
</li>
</ul>
</li>
<li><p>수집 결과를 파일로 저장 1. 호스트 정보만 저장</p>
<ul>
<li><code>sudo dnsmap gusiya.com -r /tmp/result1.txt</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bd464bb3-70cd-43a8-a507-802f10d5f005/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p>수집 결과를 파일로 저장 2. 명령어를 포함한 모든 정보 저장</p>
<ul>
<li><code>sudo dnsmap gusiya.com &gt; /tmp/result2.txt</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/415d76f2-5112-49c6-a583-dd27007b567f/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p>테스트 1. <code>Dictionary File</code>(/usr/share/dnsmap/wordlist_TLAs.txt)</p>
<ul>
<li>작업<ul>
<li>원본 파일 백업<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5295fa3f-7c5e-4e13-90a5-fda4544fd015/image.png" /></li>
<li><code>[samadal@kali /usr/share/dnsmap]$ sudo cp -r wordlist_TLAs.txt wordlist_TLAs.txt.samadal</code></li>
<li>사진 파일 안에 있는 3자리 문자(레코드명, aaa ~ zzz)에 있는 문자와 호스트명(ns, www, cafe, blog)를 비교한다.</li>
<li>www만 문서 파일 안에 넣는다</li>
</ul>
</li>
</ul>
</li>
<li>명령 실행<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/39545d79-6da8-40e9-b434-c225354f7386/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p>테스트 2. <code>Dictionary File</code> 안에 호스트(ns, www, cafe, blog, ftp, mail, db)를 추가한다.</p>
<ul>
<li>명령 실행<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e3433bdc-0cba-41d3-9205-c1b28634e577/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p>결론</p>
<ul>
<li><code>DNS</code>의 호스트를 최대한 노출 시키지 않는 방법이 최선이지만 결과적으로 <code>Brute Forcing</code>을 막을 수 있는 방법은 없다.</li>
<li>앞에서 말 한 것처럼 <code>Zone Transfer</code>를 <code>none</code>으로 하는 것이 최선의 방법이다.</li>
</ul>
</li>
</ul>
<hr />
<h1 id="span-style--colorskyblue04-port-scanning-span"><span style="color: skyblue;">04. Port Scanning </span></h1>
<h2 id="41-tcp-scan-nmap">4.1 TCP Scan (nmap)</h2>
<h3 id="개요-5">개요</h3>
<ul>
<li><code>TCP</code>를 이용한 포트 스캔을 말한다.</li>
<li><code>3-Way Handshaking(TCP 연결 과정)</code> 과정을 거친다.</li>
<li>빠른 포트 스캔을 할 수 있다.</li>
</ul>
<h3 id="nmap">nmap</h3>
<ul>
<li>포트를 스캔하기 전에 어떤 시스템이 <code>(핵심) 동작중인지를 먼저 확인</code>한다</li>
<li>응답하지 않는 시스템은 스캔을 하지 않는다.</li>
<li>가장 많이 사용하는 포트 스캔 명령어이다.<h3 id="실습환경-3">실습환경</h3>
</li>
<li><code>Kali</code><ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li><code>CentOS</code><ul>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>x</code> / <code>x</code></li>
</ul>
</li>
<li><code>Windows 10</code><ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.128</code></li>
</ul>
</li>
</ul>
<h3 id="실습-1-t-옵션">실습 1. &quot;T&quot; 옵션</h3>
<ul>
<li>개요 <ul>
<li>가장 많이 알려진 <code>포트(-T(cp), 1000개)</code>를 스캐닝한다.</li>
<li>TCP로 연결된 것들만 스캔한다. (UDP는 제외)</li>
<li>1,000중에서 <code>존재하지 않는 포트로 연결을 요청할 때</code> 열린 포트(22)에서는 더 이상 연결이 안 되게 끊어버린다.</li>
</ul>
</li>
<li>명령 실행<ul>
<li><code>sudo nmap -sT 192.168.10.128</code></li>
</ul>
</li>
<li><code>wireshark</code>로 패킷 분석<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fa5f72c6-1541-4f4f-8710-896282d89747/image.png" /></li>
</ul>
</li>
</ul>
<h3 id="실습-2-s-옵션">실습 2. &quot;S&quot; 옵션</h3>
<ul>
<li>개요 <ul>
<li>연결된 상태만 스캐닝한다.</li>
<li><code>TCP SYN Flag</code>를 스캐닝 한다</li>
</ul>
</li>
<li>명령 실행<ul>
<li><code>sudo nmap -sS 192.168.10.128</code></li>
</ul>
</li>
<li><code>wireshark</code>로 패킷 분석<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1f746b89-2237-45b8-8e8b-aaac61d42c66/image.png" /></li>
</ul>
</li>
</ul>
<h3 id="실습-3-v-옵션">실습 3. &quot;V&quot; 옵션</h3>
<ul>
<li>개요<ul>
<li>포트에서의 <code>서비스 활성화 유무(VERSION)</code>를 스캐닝한다.</li>
</ul>
</li>
<li>명령 실행<ul>
<li><code>sudo nmap -sTV -Fn --version-intensity 0 www.gusiya.com</code></li>
<li><code>-sV</code> (서비스 또는 버전 등의 정보를 정하기 위한 포트를 검색)</li>
<li><code>-V</code> (진행상태를 화면에 출력) </li>
<li><code>-F</code> (특정 포트를 스캔, 잘 알려진 포트만 검색)</li>
<li><code>--version-intensity</code> (스캔 강도 지정, <code>0(light, 정상)</code>)<ul>
<li><code>0</code> (5분 마다)</li>
<li><code>1</code> (15초 마다)</li>
<li><code>2</code> (0.4초 마다)</li>
<li><code>3</code> (기본값, 1회)</li>
<li><code>4</code> (5분 동안만)</li>
<li><code>5</code> (75초 동안 만)</li>
</ul>
</li>
<li><code>모든 포트를 대상</code>으로 <code>검사하지 않았던 포트(Unkonwn)</code>까지 스캔한다.  </li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/44616024-9dfe-446e-8ed1-c809cf3ad256/image.png" /></li>
</ul>
</li>
</ul>
<h3 id="실습-4-p-옵션">실습 4. &quot;P&quot; 옵션</h3>
<ul>
<li>개요 <ul>
<li>'모든 포트를 대상'으로 '검사하지 않았던 포트(Unkonwn)'까지 스캔한다.</li>
<li>'모든 포트'가 대상이기 때문에 시간이 많이 소요될 수 있다.</li>
</ul>
</li>
<li>명령 실행<ul>
<li><code>sudo nmap -sT -p- -Pn www.gusiya.com</code></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ec8bec5c-896b-4921-8e87-4d7220540241/image.png" /></li>
</ul>
</li>
</ul>
<h3 id="실습-5-응용">실습 5. 응용</h3>
<ul>
<li>실습 환경<ul>
<li><code>Kali</code> (Port Scanning)</li>
<li><code>Windows 10</code> (www / win 모두 출력되는지 확인)</li>
<li><code>Rocky</code> / <code>CentOS</code> (DNS Server)</li>
<li><code>Windows Server</code> (win.gusiya.com / IIS web/ FTP Server)</li>
</ul>
</li>
<li>로컬 테스트</li>
<li>원격 테스트 (2 ~ 3인 1팀으로 구성)</li>
</ul>
<hr />
<h1 id="span-style--colorskyblue05-sniffing스니핑과-spoofing스푸핑span"><span style="color: skyblue;">05. Sniffing(스니핑)과 Spoofing(스푸핑)</span></h1>
<h2 id="51-sniffing스니핑">5.1 Sniffing(스니핑)</h2>
<h3 id="개요-6">개요</h3>
<ul>
<li>네트워크 상에서 자신이 아닌 다른 상대방들의 패킷 교환을 <code>훔쳐보는 행위(도청)</code>를 말한다.</li>
</ul>
<h3 id="sniffing-종류">Sniffing 종류</h3>
<ul>
<li><code>Passive Sniffing</code></li>
<li><code>HUB</code>(Switch)와 같이 모든 노드에 동일한 전기적 신호(동기신호)가 복제되는 경우에는 단순히 스니퍼만 동작시켜도 모든 패킷을 잡아내는 방법을 말한다.</li>
<li><code>Active Sniffing</code></li>
<li><code>Switch</code> 환경에서는 해당 포트로만 데이터가 전송되기 때문에 데이터 신호를 스니퍼가 설치된 시스템에 경유하도록 <code>유도</code>하는 방법을 말한다.</li>
</ul>
<h2 id="52-spoofing스푸핑">5.2 Spoofing(스푸핑)</h2>
<h3 id="개요-7">개요</h3>
<ul>
<li><code>Sniffing</code> 공격의 대표적 기술을 말한다.</li>
<li>외부의 악의적인 네트워크 침입자가 웹사이트를 구성한 후 사용자들의 방문을 유도하고 인터넷 프로토콜인 TCP/IP(공용 프로토콜)의 구조적 결함(공용 프로토콜은 누구나 접근이 가능하기 때문에)을 이용해서 사용자의 시스템 권한을 획득한 뒤 정보를 빼가는 해킹 기법을 말한다.</li>
<li>스푸핑은, 잘 알려진 기업의 명의로 스팸 메일을 발송하거나 위조 사이트로 접속을 유도하는 기술과 로그인 하려는 컴퓨터가 허가받은 IP를 도용해서 로그인하는 기법 등을 총칭한다.</li>
<li>기법<ul>
<li><code>ARP Spoofing</code></li>
<li><code>DNS Spoofing</code></li>
<li><code>IP Spoofing</code></li>
</ul>
</li>
</ul>
<h2 id="53-실습">5.3 실습</h2>
<h3 id="실습-1-기본-실습-ip를-이용한-공격">실습 1. 기본 실습 (IP를 이용한 공격)</h3>
<h3 id="실습환경nat">실습환경(NAT)</h3>
<ul>
<li><p>Attacker <code>Kali</code></p>
<ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li><p>Victim  <code>Windows 10</code></p>
<ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
<li><p>정보 기록</p>
<ul>
<li><code>Attacker</code> <ul>
<li>(IP) <code>192.168.10.130</code></li>
<li>(MAC) <code>00:0c:29:45:b5:f9</code></li>
</ul>
</li>
<li><code>Victim</code> <ul>
<li>(IP) <code>192.168.10.131</code> </li>
<li>(MAC) <code>00-0c-29-b9-16-ea</code></li>
</ul>
</li>
<li><code>Gateway</code> <ul>
<li>(IP) <code>192.168.10.2</code></li>
<li>(MAC) <code>00-50-56-e3-3f-c3</code></li>
</ul>
</li>
</ul>
</li>
<li><p><code>Attacker</code>에서 <code>ARP Spoofing (ARP Attack)</code>을 이용한 <code>MAC Address</code> 변경</p>
<ul>
<li><p>Step 1. <code>명령어 관련 패키지(dsniff)</code> 설치 여부 확인</p>
<ul>
<li><code>[samadal@kali ~]$ which dsniff</code></li>
</ul>
</li>
<li><p>Step 2. MAC Address 확인 1. 명령어 실행 전 (win 10) </p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/faa7e1b2-d32e-4ee7-bccf-02a8b0f67675/image.png" /></li>
</ul>
</li>
<li><p>Step 3. <code>ARP Spoofing</code></p>
<ul>
<li><code>sudo arpspoof -i eth0 -t 192.168.10.131 192.168.10.2</code></li>
<li><code>sudo arpspoof -i(I/F) eth0(공격자의 이더넷) -t 192.168.10.131(희생자의 IP) 192.168.10.2(희생자의 G/W)</code></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7fc2f95f-b444-4b9a-9b80-98512b237540/image.png" /></li>
</ul>
</li>
<li><p>Step 4. MAC Address 확인 1. 명령어 실행 후</p>
<ul>
<li>공격자의 MAC 주소로 바뀜<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/44008174-2958-47bf-8905-404dafbff12e/image.png" /></li>
</ul>
</li>
<li><p>Step 5. <code>Victim</code>에서 웹브라우저 실행 후 네이버 사이트 접속</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/95df1b6c-df2a-49f7-ae37-1ff52781bd38/image.png" /></li>
</ul>
</li>
<li><p>Step 6. <code>Attacker</code>의 공격을 멈춘 후 <code>Victim</code>에서 <code>GW</code> 및 사이트 출력 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a150daf5-76fd-4f8d-b5c4-8c0e31f2f070/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/afb2629d-a44b-439a-a5e9-aa8de9ff3916/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="실습-2-도메인을-이용한-공격-1">실습 2. 도메인을 이용한 공격 1.</h3>
<ul>
<li><p>작업 개요 </p>
<ul>
<li><code>CentOS / Rocky</code>에서 <code>DNS Server</code>와 <code>Web Server</code>를 구축한다.</li>
<li><code>Kali</code>에서 <code>ARP Spoofing</code>을 실행한다.</li>
<li><code>Windows 10</code>에서 사이트 출력을 확인하고 변조된 것을 확인한다. </li>
</ul>
</li>
<li><p>실습환경(NAT)</p>
<ul>
<li>Attacker <code>Kali</code><ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li>Victim <code>CentOS</code><ul>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li>확인 <code>Kali</code><ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
</ul>
</li>
<li><p>작업</p>
<ul>
<li><p>Step 1. 3개의 시스템에 <code>IP</code>를 설정한다.</p>
</li>
<li><p>Step 2. <code>CentOS</code>에서 <code>Kali</code>에 <code>호스트</code>(attack)를 부여한다</p>
</li>
<li><p>Step 3. <code>Windows 10</code>에서 네임서버 조회 및 <code>MAC Address</code> 확인</p>
<ul>
<li>```bash
인터넷 주소            물리적 주소           유형</li>
</ul>
<p>192.168.10.2          00-50-56-e3-3f-c3     동적
192.168.10.128        00-0c-29-b0-8f-47     동적
  ```</p>
</li>
<li><p>Step 4. <code>Windows 10</code>에서 <code>www.gusiya.com (O)</code> /  <code>attack.gusiya.com (X)</code> 조회</p>
</li>
<li><p>Step 5. <code>Kali</code>에서 시스템을 재구성한다.</p>
<ul>
<li><code>attack.gusiya.com</code>를 실행한다.<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8a927dc4-62d9-4202-8f81-dfdcd35f519a/image.png" /></li>
<li><code>firefox</code>에서 <code>attack.gusiya.com</code>을 입력하고 사이트를 출력해본다</li>
<li><code>http://attack.gusiya.com</code><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7bb5059e-b583-41fb-9644-66712321d066/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li><p>Step 6. <code>Kali</code> <code>DNS Spoofing</code>으로 두 시스템에 공격을 실행한다.</p>
<ul>
<li><p><code>Kali</code></p>
<ul>
<li><p><code>DNS Spoofing</code> 명령을 실행한 후 닫지 말고 계속 실행 해 둔다.</p>
<ul>
<li><p><code>(kali)$ sudo arpspoof -i eth0 -t 192.168.10.131 192.168.10.2</code></p>
</li>
<li><p><code>(kali)$ sudo arpspoof -i eth0 -t &lt;Windows 10의 IP&gt; &lt;Gateway IP&gt;</code></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/448e9c15-e6e7-4545-904d-ca34b2987a74/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/41f72b43-ae6c-449a-9323-8aa7114a06bd/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3399f7d7-cad2-4799-815f-54d6898694c1/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c6d40b8d-3f3d-4674-b735-bd2d510f71e8/image.png" /></p>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code>Windows 10</code></p>
<ul>
<li>두 개 사이트<code>(www.gusiya.com</code> / <code>attack.gusiya.com</code>) 출력 <ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/385e9965-0365-4bc7-953b-4cb5385f7d56/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fcdac251-7d0c-4226-996c-a5585cfde5b0/image.png" /></li>
<li><code>(출력 안될경우 데몬 재실행)</code></li>
<li>(kali)$ sudo service apache 2 restart</li>
<li>(CentOS)#</li>
</ul>
</li>
<li><code>arp -a</code>를 통한 <code>MAC Address</code>를 확인 해보면 <code>Gateway</code> 주소가 변조된 것을 알 수 있다.</li>
<li>웹 브라우저에서 <code>History</code> 정보를 모두 제거하고 창을 닫고 다시 실행, 출력 해본다</li>
<li>정상적으로 출력되는 것을 알 수 있다.</li>
<li>결론 <ul>
<li><code>Windows 10</code>은 단지 사이트 출력만 하고 있기 때문에 실제 공격을 받았지만 사이트는 아무런 영향을 받지 않는다.</li>
</ul>
</li>
</ul>
</li>
<li><p><code>CentOS</code></p>
<ul>
<li>앞에서 실행하고 있던 공격을 중지하도록 한다.</li>
<li><code>DNS Spoofing</code> 명령을 실행한 후 닫지 말고 계속 실행해 둔다.<ul>
<li><code>(kali)$ sudo arpspoof -i eth0 -t &lt;DNS Server의 IP&gt; &lt;Gateway IP&gt;</code></li>
<li><code>(kali)$ sudo arpspoof -i eth0 -t 192.168.10.128 129.168.10.2</code></li>
</ul>
</li>
<li><code>arp -a</code>를 통한 <code>MAC Address</code>를 확인해보면 <code>Gateway</code> 주소는 변하지 않았다는
 것을 알 수 있다.<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0f76cfbf-0c30-4fc1-8693-4604f54718fd/image.png" /></li>
</ul>
</li>
<li><code>centOS</code>에서도 동일한 방법으로 확인해보면 변조된 것을 알 수 있다.</li>
<li>결론<ul>
<li><code>Windows 10</code>은 단지 사이트를 출력만 하고 있고 실제 공격에 대한 피해는 <code>centOS</code>이기 때문에 사이트에는 아무런 영향을 끼치지 않는다.</li>
</ul>
</li>
</ul>
</li>
<li><p>결론 </p>
<ul>
<li>공격 받는 대상이 누군이던지 사이트 출력은 아무런 영향을 받지 않는다는 것을 알 수 있다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="실습-3-도메인을-이용한-공격-2">실습 3. 도메인을 이용한 공격 2.</h3>
<ul>
<li><p>실습환경(NAT)</p>
<ul>
<li>Attacker <code>Kali</code><ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
<li>확인 <code>Windows 10</code><ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>8.8.8.8</code></li>
</ul>
</li>
</ul>
</li>
<li><p><code>vi /etc/hosts</code>(백업 후 진행) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1a396964-ea2b-42e0-8bcb-3464a79efb30/image.png" /></p>
</li>
<li><p>작업</p>
<ul>
<li><code>Spoofing</code>을 실행하지 않은 경우<ul>
<li>사이트(<a href="http://www.naver.com">www.naver.com</a> / <a href="http://www.google.com)%EB%A5%BC">www.google.com)를</a> 출력해보면 출력이 잘 된다.</li>
<li><code>MAC Address</code>의 변화도 확인한다.<ul>
<li><code>아무 변화 없음</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/beba33ac-9c62-4c6b-80b5-89994e921d13/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li><p><code>Spoofing</code>을 실행한 경우</p>
<ul>
<li><p>명령 실행</p>
<ul>
<li><code>sudo arpspoof -i -eth0 -t 192.168.10.131 192.168.10.2</code></li>
</ul>
</li>
<li><p>사이트 <code>(www.naver.com</code> / <code>www.google.com</code>)를 출력 해보면 모두 출력이 되지 않는다.</p>
</li>
<li><p><code>MAC Address의 변화도 확인해 보면 GW 주소만 변조가 되었다</code><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e9540567-6be4-4fc6-8190-66f99537aca8/image.png" /></p>
</li>
<li><p>결론</p>
<ul>
<li><code>Windows 10</code>의 <code>IP(192.168.10.131)</code>는 <code>GW</code>의 <code>IP</code>(192.168.10.2)를 통해 외부로 나가게 되는데 이 주소가 <code>Kali</code>의 <code>MAC Address</code>로 변조가 되었기 때문에 정상적인 경로로 나갈 수가 없다. 따라서 출력이 되지 않는다.</li>
</ul>
</li>
</ul>
</li>
<li><p><code>도메인을 이용한 공격 1.</code>과 <code>도메인을 이용한 공격 2.</code>의 테스트에 따른 결론</p>
<ul>
<li><code>ARP Spoofing</code> 만으로는 사이트에 어떠한 변화도 줄 수가 없다.</li>
<li>다만, <code>GW</code>의 <code>MAC Address</code>만 변경될 뿐이다.</li>
</ul>
</li>
</ul>
<h3 id="실습-4-packet-forwarding-1">실습 4. Packet Forwarding 1.</h3>
<ul>
<li><p>실습환경(NAT)</p>
<ul>
<li><code>Kali</code><ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
<li><code>Windows 10</code><ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>8.8.8.8</code></li>
</ul>
</li>
</ul>
</li>
<li><p><code>Kali</code>에서 <code>Packet Forwarding</code>을 실행하기 위한 작업</p>
<ul>
<li><code>공격자</code>(Kali)<ul>
<li><code>(kali)$ sudo cp -p /etc/hosts.samadal</code></li>
<li></li>
</ul>
</li>
<li><code>공격대상</code>(Windows 10)</li>
</ul>
</li>
<li><p><code>Kali</code>에서 터미널창을 하나 더 실행 (멈춘것처럼 나와도 그대로 둔다.)</p>
<pre><code class="language-bash">[samadal@kali ~]$ sudo fragrouter -B1
[sudo] samadal 암호:
sudo: fragrouter: 명령이 없습니다
</code></pre>
</li>
</ul>
<p>[samadal@kali ~]$ sudo vi /etc/resolv.conf</p>
<h1 id="패키지-설치를-위해-192168102-인지-확인">패키지 설치를 위해 192.168.10.2 인지 확인</h1>
<p>[samadal@kali ~]$ sudo apt -y install fragrouter</p>
<p>[samadal@kali ~]$ sudo vi /etc/resolv.conf
#192.168.10.128 로 변경</p>
<pre><code>- `Windows 10`에서 확인
  - 링크된 사이트(www.naver.com) 출력
    - 웹브라우저 화면에 정상적인 네이버 화면이 출력된다.
    - 이 때 추가된 터미널창을 보면 엄청난 양의 `IP`들이 함께 출력되고 있는 것을 볼 수 있다.

  - `MAC Address` 확인
    - `Kali`의 `MAC Address`로 변조가 된 것을 알 수 있다. ![](https://velog.velcdn.com/images/kyk02405/post/9723d69c-2a83-44fc-a86d-1bc795e9d499/image.png)

  - `Host OS`에서 웹 브라우저를 실행한 후 앞에서 올라온 여러 개의 `IP`주소를 입력, 출력
    - ![](https://velog.velcdn.com/images/kyk02405/post/eafa2084-9602-4943-afd9-a80e37d125ad/image.png)

  - `검색된 IP`의 사이트가 보안상 문제가 있는 경우라면 위에서 했던 작업(추적)을 통해 회사 정보를 빼낼 수가 있다.
- 결론
  - 공격 대상에 `ARP Spoofing`을 실행한 후 `fragerouter -B1`을 통해 공격 대상의 웹 브라우저에 출력되는 모든 내용을 공격 대상의 가상 포트를 이용해서 확인 가능하다.
  - `실습 3. 도메인을 이용한 공격 2.` 의 테스트 결과를 뒤집을 수 있는 것을 증명하고 있다.


&gt; # 📌 실습 4 결론
### ✔ 1) ARP 스푸핑만 하면 트래픽이 끊기고 인터넷이 안 됨
→ 그래서 실습 3에서 사이트가 안 열렸음
### ✔ 2) 하지만 fragrouter로 Packet Forwarding을 활성화하면
→ 공격자가 Router처럼 작동
→ 피해자는 인터넷이 정상 동작함
→ 동시에 공격자는 모든 웹 요청/응답을 볼 수 있음
### ✔ 3) 즉, “정상 사이트가 뜬다 = 안전하다”가 아님
→ 공격자는 보이지 않게 중간에서 전부 가로챌 수 있음
# 🧩 결론(완전 정리)
&gt; **ARP 스푸핑만으로는 인터넷이 끊겨서 공격이 티가 나지만,
&gt; Packet Forwarding을 활성화하면 공격 대상이 정상적으로 인터넷을 쓰는 것처럼 보이면서
&gt; 공격자는 모든 패킷을 감시할 수 있는 완전한 중간자 공격(MITM)이 가능하다.
&gt; 즉, 실습 3처럼 &quot;사이트가 뜬다 = 안전하다&quot;는 결론이 틀릴 수 있음을 보여준다.**


### 실습 5. Packet Forwarding 2. POST 방식
- 실습환경(NAT)
  - `Kali`
    - `192.168.10.130` / `C Class` / `192.168.10.128` / `192.168.10.128`
  - `CentOS`
    - `192.168.10.128` / `C Class` / `x` / `x`
  - `Windows 10`
    - `192.168.10.131` / `C Class` / `192.168.10.128` / `192.168.10.128`

- `Windows 10`에서 네임서버 조회
  - ![](https://velog.velcdn.com/images/kyk02405/post/0037d7db-caac-4f11-ad66-18d422320657/image.png)
- `Apache Web Server`의 `기본 경로(예를 들어, /export/home/samadal)`에 다음과 같은 `파일(login.html)`을 생성한다.
  - `vi /etc/httpd/conf/httpd.conf` ![](https://velog.velcdn.com/images/kyk02405/post/bb3c6c47-0601-4b42-9096-a1b7783974ef/image.png)
  - `touch /export/home/samadal/login.html`
  - `chmod 701 /export/home/samadal`
  - `systemctl restart httpd`
```html
&lt;html&gt;
   &lt;head&gt;
      &lt;title&gt;로그인 페이지&lt;/title&gt;
   &lt;/head&gt;

   &lt;body&gt;
      &lt;div class=&quot;login-wrapper&quot;&gt;
         &lt;h2&gt;Login&lt;/h2&gt;

         &lt;form method=&quot;post&quot; action=&quot;서버의url&quot; id=&quot;login-form&quot;&gt;
            &lt;input type=&quot;text&quot; name=&quot;userName&quot; placeholder=&quot;ID&quot;&gt;
            &lt;input type=&quot;password&quot; name=&quot;userPassword&quot; placeholder=&quot;Password&quot;&gt;
            &lt;label for=&quot;remember-check&quot;&gt; 
               &lt;input type=&quot;checkbox&quot; id=&quot;remember-check&quot;&gt;아이디 저장하기
               &lt;/label&gt;
            &lt;input type=&quot;submit&quot; value=&quot;Login&quot;&gt;
         &lt;/form&gt;
      &lt;/div&gt;

   &lt;/body&gt;

&lt;/html&gt;</code></pre><ul>
<li>사이트 출력<ul>
<li><code>Kali</code>에서 <code>Wireshark</code>를 실행시켜놓고 <code>Windows 10</code>에서 사이트를 출력한다.<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/314838e5-3c18-4cfb-98c2-0316d6ec92fc/image.png" /></li>
</ul>
</li>
<li>로그인창이 뜨면 ID, Password를 입력하고 <code>login</code> 버튼을 클릭한다<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e5569f53-d81a-472a-8583-3a6aa6c647b9/image.png" /></li>
</ul>
</li>
<li><code>kali</code>의 <code>Wireshark</code> 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c063bda4-7ba8-4866-bfe3-ff7123a10fba/image.png" /></li>
<li><code>POST</code>방식은 모든 내용이 출력이 되기 떄문에 보안상 취약하다는 말이다.</li>
</ul>
</li>
</ul>
<h3 id="실습-6-패킷-덤핑-및-가로채기">실습 6. 패킷 덤핑 및 가로채기</h3>
<ul>
<li><p>실습환경(NAT)</p>
<ul>
<li><code>Kali</code><ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
<li><code>Windows 10</code><ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>8.8.8.8</code></li>
</ul>
</li>
</ul>
</li>
<li><p>다음의 같이 <code>패킷 캡처링(덤핑)</code>을 실행한다.</p>
<ul>
<li><code>kali</code>에서 새로운 터미널 창을 하</li>
<li>위에 결과창에 있는 <code>210.89.168.65</code>로 다음의 명령을 실행한다.<ul>
<li><code>sudo tcpdump src 192.168.10.131 and port 80</code></li>
</ul>
</li>
<li><code>IP</code>가 도달할때까지의 라우터들을 확인<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8a8c67ce-027b-4a6e-988c-95568d7767d4/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p><code>driftnet</code>을 이용한 패킷 덤핑 이미지</p>
<ul>
<li><p><code>CLI Mode</code></p>
<ul>
<li><code>(driftnet:120146): Gtk-WARNING **: 14:59:26.358: cannot open display:</code></li>
<li><code>CLI Mode</code>에서는 실행할 수가 없다.</li>
<li>고해상도 이미지보다는 저해상도 이미지가 빨리 덤핑된다.</li>
</ul>
</li>
<li><p><code>GUI Mode</code></p>
<ul>
<li>가상 시스템보다 호스트 시스템에서 이미지 출력이 잘된다.</li>
</ul>
</li>
<li><p>sudo driftnet -i eth0</p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/919386ca-9f64-41c8-a0c5-3aa9f4aa902c/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/36dea5cc-cde7-4229-976b-76d2694a4220/image.png" /></p>
</li>
</ul>
</li>
<li><p>내용 정리</p>
<ul>
<li>Step 1. 'ARP Spoofing'을 이용한 공격대상 시스템의 'ARP 캐지 정보(GW 주소)' 변경
<code>(kali)$ sudo aprspoof -i eth0 -t 192.168.10.131 192.168.10.2</code></li>
<li>Step 2. 패킷 포워딩 설정
<code>(kali)$ sudo fragrouter -B1</code></li>
<li>Step 3. 덤핑 및 가로채기
<code>(kali)$ sudo tcpdump src 192.168.10.131 and port 80</code>
<code>(kali)$ sudo driftnet -i eth0</code></li>
</ul>
</li>
</ul>
<hr />
<h1 id="span-style--colorskyblue06-dns-dhcp-spoofing-mitm-attackspan"><span style="color: skyblue;">06. DNS, DHCP Spoofing (MITM Attack)</span></h1>
<h2 id="61-용어-설명">6.1 용어 설명</h2>
<h2 id="mitm-man-in-the-middle">MITM (Man In The Middle)</h2>
<h3 id="개요-8">개요</h3>
<ul>
<li>MITM 공격은 글자 그대로 누군가의 사이에 끼어드는 것을 말한다.</li>
<li>클라이언트와 서버의 통신에 암호화된 채널을 이용하게 되면서 등장했다.</li>
<li>MITM은 전달되는 패킷의 MAC 주소와 IP 주소 뿐만 아니라 패킷의 내용까지 바꿀 수 있다.</li>
<li>네트워크 통신을 조작하여 내용을 도청하거나 조작하는 공격을 말한다.</li>
<li>MITM 공격 방법은 ARP 스푸핑 공격을 하면서 Packet 포워딩을 하는 것이다.   </li>
</ul>
<h3 id="주의사항">주의사항</h3>
<ul>
<li>프로토콜 취약점을 이용한 공격으로 현재까지도 카페, 도서관 등의 공공장소에서 공격이 가능하다</li>
<li>ARP Spoofing 공격만으로도 범죄이기 때문에 절대 가상환경에서만 사용해야 한다.</li>
<li>따라서 절대 공공장소에서 테스트하지 말고 가상환경에서 테스트해야 한다.</li>
</ul>
<hr />
<h2 id="ettercap">ettercap</h2>
<h3 id="개요-9">개요</h3>
<ul>
<li>MITM 공격을 위한 툴을 말한다.</li>
</ul>
<h2 id="62-실습환경nat">6.2 실습환경(NAT)</h2>
<ul>
<li><code>Kali</code><ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
<li><code>Windows 10</code><ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
</ul>
<hr />
<h2 id="63-dns-spoofing-설정">6.3 DNS Spoofing 설정</h2>
<h3 id="step-1-kali의-터미널에서의-작업">Step 1. Kali의 터미널에서의 작업</h3>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e7df9a00-2451-4936-9c72-31250e97087e/image.png" /></p>
</li>
<li><p><code>MITM Attack</code> 성공 후 출력할 문서 파일(index.html) 생성</p>
</li>
<li><p><code>Kali</code>에서 <code>firefox</code> 실행 후 다음과 같이 출력</p>
<ul>
<li><code>http://localhost</code> 또는 <code>http://192.168.10.130</code></li>
<li><code>MITM Attack</code> 시 출력할 도메인 설정<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0bd4daea-d003-403d-bd79-321d99a490b4/image.png" /></li>
</ul>
</li>
<li>(옵션) 명령어 백그라운드 프로그램 실행<ul>
<li><code>sudo ettercap -G &amp;</code><h3 id="step-2kali-ettercap에서의-작업">Step 2.<code>Kali ettercap</code>에서의 작업</h3>
</li>
</ul>
</li>
</ul>
</li>
<li><p>패키지 설치</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/76233548-8356-442a-b9b1-a6bb65766e22/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8f918150-d7ba-4088-950c-f166c3f54c91/image.png" /></li>
</ul>
</li>
<li><p><code>ettercap 실행</code></p>
<ul>
<li>주 메뉴 우측 상단에 있는 '√(Accept)'을 클릭한다.</li>
<li>메인 창이 실행되면 현재 동작 중인 왼쪽 상단의 '두 번째 아이콘(Start/Stop Sniffing)'을 클릭해서 '중지'한다.</li>
<li>우측 상단에 있는 'Ettercap Menu'를 클릭한 후 'Hosts'를 클릭하고 하위에 있는 'Scan for hosts'를 클릭한다.</li>
<li>다시 'Ettercap Menu'를 클릭한 후 'Hosts'를 클릭하고 하위에 있는 'Host lists'를 클릭하면 앞에서 검색된 'IP Address'와 'MAC Addess' 목록이 출력된다.</li>
</ul>
</li>
<li><p><code>ettercap 설정</code></p>
<ul>
<li><p><code>TARGET</code>에 시스템 등록</p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1e544661-20f0-4780-ba18-a36700a76694/image.png" /></p>
</li>
<li><p><code>Ettercap Menu</code>를 클릭한 후 하단에 있는 'Plugins'를 클릭하고 하위에 있는 'Manage plugins'를 클릭한다.</p>
</li>
<li><p>'Name' 항목에 있는 'dns-spoof'를 '더블 클릭'한 후 하단의 내용을 확인한다.</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6f6d35de-5a35-4a8e-8a78-7d58f8d85a3f/image.png" /></li>
</ul>
</li>
<li><p>메인 창의 왼쪽 상단에서 있는 'Start/Stop Sniffing'을 클릭해서 'Sniffing'을 다시 실행시킨다.</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/429bd66f-f3c7-40f4-9d66-32ad930481aa/image.png" /></li>
</ul>
</li>
<li><p>우측 상단에 있는 'MITM menu'를 클릭한 후 하단에 있는 'ARP poisoning'을 클릭한 후 'OK'를 클릭한다.</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/63a87811-6a3f-4f07-af41-da0555b70b4b/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="step-3-windows-10-에서의-작업">Step 3. Windows 10 에서의 작업</h3>
<ul>
<li>명령 프롬프트 창에서 ARP의 내용을 확인해보면 G/W가 Kali의 MAC Address로 변경된 것을 확인할 수 있다.<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ce272360-c327-480f-b534-f664b60a5958/image.png" /></li>
</ul>
</li>
<li>'웹 브라우저(Whale)'를 실행한 후 '<a href="http://www.naver.com'%EC%9D%84">www.naver.com'을</a> 실행하면 'Kali'에서 작업한 '문서(index.html)'의 내용이 출력된다.</li>
</ul>
<hr />
<h2 id="64-phishing-site">6.4 Phishing Site</h2>
<h3 id="개요-10">개요</h3>
<ul>
<li><p><code>피싱(Phishing)</code>이란 <code>개인 정보(Private data)</code>와 <code>낚시의 피싱(Fishing)</code>의 합성어로 <code>개인 정보를 낚시</code>한다는 의미를 지니고 있다.</p>
</li>
<li><p>이 <code>DNS Spoofing</code>을 이용한 네이버와 동일한 창을 만든 후 로그인을 유도하는 <code>피싱 사이트</code>를 만들 수 있다.</p>
</li>
<li><p><code>로그인 버튼</code>을 클릭한 후 <code>아이디</code>와 <code>비밀번호</code>를 입력할 때 패킷을 분석, 정보를 빼낼 수가 있다.</p>
</li>
</ul>
<h3 id="실습환경nat-1">실습환경(NAT)</h3>
<ul>
<li><code>Kali</code><ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
<li><code>Windows 10</code><ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
</ul>
<h3 id="실습-1-loginhtml-파일을-이용한-사이트-출력">실습 1. login.html 파일을 이용한 사이트 출력</h3>
<ul>
<li><code>kali</code>에서 <code>/var/www/html/login.html</code> 생성</li>
<li><code>kali</code>에서 <code>wireshark</code>를 실행시킨 후 <code>windows 10</code>의 웹 브라우저에서 입력, 실행 한 후 해킹된 내용을 확인한다.<ul>
<li>앞에서 실행해 놓은 <code>Ettercap-graphical</code>은 무조건 실행이 되어 있어야 한다.</li>
</ul>
</li>
</ul>
<h3 id="실습-2-navercom의-소스를-퍼다가-피싱-사이트-만들기">실습 2. naver.com의 소스를 퍼다가 피싱 사이트 만들기</h3>
<ul>
<li><code>FTP 서비스 활성화</code><ul>
<li>패키지 설치</li>
<li>포트 추가</li>
</ul>
</li>
<li>FTP 서비스 환경 설정
<code>sudo vi /etc/vsftpd.conf</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/708fe60d-3715-4ac9-9b72-15ed8d1200ee/image.png" /><ul>
<li>기본적으로 <code>Kali</code>에서는 <code>FTP 서비스</code>가 <code>비활성화</code> 되어 있다.</li>
</ul>
</li>
<li><code>Host OS</code>에서 접속하기<ul>
<li>네이버 웹 사이트에서 우클릭 후 <code>페이지 소스 보기</code>를 클릭</li>
<li>소스를 모두 선택한 후 임의의 드라이브에 <code>index.html</code>파일로 저장<ul>
<li><code>ftp</code>로 전송</li>
<li><code>sudo chmod 755 /home/samadal</code></li>
</ul>
</li>
<li><code>kali</code>에 업로드 후 기본 경로로 이동<ul>
<li><code>sudo mv index.html /var/www/html/</code></li>
</ul>
</li>
<li>문서 파일 권한 변경<ul>
<li><code>sudo chmod 755 index.html</code></li>
</ul>
</li>
<li>앞에서 실행했던 웹브라우저에서 <code>새로고침(F5)</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/dfe9a27c-1522-489d-83b9-1fdf300cb256/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="span-style--colorskyblue07-ddos-attack분산-서비스-거부-공격span"><span style="color: skyblue;">07. DDoS Attack(분산 서비스 거부 공격)</span></h1>
<h2 id="71-dos--ddos-공격-정리">7.1 DoS &amp; DDoS 공격 정리</h2>
<h2 id="✅-dos-denial-of-service-attack">✅ DoS (Denial-of-Service Attack)</h2>
<ul>
<li><p><strong>정의</strong>: 서비스 거부 공격. 시스템의 <strong>리소스를 고갈(과부하)</strong> 시켜 정상적인 사용을 방해하는 공격 방식.</p>
</li>
<li><p><strong>공격 방식 예시</strong></p>
<ul>
<li>특정 서버에 <strong>수많은 접속 시도</strong>를 유도해 다른 이용자가 정상 이용 불가하게 만듦.</li>
<li>서버의 <strong>TCP 연결 자원</strong>을 바닥냄.</li>
</ul>
</li>
<li><p><strong>공격 목적</strong></p>
<ul>
<li>서비스의 일시적 또는 영구적 <strong>기능 마비 및 중단</strong> 유도.</li>
</ul>
</li>
<li><p><strong>주요 표적</strong></p>
<ul>
<li>은행, PG사(신용카드 결제 게이트웨이), 루트 네임 서버 등 <strong>중요한 인터넷 서비스</strong>.</li>
</ul>
</li>
<li><p><strong>실제 사례</strong></p>
<ul>
<li><code>2002년 10월 22일</code>, <code>2007년 2월 6일</code>: DNS 루트 서버를 향한 대규모 <strong>DDoS 공격</strong> 발생
→ 인터넷 URL 체계 무력화 시도, 전 인터넷 대상 공격.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="✅-ddos-distributed-denial-of-service-attack">✅ DDoS (Distributed Denial-of-Service Attack)</h2>
<ul>
<li><p><strong>정의</strong>: 분산 서비스 거부 공격. 여러 대의 공격자를 통해 <strong>동시에 다발적으로 DoS 공격</strong>을 수행하는 방식.</p>
</li>
<li><p><strong>위법성 및 정책 위반</strong></p>
<ul>
<li><strong>IAB</strong>의 '정당한 인터넷 사용 정책'에 위배.</li>
<li><strong>대다수 ISP의 정책</strong>에서도 허용되지 않음.</li>
<li><strong>각국 법률</strong>에도 저촉됨.</li>
</ul>
</li>
</ul>
<h3 id="📌-iab-internet-architecture-board">📌 IAB (Internet Architecture Board)</h3>
<ul>
<li><p><strong>설명</strong>: ISOC 산하의 인터넷 기술·엔지니어링 감독 위원회.</p>
</li>
<li><p><strong>주요 역할</strong></p>
<ul>
<li><strong>IRTF</strong> (Internet Research Task Force)와
<strong>IETF</strong> (Internet Engineering Task Force) 등의 <strong>기술 위원회 감독</strong>.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="72-포트-스캔을-이용한-ddos-attack">7.2 포트 스캔을 이용한 DDoS Attack</h2>
<h3 id="개요-11">개요</h3>
<p><code>DNS Server</code>에 <code>DDoS Attack</code>을 감행하고 네트워크(망)을 마비시키는 작업이다.</p>
<h3 id="실습환경-host-only">실습환경 (Host-only)</h3>
<ul>
<li><code>Kali</code>(Attacker)<ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li><code>CentOS</code>(Victim)<ul>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.130, 192.168.10.131</code></li>
</ul>
</li>
<li><code>Windows 10</code>(Zombie PC)<ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.128</code> / <code>192.168.10.128</code></li>
</ul>
</li>
</ul>
<h3 id="hping3">hping3</h3>
<ul>
<li><p>개요</p>
<ul>
<li><p><code>ping</code> 명령과 달리 <code>ICMP</code> 패킷을 포함한 <code>TCP/UDP/ICMP</code> 등의 패킷 전송을 할 수 있다.</p>
</li>
<li><p>주로 Port Scanning을 하거나 <code>MTU</code>(Maximum Transmission Unit)를 확인할 수 있다.</p>
</li>
</ul>
</li>
<li><p>사용법</p>
<pre><code class="language-bash">hping3 [옵션] &lt;Target IP Address&gt;</code></pre>
</li>
<li><p>실습 1. <code>Kali</code> -&gt; <code>CentOS DNS</code></p>
<ul>
<li><p>개요</p>
<ul>
<li><code>TCP Sync</code> (TCP(요청과 응답이 공존. UDP(요청)) 프로토콜과 연동되고 있는) 패킷을 보내면 <code>flags=SA(Sync/Ack)</code>로 응답이 온다.</li>
</ul>
</li>
<li><p>실행</p>
<ul>
<li><code>sudo hping3 -S www.gusiya.com -p 80 -c 5</code></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a718b738-8907-4804-bc6f-2c6dde8967ea/image.png" /></li>
</ul>
</li>
<li><p>결론</p>
<ul>
<li><code>동기 신호 전송(Sync)</code>후 <code>반송(Sync/Ack)</code> 되면 <code>TCP</code>가 완료<code>(3-Way HandShake)</code>되고 다시 전송을 하기 위해 연결 준비 상태(RST, Connection Reset)로 전환된다.</li>
</ul>
</li>
</ul>
</li>
<li><p>실습 2. <code>Kali</code> -&gt; <code>Windows 10</code></p>
<ul>
<li><p><code>테스트 1.</code> 기본 상태(포트를 별도로 지정하지 않은 상태)</p>
<ul>
<li><code>sudo hping3 -S 192.168.10.131 -c 5</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0fbcf04e-3b3d-4918-9e2c-379098faf66a/image.png" /></li>
<li>동기 신호 전송(Sync)만 전송 되고 반송 및 리셋 패킷은 나오지 않는다.</li>
</ul>
</li>
<li><p><code>테스트 2.</code> 임의 포트(포트를 2개 ~ 3개 추가)</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c1c54a19-bc6d-433d-a3c8-8a14ac6dea05/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/675a6ea0-4a05-49da-b9f6-66f00cdfe87d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/79315489-edd2-4cca-bc91-06eba6646c91/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/19647f1d-9797-4443-b882-f26970df6df7/image.png" /></li>
<li><code>sudo hping3 -S 192.168.10.131 -p 21 -c 5</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c74d2bea-2177-4bc8-92f2-4aa55bf043b4/image.png" /></li>
<li>포트만 추가되었고 실제 서비스가 동작중이지 않기 때문에 <code>테스트 1</code>과 별다른 차이점이 </li>
</ul>
</li>
</ul>
</li>
<li><p>실습 3. (DDoS Attack) <code>공격 대상 시스템 (CentOS)</code>에 <code>무작위(Random)</code>의 IP 주소를 계속 보낸다.</p>
<ul>
<li>개요 <ul>
<li><code>DNS Server</code>에 <code>DDos Attack</code>을 감행하고 네트워크(망)을 마비시키는 작업이다.</li>
</ul>
</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/efc9842b-5181-4f37-8e23-0a6a9c139d3d/image.png" /></li>
<li><code>sudo hping3 --rand-source 192.168.10.128 -p 1-1024 -S --flood</code> <ul>
<li><code>--rand-source</code> <code>(무작위)</code></li>
<li><code>192.168.10.129</code> <code>(공격 대상 IP)</code></li>
<li><code>-p 1-1024</code> <code>(스캐닝할 포트)</code></li>
<li><code>-S</code> <code>(TCP flag SYN)</code></li>
<li><code>--flood</code> <code>(플로딩, Flooding)</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="span-style--colorskyblue08-vpnspan"><span style="color: skyblue;">08. VPN</span></h1>
<h2 id="81-일반">8.1 일반</h2>
<h3 id="개요-12">개요</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0286a6c1-4304-40ae-9766-122b60d19566/image.png" /></p>
<ul>
<li>가상 사설망을 말한다.</li>
<li>회사의 본사와 지사들의 네트워크를 독점적으로 구성하는 <code>기업 전용선</code>의 <code>장점</code>을 그대로 이용하고 <code>단점</code>인 비용이 비싸다는 문제를 해결해주는 서비스를 말한다.</li>
<li>큰 범위에서의 <code>인트라넷(Intranet)</code>과 같은 망 구성을 가지고 있다.</li>
</ul>
<h2 id="82-실습-1">8.2 실습 1.</h2>
<h3 id="시스템-구성">시스템 구성</h3>
<ul>
<li><p><code>VPN Server 1대(SRV100)</code>의 <code>VPN Client 1대(Client100)</code></p>
<blockquote>
<ul>
<li><code>VPN Server(SRV100)</code></li>
</ul>
</blockquote>
<ul>
<li>기본 설정<ul>
<li><code>라우팅 및 원격 액세스</code> -&gt; <code>SRV100</code> 우클릭 후 사용 안 함 -&gt; 구성 및 사용 </li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ada0dfca-6fb5-406a-96e0-919b64e9988b/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/256030fb-4073-452b-a857-ec075d5fd3be/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/04f52269-122b-486a-9d8b-cb0a65a6f4f9/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4aa61747-5931-4358-8a6d-eb8172591a60/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ccc28758-5c26-4a3f-9d9e-edb7f3360daf/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8eaca739-5198-460e-964e-9ff33dfc961b/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/73191a5b-ae05-4ced-ba37-ce01fbd9aecc/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/94076cc9-a509-4cc5-8dc1-ad3af848f8b3/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ed8f3249-4505-4bf5-b20d-2c07f5b672a7/image.png" /></li>
</ul>
</li>
<li><code>VPN Service</code>를 사용할 사용자 생성 <code>(SRV100)</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/28a757ff-329c-45e7-94e7-e28ce243a0c5/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c7b4531b-0a5e-46c0-9b5f-a36e437d648d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/96cfd964-8dbc-4724-bffa-6ad511a3cfee/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/228c9cdb-cffb-4e53-8f2b-7ff69833066a/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p><code>VPN Client(Client 100)</code></p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4de8cd44-12c7-46d8-a2f3-26d0158be8e9/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/104869a7-9976-4df4-99d5-116d80976caf/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b848091b-e613-4168-a6f1-f7c6d727c38d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/acd9f216-357d-496b-9fef-9e10939f6e1e/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ab3e42d7-c070-4931-91bf-91ecd7500ec4/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/348f0553-5a52-4d5d-9ce3-54e3ce047af8/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3c385906-5e99-4701-9e6c-afdae4dd579d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/22482be6-734b-4803-b39e-2495cee47833/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0dde78a7-b0f3-42e1-b22b-9c5163185172/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f8546b23-9b61-4656-9e24-6f57183fd07c/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4d9c411d-70a2-42e2-bdeb-af16e3bd3b8e/image.png" /></li>
<li><code>server</code>에서 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4523be65-a3e2-465f-8547-1c549867ddf5/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0d86c879-e2e9-4343-bf48-375b094b7c6b/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h1 id="span-style--colorskyblue09ipsec-internet-protocol-securityspan"><span style="color: skyblue;">09.IPSec (Internet Protocol Security)</span></h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9cc9f501-562c-4923-b7a3-50107b48e72c/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c57a6bb0-1288-4c9f-9a78-57e6d49e8804/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/de5e49a0-c805-43a5-8939-a5385e35eac7/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/368025dc-2788-42db-abe4-b1c728b74830/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f6e42fbd-1972-41a0-b2c2-62108e62f980/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4ae05461-f279-4dae-b9db-1747adc7f246/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f681a2f3-8160-4b50-96d6-12e871de7e80/image.png" /></p>
<h2 id="91-일반">9.1 일반</h2>
<h3 id="개요-13">개요</h3>
<h2 id="92-실습">9.2 실습</h2>
<h3 id="psk">PSK</h3>
<ul>
<li><p>시스템 구성</p>
<ul>
<li><code>SRV 100</code> , <code>Client100</code></li>
</ul>
</li>
<li><p>환경 구성</p>
<ul>
<li><code>HtoH</code>, <code>wf(x)</code> + <code>PSK</code></li>
</ul>
</li>
<li><p>설정 및 테스트</p>
<ul>
<li><p>Step 1.<code>SRV100</code> 또는 <code>Clinet100</code>에서 <code>wireshark</code>를 실행한 상태에서 <code>ping</code> 테스트를 실행한다.</p>
</li>
<li><p>Step 2. <code>wireshark</code>에 올라온 <code>Protocol</code>을 확인<code>(ICMP)</code> <code>SRV100</code>과 <code>Client100</code> 모두 동일한 결과가 나타난다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b2027c42-371e-4aea-8e4b-155507914c18/image.png" /></p>
</li>
<li><p>Step 3. <code>SRV100</code>에서 <code>로컬 보안 정책(secpol.msc)</code>을 </p>
</li>
<li><p>Step 4. <code>보안 설정</code> 하단에 있는 <code>IP 보안 정책</code>의 우측에서 우클릭 후<code>IP 보안 정책 만들기</code>를 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1a699d21-ad66-4769-8360-5d78513e77f2/image.png" /></p>
</li>
<li><p>Step 5. 기본값으로 둔 상태에서 계속 진행한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9a27876c-f7ca-419e-80c9-f2f863397209/image.png" /></p>
</li>
<li><p>Step 6. <code>새 IP 보안 정책 속성</code>창이 출력되면 하단에 있는 <code>추가</code>를 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9aea2cd0-5b76-4577-9fdb-b493fdf632c8/image.png" /></p>
</li>
<li><p>Step 7. <code>IP 필터 목록</code> 탭 하단에 있는 <code>추가</code>를 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a99bfa97-ce09-4e1e-8915-82aedbb1b72a/image.png" /></p>
</li>
<li><p>Step 8. 상단에 있는 <code>추가</code>를 클릭한다. 이 때 하단에 있는 <code>추가 마법사 사용</code>은 반드시 <code>체크 해제</code>해야 한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1aa5514c-55f4-4777-8317-436c03c2ddb1/image.png" /></p>
</li>
<li><p>Step 9. <code>주소</code> 탭에서 다음과 같이 선택, 입력한다.
<code>원본 주소</code> → <code>내 IP 주소</code>를 선택한다. <code>대상 주소</code> → <code>특정 IP 주소 또는 서브네트</code>를 선택한다. <code>(192.168.100.20)</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/17cd5b1b-e453-430d-bd22-b426e1d83081/image.png" /></p>
</li>
<li><p>Step 10. <code>확인</code>을 몇 번 누르면 <code>IP 필터 목록</code> 탭 하단에 추가된 필터가 보인다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/38a690f5-eef6-40ab-9c8f-ac6fca75a26b/image.png" /></p>
</li>
<li><p>Step 11. 이 목록을 체크한 후 <code>필터 동작</code> 탭을 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f2ba813c-a020-435c-b5f0-9959fcc72e4e/image.png" /></p>
</li>
<li><p>Step 12. 하단에 있는 추가를 클릭한다. 이 때 하단에 있는 <code>추가 마법사 사용</code>은 반드시 <code>체크 해제</code>해야 한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1757f639-a078-40bc-b0f5-a3603f097a57/image.png" /></p>
</li>
<li><p>Step 13. <code>보관 방법</code>에서 <code>추가</code>를 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/61e92194-a062-4d08-bd40-2b208e1d7b8e/image.png" /></p>
</li>
<li><p>Step 14. 하단에 있는 <code>사용자 지정</code>에서 <code>설정</code>을 클릭한다.<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7aab2fa2-34a0-4fb2-81ae-dcc3903ea5f8/image.png" /></p>
</li>
<li><p>Step 15.  암호화되지 않은 데이터 및 주소 무결성'만 체크한 후 <code>확인</code>을 클릭한다.<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/06ffe5dd-56fd-4150-a952-2b0e3de386b9/image.png" /></p>
</li>
<li><p>Step 16. <code>확인</code>을 <code>두 번</code> 클릭한 후 <code>필터 동작</code> 탭을 보면 추가된 목록이 보인다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/703ac4eb-4a65-4d46-a14d-ebb3d626a2f2/image.png" /></p>
</li>
<li><p>Step 17. 이 목록을 체크한 후 <code>인증 방법</code> 탭을 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/60ad39c1-af06-47c9-bbb0-f69734b9f278/image.png" /></p>
</li>
<li><p>Step 18. 여기서는 새로 <code>추가</code>하지 말고 목록에 있는 <code>Kerberos</code>를 클릭한 후 <code>편집</code>을 이용해서 변경하도록 한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8655b2a4-97b6-4c46-8ff3-a9bd711ea4aa/image.png" /></p>
</li>
<li><p>Step 19. 하단에 있는 <code>이 문자열 사용(미리 공유한 키)</code>를 체크한 후 하단에 있는 빈 칸에 <code>P@ssw0rd</code>를 입력한 후 <code>확인</code>을 클릭한다.<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0ff5974f-941f-46ae-9266-1607bf01b18c/image.png" /></p>
</li>
<li><p>Step 20.<code>적용</code>을 클릭한 후 <code>확인</code>을 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/017d599c-0948-47ec-b949-a6d2af3b64ba/image.png" /></p>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cbcebb03-f711-4726-a339-a94a7308083a/image.png" /></p>
<ul>
<li><p>Step 21. <code>새 IP 보안 정책 속성</code>창의 <code>규칙</code> 탭 하단에 추가된 <code>보안 규칙</code>이 보인다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/09842dc0-6b7f-4bc4-8395-02fcebb9fca9/image.png" /></p>
</li>
<li><p>Step 22. <code>확인</code>을 클릭하면 <code>IP 보안 정책</code>의 우측에서 추가된 목록이 보인다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2ea9885d-49e2-4162-adcc-ea16a084a8d1/image.png" /></p>
</li>
</ul>
</li>
<li><p><code>Client100</code>에서의 작업</p>
<ul>
<li><code>SRV100</code>과 동일한 방법으로 설정한다.</li>
<li><code>100.10</code> 으로 바꾸는 것 제외하고 동일 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7a3150c2-6558-4981-824e-35bb5c562a4a/image.png" /></li>
</ul>
</li>
<li><p><code>테스트 2.</code></p>
<ul>
<li><code>SRV100</code> 또는 <code>Clinet100</code>에서 <code>wireshark</code>를 실행한 상태에서 <code>ping</code> 테스트를 실행한다.</li>
<li><code>wireshark</code>에 올라온 <code>Protocol</code>을 확인해보면 <code>테스트 1.</code>과 마찬가지로 <code>ICMP</code>로 나타난다. 즉, 보안 설정이 적용이 되지 않았다는 것을 알 수 있다. <ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/616882fd-1bdf-43a3-b88d-b2d7a54b3fba/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p><code>SRV100</code>과 <code>Client100</code>에서의 <code>보안 적용</code>을 위한 추가 작업</p>
</li>
<li><p><code>테스트 3.</code></p>
<ul>
<li><code>새 IP 보안 정책</code> 우클릭 후 <code>할당</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7082d5d9-5cea-4c12-8da8-fa1bf3edc47b/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4ff1abbb-0968-44a0-9b69-60161ba95f49/image.png" /></li>
<li><code>기밀성</code>이 적용 됨 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9aa1040f-efe7-428a-af46-b538d942ff93/image.png" /></li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/badac33b-4cf1-4b26-b66c-aae7c151e574/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7d7ebb06-988f-4f65-b7be-0ce3daa8b301/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9a991f8a-8b41-448a-b844-a8da1a649e11/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d770f104-4657-4ad8-9408-8abfed8a52e6/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6e12ac5a-fe20-43c4-bea8-6c9c24c4d7a8/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bb33b0c3-5d37-4eb9-8796-9086fcb7cc4c/image.png" /></p>
<p><code>Client100</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a564aa6e-5eef-4582-bcea-b93d6c784acf/image.png" /></p>
<p><code>SRV100</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e64ce1d7-cce3-453e-80a5-8d707b1cb2e1/image.png" /></p>
<p><code>SRV200</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2b17cbe1-037b-4d7d-aec4-37c21b3a478d/image.png" /></p>
<p><code>Client200</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/45c7ed03-03c2-425a-934e-93e6ee3659b5/image.png" /></p>
<blockquote>
<h3 id="결론-1">결론</h3>
<p><code>Client100</code> 네트워크(192.168.100.x)와 <code>Client200</code> 네트워크(192.168.200.x)가 서로 <code>ping</code>이 되고,
중간에 있는 <code>SRV100</code> ↔ <code>SRV200</code> 구간은 ESP로 암호화되어 안전하게 통신되고 있음.
이게 전형적인 사이트 간 <code>VPN</code> (Site-to-Site IPsec VPN) 실습 결과. 실무에서도 RRAS나 강력한 장비(Fortigate, Cisco, Palo Alto 등)로 똑같이 구성합니다.</p>
</blockquote>
<hr />
<h3 id="kerberos-생략">Kerberos (생략)</h3>
<hr />
<h3 id="ca-인증서">CA 인증서</h3>
<ul>
<li><p>시스템 구성</p>
<ul>
<li><code>SRV 100</code> , <code>Client100</code>, <code>SRV200</code>, <code>Client200</code></li>
</ul>
</li>
<li><p>환경 구성</p>
<ul>
<li><code>StoS</code>, <code>wf(o)</code> + <code>CA</code></li>
</ul>
</li>
<li><p>설정 및 테스트</p>
<ul>
<li><p>인증기관 설치 및 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/daf9f8de-a49f-4fc6-accb-e469af4329d2/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3e6fc674-5412-4b17-ac4c-2d31e32dbfe6/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/91c98001-76ee-4337-bf85-f41b278de905/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f3a9917f-194d-4632-a0a4-bc40e5ece73d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/90459d82-ed0a-49f4-9320-451d7ae68d56/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fccf14a3-17ad-44b9-9407-8c74c5496113/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/46894afe-7adc-476e-b31f-5655c9483d15/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6bf85a32-9dfe-4129-a365-9c29b51f7558/image.png" /></li>
</ul>
</li>
<li><p>인증서 설정 1. 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ee92fa4e-9b45-40dd-9088-bafefc88cd51/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1f4836c2-0b63-4527-967a-3adb513dcd29/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b4ef3d5d-bade-4581-98d5-ae639eb8b09e/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d0d74dbe-e560-4f05-a991-11615e5a6da2/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/83aaf665-74f6-421c-a2bd-131c70fc63e5/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5795dc46-0524-4923-9cbb-823cbec022cd/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/41437359-392a-4109-9529-fceedebe8bc2/image.png" /></li>
</ul>
</li>
<li><p>인증서 신청</p>
<ul>
<li><code>internet explorer</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c5099f1b-596b-4249-90a6-f3df50e51d3d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5f482b45-fc70-4140-9e78-35e7b37050e9/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c5123080-73db-4885-9856-43c88470279c/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4f8d7206-7192-4c1e-8a4d-2fa00b1ffaee/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/029ac8e8-c7b0-4865-92c5-bb510e8c6755/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2f0e905f-c0bd-463b-9059-b188113d9cd7/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/17b62ebd-a576-4cc0-a7ab-3ea0fa771b04/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7db502f5-f65a-40fc-9743-010091b2cd47/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8ecdf6bd-ac50-4c7a-abd2-5a4f83a1f3ce/image.png" /></li>
<li>위 설정이 안되어있으면 <code>제출</code>이 <code>활성화</code>가 안됨 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f5c125b9-a67a-4096-89fd-a5a2d2066d43/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fd439cff-010f-467e-b5fe-f9a33c2e48cc/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8b7f1cc5-6c57-4c88-96a8-f38bf042b676/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/53cef412-da19-41ce-abc7-0dfc0ab7761d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e825af16-f6f7-4311-bb53-cd4aae01aa4d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/213f5a42-8007-4cc0-acba-130b577c8c8a/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5f40bf20-b6d4-4484-ab5f-14e23279f4e5/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4243d283-c4d2-4b2f-9dbd-eb29477bc3b5/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/da9cb248-469d-4a93-a5b0-f5fe7fb26f2b/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f1915eca-af69-4430-8d4d-0abc17136c57/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ebb2fc0d-c8d4-4a54-adb7-b05c6d92d2ec/image.png" /></li>
<li>개인용에서 <code>F5</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5414fd76-fbc9-4626-a9fb-1a1b15b6f829/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/90e0ff92-398b-4ece-83c2-2a9cccf9e000/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/35699c9c-e97e-4e66-b96b-a4205d8916b6/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a873772c-547e-419d-a9c4-d58684488241/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0321d895-d6aa-4327-a932-8127aa8d71a7/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ff380927-0f33-492c-8af6-256b45640879/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2c46d159-6150-458a-a845-611aa592c5c5/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b8e2e863-513b-4599-8ff4-79afe9be3cee/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/84ec3cf9-b63e-4d29-9fdd-fdd16dacd293/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5a5eca92-ec10-4c5e-ae6a-362e649f1b99/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2d834732-7c7e-4aa8-9648-ba61004eca4a/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/51109773-eef6-4152-9450-c524c2da945f/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1d826dc9-f7d3-4f71-9521-9d2801269950/image.png" /></li>
</ul>
</li>
<li><p><code>Client100</code>에서 작업</p>
<ul>
<li><p><code>mmc</code>에서 사용자 , 로컬 컴퓨터 추가 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d205d828-b399-4a69-923e-51718a7f1f64/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f6bb2889-be61-4ba2-a56b-dc05c83aa71a/image.png" /></p>
</li>
<li><p>인터넷 옵션에서 허용 설정</p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/84937f32-e2b8-432a-993f-b47860e29d34/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/94a8a14a-1624-4277-b0ec-987c4212ce34/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/131bdda8-dad5-4d89-85c8-51f92dd0b62e/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/04087a46-2abd-4839-8060-87fcfadf62e1/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/62e7b40d-b146-4b88-8047-0c31ffbc2e94/image.png" /></p>
</li>
<li><p><code>F5</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7a16a033-779a-4abf-bc07-72039067dca3/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2d69de53-9903-47b8-a5d4-38c5cbb06497/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3d6976db-8ff6-49d6-9624-a88c737e37ce/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c0f72fbb-7109-4517-89dc-1d5d85e50078/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8ecdf6bd-ac50-4c7a-abd2-5a4f83a1f3ce/image.png" /></p>
</li>
<li><p><code>SRV100</code>에서 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/80230f23-3323-4eed-85ff-d977a06fb858/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2919fd3c-69f9-4eae-81e7-3344878b7d23/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7254cb4a-be6b-45b8-aec9-db421597a75a/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4e923a56-3de5-48d3-abda-e6a29d46e86b/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/45ff6e6f-ae44-4526-b72d-804ffdf7bced/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/dd5da0e3-012b-4d33-bfe3-fff0480f61d9/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bb95ccfd-18ea-4887-878e-2f035d1b3844/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/11dc138d-003b-47a1-9b82-a4fe03f5e689/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1887e7ba-d485-4c73-84f7-f271645093e5/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1674df1c-fada-42b4-84df-ce97db1baf3d/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e97f3328-12fd-43c4-a1fe-c135bf432b65/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4f99dbc2-a5a2-46be-94b7-0e47efa33da8/image.png" /></p>
</li>
<li><p><code>H to H</code>만 된상태<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ab701a7e-756b-4f85-bfa0-c232798e6270/image.png" /></p>
</li>
<li><p><code>secpol.msc</code>에서 작업<code>(srv100)도 작업</code></p>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a7911161-9ead-4747-a47d-db3cfc2b44d0/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5bf3e3f4-e53e-4dbe-9b74-077acaff1ad9/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/94129b42-ea8a-4862-b0aa-240ff4fe6d4d/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4006be5a-5103-4931-870f-ff140900deda/image.png" /></p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="span-style--colorskyblue10-proxy-serverspan"><span style="color: skyblue;">10. Proxy Server</span></h1>
<h2 id="101-일반">10.1 일반</h2>
<h3 id="개요-14">개요</h3>
<ul>
<li>초창기에는 <code>트래픽 분산 프로그램</code>이었다.</li>
<li><code>자유-오픈 소스</code>에서 말하길 <code>네트워크 침입 차단 시스템(NIPS: Network Intrusion Prevention System)</code>이자,</li>
<li><code>네트워크 침입 탐지 시스템(NIDS: Network Intrusion Detection System)</code>의 표준이다.</li>
<li><code>Role(롤, 미리 정해 놓은 규칙)</code> 기반의 패턴 매치 기법이 추가되고 <code>PCRE(Perl Compatible Regular Expressions)</code>를 이용한 정규표현식을 지원하면서 <code>IDS/IPS</code>의 기술 표준으로 자리 잡았다.</li>
<li><code>방어자 시스템(희생자 시스템)</code>에 <code>Snort</code>를 설치해야 하는데 이제부터 하는 작업에서의 방어자 역할 시스템은 <code>Kali</code>를 이용한다.</li>
</ul>
<h3 id="ids탐지">IDS(탐지)</h3>
<ul>
<li><code>Role(롤, 미리 정해 놓은 규칙)</code> 기반의 패턴 매치 기법으로 악의적인 공격 시도를 탐지하여 <code>내부 자산의 피해를 최소화하기 위한 시스템</code>을 말한다.<h3 id="ips차단">IPS(차단)</h3>
</li>
<li><code>IDS</code>와 같이 <code>패턴 매치 기법으로 공격을 탐지</code>하고 <code>차단 및 방어 기능도 포함</code>한 시스템을 말한다.</li>
</ul>
<h3 id="daq-data-acquisition">DAQ (Data Acquisition)</h3>
<ul>
<li>Data 수집을 의미한다.<h2 id="102-snort">10.2 Snort</h2>
<h3 id="환경구성">환경구성</h3>
</li>
<li><code>SamVM1763_Kali20234_20240202.zip</code></li>
<li><code>apt-key</code> 문제 때문이다.</li>
</ul>
<h3 id="기본-작업">기본 작업</h3>
<ul>
<li><code>Kali</code> (NAT)<ul>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
</ul>
<h3 id="웹을-통해-나타나는-일반적인-유형">웹을 통해 나타나는 일반적인 유형</h3>
<ul>
<li><code>Request</code> 와 <code>Response</code>를 판단할 수 있는 요령이니까 꼭 암기하도록 한다.</li>
<li><code>HTTP Request</code><ul>
<li><code>GET/HTTP/1.1</code></li>
</ul>
</li>
<li><code>HTTP Reponse</code><ul>
<li><code>HTTP/1.1 200 OK</code></li>
</ul>
</li>
</ul>
<h2 id="102-web-proxy">10.2 Web Proxy</h2>
<h3 id="개요-15">개요</h3>
<ul>
<li><code>Client</code>가 <code>Server</code>로 접속할 때 <code>Proxy Server</code>를 통하게 되면 <code>Server</code>에서는 <code>Client</code>의 <code>IP</code>는 모르고 <code>Proxy Server의 IP</code>만 알기 때문에 변조가 가능하다.</li>
<li><code>IP</code>를 변조하고자 할 때 많이 사용한다.</li>
<li>일반적으로 '방화벽'이라고 많이 부르기도 한다.</li>
<li>PC와 인터넷 사이의 통신을 할 때 중개인 역할을 한다.</li>
</ul>
<h3 id="📌-proxy-server">📌 Proxy Server</h3>
<ul>
<li>다른 네트워크 서비스에 <strong>간접적으로 접속</strong>할 수 있게 해주는 서버.</li>
<li>원래 목적: <strong>캐시(Cache)</strong>를 사용해 <strong>리소스(Resource) 접근 속도 향상</strong>.</li>
<li>현재는 <strong>보안, 통제</strong>, 그리고 웹 요청/응답을 <strong>감시 및 수정</strong>하는 용도로도 활용.</li>
</ul>
<h3 id="🌐-web-proxy">🌐 Web Proxy</h3>
<ul>
<li><p>웹 요청을 <strong>임시 저장소(Cache)</strong>를 통해 전달하는 <strong>중개자 역할</strong>.</p>
</li>
<li><p><strong>브라우저(Client)</strong>와 <strong>서버(Server)</strong> 간 통신 시, 중간에 위치하여 데이터를 <strong>재전송</strong>.</p>
</li>
<li><p>프록시 사용 시, <strong>Client–Server 간의 패킷 내용을 중간에서 확인</strong> 가능.</p>
</li>
<li><p>(핵심) <code>Web Proxy</code>는 프로그램을 의미하는데 이 프로그램이 설치된 컴퓨터를 <code>Proxy Server</code>라고 한다.</p>
</li>
</ul>
<hr />
<h2 id="102-web-proxy-1-odysseus">10.2 Web Proxy 1. Odysseus</h2>
<h3 id="실습-1-로컬-without-db-server">실습 1. 로컬 without DB Server</h3>
<ul>
<li><p>작업 </p>
<ul>
<li><p>악성코드를 심어서 보낸 후 실행해 놓고 로그 파일을 편취한다.</p>
</li>
<li><p>해킹 도구에 대한 강의 후 진행</p>
<blockquote>
<ul>
<li>작업환경 구성(NAT)</li>
</ul>
</blockquote>
</li>
<li><p>테스트용 시스템</p>
<ul>
<li><code>CentOS</code> / <code>Rocky</code></li>
<li><code>Server</code> 설치<code>(DNS, Web Server, FTP Server, DB Server)</code></li>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li><p><code>Web Proxy</code></p>
<ul>
<li><code>Windows 10</code>에 설치한다.</li>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
</ul>
</li>
<li><p><code>Odysseus</code> 다운로드</p>
</li>
<li><p><code>Proxy</code> 실행 시 특히 신경 쓸 내용</p>
<ul>
<li><code>Proxy Tools</code>을 실행하면 웹 브라우저의 프록시에 설정 내용 그대로 반영이 된다. 즉, 변경된다.</li>
<li>따라서 시스템 트레이에서 종료가 되더라도 변경된 Proxy가 적용된 상태가 된다.</li>
<li>따라서 웹브라우저를 실행하고 사이트를 입력해도 정상적으로 출력되던 사이트도 뜨질 않는다.</li>
<li>이럴 때는 시스템을 재부팅하지 말고 <code>Odysseus</code>에서 우클릭 후 <code>IE Proxy Settings</code>을 <code>None</code>으로 변경하면 된다.</li>
</ul>
</li>
<li><p>작업 1. 기본 웹 문서 출력</p>
<ul>
<li><p>네임서버 조회</p>
</li>
<li><p>기본 웹 문서 파일 생성</p>
<ul>
<li><code>chmod 701 /export/home/samadal/</code></li>
<li><code>vi /etc/httpd/conf/httpd.conf</code></li>
<li><code>vi index.html</code></li>
</ul>
</li>
<li><p>사이트 출력 1. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ff8903b8-6b44-4d1b-b71c-ea2ba45967ce/image.png" /></p>
</li>
<li><p><code>Odysseus</code> 실행 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1059e784-cb2a-4859-b9ee-7c14703cc669/image.png" /></p>
</li>
<li><p><code>Odysseus</code> 옵션 체크 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0b8b39dd-593c-4794-bb49-24cfc3a58da3/image.png" /></p>
</li>
<li><p>사이트 출력 2. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ef3a809f-06e3-467b-acff-1bec41122953/image.png" /></p>
</li>
<li><p>로그 확인</p>
<ul>
<li>2가지 방법<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7a0696b6-59ce-4c97-9299-7067b74f8f9b/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d8e4f8a3-4575-4b83-8182-64771c35f3ad/image.png" /></li>
</ul>
</li>
</ul>
<blockquote>
<ul>
<li><code>HTTP Request</code></li>
</ul>
</blockquote>
<ul>
<li><code>GET/HTTP/1.1</code><ul>
<li><code>HTTP Reponse</code></li>
</ul>
</li>
<li><code>HTTP/1.1 200 OK</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li><p>작업 2. <code>login.html</code>을 기본 경로에 <code>index.html</code>로 변경</p>
<ul>
<li><p>소스 파일 업로드 </p>
</li>
<li><p>로그 분석 하기 전에 가장 먼저 할 일</p>
<ul>
<li>사이트에 히스토리 정보 모두 삭제</li>
<li><code>Odysseus</code>의 체크 항목 모두 해제 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/85f42d87-cfc2-4a90-8909-eb19d982f67c/image.png" /></li>
<li>작업 관리자에서 <code>Odysseus</code> 종료 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8ac85d7c-7e5d-4479-8edf-961d11f0bb16/image.png" /></li>
<li>윈도우 탐색기에서 로그 파일 삭제 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/240764bf-1f63-4017-b098-f3c65d406f59/image.png" /></li>
</ul>
</li>
<li><p>로그 분석 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1217ae09-ceb5-4303-88c1-77ae36e61239/image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="실습-2-로컬-with-db-server">실습 2. 로컬 with DB Server</h3>
<blockquote>
<ul>
<li>작업환경 구성(NAT)</li>
</ul>
</blockquote>
<ul>
<li>테스트용 시스템<ul>
<li><code>CentOS</code> / <code>Rocky</code></li>
<li><code>Server</code> 설치<code>(DNS, Web Server, FTP Server, DB Server)</code></li>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
</ul>
<ul>
<li><p>선수 작업</p>
<ul>
<li><code>Odysseus</code> 관련 모드 서비스를 종료</li>
<li><code>DB Server</code> 구축</li>
<li><code>Apache Web Server</code> 구축</li>
<li><code>FTP Server</code> 구축</li>
<li>방화벽에서 포트 추가 및 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/57efaa80-a386-4e18-b2fc-5a1a5171786c/image.png" /></li>
<li><u><a href="https://velog.io/@kyk02405/Cloud-DX-16-phpmyadmin-Zeroboard"><strong><code>php 7.4 설치 링크</code></strong></a></u> </li>
<li>테스트 페이지 출력 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f2322dca-1dab-492b-8437-e1953c1948e8/image.png" /></li>
</ul>
</li>
<li><p><code>zeroboard</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2b8c04eb-7e19-48b4-9ed7-e8925f00d1d4/image.png" /></p>
</li>
<li><p><code>Odysseus</code></p>
<ul>
<li>제로보드 로그인 방식 변경 <ul>
<li><code>설정</code> -&gt; <code>동의</code> -&gt; <code>회원</code> -&gt; <code>회원가입</code> -&gt; <code>설정 변경</code> -&gt; <code>검색 기록</code>, <code>로그 파일</code> 삭제 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a2c53ee4-1fc6-4722-99fe-231c3a7a1665/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p><strong><code>302의 의미</code></strong></p>
<ul>
<li><p><strong>302 리다이렉트</strong>라고 하며, 요청한 <em>리소스가 임시적으로 새로운 URL로 이동했음(Temporarily Moved)</em>을 나타낸다.</p>
</li>
<li><p>따라서 <strong>브라우저 주소창의 URL은 변경되지 않고</strong>, <em>기존 URL</em>을 그대로 유지한다.</p>
</li>
<li><p>이는 <strong>기존 URL을 유지하면서</strong>, 실제 콘텐츠는 <em>새로운 URL</em>에서 조회되고 있음을 의미한다.</p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/718203c9-985c-4f8b-af7d-d660977792e6/image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="103-web-proxy-paros">10.3 Web Proxy: Paros</h2>
<h3 id="개요-16">개요</h3>
<ul>
<li><span style="color: red;">(핵심)</span> <strong>Paros</strong>는 <em>웹 사이트의 취약점 분석</em>뿐만 아니라 <em>웹 해킹 도구</em>로도 활용된다.  </li>
<li><em>Web Server*와 *Client</em> 사이에 위치하여 통신을 가로챈다.</li>
<li><em>HTTP</em>, <em>HTTPS</em> 데이터는 물론 <em>Cookies</em>, <em>Form 필드</em> 등을 중간에서 <strong>모니터링</strong>하거나 <strong>변조</strong>하여 서버로 전송할 수 있다.</li>
<li>Paros로 유입된 패킷은 <strong>일시 정지</strong> 후 <strong>변조</strong>되어 나가며, 이 과정에서 잠시 멈출 수 있다.</li>
<li><span style="color: red;">(특징)</span> <strong>GUI 환경(GUI Mode)</strong> 전용 도구로, <strong>CLI 환경(CLI Mode)</strong>에서는 실행되지 않는다.  </li>
<li><span style="color: red;">(중요)</span> <strong>32bit 전용 도구</strong>로, 사용을 위해 <strong>32bit 설치 파일</strong>이 필요하다.</li>
</ul>
<hr />
<blockquote>
<h3 id="작업환경-구성nat">작업환경 구성(NAT)</h3>
</blockquote>
<ul>
<li>테스트용 시스템<ul>
<li><code>CentOS</code> / <code>Rocky</code></li>
<li><code>Server</code> 설치<code>(DNS, Web Server, FTP Server, DB Server)</code></li>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li>웹 프록시용 시스템<ul>
<li><code>Windows 10</code>에 <code>Web Proxy</code>를 설치한다.</li>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li>필요한 프로그램<ul>
<li><code>Paros</code>, <code>Wireshark</code>, <code>JRE</code></li>
</ul>
</li>
</ul>
<hr />
<h3 id="일반">일반</h3>
<ul>
<li>필수사항<ul>
<li><code>Windows</code>에서 사용되는 <code>Paros</code>는 <code>32bit</code> 전용이기 때문에 반드시 모든 소프트웨어를 <code>32bit</code>로 설치해야 한다.</li>
</ul>
</li>
<li>설정 전에 확인할 내용</li>
</ul>
<h3 id="java-관련">Java 관련</h3>
<ul>
<li><p><code>Java</code> 설치</p>
<ul>
<li><code>JDK</code> 다운로드 및 설치<ul>
<li>다운로드</li>
<li>설치</li>
<li>확인</li>
</ul>
</li>
<li>시스템 환경 변수 설정 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/490c03a6-8ee3-40aa-9ece-d74dd03a7df7/image.png" /></li>
</ul>
</li>
<li><p><code>Apache ANT</code> 설치</p>
<ul>
<li>개요<ul>
<li>'Apache ANT'는 '자바 프로그래밍 언어'에서 사용하는 '자동화 된 소프트웨어 빌드(소스파일을 사용할 수 있도록 해주는 과정) 도구'를 말한다.</li>
<li>자바 프로젝트들을 '빌드(코드 분석, 동작할 수 있는 파일로 만들어 주는 과정)'하는데 표준으로 사용된다.</li>
<li>'Unix, Linux'의 'make'와 비슷하나 자바언어로 구현되어 있어 자바 실행환경이 필요하다.</li>
<li>'make'와 다른 점은 빌드를 위한 환경구성을 'XML 파일을 사용'한다는 것이다.</li>
<li>기본적인 빌드 파일명은, 'build.xml'이다.</li>
</ul>
</li>
<li>프로그램 다운로드 및 설치<ul>
<li><code>apache-ant-1.10.15-bin.zip</code></li>
</ul>
</li>
<li>시스템 환경 변수 설정 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cef9d4d6-081d-47c0-8c1c-0384fae187ca/image.png" /></li>
</ul>
</li>
</ul>
<h3 id="paros-설치">Paros 설치</h3>
<ul>
<li>다운로드 <code>Paros 3.2.13</code></li>
<li>설치</li>
<li>실행 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0cc14216-baab-4cef-b303-13b35ca031e4/image.png" /></li>
</ul>
<h3 id="실습-1">실습</h3>
<ul>
<li><p><code>테스트 1. without DB</code></p>
<ul>
<li><code>Windows 10</code>에서의 <code>Proxy</code> 설정<ul>
<li>수정 전 <code>(http=127.0.0.1:50000;https=127.0.0.1:50000 / x )</code></li>
<li>수정 후 <code>(127.0.0.1 / 8080 )</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1ebe4739-4ded-43c1-88f4-11133f8b9a1e/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p><code>테스트 2.</code></p>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/042c6881-479a-4373-987b-91cae2fe1b23/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/70a2d7b8-33c3-45d3-91e9-ef72ce4ae2b5/image.png" /></p>
</li>
</ul>
</li>
</ul>