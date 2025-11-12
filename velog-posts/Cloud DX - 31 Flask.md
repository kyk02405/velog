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
hint: See PEP 668 for the detailed specification.</p>
<pre><code>- `Pip`를 사용해서 `Flask` 설치 2. 오류 (허가 거부)
```bash
(flaskenv) samadal@CloudDX:/sdb/flask_project$ pip install flask --no-user
Collecting flask
  Downloading flask-3.1.2-py3-none-any.whl.metadata (3.2 kB)
Collecting blinker&gt;=1.9.0 (from flask)
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click&gt;=8.1.3 (from flask)
  Downloading click-8.3.0-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous&gt;=2.2.0 (from flask)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2&gt;=3.1.2 (from flask)
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe&gt;=2.1.1 (from flask)
  Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Collecting werkzeug&gt;=3.1.0 (from flask)
  Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Downloading flask-3.1.2-py3-none-any.whl (103 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.3/103.3 kB 7.0 MB/s eta 0:00:00
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading click-8.3.0-py3-none-any.whl (107 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 107.3/107.3 kB 19.7 MB/s eta 0:00:00
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.9/134.9 kB 22.8 MB/s eta 0:00:00
Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 224.5/224.5 kB 20.1 MB/s eta 0:00:00
Installing collected packages: markupsafe, itsdangerous, click, blinker, werkzeug, jinja2, flask
ERROR: Could not install packages due to an OSError: [Errno 13] 허가 거부: '/sdb/flask_project/flaskenv/lib/python3.12/site-packages/markupsafe'
Check the permissions.</code></pre><ul>
<li><code>Pip</code>를 사용해서 Flask 설치 3. 정상<ul>
<li>(매우 중요한 내용) <code>flash_projetc</code> 디렉토리와 이 디렉토리 하위에 <code>python3 -m venv flaskenv</code> 명령으로 생성된 <code>flask</code> 디렉토리의 소유권은 <code>root</code>가 되어서는 안된다. </li>
<li>소유권 변경<pre><code class="language-bash">(flaskenv) samadal@CloudDX:/sdb/flask_project$ pwd
/sdb/flask_project
(flaskenv) samadal@CloudDX:/sdb/flask_project$ ls -l
합계 4
drwxr-xr-x 5 root root 4096 11월 11 15:07 flaskenv
(flaskenv) samadal@CloudDX:/sdb/flask_project$ cd /sdb
(flaskenv) samadal@CloudDX:/sdb$ ls -l
합계 20
drwxr-xr-x 3 root root  4096 11월 11 15:07 flask_project
drwx------ 2 root root 16384 11월 11 14:17 lost+found
(flaskenv) samadal@CloudDX:/sdb$ sudo rm -rf lost+found/
[sudo] samadal 암호:
(flaskenv) samadal@CloudDX:/sdb$ ls -l
합계 4
drwxr-xr-x 3 root root 4096 11월 11 15:07 flask_project
(flaskenv) samadal@CloudDX:/sdb$ sudo chown samadal: flask_project/
(flaskenv) samadal@CloudDX:/sdb$ ls -l
합계 4
drwxr-xr-x 3 samadal samadal 4096 11월 11 15:07 flask_project
(flaskenv) samadal@CloudDX:/sdb$</code></pre>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="flask-applition-만들기-1-터미널에서-바로-출력">Flask Applition 만들기 1. 터미널에서 바로 출력</h3>
<ul>
<li><p>가상 환경으로 들어간 후 <code>pybo.py</code>파일 생성</p>
<ul>
<li><p>가상 환경으로 들어간 후 파일을 생성한다.</p>
<pre><code class="language-bash">(flaskenv) samadal@CloudDX:/sdb/flask_project$ vi pybo.py
(flaskenv) samadal@CloudDX:/sdb/flask_project$ nl pybo.py
 1  from flask import Flask

 2  # 'Flask(Flask) 애플리케이션'을 생성하는 부분이다.
 3
 4  # 이 코드는 'Flask(Flask) 애플리케이션'을 초기화하고 구성하는 역할을 한다.

 5  app = Flask(__name__)

 6  @app.route('/')

 7  def hello_pycloud(): return 'Hello, Python Cloud!'</code></pre>
</li>
</ul>
</li>
<li><p><code>Flask</code> 실행</p>
<ul>
<li><p><code>오류 1.</code> </p>
<ul>
<li><code>오류</code>의 원인<ul>
<li><code>Flask</code>는 기본적으로 <code>app.py</code>를 실행하도록 구성되어 있기 때문이다. </li>
<li>따라서 <code>pybo.py</code>를 <code>app.py</code>로 변경하거나 
<code>FLASK_APP 환경 변수</code>를 <code>pybo.py</code>로 변경하면 된다. </li>
</ul>
</li>
<li><code>실행</code>(오류)</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6ba3c70c-bbfa-41c1-a668-73c11cac58c7/image.png" /></li>
</ul>
</li>
<li><p><code>오류 2.</code></p>
<ul>
<li><code>수정</code><ul>
<li><code>FLASK_APP 환경변수</code>를 <code>set FLASK_APP= 파일명</code>과 같이 변경하면 된다.</li>
<li>이 때 확장자는 반드시 생략한다.</li>
</ul>
</li>
<li><code>실행</code>(오류)</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/be000b5a-984c-4c35-93d7-93462d587f6e/image.png" /></li>
</ul>
</li>
<li><p><code>정상</code></p>
<ul>
<li><code>수정</code><ul>
<li>파일명을 <code>pybo.py</code>에서 <code>app.py</code>로 변경한다.</li>
<li><code>mv pybo.py app.py</code><pre><code class="language-bash">from flask import Flask
</code></pre>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>app = Flask(<strong>name</strong>)</p>
<p>@app.route('/')
def hello_pycloud():
    return 'Hello, Python Cloud!'</p>
<p>if <strong>name</strong> == '<strong>main</strong>':
    app.run(host='0.0.0.0', port=5000)</p>
<pre><code>
![](https://velog.velcdn.com/images/kyk02405/post/2528a808-9a50-456b-a8fe-487fcc17f4fb/image.png)


---
### Flask Applition 만들기 2. 사이트에서 출력
- 작업 개요
  - `CentOS`를 `DNS`로 롤백하고 로딩한 후 네임서버(gusiya.com)를 구축하고 `Ubuntu`에 호스트(ubuntu)를 부여한다.
  - `IP Address` 변경
    - `Ubuntu` (192.168.10.140 / C Class / 192.168.10.2 / 192,168,10,141)
    - `CentOS` (192.168.10.141 / C Class / 192.168.10.2 / 192,168,10,141)    
  - `Ubuntu`에서 네임서버 조회

  - 방화벽을 통해 포트 (5000) 추가
```bash
(flaskenv) samadal@CloudDX:/sdb/flask_project$ sudo ufw allow 5000/tcp
(flaskenv) samadal@CloudDX:/sdb/flask_project$ sudo ufw enable
(flaskenv) samadal@CloudDX:/sdb/flask_project$ sudo ufw reload</code></pre><ul>
<li><p>화면 출력 시 일반적으로 나타나는 유형</p>
<pre><code class="language-bash">(flaskenv) samadal@CloudDX:/sdb/flask_project$ python3 app.py</code></pre>
<ul>
<li><code>HTTP Request (GET/HTTP/1.1)</code></li>
<li><code>HTTP Response (HTTP/1.1 200 ok)</code></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cb69126c-68cf-4352-a689-5da82e6ceed3/image.png" /></li>
</ul>
</li>
<li><p>테스트 1. IP로 입력 후 사이트 출력</p>
</li>
<li><p>테스트 2. 도메인을 입력 후 사이트 출력</p>
</li>
<li><p>테스트 3. Site Redirection</p>
<ul>
<li><code>CentOS</code>에서 <code>Web Server</code>를 활성화 시킨 후 기본경로에 <code>index.html</code>을 생성한다</li>
<li>생성한 문서 안에 임의의 시간 설정에 따른 <code>Ubuntu</code>로 이동할 수 있게끔 설정<pre><code class="language-bash"># vi /var/www/html/index.html
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;ko&quot;&gt;
&lt;head&gt;
&lt;meta charset=&quot;UTF=8&quot;&gt;
&lt;title&gt;Site Redirection Test&lt;/title&gt;
&lt;meta http-equiv=&quot;refresh&quot; content=&quot;5; url=http://ubuntu.gusiya.com:5000&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;p&gt;move&lt;a href=&quot;http://ubuntu.gusiya.com:5000&quot;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
</li>
</ul>
</li>
</ul>