# Cloud DX - 34 Mail Server

- 📅 Published: Thu, 13 Nov 2025 11:36:45 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-34)

<hr />
<h1 id="19-mail-server">19. Mail Server</h1>
<h2 id="메일-서버의-작동-형태">메일 서버의 작동 형태</h2>
<ul>
<li><code>MTA</code>로 메일을 보내고 받고 <code>MDA</code>로 받은 메일을 서버에 저장하며 <code>MUA</code>로 서버에 저장된 메일을 내 PC로 가지고 온다.</li>
<li><code>CentOS</code> <code>4 Snapshot</code></li>
</ul>
<hr />
<h2 id="메일-서버-관련-용어">메일 서버 관련 용어</h2>
<h3 id="mta-mail-transfer-agent---보내는-메일-서버"><code>MTA</code> (Mail Transfer Agent) - 보내는 메일 서버</h3>
<ul>
<li>인터넷상에 있는 하나의 컴퓨터로부터 다른 컴퓨터(메일 서버)로 전자 메일을 전송하는 서버 프로그램</li>
<li>메일을 보내고 받을 수 있는 <code>메일 서버 프로그램</code></li>
<li><code>리눅스</code>(sendmail, qmail, postfix)</li>
<li><code>윈도우</code>(MS Exchange Server)</li>
</ul>
<h3 id="mua-mail-user-agent---사용자가-확인"><code>MUA</code> (Mail User Agent) - 사용자가 확인</h3>
<ul>
<li>사용자가 메일을 송수신할 때 사용하는 클라이언트 프로그램</li>
<li>하나의 프로그램 또는 전자 메일을 송수신하는 전형적인 <code>MUA</code>의 행위를 에뮬레이트하는 스크립트</li>
<li><code>MTA</code>에서 수신된 메일을 서버에서 찾아온 후 볼 수 있는 프로그램</li>
<li><code>리눅스</code>(다람쥐)</li>
<li><code>윈도우</code>(MS Outlook, MS Outlook Express, Thunderbird)</li>
</ul>
<h3 id="mda-mail-delivery-agent---받는-메일-서버"><code>MDA</code> (Mail Delivery Agent) - 받는 메일 서버</h3>
<ul>
<li>메시지를 사용자의 우편함에 쓰기 위해 <code>MTA</code>가 사용하는 프로그램</li>
<li><code>MTA</code>에서 수신된 메일을 사용자의 '메일박스(mbox)'로 옮겨주는 프로그램 <code>(/var/spool/mail/계정명[mbox])</code></li>
<li><h3 id="mra-mail-retrieval-agent"><code>MRA</code> (Mail Retrieval Agent)</h3>
</li>
<li>원격지 서버에 있는 우편함으로부터 사용자의 <code>MUA</code>로 메시지를 가져오는 서비스</li>
</ul>
<hr />
<h2 id="메일-서버-관련-프로토콜">메일 서버 관련 프로토콜</h2>
<h3 id="smtp-simplesend-mail-transfer-protocol">SMTP (Simple(Send) Mail Transfer Protocol)</h3>
<ul>
<li><code>보내는</code> 메일 서버</li>
<li>메일 전송 프로토콜로 메일 서버가 메일을 <code>전송</code>할 때 사용하는 프로토콜</li>
<li><code>25</code>번 포트 사용<h3 id="pop3-post-office-protocol">POP3 (Post Office Protocol)</h3>
</li>
<li><code>받는</code> 메일 서버</li>
<li>메일 수신 프로토콜로 메일 서버에서 사용자가 메일을 <code>받아</code> 볼때 사용하는 프로토콜</li>
<li><code>110</code>번 포트 사용<h3 id="imap-internet-mail-access-protocol">IMAP (Internet Mail Access Protocol)</h3>
</li>
<li>메일 수신 프로토콜로 메일 서버에서 사용자가 메일을 받아 볼때 사용하는 프로토콜</li>
<li>메일 서버와의 동기화로 인해 다른 컴퓨터에서도 볼수 있다는 <code>장점</code></li>
<li>메일을 메일 서버와 동기화 하기 때문에 메일 서버에는 부하가 많아지는 <code>단점</code></li>
<li><code>143</code>번 포트 사용</li>
</ul>
<h3 id="환경-설정">환경 설정</h3>
<ul>
<li>Step 1.<code>사용자 계정</code>과 <code>메일 계정</code>의 차이점<ul>
<li><code>사용자 계정</code><pre><code class="language-bash">[root@ns ~]# useradd user1
</code></pre>
</li>
</ul>
</li>
</ul>
<p>[root@ns ~]# cat /etc/passwd | grep user1
user1:x:1001:1001::/home/user1:/bin/bash</p>
<p>[root@ns ~]# ls -ld /home/user1
drwx------ 3 user1 user1 4096 11월 13 11:38 /home/user1</p>
<p>[root@ns ~]# ls -l /var/spool/mail/
합계 0
-rw-rw----. 1 rpc     mail 0  6월 14  2024 rpc
-rw-rw----. 1 samadal mail 0  6월 14  2024 samadal
-rw-rw----  1 user1   mail 0 11월 13 11:38 user1</p>
<pre><code>- ![](https://velog.velcdn.com/images/kyk02405/post/7f5bed20-b6fd-411a-acd4-cff79eddd612/image.png)
- `CREATE_MAIL_SPOOL=yes`로 되어 있어 `user1`이 생성 됨

- `메일 계정`
  - `-M`은 메일 서버 전용 계정
```bash
[root@ns ~]# useradd -M user2 
[root@ns ~]#
[root@ns ~]# cat /etc/passwd | grep user2
user2:x:1002:1002::/home/user2:/bin/bash</code></pre><hr />
<ul>
<li><p>Step 2. 패키지 설치, 방화벽 설정, 데몬 실행</p>
<ul>
<li><p>패키지 설치 </p>
<ul>
<li><code>DNS</code> <code>(bind)</code></li>
<li><code>Apache</code> <code>(httpd)</code></li>
<li><code>SMTP</code> <code>(sendmail, saslauthd)</code><ul>
<li><code>yum -y install sendmail*</code></li>
<li><code>saslauthd</code>는 <code>SMTP</code> 동작 시 하나의 <code>서비스</code>로 동작하기 때문에 패키지가 없다. </li>
</ul>
</li>
<li><code>POP3</code> <code>(dovecot)</code><ul>
<li><code>yum -y install dovecot*</code></li>
</ul>
</li>
</ul>
</li>
<li><p>방화벽 설정</p>
</li>
<li><pre><code class="language-bash">&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;zone&gt;
&lt;short&gt;Public&lt;/short&gt;
&lt;description&gt;For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.&lt;/description&gt;
&lt;service name=&quot;ftp&quot;/&gt;
&lt;service name=&quot;ssh&quot;/&gt;
&lt;service name=&quot;smtpi&quot;/&gt;
&lt;service name=&quot;dns&quot;/&gt;
&lt;service name=&quot;http&quot;/&gt;
&lt;service name=&quot;pop3&quot;/&gt;
&lt;service name=&quot;mysql&quot;/&gt;
&lt;service name=&quot;dhcpv6-client&quot;/&gt;
&lt;port protocol=&quot;tcp&quot; port=&quot;20&quot;/&gt;
&lt;port protocol=&quot;tcp&quot; port=&quot;21&quot;/&gt;
&lt;port protocol=&quot;tcp&quot; port=&quot;22&quot;/&gt;
&lt;port protocol=&quot;tcp&quot; port=&quot;25&quot;/&gt;
&lt;port protocol=&quot;tcp&quot; port=&quot;53&quot;/&gt;
&lt;port protocol=&quot;udp&quot; port=&quot;53&quot;/&gt;
&lt;port protocol=&quot;tcp&quot; port=&quot;80&quot;/&gt;
&lt;port protocol=&quot;tcp&quot; port=&quot;110&quot;/&gt;
&lt;port protocol=&quot;tcp&quot; port=&quot;3306&quot;/&gt;
&lt;/zone&gt;</code></pre>
</li>
<li><p><code>Putty</code>에서 <code>setup</code>에서 <code>enable</code>시키기</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/45755ed7-a1c2-41df-b842-5e5d61e1573a/image.png" /></li>
</ul>
</li>
<li><pre><code class="language-bash">[root@ns ~]# systemctl restart dovecot.service
[root@ns ~]#
[root@ns ~]# systemctl restart saslauthd</code></pre>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 3. DNS Server 구성<pre><code class="language-bash">[root@ns named]# vi g.zone
    1 $TTL 1D
    2 @       IN SOA  ns.gusiya.com.  root.gusiya.com. (
    3                                         0       ; serial
    4                                         1D      ; refresh
    5                                         1H      ; retry
    6                                         1W      ; expire
    7                                         3H )    ; minimum
    8         IN      NS      ns.gusiya.com.
    9         IN      A       192.168.10.128
   10         IN      MX 10   mail.gusiya.com.
   11         IN      MX 20   mail.gusiya.com.
   12
   13 ns      IN      A       192.168.10.128
   14 www     IN      A       192.168.10.128
   15 mail    IN      A       192.168.10.128</code></pre>
<pre><code class="language-bash">[root@ns named]# vi g.rev
    1 $TTL 1D
    2 @       IN SOA  ns.gusiya.com.  root.gusiya.com. (
    3                                         0       ; serial
    4                                         1D      ; refresh
    5                                         1H      ; retry
    6                                         1W      ; expire
    7                                         3H )    ; minimum
    8         IN      NS      ns.gusiya.com.
    9         IN      A       192.168.10.128
   10         IN      MX 10   mail.gusiya.com.
   11         IN      MX 20   mail.gusiya.com.
   12
   13 128     IN      PTR     ns.gusiya.com.
   14 128     IN      PTR     www.gusiya.com.
   15 128     IN      PTR     mail.gusiya.com.</code></pre>
<pre><code class="language-bash">[root@ns named]# nslookup
&gt; ns.gusiya.com
Server:         192.168.10.128
Address:        192.168.10.128#53
</code></pre>
</li>
</ul>
<p>Name:   ns.gusiya.com
Address: 192.168.10.128</p>
<blockquote>
<p><a href="http://www.gusiya.com">www.gusiya.com</a>
Server:         192.168.10.128
Address:        192.168.10.128#53</p>
</blockquote>
<p>Name:   <a href="http://www.gusiya.com">www.gusiya.com</a>
Address: 192.168.10.128</p>
<blockquote>
<p>mail.gusiya.com
Server:         192.168.10.128
Address:        192.168.10.128#53</p>
</blockquote>
<p>Name:   mail.gusiya.com
Address: 192.168.10.128</p>
<pre><code>---
- Step 4. `SMTP` 인증을 위한 설정 (/etc/mail/sendmail.mc)
  - 설정 파일 복사
  - ```bash
[root@ns named]# cd /etc/mail/
 [root@ns mail]# cp -p sendmail.mc sendmail.mc.samadal1
 [root@ns mail]# cp -p sendmail.cf sendmail.cf.samadal2
 [root@ns mail]# rm -rf sendmail.cf</code></pre><ul>
<li>환경 설정 (/etc/mail/sendmail.mc)<ul>
<li><pre><code class="language-bash">[root@ns mail]# vi sendmail.mc
52 dnl TRUST_AUTH_MECH(`EXTERNAL DIGEST-MD5 CRAM-MD5 LOGIN PLAIN')dnl
53 dnl define(`confAUTH_MECHANISMS', `EXTERNAL GSSAPI DIGEST-MD5 CRAM-MD5 LOGIN PLAIN')dnl
116 DAEMON_OPTIONS(`Port=smtp,Addr=0.0.0.0, Name=MTA')dnl</code></pre>
</li>
<li><code>52,53번</code> 줄 삭제 , <code>116번</code> 0.0.0.0 으로 변경</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li><p>Step 5. 기본 환경 설정 (/etc/mail/sendmail.cf)</p>
<ul>
<li><p><code>SMTP Daemon</code></p>
<ul>
<li><pre><code class="language-bash">[root@ns mail]# vi sendmail.cf
269 Addr=0.0.0.0, # 부분 삭제 </code></pre>
</li>
<li><pre><code class="language-bash">[root@ns mail]# vi sendmail.cf
89 # Cwlocalhost
90 Cwmail.gusiya.com

96 #Dj$w.Foo.COM
97 Dj$mail.gusiya.com</code></pre>
</li>
<li><pre><code class="language-bash">[root@ns mail]# m4 /etc/mail/sendmail.mc &gt; /etc/mail/sendmail.cf</code></pre>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li>메일 서버 정의</li>
</ul>
<hr />
<ul>
<li>Step 6. 릴레이 접근 제어(/etc/mail/access)<ul>
<li>릴레이를 통해 허용할 도메인과 <code>IP</code>주소 등록<ul>
<li><pre><code class="language-bash">13 Connect:mail.gusiya.com                 RELAY
 14 Connect:gusiya.com                      RELAY
 15 Connect:192.168.10.128                  RELAY</code></pre>
</li>
</ul>
</li>
<li>적용<ul>
<li><pre><code class="language-bash">[root@ns mail]# makemap hash /etc/mail/access &lt; /etc/mail/access</code></pre>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 7. 메일을 수신할 호스트 등록(/etc/mail/local-host-names)<pre><code class="language-bash">[root@ns mail]# vi local-host-names
1 # local-host-names - include all aliases for your machine here.
2 mail.gusiya.com</code></pre>
</li>
</ul>
<hr />
<ul>
<li>Step 8. 수산 메일 자동 전송(/etc/mail/virtusertable)<ul>
<li>받는 메일 서버에 적혀 있는 주소로 메일이 오면 지정된 곳의 메일로 자동 전송 </li>
<li>등록<ul>
<li><pre><code class="language-bash">1 # samadal@mail.gusiya.com root@mail.gusiya.com </code></pre>
</li>
<li><pre><code class="language-bash">[root@ns mail]# makemap hash /etc/mail/virtualusertable &lt; /etc/mail/virtusertable</code></pre>
</li>
</ul>
</li>
<li>정보 적용<ul>
<li><pre><code class="language-bash">[root@ns mail]# systemctl restart sendmail.service</code></pre>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="테스트-1-로컬-시스템에서의-테스트">테스트 1. 로컬 시스템에서의 테스트</h3>
<ul>
<li><p>실습 1. 로컽 테스트</p>
<ul>
<li><p>데몬 및 서비스 실행 </p>
<pre><code class="language-bash">[root@ns mail]# systemctl enable sendmail
[root@ns mail]#
[root@ns mail]# systemctl restart sendmail.service</code></pre>
</li>
<li><p><code>telnet</code> 테스트</p>
<ul>
<li><p><code>Telnet</code> 패키지 설치하고 활성화 작업</p>
</li>
<li><p>이전에 <code>DNS</code>작업때 바꿧던<code>vi /etc/resolv.conf</code> 파일에서 192.168.10.2로 변경 후 설치</p>
</li>
<li><pre><code class="language-bash">[root@ns mail]# sudo yum install -y telnet*
 [root@ns mail]# systemctl enable telnet.socket</code></pre>
</li>
<li><p>로컽(Localhost) 테스트와 도메인을 이용한 테스트</p>
<ul>
<li>테스트 1. 로컬(Localhost)테스트<ul>
<li><pre><code class="language-bash">[root@ns mail]# telnet localhost 25
Trying ::1...
telnet: connect to address ::1: Connection refused
Trying 127.0.0.1...</code></pre>
</li>
</ul>
</li>
<li>테스트 2. 도메인을 이용한 테스트<ul>
<li><pre><code class="language-bash">[root@ns mail]# vi /etc/resolv.conf # 128로 변경
[root@ns mail]# telnet mail.gusiya.com 25</code></pre>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p>실습 2. 보내기 테스트</p>
<ul>
<li>Step 1. 로컬(Localhost)테스트에서 보내기 테스트<ul>
<li><code>mail from:&lt;계정명@도메인&gt;</code>     <code>-&gt; 보내는 사람 주소</code></li>
<li><code>rcpt to:&lt;계정명@도메인&gt;</code>        <code>-&gt; 받는 사람 주소</code></li>
<li><code>data</code> <code>-&gt; 내용 입력 시작</code></li>
<li><code>Test... sendmail!</code> <code>-&gt; 메일 내용 입력</code></li>
<li><code>.</code>    <code>-&gt; 내용 입력 끝</code></li>
<li><code>quit</code>                        <code>-&gt; 종료</code></li>
<li>입력</li>
<li>확인</li>
<li>메일이 잘 왔는지 확인<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/90a73991-a9c6-47fb-b0ba-94f7799e3164/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code>- 결론
  - `localdomain`으로 테스트 하면 받을 수 가 없다</code></pre><ul>
<li>Step 2. 도메인을 이용한 테스트에서 보내기 테스트<ul>
<li>```bash</li>
<li>실습 3. 받기 테스트 
```bash
[root@ns mail]# telnet mail.gusiya.com 110
Trying 192.168.10.128...
Connected to mail.gusiya.com.
Escape character is '^]'.</li>
<li>OK Dovecot ready.<pre><code></code></pre></li>
</ul>
</li>
</ul>
<hr />
<h3 id="다람쥐-메일">다람쥐 메일</h3>
<ul>
<li><p>설정</p>
<ul>
<li>패키지 설치<ul>
<li>외부망의 통신 가능하게 수정<ul>
<li>vi /etc/resolv.conf -&gt; .2로 수정</li>
</ul>
</li>
<li>저장소 추가<ul>
<li><pre><code class="language-bash">[root@ns config]# yum -y install epel-release</code></pre>
</li>
</ul>
</li>
<li>패키지 설치<ul>
<li><pre><code class="language-bash">[root@ns config]# yum -y install squirrelmail</code></pre>
</li>
</ul>
</li>
</ul>
</li>
<li>접속을 위한 도메인 등록 <ul>
<li><code>/usr/share/squirrelmail/config/config.pl</code><ul>
<li>2 입력 후 엔터</li>
<li>1 입력 후 엔터</li>
<li>mail.gusiya.com 입력 후 엔터</li>
<li>A 입력 후 엔터</li>
<li>4 입력 후 엔터</li>
<li>mail.gusiya.com 입력 후 엔터</li>
<li>S 입력 후 엔터</li>
<li>R 입력 후 엔터</li>
<li>2 입력 후 엔터</li>
<li>Q 입력 후 엔터</li>
<li>Y 입력 후 엔터</li>
</ul>
</li>
</ul>
</li>
<li>포트 추가<ul>
<li>114번 포트 추가<ul>
<li><code>&lt;port protocol=&quot;tcp&quot; port=&quot;114&quot;/&gt;</code></li>
</ul>
</li>
</ul>
</li>
<li><code>Apache Web Server</code> 환경설정<ul>
<li><code>[root@ns config]# mkdir /backup/; cp -p /etc/httpd/conf/httpd.conf /backup</code></li>
<li><code>[root@ns config]# vi /etc/httpd/conf/httpd.conf</code> 에서 아래와 같이 수정 및 추가</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e22aba1c-1a94-4b10-ae94-3d02bc232f35/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2d6a7ed7-d149-48e2-8294-c5cac25200b5/image.png" /></li>
</ul>
</li>
<li>기타 설정<ul>
<li>받는 메일 서버 환경 설정<ul>
<li><code>[root@ns conf.d]# vi 10-mail.conf</code> 에서 주석해제</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2490fb78-2f66-45e8-918a-4deff2d26e8b/image.png" /></li>
<li><pre><code class="language-bash">[root@ns conf.d]# systemctl restart dovecot
 [root@ns conf.d]# systemctl restart sendmail.service</code></pre>
</li>
</ul>
</li>
<li>외부망의 통신 불가능하게 설정<ul>
<li><code>[root@ns conf.d]# vi /etc/resolv.conf</code> -&gt;.128로 변경</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1b14aa87-bf2a-4d98-83a5-05744e3bac57/image.png" /></li>
<li><code>systemctl restart httpd</code></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p>다람쥐 메일 실행하고 테스트</p>
<ul>
<li><p>사이트에서 다람쥐 메일에 접속</p>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3cb55512-8a09-4fea-b7d3-51fbf604f02a/image.png" /></p>
</li>
<li><p><code>ID:samadal</code>, <code>PW:1</code>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/29bc98be-ddf8-45b1-823e-24e63de17d3c/image.png" /></p>
</li>
<li><pre><code class="language-bash">[root@ns config]# cd /var/spool/mail/
[root@ns mail]# chmod 755 samadal</code></pre>
</li>
<li><p><code>F5</code>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b2c48eb5-ab1e-489c-ae5c-b46ce565d642/image.png" /></p>
</li>
<li><p><code>Compose</code> -&gt; <code>samadal@mail.gusiya.com</code> 으로 메일 전송
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c708b705-1681-4f1f-95ed-eee9fc7e5000/image.png" /></p>
</li>
<li><p>메일 확인
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7e7974b6-476a-4897-aabd-da317a41d3fa/image.png" /></p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="테스트-2-원격-시스템에서의-접속">테스트 2. 원격 시스템에서의 접속</h3>
<ul>
<li>작업을 위한 시스템 망 구성 </li>
<li></li>
</ul>