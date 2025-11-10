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
<li><a href="https://dev.mysql.com/downloads/mysql/">MySQL</a></li>
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