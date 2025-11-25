# Cloud DX - 40 네트워크 해킹 절차 및 호스트 식별

- 📅 Published: Mon, 24 Nov 2025 08:37:16 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-40-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%ED%95%B4%ED%82%B9-%EC%A0%88%EC%B0%A8-%EB%B0%8F-%ED%98%B8%EC%8A%A4%ED%8A%B8-%EC%8B%9D%EB%B3%84)

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
<h4 id="실습-환경">실습 환경</h4>
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