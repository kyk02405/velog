# Cloud DX - 49 IDS, IPS

- 📅 Published: Tue, 25 Nov 2025 09:21:37 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-49-IDS-IPS)

<hr />
<h1 id="span-style--colorskyblue12-ids-ipsspan"><span style="color: skyblue;">12. IDS, IPS</span></h1>
<h2 id="121-개요">12.1 개요</h2>
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
<li>Data 수집을 의미한다.<h2 id="122-snort">12.2 Snort</h2>
<h3 id="환경구성">환경구성</h3>
</li>
<li><code>SamVM1763_Kali20234_20240202.zip</code></li>
</ul>
<h3 id="실습-환경">실습 환경</h3>
<ul>
<li><code>Kali</code> (NAT)<ul>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
</ul>
<h3 id="snort-설치">Snort 설치</h3>
<ul>
<li><p><code>Kali</code>는 기본적으로 <code>Snort</code>를 위한 <code>저장소</code>(Repository)가 없다</p>
</li>
<li><p><code>저장소</code>(Repository)를 위한 소스 파일 백업</p>
<pre><code class="language-bash">mv /etc/apt/sources.list /etc/apt/sources.list.samadal</code></pre>
</li>
<li><p>업데이트 제거<code>(apt update / apt upgrade)</code> 했던 모든 정보를 제거</p>
<pre><code class="language-bash">sudo find /var/lib/apt/lists -type f -exec rm {} \;</code></pre>
</li>
<li><p><code>sources.list</code>파일 생성하고 내용 입력</p>
<pre><code class="language-bash">deb http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-backports main restricted universe multiverse
deb http://archive.canonical.com/ubuntu focal partner
deb-src http://archive.canonical.com/ubuntu focal partner</code></pre>
</li>
<li><p>지정한 공개 키 추가</p>
<pre><code class="language-bash">sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32</code></pre>
</li>
<li><p>패키지 설치를 위한 저장소 갱신</p>
<pre><code class="language-bash">sudo apt update</code></pre>
</li>
<li><p><code>Snort</code> 설치</p>
<pre><code class="language-bash">sudo apt install snort</code></pre>
</li>
<li><p>입력 시 나타나는 IP 대역은 <code>192.168.10.0/24</code>로 수정한다.</p>
</li>
<li><p>확인 </p>
<pre><code class="language-bash">sudo snort -V</code></pre>
<h3 id="실습">실습</h3>
</li>
<li><p>예제 1. 버전 확인</p>
<pre><code class="language-bash">sudo snort -V</code></pre>
</li>
<li><p>예제 2. 패킷 헤더 확인</p>
<pre><code class="language-bash">sudo snort -v /home/samadal/snort-v.log</code></pre>
<ul>
<li><p>개요</p>
<ul>
<li><code>IP</code>와 <code>TCP/UDP/ICMP</code>의 헤더 확인</li>
</ul>
</li>
<li><p>실행 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/69901e6e-81bb-4b5e-9fb2-037ec9a76c8f/image.png" /></p>
<ul>
<li>패킷 입출력에서의 탐지율 분석</li>
<li>4개는 두드러진 특징을 갖고 있다고 해석</li>
</ul>
</li>
<li><p>샥스핀 분석 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/694de067-4167-4de4-93ff-5084fa7929bd/image.png" /></p>
<ul>
<li><code>TCP</code>임에도 불구하고 <code>Source</code>와 <code>Destination</code>이 항상 같은 <code>패킷(ACK)</code>만 전송 </li>
<li><code>Snort</code>의 <code>칩입탐지(IDS)</code> 기능이 동작하고 있고 들어오는 패킷만 보인다.</li>
<li>즉, 어떤 놈이 들어오는지 <code>탐지</code> 하고 있다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li><p>예제 3. <code>IP</code>와 <code>TCP/UDP/ICMP</code>의 헤더를 출력할 때 해독된 <code>Application Layer</code>의 내용들도 함께 출력</p>
<ul>
<li><p>개요</p>
</li>
<li><p>실행</p>
<ul>
<li><code>sudo snort -vd</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b80eddc6-eb71-46df-b573-7131f1472159/image.png" /></li>
<li><code>IDS</code>가 동작하고 있으며 외부로부터 들어오는 패킷을 탐지하고 있다.</li>
<li>내부에서 외부로 나가는 패킷은 해독된 상태로 출력한다. </li>
<li><code>출력이 해독되었다</code>는 것은 문제를 드러내는 것과 동일하다. 여기서는 전혀 문제될 것이 없다. 왜? 외부로 나가는 것은 <code>IDS</code>와 무관하기 때문이다. 
즉, <code>칩입</code>이 아니기 때문이다.</li>
</ul>
</li>
<li><p>샥스핀 분석 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f1341d72-eedf-4377-acb6-ccbc722df2bf/image.png" /></p>
<ul>
<li><code>snort -v</code>와 동일한 내용이 출력된다. </li>
</ul>
</li>
</ul>
</li>
<li><p>예제 4. <code>Ethernet</code> 헤더 확인</p>
<ul>
<li>실행 <ul>
<li><code>sudo snort -vde</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/45f31c60-f367-4232-b90d-57fc7a40c0f0/image.png" /></li>
</ul>
</li>
<li>로그 파일 생성<ul>
<li>단순 로그 파일 생성<ul>
<li><code>sudo snort -vde -l /home/samadal/log</code></li>
</ul>
</li>
<li>필요한 갯수 만큼 생성 <ul>
<li><code>sudo snort -vde -l . -n 2</code></li>
</ul>
</li>
<li>로깅되는 패킷을 <code>192.168.10.0/24</code>에 한정<ul>
<li><code>sudo snort -vde -l . -n 3 -h 192.168.10.0/24</code></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p>예제 5. <code>tcpdump</code> 형식으로 로그 패킷을 전송하고 경고를 생성한다. (100Mbps 속도로 실행) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cc6187a2-4083-4f20-8958-0854c4551301/image.png" /></p>
</li>
<li><p><code>sudo snort -b -A fast -n 3</code></p>
</li>
</ul>
<hr />
<h2 id="123-snort-rule-policy룰-정책-etcsnortruleslocalrules">12.3 Snort Rule Policy(룰 정책, /etc/snort/rules/local.rules)</h2>
<h3 id="개요">개요</h3>
<ul>
<li><code>Snort</code>는 기본적으로 <code>Rule 기반(Rule Policy)</code>으로 시스템을 탐지하기 때문에 사용자가 직접 작성한다.</li>
<li><code>Rule</code>은 <code>Rule Header</code>와 <code>Rule Option</code>의 구조로 되어 있다.</li>
</ul>
<hr />
<h3 id="구성">구성</h3>
<ul>
<li><p>형태
<code>[Rule Header] [Protocol(UDP/TCP/HTTP/IP)]</code>
<code>[출발지IP] [포트] [-&gt;, &lt;&gt;] [도착지IP] [포트]
[Rule Option]</code></p>
</li>
<li><p>입력 형식</p>
<ul>
<li>'IP' 대신 '대역(CIDR 표기 형태. 192.168.10.0/24)'을 지정할 수 있다.</li>
<li>'단일 포트' 대신 '모든 포트(any)'를 지정할 수 있다.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="rule-options">Rule Options</h3>
<ul>
<li>개요<ul>
<li><code>Rule Options</code>은 여러 개를 한꺼번에 입력이 가능한데 <code>;</code>으로 구분하면 된다.</li>
</ul>
</li>
<li>자주 사용되는 <code>Rule Options</code><ul>
<li><code>msg</code><ul>
<li>메시지를 출력한다.</li>
<li>&quot;&quot;를 이용해서 앞과 뒤를 묶어주면 된다.</li>
</ul>
</li>
<li><code>sid</code><ul>
<li><code>SID(Secure ID, 식별자)</code>를 출력한다.</li>
<li><code>SID</code>는 <code>1,000,000</code>번 이상으로 주면 된다.</li>
</ul>
</li>
<li><code>content</code><ul>
<li><code>페이로드(Payload)</code> 내부에서 검색할 문자열을 출력한다.<ul>
<li><code>&quot;&quot;</code>를 이용해서 앞과 뒤를 묶어주면 된다.</li>
</ul>
</li>
</ul>
</li>
<li><code>depth</code><ul>
<li>탐지할 위치를 지정한다.<ul>
<li><code>nocase</code></li>
</ul>
</li>
<li><code>대문자</code>와 <code>소문자</code>를 구분 하지 않는다.<ul>
<li><code>resp</code></li>
</ul>
</li>
<li>지정된 응답(Response) 패킷을 전송한다.</li>
<li>종류로는 <code>rst_send, rst_rcv, rst_all, icmp_net, ...</code> 등이 있다.<ul>
<li><code>react</code></li>
</ul>
</li>
<li>패킷을 차단하거나 경고 메시지를 출력한다.</li>
<li>종류로는 <code>react:blok, ...</code> 등이 있다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="실습-1-내부에서-외부로-나가는-udptcphttp-트래픽-탐지">실습 1. 내부에서 외부로 나가는 UDP/TCP/HTTP 트래픽 탐지</h3>
<ul>
<li>백업 <pre><code class="language-bash">[samadal@kali ~]$ sudo cat /etc/snort/rules/local.rules
# $Id: local.rules,v 1.11 2004/07/23 20:15:44 bmc Exp $
# ----------------
# LOCAL RULES
# ----------------
# This file intentionally does not come with signatures.  Put your local
# additions here.</code></pre>
</li>
<li>초기 상태 확인<pre><code class="language-bash">[samadal@kali ~/log]$ sudo cat /etc/snort/rules/local.rules
# $Id: local.rules,v 1.11 2004/07/23 20:15:44 bmc Exp $
# ----------------
# LOCAL RULES
# ----------------
# This file intentionally does not come with signatures.  Put your local
# additions here.</code></pre>
</li>
<li>실행<pre><code class="language-bash">[samadal@kali ~/log]$ sudo snort -dev &gt; /home/samadal/rule-1.txt
Running in packet dump mode
</code></pre>
</li>
</ul>
<p>...</p>
<p>[samadal@kali ~/log]$ sudo cat /home/samadal/rule-1.txt
11/25-17:09:55.942494 00:0C:29:B8:FB:92 -&gt; 00:50:56:C0:00:08 type:0x800 len:0x86
192.168.10.128:22 -&gt; 192.168.10.1:58847 TCP TTL:64 TOS:0x10 ID:46550 IpLen:20 DgmLen:120 DF</p>
<pre><code>### 실습 2. Client의 웹 브라우저에서 사이트 출력(www.gusiya.com)을 시도할 때의 탐지
- 실습환경(NAT)
  - `Kali`
    - `Snort`
    - `192.168.10.130` / `C Class` / `192.168.10.2` / `192.168.10.128`
  - `CentOS/Rocky`
    - `DNS server, Web Server`
    - `192.168.10.128` / `C Class` / `192.168.10.2` / `192.168.10.128`
  - `Windows 10`
    - `192.168.10.131` / `C Class` / `192.168.10.2` / `192.168.10.128`

- `Snort Rule` 추가
```bash
[samadal@kali ~]$ sudo vi /etc/snort/rules/local.rules
# $Id: local.rules,v 1.11 2004/07/23 20:15:44 bmc Exp $
# ----------------
# LOCAL RULES
# ----------------
# This file intentionally does not come with signatures.  Put your local
# additions here
alert udp 192.168.10.0/24 any -&gt; 192.168.10.0/24 53 (msg:&quot;SSM Time&quot;; sid:1101004;)</code></pre><ul>
<li>실행<ul>
<li><code>Request (GET/HTTP/1.1)</code><pre><code class="language-bash">sudo snort -vd &gt; /home/samadal/rule-2.txt</code></pre>
</li>
</ul>
</li>
<li><code>www.gusiya.com</code> 접속<pre><code class="language-bash">sudo vi /home/samadal/rule-2.txt
</code></pre>
</li>
</ul>
<pre><code>  - ![](https://velog.velcdn.com/images/kyk02405/post/edc8412b-3350-452f-8b3e-57bee396f120/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/3300f0e4-207a-405e-afb4-ee41edd8bcb4/image.png)

### 실습 3. '내부에서 외부로 나가는 HTTP 트래픽 중에서 'GET'만 탐지 (로그 파일 확인하기)'
- `Snort rule`추가 `(칼리 GUI에서 해야함)`
```bash
/etc/snort/rules/local.rules

(local.rules 에 다음과 같은 내용 추가)

alert udp 192.168.10.0/24 any -&gt; 192.168.10.0/24 53 (msg:&quot;SSM Time&quot;; sid:1101004;)
alert tcp 192.168.10.0/24 any -&gt; any 80 (msg:&quot;GET SSM&quot;; content:&quot;get&quot;; nocase; sid:1101005;)
alert tcp 192.168.10.0/24 any -&gt; any 80 (msg:&quot;GET SSM&quot;; content:&quot;GET&quot;; sid:1101006;)</code></pre><ul>
<li>실행<ul>
<li>명령을 먼저 실행하고 ‘Windows 10’의 웹브라우저에서 사이트를 출력한 후 ‘새로고침(F5)을 여러번 누른다.<pre><code class="language-bash">[samadal@kali ~]$ sudo snort -vdc /etc/snort/rules/local.rules -i eth0 &gt; /home/samadal/snort-v.log 
Running in IDS mode</code></pre>
</li>
</ul>
</li>
<li>로그 파일 확인(/var/log/snort/)<pre><code class="language-bash">[samadal@kali ~]$ cd /var/log/snort/
</code></pre>
</li>
</ul>
<p>[samadal@kali /var/log/snort]$ ll
total 196
-rw-r--r-- 1 root adm  70028 Nov 25 18:09 alert
-rw------- 1 root adm 125566 Nov 25 18:09 snort.log.1764061774</p>
<p>[samadal@kali /var/log/snort]$ cat alert
[<strong>] [1:1101006:0] GET SSM [</strong>]
[Priority: 0] 
11/25-18:09:36.190769 192.168.10.131:52252 -&gt; 192.168.10.129:80
TCP TTL:128 TOS:0x0 ID:26113 IpLen:20 DgmLen:601 DF
<strong><em>AP</em></strong> Seq: 0xDCD097AF  Ack: 0xBB2E3C1F  Win: 0x2012  TcpLen: 20</p>
<p>...</p>
<p>[<strong>] [1:1101004:0] SSM Time [</strong>]
[Priority: 0] 
11/25-18:09:37.125781 192.168.10.131:51594 -&gt; 192.168.10.129:53
UDP TTL:128 TOS:0x0 ID:26153 IpLen:20 DgmLen:70
Len: 42</p>
<p>[<strong>] [1:1101004:0] SSM Time [</strong>]
[Priority: 0] 
11/25-18:09:37.125909 192.168.10.131:50862 -&gt; 192.168.10.129:53
UDP TTL:128 TOS:0x0 ID:26154 IpLen:20 DgmLen:70
Len: 42</p>
<p>[<strong>] [1:1101004:0] SSM Time [</strong>]
[Priority: 0] 
11/25-18:09:37.126602 192.168.10.131:51216 -&gt; 192.168.10.129:53
UDP TTL:128 TOS:0x0 ID:26155 IpLen:20 DgmLen:70
Len: 42
...</p>
<pre><code>- 앞의 `실습 1. ~ 실습 3.`에서 `msg`에 입력했던 `문자열`, `sid` 등은 모두 이곳에서 확인이 가능

---
## 12.4 Security Onion
### 개요
- 보안 업무 중 `Snort (IDS(Intrusion Detection SystemIDS, 침입 탐지 시스템))` 패턴 작업 업무에서 `Security Onion 애플리케이션`을 사용한다.
- (핵심) `모의해킹 환경`에서 `Security Onion Application`에 포함된 `IDS 기능`을 활용해서 `Snort 패턴 생성 및 테스트`를 수행한다.
- `Security Onion`은 `우분투(Ubuntu) 64bit`를 기반으로 개발되었다.

### 작업환경
- VMware 이미지 설치, Snort 패턴 작성 및 Squil 접속 확인, 서비스 명령어, 업데이트, 로그 위치 및 기타 정보로 진행할 예정이다.

### 다운로드 및 초기 환경 구성
- `Security Onion`
- 시스템 구성
  - `OS`(Ubuntu 64bit) ![](https://velog.velcdn.com/images/kyk02405/post/3a8b4b39-5413-443b-a84f-9840f141b1c1/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/e0366eff-be0c-4ebe-8742-9de12be78085/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/62bd87b7-02ee-4d72-97ba-a45ab67efa31/image.png)
  - `8192MB` , `80GB`로 설정
  - ![](https://velog.velcdn.com/images/kyk02405/post/2ea1deae-64a4-44e1-aa3c-0123e8ac7fcd/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/eaf88627-2719-44ba-a8c5-59691eb00527/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/e29580ee-e602-492b-a07a-ed9fca205702/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/e4575c7c-126a-4755-b432-ad5dfaa9017c/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/7e3bfcbf-c8b7-4898-8c59-56c74fa39d10/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/d5ab4251-5a0a-4cf6-88ed-b5a0d32be546/image.png)
  - 화면이 짤릴경우 `Tab`키로 이동 후 다음 ![](https://velog.velcdn.com/images/kyk02405/post/f95e44bd-8098-44bb-93bd-b05871e09f5e/image.png)
  - 이후 다음 계속 누르고 `restart now` 클릭 
  - `check` 해제 ![](https://velog.velcdn.com/images/kyk02405/post/6ea48df0-b689-491d-a39c-d50c29ba1b7b/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/25b49d3b-8177-4db4-9b00-fdf20f79e4ea/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/1d8ce47b-5aa1-474f-9736-51d2ea9e533a/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/88958343-31a6-42a6-a0ff-551d6745243e/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/e3ca16e0-2c51-4365-a05d-14961f6817ba/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/39b1fc24-1af5-42c7-aaeb-5f8192e15bf5/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/323a7827-cb35-40d8-a56f-6691ce99fd77/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/f008c4a2-3850-476d-b940-fb1d4bc318c6/image.png)

  - ![](https://velog.velcdn.com/images/kyk02405/post/903f6073-e512-4894-b853-9aed61bfb85c/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/9b2444cf-b3b3-49d9-8f9b-5b47e371c78a/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/2b17e7f9-cef3-4f34-bcae-b633e42fb8d0/image.png)
```bash
cd /home/samadal/Desktop

sudo ./vmware-tools-distrib/vmware-install.pl 

처음 나오는 문구만 yes 이후 enter

완료 후 

sudo reboot</code></pre><h3 id="네트워크-설정">네트워크 설정</h3>
<ul>
<li>기본 작업<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2ff82336-795b-4fe5-bf77-fdb798efc066/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a8faee11-d101-4733-88ec-deab56491aee/image.png" /></li>
</ul>
</li>
</ul>
<ul>
<li>기본 설정<ul>
<li>네트워크 추가 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7fef0af4-7f0c-4634-b277-01e9ba418344/image.png" /></li>
<li><code>DHCP</code> 체크</li>
<li><code>Yes make</code></li>
<li><code>reboot</code></li>
</ul>
</li>
<li>You only have one interface (ens33), which will be configured as a management interface.<ul>
<li>우측 상단에 있는 <code>Network 아이콘</code>을 클릭한다.</li>
<li><code>Network 도구</code> 아이콘을 클릭한 후 나타나는 <code>All Settings</code> 화면에서 <code>Network</code>를 클릭한다.</li>
<li>좌측에 있는 <code>Wired</code> 항목을 클릭한 후 우측 하단에 있는 <code>설정 아이콘(톱니바퀴)</code>을 클릭한다.</li>
<li>좌측에 있는 <code>IPv4</code>를 클릭하고 우측에 있는 <code>Addresses</code> 항목에 <code>Automatic(DHCP)</code>로 되어 있는지 확인한다.</li>
<li>다 확인이 되었다면 모든 창을 <code>취소</code>하고 출력되어 있는 화면에서 <code>OK</code>를 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4a42db93-0a7c-4e26-84be-09209c0ee361/image.png" /></li>
</ul>
</li>
</ul>
<h3 id="보안도구">보안도구</h3>
<ul>
<li>기본 작업<ul>
<li>재부팅 후 <code>Setup</code></li>
<li><code>cloudsamadal</code>로 설정<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d56eec80-e8e2-4341-bee6-763527ea866d/image.png" /></li>
<li><code>P@ssw0rd2</code>로 설정 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/04d64883-93d4-4b55-99f7-fff7f1f1f3a5/image.png" /></li>
</ul>
</li>
<li>보안 도구 설치<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f5c3494a-6250-482c-a9a3-6b02d61e3095/image.png" /></li>
</ul>
</li>
</ul>
<h3 id="원격-접속">원격 접속</h3>
<ul>
<li><code>Sguil</code><ul>
<li>작업 <ul>
<li><code>Snort</code> 패턴을 작성한 다음 패턴 테스트 후 <code>Squil</code> 접속하여 확인하는 방법을 기재한다.</li>
<li>사용자 정의 <code>Snort</code> 패턴을 만들려면 <code>/etc/nsm/rules/local.rules</code> 에 사용자 정의 <code>Snort 패턴</code>을 입력한 후 룰 업데이트를 해야 한다.</li>
<li>그리고 패턴 테스트한 다음 <code>Squil</code> 프로그램에 접속하여 탐지가 되는지 확인하도록 한다.</li>
</ul>
</li>
<li><code>Rules</code> 수정<code>(local.rules)</code> 및 업데이트<pre><code class="language-bash">root@samadal-virtual-machine:/etc/nsm/rules# cp -p local.rules local.rules.samadal
</code></pre>
</li>
</ul>
</li>
</ul>
<p>root@samadal-virtual-machine:/etc/nsm/rules# vi local.rules</p>
<p>1 alert icmp any any -&gt; any any (msg:&quot;Have a nice day!&quot;; sid:1000001;)</p>
<pre><code>
- `Putty` 복제 후 복제된 창에 입력
```bash
root@samadal-virtual-machine:~# rule-update
...

Done
Please review /var/log/nsm/sid_changes.log for additional details
Fly Piggy Fly!
Restarting Barnyard2.
Restarting: samadal-virtual-machine-ens33
  * stopping: barnyard2-1 (spooler, unified2 format)                                           [  OK  ]
  * starting: barnyard2-1 (spooler, unified2 format)                                           [  OK  ]
Restarting IDS Engine.
Restarting: samadal-virtual-machine-ens33
  * stopping: snort-1 (alert data)                                                             [  OK  ]
  * starting: snort-1 (alert data)                                                             [  OK  ]
</code></pre><ul>
<li><code>Sguil</code> 실행 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a6e0b27d-ae43-4408-9c99-059c83591296/image.png" /><ul>
<li><code>cloudsamadal1</code> <code>P@ssw0rd2</code></li>
</ul>
</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a5d907af-0df3-46de-ab5f-e499e469773a/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a74357fa-ec1a-44f9-9937-5aace340b5bd/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f2e88417-06a3-4144-a712-045bcdc9e8fd/image.png" /></li>
</ul>