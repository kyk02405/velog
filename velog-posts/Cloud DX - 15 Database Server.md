# Cloud DX - 15 Database Server

- 📅 Published: Mon, 20 Oct 2025 08:13:37 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-15-Database-Server)

<hr />
<h1 id="9-database-server">9. Database Server</h1>
<h2 id="개요">개요</h2>
<ul>
<li>로컬 시스템이 아닌 웹에서의 사용자 관련 정보를 저장하는 서버를 말한다.</li>
<li>별도의 환경설정 파일이 없기 때문에 사용자가 모든 설정을 직접 해야만 한다.</li>
<li>웹과 연동되기 때문에 <code>Web Server</code>, <code>FTP server</code>를 함께 설치, 운영한다.</li>
<li>대부분이 사용자 개인 정보가 저장되기 때문에 백업은 필수이다.</li>
<li>(중요)보안 문제 때문에 IP주소를 수시로 변경한다.</li>
<li>(매우 중요) 대부분의 서버들은 <code>네임서버</code>에서 <code>호스트</code>를 부여하지만 DB 서버는 절대 호스트를 부여해서는 안된다. 왜? 서버 시스템을 유출할 수 있기 때문에.</li>
</ul>
<hr />
<h2 id="span-style--colorreddb-server에서의-필수적인-내용span"><span style="color: red;">DB server에서의 필수적인 내용</span></h2>
<h3 id="주요-용어의-크기범위는-다음과-같다">주요 용어의 크기(범위)는 다음과 같다.</h3>
<blockquote>
<p><code>Database</code> &gt; <code>Table</code> &gt; <code>Field(coulmn)</code> &gt; <code>Value</code></p>
</blockquote>
<ul>
<li>모든 명령어 뒤에는 반드시 <code>;</code>를 입력해야 한다. </li>
<li>컴퓨터에서 사용되는 라인(줄)의 끝에 <code>;</code>가 
오는 경우에는 대부분 <code>Enter</code>를 의미한다. 즉, <code>줄바꿈</code>을 하고 해당 <code>Line(줄)</code>을 끝내고 다음 줄로 이동하라는 말이다.</li>
<li><code>;</code>없이 <code>-&gt;</code>가 표시되는데 <code>해당 줄이 계속 이어진다</code>는 말이다. 즉 <code>;</code>이 입력될 때까지 출력되는 라인들은 모두 <code>-&gt;</code>가 나타나고 <code>한 줄</code>로 인식한다.</li>
<li><code>&gt;</code>와 같은 오류가 발생하면 맨 뒤에 <code>;</code>을 입력하면 된다.</li>
<li><span style="color: lightgreen;">(권장)</span> <code>자동 줄바꿈</code>은 가급적 하지 않도록 한다.</li>
</ul>
<hr />
<h2 id="필수-작업">필수 작업</h2>
<ul>
<li>패키지 확인 및 설치 (<code>dnf install mariadb-*</code>)<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8bdf7c37-1523-4baa-a741-df8c10be6f3a/image.png" /><pre><code class="language-bash">cd /etc/yum.repos.d/
touch MariaDB.repo
vi MariaDB.repo
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.11/rhel9-amd64
gpgkey = https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck = 1</code></pre>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="mariadb-초기-설정-mariadb-secure-installation">MariaDB 초기 설정 (mariadb-secure-installation)</h3>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b1e04a89-eafb-4437-b748-2d9c6edde598/image.png" /></li>
</ul>
<hr />
<ul>
<li><p>방화벽(Port, Service)</p>
<ul>
<li>포트(80/tcp), 서비스(httpd[.service])</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d09eb77b-6311-43a4-8023-663d564fc607/image.png" /></li>
</ul>
</li>
<li><p>동작 상태 확인</p>
</li>
<li><p>환경설정 파일 백업</p>
<ul>
<li>/etc/httpd/conf/httpd.conf</li>
</ul>
</li>
</ul>
<hr />
<h2 id="db-server-실행">DB Server 실행</h2>
<ul>
<li>명령<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d4969802-055d-4775-8e1d-7ef403cdbdda/image.png" /></li>
<li><code>초기 비번은 없음</code></li>
</ul>
</li>
<li>실행 <ul>
<li><pre><code class="language-bash"> mysql -u root -p mysql</code></pre>
<ul>
<li>앞에 <code>mysql</code>은 <code>명령어</code></li>
<li>뒤에 <code>mysql</code>은 <code>이름</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="span-style--colororange주-명령어span"><span style="color: orange;">주 명령어</span></h2>
<h3 id="span-style--colorskybluecreatespan"><span style="color: skyblue;">Create</span></h3>
<ul>
<li><code>데이터베이스</code>와 <code>테이블</code> 생성</li>
<li><code>문법</code><ul>
<li><code>데이터베이스 생성</code><pre><code class="language-sql">create database &lt;DATABASE명&gt;</code></pre>
</li>
<li><code>테이블 생성</code>
```sql
create table &lt;TABLE명&gt; &lt;(필드명1)&gt; (타입1) , (필드명2) (타입2), ...&gt;; </li>
</ul>
</li>
<li><code>실습</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e640269a-32e9-4089-bf3e-9b1aaa7a69d8/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/24766a30-1afa-4886-9e6b-0ca47cf87f9b/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="span-style--colorskybluedrop-span"><span style="color: skyblue;">Drop </span></h3>
<ul>
<li><code>데이터베이스</code>와 <code>테이블</code> 삭제</li>
<li><code>문법</code><ul>
<li><code>데이터베이스 생성</code><pre><code class="language-bash">drop database &lt;DATABASE명&gt;</code></pre>
</li>
<li><code>테이블 생성</code><pre><code class="language-sql">drop table &lt;TABLE명&gt; </code></pre>
</li>
</ul>
</li>
<li><code>실습</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4ad2457c-5eab-41e7-880f-c8b0f215cf46/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="span-style--colorskyblueselectspan"><span style="color: skyblue;">Select</span></h3>
<ul>
<li><code>테이블</code>안에 있는 필드의 값을 확인  </li>
<li><code>문법</code> <pre><code class="language-sql">select &lt;FIELD명1&gt;, &lt;FIELD명2&gt; ... from &lt;TABLE명&gt;;
select * from &lt;TABLE명&gt;;</code></pre>
</li>
<li><code>실습</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/343ec792-8057-4704-b2fb-9551f0c538c6/image.png" /><blockquote>
<p><code>mariadb.sys</code>: 시스템 계정으로 내부적으로 사용되는 계정 (일반적으로 로그인 불가)
<code>root</code>: MariaDB의 관리자 계정 (비밀번호가<code>invalid</code>로 표기된 건 암호화 방식이 바뀌었기 때문)
<code>mysql</code>: 내부 서비스용 계정</p>
</blockquote>
</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/486566d0-8a49-45d4-aa65-d448b82fbb8d/image.png" /><blockquote>
<p><code>mysql.db</code> 테이블은 DB별 접근 권한 정보를 저장하는 테이블인데, 지금은 사용자에게 별도로 지정된 <code>데이터베이스</code> 권한이 없어서 빈 결과가 나옴 즉, <code>root</code>, <code>mysql</code>, <code>mariadb.sys</code> 같은 계정에는 현재 DB별 <code>권한 설정(GRANT)</code>이 없는 상태라는 뜻</p>
</blockquote>
</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/99040de6-6337-4fea-a6c5-5fed63e1e15d/image.png" /><blockquote>
<p>CentOS 접속 후 
특정 필드의 값 출력
모든 필드의 값 출력</p>
</blockquote>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="span-style--colorskyblueupdatespan"><span style="color: skyblue;">Update</span></h3>
<ul>
<li><p>테이블 안에 있는 필드의 <code>내용(값)</code>을 갱신</p>
</li>
<li><p><code>password</code> 필드의 경우 반드시 함수 형태로 값을 받아들여야 한다.</p>
</li>
<li><p><code>문법</code></p>
<pre><code class="language-sql">update &lt;TABLE명&gt; set &lt;FIELD명1&gt;=&lt;값1&gt;, &lt;FIELD명2&gt;=&lt;값2&gt;, ... where &lt;조건&gt;;</code></pre>
</li>
<li><p><code>값을 채울 수 있는 공간</code></p>
</li>
<li><p>실습</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/af9fb80d-f45b-4978-9a91-5bfb66584ebb/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="span-style--colorskybluedeletespan"><span style="color: skyblue;">Delete</span></h3>
<ul>
<li>테이블 안에 있는 필드의 <code>내용(값)</code>을 삭제</li>
<li><code>문법</code><pre><code class="language-sql">delete from &lt;TABLE명&gt; `내용(값)`을 삭제</code></pre>
</li>
<li>실습<ul>
<li>익명 접속은 무조건 이 작업을 통해 제거해야 한다.</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4cc51eb2-758c-4859-af34-7fc83d7e2ebb/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="span-style--colorskyblueinsertspan"><span style="color: skyblue;">Insert</span></h3>
<ul>
<li>테이블 안에 있는 필드의 <code>내용(값)</code>을 입력(삽입, 생성)</li>
<li><code>문법</code><pre><code class="language-sql">insert into &lt;TABLE명&gt; (FIELD1, FIELD2, ...) values (VALUE1, VALUE2, ...);
insert into &lt;TABLE명&gt; values (TABLE 안에 있는 FIELD의 갯수);</code></pre>
</li>
<li>실습<ul>
<li>필드의 갯수와 값의 갯수를 따로 입력할 때는 반드시 동일하게 입력해야 한다.</li>
<li>테이블의 모든 필드의 값을 함께 입력 </li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/511c1f37-d63a-4995-ba0d-70ea7193c5c1/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2e180fbc-1497-40d3-823a-cad046fc6e50/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h2 id="span-style--colororange보조-명령어span"><span style="color: orange;">보조 명령어</span></h2>
<h3 id="span-style--colorskyblueshow"><span style="color: skyblue;"><code>Show</code></h3>
<ul>
<li><p><code>데이터베이스</code>와 <code>테이블</code>의 목록을 확인</p>
</li>
<li><p><code>문법</code> </p>
<pre><code class="language-bash">show databases;
show tables;</code></pre>
</li>
<li><p><code>실습</code></p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8c59f625-2078-4dce-8065-9681c6dc790c/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="span-style--colorskyblueuse"><span style="color: skyblue;"><code>Use</code></h3>
<ul>
<li>현재 접속해서 사용하고 있는 데이터베이스 이외의 다른 데이터베이스로 변경</li>
<li>문법<pre><code class="language-bash">user &lt;DATABAES명&gt;;</code></pre>
</li>
</ul>
<hr />
<h3 id="span-style--colorskybluedesc--describe--explain"><span style="color: skyblue;"><code>Desc</code> / <code>Describe</code> / <code>Explain</code></h3>
<ul>
<li><p><code>테이블</code>의 <code>필드 타입</code>을 확인</p>
</li>
<li><p><code>문법</code></p>
<pre><code class="language-bash">desc &lt;TABLE명&gt;;</code></pre>
</li>
<li><p><code>실습</code></p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e455a368-4eb0-4ef5-85e7-b8d9a9e311c7/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h2 id="실습-1-root로-로그인">실습 1. <code>root</code>로 로그인</h2>
<ul>
<li>데몬 재실행 후 로그인<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5bbeee90-e909-4f4b-8995-058b71f6ffe5/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h2 id="실습-2-생성한-사용자-로그인">실습 2. 생성한 사용자 로그인</h2>
<h3 id="오류">오류</h3>
<ul>
<li>Drop을 이용해서 생성한 dbsamadal을 삭제했기 때문에 오류가 발생한다.<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2592b914-bc28-4256-b5f0-041536b26371/image.png" /></li>
<li><code>root</code>로 로그인 후 확인</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/15a3f3cc-fe46-4234-95f1-fbea78d7df2a/image.png" /></li>
</ul>
</li>
</ul>
<h3 id="정상">정상</h3>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fd46e954-b202-4471-aa15-ed9ed384c08d/image.png" /></li>
</ul>
<hr />
<h2 id="실습-3-samadal-관련-내용을-모두-삭제-후-test-관련-내용을-재구성한다">실습 3. 'samadal' 관련 내용을 모두 삭제 후 'test' 관련 내용을 재구성한다.</h2>
<ul>
<li>조건<ul>
<li>DB (dbtest)</li>
<li>User (usertest)</li>
<li>Table (tbtest)</li>
<li>Field (num(int), name(char), addr(char), phone(int))</li>
<li>Values (1개 ~ 2개)<ul>
<li>작업</li>
<li>'samadal' 관련 내용 삭제</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code class="language-sql">   (cent79)# mysql -u root -p mysql
   MariaDB [mysql]&gt; drop database dbsamadal;
   MariaDB [mysql]&gt; delete from user where user='usersamadal';
   MariaDB [mysql]&gt; delete from db where user='usersamadal';
   MariaDB [mysql]&gt; exit
   MariaDB [mysql]&gt; systemctl restart mariadb</code></pre>
<ul>
<li>'test' 관련 내용을 재구성<pre><code class="language-sql"> (cent79)# mysql -u root -p mysql
 MariaDB [mysql]&gt; create database dbtest;
 MariaDB   [mysql]&gt; insert into user (host, user, password)
        values ('localhost', 'usertest', password('pwtest'));
 MariaDB [mysql]&gt; insert into db values ('localhost', 'usertest', 'pwtest',
        'y' 19개);
 MariaDB [mysql]&gt; exit
 (cent79)# systemctl restart mariadb
 (cent79)# mysql -u usertest -p dbtest
 MariaDB [dbtest]&gt; create table tbtest (num int(10), name char(20),
         addr char(60), phone int(16));
 MariaDB [mysql]&gt; insert into tbtest values (1, 'samadal', 'JongNo', '010-1234-5678');
 MariaDB [mysql]&gt; insert into tbtest values (2, 'madal', 'GangNam', '010-4321-8765');</code></pre>
</li>
</ul>
<hr />
<h2 id="실습-4-test-삭제-이후-samadal-재생성">실습 4. test 삭제 이후 samadal 재생성</h2>