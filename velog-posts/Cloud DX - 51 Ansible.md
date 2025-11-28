# Cloud DX - 51 Ansible

- 📅 Published: Thu, 27 Nov 2025 09:15:15 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-51-Ansible)

<hr />
<h1 id="02-ansible">02. Ansible</h1>
<h2 id="21-개요">2.1 개요</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4986673e-b043-42a6-9dfe-3d79b90f9ab9/image.png" /></p>
<ul>
<li><code>CentOS</code> <code>1_Updated</code> <code>2대</code></li>
<li><code>Ansible</code>은 <code>Infrastructure as Code (IaC, 인프라 관리를 코드 기반)</code>으로 자동화 해주는 <code>오픈소스 기반의 자동화 관리 도구</code>를 말한다.</li>
<li>즉, <code>IT 인프라</code>를 <code>코드 기반으로 자동 설치 및 구축/관리/프로비저닝</code> 하는 <code>프로세스</code>를 말한다.</li>
<li><code>IaC</code> 개념 도입 전 모든 작업들이 수동으로 작업되었던 것들이 개념 도입 후 <code>인프라 구축(Cloud 환경에서의)</code>이 <code>자동화</code> 할 수 있게 된 것이다.</li>
</ul>
<hr />
<h3 id="ansible-동작-원리">Ansible 동작 원리</h3>
<ul>
<li>가운데에 있는 <code>Ansible</code> 로고가 <code>Ansible</code>이 설치된 <code>Controller Server</code>에 해당된다.</li>
<li>이 <code>Controller Server</code>는 본인이 관리할 원격 서버들 목록을 인벤토리(<code>Inventory</code>, <code>서버</code>, <code>장비</code>, <code>인증 관련 라이센스 등</code>) 파일에 저장하고 있다.</li>
</ul>
<hr />
<h3 id="ansible-특징">Ansible 특징</h3>
<ul>
<li><p><code>Agentless</code></p>
<ul>
<li><p><code>Ansible 이전의 IaC</code></p>
<ul>
<li><code>Chef/Puppet</code>과 같은 <code>기존 IaC 솔루션들</code>은 <code>원격 서버에 에이전트를 설치</code>할 필요가 있었다.</li>
<li>따라서 명령을 내려주는 <code>Controller 서버</code>와 <code>원격 서버에 설치된 Agent</code>들이 명령을 주고 받는 방식으로 동작되었다.</li>
</ul>
</li>
<li><p><code>Ansible 이후의 IaC</code></p>
<ul>
<li>(핵심) 그러나 <code>Ansible</code>은 <code>SSH를 기반</code>으로 <code>원격 서버에 명령을 전달</code>하기 때문에 에이전트가 필요 없다.</li>
<li><code>Agent</code>가 필요 없다는 것은 각 원격 서버에 접속해서 agent를 설치해 줄 필요가 없다는 말이다.</li>
<li>즉, <code>Agent</code> 설치 단계를 제거하여 인프라 구축을 더 자동화에 가깝게 만든 것이다.</li>
</ul>
</li>
</ul>
</li>
<li><p><code>접근 용이성</code></p>
<ul>
<li><code>Ansible</code>은 <code>Controller 서버</code>가 원격 서버들에게 무언가 명령을 전달하도록 동작한다.</li>
<li>물론 <code>Controller 서버</code>에서 명령어를 한 줄 한 줄 입력해도 되지만, 이러한 행위는 자동화의 의미와는 거리가 멀다.</li>
<li>(핵심) 진정한 의미의 자동화를 위해서는 명령어들을 모아서 한번에 처리할 수 있어야 한다. 마치 <code>쉘 스크립트</code>와 같이 말이다.</li>
<li>(중요) <code>Ansible</code>은 이러한 <code>명령 모음집(뒤에서 소개할 Playbook)</code>을 <code>YAML</code>형식의 파일로 관리한다.</li>
<li><code>YAML</code> 파일의 훌륭한 <code>가독성</code> 덕분에 사용자들이 느  끼는 <code>Ansible</code>의 <code>진입장벽이 낮다.</code></li>
</ul>
</li>
<li><p><code>멱등성 (Idempotence)</code></p>
<ul>
<li>(핵심) <code>여러 번 수행해도 같은 결과를 뱉는 성질</code>을 말한다.</li>
<li><code>Ansible</code>은 <code>YAML</code>로 관리되는 명령집을 여러 번 수행하더라도 언제나 같은 결과가 나올 수 있도록 여러가지 관리를 합니다.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="📘-ansible-용어">📘 <code>Ansible</code> 용어</h3>
<h3 id="🔹-controller-서버">🔹 Controller 서버</h3>
<ul>
<li><code>Controller 서버</code>는 Ansible에서 공식 용어는 아니지만, 개념을 이해하기 쉽도록 사용되는 표현이다.</li>
<li>(핵심) 여러 원격 서버에 Ansible 명령을 전달하는 <strong>중앙 관리 서버</strong>를 의미한다.</li>
<li>Ansible은 <strong>Agentless</strong> 방식이기 때문에, 원격 서버에는 아무 것도 설치할 필요가 없으며 <strong>Controller 서버에만 Ansible을 설치</strong>하면 된다.</li>
</ul>
<hr />
<h3 id="🔹-인벤토리inventory">🔹 인벤토리(Inventory)</h3>
<ul>
<li><code>인벤토리(Inventory)</code>는 Ansible에서 관리할 <strong>원격 서버 목록(host list)</strong> 을 기록해 둔 파일이다.</li>
<li>다른 말로 <strong>Ansible Hosts 파일</strong>이라고도 한다.</li>
<li>(핵심) Controller 서버가 어떤 원격 서버들에 명령을 보낼지 지정하는 역할을 한다.
즉, <strong>각 Ansible Node의 IP 또는 호스트명을 기록한 파일</strong>이다.</li>
<li>기본 인벤토리는 아래 경로에 존재한다.</li>
</ul>
<pre><code>/etc/ansible/hosts</code></pre><ul>
<li>필요에 따라 프로젝트별로 사용자 지정 인벤토리를 만들 수 있다.</li>
</ul>
<pre><code>inventory.ini
inventory.yml
custom_inventory.lst</code></pre><ul>
<li>인벤토리 예시:</li>
</ul>
<pre><code class="language-ini">[web]
10.10.10.1
10.10.10.2

[db]
150.100.10.1</code></pre>
<hr />
<h3 id="🔹-플레이북playbook">🔹 플레이북(Playbook)</h3>
<ul>
<li><code>플레이북(Playbook)</code>은 원격 서버에서 실행할 작업들을 모아둔 <strong>명령 모음집</strong>이다.</li>
<li><code>YAML</code> 포맷으로 작성되며, 반복되는 서버 설정, 설치, 배포 작업을 자동화하는 핵심 요소이다.</li>
<li>쉽게 말해 <strong>Ansible에서 사용하는 스크립트 파일</strong>과 같은 개념이다.</li>
</ul>
<p>플레이북 예시:</p>
<pre><code class="language-yaml">- hosts: web
  tasks:
    - name: Apache 설치
      yum:
        name: httpd
        state: present</code></pre>
<hr />
<h2 id="22-ansible-설치-및-초기-설정">2.2 Ansible 설치 및 초기 설정</h2>
<h3 id="시스템-구성">시스템 구성</h3>
<ul>
<li><code>Controller Server</code><ul>
<li><code>CentOS</code> (<code>192.168.10.128</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code>)</li>
</ul>
</li>
<li><code>Node Server(원격 서버)</code> <ul>
<li><code>CentOS</code> (<code>192.168.10.129</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code>)</li>
</ul>
</li>
</ul>
<hr />
<h3 id="step-1-controller-server에-ansible-설치">Step 1. <code>Controller Server</code>에 <code>Ansible</code> 설치</h3>
<ul>
<li><code>EPEL yum</code> 레포지토리(패키지 저장소) 설치
```bash
[root@localhost ~]# cd /etc/yum.repos.d/
[root@localhost yum.repos.d]$ ls -l
합계 40</li>
<li>rw-r--r-- 1 root root 1665 10월 16  2024 CentOS-Base.repo</li>
<li>rw-r--r-- 1 root root 1310 10월 16  2024 CentOS-CR.repo</li>
<li>rw-r--r-- 1 root root  649  5월 21  2024 CentOS-Debuginfo.repo</li>
<li>rw-r--r-- 1 root root  630  5월 21  2024 CentOS-Media.repo</li>
<li>rw-r--r-- 1 root root 1332 10월 16  2024 CentOS-Sources.repo</li>
<li>rw-r--r-- 1 root root 9454  5월 21  2024 CentOS-Vault.repo</li>
<li>rw-r--r-- 1 root root  314 10월 16  2024 CentOS-fasttrack.repo</li>
<li>rw-r--r-- 1 root root  616 10월 16  2024 CentOS-x86_64-kernel.repo
<code></code>bash
[root@localhost yum.repos.d]# yum -y install epel-release
[root@localhost yum.repos.d]# ls -l
합계 48</li>
<li>rw-r--r-- 1 root root 1665 10월 16  2024 CentOS-Base.repo</li>
<li>rw-r--r-- 1 root root 1310 10월 16  2024 CentOS-CR.repo</li>
<li>rw-r--r-- 1 root root  649  5월 21  2024 CentOS-Debuginfo.repo</li>
<li>rw-r--r-- 1 root root  630  5월 21  2024 CentOS-Media.repo</li>
<li>rw-r--r-- 1 root root 1332 10월 16  2024 CentOS-Sources.repo</li>
<li>rw-r--r-- 1 root root 9454  5월 21  2024 CentOS-Vault.repo</li>
<li>rw-r--r-- 1 root root  314 10월 16  2024 CentOS-fasttrack.repo</li>
<li>rw-r--r-- 1 root root  616 10월 16  2024 CentOS-x86_64-kernel.repo</li>
<li>rw-r--r-- 1 root root 1050 10월  3  2017 epel-testing.repo</li>
<li>rw-r--r-- 1 root root  951 10월  3  2017 epel.repo</li>
</ul>
<p>[root@localhost yum.repos.d]# yum repolist
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
epel/x86_64/metalink                                                             | 4.4 kB  00:00:00</p>
<ul>
<li>epel: d2lzkl7pfhq30w.cloudfront.net
epel                                                                             | 4.3 kB  00:00:00
(1/3): epel/x86_64/group                                                         | 399 kB  00:00:00
(2/3): epel/x86_64/updateinfo                                                    | 1.0 MB  00:00:00
(3/3): epel/x86_64/primary_db                                                    | 8.7 MB  00:00:05
repo id                           repo name                                                       status
base/7/x86_64                     CentOS-7 - Base                                                 10,072
epel/x86_64                       Extra Packages for Enterprise Linux 7 - x86_64                  13,791
extras/7/x86_64                   CentOS-7 - Extras                                                  526
updates/7/x86_64                  CentOS-7 - Updates                                               6,173
repolist: 30,562</li>
</ul>
<pre><code>
- `Ansible` 설치
```bash
[root@localhost yum.repos.d]# yum -y install ansible

[root@localhost yum.repos.d]# rpm -qa | grep ansible
ansible-2.9.27-1.el7.noarch
[root@localhost yum.repos.d]# yum -y install ansible --version
3.4.3
  Installed: rpm-4.11.3-48.el7_9.x86_64 at 2024-06-14 10:28
  Built    : CentOS BuildSystem &lt;http://bugs.centos.org&gt; at 2021-11-24 16:33
  Committed: Michal Domonkos &lt;mdomonko@redhat.com&gt; at 2021-11-01

  Installed: yum-3.4.3-168.el7.centos.noarch at 2024-06-14 10:28
  Built    : CentOS BuildSystem &lt;http://bugs.centos.org&gt; at 2020-10-01 17:03
  Committed: CentOS Sources &lt;bugs@centos.org&gt; at 2020-09-29

  Installed: yum-plugin-fastestmirror-1.1.31-54.el7_8.noarch at 2024-06-14 10:28
  Built    : CentOS BuildSystem &lt;http://bugs.centos.org&gt; at 2020-05-12 16:27
  Committed: Michal Domonkos &lt;mdomonko@redhat.com&gt; at 2020-03-12
[root@localhost yum.repos.d]#</code></pre><hr />
<h3 id="step-2-ssh-key-설치">Step 2. SSH Key 설치</h3>
<ul>
<li><code>키 생성</code>(Controller Server)
```bash
[root@localhost yum.repos.d]# ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa):
Created directory '/root/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:gmFpVTkZRpbxp0XoDg6SZOPMeISjEz3b+/5xwmus0ww <a href="mailto:root@localhost.localdomain">root@localhost.localdomain</a>
The key's randomart image is:</li>
<li>---[RSA 2048]----+
| . .  .oB* ..    |
|. = =o o=...     |
| o &amp;=o   o. o    |
|o ooOo. . .+     |
| . ..o.oSo.      |
|    . Eo. .      |
|     . =+ .      |
|      o ==       |
|     .o=o        |</li>
<li>----[SHA256]-----+
```</li>
<li>원격 서버에 <code>인증키 복사</code> <pre><code class="language-bash">[root@localhost yum.repos.d]# ssh-copy-id root@192.168.10.129
/bin/ssh-copy-id: INFO: Source of key(s) to be installed: &quot;/root/.ssh/id_rsa.pub&quot;
The authenticity of host '192.168.10.129 (192.168.10.129)' can't be established.
ECDSA key fingerprint is SHA256:5oChX1k6Y9DGu71Q2pCEoyybzLixBDFSJddIeo4YAi4.
ECDSA key fingerprint is MD5:6e:8d:a6:57:3a:61:e8:4f:8b:db:f0:39:23:d1:ce:9a.
Are you sure you want to continue connecting (yes/no)? yes
/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
root@192.168.10.129's password:
</code></pre>
</li>
</ul>
<p>Number of key(s) added: 1</p>
<p>Now try logging into the machine, with:   &quot;ssh 'root@192.168.10.129'&quot;
and check to make sure that only the key(s) you wanted were added.</p>
<pre><code>- `Node Server`에서 확인
```bash
[root@localhost ~]# cd .ssh/
[root@localhost .ssh]# ls -l
합계 4
-rw------- 1 root root 408 11월 27 11:05 authorized_keys
[root@localhost .ssh]#</code></pre><ul>
<li>원격 서버에 접속 테스트<ul>
<li>비밀번호 입력없이 접속되어야함<pre><code class="language-bash">[root@localhost yum.repos.d]# ssh root@192.168.10.129
Last login: Thu Nov 27 11:06:15 2025
[root@localhost ~]# ifconfig
ens32: flags=4163&lt;UP,BROADCAST,RUNNING,MULTICAST&gt;  mtu 1500
    inet 192.168.10.129  netmask 255.255.255.0  broadcast 192.168.10.255
    inet6 fe80::7266:3b98:c173:3040  prefixlen 64  scopeid 0x20&lt;link&gt;
    ether 00:0c:29:45:cd:cd  txqueuelen 1000  (Ethernet)
    RX packets 547  bytes 266673 (260.4 KiB)
    RX errors 0  dropped 0  overruns 0  frame 0
    TX packets 349  bytes 44283 (43.2 KiB)
    TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
</code></pre>
</li>
</ul>
</li>
</ul>
<p>lo: flags=73&lt;UP,LOOPBACK,RUNNING&gt;  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 68  bytes 5916 (5.7 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 68  bytes 5916 (5.7 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0</p>
<p>virbr0: flags=4099&lt;UP,BROADCAST,MULTICAST&gt;  mtu 1500
        inet 192.168.122.1  netmask 255.255.255.0  broadcast 192.168.122.255
        ether 52:54:00:20:20:bb  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0</p>
<p>[root@localhost ~]# exit
logout
Connection to 192.168.10.129 closed.
[root@localhost yum.repos.d]#</p>
<pre><code>---
### Step 3. 인벤토리(Inventory, 재고) 파일 작성
-  `hosts` 파일 백업
```bash
[root@localhost ansible]# cd /etc/ansible/

[root@localhost ansible]# ls -l
합계 28
-rw-r--r-- 1 root root 19985  1월 16  2022 ansible.cfg
-rw-r--r-- 1 root root  1016  1월 16  2022 hosts
drwxr-xr-x 2 root root  4096  1월 16  2022 roles
[root@localhost ansible]# cp -p hosts hosts.samadal</code></pre><ul>
<li><code>Node Server</code> <code>IP</code>입력
```bash
[root@localhost ansible]# vi hosts</li>
</ul>
<p>192.168.10.129 # Node Server IP 입력</p>
<h1 id="this-is-the-default-ansible-hosts-file">This is the default ansible 'hosts' file.</h1>
<p>...</p>
<pre><code>- 
```bash
[root@localhost ansible]# ansible all -m ping
192.168.10.129 | SUCCESS =&gt; {
    &quot;ansible_facts&quot;: {
        &quot;discovered_interpreter_python&quot;: &quot;/usr/bin/python&quot;
    },
    &quot;changed&quot;: false,
    &quot;ping&quot;: &quot;pong&quot;
}
[root@localhost ansible]#</code></pre><hr />
<h3 id="step-4-ansible-명령어-구조">Step 4. Ansible 명령어 구조</h3>
<ul>
<li>구조 <code>Ansible</code> [Host 또는 Host 그룹] options</li>
<li>설명 <ul>
<li><code>[Host 또는 Host 그룹]</code> <ul>
<li><code>Ansible</code> 명령을 전달할 <code>원격 서버들(Node Server)</code>을 설정한다.</li>
<li><code>all</code>을 사용하면 인벤토리 파일에 입력되어 있는 모든 원격 서버들에게 명령을 전달한다.</li>
</ul>
</li>
<li><code>options</code><ul>
<li><code>-m</code> 옵션이 가장 많이 사용되는 옵션이다.</li>
<li><code>ansible</code>에서 모듈을 호출하는 옵션이다</li>
<li>모듈마다 필요한 인자값들이 다르기 때문에 계속해서 확인해야 한다.</li>
</ul>
</li>
</ul>
</li>
<li>예시 <pre><code class="language-bash">ansible all -m ping</code></pre>
</li>
</ul>
<hr />
<h2 id="23-실습">2.3 실습</h2>
<h3 id="실습-1-ansible의-이해">실습 1. Ansible의 이해</h3>
<ul>
<li>개요 <ul>
<li>간단한 기능을 확인하기 위해서 플레이북을 사용하지 않고 CLI Mode에서 명령어를 직접 입력한다.</li>
<li><code>Controller Server</code>에 <code>/Ansible/test.txt</code> 파일을 생성하고 <code>Node Server</code>에 복사하는 실습을 하도록 한다.<pre><code class="language-bash">[root@localhost ansible]# mkdir /Ansible
[root@localhost ansible]# cd /
[root@localhost Ansible]# echo &quot;nsible Structure by Samadal! &gt; test.txt
</code></pre>
</li>
</ul>
</li>
</ul>
<p>[root@localhost Ansible]# ansible all -m copy -a &quot;src=./test.txt dest=/Node1/test.txt&quot;
192.168.10.129 | CHANGED =&gt; {
    &quot;ansible_facts&quot;: {
        &quot;discovered_interpreter_python&quot;: &quot;/usr/bin/python&quot;
    },
    &quot;changed&quot;: true,
    &quot;checksum&quot;: &quot;673fed54ccc712ca8dab548e158a5d7f46f0f434&quot;,
    &quot;dest&quot;: &quot;/Node1/test.txt&quot;,
    &quot;gid&quot;: 0,
    &quot;group&quot;: &quot;root&quot;,
    &quot;md5sum&quot;: &quot;86629ef9eaa2360cbdc592fd16cd18eb&quot;,
    &quot;mode&quot;: &quot;0644&quot;,  복사된 파일의 허가권
    &quot;owner&quot;: &quot;root&quot;,  Node Server의 소유자
    &quot;size&quot;: 30,  복사된 파일의 크기
    &quot;src&quot;: &quot;/root/.ansible/tmp/ansible-tmp-1764212031.56-58019-29310862153038/source&quot;,
    &quot;state&quot;: &quot;file&quot;,  복사된 파일의 성격
    &quot;uid&quot;: 0
}</p>
<pre><code>
- 명령 실행
- 설명 
```bash
ansible all -m copy -a &quot;src=./test.txt dest=/Node1/test.txt&quot;</code></pre><ul>
<li><code>-a</code>는 <code>copy 모듈</code>에 필요한 인자값을 전달하는 옵션이다.
즉 , <code>속성값(Attribution Value)</code>을 전달하는 옵션이다.<ul>
<li><code>Node Server</code>에서 확인
```
[root@localhost /]# ls -l /Node1/
합계 4</li>
<li>rw-r--r-- 1 root root 30 11월 27 11:53 test.txt
[root@localhost /]#
```<h3 id="실습-2-옵션을-이용한-예제">실습 2. 옵션을 이용한 예제</h3>
</li>
<li>개요</li>
</ul>
</li>
<li>원격 서버가 현재 한 대밖에 없기 때문에 한 개씩만 입력하면 된다.<pre><code class="language-bash">[root@localhost Ansible]# echo 192.168.10.129 &gt;&gt; customized_inven.lst
[root@localhost Ansible]#
[root@localhost Ansible]# cat customized_inven.lst
192.168.10.129
[root@localhost Ansible]# ansible -i customized_inven.lst all -m ping -k
SSH password:
192.168.10.129 | SUCCESS =&gt; {
&quot;ansible_facts&quot;: {
    &quot;discovered_interpreter_python&quot;: &quot;/usr/bin/python&quot;
},
&quot;changed&quot;: false,
&quot;ping&quot;: &quot;pong&quot;
}</code></pre>
<ul>
<li>옵션 1. <code>-i</code> </li>
</ul>
</li>
<li>적용될 노드(들)을 선택하는 옵션</li>
<li>선수 작업</li>
<li>명령 1. <code>customized_inven.lst</code> 파일에 추가된 <code>Node</code>들에 대해서 만 응답을 받는다.<ul>
<li><code>-m</code>뒤에 <code>ping</code>이라는 모듈을 이용해서 <code>Ansible Server</code> 와 <code>Node Server</code> 사이의 통신을 체크한다.</li>
<li><code>k</code> 옵션은 <code>Node Server</code>의 <code>비밀번호</code>를 입력 받는다.</li>
</ul>
</li>
<li>명령 실행 2. <code>all</code> 대신에 <code>Node1</code>의 <code>IP주소</code>를 입력하면 <code>필요한 노드에만 원하는 작업을 수행</code>할 수 있다.
```bash
[root@localhost Ansible]# ansible -i customized_inven.lst 192.168.10.129 -m ping -k
SSH password:</li>
</ul>
<p>  192.168.10.129 | SUCCESS =&gt; {
    &quot;ansible_facts&quot;: {
        &quot;discovered_interpreter_python&quot;: &quot;/usr/bin/python&quot;
    },
    &quot;changed&quot;: false,
    &quot;ping&quot;: &quot;pong&quot;
  }</p>
<pre><code>
  - 명령 실행 3. 파일 복사
  ```bash
  [root@localhost Ansible]# ansible -i customized_inven.lst 192.168.10.129 -m copy -a &quot;src=./test.txt dest=/Node1/test.txt&quot;</code></pre><ul>
<li><p>옵션 2. <code>-k</code></p>
<ul>
<li>적용될 노드(들)의 암호를 물어보도록 설정한다.</li>
<li>이미 인증키가 등록되어 있기 때문에 이 옵션을 사용하지 않아도 결과는 모두 동일하다.</li>
<li>명령 실행<pre><code class="language-bash">[root@localhost Ansible]# ansible all -m ping -k</code></pre>
</li>
</ul>
</li>
<li><p>옵션 3. <code>--list-hosts</code></p>
<ul>
<li>적용되는 노드(들)을 확인한다.</li>
<li>어떤 노드들이 적용되는지 확인해야 할 필요가 있는데 사용법은 옵션 입력 부분 중에 입력한다.</li>
<li>명령 실행<pre><code class="language-bash">[root@localhost Ansible]# ansible all -m ping --list-hosts
 hosts (1):
   192.168.10.129</code></pre>
</li>
</ul>
</li>
<li><p>옵션 4. <code>-m shell</code></p>
<ul>
<li>사용할 모듈을 선택하는 용도로 사용된다.</li>
<li><code>shell</code> 모듈<ul>
<li>노드들에 명령 구문을 전달하고 해당 결과를 다시 반환하는 모듈이다.</li>
<li>(핵심) <code>Bash Shell</code>에서 명령을 실행하는 것과 같다고 생각하면 된다.</li>
<li>(중요) <code>shell</code>은 <code>Bash Shell</code>과 같은 역할을 하고 <code>-a</code>는 <code>uptime(가동 시간), cd,ls, df, free</code> 등의 명령구문으로 이루어져 있다.               </li>
<li>(특징) <code>shell</code> 모듈 뒤에는 <code>-a</code> 옵션으로 필요한 인자값을 넣어서 사용한다.</li>
</ul>
</li>
<li>명령 실행 1. <code>Ansible</code>에서 사용 가능한 모듈 확인 <pre><code class="language-bash">[root@localhost Ansible]# ansible-doc -l
fortios_router_community_list    Configure community lists in Fortinet...
azure_rm_devtestlab_info                                      Get Azure DevTest Lab facts
ecs_taskdefinition                                            register a task definition in ecs
...</code></pre>
</li>
<li>명령 실행 2. 모든 <code>Node Server</code>들의 가동 시간을 확인
```bash
[root@localhost Ansible]# ansible all -m shell -a &quot;uptime&quot; -k
SSH password:</li>
</ul>
<p>192.168.10.129 | CHANGED | rc=0 &gt;&gt;
12:56:07 up  2:05,  3 users,  load average: 0.00, 0.02, 0.05</p>
<pre><code>- 명령 실행 3. 각 `Node Server`들의 디스크 사용량과 메모리 사용량을 확인
```bash
[root@localhost Ansible]# ansible all -m shell -a &quot;df -h&quot;
192.168.10.129 | CHANGED | rc=0 &gt;&gt;
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        895M     0  895M   0% /dev
tmpfs           910M     0  910M   0% /dev/shm
tmpfs           910M   11M  900M   2% /run
tmpfs           910M     0  910M   0% /sys/fs/cgroup
/dev/sda1        22G  4.8G   16G  24% /
tmpfs           182M   28K  182M   1% /run/user/0
tmpfs           182M     0  182M   0% /run/user/1000</code></pre><pre><code class="language-bash">[root@localhost Ansible]# ansible all -m shell -a &quot;free -h&quot;
192.168.10.129 | CHANGED | rc=0 &gt;&gt;
               total        used        free      shared  buff/cache   available
Mem:           1.8G        691M        352M         19M        775M        949M
Swap:          2.0G          0B        2.0G</code></pre>
<ul>
<li>명령 실행 4. 큰 따옴표는 가급적 사용하는 것이 좋다
```bash
[root@localhost Ansible]# ansible all -m shell -a ls -l
ansible: error: argument -l/--limit: expected one argument
... # 오류
[root@localhost Ansible]# ansible all -m shell -a &quot;ls -l&quot;</li>
</ul>
<p>192.168.10.129 | CHANGED | rc=0 &gt;&gt;
합계 40
-rw-------. 1 root root 1800  6월 14  2024 
... # 정상
```</p>
<h3 id="실습-3-많이-사용하는-다양한-모듈">실습 3. 많이 사용하는 다양한 모듈</h3>
</li>
<li><p><code>user</code> 모듈</p>
<ul>
<li><p>개요</p>
<ul>
<li><code>Controller</code>, <code>Node1</code>, <code>Node2</code></li>
</ul>
</li>
<li><p>작업 1. 사용자 추가</p>
<ul>
<li>사용법 
```bash</li>
<li>m user -a &quot;name=사용자명&quot;
```</li>
<li>사전 확인 및 수정<ul>
<li>3개의 시스템에서 사용자 관련 파일3개(passwd, shadow, group) 에서 <code>samadal</code>을 모두 맨 밑으로 이동<pre><code class="language-bash">vi /etc/passwd
vi /etc/group
vi /etc/shadow</code></pre>
</li>
</ul>
</li>
<li>(오류)실행 1. <code>Node</code>의 <code>IP</code>가 등록된 파일<code>(customized_inven.lst)</code>을 이용해서 사용자 추가
```bash
[root@controller Ansible]# cat customized_inven.lst</li>
</ul>
<p>192.168.10.129
[root@controller Ansible]# ansible all -i customized_inven.lst -m user -a &quot;name=hmcloud1&quot;</p>
<pre><code>```bash
[root@node1 ~]# cat /etc/passwd | grep hmcloud1
hmcloud1:x:1001:1001::/home/hmcloud1:/bin/bash</code></pre><pre><code class="language-bash">[root@controller Ansible]# vi customized_inven.lst
192.168.10.129
192.168.10.130</code></pre>
<ul>
<li>(오류)실행 2. 인벤토리 파일<code>(/etc/ansible/hosts)</code>에 신규 <code>Node</code>의 <code>IP</code>를 등록한 후 사용자 추가<pre><code class="language-bash">[root@controller Ansible]# ansible all -i customized_inven.lst -m user -a &quot;name=hmcloud1&quot;</code></pre>
</li>
<li>(정상)실행 3. 신규 <code>Node</code> 시스템에 인증키 복사 후 사용자 추가
```bash
[root@controller Ansible]# ssh-copy-id <a href="mailto:root@192.168.10.130">root@192.168.10.130</a>
[root@controller Ansible]# ansible all -m shell -a &quot;ls -l /root/.ssh&quot;
[root@controller Ansible]# ansible all -i customized_inven.lst -m user -a &quot;name=hmcloud1&quot;
[root@controller Ansible]# ansible all -m shell -a &quot;cat /etc/passwd | grep hmcloud1&quot;</li>
</ul>
<p>192.168.10.129 | CHANGED | rc=0 &gt;&gt;
hmcloud1:x:1001:1001::/home/hmcloud1:/bin/bash
192.168.10.130 | CHANGED | rc=0 &gt;&gt;
hmcloud1:x:1001:1001::/home/hmcloud1:/bin/bash</p>
<pre><code></code></pre></li>
<li><p>작업 2. 사용자 삭제</p>
<ul>
<li>사용법 
```bash</li>
<li>m user -a &quot;name=사용자명 state=absent&quot;<pre><code>```bash
[root@controller Ansible]# ansible all -m user -a &quot;name=hmcloud1 state=absent&quot;</code></pre></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li><code>yum</code> 모듈<ul>
<li>개요<ul>
<li><code>패키지</code>를 설치하는 모듈이다.</li>
</ul>
</li>
<li>작업 1. <code>패키지</code> 설치 <code>유무</code>에 따른 실습 <ul>
<li><code>패키지</code> 설치가 안되어 있는 경우 (그러나 관련 패키지를 모두 설치하지는 못한다)
```bash
[root@controller Ansible]# ansible all -m shell -a &quot;rpm -qa | grep httpd&quot;
[WARNING]: Consider using the yum, dnf or zypper module rather than running 'rpm'.  If you need to use
command because yum, dnf or zypper is insufficient you can add 'warn: false' to this command task or
set 'command_warnings=False' in ansible.cfg to get rid of this message.</li>
</ul>
192.168.10.130 | CHANGED | rc=0 &gt;&gt;
httpd-2.4.6-99.el7.centos.1.x86_64
httpd-tools-2.4.6-99.el7.centos.1.x86_64
192.168.10.129 | CHANGED | rc=0 &gt;&gt;
httpd-2.4.6-99.el7.centos.1.x86_64
httpd-tools-2.4.6-99.el7.centos.1.x86_64<pre><code>- `패키지`가 설치되어 있는 경우
```bash
[root@controller Ansible]# ansible all -m shell -a &quot;rpm -qa | grep httpd&quot;
[WARNING]: Consider using the yum, dnf or zypper module rather than running 'rpm'.  If you need to use
command because yum, dnf or zypper is insufficient you can add 'warn: false' to this command task or
set 'command_warnings=False' in ansible.cfg to get rid of this message.
192.168.10.130 | CHANGED | rc=0 &gt;&gt;
httpd-2.4.6-99.el7.centos.1.x86_64
httpd-manual-2.4.6-99.el7.centos.1.noarch
httpd-tools-2.4.6-99.el7.centos.1.x86_64
httpd-devel-2.4.6-99.el7.centos.1.x86_64
192.168.10.129 | CHANGED | rc=0 &gt;&gt;
httpd-2.4.6-99.el7.centos.1.x86_64
httpd-manual-2.4.6-99.el7.centos.1.noarch
httpd-tools-2.4.6-99.el7.centos.1.x86_64
httpd-devel-2.4.6-99.el7.centos.1.x86_64</code></pre></li>
<li>작업 2. <code>Ansible</code> 환경 설정 파일(ansible.cfg) 변경 유무에 따른 패키지 확인<ul>
<li>명령 실행 시 <code>[WARNING]: Consider using ...</code>을 나타나지 않게 한다.<pre><code class="language-bash">[root@controller Ansible]# vi /etc/ansible/ansible.cfg
188 command_warnings = False</code></pre>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li><code>copy</code> 모듈<ul>
<li>개요<ul>
<li><code>Controller Server</code>에서 <code>Node Server</code>로 파일을 전송할 때 사용하는 모듈</li>
<li><code>Web Server</code>의 기본 페이지를 변경하기 위한 실습을 한다</li>
</ul>
</li>
<li>작업 1. 로컬 시스템에서의 작업<ul>
<li><code>Controller Server</code>에서 <code>웹 서버의 기본 경로(/var/www/html)</code>에 <code>파일(index.html)</code> 생성 한 후 <code>Node Server</code>에게 파일을 전송<pre><code class="language-bash">[root@controller Ansible]# vi /var/www/html/index.html
[root@controller Ansible]# ansible all -m copy -a &quot;src=/var/www/html/index.html dest=/var/www/html/index.html&quot;</code></pre>
</li>
</ul>
</li>
<li>작업 2. <code>Public Cloud</code> 시스템과 연동<ul>
<li>Step 1. <code>/Ansible</code>에 <code>ec2.lst</code>라는 파일을 생성한다.</li>
<li>Step 2. <code>/Ansible</code>에 임의의 내용이 기입된 <code>test.txt</code>라는 파일을 생성한다</li>
<li>Step 3. <code>AWS</code>에서 <code>EC2 Instance</code>를 생성하고 <code>EC2 콘솔창</code>에서 <code>/ec2</code>라는 디렉토리를 생성<ul>
<li><code>사용자 계정(user1)</code>은 이미 삭제되었기 때문에<code>관리자 계정(root)</code>으로 로그인한다</li>
<li><code>Region</code>을 <code>아시아 태평양(서울)</code>로 변경한다.</li>
<li>좌측 상단에서 <code>컴퓨팅</code> 서비스 하위에 있는 <code>EC2</code>를 클릭한다.</li>
<li>대시보드 하단에 있는 <code>인스턴스</code>를 클릭한다.</li>
<li>우측에 있는 <code>인스턴스 시작</code>을 클릭한다.</li>
<li>인스턴스 명은 <code>InstAnsible</code>로 입력한다.</li>
<li><code>Amaznon Machine Image(AMI)</code>는 <code>Amazon Linux</code>를 클릭한다.</li>
<li>(옵션(<code>키 페어(로그인)</code>에 있는 <code>새 키페어 생성</code>을 클릭한다 </li>
<li><code>키페어 명</code>은 <code>keyAnsible</code>로 입력한 후 <code>키 페어 생성</code>을 클릭한다.</li>
<li><code>다운로드</code> 폴더에 저장된 <code>키페어(KeyAnsible.pem)</code>를 확인한다.</li>
<li>우측 하단에 있는 <code>인스턴스 시작</code>을 클릭한다.</li>
<li>생성된 인스턴스를 확인하고 이름을 체크한 후 우측 상단에 있는 <code>연결</code>을 클릭한다.</li>
<li>새로운 창이 출력되고 <code>첫 번째 탭(EC2 인스턴스 연결)</code>을 클릭한 후 우측 하단에 있는 <code>연결</code>을 클릭하면 <code>EC2 콘솔창</code>이 실행된다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4fc1ffa2-4f8c-40ae-a071-3143f0e6da93/image.png" /></li>
<li>(특징)따라서 이 화면에서 작업하게 되면 <code>Putty</code>를 이용한 원격접속이 필요가 없다.</li>
<li><code>/ec2</code>라는 디렉토리를 생성한다.</li>
<li>상단의 <code>즐겨찾기</code>에 있는 <code>EC2</code>를 클릭한 후 인스턴스 목록으로 들어간다.</li>
<li><code>InstAnsible</code> 옆에 있는 <code>인스턴스 ID</code>의 링크를 클릭한다.</li>
<li><code>인스턴스 요약</code>에 있는 <code>퍼블릭 IPv4 주소</code> 하단에 있는 <code>IP(3.38.164.95)</code>를 복사한다.</li>
<li>하단에 있는 <code>보안</code>탭을 클릭하고 <code>22번 포트</code>가 등록되어 있는지 확인한다.</li>
<li>참고로 <code>EC2 인스턴스</code>는 <code>22번 포트</code>가 기본적으로 등록되어 있다.</li>
</ul>
</li>
<li>Step 4. <code>EC2 인스턴스</code>의 <code>Public IP 주소</code>를 생성한 <code>ec2.lst</code>파일에 입력한다.
```bash
[root@controller Ansible]# cat /Ansible/ec2.lst</li>
</ul>
3.38.164.95<pre><code>- Step 5. `/Ansible`에 있는 `test.txt`파일을 `EC2 인스턴스` 시스템에 복사한다.
- 오류
```bash
[root@controller Ansible]# ansible -i ec2.lst 3.38.164.95 -m copy -a &quot;src=/Ansible/test.txt dest=/ec2/test.txt&quot;
The authenticity of host '3.38.164.95 (3.38.164.95)' can't be established.
ECDSA key fingerprint is SHA256:wBSu1F5N/3fRqC1OvWMsQ9FgHZyCTfa3x4kFg44jbvw.
ECDSA key fingerprint is MD5:28:20:53:3f:f4:32:39:d0:ee:bd:1c:f6:ff:e5:bb:40.
Are you sure you want to continue connecting (yes/no)? yes
3.38.164.95 | UNREACHABLE! =&gt; {
  &quot;changed&quot;: false,
  &quot;msg&quot;: &quot;Failed to connect to the host via ssh: Warning: Permanently added '3.38.164.95' (ECDSA) to the list of known hosts.\r\nPermission denied (publickey,gssapi-keyex,gssapi-with-mic).&quot;,
  &quot;unreachable&quot;: true
}</code></pre><ul>
<li><code>ec2-user</code> <code>Permission denied</code><pre><code class="language-bash">[root@controller Ansible]# ssh-copy-id ec2-user@3.38.164.95
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: &quot;/root/.ssh/id_rsa.pub&quot;
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
Permission denied (publickey,gssapi-keyex,gssapi-with-mic).</code></pre>
</li>
<li><code>root</code>로 접속<pre><code class="language-bash">[root@controller Ansible]# ssh-copy-id root@3.38.164.95
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: &quot;/root/.ssh/id_rsa.pub&quot;
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
Permission denied (publickey,gssapi-keyex,gssapi-with-mic).</code></pre>
</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e60a44d3-fa12-4f13-8e33-7784f1ab2482/image.png" /></li>
<li>관리자에서 생성한 인스턴스를 삭제하고 사용자를 생성하고 생성된 사용자로 로그인한 후 위 작업을 다시 해본다.</li>
<li><code>Amazon Linux</code> 대신 다른 것으로 한 번 할 것을 고려해본다. 즉, <code>t3.micro</code>가 아닌 <code>t2.micro</code>로 </li>
<li>만약 <code>CentOS</code>가 <code>아시아 태평양(서울)</code>에 없다면 다른 <code>Region</code>도 고려해본다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li><p><code>Service</code> 모듈</p>
<ul>
<li><p>개요</p>
<ul>
<li><code>서비스(데몬)</code>을 관리하는 모듈이다.</li>
</ul>
</li>
<li><p>작업</p>
<ul>
<li><code>Apache Daemon</code> 실행<pre><code class="language-bash">[root@controller ~]# ansible all -m service -a &quot;name=httpd state=started&quot;
</code></pre>
</li>
</ul>
<p>192.168.10.129 | SUCCESS =&gt; {</p>
<pre><code>&quot;ansible_facts&quot;: {
    &quot;discovered_interpreter_python&quot;: &quot;/usr/bin/python&quot;
},
&quot;changed&quot;: false,
&quot;name&quot;: &quot;httpd&quot;,
&quot;state&quot;: &quot;started&quot;,
&quot;status&quot;: {
    ...
}</code></pre><p>}
192.168.10.130 | UNREACHABLE! =&gt; {</p>
<pre><code>&quot;changed&quot;: false,
&quot;msg&quot;: &quot;Failed to connect to the host via ssh: Host key verification failed.&quot;,
&quot;unreachable&quot;: true</code></pre><p>}</p>
<p>[root@controller ~]# ansible all -m shell -a &quot;ps -ef | grep httpd&quot;
192.168.10.129 | CHANGED | rc=0 &gt;&gt;
root       2101   2096  0 09:54 pts/1    00:00:00 /bin/sh -c ps -ef | grep httpd
root       2103   2101  0 09:54 pts/1    00:00:00 /bin/sh -c ps -ef | grep httpd
192.168.10.130 | CHANGED | rc=0 &gt;&gt;
root       2192   2187  0 09:54 pts/1    00:00:00 /bin/sh -c ps -ef | grep httpd
root       2194   2192  0 09:54 pts/1    00:00:00 grep httpd</p>
<p>[root@controller ~]# ansible all -m shell -a &quot;netstat -atunp | grep httpd&quot;
192.168.10.129 | CHANGED | rc=0 &gt;&gt;
tcp6       0      0 :::80                   :::*                    LISTEN      2224/httpd
192.168.10.130 | CHANGED | rc=0 &gt;&gt;
tcp6       0      0 :::80                   :::*                    LISTEN      2318/httpd</p>
<p>[root@controller ~]# systemctl restart httpd</p>
<p>[root@controller ~]# ansible all -m service -a &quot;name=httpd state=started&quot;
192.168.10.129 | SUCCESS =&gt; {</p>
<pre><code>&quot;ansible_facts&quot;: {
    &quot;discovered_interpreter_python&quot;: &quot;/usr/bin/python&quot;
},
&quot;changed&quot;: false,
&quot;name&quot;: &quot;httpd&quot;,
&quot;state&quot;: &quot;started&quot;,
&quot;status&quot;: {
...</code></pre><p>   }
}</p>
<p>192.168.10.130 | SUCCESS =&gt; {</p>
<pre><code>&quot;ansible_facts&quot;: {
    &quot;discovered_interpreter_python&quot;: &quot;/usr/bin/python&quot;
},
&quot;changed&quot;: false,
&quot;name&quot;: &quot;httpd&quot;,
&quot;state&quot;: &quot;started&quot;,
&quot;status&quot;: {
...
}</code></pre><p>}</p>
<pre><code>- `사이트 출력`
  - (오류)출력 1. `Controller Server`의 `firefox`에서 `Node Servere들`의 `IP주소`를 차례로 입력, 출력한다.
  - 출력 2. CLI Mode로 출력(확인)
```bash
[root@controller ~]# systemctl restart httpd
[root@controller ~]#
[root@controller ~]# curl http://192.168.10.129
curl: (7) Failed connect to 192.168.10.129:80; 호스트로 갈 루트가 없음
[root@controller ~]#
[root@controller ~]# curl http://192.168.10.130
curl: (7) Failed connect to 192.168.10.130:80; 호스트로 갈 루트가 없음

[root@controller ~]# ansible all -m shell -a &quot;firewall-cmd --add-service=http --permanent&quot;
192.168.10.130 | CHANGED | rc=0 &gt;&gt;
success
192.168.10.129 | CHANGED | rc=0 &gt;&gt;
success

[root@controller ~]# ansible all -m shell -a &quot;firewall-cmd --add-port=80/tcp --permanent&quot;
192.168.10.129 | CHANGED | rc=0 &gt;&gt;
success
192.168.10.130 | CHANGED | rc=0 &gt;&gt;
success

[root@controller ~]# ansible all -m shell -a &quot;firewall-cmd --reload&quot;
192.168.10.130 | CHANGED | rc=0 &gt;&gt;
success
192.168.10.129 | CHANGED | rc=0 &gt;&gt;
success

[root@controller ~]# curl http://192.168.10.129
Hello have a nice day

[root@controller ~]# curl http://192.168.10.130
Hello have a nice day</code></pre><ul>
<li><code>패키지 삭제</code>
```bash
[root@controller ~]# ansible all -m yum -a &quot;name=httpd state=absent&quot;</li>
</ul>
<p>192.168.10.129 | CHANGED =&gt; {</p>
<pre><code>&quot;ansible_facts&quot;: {
    &quot;discovered_interpreter_python&quot;: &quot;/usr/bin/python&quot;
},
&quot;changed&quot;: true,
&quot;changes&quot;: {
    &quot;removed&quot;: [
        &quot;httpd&quot;
 ...</code></pre><p>   ]
}</p>
<p>192.168.10.130 | CHANGED =&gt; {</p>
<pre><code>&quot;ansible_facts&quot;: {
    &quot;discovered_interpreter_python&quot;: &quot;/usr/bin/python&quot;
},
&quot;changed&quot;: true,
&quot;changes&quot;: {
    &quot;removed&quot;: [
        &quot;httpd&quot;
 ...</code></pre><p>   ]
}</p>
<p>[root@controller ~]# ansible all -m shell -a &quot;rpm -qa | grep httpd&quot;
192.168.10.129 | CHANGED | rc=0 &gt;&gt;
httpd-tools-2.4.6-99.el7.centos.1.x86_64
192.168.10.130 | CHANGED | rc=0 &gt;&gt;
httpd-tools-2.4.6-99.el7.centos.1.x86_64</p>
<p>[root@controller ~]# ansible all -m yum -a &quot;name=httpd-tools state=absent&quot;</p>
<pre><code>



</code></pre></li>
</ul>
</li>
</ul>
<hr />
<h3 id="실습-4-작업할-내용을-파일로-작성플레이북-playbook">실습 4. 작업할 내용을 파일로 작성(플레이북, Playbook)</h3>
<ul>
<li><p>지금까지 <code>Ansible</code>로 웹 서버를 설치하기 위해 총 <strong>5단계 작업</strong>이 필요하다는 것을 확인했다.
(예: 기본 페이지 다운로드/업로드, 패키지 설치, httpd 데몬 실행, 방화벽 설정, 사이트 출력 확인 등)</p>
</li>
<li><p>이렇게 여러 단계를 순서대로 수행해야 하는 작업에 대해 Ansible은 <strong>플레이북(Playbook)</strong>이라는 기능을 제공한다.</p>
</li>
<li><p><strong>플레이북(Playbook)</strong>의 사전적 의미는
<em>각본, 작전, 계획(Plan, Script)</em>
그중에서도 Ansible과 가장 잘 맞는 의미는 <strong>“각본(Script)”</strong>이다.</p>
</li>
<li><p>이유는 아주 간단하다.
👉 <strong>Playbook은 미리 정의된 작업을 지정한 순서대로 자동 실행하는 ‘절차적 실행 계획’</strong>이기 때문이다.
즉, 사람이 직접 명령어를 하나씩 입력하지 않아도
<strong>Ansible이 플레이북에 적힌 대로 순서대로 자동 수행</strong>하는 구조다.</p>
</li>
<li><p>본격적으로 웹 서버 설치 과정을 Playbook으로 변환하여 실행하면서,
<strong>플레이북이 어떤 구조로 작성되고 어떤 방식으로 동작하는지</strong> 직접 살펴볼 것이다.</p>
</li>
<li><p>그 전에 Playbook을 구성하는 핵심 요소 두 가지를 먼저 알고 가야 한다:</p>
</li>
</ul>
<hr />
<h3 id="🔑--yamlyaml-형식">🔑  YAML(Yaml) 형식</h3>
<ul>
<li>Ansible Playbook은 <strong>YAML 포맷</strong>으로 작성된다.</li>
<li>YAML은 사람이 읽기 쉽게 설계된 데이터 표현 방식으로, 들여쓰기와 구조가 매우 중요하다.</li>
<li>JSON보다 직관적이고 간단하기 때문에 Playbook 작성에 적합하다.</li>
</ul>
<hr />
<h3 id="🔑--멱등성idempotence">🔑  멱등성(Idempotence)</h3>
<ul>
<li><p>Ansible에서 가장 중요한 원리.</p>
</li>
<li><p>“<strong>한 번 실행하든, 여러 번 실행하든 결과가 항상 동일</strong>하다”는 의미이다.</p>
</li>
<li><p>예:</p>
<ul>
<li>httpd가 이미 설치되어 있다면, 다시 설치하지 않는다.</li>
<li>서비스가 이미 실행 중이면 start 명령을 또 실행해도 시스템 상태는 변하지 않는다.</li>
</ul>
</li>
<li><p>즉, <strong>Playbook을 여러 번 실행해도 안전하게 유지되는 것</strong>이 Ansible의 강점이다.</p>
</li>
</ul>
<hr />
<h3 id="예제를-통한-이해">예제를 통한 이해</h3>
<h4 id="멱등성이-없는-경우">멱등성이 없는 경우</h4>
<h4 id="멱등성이-있는-경우">멱등성이 있는 경우</h4>
<ul>
<li><p>개요</p>
<ul>
<li><code>shell</code> 모듈은 명령을 그대로 전달하기 때문에 멱등성이 고려되지 않기 때문에 <code>lineinfile</code> 모듈을 사용한다.</li>
<li><code>Ansible</code>에서 제공하는 거의 대부분의 모듈은 멱등성이 적용되어 있지만 (중요) <code>shell</code>과 같은 명령어를 그대로 전달하는 경우에는 멱등성이 없다.</li>
<li><code>path=&lt;경로를 포함한 파일&gt;</code>, <code>line=&lt;추가할 내용&gt;</code>을 의미한다.</li>
</ul>
</li>
<li><p>명령
```bash
[root@controller Ansible]# ansible localhost -c local -m lineinfile -a &quot;path=customized_inven.lst line=192.168.10.132&quot;
localhost | CHANGED =&gt; {
  &quot;backup&quot;: &quot;&quot;,
  &quot;changed&quot;: true,
  &quot;msg&quot;: &quot;line added&quot;
}
[root@controller Ansible]# cat customized_inven.lst</p>
</li>
</ul>
<p>192.168.10.129
192.168.10.130
192.168.10.131
192.168.10.131
192.168.10.132
[root@controller Ansible]# ansible localhost -c local -m lineinfile -a &quot;path=customized_inven.lst line=192.168.10.132&quot;localhost | SUCCESS =&gt; {
    &quot;backup&quot;: &quot;&quot;,
    &quot;changed&quot;: false,
    &quot;msg&quot;: &quot;&quot;
}
[root@controller Ansible]# cat customized_inven.lst
192.168.10.129
192.168.10.130
192.168.10.131
192.168.10.131
192.168.10.132 # 더 이상 추가되지 않음</p>
<pre><code>---

### 플레이북 (PlayBook)
- 개요
  - `플레이북 (PlayBook)`은 `Ansible PlayBook(ansible-playbook)`이라는 파일로 실행된다.
  -  기존에 웹 서버를 설치하기 위해 수행했던 부분들을 모두 `플레이북(PlayBook)` 안에 녹여내고 `Ansible PlayBook(ansible-playbook)`으로 실행하도록 한다.
- 코드 생성
```bash
[root@controller Ansible]# vi nginx_install.yml

- name: Install nginx on linux
  hosts: nginx
  gather_facts: no

  tasks:
    - name: install epel-release
      yum: name=epel-release state=latest
    - name: install nginx web server
      yum: name=nginx state=present
    - name: upload default index.html for web server
      get_url: url=https://www.nginx.com dest=/usr/share/nginx/html/ mode=0644
    - name: start nginx web server
      service: name=nginx state=started</code></pre><ul>
<li>실행 1. 오류<pre><code class="language-bash">[root@controller Ansible]# ansible-playbook nginx_install.yml
[WARNING]: Could not match supplied host pattern, ignoring: nginx
</code></pre>
</li>
</ul>
<p>PLAY [Install nginx on linux] <strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong>
skipping: no hosts matched</p>
<p>PLAY RECAP <strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>*****</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></p>
<pre><code>- `/etc/ansible/hosts` 첫줄 `[nginx]` 추가 후 실행
```bash
[root@controller Ansible]# cat /etc/ansible/hosts
[nginx] 
192.168.10.129
192.168.10.130
# This is the default ansible 'hosts' file.
#</code></pre><ul>
<li>실행 2. 정상<pre><code class="language-bash">[root@controller Ansible]# ansible-playbook nginx_install.yml
</code></pre>
</li>
</ul>
<p>PLAY [Install nginx on linux] <strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></p>
<p>TASK [install epel-release] <strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>****</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong>
changed: [192.168.10.130]
changed: [192.168.10.129]
...</p>
<pre><code>- 설명
  - `---`
    - `플레이북`의 처음은 `---`으로 시작하여 `yml`파일임을 명시한다.
    - `Shell Scripting`에서의 맨 첫줄에 `#!/bin/bash` 등과 유사하다.
    - 일반적으로 말하는 `컴퓨터 언어(C/C++, Java, ...)`에서의 `Header File 선언(#include &lt;stdio.h&gt;`과도 유사하다.
</code></pre>