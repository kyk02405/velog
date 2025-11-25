# Cloud DX - 44 DDoS Attack(분산 서비스 거부 공격)

- 📅 Published: Mon, 24 Nov 2025 08:46:14 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-44-DDoS-Attack%EB%B6%84%EC%82%B0-%EC%84%9C%EB%B9%84%EC%8A%A4-%EA%B1%B0%EB%B6%80-%EA%B3%B5%EA%B2%A9)

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
<h3 id="개요">개요</h3>
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