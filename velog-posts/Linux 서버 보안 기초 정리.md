<hr />
<h2 id="리눅스-서버-운영체제">리눅스 서버 운영체제</h2>
<p>• 서버 시장에서 점유율 높음
• 대용량 서버 시장(Unix) 및 클라우드 환경(Linux)
• 클라우드 환경에서는 대부분 리눅스 기반으로 동작
• 웹에서 리눅스 사용 : <a href="https://bellard.org/jslinux/">https://bellard.org/jslinux/</a></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2016f19f-9dcc-4815-a0fb-5cd13feec2f2/image.png" /></p>
<hr />
<h2 id="시스템-보안">시스템 보안</h2>
<ul>
<li>계정관리<ul>
<li>사용자 식별을 위한 가장 기본적인 인증
수단은 ID/PW</li>
</ul>
</li>
<li>세션 관리<ul>
<li>일정 시간이 지나면 세션을 종료하고,
비인가자의 세션 가로채기를 통제</li>
</ul>
</li>
<li>접근 제어<ul>
<li>네트워크 안에서 시스템을 다른
시스템으로부터 적절히 보호할 수 있도록
접근 통제</li>
</ul>
</li>
<li>권한 관리<ul>
<li>시스템의 각 사용자가 적절한 권한으로
정보자산에 접근하도록 통제</li>
</ul>
</li>
<li>로그 관리<ul>
<li>시스템 내부나 네트워크를 통해 외부에서
시스템에 어떤 영향을 미칠 경우 그 내용을
기록 및 관리</li>
</ul>
</li>
<li>취약점 관리<ul>
<li>시스템 자체의 결함을 체계적으로 관리</li>
</ul>
</li>
</ul>
<hr />
<h2 id="계정관리">계정관리</h2>
<ul>
<li>보안의 네 가지 인증방법<ul>
<li>알고 있는 것<ul>
<li>머릿속에 기억하고 있는 정보를 통한 인증</li>
<li>(예) ID/PW</li>
</ul>
</li>
<li>가지고 있는 것<ul>
<li>신분증이나 OTP 장치 등으로 인증</li>
<li>(예) 출입카드</li>
</ul>
</li>
<li>자신의 모습<ul>
<li>생체정보를 통한 인증</li>
<li>(예) 지문 인식, 홍채 인식</li>
</ul>
</li>
<li>위치하는 곳<ul>
<li>현재 접속을 시도하는 위치를 확인</li>
<li>콜백(call back)을 사용해 인증
※ 콜백 : 접속을 요청한 사람을 확인하기 위해 등록된 전화번호로 전화를 되걸어 본인 확인</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="계정관리-1">계정관리</h2>
<ul>
<li>사용자 계정<ul>
<li>시스템 접근(로그인)을 위해서는 계정(account)이 필요</li>
<li>운영체제는 계정별 자원(프로세스, 파일 등)에 할당된 접근 권한으로 운영을 허용</li>
<li>운영체제는 사용자(user)별 접근 권한 및 그룹(group)별 접근 권한을 지원</li>
<li>시스템 내 모든 계정은 그룹에 포함되어 관리</li>
<li>관리자(root) 계정 &amp; 일반 사용자 계정</li>
</ul>
</li>
<li>리눅스에서 관리자 계정 : root<ul>
<li>리눅스의 기본 관리자 계정</li>
<li>컴퓨터를 전체적으로 관리할 수 있는 막강한 권한이 있는 계정</li>
<li>복잡한 비밀번호 사용 등 엄격한 관리 필요</li>
</ul>
</li>
<li>관리자 계정의 관리 지침<ul>
<li>Root 계정으로 원격 접속 금지</li>
<li>비밀번호 파일을 shadow 파일로 보호</li>
<li>잘못된 비밀번호를 계속 입력하면, 그 계정은 잠겨야 함</li>
</ul>
</li>
<li>원격에서 root 계정으로 접속 금지<ul>
<li>원격지에서 서버에 접속하기 위해 ssh, telnet 등의 프로그램을 이용</li>
<li>네트워크를 통해 root 계정을 원격 접속 허용하면 1차 공격 대상으로써 위험!</li>
<li>Ubuntu에서는 root 로그인이 안되도록 기본 설정되어 있음<ul>
<li>필요하다면, 일반 유저로 접속한 후 root 계정을 불러오는 좋음</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/53e8795b-6982-4e98-bce7-81169a6d2826/image.png" /></p>
<hr />
<h3 id="참고-리눅스에서-ssh-서버-설치">(참고) 리눅스에서 ssh 서버 설치</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bd4d4e02-2bad-4a05-ab31-629cc7afb846/image.png" /></p>
<blockquote>
<p>시스템의 패키지 목록을 최신화 : ~$ sudo apt update
ssh-server 설치 : ~$ sudo apt install openssh-server
ssh 동작 확인</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5260af1d-295f-40c0-918b-696f46d9d45c/image.png" /></p>
<ul>
<li>root 원격접근 차단위한 설정 :<ul>
<li>설정 파일 : /etc/ssh/sshd_config</li>
<li>임의의 port 설정<ul>
<li>ssh의 기본 포트 22를 다른 포트로 설정</li>
</ul>
</li>
<li>PermitRootLogin no 로 설정<ul>
<li>root 사용자의 로그인 허용 여부 설정을 위해 (yes / no / prohibit-password /without-password / forced-commands-only) 중 하나 설정<ul>
<li>yes : root 계정으로 원격 로그인 가능</li>
<li>no : root 계정으로 원격 로그인 불가</li>
<li>prohibit-password : 비밀번호를 사용한 로그인 불가, key 파일을 사용해 로그인 (default)</li>
<li>without-password : 원격에서 키 로그인은 허용하며, 원격 패스워드 로그인은 금지</li>
<li>forced-commands-only : 원격에서 키 로그인은 허용하지만, 로그인 대신 command를 사용해서 명령만 전달 가능</li>
</ul>
</li>
</ul>
</li>
<li>MaxAuthTries<ul>
<li>로그인 시도 횟수 설정</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="계정관리-2">계정관리</h2>
<ul>
<li>비밀번호 파일을 shadow 파일로 보호<ul>
<li>계정정보와 암호화된 패스워드를 별도의 파일로 관리</li>
<li>사용 권한을 오직 root 사용자만 읽어볼 수 있음</li>
<li>계정 관리 명령어<ul>
<li>사용자 추가 : adduser [계정명]</li>
<li>비밀번호 설정 : passwd [계정명]</li>
<li>사용자 삭제 : deluser [계정명] ( → 관리자(root) 권한으로만 실행 가능)</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ee35cb88-51b9-4194-a373-e26a0ad20488/image.png" /></p>
<hr />
<ul>
<li>비밀번호 파일을 shadow 파일로 보호<ul>
<li>설정 파일 : /etc/passwd</li>
<li>다양한 사용자 관련 정보가 저장됨<ul>
<li>계정 이름</li>
<li>사용자의 비밀번호 정보</li>
<li>사용자 ID</li>
<li>그룹 ID</li>
<li>사용자 코멘트(시스템 설정에 영향을 주지 않음)</li>
<li>사용자의 홈 디렉터리</li>
<li>사용자가 기본적으로 사용한 쉘 종류 등도 저장 (ex) /bin/bash</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/66bad642-1289-4207-af27-d89a679edf99/image.png" /></p>
<hr />
<ul>
<li>비밀번호 파일을 shadow 파일로 보호<ul>
<li>설정 파일 : /etc/shadow<ul>
<li>사용자 계정 별 비밀번호를 관리
(백업파일 : /etc/shadow-)</li>
<li>파일은 시스템관리자(root)만 접근이 가능</li>
<li>비밀번호는 암호화되어 관리됨(“!” 문구가 앞에있으면 접근 불가 상태가 됨)</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/913e82c5-3ab5-42ee-9cf8-41ef92a880fc/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6b3dcb8a-2de6-4494-a90b-387fe3c563de/image.png" /></p>
<hr />
<ul>
<li>계정별 소유권</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c3d36cba-0658-43a2-9e14-1e13d1a3496a/image.png" /></p>
<hr />
<ul>
<li>그룹 정보<ul>
<li>설정 파일 : /etc/group &amp; /etc/gshadow<ul>
<li>그룹별 비밀번호를 관리(백업 파일 : /etc/gshadow-)</li>
<li>파일은 시스템 관리자(root)만 접근 가능</li>
<li>비밀번호는 암호화되어 관리</li>
<li>그룹 관리 명령어<ul>
<li>그룹 추가 : addgroup [그룹명]</li>
<li>그룹 삭제 : delgroup [그룹명]</li>
<li>그룹 확인 : groups</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/73b40674-c8d9-4c2e-b146-53c5d9939c65/image.png" /></p>
<hr />
<ul>
<li><p>사용자 전환</p>
<ul>
<li>su [계정명] 혹은 su – [계정명]<ul>
<li>시스템 관리자(root) 로 전환시 [계정명] 입력하지 않아도 됨</li>
</ul>
</li>
<li>사용자 전환 시 반드시 해당 계정의 비밀번호를 입력해야 함<ul>
<li>단, 시스템 관리자(root)가 다른 계정으로 전환할 때는 비밀번호 입력 X</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/58337860-765e-47de-aca6-35f454c9da47/image.png" /></p>
</li>
</ul>
<hr />
<ul>
<li><p>대리 실행</p>
<ul>
<li>sudo [-u user] [명령어]</li>
<li>지정한 사용자 계정으로 명령어 실행<ul>
<li>지정한 계정이 없을 경우 입력한 명령어는 시스템 관리자(root) 계정으로 실행됨</li>
</ul>
</li>
<li>지정된 명령어만 해당 계정으로 동작함<ul>
<li>프로세스 종료 후 원래 계정으로 복귀</li>
</ul>
</li>
<li>시스템에서 별도로 지정된 계정만 이용할 수 있음<ul>
<li>/etc/sudo.conf, /etc/sudoers, /etc/sudoers.d/*</li>
</ul>
</li>
</ul>
</li>
<li><p>su와 sudo의 차이</p>
<ul>
<li>su는 지정된 사용자 계정으로 전환</li>
<li>sudo는 일시적으로 지정된 사용자 계정으로 명령어 실행</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a9665211-3cc1-4c11-871b-928339a6465c/image.png" /></p>
</li>
</ul>
<hr />
<ul>
<li>패스워드 관리<ul>
<li>부적절한 패스워드<ul>
<li>길이가 너무 짧거나 널(Null)인 패스워드</li>
<li>사전에 나오는 단어나 그 조합 또는 변형</li>
<li>키보드 자판의 일련 나열</li>
<li>사용자 계정 정보로 유추할 수 있는 단어</li>
</ul>
</li>
<li>적절한 패스워드<ul>
<li>기억하기 쉽지만 크래킹하기 어려운 패스워드</li>
</ul>
</li>
<li>패스워드 정책<ul>
<li>패스워드의 길이와 복잡도 설정
ex) 8자 이상, 숫자 &amp; 알파벳 &amp; 특수문자 혼합 등</li>
<li>패스워드 변경 정책 : 60일 혹은 90일 간격으로 패스워드 변경하도록 설정</li>
<li>잘못된 패스워드 입력시 계정 잠금</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="그밖의-계정관리">그밖의 계정관리</h2>
<ul>
<li>데이터베이스의 계정 관리<ul>
<li>데이터베이스에도 운영체제처럼 계정이 존재</li>
<li>MS-SQL의 관리자 계정은 sa, 오라클의 관리자 계정은 sys, system<ul>
<li>둘 다 관리자 계정이지만 sys와 달리 system은 데이터베이스를 생성할 수 없음</li>
</ul>
</li>
</ul>
</li>
<li>응용 프로그램의 계정 관리<ul>
<li>취약한 응용 프로그램을 통해 공격자가 운영체제에 접근하여 민감한 정보를 습득한 뒤 운영체제를 공격
하는 데 이용할 수 있음</li>
<li>TFTP처럼 사용자 인증 없이 파일 전송하는 응용 프로그램-은 더욱 세심한 주의가 필요 → cf) SFTP</li>
</ul>
</li>
<li>네트워크 장비의 계정 관리<ul>
<li>네트워크 장비는 보통 패스워드만 알면 접근이 가능</li>
<li>시스코 장비의 계정의 모드 구별<ul>
<li>네트워크 장비의 상태만 확인할 수 있는 사용자 모드</li>
<li>네트워크에 대한 설정 변경이 가능한 관리자 모드</li>
<li>처음 접속시 사용자 모드로 로그인 되며, 사용자 모드에서 관리자 모드로 로그인하려면 enable 명령어와 함께 별도의 패스워드를 입력</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7044a433-dad1-4c24-9e62-d06ef21da4c4/image.png" /></p>
<hr />
<h2 id="세션관리">세션관리</h2>
<ul>
<li><p>세션</p>
<ul>
<li><p>사용자와 시스템 사이 또는 두 시스템 사이의 활성화된 접속을 의미</p>
</li>
<li><p>즉, 클라이언트와 서버 간의 연결 상태를 의미</p>
</li>
<li><p>웹서버의 연결성을 유지하기 위해 세션 사용</p>
<ul>
<li>HTTP는 stateless(클라이언트의 상태를 저장하지 않음) &amp; connectionless(연결이 1회성)</li>
</ul>
</li>
<li><p>일정 시간 이후 자동 세션 종료</p>
<ul>
<li>비인가자가 해당 세션을 갖지 못하게 함</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c518668b-353e-4217-bbd8-5de37e2d8636/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4cc86d67-4146-4be6-ac24-72261fd83590/image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="패치관리">패치관리</h2>
<ul>
<li>패치의 필요성<ul>
<li>운영체제도 일종의 소프트웨어<ul>
<li>새로운 버그 및 취약점이 발견됨</li>
<li>발견된 취약점을 악용하는 보안 공격 발생</li>
</ul>
</li>
<li>패치 적용을 통한 보안성 및 시스템 안정성 확보</li>
<li>(예) Ubuntu LTS에 대해 19개의 보안취약점을 해결하는 업데이트 실시(2023년)</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/aa04d428-d037-4ac5-bb7f-dc720334a55a/image.png" /></p>
<hr />
<h2 id="로그-관리">로그 관리</h2>
<ul>
<li>개요<ul>
<li>시스템 로그<ul>
<li>시스템의 성능, 오류, 경고 및 운영 정보 등이 기록</li>
</ul>
</li>
<li>서버 보안 관리자의 역할<ul>
<li>시스템 로그를 정기적으로 분석</li>
<li>침입 유무 파악, 침입 시도 의심 사례의 분석 및 보고</li>
</ul>
</li>
<li>유닉스의 표준적 로그 인터페이스: syslog</li>
</ul>
</li>
</ul>
<p>  <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4df8a865-ebfd-4274-a5db-4d22f318216d/image.png" /></p>
<hr />
<ul>
<li>syslog.conf<ul>
<li>어떤 로그를 어디에 남길지에 대한 로그 저장 규칙을 정의</li>
<li>syslog.conf 의 예</li>
</ul>
</li>
</ul>
<table>
<thead>
<tr>
<th>로그 수준</th>
<th>설정</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>Emergency (emerg)</td>
<td><code>*.emerg *</code></td>
<td>모든 형태(*)로 로그 저장 (로그 파일, 콘솔 포함)</td>
</tr>
<tr>
<td>Alert (alert)</td>
<td><code>*.alert /var/adm/syslog.log</code></td>
<td>심각한 에러 발생 시 파일(<code>/var/adm/syslog.log</code>)에 저장</td>
</tr>
<tr>
<td>None (authpriv)</td>
<td><code>authpriv.none /var/log/messages</code></td>
<td>보안 로그(authpriv)는 어떤 수준에서도 저장하지 않음</td>
</tr>
<tr>
<td>All (authpriv)</td>
<td><code>authpriv.* /var/log/messages</code></td>
<td>보안 로그(authpriv)의 모든 수준(*)을 <code>/var/log/messages</code>에 저장</td>
</tr>
</tbody></table>
<hr />
<ul>
<li>syslog 의 로그 수준<ul>
<li>모든 로그를 남기는 것은 성능과 부하 측면에서 현실적으로 불가능</li>
<li>어느 이상의 심각한 수준에 대해서 선별적으로 로그를 남기는 것을 권장<ul>
<li>서버에서 다루고 있는 보안 수준에 따라 로그 수준(level)을 결정</li>
</ul>
</li>
</ul>
</li>
</ul>
<table>
<thead>
<tr>
<th>수준(Level)</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Emergency</strong></td>
<td>시스템이 전면 중단되는 패닉(panic)이 발생할 정도로 심각한 수준</td>
</tr>
<tr>
<td><strong>Alert</strong></td>
<td>주의가 필요한 심각한 오류가 발생한 수준</td>
</tr>
<tr>
<td><strong>Critical</strong></td>
<td>하드웨어 등의 심각한 오류가 발생한 경우</td>
</tr>
<tr>
<td><strong>Error</strong></td>
<td>일상적인 오류가 발생한 경우</td>
</tr>
<tr>
<td><strong>Warning</strong></td>
<td>경고 수준</td>
</tr>
<tr>
<td><strong>Notice</strong></td>
<td>오류는 아니지만 관리자의 조치가 필요한 경우</td>
</tr>
<tr>
<td><strong>Informational</strong></td>
<td>의미 있는 정보가 있는 경우</td>
</tr>
<tr>
<td><strong>Debug</strong></td>
<td>문제가 있는 것은 아니고 문제 해결을 돕기 위해 부가적인 정보를 제공하기 위한 경우</td>
</tr>
</tbody></table>
<hr />
<ul>
<li>syslog 로그 파일의 종류 및 경로<ul>
<li>대부분 로그 파일의 경로가 미리 약속되어 있음</li>
</ul>
</li>
</ul>
<table>
<thead>
<tr>
<th>구분</th>
<th>로그 생성 시스템(facility)</th>
<th>파일 경로</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>시스템 로그</strong></td>
<td>(기본)</td>
<td><code>/var/adm/syslog.log</code></td>
<td>운영체제에 의해 생성되는 메인 로그</td>
</tr>
<tr>
<td></td>
<td></td>
<td><code>/var/adm/messages</code></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td><code>/var/log/messages</code></td>
<td></td>
</tr>
<tr>
<td><strong>보안 로그</strong></td>
<td><code>auth</code></td>
<td><code>/var/adm/auth.log</code></td>
<td>로그인의 실패 등 보안과 관련된 로그</td>
</tr>
<tr>
<td></td>
<td><code>authpriv</code></td>
<td><code>/var/log/secure</code></td>
<td></td>
</tr>
<tr>
<td><strong>메일 로그</strong></td>
<td><code>mail</code></td>
<td><code>/var/adm/mail.log</code></td>
<td>(sendmail 등에 의한) 메일 관련 로그</td>
</tr>
<tr>
<td></td>
<td></td>
<td><code>/var/log/maillog</code></td>
<td></td>
</tr>
<tr>
<td><strong>부팅 로그</strong></td>
<td><code>local0 ~ local7</code></td>
<td><code>/var/adm/ras/bootlog</code></td>
<td>운영체제 부팅 시의 로그</td>
</tr>
<tr>
<td></td>
<td></td>
<td><code>/var/log/boot.log</code></td>
<td></td>
</tr>
<tr>
<td><strong>커널 로그</strong></td>
<td><code>Kern</code></td>
<td><code>/dev/console</code></td>
<td>운영체제가 콘솔에 출력하는 로그</td>
</tr>
</tbody></table>
<hr />
<ul>
<li><p>보안 로그 (/var/log/secure)의 예
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6acda362-8497-4d80-8962-42ad04b1f923/image.png" /></p>
<ul>
<li>su 명령어를 통해 sjinlee 사용자가 root 사용자 변경을 시도했지만 실패
→ Password check failed for user ( root ) ….. Logname=sjinlee</li>
<li>단순 비밀번호 실패가 아니라 여러 차례 반복적으로 시도된 경우</li>
<li>보안적으로 위험한 공격일 가능성 있음 → 이를 분석하여 보고하는 역할을 수행</li>
<li>로그 관리 관련 시스템 보안 관리자의 주의할 점<ul>
<li>로그 파일 용량의 정기적 점검 필요<ul>
<li>로그 파일을 위한 디스크 용량이 충분한지 정기적으로 점검</li>
<li>적절한 보관 주기에 따라 기존의 로그를 삭제하거나 혹은 다른 보관 매체로 이동</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="서비스-관리">서비스 관리</h2>
<ul>
<li>이메일 서비스를 관리하라<ul>
<li>리눅스의 이메일 서비스 : sendmail 서비스</li>
<li>이메일을 보내거나(발송) 받는(수신) 등의 역할 수행<ul>
<li>보안 공격자들의 집중적인 공격 목표</li>
</ul>
</li>
<li>보안 취약점이 많이 알려져 있음
(예) 버퍼 오버플로우 공격에 의한 시스템 권한 획득</li>
<li>가능한 sendmail을 비활성화 권장<ul>
<li>서비스 정지 : systemctl stop sendmail</li>
<li>서비스 비활성화 : systemctl disable sendmail</li>
<li>추천 스택 : Postfix(SMTP 서버용) + Dovecot(IMAP/POP3 서버용) + 추가적인 보안도구(스팸 필터링, 바이러스 검사 등)</li>
</ul>
</li>
<li>반드시 사용해야만 하는 경우: 최신의 sendmail 버전을 유지 필요 (보안 취약점 보완)<ul>
<li>최신 버전 정보: 한국인터넷진흥원 (KISA) 홈페이지를 통해 확인 가능</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5f840588-8f20-4fba-a7fd-459fb2fb2902/image.png" /></p>
<hr />
<ul>
<li>안전한 소프트웨어 개발을 위해 소스코드에서 보안 취약점을 제거</li>
<li>동의어 : 안전한 코딩 또는 시큐어 코딩 (Secure Coding)</li>
<li>시큐어 코딩이 적용된 소프트웨어 개발 과정</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/94951351-1894-473e-8cc5-582822afe7b9/image.png" /></p>
<blockquote>
<p> 소스코드의 보안 취약점을 이용한 사이버 공격은 방화벽, 침입 차단 시스템, 침입 방지 시스템 등의 일반적인 보안 장비로는
대응이 어려움 → 보안장비들은 ‘정상’으로 인식</p>
</blockquote>
<ul>
<li>대표적인 시큐어 코딩 가이드<ul>
<li>CERT(컴퓨터 비상 대응팀, Computer Emergency Response   Team) 의 가이드</li>
<li>우리나라 : 행정안전부의 소프트웨어 보안 개발 가이드</li>
<li>boho.or.kr</li>
</ul>
</li>
</ul>
<hr />
<h3 id="①-메모리-버퍼-오버플로memory-buffer-overflow-공격">① 메모리 버퍼 오버플로(Memory Buffer Overflow) 공격</h3>
<ul>
<li>프로그램이 실행되는 도중에 메모리 오류가 발생하여 의도하지 않는 동작이 일어나는 보안 취약점</li>
<li>개발자가 예상한 범위를 벗어난 입력 값이 전달<ul>
<li>지정된 크기의 저장 공간(버퍼, Buffer)보다 넘치게(오버플로, Overflow) 저장<ul>
<li>이렇게 넘치게 저장된 값으로 시스템에 보안 문제를 일으키는 보안 공격</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/248cdafd-8814-4069-b365-12bce158b023/image.png" /></p>
<hr />
<ul>
<li>버퍼 오버플로가 발생할 수 있는 안전하지 않은 C 소스코드의 예제<pre><code class="language-c">01: #include &lt;stdio.h&gt;
02: int main(int argc, char* argv[])
03: {
04: char buffer[10] = {0};
05: if (argv[1] != NULL)
06: strcpy(buffer, argv[1]); // 안전하지 않은 코드
07: printf(&quot;%s\n&quot;,buffer);
08: }</code></pre>
<pre><code class="language-c">a.out 012345 [엔터]
012345</code></pre>
</li>
</ul>
<ul>
<li>사용자가 입력한 값의 길이가 10보다 클 때<ul>
<li>0123456789…0123456789ABCD</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>보안 공격자가 버퍼 오버플로 결함을 통해 공격<ul>
<li>전달하는 데이터의 길이와 내용을 적절히 조정해서 프로그램이 의도하지 않는 방식으로 실행 가능</li>
<li>예) buffer에 인접한 메모리 영역 : 프로그램 흐름 제어와 관련된 값을 저장하는 곳<ul>
<li>다음 단계로 이동되어야 할 메모리 주소 저장</li>
<li>메모리 주소 0xABCD로 설정하여, 함수 auth_success()가 다음 단계에서 실행되도록 함</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8c5dcc9a-571b-4cfa-b8b5-559797ca52bc/image.png" /></p>
<hr />
<ul>
<li>대응 방안<ul>
<li>최신 운영체제의 자체 방어<ul>
<li>예) <ul>
<li>스택 실행 권한 해제(Non-Executable Stack), </li>
<li>랜덤 스택(ASLR: Address Space Layout Randomization),</li>
<li>데이터실행 방지(DEP: Data Execution Prevention),</li>
<li>스택 가드(Stack Guard), </li>
<li>스택 실드(Stack Shield) 등</li>
</ul>
</li>
</ul>
</li>
<li>오피스, 어도비(Adobe) 등의 보안 패치<ul>
<li>보안 공격자들이 새롭게 찾아낸 메모리 버퍼 오버플로 공격을 막으려고 프로그램을 수정</li>
</ul>
</li>
<li>시큐어 코딩 : 개발자는 개발 단계에서부터 이러한 메모리 버퍼 오버플로가 발생하지 않도록 안전한 코딩을
하는 것이 필요</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>보안 대책 1: 입력 값에 대한 길이(크기) 검증<pre><code>05: if (argv[1] != NULL &amp;&amp; strlen(argv[1]) &lt; sizeof(buffer) )
06: strcpy(buffer, argv[1]);</code></pre></li>
<li>보안 대책 2: 오버플로에 안전한 라이브러리 사용</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/041df62f-421b-45ad-9269-10ea4ae5005e/image.png" /></p>
<ul>
<li>보안 대책 3: 정적 소스 분석 도구로 미리 수정하기<ul>
<li>예) valgrind, cppch eck, mudflap 등과 같은 상용이나 공개 분석 도구 사용</li>
</ul>
</li>
</ul>
<hr />
<h3 id="②-포맷-스트링-공격">② 포맷 스트링 공격</h3>
<ul>
<li><p>포맷 스트링을 이용해 프로그램의 특정 메모리
내용을 읽거나 스는 보안 공격 기법</p>
<ul>
<li>이 정보를 이용해 악의적인 코드 실행 가능</li>
</ul>
</li>
<li><p>포맷 스트링(Format String)</p>
<ul>
<li>C 언어의 printf( ) 등의 함수에서 사용되는 문자열의
입·출력 형태를 정의하는 문자열</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/43ca0856-39bc-4b84-9ef7-be8209687ddd/image.png" /></p>
<pre><code class="language-c">01: #include &lt;stdio.h&gt;
02: int main(int argc, char* argv[])
03: {
04: int a = 100;
05: printf(&quot;%x \n&quot;, a); // %x의 사용 (➔ 64(16진수) 출력)
06: printf(&quot;%d \n&quot;, a); // %d의 사용 (➔ 100(10진수) 출력)
07: }</code></pre>
<hr />
<ul>
<li>포맷 스트링을 이용한 메모리 주소 확인</li>
</ul>
<pre><code class="language-c">01: #include &lt;stdio.h&gt;
02: int main(int argc, char* argv[])
03: {
04: printf( argv[1] ); // 보안적으로 취약한 코드
05: }</code></pre>
<pre><code>【실행 예】
$ a.out addr-%x [엔터]
addr-eec41a10</code></pre><blockquote>
<p>현재 실행되고 있는 메모리 주소 확인</p>
</blockquote>
<pre><code class="language-c">04: printf(&quot;%s&quot;, argv[1] ); // 보안상 안전한 코드</code></pre>
<pre><code>【실행 예】
$ a.out addr-%x [엔터]
addr-%s</code></pre><hr />
<ul>
<li>포맷 스트링을 이용한 메모리 변조</li>
<li>%n은 메모리 값을 읽은 것이 아닌,
현재까지 화면에 출력된 문자 수를 저장!</li>
</ul>
<pre><code class="language-c">01: #include &lt;stdio.h&gt;
02: int main(int argc, char* argv[])
03: {
04: int value = 100, target = 0;
05: printf(&quot;%d%n \n&quot;, value, &amp;target);
06: printf(&quot;%d \n&quot;, target);
07: printf(&quot;%16d%n\n&quot;, value, &amp;target);
08: printf(&quot;%d \n&quot;, target);
07: }</code></pre>
<pre><code>【실행 예】
$ a.out [엔터]
100
3
100
16</code></pre><hr />
<ul>
<li>포맷 스트링을 이용한 메모리 변조<ul>
<li>포맷 스트링 파라미터 %n은 메모리의 값 저장 : 메모리 변조 가능<ul>
<li>변경하려는 값이 메모리 주소 0xeec41a10 (10진수로는 4005829136) 라면, %4005829136d로 설정</li>
<li>자신이 전달하는 데이터의 길이와 내용을 조절해서 프로그램이 의도하지 않은 방식으로 동작 가능해짐</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code>    eec41a10 → %4005829136d</code></pre><ul>
<li>대응 방안<ul>
<li>%n이나 %hn은 가능한 사용하지 않을 것</li>
<li>소스에 대한 정적 분석 : 이러한 위험 요소를 찾아서 미리 조치 (제거)</li>
</ul>
</li>
</ul>
<hr />
<h3 id="③-경쟁-조건race-condition">③ 경쟁 조건(Race Condition)</h3>
<ul>
<li>여러 개의 프로세스 혹은 스레드가 동시에 공유하는 자원에 대해 동시에 접근하려는 상태<ul>
<li>예) 파일 1개를 2개의 프로세스가 동시에 사용하려고 시도하는 경 우</li>
<li>공유되는 자원을 동시에 여러 개의 프로세스 또는 스레드가 사용 하려고 할 때 자원의 일관성이 깨짐</li>
</ul>
</li>
<li>대응 방안<ul>
<li>동기화 구문 사용 : 한 번에 하나의 프로세스만 접근하도록<ul>
<li>성능 감소가 발생하므로 꼭 필요할 때만 최소화하여 사용해야 함</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5c55e837-5dca-47ca-9937-2d1d444eb987/image.png" /></p>
<hr />
<h2 id="참고-vi-에디터">(참고) vi 에디터</h2>
<ul>
<li>vi 에디터 실행 및 모드<ul>
<li>vi 에디터의 실행<ul>
<li>vi [편집 하려는 file의 경로]</li>
</ul>
</li>
<li>모드<ul>
<li>삽입 모드 : 원하는 글자를 입력하는 상태</li>
<li>명령어 모드 : 방향키로 이동하거나, 글자 삭제 등의 편집이 가능한 상태</li>
<li>라인 편집 모드 : 파일을 저장하거나 종료할 수 있는 상태</li>
</ul>
</li>
</ul>
</li>
</ul>
<p> <img alt="업로드중.." src="blob:https://velog.io/69b20823-e705-42a1-8401-9392b4ac7ce5" /></p>
<hr />
<h3 id="vi-에디터-명령어계속">vi 에디터 명령어(계속)</h3>
<ul>
<li>이동 명령어 </li>
</ul>
<table>
<thead>
<tr>
<th>명령어</th>
<th>의미</th>
<th>비고</th>
</tr>
</thead>
<tbody><tr>
<td><code>h</code></td>
<td>왼쪽으로 한 칸 이동</td>
<td></td>
</tr>
<tr>
<td><code>j</code></td>
<td>아래 줄로 이동</td>
<td></td>
</tr>
<tr>
<td><code>k</code></td>
<td>윗 줄로 이동</td>
<td></td>
</tr>
<tr>
<td><code>l</code></td>
<td>오른쪽으로 한 칸 이동</td>
<td></td>
</tr>
<tr>
<td><code>0</code></td>
<td>현재 줄의 처음으로 이동</td>
<td>숫자 <code>0</code></td>
</tr>
<tr>
<td><code>L</code></td>
<td>화면의 마지막 라인으로 이동</td>
<td></td>
</tr>
<tr>
<td><code>Ctrl+f</code></td>
<td>한 페이지 아래로 이동</td>
<td></td>
</tr>
<tr>
<td><code>Ctrl+b</code></td>
<td>한 페이지 위로 이동</td>
<td></td>
</tr>
</tbody></table>
<ul>
<li>라인 번호</li>
</ul>
<table>
<thead>
<tr>
<th>명령어</th>
<th>의미</th>
<th>비고</th>
</tr>
</thead>
<tbody><tr>
<td><code>set nu</code></td>
<td>Vim에서 라인 번호 출력</td>
<td></td>
</tr>
<tr>
<td><code>set nonu</code></td>
<td>Vim에서 라인 번호 출력 취소</td>
<td></td>
</tr>
</tbody></table>
<ul>
<li>파일 저장 및 종료 명령어</li>
</ul>
<table>
<thead>
<tr>
<th>명령어</th>
<th>의미</th>
<th>비고</th>
</tr>
</thead>
<tbody><tr>
<td><code>:w</code></td>
<td>현재 편집하는 파일을 저장</td>
<td><strong>Write</strong></td>
</tr>
<tr>
<td><code>:q</code></td>
<td>현재 편집하는 파일을 저장하지 않고 종료</td>
<td><strong>Quit</strong></td>
</tr>
<tr>
<td><code>:wq</code></td>
<td>현재 편집하는 파일을 저장하고 종료</td>
<td><strong>Write &amp; Quit</strong></td>
</tr>
<tr>
<td><code>:q!</code></td>
<td>현재 편집하는 파일을 저장하지 않고 강제 종료</td>
<td><strong>Quit (Force)</strong></td>
</tr>
</tbody></table>
<ul>
<li>편집 명령어</li>
</ul>
<table>
<thead>
<tr>
<th>명령어</th>
<th>의미</th>
<th>비고</th>
</tr>
</thead>
<tbody><tr>
<td><code>i</code></td>
<td>현재 커서가 있는 곳에 글자를 추가</td>
<td><strong>Insert</strong></td>
</tr>
<tr>
<td><code>a</code></td>
<td>커서의 우측에 글자를 추가</td>
<td><strong>Append</strong></td>
</tr>
<tr>
<td><code>x</code></td>
<td>현재 커서가 있는 곳의 글자를 삭제</td>
<td></td>
</tr>
<tr>
<td><code>dd</code></td>
<td>현재 커서가 위치한 라인(한 줄)을 삭제</td>
<td><strong>Delete Line</strong></td>
</tr>
<tr>
<td><code>yy</code></td>
<td>현재 줄을 버퍼로 복사</td>
<td><strong>Ctrl + C</strong></td>
</tr>
<tr>
<td><code>p</code></td>
<td>현재 커서가 있는 줄 바로 아래에 붙여넣기</td>
<td><strong>Ctrl + V</strong></td>
</tr>
</tbody></table>
<hr />
<h2 id="참고-vi-에디터-실습">(참고) vi 에디터 실습</h2>
<p>• vi로 test.c 생성 후 컴파일</p>
<p><img alt="업로드중.." src="blob:https://velog.io/499a23c9-87d0-4491-a969-0dde43dac50c" /></p>