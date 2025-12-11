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