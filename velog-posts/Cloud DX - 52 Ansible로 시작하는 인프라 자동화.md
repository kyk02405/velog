# Cloud DX - 52 Ansible로 시작하는 인프라 자동화

- 📅 Published: Fri, 28 Nov 2025 08:41:42 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-52-%EC%95%A4%EC%84%9C%EB%B8%94%EB%A1%9C-%EC%8B%9C%EC%9E%91%ED%95%98%EB%8A%94-%EC%9D%B8%ED%94%84%EB%9D%BC-%EC%9E%90%EB%8F%99%ED%99%94)

<h1 id="03-교재-앤서블로-시작하는-인프라-자동화">03 (교재) 앤서블로 시작하는 인프라 자동화</h1>
<h2 id="vm-을-활용한-실습-환경-준비하기-1-linux환경-with-kvm">VM 을 활용한 실습 환경 준비하기 1. Linux환경 with KVM</h2>
<h3 id="개요">개요</h3>
<ul>
<li><code>Controller Server</code> 1대와 <code>Node Server</code> 3대로 구성되어 있다.</li>
<li>시스템 구성 특징<ul>
<li>개별적으로 4대의 가상머신을 생성하는 것이 아니라 <code>KVM</code> 안에 가상머신들을 설치하는 것이다.</li>
<li><code>Host OS(Windows 10)</code> &gt; <code>VMWare</code> &gt; <code>Ubuntu 24.04.3</code> &gt; <code>KVM</code> &gt; <code>Ansible VM</code> 와 같이 구성해야 한다는 말이다.<h3 id="시스템-구성">시스템 구성</h3>
</li>
</ul>
</li>
<li><code>ansible-server</code><ul>
<li><code>CentOS Stream 9 / 2(CPU) / 4(RAM) / 100GB / 192.168.100.4</code> </li>
</ul>
</li>
<li><code>tnode1-centos</code><ul>
<li><code>CentOS Stream 9 / 2(CPU) / 4(RAM) / 50GB / 192.168.100.5</code></li>
</ul>
</li>
<li><code>tnode2-ubuntu</code><ul>
<li><code>ubuntu 20.04.6 / 2(CPU) / 4(RAM) / 50GB / 192.168.100.6</code></li>
</ul>
</li>
<li><code>tnode3-rhel(rocky)</code><ul>
<li><code>RHEL 8.10 / 2(CPU) / 4(RAM) / 50GB / 192.168.100.7</code> </li>
</ul>
</li>
</ul>
<hr />
<h3 id="작업">작업</h3>
<ul>
<li>Step 1. Ubuntu 24.04.3 압축 파일을 해제한 후 VMWare에서 불러온다.<ul>
<li>로딩 후 <code>1_Updated</code>로 롤백한다</li>
<li>다른 것은 그냥 두고 <code>RAM</code>만 <code>8192</code>로 수정한다.</li>
</ul>
</li>
<li>Step 2. <code>KVM</code> 및 <code>virt-manager</code> 설치<ul>
<li>CPU 가상화 여부 확인</li>
<li>시스템 업데이트 및 업그레이드</li>
<li>KVM 관련 패키지 설치</li>
<li><code>virt-manager</code> 설치</li>
</ul>
</li>
<li>Step 3. <code>GUI Mode</code>에서 <code>virt-manager</code> 실행</li>
</ul>
<h3 id="가상-머신-생성-및-운영체제-설치"><code>가상 머신 생성</code> 및 <code>운영체제 설치</code></h3>
<ul>
<li><p>Step 1. <code>가상 머신 관리자</code> 창에서 <code>새 가상 머신 생성</code> 아이콘을 클릭한다.</p>
</li>
<li><p>Step 2. <code>운영체제를 설치하는 방법 선택</code>에서 <code>로컬 설치 매체(ISO 이미지나 CDROM)</code>을 체크한 후<br /><code>앞으로</code>를 클릭한다.</p>
</li>
<li><p>Step 3. <code>ISO 이미지나 CDROM 설치 미디어 선택</code> 하단에 있는 <code>화살표</code>를 누르면<br /><code>미디어가 탐지되지 않습니다(/dev/sr0)</code>가 보인다.<br />이것은 <code>ISO 이미지</code>를 인식하지 못해서이다.<br />일반적으로 리눅스에서 <code>ISO 파일</code>을 마운트 하면 <code>/dev/sr0</code>로 자동 인식되지만<br />지금은 미디어 삽입을 하지 않았기 때문에 발생하는 정상적인 메시지이다.</p>
</li>
<li><p>Step 4. 현재 진행 중인 상태를 닫고 <code>ISO 이미지 파일</code>을 로딩해야 하므로 <code>취소</code>를 클릭한다.</p>
</li>
<li><p>Step 5. <code>VMWare</code>에서 <code>ansible-server</code>로 사용할 <code>CentOS Stream 9</code> 이미지를 로딩한다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/aabdbeea-32b0-4130-afb6-1517be606200/image.png" /></p>
</li>
<li><p>Step 6. <code>Step 1 ~ Step 3</code>을 다시 진행한다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/701cf78f-ea2f-4259-8207-d46aadae1fb4/image.png" /></p>
</li>
<li><p>Step 7. 같은 방법으로 <code>Node Server 3대</code>를 설치한다.</p>
</li>
<li><p>Step 8. 설치 완료 후 해야 하는 작업</p>
<ul>
<li><code>Kernel Update</code> 진행</li>
<li>네트워크 설정을 통해 IP 설정</li>
<li>비밀번호 변경</li>
<li><code>dnf update</code></li>
<li><code>nmcli</code></li>
</ul>
</li>
</ul>
<ul>
<li>snapshot 지우고 expend 256GB 추가<pre><code class="language-bash">sudo growpart /dev/sda 2
</code></pre>
</li>
</ul>
<p>sudo resize2fs /dev/sda2</p>
<p>samadal@CloudDX:~$ df -h
파일 시스템     크기  사용  가용 사용% 마운트위치
tmpfs           790M  1.8M  788M    1% /run
/dev/sda2       252G   26G  217G   11% /
tmpfs           3.9G     0  3.9G    0% /dev/shm
tmpfs           5.0M     0  5.0M    0% /run/lock
tmpfs           3.9G     0  3.9G    0% /run/qemu
tmpfs           790M   92K  790M    1% /run/user/120
tmpfs           790M   80K  790M    1% /run/user/1000</p>
<pre><code>
---
## VM 을 활용한 실습 환경 준비하기 2. Windows 환경 with Oracle VirtualBox


### 시스템 구성 
- `ansible-server`
  - `CentOS Stream 9 / 2(CPU) / 4(RAM) / 100GB / 192.168.100.4` 
- `tnode1-centos`
  - `CentOS Stream 9 / 2(CPU) / 4(RAM) / 50GB / 192.168.100.5`
- `tnode2-ubuntu`
  - `ubuntu 20.04.6 / 2(CPU) / 4(RAM) / 50GB / 192.168.100.6`
- `tnode3-rhel(rocky)`
  - `RHEL 8.10 / 2(CPU) / 4(RAM) / 50GB / 192.168.100.7` 

- Step 1. `3_VMs` 폴더에 `Ansible` 이라는 이름의 폴더를 생성한다. 
- Step 2. `VirtualBox`를 실행한 후 상단에 있는 `새로 만들기`를 클릭한다.
- Step 3. 다음의 내용으로 입력 후 `완료`를 클릭한다
  - ![](https://velog.velcdn.com/images/kyk02405/post/2a6308e6-b9a4-4cc2-8e81-a45c850d72e7/image.png)

  - `VM Name` -&gt; `ansible_server`
  - `VM Folder` -&gt; `D:\3_VMs\VB\Ansible` 

  - `ISO Image` -&gt; `D:\1_ISO\CentOS-Stream-9-latest-x86_64-dvd1.iso`
  - `Set up unattended guest OS installation`   → `비밀번호(P@ssw0rd)` 두 번 입력
  - `Specify virtual hardware`   → 4096MB / 2CPU
  - `Specify virtual hard disk`   → 100.00GB
- Step 4. 같은 방법으로 `구성 정보`에 따라서 나머지 `시스템 3대`도 구성한다.
- Step 5. 수정 사항
  - 사용하지 않는 장치 제거
    - 각 시스템을 한 개씩 선택한 후 상단에 있는 `설정`을 클릭한다.
    - `Expert`탭을 클릭한 후 하단에 있는 `시스템`을 클릭하고 우측에 있는 `플로피`를 체크 해제한다.
  - `설치 미디어(ISO 파일)` 자동 인식 설정
    - 각 시스템을 한 개씩 선택한 후 상단에 있는 `설정`을 클릭한다.
    - `Export`탭을 클릭한 후 하단에 있는 `저장소`를 클릭하고 우측에 있는 `컨트롤러:IDE` 하단에 있는 `비어 있음`을 클릭한다.
    - 우측에 있는 `Optical Drive` 항목에 있는 `CD-ROM` 아이콘을 클릭한다.
    - 각 시스템에 맞는 `ISO 파일`을 선택한다.
  - `NAT 네트워크` 추가
    - 우측의 `네트워크`를 클릭한 후 `어뎁터 1`에서 `NAT 네트워크`를 선택하면 `확인`이 `비활성 상태`로 나타난다.
    - (주의사항) 왼쪽에 세로로 되어 있는 메뉴 중에서 `다섯 번째 아이콘(네트워크)`를 클릭한다.
    - `NAT 네트워크` 탭을 클릭하면 `기본값`은 비어 있는 상태로 나타난다.
    - 상단에 있는 `만들기`를 클릭한다.
    - 하단에 `NatNetwork` 인터페이스가 추가된 것을 확인한다.
  - 각 시스템별 `NatNetwork` 인터페이스 적용
    - `ansible-server`을 선택한 후 상단에 있는 `설정`을 클릭한다.
      - `Expert`탭을 클릭한 후 하단에 있는 네트워크를 클릭한다.
      - 우측의 있는 `어뎁터 1`에서 `NAT 네트워크`를 선택한다.
      - 이 때 `거부`를 클릭한 후 `모두 허용`으로 변경한 후 `확인`을 클릭한다.
      - 나머지 3개 시스템도 동일하게 작업한다.
- Step 6. 포트포워딩
  - `Ansible`이 설치되는 시스템인 `ansible-server`을 선택한 후 상단에 있는 `설정`을 클릭한다.
  - 아래와 같이 변경 ![](https://velog.velcdn.com/images/kyk02405/post/b3d07c94-7b16-41d0-a6c1-2ceca2a136d7/image.png)
  - 이후 각 가상머신에서 `ping`이 외부로 되는지 확인
  ```bash 
  ping 8.8.8.8</code></pre><hr />
<h2 id="ansible-server에-ansible-설치">ansible-server에 ansible 설치</h2>
<ul>
<li>개요<ul>
<li>기본적으로 외부로의 통신이 되지 않기 때문에 시스템별 IP 설정을 <code>DHCP</code>로 변경 후 설치하면 된다.</li>
</ul>
</li>
<li>설치<pre><code class="language-bash">dnf install epel-release
dnf install ansible</code></pre>
</li>
</ul>
<hr />
<h2 id="32-ansible-기본-사용법">3.2 Ansible 기본 사용법</h2>
<h3 id="321-인벤토리를-이용한-자동화-대상-호스트-설정-p50">3.2.1 인벤토리를 이용한 자동화 대상 호스트 설정 (p50~)</h3>
<h4 id="파일-생성-방법-1-ip를-이용한-인벤토리-파일-생성">파일 생성 방법 1. IP를 이용한 인벤토리 파일 생성</h4>
<ul>
<li><p><code>my-ansible</code> 디렉토리 생성 / p50</p>
<pre><code class="language-bash">  [root@localhost ~]# df -h
  Filesystem           Size  Used Avail Use% Mounted on
  devtmpfs             4.0M     0  4.0M   0% /dev
  tmpfs                1.8G     0  1.8G   0% /dev/shm
  tmpfs                732M  9.3M  722M   2% /run
  /dev/mapper/cs-root   64G  5.3G   59G   9% /
  /dev/vda1            960M  436M  525M  46% /boot
  /dev/mapper/cs-home   32G  255M   31G   1% /home
  tmpfs                366M   92K  366M   1% /run/user/0

  # ‘my-ansible’ 디렉토리 생성
  [root@localhost ~]# mkdir my-ansible
  [root@localhost ~]# 
  [root@localhost ~]# cd my-ansible/
  [root@localhost my-ansible]# 
  [root@localhost my-ansible]# ll
  합계 0

  # IP를 이용한 'invenroty' 파일 생성
  [root@localhost my-ansible]# vi inventory
  [root@localhost my-ansible]# 
  [root@localhost my-ansible]# cat inventory 
  192.168.100.5
  192.168.100.6
  192.168.100.7
</code></pre>
</li>
</ul>
<h4 id="파일-생성-방법-2-호스트명을-이용한-인벤토리-파일-생성">파일 생성 방법 2. 호스트명을 이용한 인벤토리 파일 생성</h4>
<ul>
<li><p>둘 중에 하나만 사용</p>
<pre><code class="language-bash">  root@localhost my-ansible]# vi /etc/hosts
  [root@localhost my-ansible]# 
  [root@localhost my-ansible]# cat /etc/hosts
  127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
  ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
  192.168.100.5   tnode1-centos.exp.com
  192.168.100.6   tnode2-ubuntu.exp.com
  192.168.100.7   tnode3-rhel.exp.com
  [root@localhost my-ansible]# ls -l
  합계 4
  -rw-r--r--. 1 root root 42 12월  1 11:57 inventory
  [root@localhost my-ansible]# 
  [root@localhost my-ansible]# vi inventory 
  [root@localhost my-ansible]# 
  [root@localhost my-ansible]# cp -p /etc/hosts inventory 
  cp: overwrite 'inventory'? y
  [root@localhost my-ansible]# vi inventory 
  [root@localhost my-ansible]# 
  [root@localhost my-ansible]# cat inventory 
  tnode1-centos.exp.com
  tnode2-ubuntu.exp.com
  tnode3-rhel.exp.com
  [root@localhost my-ansible]# 
</code></pre>
</li>
</ul>
<hr />
<h3 id="322-역할에-따른-호스트-그룹-설정">3.2.2 역할에 따른 호스트 그룹 설정</h3>
<h3 id="개요-1">개요</h3>
<ul>
<li>작업을 하다 보면 호스트별로 <code>롤(역할)</code>을 주고 <code>롤</code>별로 특정 작업을 수행해야 하는 경우가 있다.</li>
<li>웹 서비스 구성을 예로 들면 웹 서비스를 구성하기 위해서는 웹 서버와 데이터베이스 서버가 필요하다.</li>
<li>그런데 이런 서버들을 <code>고가용성(High Availability, HA)</code>을 위해 여러 대로 구성할 경우 인벤토리도 유형별로 호스트를 설정할 수 있다.</li>
</ul>
<h3 id="그룹별-호스트-설정">그룹별 호스트 설정</h3>
<ul>
<li><p><code>Ansible Playbook</code> <code>실행(ansible-playbook)</code> 시 그룹별로 작업을 처리할 수 있기 때문에 좀 더 효과적이라고 할 수 있다.</p>
</li>
<li><p>이 경우 그룹명을 <code>대괄호([])</code> 내에 작성하고 해당 그룹에 속하는 호스트명이나 IP를 한 줄에 하나씩 나열한다.</p>
</li>
<li><p>다음의 인벤토리는 두 개의 호스트 그룹인 <code>webservers</code>와 <code>db-servers</code>를 정의한 것이다.</p>
<pre><code class="language-bash">  [webservers]
  webl.example.com
  web2.example com

  [db-servers]
  dbl.example.com
  db2.example com

  [east-datacenter] 
  web1.example.com 
  db01.examole.com

  [west-datacenter] 
  web2.example.com 
  db02.example.com

  [production] 
  web1.example.com 
  web2.example.com 
  db01.example.com 
  db02.example.com

  [development]
  192.0.2.42</code></pre>
</li>
<li><p>중첩 그룹</p>
<ul>
<li><p><code>Ansible Inventory</code>는 호스트 그룹에 기존에 정의한 호스트 그룹을 포함할 수도 있다.</p>
</li>
<li><p>이 경우 호스트 그룹 이름 생성시 <code>:children</code>이라는 접미사를 추가하면 된다.</p>
</li>
<li><p>다음은 <code>webservers</code> 및 <code>db-servers</code> 그룹의 모든 호스트를 포함하는 <code>datacenter</code> 그룹을 생성하는 예이다.</p>
<pre><code class="language-bash">  [webservers]
  web1.example.com
  web2.example.com

  [db-servers]
  db01.example.com
  db02.example.com

  [datacenter:children]
  webservers
  dbservers</code></pre>
</li>
</ul>
</li>
</ul>
<h3 id="323-인벤토리-확인">3.2.3 인벤토리 확인</h3>
<h3 id="ansible-관련-파일-3개">Ansible 관련 파일 3개</h3>
<ul>
<li><p>Ansible의 환경설정</p>
<p>  <code>/etc/ansible/ansible.cfg</code></p>
</li>
<li><p>사용자 지정 인벤토리</p>
<p>  <code>/임의의 디렉토리/inventory/customized_inven.lst</code></p>
</li>
<li><p>기본 인벤토리</p>
<p>  <code>cat /etc/ansible/hosts</code></p>
<h3 id="인벤토리-그룹-구성">인벤토리 그룹 구성</h3>
</li>
<li><p>인벤토리 파일 생성</p>
</li>
</ul>
<pre><code>[root@ansible-server ~]# cd my-ansible/
[root@ansible-server my-ansible]# vi ./inventory
[root@ansible-server my-ansible]# cat inventory

[web]
tnode-1centos.exp.com
tnode2-ubuntu.exp.com

[db]
tnode3-rhel.exp.com

[all:children]
web
db</code></pre><ul>
<li>생성한 인벤토리 확인 및 특정 인벤토리로 지정</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# ansible-inventory -i ./inventory --list
{
    &quot;_meta&quot;: {
        &quot;hostvars&quot;: {}
    },
    &quot;all&quot;: {
        &quot;children&quot;: [
            &quot;ungrouped&quot;,
            &quot;web&quot;,
            &quot;db&quot;
        ]
    },
    &quot;db&quot;: {
        &quot;hosts&quot;: [
            &quot;tnode3-rhel.exp.com&quot;
        ]
    },
    &quot;web&quot;: {
        &quot;hosts&quot;: [
            &quot;tnode-1centos.exp.com&quot;,
            &quot;tnode2-ubuntu.exp.com&quot;
        ]
    }
}
</code></pre><ul>
<li>인벤토리 정보를 트리상태로 확인퍄</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# ansible-inventory -i ./inventory --graph
@all:
  |--@ungrouped:
  |--@web:
  |  |--tnode-1centos.exp.com
  |  |--tnode2-ubuntu.exp.com
  |--@db:
  |  |--tnode3-rhel.exp.com
</code></pre><ul>
<li><code>Ansible</code> 환경 설정 파일을 이용한 인벤토리 구성</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# vi ansible.cfg
[root@ansible-server my-ansible]# cat ansible.cfg
[defaults]
inventory = ./inventory</code></pre><hr />
<h1 id="33-첫-번째-플레이북-작성하기">3.3 첫 번째 플레이북 작성하기</h1>
<h3 id="331-플레이북-환경-설정">3.3.1 플레이북 환경 설정</h3>
<ul>
<li>기본 설정 파일과 사용자 지정 설정 파일의 차이점</li>
</ul>
<pre><code>#이거 하면 Easy-Ansible깔림
git clone https://github.com/naleejang/Easy-Ansible.git

[root@localhost chapter_05.1]# pwd
/root/my-ansible/Easy-Ansible/chapter_05.1
[root@localhost chapter_05.1]# wc /etc/ansible/ansible.cfg
 11  89 614 /etc/ansible/ansible.cfg
[root@localhost chapter_05.1]# wc ./ansible.cfg
 10  23 173 ./ansible.cfg
[root@localhost chapter_05.1]# wc /etc/ansible/ansible.cfg ./ansible.cfg
 11  89 614 /etc/ansible/ansible.cfg
 10  23 173 ./ansible.cfg
 21 112 787 합계
[root@localhost chapter_05.1]# wc -l /etc/ansible/ansible.cfg ./ansible.cfg
 11 /etc/ansible/ansible.cfg
 10 ./ansible.cfg
 21 합계
[root@localhost chapter_05.1]# wc -c /etc/ansible/~~~??????</code></pre><ul>
<li><p>앤서블 플레이북 환경 설정</p>
<pre><code class="language-bash">  [root@localhost my-ansible]# vi ansible.cfg 
  [defaults]
  inventory = ./inventory
  remote_user = root
  ask_pass = false

  [privilege_escalation]
  become = true
  become_method = sudo
  become_user = root
  become_ask_pass = false</code></pre>
</li>
<li><p>앤서블 접근을 위한 SSH 인증 구성</p>
<ul>
<li><p>개요</p>
<ul>
<li>앤서블은 로컬 사용자에게 개인 'SSH 키'가 있거나 관리 호스트에서 원작 사용자임을 인증 가능한 키가 구성된 경우 자동으로 로그인된다.</li>
<li><code>SSH 키</code> 기반의 인증을 구성할 때는 <code>ssh-keygen</code> 명령어를 이용하여 다음과 같이 생성할 수 있다.</li>
<li>또한 <code>ssh-copy-id</code> 명령어를 이용하여 <code>SSH 공개키</code>를 해당 호스트로 복사할 수 있다.</li>
</ul>
</li>
<li><p>ssh 키 생성 및 복사 
<code>ssh-keygen</code> / <code>for i in {5..7}; do ssh-copy-id root@192.168.100.$i; done</code></p>
<pre><code class="language-bash">  [root@localhost chapter_05.1]# pwd
  /root/my-ansible/Easy-Ansible/chapter_05.1
  [root@localhost chapter_05.1]# ssh-keygen

  #우분투는 ssh 패키지 설치, 나머지는 22번 포트 개방
  ufw allow 22/tcp
  ufw reload
  apt install -y openssh-server
  root@tnode2-VirtualBox:~# vi /etc/ssh/sshd_config
       35 PermitRootLogin yes
  service ssh restart</code></pre>
</li>
<li><p>asnsible.cfg 수정</p>
<pre><code class="language-bash">  [root@localhost my-ansible]# cat ansible.cfg 
  [defaults]
  inventory = ./inventory
  remote_user = root
  ask_pass = false

  [privilege_escalation]
  become = true
  become_method = sudo
  become_user = root
  become_ask_pass = false

  [root@localhost my-ansible]# cat inventory 
  [web]
  tnode1-centos.exp.com
  tnode2-ubuntu.exp.com

  [db]
  tnode3-rocky.exp.com

  [all:children]
  web
  db

  [root@localhost my-ansible]# vi /etc/hosts
  192.168.100.5   tnode1-centos.exp.com
  192.168.100.6   tnode2-ubuntu.exp.com
  192.168.100.7   tnode3-rocky.exp.com</code></pre>
</li>
<li><p>ping 테스트</p>
<pre><code class="language-bash">  [root@localhost chapter_05.1]# ansible -m ping web
  tnode2-ubuntu.exp.com | SUCCESS =&gt; {
      &quot;ansible_facts&quot;: {
          &quot;discovered_interpreter_python&quot;: &quot;/usr/bin/python3&quot;
      },
      &quot;changed&quot;: false,
      &quot;ping&quot;: &quot;pong&quot;
  }
  tnode1-centos.exp.com | SUCCESS =&gt; {
      &quot;ansible_facts&quot;: {
          &quot;discovered_interpreter_python&quot;: &quot;/usr/bin/python3&quot;
      },
      &quot;changed&quot;: false,
      &quot;ping&quot;: &quot;pong&quot;
  }</code></pre>
</li>
</ul>
</li>
</ul>
<h3 id="332-플레이북-작성하기">3.3.2 플레이북 작성하기</h3>
<ul>
<li><p>first-playbook.yml 생성</p>
<pre><code class="language-bash">  [root@localhost chapter_05.2]# vi first-playbook.yml 
  ---
  - hosts: all
    tasks:
      - name: Print message
        debug:
          msg: Hello Ansible World
</code></pre>
</li>
<li><p>플레이북 문법 확인</p>
<pre><code class="language-bash">  # 에러일 경우
  [root@localhost chapter_05.2]# ansible-playbook --syntax-check first-playbook-with-error.yml 
  ERROR! conflicting action statements: debug, msg

  The error appears to be in '/root/my-ansible/Easy-Ansible/chapter_05.2/first-playbook-with-error.yml': line 4, column 7, but may
  be elsewhere in the file depending on the exact syntax problem.

  The offending line appears to be:

    tasks:
      - name: Print message
        ^ here

  # 정상일 경우  
  [root@localhost chapter_05.2]# ansible-playbook --syntax-check first-playbook.yml 

  playbook: first-playbook.yml</code></pre>
</li>
<li><p>첫 번째 플레이북 실행하기 <code>ansible-playbook &lt;실행파일.yml&gt;</code></p>
<pre><code class="language-bash">  [root@localhost my-ansible]# ansible-playbook first-playbook.yml

  PLAY [all] *************************************************************************************

  TASK [Gathering Facts] *************************************************************************
  ok: [tnode3-rocky.exp.com]
  ok: [tnode2-ubuntu.exp.com]
  ok: [tnode1-centos.exp.com]

  TASK [Print message] ***************************************************************************
  ok: [tnode1-centos.exp.com] =&gt; {
      &quot;msg&quot;: &quot;Hello Ansible World&quot;
  }
  ok: [tnode2-ubuntu.exp.com] =&gt; {
      &quot;msg&quot;: &quot;Hello Ansible World&quot;
  }
  ok: [tnode3-rocky.exp.com] =&gt; {
      &quot;msg&quot;: &quot;Hello Ansible World&quot;
  }

  PLAY RECAP *************************************************************************************
  tnode1-centos.exp.com      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
  tnode2-ubuntu.exp.com      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
  tnode3-rocky.exp.com       : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0</code></pre>
</li>
<li><p>플레이북 실행 점검하기 <code>ansible-playbook --check &lt;점검할yml&gt;</code></p>
<pre><code class="language-bash">  #한 줄로 하면 ansible all -m service -a &quot;name=sshd state=restarted&quot;
  cat restart-service.yml
  ---
  - hosts: all
    tasks:
      - name: Restart sshd service
        ansible.builtin.service:   #service는 모듈, builtin는 Class, ansible은 패키지
          name: sshd
          state: restarted

  #점검하기  
  [root@localhost my-ansible]# ansible-playbook --check restart-service.yml

  PLAY [all] *************************************************************************************

  TASK [Gathering Facts] *************************************************************************
  ok: [tnode2-ubuntu.exp.com]
  ok: [tnode3-rocky.exp.com]
  ok: [tnode1-centos.exp.com]

  TASK [Restart sshd service] ********************************************************************
  changed: [tnode2-ubuntu.exp.com]
  changed: [tnode1-centos.exp.com]
  changed: [tnode3-rocky.exp.com]

  PLAY RECAP *************************************************************************************
  tnode1-centos.exp.com      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
  tnode2-ubuntu.exp.com      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
  tnode3-rocky.exp.com       : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

  #실행하기
  [root@localhost my-ansible]# ansible-playbook restart-service.yml

  PLAY [all] *************************************************************************************

  TASK [Gathering Facts] *************************************************************************
  ok: [tnode2-ubuntu.exp.com]
  ok: [tnode1-centos.exp.com]
  ok: [tnode3-rocky.exp.com]

  TASK [Restart sshd service] ********************************************************************
  changed: [tnode2-ubuntu.exp.com]
  changed: [tnode3-rocky.exp.com]
  changed: [tnode1-centos.exp.com]

  PLAY RECAP *************************************************************************************
  tnode1-centos.exp.com      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
  tnode2-ubuntu.exp.com      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
  tnode3-rocky.exp.com       : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

  #tnode1의 로그에서 sshd가 재시작한 것을 확인할 수 있다.
  root@localhost ~]# vi /var/log/messages
  #Dec  1 17:38:03 localhost python3[5333]: ansible-ansible.legacy.systemd Invoked with name=sshd state=restarted daemon_reload=False daemon_reexec=False scope=system no_block=False enabled=None force=None masked=None
  Dec  1 17:38:03 localhost systemd[1]: Stopping OpenSSH server daemon...
  Dec  1 17:38:03 localhost systemd[1]: sshd.service: Deactivated successfully.
  Dec  1 17:38:03 localhost systemd[1]: Stopped OpenSSH server daemon.
  Dec  1 17:38:03 localhost systemd[1]: Stopped target sshd-keygen.target.
  Dec  1 17:38:03 localhost systemd[1]: Stopping sshd-keygen.target...</code></pre>
</li>
</ul>
<h1 id="34-변수와-팩트-사용하기">3.4 변수와 팩트 사용하기</h1>
<h2 id="341-변수의-종류와-사용법-rootmy-ansibleeasy-ansiblechapter_061">3.4.1 변수의 종류와 사용법 (/root/my-ansible/Easy-Ansible/chapter_06.1)</h2>
<h3 id="그룹-변수">그룹 변수</h3>
<ul>
<li>개요<ul>
<li>인벤토리에 정의되며, 모든 그름에서 적용되는 변수</li>
<li>인벤토리에 정의된 호스트 그룹에 적용한 변수를 사용한다.</li>
</ul>
</li>
<li>Step 1. <code>inventory</code> 확인</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# cat inventory
[web]
tnode1-centos.exp.com 
tnode2-ubuntu.exp.com 

[db]
tnode3-rhel.exp.com 

[all:children]
web
db

[all:vars]
user=ansible  -&gt;  '변수 = 값'</code></pre><ul>
<li>Step 2. 사용자 생성</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# cat create-user.yml
---

- hosts: all
  tasks:
  - name: Create User {{ user }}  -&gt; 'Playbook'에서 불러와서 사용하기 위해서는 '{{}}'를 사용해야 한다.
    ansible.builtin.user:         -&gt; (매우 중요) 변수 양 옆에는 반드시 '한 칸씩' 띄워야 한다.
      name: &quot;{{ user }}&quot;
      state: present              -&gt; 'Playbook' 실행 시 'TASK'에 출력한다.
</code></pre><ul>
<li>Step 3. <code>Playbook</code> 실행</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# ansible-playbook create-user.yml

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [tnode2-ubuntu.exp.com]
ok: [tnode1-centos.exp.com]
ok: [tnode3-rhel.exp.com]

TASK [Create User ansible]  -&gt; 에서 변수의 값인 'ansible'이라는 문자열을 확인한다. *****************************************************
changed: [tnode2-ubuntu.exp.com]
changed: [tnode3-rhel.exp.com]
changed: [tnode1-centos.exp.com]

PLAY RECAP *********************************************************************
tnode1-centos.exp.com      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
tnode2-ubuntu.exp.com      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
tnode3-rhel.exp.com        : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0</code></pre><ul>
<li>Step 4. 실제 생성한 사용자 확인</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# ansible all -m shell -a &quot;cat /etc/passwd | grep ansible; ls -l /home&quot;
tnode2-ubuntu.exp.com | CHANGED | rc=0 &gt;&gt;
ansible:x:1001:1001::/home/ansible:/bin/sh
합계 8
drwxr-xr-x  2 ansible       ansible       4096 12월  2 09:54 ansible
drwxr-xr-x 14 tnode2-ubuntu tnode2-ubuntu 4096 12월  1 12:18 tnode2-ubuntu
tnode3-rhel.exp.com | CHANGED | rc=0 &gt;&gt;
ansible:x:1001:1001::/home/ansible:/bin/bash
합계 8
drwx------. 3 ansible     ansible     4096 12월  2 09:54 ansible
drwx------. 3 tnode3-rhel tnode3-rhel 4096 12월  1 16:35 tnode3-rhel
tnode1-centos.exp.com | CHANGED | rc=0 &gt;&gt;
ansible:x:1001:1001::/home/ansible:/bin/bash
합계 8
drwx------. 3 ansible       ansible       4096 12월  2 09:54 ansible
drwx------. 3 tnode1-centos tnode1-centos 4096 12월  1 11:20 tnode1-centos</code></pre><h3 id="호스트-변수">호스트 변수</h3>
<ul>
<li>개요<ul>
<li>변수를 해당 호스트에서만 사용한다.</li>
<li>인벤토리에 정의되며, 특정 호스트에만 적용되는 변수<ul>
<li>앤서블팩트<ul>
<li>플레이북 실행 시 자동으로 호스트에서 수집한 변수</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>Step 1. <code>db 그룹</code>에 변수 선언과 함께 초기값 대입</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# cp -p inventory inventory.samadal  -&gt;  백업용
[root@ansible-server chapter_06.1]# vi inventory
[root@ansible-server chapter_06.1]# cat inventory
[web]
tnode1-centos.exp.com 
tnode2-ubuntu.exp.com 

[db]
tnode3-rhel.exp.com user=ansible1 

[all:children]
web
db

[all:vars]
user=ansible
</code></pre><ul>
<li>Step 2. <code>hosts’를</code>all<code>에서</code>db` 호스트로 변경</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# vi create-user1.yml 
[root@ansible-server chapter_06.1]# cat create-user1.yml 
---

- hosts: db
  tasks:
  - name: Create User {{ user }}
    ansible.builtin.user:
      name: &quot;{{ user }}&quot;
      state: present</code></pre><ul>
<li>Step 3. <code>Playbook</code> 실행</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# ansible-playbook create-user1.yml

PLAY [db] **********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [tnode3-rhel.exp.com]

TASK [Create User ansible1] ****************************************************
changed: [tnode3-rhel.exp.com]

PLAY RECAP *********************************************************************
tnode3-rhel.exp.com        : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0</code></pre><ul>
<li>Step 4. 실제 생성한 사용자 확인</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# ansible all -m shell -a &quot;cat /etc/passwd | grep ansible; ls -l /home&quot;
tnode2-ubuntu.exp.com | CHANGED | rc=0 &gt;&gt;
ansible:x:1001:1001::/home/ansible:/bin/sh
합계 8
drwxr-xr-x  2 ansible       ansible       4096 12월  2 09:54 ansible
drwxr-xr-x 14 tnode2-ubuntu tnode2-ubuntu 4096 12월  1 12:18 tnode2-ubuntu
tnode3-rhel.exp.com | CHANGED | rc=0 &gt;&gt;
ansible:x:1001:1001::/home/ansible:/bin/bash
ansible1:x:1002:1002::/home/ansible1:/bin/bash
합계 12
drwx------. 3 ansible     ansible     4096 12월  2 09:54 ansible
drwx------. 3 ansible1    ansible1    4096 12월  2 10:20 ansible1
drwx------. 3 tnode3-rhel tnode3-rhel 4096 12월  1 16:35 tnode3-rhel
tnode1-centos.exp.com | CHANGED | rc=0 &gt;&gt;
ansible:x:1001:1001::/home/ansible:/bin/bash
합계 8
drwx------. 3 ansible       ansible       4096 12월  2 09:54 ansible
drwx------. 3 tnode1-centos tnode1-centos 4096 12월  1 11:20 tnode1-centos</code></pre><h3 id="플레이-변수">플레이 변수</h3>
<ul>
<li>개요<ul>
<li><code>Playbook</code> 내에서만 선언되는 변수를 말한다.</li>
<li>플레이북실행 시 실행 결과를 저장한 변수</li>
</ul>
</li>
<li>Step 1. <code>YAML</code> 파일 수정</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# vi create-user3.yml 
[root@ansible-server chapter_06.1]# cat create-user3.yml 
---

- hosts: all
  vars:
    user: ansible2

  tasks:
  - name: Create User {{ user }}
    ansible.builtin.user:
      name: &quot;{{ user }}&quot;
      state: present</code></pre><ul>
<li>Step 2. <code>Playbook</code> 실행</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# ansible-playbook create-user3.yml

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [tnode2-ubuntu.exp.com]
ok: [tnode1-centos.exp.com]
ok: [tnode3-rhel.exp.com]

TASK [Create User ansible2] ****************************************************
changed: [tnode2-ubuntu.exp.com]
changed: [tnode3-rhel.exp.com]
changed: [tnode1-centos.exp.com]

PLAY RECAP *********************************************************************
tnode1-centos.exp.com      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
tnode2-ubuntu.exp.com      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
tnode3-rhel.exp.com        : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  </code></pre><ul>
<li>Step 3. 플레이 변수를 별도의 파일로 분리</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# vi vars/users.yml
[root@ansible-server chapter_06.1]# cat vars/users.yml 
user: ansible4
[root@ansible-server chapter_06.1]# ls -l vars/
합계 4
-rw-r--r--. 1 root root 15 12월  1 15:59 users.yml
[root@ansible-server chapter_06.1]# vi create-user4.yml
[root@ansible-server chapter_06.1]# cat create-user4.yml 
---

- hosts: all
  vars_files:
    - vars/users.yml

  tasks:
  - name: Create User {{ user }}
    ansible.builtin.user:
      name: &quot;{{ user }}&quot;
      state: present</code></pre><ul>
<li>Step 4. <code>Playbook</code> 실행</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# ansible-playbook create-user4.yml

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [tnode2-ubuntu.exp.com]
ok: [tnode1-centos.exp.com]
ok: [tnode3-rhel.exp.com]

TASK [Create User ansible4] ****************************************************
changed: [tnode2-ubuntu.exp.com]
changed: [tnode3-rhel.exp.com]
changed: [tnode1-centos.exp.com]

PLAY RECAP *********************************************************************
tnode1-centos.exp.com      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
tnode2-ubuntu.exp.com      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
tnode3-rhel.exp.com        : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 </code></pre><ul>
<li>Step 5. 실제 생성한 사용자 확인</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# ansible all -m shell -a &quot;cat /etc/passwd | grep ansible4&quot;
tnode2-ubuntu.exp.com | CHANGED | rc=0 &gt;&gt;
ansible4:x:1003:1003::/home/ansible4:/bin/sh
tnode3-rhel.exp.com | CHANGED | rc=0 &gt;&gt;
ansible4:x:1004:1004::/home/ansible4:/bin/bash
tnode1-centos.exp.com | CHANGED | rc=0 &gt;&gt;
ansible4:x:1003:1003::/home/ansible4:/bin/bash</code></pre><h3 id="추가-변수">추가 변수</h3>
<ul>
<li>개요<ul>
<li>외부에서 <code>ansible-playbook</code>을 실행할 때 파라미터와 함께 넘겨주는 변수를 말한다.</li>
<li>지금까지 알아본 변수들 중에서 우선 순위가 가장 높다.</li>
<li>플레이북 실행 시 함께 선언되는 변수</li>
</ul>
</li>
<li>Step 1. <code>Playbook</code> 실행</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# ansible-playbook -e user=ansible5 create-user4.yml

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [tnode2-ubuntu.exp.com]
ok: [tnode1-centos.exp.com]
ok: [tnode3-rhel.exp.com]

TASK [Create User ansible5] ****************************************************
changed: [tnode2-ubuntu.exp.com]
changed: [tnode3-rhel.exp.com]
changed: [tnode1-centos.exp.com]

PLAY RECAP *********************************************************************
tnode1-centos.exp.com      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
tnode2-ubuntu.exp.com      : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  </code></pre><ul>
<li>Step 2. 실제 생성한 사용자 확인</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# ansible all -m shell -a &quot;cat /etc/passwd | grep ansible5&quot;
tnode2-ubuntu.exp.com | CHANGED | rc=0 &gt;&gt;
ansible5:x:1004:1004::/home/ansible5:/bin/sh
tnode3-rhel.exp.com | CHANGED | rc=0 &gt;&gt;
ansible5:x:1005:1005::/home/ansible5:/bin/bash
tnode1-centos.exp.com | CHANGED | rc=0 &gt;&gt;
ansible5:x:1004:1004::/home/ansible5:/bin/bash</code></pre><h3 id="작업-변수">작업 변수</h3>
<ul>
<li>개요<ul>
<li><code>Playbook</code> <code>TASK</code>의 수행 결과를 저장한다.</li>
<li>특정 작업 수행한 후 그 결과를 후속 작업에서 사용할 때 주로 사용된다.</li>
</ul>
</li>
<li>Step 1. <code>YAML</code> 파일 수정</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# vi create-user6.yml
[root@ansible-server chapter_06.1]# cat create-user6.yml
---

- hosts: db
  tasks:
  - name: Create User {{ user }}
    ansible.builtin.user:
      name: &quot;{{ user }}&quot;
      state: present
    register: result

  - ansible.builtin.debug:
      var: result
</code></pre><ul>
<li>Step 2. <code>Playbook</code> 실행</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# ansible-playbook -e user=ansible6 create-user6.yml

PLAY [db] **********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [tnode3-rhel.exp.com]

TASK [Create User ansible6] ****************************************************
changed: [tnode3-rhel.exp.com]

TASK [ansible.builtin.debug] ***************************************************
ok: [tnode3-rhel.exp.com] =&gt; {
    &quot;result&quot;: {
        &quot;changed&quot;: true,
        &quot;comment&quot;: &quot;&quot;,
        &quot;create_home&quot;: true,
        &quot;failed&quot;: false,
        &quot;group&quot;: 1006,
        &quot;home&quot;: &quot;/home/ansible6&quot;,
        &quot;name&quot;: &quot;ansible6&quot;,
        &quot;shell&quot;: &quot;/bin/bash&quot;,
        &quot;state&quot;: &quot;present&quot;,
        &quot;system&quot;: false,
        &quot;uid&quot;: 1006
    }
}

PLAY RECAP *********************************************************************
tnode3-rhel.exp.com        : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
</code></pre><ul>
<li>Step 3. 실제 생성한 사용자 확인</li>
</ul>
<pre><code>[root@ansible-server chapter_06.1]# ansible all -m shell -a &quot;cat /etc/passwd | grep ansible6&quot;</code></pre><h2 id="342-패스워드를-안전하게-보관할-수-있는-ansible-vault">3.4.2 ‘패스워드’를 안전하게 보관할 수 있는 ‘Ansible Vault’</h2>
<h3 id="암호화-된-파일-만들기">암호화 된 파일 만들기</h3>
<ul>
<li>Step 1. <code>ansible-vault</code>라는 명령어와 함께 생성하려는 플레이북 파일명을 입력</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# ansible-vault create mysecret.yml
New Vault password: P@ssw0rd!
Confirm New Vault password: P@ssw0rd!

(vi 에디터 창이 열리면 다음과 같이 입력한 후 !wq를 사용하여 저장)

user: ansible
password: P@ssw0rd!</code></pre><ul>
<li>Step 2. 암호화된 파일 확인</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# ll mysecret.yml
-rw-------. 1 root root 484 12월  2 11:51 mysecret.yml
[root@ansible-server my-ansible]# cat mysecret.yml
$ANSIBLE_VAULT;1.1;AES256
39613133373362343036653939356137386263333131363461643837623132383438323261373266
3834633530363665393933653938353565353563633232340a346338343730323538626666633439
33356164333933646337383962366130396466353661393962346463656433383732666534333339
3437613262376433320a346437306662386130353664306139646632376132653165343638393562
63633365336436333834396636343535323663623664373266363634653838343834663131356439
3165663433393766643639386535663138626532613933323435</code></pre><ul>
<li>Step 3. <code>ansible-vault view</code> 명령어를 사용하여 암호화된 파일 확인</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# ansible-vault view mysecret.yml
Vault password: 
user: ansible
password: P@ssw0rd!</code></pre><h3 id="파일을-이용한-암호화-파일-만들기">파일을 이용한 암호화 파일 만들기</h3>
<ul>
<li>vault-pass 라는 파일을 생성</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# vi vault-pass
[root@ansible-server my-ansible]# cat vault-pass 
P@ssw0rd!</code></pre><ul>
<li>옵션 <code>--vault-pass-file</code>을 사용</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# ansible-vault create --vault-pass-file ./vault-pass mysecret1.yml

(vi 에디터 창이 열리면 다음과 같이 입력한 후 !wq를 사용하여 저장)

user: ansible
password: P@ssw0rd!</code></pre><ul>
<li>파일 내용 확인</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# ll mysecret1.yml
-rw-------. 1 root root 484 12월  2 12:03 mysecret1.yml
[root@ansible-server my-ansible]# ansible-vault view --vault-pass-file ./vault-pass mysecret1.yml 
user: ansible
password: P@ssw0rd!
</code></pre><h3 id="기존-파일-암호화">기존 파일 암호화</h3>
<ul>
<li><code>ansible-vault encrypt</code> 명령어를 이용하여 파일 암호화 하기</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# ansible-vault encrypt create-user.yml
New Vault password: P@ssw0rd!
Confirm New Vault password: P@ssw0rd!
Encryption successful</code></pre><ul>
<li>암호화된 파일의 접근 권한 확인 (소유자만 읽고 쓰기 가능)</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# ll create-user.yml
-rw-------. 1 root root 873 12월  2 12:11 create-user.yml</code></pre><ul>
<li>암호화된 파일 복호화</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# ansible-vault decrypt create-user.yml --output=create-user-decrypted.yml
Vault password: P@ssw0rd!
Decryption successful</code></pre><ul>
<li>복호화된 파일 확인</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# ll create-user*
-rw-------. 1 root root 132 12월  2 12:14 create-user-decrypted.yml
-rw-------. 1 root root 873 12월  2 12:11 create-user.yml
[root@ansible-server my-ansible]# cat create-user-decrypted.yml
---

- hosts: all
  tasks:
  - name: Create User {{ user }}
    ansible.builtin.user:
      name: &quot;{{ user }}&quot;
      state: present</code></pre><h3 id="암호화-된-파일의-패스워드-변경">암호화 된 파일의 패스워드 변경</h3>
<ul>
<li><code>ansible-vault rekey</code> 명령어를 사용하여 패스워드 변경</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# ansible-vault rekey mysecret.yml
Vault password: P@ssw0rd!
New Vault password: NewP@ssw0rd!
Confirm New Vault password: NewP@ssw0rd!
Rekey successful</code></pre><ul>
<li>패스워드를 입력해놓은 파일을 이용해 패스워드 변경</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# vi vault-pass
[root@ansible-server my-ansible]# cat vault-pass 
P@ssw0rd!
[root@ansible-server my-ansible]# ansible-vault rekey --new-vault-password-file=./vault-pass mysecret.yml
Vault password: NewP@ssw0rd!
Rekey successful
</code></pre><h3 id="암호화-된-플레이북-실행">암호화 된 플레이북 실행</h3>
<ul>
<li><code>YAML</code>파일을 vars 디렉토리로 이동</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# mv ./mysecret.yml vars/
[root@ansible-server my-ansible]# ansible-vault view vars/mysecret.yml
Vault password: P@ssw0rd!
user: ansible
password: P@ssw0rd!</code></pre><ul>
<li><code>create-user.yml</code> 파일 수정</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# vi create-user.yml
[root@ansible-server my-ansible]# cat create-user.yml
---

- hosts: db
  vars_files:
    - vars/mysecret.yml

  tasks:
  - name: Create User {{ user }}
    ansible.builtin.user:
      name: &quot;{{ user }}&quot;
      state: present
</code></pre><ul>
<li>암호화된 플레이북 실행</li>
</ul>
<pre><code>[root@ansible-server my-ansible]# ansible-playbook create-user.yml
ERROR! Attempting to decrypt but no vault secrets found
[root@ansible-server my-ansible]# ansible-playbook --vault-password-file=./vault-pass create-user.yml

PLAY [db] **********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [tnode3-rhel.exp.com]

TASK [Create User ansible] *****************************************************
ok: [tnode3-rhel.exp.com]

PLAY RECAP *********************************************************************
tnode3-rhel.exp.com        : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
</code></pre><h2 id="343-자동-예약-변수-facts">3.4.3 자동 예약 변수 <code>Facts</code></h2>
<h3 id="개요-2">개요</h3>
<ul>
<li><code>Ansible</code>이 <code>관리 호스트</code>(Controller Server)에서 자동으로 검색한 변수를 말한다.</li>
<li><code>관리 호스트</code>에서 <code>수집한 값</code>에 의존하는 정보들이 포함되어 있다.</li>
</ul>
<hr />
<h3 id="facts-1-facts-사용하기">Facts 1. <code>Facts</code> 사용하기</h3>
<ul>
<li><p><strong>Step 1. 코드</strong></p>
</li>
<li><p><strong>Step 2. <code>Ansible Playbook</code>을 이용해서 파일 실행</strong></p>
<ul>
<li><code>db</code>시스템의 모든 정보를 출력</li>
</ul>
</li>
<li><p><strong>Step 3. 특정 값만 추출해서 사용</strong></p>
</li>
</ul>
<hr />
<h3 id="fact-2-변수로-사용할-수-있는-ansible-facts">Fact 2. 변수로 사용할 수 있는 <code>Ansible Facts</code></h3>
<ul>
<li><code>p92 ~ 93</code> 에 있는 표를 참고한다.</li>
</ul>
<hr />
<h3 id="fact-3-facts-수집-끄기">Fact 3. <code>Facts</code> 수집 끄기</h3>
<ul>
<li><p><strong>개요</strong></p>
<ul>
<li><code>Facts</code> 수집을 위해서 해당 호스트에 특정 패키지를 설치해야 하는 경우가 있다.</li>
<li>그러나 패키지 오류 등으로 인해 설치가 안되는 경우에는 <code>Facts</code> 수집도 할 수가 없다.</li>
<li>이와 같은 이유 등으로 호스트에 과부하가 걸리는 경우가 있는데 이런 경우에는 <code>Facts</code> 수집 기능을 <code>비활성화</code> 하는 것이 좋다.</li>
</ul>
</li>
<li><p><strong>Step 1. 파일 수정</strong></p>
</li>
<li><p><strong>Step 2. <code>Ansible Playbook</code>을 이용해서 파일 실행</strong></p>
<ul>
<li>TASK [Print all facts] *** <code>Facts</code>를 수집하지 않았기 때문에 <code>Facts</code>에서 수집한 변수를
사용하려고 하면 오류가 발생한다.</li>
</ul>
</li>
<li><p><strong>Step 3. <code>Ansible Playbook</code>에 <code>Facts</code> 수집 설정</strong></p>
</li>
<li><p><strong>Step 4. <code>Ansible Playbook</code> 실행</strong></p>
</li>
</ul>
<hr />
<h3 id="fact-4-사용자-지정-fact-만들기">Fact 4. 사용자 지정 <code>Fact</code> 만들기</h3>
<ul>
<li><p><strong>개요</strong></p>
<ul>
<li><code>사용자 지정 Facts</code>는 <code>관리 호스트</code>의 로컬에 있는 <code>/etc/ansible/facts.d/</code> 디렉터리에 <code>*.fact</code>로 저장되어야만 <code>Ansible</code>이 <code>Playbook</code>을 실행할 때 자동으로 <code>Facts</code>를 수집할 수가 있다.</li>
</ul>
</li>
<li><p><strong>Step 1. <code>/etc/ansible/facts.d/</code> 디렉터리를 생성하고 <code>사용자 지정 Facts</code> 파일 생성</strong></p>
</li>
<li><p><strong>Step 2. 파일 생성</strong></p>
</li>
<li><p><strong>Step 3.</strong></p>
</li>
<li><p><strong>Step 4.</strong></p>
</li>
</ul>
<hr />
<h1 id="35-반복문과-조건문을-이용한-제어문">3.5 반복문과 조건문을 이용한 제어문</h1>