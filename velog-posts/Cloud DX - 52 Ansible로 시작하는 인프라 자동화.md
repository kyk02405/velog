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
<li><p>‘my-ansible’ 디렉토리 생성 / p50</p>
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
<li>작업을 하다 보면 호스트별로 '롤(역할)'을 주고 '롤'별로 특정 작업을 수행해야 하는 경우가 있다.</li>
<li>웹 서비스 구성을 예로 들면 웹 서비스를 구성하기 위해서는 웹 서버와 데이터베이스 서버가 필요하다.</li>
<li>그런데 이런 서버들을 '고가용성(High Availability, HA)'을 위해 여러 대로 구성할 경우 인벤토리도 유형별로 호스트를 설정할 수 있다.</li>
</ul>
<h3 id="그룹별-호스트-설정">그룹별 호스트 설정</h3>
<ul>
<li><p>'Ansible Playbook' '실행(ansible-playbook)' 시 그룹별로 작업을 처리할 수 있기 때문에 좀 더 효과적이라고 할 수 있다.</p>
</li>
<li><p>이 경우 그룹명을 '대괄호([])' 내에 작성하고 해당 그룹에 속하는 호스트명이나 IP를 한 줄에 하나씩 나열한다.</p>
</li>
<li><p>다음의 인벤토리는 두 개의 호스트 그룹인 'webservers'와 'db-servers'를 정의한 것이다.</p>
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
<li><p>'Ansible Inventory'는 호스트 그룹에 기존에 정의한 호스트 그룹을 포함할 수도 있다.</p>
</li>
<li><p>이 경우 호스트 그룹 이름 생성시 ':children'이라는 접미사를 추가하면 된다.</p>
</li>
<li><p>다음은 'webservers' 및 'db-servers' 그룹의 모든 호스트를 포함하는 'datacenter' 그룹을 생성하는 예이다.</p>
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
<h2 id="33-첫-번째-플레이북-작성하기">3.3 첫 번째 플레이북 작성하기</h2>
<h3 id="331-기본-설정-파일과-사용자-지정-설정-파일의-차이점">3.3.1 기본 설정 파일과 사용자 지정 설정 파일의 차이점</h3>
<h3 id="앤서블-플레이북-환경-설정">앤서블 플레이북 환경 설정</h3>
<h3 id="앤서블-접근을-위한-ssh-인증-구성">앤서블 접근을 위한 SSH 인증 구성</h3>
<ul>
<li>개요<ul>
<li>앤서블은 로컬 사용자에게 개인 <code>SSH 키</code>가 있거나 관리 호스트에서 원작 사용자임을 인증 가능한 키가 구성된 경우 자동으로 로그인된다.</li>
</ul>
</li>
</ul>
<p><code>SSH 키</code> 기반의 인증을 구성할 때는 <code>ssh-keygen</code> 명령어를 이용하여 다음과 같이 생성할 수 있다.<br />또한 <code>ssh-copy-id</code> 명령어를 이용하여 <code>SSH 공개키</code>를 해당 호스트로 복사할 수 있다.</p>
<hr />
<h4 id="ssh-key-설치">SSH Key 설치</h4>
<ul>
<li><code>키 생성</code>(Controller Server)<pre><code class="language-bash">[root@localhost yum.repos.d]# ssh-keygen
[root@localhost chapter_05.1]# for i in {5..7}; do ssh-copy-id root@192.168.100.$i; done</code></pre>
</li>
</ul>
<h3 id="332-첫-번째-플레이북-작성하기">3.3.2 첫 번째 플레이북 작성하기</h3>
<pre><code class="language-bash">/home/samadal/my-ansible/Easy-Ansible/chapter_05.2</code></pre>