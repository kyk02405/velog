# Cloud DX - 52 Ansible로 시작하는 인프라 자동화

- 📅 Published: Fri, 28 Nov 2025 08:41:42 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-52-Ansible%EB%A1%9C-%EC%8B%9C%EC%9E%91%ED%95%98%EB%8A%94-%EC%9D%B8%ED%94%84%EB%9D%BC-%EC%9E%90%EB%8F%99%ED%99%94)

<h1 id="03-교재-앤서블로-시작하는-인프라-자동화">03 (교재) 앤서블로 시작하는 인프라 자동화</h1>
<h2 id="31-vm을-활용한-실습-환경-준비하기">3.1 VM을 활용한 실습 환경 준비하기</h2>
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
<li><code>ubuntu 24.04.3 / 2(CPU) / 4(RAM) / 50GB / 192.168.100.6</code></li>
</ul>
</li>
<li><code>tnode3-rhel</code><ul>
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
<li>Step 2. ‘KVM’ 및 ‘virt-manager’ 설치<ul>
<li>CPU 가상화 여부 확인</li>
<li>시스템 업데이트 및 업그레이드</li>
<li>KVM 관련 패키지 설치</li>
<li>‘virt-manager’ 설치</li>
</ul>
</li>
<li>Step 3. ‘GUI Mode’에서 ‘virt-manager’ 실행</li>
</ul>
<h3 id="가상-머신-생성-및-운영체제-설치">‘가상 머신 생성’ 및 ‘운영체제 설치’</h3>
<ul>
<li><p>Step 1. '가상 머신 관리자' 창에서 '새 가상 머신 생성' 아이콘을 클릭한다.</p>
</li>
<li><p>Step 2. '운영체제를 설치하는 방법 선택'에서 '로컬 설치 매체(ISO 이미지나 CDROM)'를 체크한 후
'앞으로'를 클릭한다.</p>
</li>
<li><p>Step 3. 'ISO 이미지나 CDROM 설치 미디어 선택' 하단에 있는 '화살표'를 누르면
'미디어가 탐지되지 않습니다(/dev/sr0)'가 보인다. 이것은 'ISO 이미지'를 인식하지 못해서이다.
일반적으로 리눅스에서 'ISO 파일'을 마운트 하면 '/dev/sr0'로 자동 인식이 되는데 미디어를
삽입하지 않았기 때문에 나타나는 당연한 결과이다.</p>
</li>
<li><p>Step 4. 현재 진행중인 상태를 닫고 'ISO 이미지 파일'을 로딩해야 하기 때문에 '취소'를 클릭한다.</p>
</li>
<li><p>Step 5. 'VMWare'에서 'ansible-server'로 사용할 'CentOS CentOS Stream 9' 이미지를 로딩한다.</p>
<p>  <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/aabdbeea-32b0-4130-afb6-1517be606200/image.png" /></p>
</li>
</ul>
<ul>
<li><p>Step 6. ‘Step 1. ~ Step 3.’ 까지 다시 진행한다</p>
<p>  <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/701cf78f-ea2f-4259-8207-d46aadae1fb4/image.png" /></p>
</li>
</ul>
<ul>
<li><p>Step 7. 같은 방법으로 ‘Node Server 3대’를 설치한다.</p>
</li>
<li><p>Step 8. 설치 완료 후 해야 하는 작업</p>
<ul>
<li>‘Kernel Update’를 진행한다.</li>
<li>네트워크 설정을 통해 IP를 설정한다.</li>
<li>비밀번호도 편하게 변경한다.</li>
<li>dnf update</li>
<li>nmcli</li>
</ul>
</li>
<li><p>snapshot 지우고 expend 256GB 추가</p>
<pre><code class="language-bash">sudo growpart /dev/sda 2
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
<p>```</p>
<h2 id="vm-을-활용한-실습-환경-준비하기-2-windows-환경">‘VM’ 을 활용한 실습 환경 준비하기 2. Windows 환경</h2>
<h3 id="kvm-및-virt-manager-설치">KVM 및 virt-manager 설치</h3>