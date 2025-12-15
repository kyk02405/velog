# Cloud DX - 56 Kubernetes

- 📅 Published: Wed, 10 Dec 2025 09:11:32 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-56-Kubernetes)

<h1 id="7-kubernetes">7. Kubernetes</h1>
<h2 id="71-일반">7.1 일반</h2>
<h2 id="인프라-환경-개요">인프라 환경 개요</h2>
<h3 id="📌-온프레미스on-premises">📌 온프레미스(On-Premises)</h3>
<ul>
<li><p>기업 내부 전산실에 직접 구축된 인프라 환경을 의미한다.
예: 기업 전용선, 랙(Rack), 서버, 스토리지 등</p>
</li>
<li><p>인프라 엔지니어가 서버·네트워크·OS 설치 등 <strong>개발 환경을 직접 구성</strong>해 제공한다.</p>
</li>
<li><p>개발자는 제공된 환경 위에 필요한 도구와 애플리케이션을 직접 설치하여 사용한다.
→ <strong>물리적인 환경을 직접 관리해야 한다</strong>는 특징이 있다.</p>
</li>
</ul>
<hr />
<h3 id="📌-iaas-infrastructure-as-a-service">📌 IaaS (Infrastructure as a Service)</h3>
<p><strong>서비스로서의 인프라 환경</strong></p>
<ul>
<li><p>자판기에서 필요한 음료를 고르듯,
<strong>미리 구성된 가상 인프라를 필요할 때 선택하여 사용할 수 있는 환경</strong>을 의미한다.</p>
</li>
<li><p>사용자는 필요한 만큼만 선택해 조합하여 사용할 수 있다.
예: AWS EC2, GCP Compute Engine, Azure VM 등</p>
</li>
<li><p>하드웨어 구매·설치·유지보수 등의 부담이 없고,
<strong>스케일링과 자동화가 용이한 현대적 인프라 형태</strong>이다.</p>
</li>
</ul>
<hr />
<h1 id="kubernetesk8s-개요">Kubernetes(K8s) 개요</h1>
<h2 id="1-컨테이너-인프라-환경cic이란">1. 컨테이너 인프라 환경(CIC)이란?</h2>
<p><strong>컨테이너 인프라 환경(CIC, Container Infrastructure Configuration)</strong>은
컨테이너를 중심으로 구성된 인프라 환경을 말한다.</p>
<p>여기서 말하는 <strong>컨테이너(Container)</strong>는</p>
<ul>
<li>하나의 운영체제 커널 위에서</li>
<li>다른 프로세스에 영향을 받지 않고</li>
<li><strong>독립적으로 실행되는 프로세스 상태</strong>를 의미한다. <em>(핵심)</em></li>
</ul>
<p>컨테이너는 <strong>VMWare, VirtualBox 같은 가상 머신(VM)</strong> 위에서 실행되는 프로세스보다
자원 사용이 적고, 훨씬 가볍고 빠르게 동작한다.</p>
<p>CIC는 크게 다음 요소로 구성된다.</p>
<ul>
<li>컨테이너(Container)</li>
<li>컨테이너 관리(Container Management)</li>
<li>개발 환경 구성 및 배포 자동화(CI/CD)</li>
<li>모니터링(Monitoring)</li>
</ul>
<hr />
<h2 id="2-컨테이너container">2. 컨테이너(Container)</h2>
<ul>
<li>애플리케이션 실행에 필요한 환경을 하나의 <strong>가벼운 패키지</strong>로 묶어 제공한다.</li>
<li>다양한 환경에서 동일하게 동작하므로 <strong>높은 이식성(Portability)</strong>을 제공한다.</li>
<li>“어디서 실행해도 동일한 결과가 나온다”는 장점이 있다.</li>
</ul>
<hr />
<h2 id="3-컨테이너-런타임container-runtime">3. 컨테이너 런타임(Container Runtime)</h2>
<p>컨테이너를 실제로 실행하는 소프트웨어를 말한다.</p>
<ul>
<li><p>Kubernetes v1.30에서는 <strong>CRI(Container Runtime Interface)</strong> 요구사항을 충족하는 런타임만 사용 가능하다.</p>
</li>
<li><p>공식 문서 기준 지원되는 대표 런타임:</p>
<ul>
<li><strong>containerd</strong></li>
<li><strong>CRI-O</strong></li>
<li><strong>도커 엔진(Docker Engine)</strong></li>
<li><strong>Mirantis Container Runtime</strong></li>
</ul>
</li>
</ul>
<hr />
<h2 id="4-오케스트레이션orchestration">4. 오케스트레이션(Orchestration)</h2>
<p>오케스트레이션은 원래 “관현악 편성법”이라는 의미이며,
IT에서는 다음을 의미한다.</p>
<ul>
<li>컨테이너의 <strong>배포</strong>,</li>
<li>컨테이너의 <strong>확장</strong>,</li>
<li>컨테이너 <strong>라이프사이클 관리</strong>,</li>
<li>컨테이너 <strong>통합 관리</strong> 전체 과정을 자동화하는 기술</li>
</ul>
<p>즉, <strong>수많은 컨테이너를 알아서 관리해주는 시스템</strong>을 말한다.</p>
<hr />
<h2 id="5-도커docker">5. 도커(Docker)</h2>
<ul>
<li>컨테이너를 생성하고 실행할 수 있도록 관리해주는 대표적인 컨테이너 도구.</li>
<li>OS 환경에 관계없이, 컨테이너 내부에서는 <strong>동일한 실행 환경을 보장</strong>한다.</li>
<li>CIC의 기반 기술.</li>
</ul>
<hr />
<h2 id="6-쿠버네티스kubernetes-k8s">6. 쿠버네티스(Kubernetes, K8s)</h2>
<blockquote>
<p>컨테이너 런타임을 기반으로, <strong>컨테이너를 오케스트레이션(관리)</strong>하는 도구.</p>
</blockquote>
<p>쿠버네티스는 다음과 같은 역할을 수행한다.</p>
<ul>
<li>복잡한 컨테이너 환경을 선언적 구성으로 쉽게 관리</li>
<li>자동화된 배포·롤아웃·롤백</li>
<li>서비스 중단 없이 확장/축소(Auto Scaling)</li>
<li>장애 발생 시 자동 복구(Self-Healing)</li>
<li>고가용성, 확장성, 이식성을 갖춘 오픈소스 플랫폼</li>
</ul>
<p>즉, <strong>수많은 컨테이너를 안정적이고 자동으로 운영하기 위한 통합 관리 솔루션</strong>이다.</p>
<p>또한 Kubernetes는 컨테이너 런타임과 통신하여 전체 시스템을 제어하며,
애플리케이션이 동작하는 데 필요한 요소들을 자동으로 조정·관리해준다.</p>
<hr />
<h2 id="7-젠킨스jenkins">7. 젠킨스(Jenkins)</h2>
<ul>
<li><strong>CI(Continuous Integration)</strong>, <strong>CD(Continuous Deployment)</strong>를 위한 자동화 도구.</li>
<li>빌드 → 테스트 → 패키징 → 배포 과정을 표준화하고 자동화한다.</li>
<li>기능 단위로 자주 배포하는 컨테이너 기반 환경(CIC)에 매우 적합한 도구.</li>
</ul>
<hr />
<h2 id="8-프로메테우스prometheus--그라파나grafana">8. 프로메테우스(Prometheus) &amp; 그라파나(Grafana)</h2>
<p>컨테이너 환경을 모니터링하기 위한 대표 도구.</p>
<ul>
<li><strong>Prometheus</strong>
→ 메트릭(상태 데이터) 수집 및 저장</li>
<li><strong>Grafana</strong>
→ Prometheus 데이터 시각화(GUI 기반 대시보드)</li>
</ul>
<hr />
<h2 id="9-api-application-programming-interface">9. API (Application Programming Interface)</h2>
<ul>
<li>컴퓨터(하드웨어)와 소프트웨어 간의 연결을 의미하는 개념.</li>
<li>한 소프트웨어가 다른 소프트웨어의 기능을 사용할 수 있도록 제공하는 인터페이스.</li>
<li>리눅스의 <code>mount</code>처럼 <strong>연결해주는 관문 역할</strong>을 한다고 보면 된다.</li>
</ul>
<hr />
<h3 id="kubernetes-실습-환경">Kubernetes 실습 환경</h3>
<ul>
<li><code>Virtualization Solution Tool</code> : <code>Oracle Virtual Box</code></li>
<li><code>Host OS</code> : <code>Windows 10 / 11</code></li>
<li><code>Guest OS</code> : <code>Rocky Linux 9.6 / CentOS 7.9</code></li>
<li><code>Container Tool</code> : <code>Docker Latest</code></li>
<li><code>Container Orchestration Tool</code> : <code>Kubernetes 1.28</code> -&gt; <code>1.29 Upgrade</code></li>
<li><code>Runtime</code> 환경이 적용된 <code>Containerd</code></li>
<li><code>3-Node Cluster</code> : <code>Master Plane 1EA / Worker Node 2EA</code></li>
</ul>
<hr />
<h2 id="72-vagrant를-이용한-ansible-실습-환경-구성">7.2 Vagrant를 이용한 Ansible 실습 환경 구성</h2>
<h3 id="구성-후-테스트">구성 후 테스트</h3>
<ul>
<li>Step 1. <code>Provisioning</code>에 필요한 기본 코드인 <code>Vagrantfile</code>을 생성한다.<ul>
<li>데이터 저장 폴더로 이동</li>
<li>상태 1. <code>vagrant init</code><ul>
<li>파일이 없는 상태일 때 입력하는 명령인데 다음과 같이 나올 경우에는 업데이트를 해야한다.</li>
</ul>
</li>
<li>상태 2. <code>vagrant init</code><ul>
<li>이미 존재하는 경우에는 오류가 아닌 오류가 발생한다.</li>
</ul>
</li>
<li>상태 3. <code>vagrant init</code><ul>
<li><code>vagrantfile</code> 삭제 후 다시 생성<pre><code class="language-cmd">del vagrantfile
vagrant init</code></pre>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 2. <code>Vagrantfile</code> 내용 확인 ![]<ul>
<li><code>type vagrant</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2814aa8a-2368-436e-a254-cd26f4b6e2ad/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<ul>
<li><p>Step 3. <code>Provisioning</code> 작업 1. 오류 발생 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/44f0eea2-08b4-44d9-9937-3bce5da62818/image.png" /></p>
<ul>
<li>오류 발생 이유 <ul>
<li>현재 설치되어 있는 이미지가 <code>base</code>로 되어 있기 때문이다.</li>
<li>즉, 해당 이미지를 <code>Vagrant</code>가 찾지 못해서 발생하는 오류이다.</li>
</ul>
</li>
<li>실행</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 4. <code>OS Images</code> 선택<ul>
<li>설치 할 <code>OS Image</code>를 선택하기 위해서 <code>base</code>에 <code>사용자가 설치할 가상 머신</code>을 기입하면 된다.</li>
<li><code>Vagrant</code>에서는 설치할 수 있는 가상 머신들을 사용자들이 올려서 공유할 수 있도록 하는 공간을 제공하고 있다.</li>
<li><u><a href="https://portal.cloud.hashicorp.com/vagrant/discover/rockylinux/9"><code>HashiCorp</code></a></u> 에서 rockylinux 설치</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 5.<code>Vagrant file</code>을 수정 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/84204dca-b087-455b-8e5c-9467041b38a1/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4ce1bd6c-5540-4d9d-a7c2-6ea60394c6d2/image.png" /><ul>
<li><code>Vagrant file</code><pre><code class="language-bash"># -*- mode: ruby -*-
# vi: set ft=ruby :
</code></pre>
</li>
</ul>
</li>
</ul>
<p>Vagrant.configure(&quot;2&quot;) do |config|
  config.vm.box = &quot;rockylinux/9&quot;
  config.vm.box_version = &quot;6.0.0&quot;
end</p>
<pre><code>---
- Step 6. `Provisioning` 작업 2. `Rocky Linux 9.5`
  - `HashiCorp`안 디렉토리 전체 삭제 ![](https://velog.velcdn.com/images/kyk02405/post/b5a3f110-defb-45a4-a376-1edb07dc3245/image.png)
  - `cmd`창에서 Step 1. 복사 후 입력 ![](https://velog.velcdn.com/images/kyk02405/post/67f452a9-dafa-4492-945d-98a4f92b7b87/image.png)
  - `vagrant up` 치면 오류 발생![](https://velog.velcdn.com/images/kyk02405/post/38f70a59-272b-4484-b185-76bbbf8dd659/image.png)
  - `vagrantfile` 수정 ![](https://velog.velcdn.com/images/kyk02405/post/8e0f640e-3d84-447d-9117-1760301d2026/image.png)
    - `config.vm.box_version = &quot;5.0.0&quot;`으로 변경
  - `vagrant up` 다시 실행 ![](https://velog.velcdn.com/images/kyk02405/post/39e0d19a-6804-4230-98d6-cfb4b9a68ce8/image.png)

---
- Step 7. 결과 확인 ![](https://velog.velcdn.com/images/kyk02405/post/581351c1-9ee2-4cd9-afca-e539fc63e331/image.png)
  - `VirtialBox`에 가상 머신 `HashiCorp_default`가 생성된 것을 확인한다. 이름을 별도로 지정하지 않았기 때문에 임의로 붙여진다.
  - `VirtualBox`에서 생성된 `가상 머신`이 제대로 동작하는지 `SSH`로 확인한다. ![](https://velog.velcdn.com/images/kyk02405/post/d570e5c2-168a-4bd7-a649-fc67a4b3133f/image.png)
  ```bash
  D:\3_VMs\HashiCorp&gt;Vagrant ssh
  [vagrant@localhost ~]$ uptime
  01:12:55 up 10 min,  1 user,  load average: 0.00, 0.01, 0.00
  [vagrant@localhost ~]$ cat /etc/redhat-release
  Rocky Linux release 9.5 (Blue Onyx)
  [vagrant@localhost ~]$</code></pre><hr />
<ul>
<li>Step 8. <code>vagrant</code> 삭제 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/49cba6cd-ac47-4236-846f-80e05d575198/image.png" /></li>
</ul>
<pre><code class="language-bash">[vagrant@localhost ~]$ exit
logout

D:\3_VMs\HashiCorp&gt;Vagrant -f destroy
    default: Are you sure you want to destroy the 'default' VM? [y/N] y
==&gt; default: Forcing shutdown of VM...
==&gt; default: Destroying VM and associated drives...</code></pre>
<hr />
<h2 id="72-vagrant-filevagrantfile를-이용한-테스트-환경-구축">7.2 Vagrant File(Vagrantfile)를 이용한 테스트 환경 구축</h2>
<h3 id="실습-환경-구축">실습 환경 구축</h3>
<h4 id="실습-1-가상-머신에-필요한-설정-등을-vagrantfile을-이용해서-자동으로-적용되는-가상-머신-생성">실습 1. <code>가상 머신</code>에 필요한 설정 등을 <code>Vagrantfile</code>을 이용해서 자동으로 적용되는 가상 머신 생성</h4>
<ul>
<li><p>개요</p>
<ul>
<li><p><code>vagrantfile</code> 수정을 통해 원하는 구성이 자동으로 <code>Rocky Linux</code>에 입력되도록 한다.</p>
</li>
<li><p>소스코드 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a97d703e-5e18-451d-915a-697fcd675244/image.png" /></p>
<pre><code class="language-txt"># -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(&quot;2&quot;) do |config| 
config.vm.define &quot;m-k8s&quot; do |cfg|
  cfg.vm.box = &quot;rockylinux/9&quot;
  cfg.vm.box_version = &quot;5.0.0&quot;
  cfg.vm.provider &quot;virtualbox&quot; do |vb|
    vb.name = &quot;m-k8s(clouddx_Rocky95)&quot;
    vb.cpus = 2
    vb.memory = 2048
    vb.customize [&quot;modifyvm&quot;, :id, &quot;--groups&quot;, &quot;/k8s-SM(clouddx_Rocky95)&quot;]
  end
  cfg.vm.host_name = &quot;m-k8s&quot;
  cfg.vm.network &quot;private_network&quot;, ip: &quot;192.168.1.10&quot;
  cfg.vm.network &quot;forwarded_port&quot;, guest: 22, host: 60010, auto_correct: true, id: &quot;ssh&quot;
  cfg.vm.synced_folder &quot;../data&quot;, &quot;/vagrant&quot;, disabled: true
end
end</code></pre>
</li>
<li><p>코드 설명 </p>
<ul>
<li><code>1 ~ 2번째 줄</code><ul>
<li>필수적으로 코드 맨앞에 선언 해줘야 한다.</li>
<li>두 줄 모두 <code>#</code>을 붙여줘야 한다.</li>
</ul>
</li>
<li><code>3번째 줄</code><ul>
<li><code>Vagrant</code>에서 루비로 코드를 읽어들여서 실행할 때는 동작하는 API 버전을 말한다.</li>
<li><code>do |config]|</code>는 <code>Vagrant</code> 설정의 시작을 알린다. </li>
<li>do |이름|으로 시작한 작업은 코드 하단에 <code>end</code>로 끝나야 한다,</li>
</ul>
</li>
<li><code>4 ~ 6번째 줄</code><ul>
<li>VB에서 보이는 가상 머신을 m-k8s로 정의한다.</li>
<li>가상 머신으로 설치될 OS의 이름, 버전 등 세부설정을 한다.</li>
</ul>
</li>
<li><code>7번째 줄</code><ul>
<li><code>Vagrant</code>의 프로바이더가 <code>VB</code>라는 것을 정의한다.</li>
<li><code>Provider</code>는 <code>Vagrant</code>를 통해서 제공되는 코드가 실제로 가상 머신으로 배포되게 하는 소프트웨어를 말하는데 <code>Virtual Box</code>가 여기에 해당한다.</li>
</ul>
</li>
</ul>
</li>
<li><p><code>Provisioning</code> 작업</p>
<ul>
<li>Step 1. 코드 실행 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ac081c9d-0a9c-4b96-8acb-6667802d1807/image.png" /></li>
</ul>
<pre><code class="language-bash">vagrant up</code></pre>
<ul>
<li><p>Step 2. 포트 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/05176ca8-3a9b-4f9a-9be6-bb6ebd835570/image.png" /></p>
<ul>
<li>가상 머신이 동작중일 때만 포트 포워딩된 포트를 확인할 수 가 있다.</li>
</ul>
</li>
<li><p>Step 3. 네트워크 관리자에서 새로 생성된 네트워크 대역을 확인한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/01c8ac4a-aaaa-46cd-ab77-9a4ac0833caf/image.png" /></p>
</li>
</ul>
</li>
<li><p>접속(SSH) 테스트 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9696777f-4b7f-467d-8b5b-9d7428e2d437/image.png" /></p>
</li>
<li><p>가상 머신 제거 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8ec41b5b-41de-4ad6-bac8-ef9104f9af3d/image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<h4 id="실습-2-가상-머신에-추가-패키지-설치">실습 2. 가상 머신에 추가 패키지 설치</h4>
<ul>
<li>개요<ul>
<li><code>Vagrantfile</code> 수정을 통해 Rocky Linux에 필요한 패키지를 설치한다.</li>
<li>vagrantfile을 수정하여 Rocky에 필요한 패키지를 설치한다.</li>
</ul>
</li>
<li>소스 코드</li>
</ul>
<ul>
<li><p>코드 실행</p>
<p>  <code>Vagrant up</code></p>
</li>
<li><p>전송(SSH)테스트</p>
<p>  <code>vagrant ssh</code></p>
</li>
<li><p>가상 머신 제거</p>
<p>  <code>vagrant destroy -f</code></p>
</li>
</ul>
<hr />
<h4 id="실습-3-가상-머신-4대master-nodecontroller-server-1대-worker-node-node-server-3대-구성">실습 3. 가상 머신 4대(Master Node(Controller Server) 1대, Worker Node (Node Server) 3대) 구성</h4>
<p><u><a href="https://drive.google.com/file/d/1LeJPFwCYMopdM2VRurKOBe4E1fYwc6wT/view?usp=drive_link">zip파일 다운로드 하기</a></u> 
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ebc60235-9c32-4ee8-97f9-e2566ed900f8/image.png" /></p>
<ul>
<li><code>config.sh</code><pre><code class="language-bash">#!/usr/bin/env bash
# modify permission  
chmod 744 ./ping_2_nds.sh</code></pre>
</li>
<li><code>install_pkg.sh</code><pre><code class="language-bash">#!/usr/bin/env bash
</code></pre>
</li>
</ul>
<h1 id="install-packages">install packages</h1>
<p>yum install vim-enhanced -y </p>
<pre><code>- `ping_2_nds.sh`
```bash
# ping 3 times per nodes
ping 192.168.1.101 -c 3
ping 192.168.1.102 -c 3
ping 192.168.1.103 -c 3</code></pre><ul>
<li><code>Vagrantfile</code><pre><code class="language-bash"># -*- mode: ruby -*-
# vi: set ft=ruby :
</code></pre>
</li>
</ul>
<p>Vagrant.configure(&quot;2&quot;) do |config| 
  config.vm.define &quot;m-k8s&quot; do |cfg|
    cfg.vm.box = &quot;rockylinux/9&quot;
    cfg.vm.box_version = &quot;5.0.0&quot;
    cfg.vm.provider &quot;virtualbox&quot; do |vb|
      vb.name = &quot;m-k8s(clouddx_Rocky95)&quot;
      vb.cpus = 2
      vb.memory = 2048
      vb.customize [&quot;modifyvm&quot;, :id, &quot;--groups&quot;, &quot;/k8s-SM(clouddx_Rocky95)&quot;]
    end
    cfg.vm.host_name = &quot;m-k8s&quot;
    cfg.vm.network &quot;private_network&quot;, ip: &quot;192.168.1.10&quot;
    cfg.vm.network &quot;forwarded_port&quot;, guest: 22, host: 60010, auto_correct: true, id: &quot;ssh&quot;
    cfg.vm.synced_folder &quot;../data&quot;, &quot;/vagrant&quot;, disabled: true<br />    cfg.vm.provision &quot;shell&quot;, path: &quot;install_pkg.sh&quot;
    cfg.vm.provision &quot;file&quot;, source: &quot;ping_2_nds.sh&quot;, destination: &quot;ping_2_nds.sh&quot;
    cfg.vm.provision &quot;shell&quot;, path: &quot;config.sh&quot;
  end</p>
<p>  #=============#</p>
<h1 id="added-nodes">Added Nodes</h1>
<p>  #=============#</p>
<p>  (1..3).each do |i|
    config.vm.define &quot;w#{i}-k8s&quot; do |cfg|
      cfg.vm.box = &quot;rockylinux/9&quot;
      cfg.vm.box_version = &quot;5.0.0&quot;
      cfg.vm.provider &quot;virtualbox&quot; do |vb|
        vb.name = &quot;w#{i}-k8s(clouddx_Rocky95)&quot;
        vb.cpus = 1
        vb.memory = 1024
        vb.customize [&quot;modifyvm&quot;, :id, &quot;--groups&quot;, &quot;/k8s-SM(clouddx_Rocky95)&quot;]
      end
      cfg.vm.host_name = &quot;w#{i}-k8s&quot;
      cfg.vm.network &quot;private_network&quot;, ip: &quot;192.168.1.10#{i}&quot;
      cfg.vm.network &quot;forwarded_port&quot;, guest: 22, host: &quot;6010#{i}&quot;,auto_correct: true, id: &quot;ssh&quot;
      cfg.vm.synced_folder &quot;../data&quot;, &quot;/vagrant&quot;, disabled: true
      cfg.vm.provision &quot;shell&quot;, path: &quot;install_pkg.sh&quot;
    end
  end
end</p>
<pre><code>- 코드 실행
```bash
vagrant up</code></pre><ul>
<li><p>접속(SSH) 테스트</p>
<ul>
<li><p><code>m-k8s</code>에 접속</p>
<pre><code class="language-bash">vagrant ssh m-k8s</code></pre>
</li>
<li><p>네트워크 상태 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8e2df110-e81c-4cef-a750-a68bc4c144aa/image.png" /></p>
<ul>
<li><code>net-tools</code> 설치 후 확인</li>
</ul>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8d659b73-2974-4ca6-ab53-57e19e3a665f/image.png" /></p>
<ul>
<li><code>passwd : vagrant</code></li>
</ul>
</li>
</ul>
</li>
<li><p>가상 머신 제거</p>
</li>
</ul>
<hr />
<h2 id="73-터미널-접속-프로그램-superputty을-이용한-다수의-가상-머신-접속">7.3 터미널 접속 프로그램 (SuperPutty)을 이용한 다수의 가상 머신 접속</h2>
<hr />
<h3 id="개요">개요</h3>
<ul>
<li><code>SuperPuTTY</code>를 이용해서 가상 머신 시스템에 로그인할 떄 오류가 발생하면 그냥 비번 입력하고 들어가면 된다.</li>
<li><code>Kubernetes</code>가 <code>192.168.1.x</code> 대역으로 사용하기 때문에 <code>VMWare</code>의 <code>Virtual Network Adapt</code>에서 <code>Host-only</code> 대역과 겹칠 수가 있기 때문에 미리 확인하고 변경해야 한다.</li>
</ul>
<hr />
<h3 id="superputty와-putty-연동">SuperPuTTY와 PuTTY 연동</h3>
<p><u><a href="https://github.com/jimradford/superputty/releases/tag/1.5.0.0">https://github.com/jimradford/superputty/releases/tag/1.5.0.0</a></u></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/97459c82-8025-48ab-b709-e4e60ad43483/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/215bbe9b-82f9-4348-a1a2-40e68e920985/image.png" /></p>
<hr />
<h3 id="putty의-설정-내용을-superputty에-적용">PuTTY의 설정 내용을 SuperPuTTY에 적용</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5eae5169-b80f-4138-90c4-502e4e02917e/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9b66517b-2b24-4397-a032-6893c40b524f/image.png" /></p>
<hr />
<h3 id="다수의-가상-머신-접속을-위한-설정">다수의 가상 머신 접속을 위한 설정</h3>
<ul>
<li><p>Step 1. 소스를 로딩한 후 실행한다.
<u><a href="https://drive.google.com/file/d/1aMrNAIq9LWY0gIe2YUe8lFfMAKnmdAer/view?usp=drive_link">소스 다운로드</a></u></p>
</li>
<li><p>Step 2. <code>Provisioning</code>을 진행한다.
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/12c859a5-bd57-4939-bf13-a742b1e5be26/image.png" /></p>
</li>
<li><p>Step 3.<code>Master Node System</code> 등록</p>
<ul>
<li><code>PuTTY Sessions</code> -&gt; <code>New Folder</code> -&gt; <code>k8s</code> -&gt; <code>New</code>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/acfda6b8-bacb-4a39-9d70-be34c8da7742/image.png" /></li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/958a8bda-8268-4e03-b873-ef41d95e25f2/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5fec201c-bfad-4908-b415-e4f3e2925e2d/image.png" /></p>
<ul>
<li><p>Step 4. <code>Worker Node System</code> 등록 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7ff7244a-a295-45f9-bb0b-b877cf31886d/image.png" /></p>
<ul>
<li><code>TCP Port</code> : 60101, 60102, 60103</li>
</ul>
</li>
<li><p>Step 5. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8f90540e-c381-4998-a709-15042a970171/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/958adda6-9626-4869-b03f-84754eac5933/image.png" /></p>
</li>
</ul>
<hr />
<h2 id="74-컨테이너를-다루는-표준-아키텍처-kubernetes">7.4 컨테이너를 다루는 표준 아키텍처 'Kubernetes'</h2>
<h3 id="kubernetes-이해하기">'Kubernetes' 이해하기</h3>
<ul>
<li>'Kubernetes'를 컨테이너 관리 도구'라고 설명했지만, 실제로 'Kubernetes'는
 '컨테이너 오케스트레이션 (Container Orchestration)'을 위한 솔루션이다.            즉, '컨테이너만 관리하는 '단순 관리'가 아닌 여러 가지(컨테이너 뿐만 아니라
 다양한 서비스(Apps)들)를 한 번에 관리할 수 있는 '통합 관리'를 위한 솔루션을 제공한다.         ; '오케스트레이션 (Orchestration)'이란 복잡한 단계를 관리하고 요소들의 유기적인 관계를
 미리 정의해 손쉽게 사용하도록 서비스를 제공하는 것을 의미한다.
 즉, '통합적인 관리'라고 보면 된다.</li>
<li>다수의 컨테이너를 유기적으로 연결, 실행, 종료할 뿐만 아니라 상태를 추적하고 보존하는 등
 컨테이너를 안정적으로 사용할 수 있게 만들어주는 것이 '컨테이너 오케스트레이션'이다.</li>
</ul>
<h3 id="실습-1-kubernetes-구성하기-kubernetes-테스트-환경-구축">실습 1. 'Kubernetes' 구성하기 ('Kubernetes' 테스트 환경 구축)</h3>
<h4 id="개요-1">개요</h4>
<ul>
<li>'Kubernetes'가 설치되는 'Master Node(Master System, Server Node)'는 가상 머신을 이용해서 쉽게 'On-premis(온-프레미스) 환경'에 가깝게 즉, 'Server Node(Server)'와 'Worker Node(Client)'가 한 공간에서  동작되도록 구성하고 설치되는 과정으르 'Vagrant'로 자동화하고 필요하면 'Kubernetes' 테스트 환경을 재구성할 수 있게 하겠다.</li>
</ul>
<hr />
<h4 id="step-1-vagrant-스크립트-파일-구성">Step 1. <code>Vagrant</code> 스크립트 파일 구성</h4>
<p><u><a href="https://drive.google.com/file/d/1MJmyTGfut7LH2QLPjSjg2xgb2NpmvP_L/view?usp=drive_link">실습 zip</a></u></p>
<ul>
<li><code>Vagrantfile</code> (노드 생성)</li>
<li><code>config.sh</code><ul>
<li><code>kubeadm</code>으로 <code>kubernetres</code>를 설치하기 위한 사전 조건을 설정하는 스크립트 파일이다.</li>
</ul>
</li>
<li><code>install_pkg.sh</code><ul>
<li>클러스터를 구성하기 위해서 가상 머신에 설치되어야 하는 의존성 패키지를 명시한다.</li>
</ul>
</li>
</ul>
<hr />
<h4 id="step-2-provisioning">Step 2. <code>Provisioning</code></h4>
<ul>
<li><code>Provisioning</code> 결과는 폴더에 포함된 파일들을 이용한 클러스터가 자동으로 구성된다.</li>
<li><code>SuperPuTTy</code>를 실행한 후 <code>m-k8s</code>를 더블클릭 후 터미널에 접속한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/63951d52-5365-463d-a85e-083f75e26065/image.png" /></li>
</ul>
<hr />
<h1 id="75-파드pods-배포를-중심으로-kubernetes-구성-요소-살펴보기">7.5 파드(Pods) 배포를 중심으로 Kubernetes 구성 요소 살펴보기</h1>
<h3 id="일반">일반</h3>
<ul>
<li><p>중요 용어</p>
<ul>
<li><p><code>Pods</code> (리소스 관리, 자원 관리)</p>
<ul>
<li><code>Kubernetes</code>의 <code>자원 객체(Resource Object)</code>를 말한다.</li>
<li><code>1개 이상</code>의 컨테이너로 구성된 <code>컨테이너 집합</code>을 의미한다.</li>
<li><code>컨테이너 애플리케이션(</code>실행<code>과 관련된 명령어)</code>을 배포하기 위한 <code>기본 단위</code>를 말한다. 즉, 하나의 <code>Pod</code>는 하나의 <code>완전한 애플리케이션</code>이라고 할 수 있다.</li>
<li><code>Pod를 생성한다.</code>라는 말은 단독으로 동작할 수 있는 애플리케이션을 생성한다.`라는 말이다.</li>
<li><code>Pod</code>는 애플리케이션을 여러 컨테이너로 분리할 때 컨테이너들이 공유해야 하는 리소스를 관리하면서 하나의 논리적인 단위로 사용된다.</li>
</ul>
</li>
<li><p><code>Namespace</code> (자원 공유)</p>
<ul>
<li>시스템(리눅스)<code>에서의</code>Namespace<code>는 운영체제 커널에서 여러 프로세스 그룹에게 독자적인</code>자원 공간`을 제공하기 위해 사용되는 기술을 말한다.</li>
<li><code>Kubernetes</code>가 단순 컨테이너를 사용하지 않고 컨테이너 관리를 위한 <code>기본 단위</code>로 <code>파드</code>를 사용하는 이유는, <code>여러 시스템(리눅스)</code>들이 <code>Namespace</code>를 공유하는 여러 컨테이너를 논리적인 집합으로 사용하기 위함이다.</li>
<li>즉, <code>Pod</code> 내에 여러 컨테이너가 같은 네트워크 I/F를 <code>공유</code>하고 서로의 <code>파일 시스템(파티션)</code>에 접근할 수 있다.</li>
</ul>
</li>
</ul>
</li>
<li><p>Node 활성화</p>
</li>
</ul>
<h3 id="kubernetes-구성-요소">Kubernetes 구성 요소</h3>
<ul>
<li><p>초기 확인 작업</p>
<ul>
<li><p>Kubernetes 구성 요소 확인</p>
<ul>
<li><p>현재 접속되어 있는 <code>m-k8s</code>에서 <code>kubectl get pods --all-namespaces</code> 명령으로 확인한다.</p>
<ul>
<li>kubectl get pods -A 도 가능</li>
</ul>
<p><img alt="image.png" src="attachment:4fa5cd4f-9ba4-49ec-8533-b73105ad0f4e:image.png" /></p>
<p><img alt="image.png" src="attachment:700f7a7d-0a1e-4f4a-a1f2-bd0587386b2e:image.png" /></p>
</li>
</ul>
</li>
<li><p>(매우 중요) <code>STATUS</code> 필드에 <code>Ready</code>가 아니라 <code>Pending(보류중)</code>이 나오면 절대 안된다.</p>
</li>
<li><p><code>--all-namespaces</code></p>
<ul>
<li>기본 네임스페이스<code>인</code>default 외에 모든 것을 표시하겠다`는 의미인데 즉, 지원 가능한 모든 네임스페이스에서 파드를 수집해서 보여준다.</li>
<li><code>Kubernetes</code> 클러스터를 이루는 구성 요소들은 파드 형태로 이루어져 있음을 알 수 있다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="kubernetes-구성-요소의-이름-생성-규칙">Kubernetes 구성 요소의 이름 생성 규칙</h3>
<ul>
<li><p><code>Kubernetes</code>의 구성 요소는 동시에 여러 개가 존재하는 경우 중복된 이름을 피하려고 뒤에 <code>해시(hash) 코드</code>가 삽입되는데 이때 <code>해시 코드</code>는 <code>무작위 문자열</code>로 생성된다.</p>
<p><img alt="image.png" src="attachment:2a873a7d-3617-4dac-a046-506079cb270e:image.png" /></p>
</li>
<li><p>구성 요소의 이름을 직접 지정할 수도 있지만, 구성 요소는 언제라도 문제가 발견되면 다시 생성되는 특성을 가지는 파드로 이루어져 있어서 <code>자동으로 이름을 지정하는 것이 관리</code>하기 쉽다.</p>
</li>
<li><p><code>coredns</code>에는 중간에 <code>5644d7b6d9</code>라는 문자열이 하나 더 있는데, 이는 <code>레플리카셋(ReplicaSet)</code>을 무작위 문자열로 변형해 추가한 것이다.</p>
<p><img alt="image.png" src="attachment:c06b38a3-c6e8-4158-8641-f14dae7c1c4e:image.png" /></p>
</li>
</ul>
<h3 id="관리자나-개발자가-pods를-배포할-때의-진행-순서"><code>관리자</code>나 <code>개발자</code>가 <code>Pods</code>를 배포할 때의 진행 순서</h3>
<ul>
<li><p>개요</p>
<ul>
<li><code>Step 1. ~ Step 8.</code>는 <code>기본 설정으로 배포</code>된 <code>Kubernetes</code>에서 이루어지는 통신 단계를 구분한 것이다.</li>
</ul>
</li>
<li><p><code>Master Node</code></p>
<ul>
<li><p>Step 1. <code>kubectl</code></p>
<ul>
<li><code>Kubernetes</code> 클러스터에 명령을 내리는 역할을 한다.</li>
<li>다른 구성 요소들과 다르게 바로 실행되는 명령 형태인 <code>바이너리(binary)</code>로 배포되기 때문에 <code>Master Node</code>에 있을 필요는 없다.</li>
<li>하지만 통상적으로 <code>API 서버(소프트웨어 사이의 I/F)</code>와 주로 통신하므로 이 책에서는 <code>API 서버</code>가 위치한 <code>마스터 노드</code>에 구성했다.</li>
</ul>
</li>
<li><p>Step 2. <code>API 서버</code></p>
<ul>
<li><code>Kubernetes</code> 클러스터의 중심 역할을 하는 <code>통로(소프트웨어 사이의 I/F)</code>이다.</li>
<li>주로 <code>상태 값을 저장</code>하는 <code>etcd</code>와 통신하지만, 그 밖의 요소들 또한 <code>API 서버</code>를 중심에 두고 통신하므로 <code>API 서버</code>의 역할이 매우 중요하다고 할 수 있다.</li>
<li>회사에 비유하면 <code>모든 직원과 상황을 관리하고 목표를 설정</code>하는 <code>관리자</code>에 해당한다.</li>
</ul>
</li>
<li><p>Step 3. <code>etcd</code></p>
<ul>
<li>구성 요소들의 <code>상태 값</code>이 모두 저장되는 곳을 말한다. 즉, 회사의 관리자가 모든 보고 내용을 기록하는 <code>노트</code>라고 생각하면 된다.</li>
<li><code>etcd</code>는 <code>리눅스의</code>구성 정보가 저장<code>된</code>etc 디렉터리<code>와</code>distributed(분산)<code>의 합성어이다. 즉,</code>구성 정보를 분산(퍼뜨린다.)해서 저장하겠다는 의미이다.</li>
<li>실제로 <code>etcd</code> 이외의 다른 구성 요소는 상태 값을 관리하지 않는다.</li>
<li>그러므로 <code>etcd</code>의 정보만 백업되어 있다면 <code>긴급한 장애 상황</code>에서도 <code>Kubernetes</code> 클러스터는 복구할 수 있다.</li>
<li><code>etcd</code>는 분산 저장이 가능한 <code>key-value</code> 저장소이므로 복제해서 여러 곳에 저장해 두면 하나의 <code>etcd</code>에서 장애가 발생하더라도 시스템의 가용성을 확보할 수 있다.</li>
<li>이와 같은 <code>멀티 마스터 노드 형태</code>는 부록에서 <code>kubespray</code>로 구성해 보도록 한다.</li>
</ul>
</li>
<li><p>Step 4. <code>Controller Manager (컨트롤러 매니저)</code></p>
<ul>
<li><code>Kubernetes</code> 클러스터의 <code>Object(Pods의 자원)</code> 상태를 관리한다.</li>
<li><code>Worker Node</code>에서 통신이 안되면 <code>상태 체크와 복구</code>는 <code>Controller Manager</code>에 속한 <code>Node Controller</code>에서 이루어진다.</li>
<li>다른 예로 <code>레플리카셋 컨트롤러</code>는 <code>레플리카셋</code>에 요청받은 <code>Pod</code>의 갯수대로 <code>Pod</code>를 생성한다.</li>
<li>이와 같이 다양한 상태 값을 관리하는 주체들이 <code>컨트롤러 매니저</code>에 소속되어 각자의 역할을 수행한다.</li>
</ul>
</li>
<li><p>Step 5. <code>Scheduler (스케줄러)</code></p>
<ul>
<li>노드의 상태와 자원, 레이블, 요구 조건 등을 고려해 <code>Pod</code>를 어떤 <code>Worker Node</code>에 생성할 것인지를 결정하고 할당한다.</li>
<li><code>Scheduler</code>라는 이름에 걸맞게 <code>Pod</code>를 조건에 맞는 <code>Worker Node</code>에 지정하고, <code>Pod</code>가 <code>Worker Node</code>에 할당되는 일정을 관리하는 역할을 담당한다.</li>
</ul>
</li>
</ul>
</li>
<li><p><code>Worker Node</code></p>
<ul>
<li><p>Step 6. <code>kubelet</code></p>
<ul>
<li><code>Pod</code>의 <code>구성 내용(Podspec)</code>을 받아서 컨테이너 런타임으로 전달하고, 즉, <code>Pod</code> 안에 있는 컨테이너들이 정상적으로 작동하는지 모니터링한다.</li>
</ul>
</li>
<li><p>Step 7. <code>컨테이너 런타임 (CRI, Container Runtime Interface)</code></p>
<ul>
<li><code>Pod</code>를 이루는 컨테이너의 실행을 담당한다.</li>
<li><code>Pod</code> 안에서 다양한 종류의 컨테이너가 문제 없이 작동하게 만드는 <code>표준 인터페이스</code>를 말한다.</li>
</ul>
</li>
<li><p>Step 8. <code>파드 (Pod)</code></p>
<ul>
<li>한 개 이상의 컨테이너로 단일 목적의 일을 하기 위해서 모인 단위를 말한다.</li>
<li>즉, 웹서버 역할을 할 수도 있고 로그나 데이터를 분석할 수도 있다.</li>
<li>여기서 중요한 것은 <code>Pod</code>는 <code>언제라도 죽을 수 있는 존재</code>라는 점인데 이것이 <code>Kubernetes</code>를 처음 배울 때 가장 이해하기 어려운 부분이다.</li>
<li><code>가상 머신</code>은 언제라도 죽을 수 있다고 가정하고 디자인하지 않지만, <code>Pod</code>는 언제라도 죽을 수 있다고 가정하고 설계됐기 때문에 <code>Kubernetes</code>는 여러 대안을 디자인했다.</li>
<li>어려운 내용이므로 여러 가지 테스트를 통해 여러분이 이해하도록 돕겠다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="명령어를-이용한-kubernetes-구성-요소의-기능-확인">명령어를 이용한 Kubernetes 구성 요소의 기능 확인</h3>
<ul>
<li><p>kubectl</p>
<ul>
<li><p>개요</p>
<ul>
<li>Kubernetes Cluster의 외부에서 Kubernetes Cluster에 명령을 내릴 수도 있다.</li>
</ul>
</li>
<li><p>Step 1. 활성화 되어 있는 <code>Worker Node</code> 중에서 <code>w3-k8s</code>에 원격으로 접속한다.</p>
</li>
<li><p>Step 2. kubectl은 <code>API Server</code>를 통해서 Kubernetes에 명령을 내린다.</p>
</li>
<li><p>Step 3. Master Node에서 Worker Node로 파일(admin.conf) 복사</p>
<p><img alt="image.png" src="attachment:b2d2764a-198f-43d0-a126-bd0b74df53c5:image.png" /></p>
</li>
</ul>
</li>
<li><p>kubelet</p>
<ul>
<li><p>개요</p>
<ul>
<li>Kubernetes에서 Pods의 생성과 상태 관리 및 복구 등을 담당한다.</li>
<li>kubelet가 문제가 있을 경우 Pods가 정상적으로 관리되지 않는다.</li>
</ul>
</li>
<li><p>Step 1. YAML 파일 업로드</p>
<ul>
<li><p>nginx 웹서버 Pod 배포를 위해 nginx-pod.yaml을 <code>m-k8s</code>에 업로드한다.</p>
<ul>
<li><p>E:\3_VMs\HashiCorp 에 해당 파일을 업로드</p>
<p><a href="">nginx-pod.yaml</a></p>
</li>
<li><p>scp 명령어를 사용해서 전송</p>
</li>
</ul>
<pre><code>E:\3_VMs\HashiCorp&gt;scp nginx-pod.yaml root@192.168.1.10:/root
The authenticity of host '192.168.1.10 (192.168.1.10)' can't be established.
ED25519 key fingerprint is SHA256:5AIsRZ4k9hHgfgh0YnmAK8k8dqmxWqaTjVB1Q+DCT+k.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
Warning: Permanently added '192.168.1.10' (ED25519) to the list of known hosts.
root@192.168.1.10's password:
nginx-pod.yaml                                            100%  115   112.3KB/s   00:00

E:\3_VMs\HashiCorp&gt;</code></pre><ul>
<li><p>확인</p>
<p><img alt="image.png" src="attachment:e8bbc34e-db5f-4beb-9881-1181858cdd9d:image.png" /></p>
</li>
</ul>
</li>
</ul>
</li>
<li><p>Step 2. 기능 검증을 위한 Pod 배포</p>
<ul>
<li><p><code>Master Node</code>에서 <code>nginx 웹서버 Pod</code>를 배포한다.</p>
<p><img alt="image.png" src="attachment:ae5e064f-f07b-494d-9d7f-bc09d05e868e:image.png" /></p>
</li>
<li><p>Pod의 구성 내용이 들어있는 nginx-pod.yaml 파일을 이용해서 파드를 배포한다.</p>
</li>
<li><p>Pod의 구성 내용을 파일로 읽어 들여서 1개의 Pod를 임의의 Worker Node에 배포</p>
</li>
</ul>
</li>
<li><p>Step 3. Pod가 <code>정상적으로 배포된 상태(Running)</code>인지 확인한다.</p>
<ul>
<li><p><code>Running</code> 대신 <code>Pending(보류중)</code> 또는 <code>ImagePullBackOff(이미지를 가지고 오지 못하는 경우)</code>가 나올 수가 있는데, 일정 시간이 지나면 자동으로 <code>Running</code>으로 변경된다.</p>
<p><img alt="image.png" src="attachment:984e1f4a-4004-461f-90d8-648facbd910f:image.png" /></p>
</li>
</ul>
</li>
<li><p>Step 4. Pod가 배포된 Worker Node 확인</p>
<p><img alt="image.png" src="attachment:3d314d8b-b66e-42ee-8b01-ad1c879b992d:image.png" /></p>
</li>
<li><p>Step 5. Pod가 배포된 Worker Nodes인 <code>NODE</code> 필드의 Worker Node로 이동한 후 kubelet 서비스를 중지한다.</p>
<p><img alt="image.png" src="attachment:c1c15c8b-4bfe-4b92-9094-ef34cfc7ffe2:image.png" /></p>
</li>
<li><p>Step 6. <code>m-k8s</code>에서 상태를 확인하고 Pods를 삭제한다.</p>
<p><img alt="image.png" src="attachment:03cf5c69-6c7a-4dfe-a008-1db28820e73c:image.png" /></p>
</li>
<li><p>Step 7. Kubelet 재실행 (복구)</p>
<ul>
<li><p>기능을 재실행한다.</p>
</li>
<li><p>출력 화면처럼 Pod가 제대로 관리되지 않고 있다… 는 것을 알 수 있다.</p>
<p><img alt="image.png" src="attachment:a21ec5f7-6bd8-4040-a5ec-7f8820052215:image.png" /></p>
</li>
</ul>
</li>
</ul>
</li>
<li><p>kube-proxy</p>
<ul>
<li><p>개요</p>
<ul>
<li><code>kubelet</code>는 <code>Pod</code>의 상태를 관리하고 <code>kube-proxy</code>는 <code>Pod</code>의 통신을 담당한다.</li>
<li><code>config.sh</code> 파일에서 <code>br_netfilter</code> 커널 모듈을 <code>적재</code>하고 <code>iptables</code>를 거쳐 통신하도록 설정했다.</li>
</ul>
</li>
<li><p>Step 1. 테스트하기 위해서 Master Node인 <code>m-k8s</code>에서 다시 Pod를 배포한다.</p>
<p><code>kubectl create -f nginx-pod.yaml</code></p>
</li>
<li><p>Step 2. Pod의 IP주소와 Worker Node를 확인한다.</p>
<p><img alt="image.png" src="attachment:02cac9d3-9c73-43fc-90db-ba03b3c9f5a2:image.png" /></p>
</li>
<li><p>Step 3. IP가 검색된 문서 내용에서 코드를 확인한다.</p>
<ul>
<li><p><code>curl(Client URL)</code> 명령어를 이용해서 Pod의 IP Address로 Nginx 웹서버의 메인 페이지의 문서 내용을 확인한다.</p>
<p><img alt="image.png" src="attachment:86c65b4c-3030-4099-9399-bbe225c7fe5d:image.png" /></p>
</li>
</ul>
</li>
<li><p>Step 4. kube-proxy에 문제가 생기는 상황을 만든다.</p>
<ul>
<li><p><code>배포 명령의 결과(kubectl get pods -o wide)</code>를 통해 나온 <code>노드(w1-k8s)</code>로 접속한다.</p>
</li>
<li><p>Pod가 위치한 Worker Node에서 br_netfilter 모듈을 제거한다.</p>
</li>
<li><p>명령 실행 후 네트워크 데몬을 재실행하면 변경된 내용이 반영된다.</p>
<p><img alt="image.png" src="attachment:07be76d8-b984-48b3-8057-7061daef60fe:image.png" /></p>
</li>
</ul>
</li>
<li><p>Step 5. IP가 검색된 문서 내용에서 코드를 확인한다.</p>
<ul>
<li><p><code>curl(Client URL)</code> 명령어를 이용해서 Pod의 IP Address로  Nginx 웹 서버의 메인 페이지의 문서 내용을 확인한다.</p>
</li>
<li><p>Pod에서 정보를 받아오지 못하기 때문에 강제종료 시킨다.</p>
<p><img alt="image.png" src="attachment:b358ce0b-b72e-4ea3-a963-50abb5c5a3da:image.png" /></p>
</li>
</ul>
</li>
<li><p>Step 6. <code>Pod</code>의 상태 확인</p>
<ul>
<li><p>개요</p>
<ul>
<li><code>Pod</code>의 노드 위치와 IP가 변경되지 않았는지, 작동 상태에 문제가 없는지 등을 확인한다.</li>
<li><code>kubelet</code>을 통해 확인된 <code>Pod</code>의 <code>노드 위치</code>와 <code>IP Address</code>는 그대로이고 상태도 <code>작동 중(Running)</code>으로 문제가 없는 것처럼 보인다.</li>
<li>하지만 <code>kube-proxy</code>가 이용하는 <code>br_netfilter</code> 모듈에 문제가 있어서 <code>Pod</code>의 <code>Nginx 웹 서버</code>와의 통신만이 정상적으로 이루어지지 않는 상태이다. 즉, <code>curl</code>로 <code>nginx 서버</code>에 접속했으나 연결이 되지 않고 <code>Connection timed out</code>이라고 출력된다.</li>
</ul>
</li>
</ul>
</li>
<li><p>Step 7. 정상적인 상태로 작업한다.</p>
<ul>
<li><p>br_netfilter 모듈을 커널에 다시 적재하고 시스템을 재시작한다.</p>
<p><code>modprobe br_netfilter</code></p>
</li>
</ul>
</li>
<li><p>Step 8. 상태 확인</p>
<p><img alt="image.png" src="attachment:7b4bcff1-7002-49b5-964b-bad58b17f00e:image.png" /></p>
</li>
<li><p>Step 9. Nginx 웹서버의 내용 출력</p>
</li>
<li><p>Step 10. 삭제</p>
<p><img alt="image.png" src="attachment:9cfdc2e3-ab52-4e6f-a4e0-27735e344632:image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="76-kubernetes-기본-사용법-배우기">7.6 Kubernetes 기본 사용법 배우기</h1>
<h3 id="주요-용어">주요 용어</h3>
<ul>
<li><p>Node(노드)</p>
<ul>
<li><code>Kubernetes</code> 스케쥴러에서 Pod를 할당 받고 처리하는 역할을 담당한다.</li>
<li>배포하는 시스템(Master Node)과 배포받는 시스템(Worker Node)들을 말한다.</li>
</ul>
</li>
<li><p>Pod(파드)</p>
<ul>
<li><code>Kubernetes</code>의 기본 단위를 말한다.</li>
<li>Pod는 여러 개의 Container를 하나의 Application으로 동작하도록 만드는 Container 들의 묶음이다.</li>
</ul>
</li>
<li><p>Replica Set(레플리카셋 오브젝트)</p>
<ul>
<li>일정한(원하는) 갯수의 Pod를 유지하게 해주는 Controller이다.</li>
<li><code>갯수 유지</code>가 핵심이다.</li>
</ul>
</li>
<li><p>Deployment(디플로이먼트 오브젝트)</p>
<ul>
<li>이미지를 이용해서 Pod를 생성할 때 <code>Replicase Object</code>와 함께 사용하면 문제 발생 시  Pod를 항상 정상적으로 유지될 수 있도록 관리한다.</li>
</ul>
</li>
<li><p>Scheduler(스케쥴러)</p>
<ul>
<li>Worker Node에 Pod를 생성하도록 선언하는 것을 말한다.</li>
</ul>
</li>
</ul>
<h3 id="실습-1-pod-생성">실습 1. Pod 생성</h3>
<ul>
<li><p>Pod 생성</p>
<ul>
<li><p>방법 1. <code>kubectl run</code> 명령</p>
<ul>
<li><p>현재 Pod 상태 확인</p>
</li>
<li><p>생성</p>
</li>
<li><p>확인</p>
<p><img alt="image.png" src="attachment:5299be2b-1cad-4a39-b73d-b6bbd77161da:image.png" /></p>
</li>
</ul>
</li>
<li><p>방법 2. <code>kubectl create</code> 명령</p>
<ul>
<li><p>Pod 생성</p>
<ul>
<li><p><code>image</code>라는 옵션이 없다는 에러가 출력되고 Pod는 생성되지 않는다. 즉, 문법 오류이다.</p>
<p><img alt="image.png" src="attachment:1fd0cdb0-729b-4692-a756-4c15c6da6ded:image.png" /></p>
</li>
</ul>
</li>
<li><p><code>create deployment</code>와 함께 동일한 Pod를 생성</p>
<p><img alt="image.png" src="attachment:34983250-83bb-46b2-aaeb-cdb989135f91:image.png" /></p>
</li>
<li><p>(비추천) 다른 이름으로 생성하면 되니까 굳이 레플리카셋을 추가할 필요가 없다.</p>
</li>
<li><p>생성했던 Pod를 삭제한다.</p>
<ul>
<li><p>deployment로 생성한 Pod는 삭제시에도 deployment를 사용해야 하고 Pod명만 입력해야 한다.</p>
<p><img alt="image.png" src="attachment:5e6b36b4-6917-4d3e-9f38-ced1ed5a246d:image.png" /></p>
</li>
</ul>
</li>
</ul>
</li>
<li><p>정상적인 방법으로 pod를 다시 생성하고 확인한다.</p>
<p><img alt="image.png" src="attachment:d24e754a-245d-487e-b924-cfb642d700ef:image.png" /></p>
</li>
<li><p>생성된 Pod를 통해 웹 페이지 정보를 제대로 받아오는지 확인한다.</p>
<ul>
<li><p>Pod가 모두 동작되는지 확인하고 IP주소도 확인한다.</p>
<p><img alt="image.png" src="attachment:b7c76005-5422-446d-aab6-8d05a025f7c8:image.png" /></p>
</li>
<li><p>curl 명령을 이용해서 웹페이지 정보를 받아오는지 확인한다.</p>
<p><img alt="image.png" src="attachment:5e219176-9f0b-4676-ac48-93b20dbdecc5:image.png" /></p>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code>run</code>과 <code>create deployment</code>를 이용한 <code>Pod 생성</code>의 차이점</p>
<ul>
<li><p><code>run</code></p>
<ul>
<li>Pod를 생성하면 단일 Pod 1개만 생성되고 관리된다.</li>
</ul>
</li>
<li><p><code>create deployment</code></p>
<ul>
<li><code>Deplyment</code>라는 <code>관리 그룹</code> 내에서 Pod가 생성되고 관리된다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="실습2-object오브젝트">실습2. Object(오브젝트)</h3>
<ul>
<li><p>개요</p>
<ul>
<li><code>Pod</code>와 <code>Deployment</code>는 <code>Spec(스팩)과 Status(상태)</code> 등의 값을 가지고 있다.</li>
<li>이러한 값을 가지고 <code>Pod</code>와 <code>Deployment</code>를 개별 속성을 포함해서 부르는 단위를 <code>Object</code>라고 말한다.</li>
<li>여러 유형의 <code>Object(기본 오브젝트, Deployment 오브젝트)</code>를 제공하고 있다.</li>
</ul>
</li>
<li><p>Object 1. 기본 오브젝트</p>
<ul>
<li><p><code>Pod (파드)</code></p>
<ul>
<li><code>Kubernetes</code>에서 실행되는 최소 단위 즉, <code>웹 서비스</code>를 구동하는데 필요한 최소단위를 말한다.</li>
<li>독립적인 공간과 사용 가능한 IP를 가지고 있다.</li>
<li>한 개의 <code>Pod</code>는 1개 이상의 컨테이너를 가지고 있기 때문에 여러 기능을 묶어서 하나의 목적으로 사용할수 있다.</li>
<li>범용으로 사용할 때는 대부분 1개의 파드에 1개의 컨테이너를 적용한다.</li>
</ul>
</li>
<li><p><code>Namespaces (네임스페이스)</code></p>
<ul>
<li><p><code>Kubernetes Cluster</code>에서 사용되는 리소소들을 구분해서 관리하는 그룹을 말한다.</p>
</li>
<li><p>특별히 지정하지 않으면 기본으로 할당되는 <code>default</code>, <code>Kubernetes</code> 시스템에서 사용하는 <code>kube-system</code>, 온프레미스에서 <code>Kubernetes</code>를 사용할 경우 외부에서 <code>Kubernetes Cluster</code> 내부로 접속하게 해주는 <code>Container</code>들이 속해 있는 <code>metalb-system</code>이 있다.</p>
<ul>
<li><p><code>default 오브젝트</code></p>
<ul>
<li>특별히 지정하지 않으면 기본으로 할당되고 사용된다.</li>
</ul>
</li>
<li><p><code>kube-system 오브젝트</code></p>
<ul>
<li><code>Kubernetes</code> 시스템에서 할당되고 사용된다.</li>
</ul>
</li>
<li><p><code>metalb-system 오브젝트</code></p>
<ul>
<li>온프레미스에서 <code>Kubernetes</code>를 사용할 경우 외부에서 <code>Kubernetes Cluster</code> 내부로 접속하게 해주는 <code>Container</code>들이 속해 있다.</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p><code>Volume (볼륨)</code></p>
<ul>
<li><code>Pod</code>가 생성될 때 <code>Pod</code>에서 사용할 수 있는 디렉터리를 제공한다.</li>
<li>기본적으로 <code>Pod</code>는 지속되는 것이 아니라 제공되는 디렉터리도 임시로 사용한다.</li>
<li><code>Pod</code>가 사라지더라도 저장과 보존이 가능한 디렉터리를 <code>볼륨 오브젝트</code>를 통해 사용할 수 있다.</li>
</ul>
</li>
<li><p><code>Service (서비스)</code></p>
<ul>
<li><code>Pod</code>는 <code>Cluster</code>내에서 <code>유동적</code>이기 때문에 접속 정보가 고정일 수가 없다.</li>
<li><code>Pod</code> 접속을 안정적으로 유지하도록 <code>서비스</code>를 통해서 내부와 외부로 연결이 된다.</li>
<li><code>서비스</code>는 새로 <code>Pod</code>가 생성될 때 부여되는 <code>새로운 IP</code>를 기존에 제공했던 기능과 연결해 준다.</li>
<li>기존에 운영하고 있던 <code>인프라</code>에서 <code>로드밸런서</code>, <code>게이트웨이</code>와도 비슷한 역할을 한다.</li>
</ul>
</li>
</ul>
</li>
<li><p>Object 2. <code>Deployment</code> 오브젝트</p>
<ul>
<li><p>개요</p>
<ul>
<li><p><code>기본 오브젝트</code>만으로도 <code>Kubenetes</code>를 사용할 수 있지만 한계가 있어서 이를 좀 더 효율적으로 작동하도록 기능들을 <code>조합하고 추가(확장성)</code>해 구현한 것을 말한다.</p>
</li>
<li><p>이외에도 <code>데몬셋(DaemonSet)</code>, <code>컨피그맵(ConfigMap)</code>, <code>레플리카셋(ReplicaSet)</code>, <code>PV(PersistentVolume)</code>, <code>PVC(PersistentVolumeClaim)</code>, <code>스테이트풀셋(StatefulSet)</code> 등이 있다.</p>
<ul>
<li>앞으로도 요구 사항에 따라 목적에 맞는 오브젝트들이 추가될 것이다.</li>
<li><code>Kubenetes</code>에서 가장 많이 쓰이는 <code>Deployment</code> 오브젝트는 <code>Pod</code>에 기반을 두고 있으며, 레플리카셋 오브젝트를 합쳐 놓은 형태이다.</li>
</ul>
</li>
</ul>
</li>
<li><p><code>Deployment 오브젝트</code>의 생성과 삭제</p>
<ul>
<li><p>생성</p>
<p><img alt="image.png" src="attachment:298a01dd-2b2d-427d-bebc-5f03223749ec:image.png" /></p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="실습-3-replicaset-오브젝트">실습 3. ReplicaSet 오브젝트</h3>
<ul>
<li><p>개요</p>
<ul>
<li>많은 사람들을 대상으로 웹 서비스를 하려면 다수의 <code>Pod</code>가 필요한데 이를 한 개씩 생성하는 것은 매우 비효율적이다.</li>
<li>(핵심) <code>Kubernetes</code>에서는 다수의 <code>Pod</code>를 만드는 <code>레플리카셋 오브젝트</code>를 제공한다.</li>
<li>만약 <code>Pod</code>를 3개를 만든다고 <code>레플리카셋</code>에 선언을 하면 <code>컨트롤러 매니저</code>, <code>스케쥴러</code>가 <code>Worker Node</code>에 <code>Pod</code> 3개를 만들도록 선언한다.</li>
<li><code>레플리카셋</code>은 <code>Pod</code>의 수를 보장하는 기능만 제공하기 때문에 <code>롤링 업데이트</code> 기능이 추가된 <code>Deployment</code>를 사용해서 <code>Pod</code>의 수를 관리한다.</li>
</ul>
</li>
<li><p>실행 1. 정상</p>
<ul>
<li><p><code>kubectl describe pod dpy-hname-59778b9bb-q7l8r -n default</code></p>
<pre><code>[root@m-k8s ~]# kubectl describe pod dpy-hname-59778b9bb-q7l8r -n default
Name:         dpy-hname-59778b9bb-q7l8r
Namespace:    default
Priority:     0
Node:         w2-k8s/192.168.1.102
Start Time:   Fri, 12 Dec 2025 17:38:39 +0900
Labels:       app=dpy-hname
              pod-template-hash=59778b9bb
Annotations:  cni.projectcalico.org/podIP: 172.16.103.130/32
Status:       Running
IP:           172.16.103.130
IPs:
  IP:           172.16.103.130
Controlled By:  ReplicaSet/dpy-hname-59778b9bb
Containers:
  echo-hname:
    Container ID:   docker://b1d25cb22620f69d51b5f351bf7ff892a6371a3580dacac2b94a76f70858a7f3
    Image:          sysnet4admin/echo-hname
    Image ID:       docker-pullable://sysnet4admin/echo-hname@sha256:6df896ded565cab71562ccbafc2be6d830c92391f021343d5f1dff7f9a727bce
    Port:           &lt;none&gt;
    Host Port:      &lt;none&gt;
    State:          Running
      Started:      Fri, 12 Dec 2025 17:38:53 +0900
    Ready:          True
    Restart Count:  0
    Environment:    &lt;none&gt;
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-88qqr (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  default-token-88qqr:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-88qqr
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  &lt;none&gt;
Tolerations:     node.kubernetes.io/not-ready:NoExecute for 300s
                 node.kubernetes.io/unreachable:NoExecute for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  16m   default-scheduler  Successfully assigned default/dpy-hname-59778b9bb-q7l8r to w2-k8s
  Normal  Pulling    16m   kubelet, w2-k8s    Pulling image &quot;sysnet4admin/echo-hname&quot;
  Normal  Pulled     16m   kubelet, w2-k8s    Successfully pulled image &quot;sysnet4admin/echo-hname&quot;
  Normal  Created    16m   kubelet, w2-k8s    Created container echo-hname
  Normal  Started    16m   kubelet, w2-k8s    Started container echo-hname</code></pre></li>
</ul>
</li>
<li><p>실행 2. 오류</p>
<ul>
<li>(toomanyrequest, 너무 많은 요청) 때문에 출력이 제대로 되지 않을 수가 있다.</li>
</ul>
</li>
<li><p>실행 3. -</p>
<ul>
<li><p>배포된 Pods의 상태를 확인</p>
<p><img alt="image.png" src="attachment:c92ad50d-4655-4933-88e6-8f68d44b55d7:image.png" /></p>
</li>
<li><p><code>nginx-pod</code>를 <code>Scale</code>을 이용해서 3개로 증가</p>
</li>
<li><p><code>nginx-pod</code>는 <code>kubectl create nginx-pod --image=nginx</code> 명령어를 이용해서 생성한 Pod이기 때문에 <code>resource</code>로써 사용할 수가 없다. 따라서 <code>resource</code>를 확인할 수가 없다는 오류가 발생한다. <code>Deployment</code>로 생성된 <code>dpy-nginx</code>를 <code>Scale</code> 명령을 사용해서 실행한다.</p>
</li>
<li><p><code>Scale</code>로 추가된 2개의 <code>nginx-pod</code>를 확인한다.</p>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="실습-4-spec을-지정해서-오브젝트-생성">실습 4. Spec을 지정해서 오브젝트 생성</h3>
<ul>
<li><p>이미지 구분</p>
<ul>
<li><p>mariadb</p>
<ul>
<li><code>Docker</code>에서 이미지 검색을 위한 명령어인 <code>search</code>를 통해서 확인 가능한 이미지이다.</li>
</ul>
</li>
<li><p>samadalwho/mariadb</p>
<ul>
<li><p>Container`를 이용해서 생성한 이미지</p>
</li>
<li><p>일반적으로 <code>Docker Hub</code>에서 다운로드 한다.</p>
</li>
<li><p><code>Docker Hub</code>가 <code>Public</code>인 경우</p>
<ul>
<li>추가 비용이 없다.</li>
<li>search 명령을 이용해서는 확인할 수가 있다.</li>
</ul>
</li>
<li><p><code>Docker Hub</code>가 <code>Private</code>인 경우</p>
<ul>
<li>추가 비용이 있다.</li>
<li>search 명령을 이용해서는 확인할 수가 없다.</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p>개요</p>
<ul>
<li><code>kubectl create deployment dpy-hname --image=sysnet4admin/echo-hname</code> 명령을 이용해서 <code>Deployment</code>를 생성하게 되면 1개의 <code>Pod</code>만 생성된다. 즉,<code>명령어</code>를 이용해서는 3개의 <code>Pod</code>를 가진 <code>Deployment 오브젝트</code>를 생성 할 수 없다.</li>
<li>만약, <code>Deployment</code>를 생성하면서 한 번에 여러 개의 <code>Pod</code>를 생성하려면 <code>create</code>에서는 <code>replicas</code> 옵션은 사용할 수 없고 <code>scale</code>은 이미 생성된 <code>Deployment</code>에서만 사용 가능하다.</li>
<li>(핵심) 따라서 이와 같은 설정을 적용하려면 필요한 내용을 파일로 작성해야 한다. 이 때 작성하는 파일을 <code>Spec(스팩)</code>이라고 한다.</li>
<li><code>오브젝트 스팩</code>은 일반적으로 <code>야믈(YAML, Yet Another Markup Language)</code> 문법으로 작성한다.</li>
</ul>
</li>
<li><p><code>야믈 (YAML)</code></p>
<ul>
<li><p>처음에는 <code>또 다른 마크업 언어(Yet Another Markup Language)</code>의 약어였다.</p>
</li>
<li><p>그러나 <code>공식 사이트([http://www.yaml.org](http://www.yaml.org/))</code>에서 <code>데이터의 내용을 쉽게 파악할 수 있는 표준</code>이라고 설명하며 <code>야믈은 단순히 마크업 언어가 아니다(YAML Ain't Markup Language)</code>라고 다시 정의했다.</p>
</li>
<li><p>여기서 <code>마크업(Markup)</code>이란 <code>문서나 데이터의 구조를 태그를 이용해 기술</code>하는 것을 의미한다.</p>
</li>
<li><p>익히 알고 있는 <code>HTML(HyperText Markup Language)</code>이 가장 유명한 마크업 언어 중 하나이다.</p>
</li>
<li><p>3개의 <code>nginx</code> <code>Pod</code>를 <code>Deployment 오브젝트</code>로 생성</p>
<ul>
<li><code>명령어</code>를 이용해서는 3개의 <code>Pod</code>를 가진 <code>Deployment 오브젝트</code>를 생성 할 수 없기 때문에 <code>오브젝트 스팩</code>을 작성해서 <code>Deployment 오브젝트</code>를 생성해야 한다.</li>
<li><code>echo-hname.yaml</code> / <code>nginx-pod.yaml</code></li>
</ul>
</li>
</ul>
</li>
<li><p>실행</p>
<ul>
<li><p>(생략) 파일 업로드 1. Windows 10에서 ‘scp’를 이용해서 ‘2개의 YAML 파일’을 업로드한다.</p>
</li>
<li><p>파일 업로드 2. <code>kubernetes</code> 버전에 따라서 사용 가능한 <code>API</code> 버전이 다르기 때문에 꼭 확인 해야한다.</p>
</li>
<li><p><code>echo-hname-yml</code> 파일을 이용해서 <code>Deployment</code>를 생성하는데 현재 <code>Deployment</code>는 <code>Pods</code> 3개를 생성하도록 <code>replicas</code>에 정의되어 있다.</p>
</li>
<li><p><code>echo-hname.yaml</code> 파일을 수정해서 <code>Pod</code>를 <code>replicas</code>를 6개로 늘린다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0de5c8de-4231-45aa-af37-36ad1e16bca7/image.png" /></p>
<pre><code class="language-bash">[root@m-k8s 3.2.4]# sed -i 's/replicas: 3/replicas: 6/' ./echo-hname.yaml</code></pre>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/07856246-3ecf-4e7a-b5c9-9dc8ad1f31ac/image.png" /></p>
</li>
<li><p>결론</p>
<ul>
<li><code>kubectl scale deployment dpy-nginx --replicas=3</code> 명령으로 <code>Pod</code>수를 늘릴수 있지만 명령이 아닌 문서 파일로 <code>Pod</code> 수를 늘리고 오브젝트의 스펙을 변경해서 적용하면 된다.</li>
<li>그리고 위의 2개의 명령으로 인한 오류는 <code>apply</code> 명령을 사용하면 된다</li>
</ul>
</li>
</ul>
</li>
<li><p><code>apply</code>로 오브젝트 생성 관리</p>
<ul>
<li><code>Pod</code> 생성을 위한 명령어 3가지<ul>
<li><code>run</code> <code>(단일 Pod만을 생성)</code></li>
<li><code>create</code> <code>(Deployment 생성 시 파일의 변경사항을 바로 적용할 수가 없다.)</code></li>
<li><code>apply</code> <code>(명령이 아닌 문서 파일로 Pod 수를 늘리고 스펙도 변경해서 적용할 수가 있다.)</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="실습-5-pod의-컨테이너-복구-방법">실습 5. ‘Pod’의 컨테이너 복구 방법</h3>
<ul>
<li><p>개요</p>
<ul>
<li>지금까지 'Pod(컨테이너들의 집합)'와 'Deployment(Pod 생성 유형)', 'Object(Pods)' 들에 관해 알아봤다. 이제 본격적으로 배운 내용을 사용해 본다.</li>
<li>'Kubernetes'는 거의 모든 부분이 '자동 복구되도록 설계'되어 있다.</li>
<li>특히 'Pod'의 자동 복구 기술을 '셀프 힐링(Self-Healing)'이라고 한다.</li>
<li>이 기술은 제대로 작동하지 않는 컨테이너를 다시 시작하거나 교체해서 파드가 정상적으로 작동하게 한다.</li>
</ul>
</li>
<li><p>실행</p>
<ul>
<li><p>Pod에 접속하기 위한 IP 확인</p>
</li>
<li><p>Pod Container의 Shell에 접속</p>
<p><code>kubectl exec -it nginx-pod -- /bin/bash</code></p>
</li>
</ul>
</li>
<li><p>참고 (Docker에서의 컨테이너 생성과 접속)</p>
<p>  sudo docker run -itd --name samadalweb centos:7 /bin/bash
  sudo docker create -it --name samadalweb centos:7 /bin/bash</p>
<p>  sudo docker start samadalweb
  sudo docker exec -it samadalweb /bin/bash</p>
</li>
<li><p>‘--’의 의미</p>
<ul>
<li>‘exec’에 대한 인자값을 나누고 싶을 때 사용한다.</li>
<li>명령과 옵션을 구분하기 위해 사용한다.</li>
</ul>
</li>
<li><p>'Bash Shell'에 접속하면 컨테이너에서 구동하는 'nginx'의 'PID(Process ID, 프로세서 식별자)'를 확인한다. 'nginx'의 'PID'는 항상 '1'이다.<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b016d0f9-f392-4cbd-b961-d489a52cb37f/image.png" /></p>
</li>
</ul>
<ul>
<li>명령 실행<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/439e23ca-5262-4370-92b9-0197505ad413/image.png" /></li>
</ul>
<ul>
<li>Pod의 동작 보장 기능<ul>
<li>개요<ul>
<li>Kubetnetes에서는 Pod에 문제가 생기면 Pod를 자동 복구하고 Pod가 항상 동작되도록 보장해주는 기능이 있다.</li>
</ul>
</li>
<li>실행<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7cb29939-958e-4a03-a08a-b074618b0940/image.png" /></li>
</ul>
</li>
</ul>