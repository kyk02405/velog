# Cloud DX - 43 DNS, DHCP Spoofing (MITM Attack)

- 📅 Published: Mon, 24 Nov 2025 08:45:33 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-43-DNS-DHCP-Spoofing-MITM-Attack)

<hr />
<h1 id="span-style--colorskyblue06-dns-dhcp-spoofing-mitm-attackspan"><span style="color: skyblue;">06. DNS, DHCP Spoofing (MITM Attack)</span></h1>
<h2 id="61-용어-설명">6.1 용어 설명</h2>
<h2 id="mitm-man-in-the-middle">MITM (Man In The Middle)</h2>
<h3 id="개요">개요</h3>
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
<h3 id="개요-1">개요</h3>
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
<h3 id="개요-2">개요</h3>
<ul>
<li><p><code>피싱(Phishing)</code>이란 <code>개인 정보(Private data)</code>와 <code>낚시의 피싱(Fishing)</code>의 합성어로 <code>개인 정보를 낚시</code>한다는 의미를 지니고 있다.</p>
</li>
<li><p>이 <code>DNS Spoofing</code>을 이용한 네이버와 동일한 창을 만든 후 로그인을 유도하는 <code>피싱 사이트</code>를 만들 수 있다.</p>
</li>
<li><p><code>로그인 버튼</code>을 클릭한 후 <code>아이디</code>와 <code>비밀번호</code>를 입력할 때 패킷을 분석, 정보를 빼낼 수가 있다.</p>
</li>
</ul>
<h3 id="실습환경nat">실습환경(NAT)</h3>
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