# Cloud DX - 41 Port Scanning

- 📅 Published: Mon, 24 Nov 2025 08:41:42 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-Port-Scanning)

<hr />
<h1 id="span-style--colorskyblue04-port-scanning-span"><span style="color: skyblue;">04. Port Scanning </span></h1>
<h2 id="41-tcp-scan-nmap">4.1 TCP Scan (nmap)</h2>
<h3 id="개요">개요</h3>
<ul>
<li><code>TCP</code>를 이용한 포트 스캔을 말한다.</li>
<li><code>3-Way Handshaking(TCP 연결 과정)</code> 과정을 거친다.</li>
<li>빠른 포트 스캔을 할 수 있다.</li>
</ul>
<h3 id="nmap">nmap</h3>
<ul>
<li>포트를 스캔하기 전에 어떤 시스템이 <code>(핵심) 동작중인지를 먼저 확인</code>한다</li>
<li>응답하지 않는 시스템은 스캔을 하지 않는다.</li>
<li>가장 많이 사용하는 포트 스캔 명령어이다.<h3 id="실습환경">실습환경</h3>
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