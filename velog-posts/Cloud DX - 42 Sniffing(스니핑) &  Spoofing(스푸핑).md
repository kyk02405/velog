# Cloud DX - 42 Sniffing(스니핑) &  Spoofing(스푸핑)

- 📅 Published: Mon, 24 Nov 2025 08:44:29 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-42-Sniffing%EC%8A%A4%EB%8B%88%ED%95%91-Spoofing%EC%8A%A4%ED%91%B8%ED%95%91)

<hr />
<h1 id="span-style--colorskyblue05-sniffing스니핑과-spoofing스푸핑span"><span style="color: skyblue;">05. Sniffing(스니핑)과 Spoofing(스푸핑)</span></h1>
<h2 id="51-sniffing스니핑">5.1 Sniffing(스니핑)</h2>
<h3 id="개요">개요</h3>
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
<h3 id="개요-1">개요</h3>
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