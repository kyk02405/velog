# Cloud DX - 54 Git

- 📅 Published: Thu, 04 Dec 2025 07:41:11 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-54-Git)

<h1 id="22-git">22. Git</h1>
<h2 id="221-개요">22.1 개요</h2>
<ul>
<li><p><code>깃</code>은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 <code>분산 버전 관리 시스템</code>을 말한다.</p>
</li>
<li><p><code>소프트웨어 개발에서 소스 코드 관리(주목적)</code>에 주로 사용되지만 어떠한 집합의 파일의 변경사항을 지속적으로 추적하기 위해 사용될 수 있다.</p>
</li>
<li><p>기하학적 불변 이론을 바탕으로 설계됐고, 분산 버전 관리 시스템으로서 빠른 수행 속도에 중점을 두고 있는 것이 특징이며 데이터 무결성, 분산, 비선형 워크플로를 지원한다.</p>
</li>
<li><p><code>깃</code>은 2005년에 리눅스 커널 개발을 위해 초기 개발에 기여한 다른 커널 개발자들과 함께 2005년에 <code>리누스 토르발스</code>가 처음 개발한 것이다.</p>
</li>
<li><p>2005년부터 지금까지 <code>주니오 하마노(Junio Hamano)</code>가 소프트웨어의 유지보수를 맡고 있다.</p>
</li>
<li><p>다른 대부분의 분산 버전 관리 시스템처럼, 또 대부분의 클라이언트-서버 시스템과 달리, 모든 노드의 모든 깃 디렉터리는 네트워크 접속이나 중앙 서버와는 독립적으로 동작하는 완전한 이력 및 완전한 버전 추적 기능을 갖춘 성숙한 저장소이다.</p>
</li>
<li><p><code>깃</code>은 <code>GNU 일반 공중 사용 허가서 v2</code> 하에 배포되는 자유 소프트웨어이다.</p>
</li>
</ul>
<h2 id="222-환경-구성-및-다운로드-설치">22.2 환경 구성 및 다운로드, 설치</h2>
<ul>
<li>작업 환경</li>
<li><code>git</code> 다운로드</li>
<li>설치</li>
<li>확인</li>
</ul>
<hr />
<h2 id="223-github">22.3 Github</h2>
<ul>
<li><p>회원 가입 및 로그인</p>
</li>
<li><p>저장소 확인</p>
</li>
<li><p>저장소 생성 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9e2dc149-d5e5-4d53-b9c1-a07f1bbc5eb7/image.png" /></p>
</li>
<li><p>저장소 삭제</p>
</li>
</ul>
<hr />
<h3 id="github의-저장소를-로컬-시스템으로-인식시키기"><code>github</code>의 저장소를 로컬 시스템으로 인식시키기</h3>
<pre><code class="language-bash">Administrator@Win1022H2 MINGW64 /e/CLOUD
$ git config --global user.name &quot;kyk02405&quot;

Administrator@Win1022H2 MINGW64 /e/CLOUD
$ git config --global user.email &quot;kyk02405@gmail.com&quot;</code></pre>
<ul>
<li><code>Adminstrator</code> -&gt; 호스트 OS에 로그인 한 사용자 명</li>
<li><code>@Win1022H2 MINGW64</code> -&gt; 호스트 OS의 컴퓨터 이름</li>
<li><code>/e/CLOUD</code> -&gt; <code>github</code>와 연결된 통로</li>
</ul>
<hr />
<h3 id="github에-있는-저장소-불러오기"><code>github</code>에 있는 저장소 불러오기</h3>
<p><code>E:CLOUD</code> 생성 후 우클릭 디렉토리 안에서 <code>Git bash here</code> 실행</p>
<pre><code class="language-bash">$ git clone https://github.com/kyk02405/cloudgit
Cloning into 'cloudgit'...
warning: You appear to have cloned an empty repository.</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/53f994f4-2e57-4e9d-9c1a-c7ba019d53fb/image.png" /></p>
<hr />
<h3 id="파일-작업-생성-수정-삭제-등-후-스테이징-영역으로-이동시키기">파일 작업 (생성, 수정, 삭제 등) 후 스테이징 영역으로 이동시키기</h3>
<ul>
<li><p><code>Commit</code>할 로컬 시스템의 상태 확인</p>
<ul>
<li><p><code>Commit</code>은 작업한 내용을 저장소에 기록하는 명령어이다.</p>
</li>
<li><p>명령 실행 전 사전 작업</p>
<ul>
<li><code>E:\CLOUD\cloudgit</code> 으로 이동 후 임의의 내용(문서 파일, 실행 파일 등) 추가한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e608dee4-ced3-4f5e-97e3-b287d79f3177/image.png" /></li>
<li>문서 파일은 임의의 내용으로 채운 <code>samadal.txt</code>로 만든다.</li>
<li>실행 파일은 <code>C:\Windows</code>에 있는 <code>HelpPane.exe</code>를 복사한다.</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/252b6791-cad3-4bf4-a937-977780569045/image.png" /></li>
</ul>
</li>
<li><p>명령 실행</p>
</li>
</ul>
</li>
<li><p>작업한 대상들을 스테이징<code>(E:\CLOUD\cloudgit)</code> 영역으로 이동 시키기</p>
<ul>
<li>개요<ul>
<li><code>git add</code> 명령을 통해 <code>Untracked files</code>을 모두 스테이징 영역으로 이동시킨다.</li>
</ul>
</li>
<li>명령 실행<pre><code class="language-bash">Administrator@Win1022H2 MINGW64 /e/CLOUD/cloudgit (main)
$ git status
On branch main
</code></pre>
</li>
</ul>
</li>
</ul>
<p>No commits yet</p>
<p>Untracked files:
  (use &quot;git add ...&quot; to include in what will be committed)
        HelpPane.exe
        samadal.txt</p>
<p>nothing added to commit but untracked files present (use &quot;git add&quot; to track)</p>
<p>Administrator@Win1022H2 MINGW64 /e/CLOUD/cloudgit (main)
$ git add samadal.txt</p>
<p>Administrator@Win1022H2 MINGW64 /e/CLOUD/cloudgit (main)
$ git add *</p>
<p>Administrator@Win1022H2 MINGW64 /e/CLOUD/cloudgit (main)
$ git status
On branch main</p>
<p>No commits yet</p>
<p>Changes to be committed:
  (use &quot;git rm --cached ...&quot; to unstage)
        new file:   HelpPane.exe
        new file:   samadal.txt</p>
<pre><code>- `github`에 전송 `(Commit)`하기
```bash
$ git commit -m &quot;Create Cloodgit&quot;
[main (root-commit) 2df3c81] Create Cloodgit
 2 files changed, 1 insertion(+)
 create mode 100644 HelpPane.exe
 create mode 100644 samadal.txt</code></pre><ul>
<li><code>github</code>에 업로드 <code>(Push)</code>하기<ul>
<li>개요<ul>
<li><code>origin</code>은 <code>등록한 원격저장소</code>를 말하고 <code>main</code>은 <code>브랜치 이름</code>인데 무조건 외우도록 한다.
즉, <code>원격저장소 이름을 origin으로 등록한 것이고 해당 저장소의 master 브랜치로 push한다는 명령어</code>이다.</li>
</ul>
</li>
<li>명령 실행 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d67cf471-6ab2-4605-a3fd-e3bb41c8cdcc/image.png" /><pre><code class="language-bash">Administrator@Win1022H2 MINGW64 /e/CLOUD/cloudgit (main)
$ git push origin main
info: please complete authentication in your browser...
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 265.91 KiB | 7.82 MiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/kyk02405/cloudgit
* [new branch]      main -&gt; main</code></pre>
</li>
<li>확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a1a29680-bc4e-4982-862e-7750f9911a41/image.png" /></li>
</ul>
</li>
</ul>
<blockquote>
<ul>
<li>: 실습
 ; 앞에서 작업한 github에 있는 저장소 등을 모두 삭제한다.
 ; 리눅스에서 DB를 구축한 후 제로보드와 연동시킨다.
 ; 제로보드에 로그인 한 후 사용자를 2개만 생성한다.
 ; 구성이 완료된 후 DB를 백업(db_20240610_각자이름이니셜.sql)한다.
 ; 파일을 gitHub의 저장소로 업로드한다.
 ; 테스트 1.<pre><code>-&gt; 온프레미스 환경의 각 팀별 도메인에 github의 저장소를 링크시킨다.</code></pre> ; 테스트 2.<pre><code>-&gt; 팀별 도메인의 메인 페이지를 서로 교환한 후 저장소를 통해 다운로드 하고 각자의 DB서버와 연동시킨다.</code></pre></li>
</ul>
</blockquote>