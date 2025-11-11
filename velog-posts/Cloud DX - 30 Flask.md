# Cloud DX - 30 Flask

- 📅 Published: Mon, 10 Nov 2025 09:29:07 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-30-Flask)

<hr />
<h1 id="16-flask-web-application과-database">16. Flask Web Application과 Database</h1>
<h2 id="sql-실습-환경-구성">SQL 실습 환경 구성</h2>
<h3 id="mysql-설치">MySQL 설치</h3>
<ul>
<li>시스템 구성</li>
<li><code>Guest OS</code> (Windows 10)에서 작업 한다.</li>
<li><code>RAM</code>(8192), HDD(128GB)</li>
<li>사용되는 리눅스는 <code>CentOS</code>를 사용한다. </li>
</ul>
<h3 id="다운로드">다운로드</h3>
<ul>
<li><a href="https://dev.mysql.com/downloads/mysql/">MySQL</a> &lt;-</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/49973647-cfaa-4f1b-b248-ca78e8ae6f21/image.png" /></li>
</ul>
<h3 id="설치">설치</h3>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3f06c2cb-c781-4c02-b9c2-9a6d6b633187/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6569992e-71bf-46a2-994f-b4af2054158f/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1b284aef-4be2-47aa-9e4e-c59a83c78365/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/314c70f2-73e8-4e83-ad20-7800c08f0dad/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a100cebd-7a13-415d-80a0-9e9465fc5ef7/image.png" /></li>
</ul>
<h3 id="작동-여부-확인">작동 여부 확인</h3>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f652e6c1-7d12-4784-8411-6be3565b8403/image.png" /></li>
<li>데몬 서비스 동작 확인<h3 id="접속-테스트">접속 테스트</h3>
</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/334c17d1-dac8-4928-81e0-fabf9294f48a/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c72ea176-d355-4f9e-bd5b-aeec6f323bb3/image.png" /></li>
</ul>
<h3 id="환경-변수-추가">환경 변수 추가</h3>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4b33990e-5af9-47fc-9cb6-b3ae8027174e/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/281367cf-4b23-4ab5-976c-fd53f1ba4e2f/image.png" /></li>
</ul>
<hr />
<h2 id="mysql-workbench-워크벤치">MySQL Workbench (워크벤치)</h2>
<h3 id="개요">개요</h3>
<ul>
<li><code>MySQL</code> 공식 관리 도구를 말한다. </li>
</ul>
<h3 id="다운로드-및-설치">다운로드 및 설치</h3>
<h3 id="실행-테스트">실행 테스트</h3>
<ul>
<li>설치 후 프로그램이 자동 실행되면 첫 화면 좌측에 <code>root</code> 계정으로 자동 로그인이 된 상태로 나타난다. (<code>root</code> / <code>localhost:3306</code>)</li>
<li>이 영역을 <code>더블 클릭</code>하면 <code>Connect to MySQL Server</code>라는 작은 창이 나타나는데 <code>비밀번호(doitmysql)</code>를 입력한다. 이 때 하단의 <code>Save password in vault</code>를 체크한다.  <ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e789393b-369f-4744-b8c7-d9dc8ee3d5d6/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/68ea502b-7b51-44e8-a8af-56ff5c2c4e07/image.png" /></li>
</ul>
</li>
</ul>
<p>  현재 접속 정보는 <code>MySQL@localhost:3306</code> / <code>root</code> / <code>doitmysql</code>이다.</p>
<ul>
<li><code>MySQL Workbench</code> 창이 출력되는데 하단에 있는 <code>Don't show this message again</code>을 체크한 후 <code>Continue Anyway</code>를 클릭한다.</li>
<li><code>MySQL Workbench</code> 창이 출력되면서 <code>Local Instance MySQL</code> 큰 탭이 출력되고 하단에 다양한 모양의 <code>서브 창</code>들이 나타난 것을 볼 수 있다.</li>
</ul>
<h3 id="테스트">테스트</h3>
<ul>
<li>중앙에 보면 <code>Query 1</code>이라는 탭이 있는데 하단에 <code>select @@hostname;</code>을 입력한다.</li>
<li>바로 위에 아이콘 중에서 <code>첫 번 째 번개</code>인 <code>Execute the selected ...</code> 아이콘을 클릭한다. </li>
<li>하단에 있는 영역에 결과가 출력되는 것을 확인할 수 있다.</li>
</ul>
<hr />
<h2 id="mysql-workbench-워크벤치-사용법">MySQL Workbench (워크벤치) 사용법</h2>
<h3 id="실습-1-mysql-workbench와-cmd에서의-비교">실습 1. MySQL Workbench와 cmd에서의 비교</h3>
<ul>
<li><p><code>MySQL Workbench</code></p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3eb6c963-5e88-4f8c-9ef1-07b6f871e145/image.png" /></li>
</ul>
</li>
<li><p><code>cmd</code></p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7bc5ed28-f970-4661-9eab-020b6677c41b/image.png" /></li>
</ul>
</li>
</ul>
<blockquote>
<p><code>GUI</code>기반 이냐, <code>CLI</code>기반이냐의 차이만 있을 뿐이다.</p>
</blockquote>
<hr />
<h3 id="실습-2-workbench에서-dbsamadal이라는-db를-생성하고-cmd창에서-확인한다">실습 2. Workbench에서 dbsamadal이라는 DB를 생성하고 cmd창에서 확인한다.</h3>
<ul>
<li>Database 생성<pre><code class="language-sql">(work) create database dbsamadal;
(cmd) mysql -u root -p mysql
(cmd) show databases;</code></pre>
</li>
<li>사용자 생성 1. 오류 <ul>
<li>개요 <ul>
<li><code>cmd</code>창에서 사용자를 생성하고 <code>Workbench</code>에서 확인한다.</li>
<li><code>Mariadb</code>에서는 다음과 같이 생성했었다.<pre><code class="language-sql">(mariadb) insert into user (host, user, password) values ('localhost', 'usersamadal', password('pwsamadal'));</code></pre>
</li>
</ul>
</li>
<li>(중요) <code>MySQL</code>에서는 <code>password</code> 필드가 없기 때문에 MariaDB와 같이 생성 할 수가 없다.<pre><code class="language-sql">(cmd) show tables;
(cmd) desc user;</code></pre>
</li>
<li>(실제 생성 명령) 따라서 <code>grant</code> 명령을 이용해서 생성해줘야 한다.</li>
</ul>
</li>
<li>사용자 생성 2. 생성</li>
<li>(중요) <code>MySQL</code>에서는 <code>password</code> 필드가 없기 때문에 명령 입력 시 오류가 발생한다.<pre><code class="language-sql">mysql&gt; grant all on dbsamadal.* to usersamadal@'localhost' identified by 'pwsamadal';
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'identified by 'pwsamadal'' at line 1</code></pre>
</li>
</ul>
<pre><code class="language-sql">mysql&gt; grant all privileges on dbsamadal.* to usersamadal@'localhost';
ERROR 1410 (42000): You are not allowed to create a user with GRANT</code></pre>
<ul>
<li><code>MySQL</code>에서는 사용자를 먼저 생성하고 <code>DB</code>와 연결 해야한다.</li>
<li>생성된 사용자를 확인한다.<pre><code class="language-sql">mysql&gt; SELECT host, user FROM user;
+-----------+------------------+
| host      | user             |
+-----------+------------------+
| localhost | mysql.infoschema |
| localhost | mysql.session    |
| localhost | mysql.sys        |
| localhost | root             |
| localhost | usersamadal      |
+-----------+------------------+
5 rows in set (0.00 sec)</code></pre>
<ul>
<li>생성된 사용자에게 모든 명령어를 실행할 수 있는 권한을 부여한다.</li>
</ul>
</li>
<li>권한 부여</li>
<li>사용자를 생성하고 권한을 부여하면 <code>user</code> 테이블 뿐만 아니라 <code>db</code> 테이블에도 자동 생성된다.</li>
<li><code>MariaDB</code> 수업할 때 했던 내용을 참고하면, <code>grant</code> 명령으로 사용자를 생성하면 <code>user</code> 테이블에 사용자가 생성되고 <code>db</code> 테이블에는 사용자와 사용자가 사용할 DB가 자동 연동된다.<pre><code class="language-sql">FLUSH PRIVILEGES;</code></pre>
</li>
</ul>
<hr />
<h3 id="실습-3-databased-backup--restore">실습 3. Databased Backup &amp; Restore</h3>
<h4 id="database-backup"><code>Database Backup</code></h4>
<ul>
<li>백업 명령어 작동 유무 확인<pre><code class="language-cmd">C:\&gt;mysqldump
Usage: mysqldump [OPTIONS] database [tables]
OR     mysqldump [OPTIONS] --databases [OPTIONS] DB1 [DB2 DB3...]
OR     mysqldump [OPTIONS] --all-databases [OPTIONS]
For more options, use mysqldump --help</code></pre>
</li>
</ul>
<ul>
<li><code>DB</code> 전체 백업</li>
</ul>
<pre><code class="language-cmd">C:\&gt;mysqldump -u root -p --all-databases &gt; e:\full.sql</code></pre>
<ul>
<li><p>원하는 <code>DB</code>만 백업</p>
<pre><code class="language-cmd">C:\&gt;mysqldump -u root -p mysql &gt; e:\omysql.sql</code></pre>
</li>
<li><p>테이블만 백업</p>
<pre><code>C:\&gt;mysqldump -u root -p mysql user &gt; e:\tbbackup.sql</code></pre></li>
<li><p>테이블 구조만 백업</p>
<pre><code>C:\&gt;mysqldump -u root -p --no-data mysql user &gt; e:\nodata.sql</code></pre></li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e0621c81-3462-493c-9b59-b2794819708e/image.png" /></p>
</li>
</ul>
<hr />
<h4 id="database-restore"><code>Database Restore</code></h4>
<ul>
<li>원하는 <code>DB</code>만 복구<pre><code>E:\&gt;mysql -u root -p mysql &lt; e:\full.sql</code></pre></li>
<li>작업 중인 <code>DB</code>에 변화를 준 백업한 내용 복구<pre><code class="language-sql">mysql&gt; create table tbsamadal (num int(10), name char(20), addr char(80));
</code></pre>
</li>
</ul>
<p>mysql&gt; show tables;
+------------------------------------------------------+
| Tables_in_mysql                                      |
+------------------------------------------------------+
| columns_priv                                         |
...
| tbsamadal                                            |
...
+------------------------------------------------------+
39 rows in set (0.00 sec)</p>
<p>mysql&gt; flush privileges;</p>
<p>mysql&gt; exit</p>
<p>E:&gt;mysql -u root -p mysql &lt; e:\full.sql</p>
<p>mysql&gt; show tables;</p>
<h1 id="테이블-변화-없음">테이블 변화 없음</h1>
<p>mysql&gt; show databases;
+--------------------+
| Database           |
+--------------------+
| dbsamadal          |
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| world              |
+--------------------+
7 rows in set (0.00 sec)</p>
<p>mysql&gt; drop database dbsamadal;</p>
<p>mysql&gt; show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| world              |
+--------------------+
6 rows in set (0.00 sec)</p>
<p>mysql&gt; flush privileges;</p>
<p>mysql&gt; exit</p>
<p>E:&gt;mysql -u root -p mysql &lt; e:\full.sql</p>
<p>E:&gt;mysql -u root -p mysql</p>
<p>mysql&gt; show databases;
+--------------------+
| Database           |
+--------------------+
| dbsamadal          |
| information_schema |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| world              |
+--------------------+
7 rows in set (0.00 sec)</p>
<pre><code>```bash
(server-129) mysqldump -u root -p mysql &gt; /export/home/samadal/full.sql

(server-129) scp /export/home/samadal/full.sql samadal@192.168.10.131:/dbback/ </code></pre><hr />
<h1 id="flask">Flask</h1>
<h2 id="개요-1">개요</h2>
<ul>
<li>'Ubuntu 24.04.2'에 'Flask'를 설치하여 가볍고 오픈 소스인 'Python 프레임워크'로 최신 '웹 애플리케이션'을 만든다.</li>
</ul>