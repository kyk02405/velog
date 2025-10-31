# Cloud DX - 22 ACL

- 📅 Published: Wed, 29 Oct 2025 09:18:42 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-22-ACL)

<hr />
<h1 id="span-style--colorskyblueaclspan"><span style="color: skyblue;">ACL</span></h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/601039ac-11bd-4f73-af80-8b368d20c2c0/image.png" /></p>
<h2 id="개요">개요</h2>
<ul>
<li>기본적으로 <code>ACL</code>은 방화벽과 같은 개념이다.</li>
<li>사용 용도에 따라 <code>Router</code>를 경유하는<code>Packet</code>을 <span style="color: red;"><strong><code>필터링</code></strong></span>(일반적인 용도로 사용), 트래픽 식별, 암호화, 분류, 변환 작업을 수행한다.</li>
<li><code>I/F</code>를 통해서 들어오고 나가는 데이터를 검사하고 필터링 정책에 따라 데이터를 <code>포워딩(Forwarding)</code> 및 <code>금지(Drop)</code> 시킨다.</li>
</ul>
<h3 id="단계별-설정">단계별 설정</h3>
<ul>
<li>1단계, 2단계, 3단계가 끝난 후 정상적으로 통신이 된다고 가정했을 때 4단게인 <code>ACL</code>를 적용</li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c5c7bbd4-6742-4ce0-a412-1d337233f2ab/image.png" /></p>
<h2 id="span-style--colorredstandard-access-listspan"><span style="color: red;">Standard Access List</span></h2>
<ul>
<li><code>Source Address</code>를 검사한다 </li>
<li>검사결과에 따라 전체 <code>Protocol Suite</code>에 대한 <code>Packet</code> 출력을 허용하거나 거부한다</li>
<li>실습에선 <code>Standard ACL</code> 만 사용</li>
</ul>
<h2 id="extended-access-list">Extended Access List</h2>
<ul>
<li><code>Source Address</code>와 <code>Destination Address</code>를 모두 검사한다 </li>
<li>특정 <code>Protocol</code>, <code>Port번호</code>, 다른 <code>매개변수</code>를 검사하여 유연하게 제어가 가능하다 </li>
</ul>
<hr />
<h2 id="명령어">명령어</h2>
<h3 id="step-1--access-list-명령어로-ip-traffic-filter-list에-entry를-만든다">Step 1 : access-list 명령어로 IP Traffic Filter list에 Entry를 만든다</h3>
<pre><code class="language-swift">Router(config)#access-list access-list-number  {permit | deny} {test_conditions} </code></pre>
<h3 id="step-2--ip-access-group-명령으로-기존-access-list를-interface에-적용한다">Step 2 : IP access-group 명령으로 기존 Access-List를 Interface에 적용한다</h3>
<pre><code class="language-swift">Router(config-if)#{protocol} access-group access-list-number  {in | out}  </code></pre>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1fef48bc-776f-4a17-b7c9-1005abf83a5b/image.png" /></p>
<ul>
<li><code>172.16.0.0 0.0.255.255</code> 나가는 트래픽 허용</li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/81aa737c-9b62-4ad0-926f-4b9e71d38d18/image.png" /></p>
<ul>
<li><code>172.16.4.13 0.0.0.0</code> 로 나가는 트래픽 전부 차단</li>
<li><code>0.0.0.0 255.255.255.255</code> 그 외 는 전부 허용</li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/aa7d1684-956d-485b-b79f-581236302d32/image.png" /></p>
<ul>
<li><code>172.16.4.0 0.0.0.255</code> 차단</li>
<li><code>permit any</code> 전부 허용 </li>
</ul>
<hr />
<h2 id="01pkt">01.pkt</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/73c1cea1-17bb-4da9-8b7a-26f969ac6b49/image.png" /></p>
<ul>
<li><code>Static Routing</code>에서의 <code>02.pkt</code>를 복사한 후 <code>01.pkt</code>로 이름을 변경한 후 작업</li>
<li>조건<ul>
<li><code>ACL</code> 설정 전 (모든 <code>PC</code>들 끼리 통신이 된다.)</li>
<li><code>ACL</code> 설정 후 (<code>PC1</code>에서 <code>PC4</code>는 통신이 되고 <code>PC3</code>은 통신이 안된다)</li>
</ul>
</li>
</ul>
<h3 id="설정">설정</h3>
<ul>
<li><p><code>1</code>, <code>2</code>, <code>3</code>단계는 완료되어 있는 상태이다.</p>
</li>
<li><p><code>4</code>단계, <code>ACL</code> 설정</p>
<ul>
<li>기존에 설정되어 있는 <code>ACL</code>확인<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7949f853-427b-4c36-991e-cf0dc5cea8e9/image.png" /></li>
</ul>
</li>
</ul>
<blockquote>
<ul>
<li>방법 1. 특정 네트워크에 있는 특정 IP가 설정되니 시스템에 <code>ACL</code>을 적용</li>
</ul>
</blockquote>
<ul>
<li>Step 1.  <code>IP Traffic Filter list</code>에 <code>Entry</code>를 만든다.<pre><code class="language-bash">R1(config)# access-list 1 deny 10.100.1.1 0.0.0.0
R1(config)# access-list 1 permit any</code></pre>
</li>
<li>Step 2. <code>Ip access-group</code> 명령으로 <code>Access-List</code>를 <code>Interface</code>에 적용한다<pre><code class="language-bash">R1(config)#int f0/0
R1(config-if)# ip access-group 1 out</code></pre>
</li>
<li>Step 3. <code>ACL</code> 적용<pre><code class="language-bash">R1(config-if)# ^ + z
R1#
R1# wr</code></pre>
</li>
<li>Step 4. 확인<pre><code class="language-bash">R1# sh r
R1# sh access-lists</code></pre>
</li>
<li>Step 5. 테스트<ul>
<li><code>PC1</code>-&gt;<code>PC3</code> 핑 테스트</li>
</ul>
</li>
<li>Step 6. <code>R1</code>에 적용되어 있는 <code>ACL</code> 설정 제거<pre><code class="language-bash">R1# sh run
R1# sh access-lists
R1# conf t
R1(config)# int f0//0
R1(config-if)# no ip access-group 1 out
R1(config-if)# exit
R1(config)# no access-list 1
R1(config)# ^ + z
R1# wr
R1# sh r
R1# sh access-lists</code></pre>
</li>
</ul>
</li>
</ul>
<hr />
<blockquote>
<ul>
<li>방법 2. 특정 네트워크에 있는 특정 IP가 설정되니 시스템에 <code>ACL</code>을 적용<ul>
<li>Step 1.  <code>IP Traffic Filter list</code>에 <code>Entry</code>를 만든다.<pre><code class="language-bash">R2(config)# access-list 1 deny 10.100.1.1 0.0.0.0
R2(config)# access-list 1 permit any</code></pre>
</li>
<li>Step 2. <code>Ip access-group</code> 명령으로 <code>Access-List</code>를 <code>Interface</code>에 적용한다<pre><code class="language-bash">R2(config)#int f0/0
R2(config-if)# ip access-group 1 in</code></pre>
</li>
<li>Step 3. <code>ACL</code> 적용<pre><code class="language-bash">R2(config-if)# ^ + z
R2#
R2# wr</code></pre>
</li>
<li>Step 4. 확인<pre><code class="language-bash">R2# sh r
R2# sh access-lists</code></pre>
</li>
<li>Step 5. 테스트<ul>
<li><code>PC1</code>-&gt;<code>PC3</code> 핑 테스트</li>
</ul>
</li>
<li>Step 6. <code>R2</code>에 적용되어 있는 <code>ACL</code> 설정 제거<pre><code class="language-bash">R2# sh run
R2# sh access-lists
R2# conf t
R2(config)# int f0//0
R2(config-if)# no ip access-group 1 out
R2(config-if)# exit
R2(config)# no access-list 1
R2(config)# ^ + z
R2# wr
R2# sh r
R2# sh access-lists</code></pre>
</li>
</ul>
</li>
</ul>
</blockquote>
<pre><code>
---
## 02.pkt
![](https://velog.velcdn.com/images/kyk02405/post/1bdaed3d-054c-4218-ba58-f6d454eb0dc0/image.png)


---
# &lt;span style = &quot;color:skyblue&quot;&gt;GNS3&lt;/span&gt;

## 개요
- 시뮬레이션 프로그램
- `네트워크`, `장비`, `서버 시스템` 등을 `작업창(Workspace)`에 모두 불러와서 실제 동작할 수 있도록 해준다.

## 필수 프로그램 다운로드 및 설치

- `XShell`
- `GNS3`
 ![](https://velog.velcdn.com/images/kyk02405/post/a12a3866-0c7e-4878-80ec-77ef2fd2e72e/image.png)
![](https://velog.velcdn.com/images/kyk02405/post/1f68e94c-6868-4a21-bbcb-7eecff99573d/image.png)
---
## GNS3에 IOS 등록하기
### 콘솔 접속을 위한 XShell 등록
- `Edit` - `Console applications` - `Console settings` - `Edit` - `Xshell5` - 
  - `XShell 5`등록 (C:\Program Files (x86)\NetSarang\Xshell 5)
  - `XShell 8`로 변경 (C:\Program Files (x86)\NetSarang\Xshell 8)
    - ![](https://velog.velcdn.com/images/kyk02405/post/f0b140a3-3b34-4ac6-bf5a-1313c1f50fd5/image.png)
---
### GNS3에 IOS 등록하기
- 작업 폴더 생성

- GNS3에 IOS등록하기
---
### 간단한 토폴로지를 구성하고 GNS3 기본 기능 알아보기
- 장비 추가
  - ![](https://velog.velcdn.com/images/kyk02405/post/e4d0922a-5c88-48f9-8d56-ea60ae75fe41/image.png)


- 장비별 설정
  - ![](https://velog.velcdn.com/images/kyk02405/post/a1f3f1bc-f9a7-47b0-bed1-e09d2b22fc14/image.png)


- 토폴로지 구성
  - ![](https://velog.velcdn.com/images/kyk02405/post/c3feed05-3291-480d-af26-f021e2e1818a/image.png)


---
### 시스템 관련 실습
- 기본 토폴로지 구성 
  - OS (Linux. Windows Server, Windows 10)
  - Router 1개
  - Switch 1개
  - VPCS 1개

- ![](https://velog.velcdn.com/images/kyk02405/post/3f5b956f-452d-4601-8fc2-86c3bbd555be/image.png)
- ![업로드중..](blob:https://velog.io/c97cc4c5-6767-4f15-a0e7-fa6bd592bf64)

&gt;### Rocky Linux 9.6 로딩한 후 XShell을 이용한 원격 접속
- 로딩된 `Rocky Linux 9.6` 아이콘 위에서 우클릭 후 `Start`를 클릭한다.
- `VMWare`가 자동으로 로딩되면 `탭`에서 우클릭 후 `Network Adapter`를 `Host-only`로 지정한다.
- `root`로 로그인 한 후 `IP`를 지정한다
- 이 떄 `VPCS`가 `192.168.10.1 /24`로 지정했기 때문에 `192.168.10.2`로 지정한다.
- 그리고 `Gateway`는 `192.168.10.254`로 지정한다.
- (매우 중요) `GNS3`에서는 원격접속이 모두 `Telnet`이기 때문에 `Telnet`관련 작업들을 모두 설정을 해야한다.
- 현재 `Network Adapter`가 `Host-only`로 지정되어 있기 때문에 외부와의 접속이 안된다. 
- 따라서 `Rocky Linux 9.6` ISO 파일을 로딩한 후 패키지를 설치하면 된다.
- `VMWare`의 `Rocky Linux 9.6` 탭에서 우클릭 후 `ISO`파일을 삽입한다.
- 터미널을 열고 마운트 정보를 확인한 후 `Telnet` 패키지가 있는 경로로 이동한다.
```bash
            (rocky96)# pwd
         /run/media/root/Rocky-9-6-x86_64-dvd/AppStream/Packages/t
            (rocky96)# ls -l telnet-*
         -rw-r--r-- 1 root root 64632  5월 16  2022 telnet-0.17-85.el9.x86_64.rpm
         -rw-r--r-- 1 root root 38537  5월 16  2022 telnet-server-0.17-85.el9.x86_64.rpm</code></pre><pre><code class="language-bash">[root@localhost t]# rpm -ivh telnet-*
Verifying...                          ################################# [100%]
준비 중...                         ################################# [100%]
Updating / installing...
   1:telnet-server-1:0.17-85.el9      ################################# [ 50%]
   2:telnet-1:0.17-85.el9             ################################# [100%]
[root@localhost t]# rpm -qa | grep telnet
telnet-server-0.17-85.el9.x86_64
telnet-0.17-85.el9.x86_64
[root@localhost t]# </code></pre>
<ul>
<li>방화벽을 이용해서 <code>포트</code>와 <code>서비스</code>를 등록한다.<pre><code class="language-bash">vi /etc/firewalld/zones/public.xml
[root@localhost t]# 
[root@localhost t]# firewall-cmd --reload
success
[root@localhost t]# firewall-cmd --list-ports
22/tcp 23/tcp
[root@localhost t]# firewall-cmd --list-services
cockpit dhcpv6-client ssh telnet</code></pre>
</li>
<li><code>Telnet</code> 데몬을 실행한다.<pre><code class="language-bash">[root@localhost t]# systemctl enable telnet.socket 
Created symlink /etc/systemd/system/sockets.target.wants/telnet.socket → /usr/lib/systemd/system/telnet.socket.
[root@localhost t]# systemctl restart telnet.socket </code></pre>
</li>
<li>5004 포트추가</li>
</ul>