# Cloud DX - 31 Flask

- 📅 Published: Tue, 11 Nov 2025 03:56:39 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-31-Flask)

<hr />
<h1 id="flask">Flask</h1>
<h2 id="개요">개요</h2>
<ul>
<li><p><code>Ubuntu 24.04.2</code>에 <code>Flask</code>를 설치하여 가볍고 오픈 소스인 <code>Python 프레임워크</code>로 최신 '웹 애플리케이션'을 만든다.</p>
</li>
<li><p><code>Flash</code>는 <code>Python</code>으로 작성된 <code>Micro Web Framework</code>(마이크로 웹 프레임워크)이며 그 중에서 <code>Micro Framework(마이크로 프레임워크)</code>로 분류된다.</p>
</li>
<li><p>Micro Framework(마이크로 프레임워크)'는 사용자가 필요로 하는 기능만 뽑아서 만들고자 하는 형태로 확장하는 것을 의미한다.</p>
</li>
<li><p><code>Flask</code>는 단순성, 유연성, 방대한 문서로 인해 개발자들 사이에서 <code>Python</code>을 사용해 <code>Web pplication(웹 애플리케이션)</code>과 <code>API(Application Programming Interface)</code>를 구축하는 데 널리 사용되고 있다.</p>
</li>
<li><p><code>Python</code>으로 작성한 내용의 결과를 웹 서버로 나타내기 위해 <code>Flask</code>를 통해 간단한 <code>API 서버</code>를 만들어 배포한다.</p>
</li>
</ul>
<h2 id="가상환경">가상환경</h2>
<h3 id="개요-1">개요</h3>
<ul>
<li><p><code>Python 가상 환경</code>은 자체 라이브러리 및 종속성 세트와 함께 특정 Python 설치가 포함된 독립된 디렉토리이다.</p>
</li>
<li><p>이를 통해 서로 간섭하지 않고 각각 고유한 버전의 <code>Python</code>과 설치된 패키지가 있는 서로 다른 프로젝트에 대해 격리된 환경을 만들 수 있다.</p>
</li>
</ul>
<h3 id="작업-환경-구성">작업 환경 구성</h3>
<ul>
<li><code>OS (ubuntu 24.04.3)</code></li>
<li><code>개발환경 (MS Visual Studio Code)</code></li>
</ul>
<h3 id="ubuntu-24043-가상-환경에-flask-설치">ubuntu 24.04.3 가상 환경에 Flask 설치</h3>
<ul>
<li>Step 1. Flask 프로젝트 환경설정<ul>
<li>개요<ul>
<li><code>Pip</code>를 사용해서 <code>ubuntu</code> <code>python 패키지</code>로 <code>Flask</code>를 설치할 수 있다.</li>
<li><code>Python</code>과 <code>Pip</code>는 <code>Ubuntu</code>에 기본적으로 설치가 되어 있으며, <code>Flask</code>는 모든 활성 버전에서 작동한다.</li>
<li>이제 설치된 <code>Python</code> 버전을 확인하고 <code>서버(Ubuntu 시스템)</code>에 새 가상 환경을 만들도록 한다.</li>
</ul>
</li>
<li>시스템 구성<ul>
<li><code>IP</code>는 <code>192.168.10.140</code>로 설정한다.</li>
<li>프로젝트 설치를 위한 저장소(16GB)를 추가한다.</li>
<li>자동 마운트</li>
</ul>
</li>
</ul>
</li>
</ul>