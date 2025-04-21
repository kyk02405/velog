<hr />
<h1 id="시스템이란">시스템이란?</h1>
<ul>
<li>시스템<ul>
<li>보안 공격의 대상이 될 수 있는 단위</li>
<li>보안 공격자의 공격 대상</li>
<li>대표적으로 서버용 운영체제(Server OS) 시스템</li>
</ul>
</li>
<li>최근의 많은 보안 사고들은 네트워크를 통해 외부에서 침입한 공격에 의해 일어남</li>
<li>시스템의 보안성을 평가하는 4가지 항목<ul>
<li>계정 관리</li>
<li>서비스 관리</li>
<li>패치 관리</li>
<li>로그 관리</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/49e26739-6be5-4f67-8676-d1019c1b883e/image.png" /></p>
<hr />
<h1 id="윈도우-서버-보안">윈도우 서버 보안</h1>
<ul>
<li><strong>서버</strong><ul>
<li>서비스를 제공하는 시스템</li>
<li>서버용 운영체제(Server OS)가 설치된 컴퓨터<br />(예: 웹서버, DB서버, 파일서버 등)</li>
</ul>
</li>
<li>대표적인 서버 OS</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9a3e9bdb-df95-478c-93c2-17cd6f511f3b/image.png" /></p>
<blockquote>
<p>🔗 <a href="https://byline.network/2024/09/240909_004/">2024 행정 및 공공기관의 정보자원 통계 보기</a></p>
</blockquote>
<hr />
<h1 id="계정-관리">계정 관리</h1>
<ul>
<li><p><strong>계정(Account)</strong><br />시스템에 접근하는 것이 허가된 사용자인지를 검증하기 위한 정보</p>
<ul>
<li><strong>아이디(ID, Identification)</strong>  </li>
<li><strong>패스워드(Password, 암호 혹은 비밀번호)</strong></li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c20d5c7a-a89a-4c07-af01-1a1f73e4dff1/image.png" /></p>
<ul>
<li><strong>관리자 계정(Administrator)</strong><ul>
<li>컴퓨터를 전체적으로 관리할 수 있는 막강한 권한이 있는 계정<ul>
<li>일반 사용자 계정 생성, 소프트웨어 설치, 운영체제 환경 설정 변경, 로그 제거 등 가능</li>
</ul>
</li>
<li>엄격한 관리가 필요함</li>
<li>(참고) 리눅스에서의 관리자 계정: <code>root</code></li>
</ul>
</li>
</ul>
<hr />
<h1 id="계정-관리-지침-1">계정 관리 지침 1</h1>
<ul>
<li><strong>가능한 관리자 계정의 개수 최소화</strong><ul>
<li>관리자 계정의 개수가 증가하면,<ul>
<li>관리자 계정에 대한 보안 위험 범위 확대</li>
<li>보안상의 관리 비용 증가</li>
</ul>
</li>
<li>최소 관리자 계정 개수 유지</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f86082d8-58fa-49dc-9e56-2feb76aed4f4/image.png" /></p>
<ul>
<li><strong>관리자 계정 확인 방법</strong><ul>
<li>계정을 탈취한 해커가 관리자 계정 그룹에 등록했을 수 있음</li>
<li>실행 위치 : 
<code>제어판 &gt; 시스템 및 보안 &gt; 관리 도구 &gt; 컴퓨터 관리</code></li>
<li>메뉴 : 
<code>로컬 사용자 및 그룹 &gt; 그룹</code></li>
</ul>
</li>
</ul>
<hr />
<h1 id="계정-관리-지침-1-1">계정 관리 지침 1</h1>
<h3 id="✅-표-2-2-윈도우-운영체제에서의-대표적-그룹의-예">✅ 표 2-2. 윈도우 운영체제에서의 대표적 그룹의 예</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>특징</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Administrators</strong></td>
<td>관리자 그룹, 윈도우 시스템의 모든 권한을 가지고 있음. 사용자 계정을 만들거나 없앨 수 있으며, 디렉터리와 프린터를 공유하는 명령을 내릴 수 있고, 자원에 대한 권한을 설정할 수 있음.</td>
</tr>
<tr>
<td><strong>Power users</strong></td>
<td>Administrators 그룹이 가진 권한을 대부분 가짐. 로컬 컴퓨터에서만 관리할 능력을 가지고 있으며, 해당 컴퓨터 외의 네트워크에서는 일반 사용자로 존재함.</td>
</tr>
<tr>
<td><strong>Backup operators</strong></td>
<td>윈도우 시스템에서 시스템 파일을 백업하는 권한을 가짐. 로컬 컴퓨터에 로그인하고 시스템을 종료할 수 있음.</td>
</tr>
<tr>
<td><strong>Users</strong></td>
<td>사용자 대부분이 속한 그룹. 네트워크를 통해 서버나 다른 도메인 구성요소에 로그인할 수 있음. 관리자 계정보다는 제한된 권한만 가짐.</td>
</tr>
<tr>
<td><strong>Guests</strong></td>
<td>Users 그룹과 같은 권한을 가짐. 네트워크를 통해 서버에는 로그인할 수 있지만, 서버로의 로컬 로그인은 금지됨.</td>
</tr>
</tbody></table>
<hr />
<h1 id="계정-관리-지침-2">계정 관리 지침 2</h1>
<ul>
<li>관리자 아이디 변경<ul>
<li>윈도우 관리자 계정은 여러 번 로그인 실패해도 계정이 잠기지 않음!</li>
<li>관리자 계정 아이디를 Administrator 대신에 다른 이름으로 변경 
→‘<strong>무차별 공격</strong>’ (브루트 포스, Brute Force) 대비 : <span style="color: red;">충분한 시간과 가능한 암호 조합을 모두 시도하면 풀림</span></li>
<li>실행 위치 :
<code>제어판 &gt; 시스템 및 보안 &gt; 관리 도구 &gt; 로컬 보안 정책 혹은, 실행 &gt; secpol.msc &lt;Enter&gt;</code></li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7f342f36-20c6-4a61-91f0-6237af0b5808/image.png" /></p>
<hr />
<h1 id="🔐-암호-관리-요약">🔐 암호 관리 요약</h1>
<ul>
<li><p><strong>암호</strong>: 로그인 시 사용되는 비밀번호(Password)</p>
</li>
<li><p><strong>기본 인증 방법</strong>: 비밀번호 기반 인증(Authentication)</p>
</li>
<li><p><strong>문제점</strong>: 비밀번호가 많아지면 기억 및 관리 어려움 → 비밀번호 관리자, 다단계 인증(MFA) 필요</p>
</li>
<li><p><strong>보안 위협</strong>: 공격자는 자주 사용되는 비밀번호를 모아둔 <strong>암호 사전(Dictionary)</strong> 을 사용</p>
</li>
<li><p><strong>많이 쓰이는 위험한 비밀번호 예시</strong>:  
<code>123456</code>, <code>123456789</code>, <code>qwerty</code>, <code>password</code>, <code>111111</code>, <code>abc123</code> 등</p>
</li>
<li><p><strong>비밀번호 미설정 계정</strong>: 🔓 대문 열어둔 집과 같음</p>
</li>
</ul>
<hr />
<h3 id="✅-좋은-암호의-특징">✅ 좋은 암호의 특징</h3>
<ul>
<li><strong>길이</strong>: 최소 8자 이상</li>
<li><strong>복잡성</strong>: 영어(대·소문자), 숫자, 특수문자 조합</li>
<li><strong>보안 정책</strong>: '로컬 보안 정책'을 통해 강제 설정 가능</li>
</ul>
<hr />
<h3 id="💡-추천-암호-조합-방식">💡 추천 암호 조합 방식</h3>
<blockquote>
<p>쉬운 단어 2개 + 4자리 숫자 + 특수기호 2개 조합<br />예시:  </p>
</blockquote>
<ul>
<li><code>BlueRed1347&amp;*</code>  </li>
<li><code>Blue1347&amp;Red*</code></li>
</ul>
<hr />
<h1 id="🔎-털린-내-정보-찾기-서비스">🔎 털린 내 정보 찾기 서비스</h1>
<ul>
<li>개인정보 유출 여부 확인 가능</li>
<li>본인 인증 후, 유출된 <strong>아이디 / 비밀번호 / 이름 / 연락처 / 주소</strong> 등 확인 가능</li>
<li>한국인터넷진흥원(KISA) 제공</li>
</ul>
<p>👉 <a href="https://kidc.eprivacy.go.kr/">털린 내 정보 찾기 서비스 바로가기</a></p>
<hr />
<p>알겠어! 요청대로 문단 제목을 <code>#</code>로 수정해서 정리해줄게:</p>
<hr />
<h1 id="🛡️-암호-관리-보안-정책-설정">🛡️ 암호 관리 (보안 정책 설정)</h1>
<ul>
<li><strong>비밀번호 강제 정책 설정</strong> 가능  </li>
<li><strong>실행 경로</strong>:  
<code>시작 &gt; 제어판 &gt; 시스템 및 보안 &gt; 관리 도구 &gt; 로컬 보안 정책</code><br />또는 <code>시작 &gt; 실행 &gt; secpol.msc</code></li>
<li><strong>윈도우 운영체제 기준 복잡성 규칙</strong>:  <ul>
<li><strong>2가지 종류 조합</strong> (예: 문자 + 숫자) → <strong>최소 길이: 10자리</strong>  </li>
<li><strong>3가지 이상 조합</strong> (예: 대문자 + 숫자 + 특수문자) → <strong>최소 길이: 8자리</strong></li>
</ul>
</li>
</ul>
<h3 id="🔠-비밀번호-구성-요소">🔠 비밀번호 구성 요소</h3>
<ul>
<li><strong>가. 영어 대문자 (26개)</strong>: 예) A, B, …, Z  </li>
<li><strong>나. 영어 소문자 (26개)</strong>: 예) a, b, …, z  </li>
<li><strong>다. 숫자 (10개)</strong>: 예) 0, 1, …, 9  </li>
<li><strong>라. 특수문자 (32개)</strong>: 예) !, @, #, $, %, 등</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9c212123-8fa1-4aeb-83a6-5950d10b443d/image.png" /></p>
<hr />
<h1 id="🔐-암호-관리-사례">🔐 암호 관리 사례</h1>
<h3 id="✅-윈도우-운영체제에서-정의된-복잡성을-만족하는-비밀번호">✅ 윈도우 운영체제에서 정의된 복잡성을 만족하는 비밀번호</h3>
<ul>
<li><code>a012345678</code> → <strong>소문자 + 숫자</strong> 구성 (<strong>2가지 종류</strong>), <strong>길이 10자리</strong></li>
<li><code>a012345*</code> → <strong>소문자 + 숫자 + 특수문자</strong> 구성 (<strong>3가지 종류</strong>), <strong>길이 8자리</strong></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3388cfe2-573e-4180-ad41-2e50005104ba/image.png" /></p>
<hr />
<h1 id="🔐-암호-관리-지침-1">🔐 암호 관리 지침 1</h1>
<ul>
<li><strong>잘못된 비밀번호를 계속 입력하면 계정은 잠겨야 한다.</strong><ul>
<li>무차별 공격(Brute Force): 가능한 모든 암호를 하나씩 대입</li>
<li>사전(dictionary) 공격: 사전에 있는 단어를 우선 시도해 시간 절약</li>
<li>계정이 잠기면 추가적인 비밀번호 시도 불가능</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8fe52619-52d0-4260-bfe5-77e4ba93aa5a/image.png" /></p>
<hr />
<h1 id="🔐-암호-관리-지침-1-1">🔐 암호 관리 지침 1</h1>
<ul>
<li><strong>잘못된 비밀번호를 계속 입력하면 계정은 잠겨야 한다.</strong><ul>
<li>로그인 실패 횟수 제한 설정</li>
<li>계정 잠금 시간은 길수록 보안성 ↑ (60시간 이상 권장)</li>
<li>실행 위치:<br /><code>제어판 &gt; 시스템 및 보안 &gt; 관리 도구 &gt; 로컬 보안 정책</code><br />또는 <code>실행 &gt; secpol.msc</code></li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/98f33117-fe69-4e39-a333-ef7b31e44b39/image.png" /></p>
<hr />
<h1 id="🔐-암호-관리-지침-2">🔐 암호 관리 지침 2</h1>
<ul>
<li><strong>비밀번호는 정기적으로 변경해주어야 한다</strong>  <ul>
<li><strong>공격자가 무차별 공격 등으로 비밀번호를 찾아낸 경우에 대해서도 보호 가능</strong>  </li>
<li><strong>권장 최대 암호 사용 기간: 90일 이하</strong>  </li>
<li><strong>실행 위치</strong> : 제어판 &gt; 시스템 및 보안 &gt; 관리 도구 &gt; 로컬 보안 정책  </li>
<li><em>혹은*</em>, 실행 &gt; <code>secpol.msc</code>  </li>
<li><strong>그 외</strong> : Guest 계정 기본 잠금, 사용중지 등 설정</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2a54b567-3a36-4136-8ec2-a786add5d9a7/image.png" /></p>
<hr />
<h1 id="🛠️-서비스-관리-지침-1">🛠️ 서비스 관리 지침 1</h1>
<ul>
<li><strong>공유 폴더에 대한 익명 사용자의 접근을 막아라</strong>  <ul>
<li><strong>일반 기업이나 공공기관에서는 파일 서버로 윈도우 서버를 많이 사용</strong>  </li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b0428675-8762-4f0d-9352-0c3a8fbe36eb/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e6eaff4c-1982-4d2e-93c1-156f7392f3b2/image.png" /></p>
<ul>
<li><strong>인가(Authorization)되지 않은 익명의 사용자가 네트워크를 통하여 중요한 문서에 접근할 수 있다면</strong>  </li>
<li><em>보안적으로 상당히 심각한 문제가 발생할 수 있음*</em></li>
</ul>
<hr />
<h1 id="서비스-관리-지침-1">서비스 관리 지침 1</h1>
<ul>
<li>공유 폴더에 대한 익명 사용자의 접근을 막아라<ul>
<li>윈도우에서는 시스템에서 공유되고 있는 폴더를
확인할 수 있도록 GUI로 제공</li>
<li>폴더에 대한 공유 설정 시, Everyone 계정을 포함하면 안 됨</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/450073f5-31b1-4e26-85af-50453eddd074/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b754a0f7-39a7-4ffe-88b8-bc61b89ab7e6/image.png" /></p>
<hr />
<h1 id="서비스-관리-지침-1-1">서비스 관리 지침 1</h1>
<ul>
<li>공유 폴더에 대한 익명 사용자의 접근을 막아라<ul>
<li>현재 시스템에서 공유되고 있는 폴더 확인</li>
<li>실행 위치 : 
<code>제어판 &gt; 관리 도구 &gt; 컴퓨터 관리 &gt; 공유 폴더 혹은, 실행 &gt; fsmgmt.msc</code></li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/894ca329-9df0-41ea-abfc-dddcd3d1c45a/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/30bb259e-ab7c-4de4-8a96-33650762cf8b/image.png" /></p>
<hr />
<h1 id="서비스-관리-지침-2">서비스 관리 지침 2</h1>
<ul>
<li>하드디스크의 기본 공유를 제거하라<ul>
<li>기본 공유 폴더 : 운영체제를 설치할 때 자동으로 생성하는 공유 폴더<ul>
<li>목적 : 네트워크 등을 이용하여 원격으로 컴퓨터를 관리하기 위한 목적</li>
</ul>
</li>
<li>C$와 D$ 같은 기본 공유 폴더를 통해서 인가받지 않은 사용자가 하드디스크 내의 모든 폴더나
파일에 접근할 수도 있음</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ddedf804-5599-49b4-9f98-a4425529e31e/image.png" /></p>
<hr />
<h1 id="서비스-관리-지침-3">서비스 관리 지침 3</h1>
<ul>
<li>불필요한 서비스를 제거하라<ul>
<li>보안 공격자들은 아주 사소한 운영체제의 약점을 집요하게 공격
→ 보안 관리자는 서버의 사소한 약점에 대해서도 철저히 준비해야 함</li>
</ul>
</li>
<li>윈도우 서비스<ul>
<li>일반 사용자의 간섭 없이 백그라운드로 특정한 기능을 수행하는 프로그램</li>
<li>윈도우 시작시 자동 실행됨<ul>
<li>유닉스의 데몬(Daemon)과 같은 역할</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="서비스-관리-지침-3-1">서비스 관리 지침 3</h1>
<ul>
<li><strong>불필요한 서비스를 제거하라</strong><ul>
<li>[프로세스] 탭의 사용자 이름에 <code>SYSTEM, LOCAL SERVICE, NETWORK</code>로 되어 있는 것<ul>
<li>단, <code>SYSTEM</code>으로 된 프로세스는 서비스 프로세스, 혹은 운영 체제 자체 프로세스(커널 프로세스</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c46fe05b-41ac-4416-aac8-1a14ef83911d/image.png" /></p>
<hr />
<h1 id="서비스-관리-지침-3-2">서비스 관리 지침 3</h1>
<ul>
<li>불필요한 서비스를 제거하라<ul>
<li>보안 가이드에서 보통 권고되는 '중지 대상' 서비스</li>
<li>Windows Server 2008부터는 지원하지 않도록 조치됨</li>
<li>다만, Windows 2000 Server와 같은 옛날 운영체제를 사용하는 사이트에서는 관리자가 수동 설정!</li>
</ul>
</li>
</ul>
<h3 id="📋-표-2-3-보안-권고-사항-중지-대상-서비스-목록">📋 표 2-3 보안 권고 사항: 중지 대상 서비스 목록</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>기능</th>
<th>비고</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Alerter</strong></td>
<td>서버에서 클라이언트로 경고 메시지를 보냄</td>
<td>Windows Server 2008부터 지원 안 됨</td>
</tr>
<tr>
<td><strong>Clipbook</strong></td>
<td>서버의 Clipbook을 다른 클라이언트로 공유</td>
<td>Windows Server 2008부터 지원 안 됨</td>
</tr>
<tr>
<td><strong>Messenger</strong></td>
<td>서버에서 클라이언트로 메시지를 보냄</td>
<td>Windows Server 2008부터 지원 안 됨</td>
</tr>
<tr>
<td><strong>Simple TCP/IP Services</strong></td>
<td>Echo(포트 7), Discard(포트 9) 등의 TCP/IP 서비스 제공</td>
<td></td>
</tr>
</tbody></table>
<hr />
<h1 id="서비스-관리-지침-3-3">서비스 관리 지침 3</h1>
<ul>
<li>불필요한 서비스를 제거하라<ul>
<li>윈도우 서비스 관리 도구<ul>
<li>불필요한 서비스 중지 : 시작 유형을 ‘사용 안 함’으로 설정</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/be213d6d-e1d1-4038-be5d-ec0707415329/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/dbfc4d89-bb90-4c3d-b2f1-a6456b691b0e/image.png" /></p>
<hr />
<h1 id="서비스-관리-지침-4">서비스 관리 지침 4</h1>
<ul>
<li><p>FTP 서비스를 가능한 사용하지 않거나 접근 제어를 엄격하게</p>
<ul>
<li>FTP(File Transfer Protocol) 서비스<ul>
<li>원격의 서버와 클라이언트 사이의 파일 전송을 위한 통신 프로토콜 중 하나</li>
<li>윈도우 서버 운영체제에서는 FTP 서비스 제공</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a4edbf92-829a-42ea-a486-bb89707414d4/image.png" /></p>
<ul>
<li>FTP 서비스 기본 운영 사항<ul>
<li>FTP 서비스 대상이 되는 파일 시스템의 접근 권한 설정 : Everyone 계정 제거</li>
<li>익명 인증(Anonymous FTP) 금지</li>
<li>FTP 접근 제어 설정 : 접속 가능한 IP 주소 대역 설정</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="서비스-관리-지침-4-1">서비스 관리 지침 4</h1>
<ul>
<li><strong>FTP 서비스를 가능한 사용하지 않거나 접근 제어를 엄격하게</strong><ul>
<li>FTP 서비스 기본 운영 사항(1)<ul>
<li>대상이 되는 파일 시스템의 접근 권한 설정 : Everyone 계정 제거</li>
<li>설정 : ‘인터넷정보서비스 관리자’에서 FTP의 사용자 권한 편집<ul>
<li>Windows 기능 켜기/끄기에서 FTP 서버 체크 부분을 체크하면 FTP 서버 활성화 됨</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1ae50997-1b96-4b3e-a9aa-4933a106e81e/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c7c21344-37a3-408d-a156-07ce0c0bb5f5/image.png" /></p>
<hr />
<h1 id="서비스-관리-지침-4-2">서비스 관리 지침 4</h1>
<ul>
<li><strong>FTP 서비스를 가능한 사용하지 않거나 접근 제어를 엄격하게</strong><ul>
<li>FTP 서비스 기본 운영 사항(2)<ul>
<li><strong>익명 인증(Anonymous FTP) 금지</strong><ul>
<li>ID가 anonymous, 비밀번호는 아무 이메일 주소만 입 하기만 하면 로그인이 성공하는 계정</li>
<li>일반 기업이나 공공 기관에서 익명 인증을 허용 하면, 원격에서 인증받지 않은 사용자 아무나 파일에 접근 가능 
→ 심각한 보안 위협</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/91b1df77-4629-47d6-a27f-29227191fd7e/image.png" /></p>
<hr />
<h1 id="서비스-관리-지침-4-3">서비스 관리 지침 4</h1>
<ul>
<li><strong>FTP 서비스를 가능한 사용하지 않거나 접근 제어를 엄격하게</strong><ul>
<li>FTP 서비스 기본 운영 사항(3)<ul>
<li>FTP 접근 제어 설정 : 접속 가능한 IP 주소 대역 설정<ul>
<li>FTP 서비스는 계정과 비밀번호가 암호화되지 않은 채로 전송</li>
<li>간단한 스니퍼(Sniffer)에 의해서도 중간에서 탈취가 가능
→ 최악의 경우에는 ID와 비밀번호의 유출 가정
→ 접속 가능한 IP 대역 자체를 아예 제한</li>
<li>예) 회사 내부의 IP 대역으로 한정
→ 외부 IP에서 FTP 접속 시도에 대한 강제적 접속 거부</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="서비스-관리-지침-4-4">서비스 관리 지침 4</h1>
<ul>
<li>FTP 서비스를 가능한 사용하지 않거나 접근 제어를 엄격하게<ul>
<li>FTP 서비스 기본 운영 사항(3)<ul>
<li>FTP IP 주소 및 도메인 제한 설정</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/044f6e02-3386-428a-bb44-329cadf4db9a/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fbe57a9d-549b-4790-a19d-fc534b2527b9/image.png" /></p>
<hr />
<h1 id="서비스-관리-지침-4-5">서비스 관리 지침 4</h1>
<ul>
<li>SFTP란<ul>
<li>SFTP (Secure File Transfer Protocol 혹은 SSH File Transfer Protocol)가 권장</li>
<li>SSL 암호화 통신 프로토콜을 사용(SSL 인증서 필요)</li>
<li>스니핑을 통해서도 ID와 비밀번호의 유출 가능성 낮음<ul>
<li>FTP는 평문으로 전송</li>
</ul>
</li>
<li>Windows Server 2008부터 제공되는 IIS 7.0 이상 버전에서는 지원</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b6e65cb0-1eb8-447a-bf49-432e3b5966e0/image.png" /></p>
<hr />
<h1 id="패치-관리-지침-1">패치 관리 지침 1</h1>
<ul>
<li>윈도우 운영체제의 패치<ul>
<li>보안은 보안 정책 수립, 훈련, 실행/통제를 통해 지속적으  로 관리가 필요</li>
<li>운영체제의 버그 및 취약점에 대한 패치(patch)가 공지되면, 가능한 신속한 적용 필요<ul>
<li>소프트웨어는 항상 버그 및 취약점을 내포하고 있다는 것을 염두!</li>
</ul>
</li>
<li>자동 업데이트 권장</li>
</ul>
</li>
</ul>
<hr />
<h1 id="패치-관리-지침-1-1">패치 관리 지침 1</h1>
<ul>
<li><strong>핫픽스 vs. 서비스 팩</strong><ul>
<li><strong>핫픽스(hot-fix)</strong><ul>
<li>컴퓨터 소프트웨어의 버그에 대한 수정이나 보안 취약점 보완을 위해 긴급히 배포하는 패치</li>
<li>보통 하나의 핫픽스는 1개의 보안 취약점 혹은 1개의 버그에 대해서만 다룸</li>
<li>핫픽스 후, 잘 동작하던 응용 프로그램이 오류가 발생할 수 있음(응용 프로그램의 새 버전 필요)</li>
</ul>
</li>
<li><strong>서비스 팩(service pack)</strong><ul>
<li>하나의 설치 패키지에 여러 개의 패치 및 개선 사항이 모여 있는 프로그램</li>
<li>기존에 없던 새로운 기능이 추가되거나 성능 개선 등의 내용이 포함되기도 함<ul>
<li>운영체제의 핵심인 커널이 변경되기도 함</li>
</ul>
</li>
</ul>
</li>
<li><strong>패치를 따로따로 설치하는 것보다 서비스 팩을 설치하는 것을 권장</strong><ul>
<li>설치가 간단, 오류 발생 가능성 낮음</li>
<li>최근에는 사용자가 업데이트 설정을 하지 않더라도, PMS(Patch Management System)과 같은 보안소프트웨어로 강제로 패치가 되도록 설정하기도 함</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="패치-관리-지침-2">패치 관리 지침 2</h1>
<ul>
<li>백신 프로그램의 업데이트 <ul>
<li>주기적 업데이트의 필요성 <ul>
<li>계속 새로운 바이러스가 만들어짐  → 최신 바이러스 정보에 대한 주기적인 업데이트 필요</li>
</ul>
</li>
<li>자동 업데이트 설정 및 주기<ul>
<li>백신 프로그램의 자동 업데이트 기능 권장 : 대부분 매주 1 회 이상 정기 업데이트 제공</li>
<li>예약 업데이트 기능: 점심 시간등 사용자가 PC를 사용하지 않는 시간을 이용</li>
</ul>
</li>
<li>기업이나 공공기관에서는 사용자의
업데이트 여부를 모니터링 필요</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/29f59c4d-5684-40d1-8c02-432966aff093/image.png" /></p>
<hr />
<h1 id="로그-관리">로그 관리</h1>
<ul>
<li><strong>로그란?</strong><ul>
<li>책임 추적성(Accountability ): 사용자의 행위에 대해 나중에 추적할 수 있게 한다<ul>
<li>누가, 언제, 무엇을 했는지 파악할 수 있는 보안 시스템의 기본적인 요소</li>
<li>로그 : 책임 추적성을 가능하게 하는 기반 자료</li>
</ul>
</li>
</ul>
</li>
<li><strong>로그 관리</strong><ul>
<li>전자금융거래법 등의 법규 및 지침을 통해 강제적으로 로그를 저장하고 관리</li>
<li>데이터 종류, 파일 저장 위치, 보관 기간 등에 주의</li>
<li>로그 백업</li>
</ul>
</li>
</ul>
<hr />
<h1 id="로그-관리-1">로그 관리</h1>
<ul>
<li><strong>로그 분석의 목적</strong><ul>
<li>외부로부터의 침입 감지 및 추적</li>
<li>시스템 성능 관리 및 시스템의 장애 원인 분석</li>
<li>시스템 취약점 분석 및 이상징후 파악</li>
<li>침해 사고 시 근거 자료로 활용(포렌식 분석)</li>
<li>각종 법규 및 지침에서의 관리 의무화 항목</li>
</ul>
</li>
<li><strong>금융기관에서 로그 관리 사례</strong><ul>
<li>고객의 금융 거래 내역과 정보를 추적과 보관<ul>
<li>입출금 내역, 이체 내역, 대출 신청 이력 등</li>
</ul>
</li>
</ul>
</li>
<li><strong>전자 상거래에서 로그 관리 사례</strong><ul>
<li>온라인 쇼핑몰에서 다양한 고객의 행동들을 로그로 남겨 분석(개인화된 상품 추천)<ul>
<li>고객의 구매 이력, 클릭한 제품, 장바구니에 담은 제품 등</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="로그-관리-2">로그 관리</h1>
<ul>
<li>로그 보기<ul>
<li>이벤트 뷰어<ul>
<li>실행 위치:
<code>제어판 &gt; 관리 도구 &gt; 컴퓨터 관리 &gt; 이벤트 뷰어 혹은, 실행 &gt; eventvwr.msc</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/54dc7f2a-c892-4b3b-8ca9-6ea94001d4da/image.png" /></p>
<hr />
<h1 id="로그-관리-3">로그 관리</h1>
<ul>
<li>로그 보기<ul>
<li><strong>응용 프로그램(application)</strong><ul>
<li>일반 응용 프로그램(예: 오피스)에서 발생한 이벤트</li>
<li>로그 기록은 소프트웨어 개발사에 의해 결정</li>
</ul>
</li>
<li><strong>보안(security)</strong><ul>
<li>로그온 시도(성공/실패)</li>
<li>사용자 계정 추가/삭제(권한 변경)</li>
<li>로그 기록은 관리자에 의한 감사 로그 설정에 의해 결정(유일하게 기록할 이벤트 유형을 사용자가 변경 가능)</li>
</ul>
</li>
<li><strong>설정(setup)</strong><ul>
<li>윈도우에 응용 프로그램 설치 및 설정 관련 이벤트</li>
</ul>
</li>
<li><strong>시스템(system)</strong><ul>
<li>윈도우 시스템 구성요소에서 기록한 이벤트 (기록 유형이 정해져 있음)<ul>
<li>장치 드라이버의 로드 여부</li>
<li>시스템 서비스의 시작 여부 </li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1b0d0794-4ba1-4cb0-ab5a-c85129e3410a/image.png" /></p>
<hr />
<h1 id="로그-관리-4">로그 관리</h1>
<ul>
<li>보안 로그 사례</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/37a41cdc-3a95-4317-9d03-c20bc2d6a4e3/image.png" /></p>
<hr />
<h1 id="로그-관리-5">로그 관리</h1>
<ul>
<li>이벤트 로그 속성</li>
</ul>
<h3 id="📋-표-2-5-이벤트-속성-정리">📋 표 2-5 이벤트 속성 정리</h3>
<table>
<thead>
<tr>
<th>속성 이름</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>키워드</strong></td>
<td>이벤트를 필터링하거나 검색하는 데 사용할 수 있는 범주 또는 태그의 집합이다. 예를 들면 &quot;감사 실패&quot;, &quot;네트워크&quot;, &quot;보안&quot;, &quot;리소스를 찾을 수 없습니다.&quot;가 있다.</td>
</tr>
<tr>
<td><strong>날짜 및 시간</strong></td>
<td>이벤트가 기록된 날짜 및 시간을 나타낸다.</td>
</tr>
<tr>
<td><strong>원본</strong></td>
<td>이벤트를 기록한 소프트웨어로 &quot;SQL Server&quot; 등의 프로그램 이름이거나 드라이버 이름 등의 시스템 구성요소 또는 대형 프로그램의 구성요소일 수 있다. 예를 들어 &quot;Enklii&quot;는 EtherLink II 드라이버를 나타낸다.</td>
</tr>
<tr>
<td><strong>이벤트 ID</strong></td>
<td>특정 이벤트 유형을 식별하는 번호. 설명의 첫 줄에는 대개 이벤트 유형의 이름이 나온다. 예를 들면 6005는 이벤트 로그 서비스가 시작될 때 발생하는 이벤트 ID이다. 이런 이벤트 설명의 첫 줄은 &quot;이벤트 로그 서비스가 시작되었습니다.&quot;이다. 이벤트 ID와 원본은 제품 지원 담당자가 시스템 문제를 해결하는 데 사용할 수 있다.</td>
</tr>
<tr>
<td><strong>작업 범주</strong></td>
<td>&quot;로그온&quot; 혹은 &quot;로그오프&quot;와 같이 어떤 동작 혹은 작업을 하다가 발생한 이벤트인지 알려준다.</td>
</tr>
</tbody></table>
<hr />
<h1 id="로그-관리-6">로그 관리</h1>
<ul>
<li><strong>감사(audit)</strong><ul>
<li>단체 규율과 구성원의 행동, 업무에 문제가 있는지 조사하고 감찰하는 직무 - 나무위키</li>
</ul>
</li>
<li><strong>감사 정책 설정</strong><ul>
<li>로그 ‘감사 정책’ : 어떤 로그를 남길지 정의한 규칙<ul>
<li>감사자와 IT 담당자가 사용자의 작업 내역을 추적하기 용이하도록 지원</li>
</ul>
</li>
<li>실제 서버에서 운영되는 서비스 및 보안 수준 등에 따라 어떤 로그를 남겨야 하는지 결정</li>
</ul>
</li>
<li><strong>감사 로그의 활용</strong><ul>
<li>시스템 내에서 비정상적이거나 불법적인 행위를 인지</li>
<li>잠재적인 보안 문제 식별에 대한 증거 및 분석 자료</li>
<li>포렌식 증거(법적 근거자료)로 활용</li>
</ul>
</li>
</ul>
<hr />
<h1 id="로그-관리-7">로그 관리</h1>
<ul>
<li><strong>로그 분석 방법: 필터링</strong><ul>
<li>대용량의 로그에서 의미 있는 정보를 찾아 내는 방법
→ 이벤트 필터링 기법</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7e59ff8b-333b-499b-81b2-4b7e50c958ac/image.png" /></p>
<hr />
<h1 id="로그-관리-8">로그 관리</h1>
<ul>
<li>로그 분석 방법 : 필터링<ul>
<li>중요 보안 관련 이벤트 ID</li>
</ul>
</li>
</ul>
<h3 id="📋-표-2-6-중요-보안-관련-이벤트-id">📋 표 2-6 중요 보안 관련 이벤트 ID</h3>
<table>
<thead>
<tr>
<th>범주</th>
<th>이벤트 ID</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>계정 로그인</strong></td>
<td>4624</td>
<td>계정에 성공적으로 로그인했습니다.</td>
</tr>
<tr>
<td></td>
<td>4625</td>
<td>계정에 로그인하지 못했습니다.</td>
</tr>
<tr>
<td><strong>자격 증명 유효성 검사</strong></td>
<td>4768</td>
<td>컴퓨터 계정에 대해 자격 증명의 유효성을 검사하려고 했습니다.</td>
</tr>
<tr>
<td></td>
<td>4777</td>
<td>도메인 컨트롤러 계정 자격 증명의 유효성을 검사하지 못했습니다.</td>
</tr>
<tr>
<td><strong>계정 관리</strong></td>
<td>4720</td>
<td>사용자가 계정을 만들었습니다.</td>
</tr>
<tr>
<td></td>
<td>4722</td>
<td>사용자가 계정을 사용할 수 있습니다.</td>
</tr>
<tr>
<td></td>
<td>4723</td>
<td>계정의 암호를 변경하려고 했습니다.</td>
</tr>
<tr>
<td></td>
<td>4724</td>
<td>계정의 암호를 원래대로 했습니다.</td>
</tr>
<tr>
<td></td>
<td>4725</td>
<td>사용자가 계정을 사용하지 않도록 설정했습니다.</td>
</tr>
<tr>
<td></td>
<td>4726</td>
<td>사용자가 계정이 삭제되었습니다.</td>
</tr>
<tr>
<td></td>
<td>4740</td>
<td>사용자가 계정이 잠겼습니다.</td>
</tr>
<tr>
<td><strong>시스템</strong></td>
<td>512</td>
<td>Windows를 시작하고 있습니다.</td>
</tr>
<tr>
<td></td>
<td>513</td>
<td>Windows를 종료하고 있습니다.</td>
</tr>
<tr>
<td></td>
<td>517</td>
<td>보안 로그를 수정하였습니다.</td>
</tr>
<tr>
<td></td>
<td>612</td>
<td>보안 로그를 삭제하였습니다.</td>
</tr>
</tbody></table>
<hr />
<h1 id="로그-관리-9">로그 관리</h1>
<ul>
<li><strong>로그 관리 방안</strong><ul>
<li><strong>최대 이벤트 로그 크기 산정</strong><ul>
<li>너무 크게 설정 → 너무 많은 로그 저장 → 시스템 장애 발생</li>
<li>너무 작게 설정 → 중요 로그가 삭제</li>
</ul>
</li>
<li><strong>최대 로그 크기 결정의 예</strong><ul>
<li>보통 평균 이벤트는 약 500바이트 소비</li>
<li>1일 약 1000개의 이벤트가 발생한다고 가정</li>
<li>1달(30일) 동안 로그가 저장되어야 한다고 기준 설정</li>
<li>최대 로그 크기 = 500 * 1,000 * 30 = 15,000,000 byte = 약 14.3Mbyte</li>
</ul>
</li>
<li><strong>중요 로그는 백업 수행</strong><ul>
<li>예상하지 못한 대량의 로그로 중요 로그 삭제 가능성은 여전히 존재!</li>
<li>자동 로그 백업, 원격 로그 서버 구성, 관리자의 수동 백업 등</li>
</ul>
</li>
<li><strong>주기적으로 쌓인 로그 분석 및 검토 수행</strong><ul>
<li>로그를 많이 남기더라도 분석하지 않으면 무의미한 데이터가 됨</li>
<li>침입 유무나 침입 시도 의심 사례들을 분석해야 접근 차단 등의 조치를 수행할 수 있음</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="로그-관리-10">로그 관리</h1>
<ul>
<li>로그 관리 방안<ul>
<li>최대 로그 크기 설정</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/414f3440-e0ed-44d7-b45f-08bc998db4b3/image.png" /></p>