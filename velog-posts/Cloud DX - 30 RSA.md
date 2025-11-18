# Cloud DX - 30 RSA

- 📅 Published: Mon, 10 Nov 2025 05:41:14 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-29-RSA)

<hr />
<h1 id="rsa-공개키를-이용한-ssh-접속">RSA 공개키를 이용한 SSH 접속</h1>
<h2 id="사용해야-하는-이유">사용해야 하는 이유</h2>
<ul>
<li>기존의 사이트틀에서는 사용자의 ID와 PW를 요구하고 있는 실정이다.</li>
<li>이와 같은 방법은 비밀번호를 입력할 떄 노출에 따른 보안상 문제가 발생할 가능성이 많다.</li>
<li>이에 따라 인증방식을 보다 쉽고 안전하게 운영할 피룡가 발생된다.</li>
<li><code>RSA 공개키</code>는 이와 같이 ID와 PW 입력 없이 시스템에 접속할 수 있도록 해준다.</li>
<li><code>RSA 공개키 암호</code>를 사용해서 <code>Server</code>에 공개키(Public Key)를 저장해 두고 사용자(Client)는 개인(Private key)를 가지고 접속한다.</li>
</ul>
<hr />
<h2 id="실습-1-without-keygen">실습 1. without KeyGen</h2>
<ul>
<li>rocky 2개 (snapshot) 띄우고 </li>
<li>129 ,130(reboot) 으로 ip 변경 후 작업</li>
</ul>
<h3 id="server에서-작업">Server에서 작업</h3>
<ul>
<li>192.168.10.129, 접속을 허용 하는 놈</li>
<li>Client에서 생성한 공개키가 저장될 디렉터리(.ssh)</li>
<li>SSH 환경설정<pre><code class="language-bash"></code></pre>
</li>
</ul>
<p>login as: root
<a href="mailto:root@192.168.10.129">root@192.168.10.129</a>'s password:
Activate the web console with: systemctl enable --now cockpit.socket</p>
<p>Last login: Mon Nov 10 11:50:23 2025
[root@localhost ~]# mkdir -p /export/home/
[root@localhost ~]# usermod -m -d /export/home/samadal samadal
usermod: 바뀐 점이 없음
[root@localhost ~]# cat /etc/passwd | grep samadal
samadal:x:1000:1000:samadal:/export/home/samadal:/bin/bash
[root@localhost ~]# cd /export/home/samadal/
[root@localhost samadal]# mkdir .ssh
[root@localhost samadal]# ls -ld .ssh
drwxr-xr-x. 2 root root 4096 11월 10 11:53 .ssh
[root@localhost samadal]# chmod 700 .ssh
[root@localhost samadal]# chown samadal. .ssh
[root@localhost samadal]#
[root@localhost samadal]# mkdir /backup/
[root@localhost samadal]# cp -p /etc/ssh/sshd_config /backup
[root@localhost samadal]# vi /etc/ssh/sshd_config
[root@localhost samadal]# systemctl restart sshd</p>
<pre><code>

### Client에서 작업
- 192.168.10.130, 접속을 하는 놈
- 공개키와 개인키 생성
```bash
Last login: Mon Nov 10 11:50:09 2025
[root@localhost ~]# su - samadal
[samadal@localhost ~]$
[samadal@localhost ~]$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/samadal/.ssh/id_rsa):
Created directory '/home/samadal/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/samadal/.ssh/id_rsa
Your public key has been saved in /home/samadal/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:gXkc/Pp6CNvhrN9uaI/eQT2aXpxOerUdW+2Q7Ky3C2k samadal@localhost.localdomain
The key's randomart image is:
+---[RSA 3072]----+
|       ..        |
|       +..       |
|      o +.       |
|       . ...     |
|        S.. o. ..|
|      . o. + +=.o|
|       * =+ E+ =+|
|      . B=+B..=.o|
|      .==*B.oooo |
+----[SHA256]-----+
[samadal@localhost ~]$ exit
로그아웃
[root@localhost ~]# cd /home/samadal/.ssh
[root@localhost .ssh]# ls -l
합계 8
-rw-------. 1 samadal samadal 2622 11월 10 12:01 id_rsa
-rw-r--r--. 1 samadal samadal  583 11월 10 12:01 id_rsa.pub
[root@localhost .ssh]#</code></pre><ul>
<li>생성된 공개키를 <code>Server</code>에 전송<pre><code class="language-bash">[root@localhost .ssh]# scp id_rsa.pub samadal@192.168.10.129:/export/home/samadal/.ssh/authorized_keys
The authenticity of host '192.168.10.129 (192.168.10.129)' can't be established.
ED25519 key fingerprint is SHA256:RJA2UzbmHLtTNMXi0xS8Bu8UjjMOT+cjRfXjD/bYi+U.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.10.129' (ED25519) to the list of known hosts.
samadal@192.168.10.129's password:
id_rsa.pub                                                            100%  583     1.0MB/s   00:00
[root@localhost .ssh]#</code></pre>
```bash<h1 id="서버에서129-인증키가-들어-온-것을-확인">서버에서(129) 인증키가 들어 온 것을 확인</h1>
[root@localhost samadal]# pwd
/export/home/samadal
[root@localhost samadal]# cd .ssh
[root@localhost .ssh]# ls -l
합계 4</li>
<li>rw-r--r--. 1 samadal samadal 583 11월 10 12:07 authorized_keys
```</li>
<li>개인키를 이용해서 Server에 접속<pre><code class="language-bash">[root@localhost .ssh]# su - samadal
[samadal@localhost ~]$ ssh -i /home/samadal/.ssh/id_rsa samadal@192.168.10.129
The authenticity of host '192.168.10.129 (192.168.10.129)' can't be established.
ED25519 key fingerprint is SHA256:RJA2UzbmHLtTNMXi0xS8Bu8UjjMOT+cjRfXjD/bYi+U.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.10.129' (ED25519) to the list of known hosts.
Last login: Thu Oct  2 15:56:41 2025 from 192.168.10.1
[samadal@localhost ~]$ exit
로그아웃
Connection to 192.168.10.129 closed.
[samadal@localhost ~]$ ssh -i /home/samadal/.ssh/id_rsa samadal@192.168.10.129
Last login: Mon Nov 10 12:16:01 2025 from 192.168.10.130
[samadal@localhost ~]$ ifconfig ens160
ens160: flags=4163&lt;UP,BROADCAST,RUNNING,MULTICAST&gt;  mtu 1500
      inet 192.168.10.129  netmask 255.255.255.0  broadcast 192.168.10.255
      inet6 fe80::20c:29ff:fee2:1cde  prefixlen 64  scopeid 0x20&lt;link&gt;
      ether 00:0c:29:e2:1c:de  txqueuelen 1000  (Ethernet)
      RX packets 738731  bytes 1094430001 (1.0 GiB)
      RX errors 0  dropped 0  overruns 0  frame 0
      TX packets 157749  bytes 8691026 (8.2 MiB)
      TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0</code></pre>
</li>
</ul>
<hr />
<h2 id="실습-2-with-keygen">실습 2. with KeyGen</h2>
<h3 id="작업-1-client에서-파일-생성하고-server에-업로드-한-후-접속">작업 1. Client에서 파일 생성하고 Server에 업로드 한 후 접속</h3>
<ul>
<li><code>hostOS</code>에서 작업
<code>PuttyGen</code> -&gt;<code>Generate</code> -&gt; <code>키생성</code> -&gt; <code>save private 클릭</code> -&gt;<code>D:130</code> 으로 저장후 </li>
<li>공용키 전송
```bash<h1 id="129">129</h1>
[root@localhost .ssh]# rm -rf *
[root@localhost .ssh]# vi authorized_keys
[root@localhost .ssh]#
[root@localhost .ssh]# chown samadal. authorized_keys
[root@localhost .ssh]#
[root@localhost .ssh]# ls -l
합계 4</li>
<li>rw-r--r--. 1 samadal samadal 398 11월 10 12:50 authorized_keys
[root@localhost .ssh]#
```</li>
<li>파일 전송 방법 2가지<ul>
<li>#130에서 송신(업로드) - <code>Client</code>에서 실행</li>
<li>#129에서 수신(다운로드) - <code>Server</code>에서 실행</li>
</ul>
</li>
</ul>
<pre><code class="language-bash">#client
scp /home/samadal/./ssh/id_rsa.pub samadal@192.168.10.129:/export/home/samadal/.ssh/authorized_keys

#server
scp samadal@192.168.10.130:/home/samadal/.ssh/id_rsa.pub /export/home/samadal/.ssh/authorized_keys</code></pre>