# Cloud DX - 53 Vagrant를 이용한 Ansible 서버 관리 자동화

- 📅 Published: Wed, 03 Dec 2025 04:06:46 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-53-Vagrant%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-Ansible-%EC%84%9C%EB%B2%84-%EA%B4%80%EB%A6%AC-%EC%9E%90%EB%8F%99%ED%99%94)

<h1 id="04-vagrant를-이용한-ansible-서버-관리-자동화">04. Vagrant를 이용한 Ansible 서버 관리 자동화</h1>
<h2 id="41-실습-환경-구성">4.1 실습 환경 구성</h2>
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
</ul>
<h3 id="작업">작업</h3>
<ul>
<li>Step 1. 스크립트 생성<ul>
<li>폴더<code>D:\3_VMs\HashiCorp\Vagrant</code>생성</li>
<li>실행창에서 경로 이동</li>
</ul>
</li>
</ul>