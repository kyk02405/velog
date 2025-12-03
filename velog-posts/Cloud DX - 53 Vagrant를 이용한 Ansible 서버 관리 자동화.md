# Cloud DX - 53 Vagrant를 이용한 Ansible 서버 관리 자동화

- 📅 Published: Wed, 03 Dec 2025 04:06:46 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-53-Vagrant%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-Ansible-%EC%84%9C%EB%B2%84-%EA%B4%80%EB%A6%AC-%EC%9E%90%EB%8F%99%ED%99%94)

<h1 id="05-vagrant를-이용한-ansible-서버-관리-자동화">05. Vagrant를 이용한 Ansible 서버 관리 자동화</h1>
<h2 id="51-실습-환경-구성">5.1 실습 환경 구성</h2>
<h3 id="개요">개요</h3>
<ul>
<li><p><code>Vagrant</code>는 사용자의 요구에 맞게 시스템 자원을 할당, 배치, 배치해 두었다가 필요할 때에 시스템을 사용할 수 있는 상태로 만들어 준다.</p>
</li>
<li><p>(매우 중요) <code>Vagrant</code>를 이용해서 작업하기 위해서는 작업되는 시스템은 반드시 <code>Host OS</code>여야 한다.</p>
<ul>
<li><code>Vagrant</code>는 <code>일반 문서 파일</code>로 되어 있는데 <code>cmd</code>에서 명령을 입력하는 방식으로 실행된다.</li>
<li><code>Vagrant</code>가 실행이 되면 <code>가상머신이 자동으로 로딩</code>되고 동작 하는데 즉, 가상 머신은 <code>가상 머신 툴</code>을 통해 자동으로 로딩되고 동작을 한다는 말이다.</li>
<li>이 때 사용되는 <code>가상 머신 툴</code>은 <code>Oracle VirtualBox</code>이다.</li>
<li>따라서 <code>Oracle VirtualBox</code> 안에 <code>Windows 10</code>를 설치하고 <code>Vagrant</code>를 실행하게 되면 오류가 발생한다.</li>
</ul>
</li>
</ul>
<h3 id="provisioning프로비저닝-공급">Provisioning(프로비저닝, 공급)</h3>
<ul>
<li><code>어떤 프로세스(진행 상황 등)</code>나 서비스를 실행하기 위한 준비 단계를 <code>프로비저닝(Provisioning)</code>이라고 말한다.</li>
<li>네트워크나 컴퓨팅 자원을 준비하는 단계</li>
<li>준비된 컴퓨팅 자원에 사이트 패키지나 애플리케이션 의존성을 준비하는 단계</li>
</ul>
<h3 id="시스템-구성">시스템 구성</h3>
<ul>
<li><code>Host OS</code>인 <code>Windows 10</code>이 설치된 시스템</li>
<li><a href="https://developer.hashicorp.com/vagrant"><code>https://www.vagrantup.com</code></a>에 접속하면 <code>https://developer.hashicorp.com/vagrant</code>로 리다이렉션 된다.</li>
<li>상단에 있는 <code>Install</code>을 클릭한 후 좌측에서 <code>Windows</code>를 클릭한다.</li>
<li>우측에 있는 <code>Binary download</code> 하단에 있는 <code>AMD64 Version: 2.4.9</code> 옆에 있는 <code>Download</code>를 클릭한다.</li>
<li>다운로드 받은 <code>파일(vagrant_2.4.9_windows_amd64.msi)</code>을 기본값으로 설치한 후 재부팅한다.</li>
</ul>
<hr />
<h2 id="42-vagrant로-provisioning하기">4.2 Vagrant로 Provisioning하기</h2>
<h3 id="개요-1">개요</h3>
<ul>
<li><code>Vargrant</code>로 <code>Provisioning</code>하기 위해서는 <code>스크립트</code>를 작성해야 한다.<h3 id="provisioning을-위한-vagrant-명령어">Provisioning을 위한 Vagrant 명령어</h3>
</li>
<li><code>Provisioning</code>을 위한 예제 스크립트를 생성한다.</li>
</ul>
<pre><code>vagrant init</code></pre><ul>
<li><code>Vagrant</code> 파일을 읽어 들여서 <code>Provisioning</code>을 진행한다. 가상 머신을 생성한다.</li>
</ul>
<pre><code>vagrant up</code></pre><ul>
<li><code>Vagrant</code>에서 다루는 가상 머신들을 삭제한다.</li>
</ul>
<pre><code>vagrant halt</code></pre><ul>
<li><code>Vagrant</code>에서 관리하는 가상 머신들을 삭제한다.</li>
</ul>
<pre><code>vagrant destroy</code></pre><ul>
<li><code>Vagrant</code>에서 관리하는 가상 머신에 SSH로 접속한다.</li>
</ul>
<pre><code>vagrant ssh</code></pre><ul>
<li><code>Vagrant</code>에서 관리하는 가상 머신에 변경된 설정을 적용한다.</li>
</ul>
<pre><code>vagrant provision</code></pre><hr />
<h3 id="작업">작업</h3>
<ul>
<li><p>Step 1. 스크립트 생성</p>
<ul>
<li>폴더<code>D:\3_VMs\HashiCorp\Vagrant</code>생성</li>
<li>실행창에서 경로 이동</li>
<li><code>Vagrant</code> 초기화 명령(<code>init</code>)을 통해서 예제 스크립트 생성<pre><code class="language-bash">E:\3_VMs\HashiCorp&gt;dir
E 드라이브의 볼륨: 새 볼륨
볼륨 일련 번호: 4CCA-9887
</code></pre>
</li>
</ul>
<p>E:\3_VMs\HashiCorp 디렉터리</p>
</li>
</ul>
<p>2025-12-03  오후 01:16    <dir>          .
2025-12-03  오후 01:16    <dir>          ..
2025-12-03  오후 01:16    <dir>          Vagrant
               0개 파일                   0 바이트
               3개 디렉터리  271,741,480,960 바이트 남음</p>
<p>E:\3_VMs\HashiCorp&gt;vagrant init
A <code>Vagrantfile</code> has been placed in this directory. You are now
ready to <code>vagrant up</code> your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
<code>vagrantup.com</code> for more information on using Vagrant.</p>
<p>E:\3_VMs\HashiCorp&gt;type Vagrantfile</p>
<h1 id="---mode-ruby---">-<em>- mode: ruby -</em>-</h1>
<h1 id="vi-set-ftruby-">vi: set ft=ruby :</h1>
<h1 id="all-vagrant-configuration-is-done-below-the-2-in-vagrantconfigure">All Vagrant configuration is done below. The &quot;2&quot; in Vagrant.configure</h1>
<h1 id="configures-the-configuration-version-we-support-older-styles-for">configures the configuration version (we support older styles for</h1>
<h1 id="backwards-compatibility-please-dont-change-it-unless-you-know-what">backwards compatibility). Please don't change it unless you know what</h1>
<h1 id="youre-doing">you're doing.</h1>
<p>Vagrant.configure(&quot;2&quot;) do |config|</p>
<h1 id="the-most-common-configuration-options-are-documented-and-commented-below">The most common configuration options are documented and commented below.</h1>
<h1 id="for-a-complete-reference-please-see-the-online-documentation-at">For a complete reference, please see the online documentation at</h1>
<h1 id="httpsdocsvagrantupcom"><a href="https://docs.vagrantup.com">https://docs.vagrantup.com</a>.</h1>
<h1 id="every-vagrant-development-environment-requires-a-box-you-can-search-for">Every Vagrant development environment requires a box. You can search for</h1>
<h1 id="boxes-at-httpsvagrantcloudcomsearch">boxes at <a href="https://vagrantcloud.com/search">https://vagrantcloud.com/search</a>.</h1>
<p>  config.vm.box = &quot;base&quot;</p>
<h1 id="disable-automatic-box-update-checking-if-you-disable-this-then">Disable automatic box update checking. If you disable this, then</h1>
<h1 id="boxes-will-only-be-checked-for-updates-when-the-user-runs">boxes will only be checked for updates when the user runs</h1>
<h1 id="vagrant-box-outdated-this-is-not-recommended"><code>vagrant box outdated</code>. This is not recommended.</h1>
<h1 id="configvmbox_check_update--false">config.vm.box_check_update = false</h1>
<h1 id="create-a-forwarded-port-mapping-which-allows-access-to-a-specific-port">Create a forwarded port mapping which allows access to a specific port</h1>
<h1 id="within-the-machine-from-a-port-on-the-host-machine-in-the-example-below">within the machine from a port on the host machine. In the example below,</h1>
<h1 id="accessing-localhost8080-will-access-port-80-on-the-guest-machine">accessing &quot;localhost:8080&quot; will access port 80 on the guest machine.</h1>
<h1 id="note-this-will-enable-public-access-to-the-opened-port">NOTE: This will enable public access to the opened port</h1>
<h1 id="configvmnetwork-forwarded_port-guest-80-host-8080">config.vm.network &quot;forwarded_port&quot;, guest: 80, host: 8080</h1>
<h1 id="create-a-forwarded-port-mapping-which-allows-access-to-a-specific-port-1">Create a forwarded port mapping which allows access to a specific port</h1>
<h1 id="within-the-machine-from-a-port-on-the-host-machine-and-only-allow-access">within the machine from a port on the host machine and only allow access</h1>
<h1 id="via-127001-to-disable-public-access">via 127.0.0.1 to disable public access</h1>
<h1 id="configvmnetwork-forwarded_port-guest-80-host-8080-host_ip-127001">config.vm.network &quot;forwarded_port&quot;, guest: 80, host: 8080, host_ip: &quot;127.0.0.1&quot;</h1>
<h1 id="create-a-private-network-which-allows-host-only-access-to-the-machine">Create a private network, which allows host-only access to the machine</h1>
<h1 id="using-a-specific-ip">using a specific IP.</h1>
<h1 id="configvmnetwork-private_network-ip-1921683310">config.vm.network &quot;private_network&quot;, ip: &quot;192.168.33.10&quot;</h1>
<h1 id="create-a-public-network-which-generally-matched-to-bridged-network">Create a public network, which generally matched to bridged network.</h1>
<h1 id="bridged-networks-make-the-machine-appear-as-another-physical-device-on">Bridged networks make the machine appear as another physical device on</h1>
<h1 id="your-network">your network.</h1>
<h1 id="configvmnetwork-public_network">config.vm.network &quot;public_network&quot;</h1>
<h1 id="share-an-additional-folder-to-the-guest-vm-the-first-argument-is">Share an additional folder to the guest VM. The first argument is</h1>
<h1 id="the-path-on-the-host-to-the-actual-folder-the-second-argument-is">the path on the host to the actual folder. The second argument is</h1>
<h1 id="the-path-on-the-guest-to-mount-the-folder-and-the-optional-third">the path on the guest to mount the folder. And the optional third</h1>
<h1 id="argument-is-a-set-of-non-required-options">argument is a set of non-required options.</h1>
<h1 id="configvmsynced_folder-data-vagrant_data">config.vm.synced_folder &quot;../data&quot;, &quot;/vagrant_data&quot;</h1>
<h1 id="disable-the-default-share-of-the-current-code-directory-doing-this">Disable the default share of the current code directory. Doing this</h1>
<h1 id="provides-improved-isolation-between-the-vagrant-box-and-your-host">provides improved isolation between the vagrant box and your host</h1>
<h1 id="by-making-sure-your-vagrantfile-isnt-accessible-to-the-vagrant-box">by making sure your Vagrantfile isn't accessible to the vagrant box.</h1>
<h1 id="if-you-use-this-you-may-want-to-enable-additional-shared-subfolders-as">If you use this you may want to enable additional shared subfolders as</h1>
<h1 id="shown-above">shown above.</h1>
<h1 id="configvmsynced_folder--vagrant-disabled-true">config.vm.synced_folder &quot;.&quot;, &quot;/vagrant&quot;, disabled: true</h1>
<h1 id="provider-specific-configuration-so-you-can-fine-tune-various">Provider-specific configuration so you can fine-tune various</h1>
<h1 id="backing-providers-for-vagrant-these-expose-provider-specific-options">backing providers for Vagrant. These expose provider-specific options.</h1>
<h1 id="example-for-virtualbox">Example for VirtualBox:</h1>
<p>  #</p>
<h1 id="configvmprovider-virtualbox-do-vb">config.vm.provider &quot;virtualbox&quot; do |vb|</h1>
<h1 id="-display-the-virtualbox-gui-when-booting-the-machine"># Display the VirtualBox GUI when booting the machine</h1>
<h1 id="vbgui--true">vb.gui = true</h1>
<p>  #</p>
<h1 id="-customize-the-amount-of-memory-on-the-vm"># Customize the amount of memory on the VM:</h1>
<h1 id="vbmemory--1024">vb.memory = &quot;1024&quot;</h1>
<h1 id="end">end</h1>
<p>  #</p>
<h1 id="view-the-documentation-for-the-provider-you-are-using-for-more">View the documentation for the provider you are using for more</h1>
<h1 id="information-on-available-options">information on available options.</h1>
<h1 id="enable-provisioning-with-a-shell-script-additional-provisioners-such-as">Enable provisioning with a shell script. Additional provisioners such as</h1>
<h1 id="ansible-chef-docker-puppet-and-salt-are-also-available-please-see-the">Ansible, Chef, Docker, Puppet and Salt are also available. Please see the</h1>
<h1 id="documentation-for-more-information-about-their-specific-syntax-and-use">documentation for more information about their specific syntax and use.</h1>
<h1 id="configvmprovision-shell-inline--shell">config.vm.provision &quot;shell&quot;, inline: &lt;&lt;-SHELL</h1>
<h1 id="apt-get-update">apt-get update</h1>
<h1 id="apt-get-install--y-apache2">apt-get install -y apache2</h1>
<h1 id="shell">SHELL</h1>
<p>end</p>
<pre><code>
* Step 2. 가상 머신 생성 1. `OS Image`가 로딩되어 있지 않은 경우

  * (안 나타날 수도 있다)실행 1. `Hype-V` 적용 유무에 따른 오류 ![](https://velog.velcdn.com/images/kyk02405/post/f968d5d0-018e-4c45-88b1-772833e69848/image.png)

  * 실행 2. base 이미지

    * 해당 이미지를 `Vagrant`가 찾지 못해서 발생하는 오류 ![](https://velog.velcdn.com/images/kyk02405/post/319a89b2-94a6-4548-a364-95d4a915ce00/image.png)


* Step 3. 가상 머신 생성 2. `OS Iamge`가 로딩 및 다운로드, 설치가 되어 있는 경우

  * 작업 진행

    * 설치 할 `OS Image`를 선택하기 위해서 `config.vm.box = &quot;base&quot;`에서 `base`에 사용자가 설치할 가상 머신을 기입하면 된다.
    * `Vagrant`에서는 설치할 수 있는 가상 머신들을 사용자들이 올려서 공유할 수 있도록 하는 공간을 제공하고 있다.
    * CentOS를 설치 할 예정이기 때문에 `https://app.vagrantup.com/boxes/search`에서 `centos`를 검색한다
    * `Discover Vagrant Boxes` 하단에 있는 `centos/7`을 확인한다.
  - 실행
    - 3_VMs\HashiCorp\Vagrantfile 파일 수정 ![](https://velog.velcdn.com/images/kyk02405/post/1db41a5f-5a97-442f-9a57-1abe708e68ee/image.png)
    - cmd에서 Vagrant up 명령어 다시 실행

* Step 4. 확인
  - VirtualBox에서 확인 ![](https://velog.velcdn.com/images/kyk02405/post/fc66444f-520d-4dfb-95f0-e4e9180fd6ea/image.png)
  - Vagrant 명령어로 확인 ![](https://velog.velcdn.com/images/kyk02405/post/305b8626-4d56-4400-8024-bb8e49ebcb16/image.png)

### 'Vagrant' 'Guest Additions(게스트 에디션)'을 설치하는 플러그인 설치

- 가상 머신에 게스트 에디션이 설치되어 있지 않아서 포트 포워딩 및 여러 가지 기능이 제공되지 않고 ssh 접속이 되지 않을 수 있다.
- `게스트 에디션(Guest Additions)` 설치 없이 '포트 포워딩'이 잘 되는지 확인
- 플러그인 설치
  - 문법</code></pre><p>vagrant plugin install &lt;패키지 이름&gt;
vagrant plugin uninstall &lt;패키지 이름&gt;
vagrant plugin list</p>
<pre><code>
- `Vagrant` 삭제</code></pre><p>D:\3_VMs\HashiCorp&gt;Vagrant destroy
    default: Are you sure you want to destroy the 'default' VM? [y/N] y
==&gt; default: Forcing shutdown of VM...
==&gt; default: Destroying VM and associated drives...</p>
<p>D:\3_VMs\HashiCorp&gt;</p>
<p>```</p>
<h2 id="52-ansible-server에-ansible-실행-환경-구성하기">5.2 Ansible Server에 Ansible 실행 환경 구성하기</h2>
<h3 id="개요-2">개요</h3>
<ul>
<li>'Vagrant' 파일을 수정해서 자동으로 손쉽게 'Ansible' 서버를 구축하는 방법에 대한 내용을 알아본다. 즉, 'Ansible' 서버가 구동될 수 있는 수준으로 환경을 자동 구성하도록 한다.</li>
</ul>
<h3 id="ansible-server-환경-구성하기">Ansible Server 환경 구성하기</h3>
<ul>
<li><p>구성하기 1. 예제 스크립트 자동 생성</p>
<ul>
<li><p>소스 코드 및 명령어 참고 사이트</p>
<ul>
<li>‘18.04 LTS’ 버전을 설치 완료한 후 ‘20.04.6 LTS’ 버전으로 진행한다.</li>
</ul>
</li>
<li><p>‘Vagrant’로 ‘Provisioning’ 하기 위한 ‘파일(Vagrantfile)’ 생성 및 확인</p>
<ul>
<li><p>코드 입력 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/422f12ed-8723-4406-af25-ee7cb22d1c44/image.png" /></p>
</li>
<li><p>변경사항 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bd1cf13c-3ecf-42ae-b7e8-9747e609c704/image.png" /></p>
<ul>
<li>가상 머신 생성</li>
</ul>
</li>
<li><p>설치 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/69217a27-3e4d-4894-aeb3-eaa590997972/image.png" /></p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li><p>원격 접속</p>
<ul>
<li><p>Step 1. 우분투에 접속 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5442e3a8-0b84-4637-bd97-2504d3f8c7b1/image.png" /></p>
</li>
<li><p>Step 2. 기본 환경 설정</p>
<pre><code class="language-bash"> sudo apt update

 sudo apt upgrade

 cat /etc/issue

 sudo reboot

 sudo do-release-upgrade</code></pre>
</li>
<li><p>Step 3. 모든 테스트를 완료한 후 가상 머신 관련 모든 내용 삭제</p>
</li>
</ul>
</li>
</ul>