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
<h3 id="step-1-flask-프로젝트-환경설정">Step 1. Flask 프로젝트 환경설정</h3>
<ul>
<li><p>개요</p>
<ul>
<li><code>Pip</code>를 사용해서 <code>ubuntu</code> <code>python 패키지</code>로 <code>Flask</code>를 설치할 수 있다.</li>
<li><code>Python</code>과 <code>Pip</code>는 <code>Ubuntu</code>에 기본적으로 설치가 되어 있으며, <code>Flask</code>는 모든 활성 버전에서 작동한다.</li>
<li>이제 설치된 <code>Python</code> 버전을 확인하고 <code>서버(Ubuntu 시스템)</code>에 새 가상 환경을 만들도록 한다.</li>
</ul>
</li>
<li><p>시스템 구성</p>
<ul>
<li><code>IP</code>는 <code>192.168.10.140</code>로 설정한다.</li>
<li>프로젝트 설치를 위한 저장소(16GB)를 추가한다.</li>
<li>자동 마운트</li>
</ul>
</li>
<li><p>패키지 업데이트 </p>
</li>
<li><p>설치되어 있는 <code>Python</code> 및 <code>Pip</code>버전 확인</p>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo python3 -V
samadal@CloudDX:~$ sudo pip -V</code></pre>
</li>
<li><p>패키지가 설치되어 있지 않은 경우</p>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo apt install -y python3-pip python3</code></pre>
</li>
<li><p>Python <code>가상 환경 모듈(Virtual Enviorment Module)</code> 설치</p>
</li>
<li><p><code>Flash Project</code>를 위한 디렉토리 생성</p>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo mkdir /sdb/flask_project
samadal@CloudDX:~$ cd /sdb/flask_project</code></pre>
</li>
<li><p>flaskenv 명령을 이용한 신규 가상 환경 생성</p>
<ul>
<li><code>flaskenv 서버</code>에 <code>Python Package</code>를 설치하고 관리하는 환경을 생성한다.<pre><code class="language-bash">samadal@CloudDX:/sdb/flask_project$ sudo python3 -m venv flaskenv</code></pre>
</li>
</ul>
</li>
<li><p>소유권 확인 (모든 파일이 내용이 모두 <code>root</code>로 되어 있다.</p>
<pre><code class="language-bash">samadal@CloudDX:/sdb/flask_project/flaskenv/bin$ ls -l
합계 36
-rw-r--r-- 1 root root 9033 11월 11 15:07 Activate.ps1
-rw-r--r-- 1 root root 2050 11월 11 15:07 activate
-rw-r--r-- 1 root root  931 11월 11 15:07 activate.csh
-rw-r--r-- 1 root root 2206 11월 11 15:07 activate.fish
-rwxr-xr-x 1 root root  244 11월 11 15:07 pip
-rwxr-xr-x 1 root root  244 11월 11 15:07 pip3
-rwxr-xr-x 1 root root  244 11월 11 15:07 pip3.12
lrwxrwxrwx 1 root root    7 11월 11 15:07 python -&gt; python3
lrwxrwxrwx 1 root root   16 11월 11 15:07 python3 -&gt; /usr/bin/python3
lrwxrwxrwx 1 root root    7 11월 11 15:07 python3.12 -&gt; python3</code></pre>
</li>
<li><p><code>flask</code> 가상 환경을 활성화 한 후 프롬프트가 <code>Flask 가상 환경</code>으로 변경되었는지 확인한다.</p>
<pre><code class="language-bash">samadal@CloudDX:/sdb/flask_project$
samadal@CloudDX:/sdb/flask_project$ source flaskenv/bin/activate
(flaskenv) samadal@CloudDX:/sdb/flask_project$ deactivate
samadal@CloudDX:/sdb/flask_project$</code></pre>
</li>
</ul>
<hr />
<h3 id="step-2-ubuntu-서버의-활성-flaskenv-가상-환경에-flask를-설치">Step 2. Ubuntu 서버의 활성 Flaskenv 가상 환경에 Flask를 설치</h3>
<ul>
<li><code>Pip</code>를 사용해서 <code>Flask</code> 설치 1. 오류 (가상환경이 아니어서 오류)<pre><code class="language-bash">samadal@CloudDX:~$ pip install flask
error: externally-managed-environment
</code></pre>
</li>
</ul>
<p>× This environment is externally managed
╰─&gt; To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.</p>
<pre><code>If you wish to install a non-Debian-packaged Python package,
create a virtual environment using python3 -m venv path/to/venv.
Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
sure you have python3-full installed.

If you wish to install a non-Debian packaged Python application,
it may be easiest to use pipx install xyz, which will manage a
virtual environment for you. Make sure you have pipx installed.

See /usr/share/doc/python3.12/README.venv for more information.</code></pre><p>note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```</p>