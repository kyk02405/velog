<hr />
<h1 id="1-웹이란">1. 웹이란?</h1>
<h2 id="-웹web">• 웹(Web)</h2>
<ul>
<li>하이퍼텍스트(HyperText) 문서들이 인터넷(Internet)을 통해서 연결된 시스템</li>
<li>마치 거미줄(Web) 처럼 복잡하게 연결되었기 때문에 붙여진 이름</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4ee651a9-20c0-4828-b54b-bb7e8c19c642/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/65439376-b5a6-4571-9f12-00029dda47b8/image.png" /></p>
<hr />
<h2 id="-구성">• 구성</h2>
<ul>
<li>통신 프로토콜 : HTTP(HyperText Transfer Protocol)</li>
<li>콘텐트 : 하이퍼텍스트 문서들<ul>
<li>링크(Link, Hyperlink 혹은 참조)를 통해 다른 문서로 접근할 수 있는 문서<ul>
<li>예) HTML(HyperText Markup Language) 문서</li>
</ul>
</li>
</ul>
</li>
<li>주소 체계 : URL(Uniform Resource Locator)</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3df99e75-e4a6-46d6-820f-1dd01d924524/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2df1f240-9f17-4544-8b76-56fa97045d57/image.png" /></p>
<hr />
<h2 id="-웹의-시작">• 웹의 시작</h2>
<ul>
<li>정식 이름: 월드-와이드-웹(WWW: World Wide Web)<ul>
<li>줄여서 WWW 또는 W3라고도 불림</li>
</ul>
</li>
<li>시작: 1989년 유럽 입자 물리 연구소(CERN)<ul>
<li>전 세계 여러 대학과 연구기관에서 흩어져 일하는 물리학자들이 상호간의 신속한 정보 교환과 공동 연구를
위해 고안</li>
<li>소프트웨어 공학자인 팀 버너스 리(Tim Berners Lee) 등에 의해 제안</li>
</ul>
</li>
<li>최초의 웹 페이지와 웹 서버</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/600ce7fd-6e7e-4073-91d0-e6a5c2f03604/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bac5a50f-f0a7-4422-9024-25a64f943995/image.png" /></p>
<hr />
<h1 id="2-http의-개념">2. HTTP의 개념</h1>
<ul>
<li>HTTP(HyperText Transfer Protocol) 통신 프로토콜<ul>
<li>2대의 컴퓨터가 통신하는 경우 한 쪽은 클라이언트, 다른 한 쪽은 서버<ul>
<li>예: 웹 브라우저가 클라이언트가 되어 서버로 요청 메시지를 보내고, 그 결과로 응답(Response) 메시지를전달 받음</li>
</ul>
</li>
<li>클라이언트가 요청 메시지를 먼저 보내고, 그 결과로 응답 메시지를 전달</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8c19c9a2-eaaf-4397-9ec9-b56e9e0e9006/image.png" /></p>
<hr />
<h2 id="21-http-요청-메시지">2.1 HTTP 요청 메시지</h2>
<h3 id="http-요청-메시지-전송">HTTP ‘요청 메시지’ 전송</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3327f9c1-cf28-43fa-8226-c9ff5d09e7dd/image.png" /></p>
<h3 id="get-메소드의-구성">GET 메소드의 구성</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1b1222ea-5b8b-4bfe-8bf8-227ee279445d/image.png" /></p>
<h3 id="post-메소드의-구성">POST 메소드의 구성</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0c6b04af-3e8f-46e8-befc-2238e2c07d2c/image.png" /></p>
<hr />
<h3 id="-구성요소-1--메소드method---서버가-수행해야-할-동작-정의">• 구성요소 1 : 메소드(Method) - 서버가 수행해야 할 동작 정의</h3>
<h3 id="📘-http-메서드-정리">📘 HTTP 메서드 정리</h3>
<table>
<thead>
<tr>
<th>메소드</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td>GET</td>
<td>서버가 자원을 전송해 줄 것을 요청</td>
</tr>
<tr>
<td>POST</td>
<td>요청 바디(Body)를 통해 클라이언트가 서버로 데이터 전송</td>
</tr>
<tr>
<td>HEAD</td>
<td>서버가 (자원 내용은 전송하지 않고) 헤더만 전송해 줄 것을 요청</td>
</tr>
<tr>
<td>OPTIONS</td>
<td>서버가 지원하는 메소드들 질의</td>
</tr>
<tr>
<td>TRACE</td>
<td>클라이언트가 보낸 요청을 그대로 반환</td>
</tr>
<tr>
<td>PUT</td>
<td>클라이언트가 서버의 지정한 URI로 자원을 전송</td>
</tr>
<tr>
<td>DELETE</td>
<td>서버의 자원을 삭제</td>
</tr>
<tr>
<td>CONNECT</td>
<td>프록시 터널링을 위해 예약된 메소드</td>
</tr>
</tbody></table>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/58b6910f-6197-49fb-af85-0768f8a4b1f2/image.png" /></p>
<hr />
<h3 id="-구성요소-2--요청-uri">• 구성요소 2 : 요청 URI</h3>
<ul>
<li>상대 경로 및 절대 경로(Absolute path)로 요청 가능</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f7d5124f-c75f-4bcc-9be8-679da2223a87/image.png" /></p>
<hr />
<h3 id="-구성요소-3--프로토콜-버전---http-프로토콜을-이용하여-통신을-할-때-사용하는-버전-정의">• 구성요소 3 : 프로토콜 버전 - HTTP 프로토콜을 이용하여 통신을 할 때 사용하는 버전 정의</h3>
<h3 id="🌐-http-버전-정리">🌐 HTTP 버전 정리</h3>
<table>
<thead>
<tr>
<th>버전</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td>HTTP/0.9</td>
<td>최초 정식 버전(1.0)의 이전 버전. GET 메서드만 지원하며 헤더가 없음. 현재는 사용되지 않음.</td>
</tr>
<tr>
<td>HTTP/1.0</td>
<td>1996년 5월 RFC1945로 정의된 최초의 정식 버전. 초기 버전이지만 아직도 많은 웹 서버가 지원함.</td>
</tr>
<tr>
<td>HTTP/1.1</td>
<td>1997년 1월 발표, 가장 일반적으로 사용되는 버전. 이후 RFC2616, RFC7230~RFC7235로 개정되어 가장 최신의 1.x 버전.</td>
</tr>
<tr>
<td>HTTP/2.0</td>
<td>2015년 5월 RFC7540으로 발표. HTTP/1.1과의 호환성을 유지하면서도 다중화, 헤더 압축 등으로 성능 개선을 목표로 개발됨. 여전히 HTTP/1.1이 더 많이 사용됨.</td>
</tr>
</tbody></table>
<hr />
<h3 id="-구성요소-4--헤더---요청-시에-필요한-조건이나-특성-등을-나타내는-필드field">• 구성요소 4 : 헤더 - 요청 시에 필요한 조건이나 특성 등을 나타내는 필드(Field)</h3>
<h3 id="📑-http-헤더의-예">📑 HTTP 헤더의 예</h3>
<table>
<thead>
<tr>
<th>헤더</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td>Host: <a href="http://www.infinitybooks.co.kr">www.infinitybooks.co.kr</a></td>
<td>필드 이름: Host<br />필드 값: <a href="http://www.infinitybooks.co.kr">www.infinitybooks.co.kr</a><br />의미: 요청하는 호스트 정보 지정</td>
</tr>
<tr>
<td>Content-Type: text/html</td>
<td>필드 이름: Content-Type<br />필드 값: text/html<br />의미: 데이터의 타입 지정</td>
</tr>
<tr>
<td>Keep-Alive: timeout=30, max=200</td>
<td>필드 이름: Keep-Alive<br />필드 값: timeout=30 및 max=200<br />의미: 세션 유지 정보 지정</td>
</tr>
</tbody></table>
<hr />
<h3 id="-구성요소-5--요청-바디body---클라이언트가-서버로-보내는-추가적인-데이터">• 구성요소 5 : 요청 바디(Body) - 클라이언트가 서버로 보내는 추가적인 데이터</h3>
<ul>
<li>POST 메소드를 사용할 경우 추가됨</li>
<li>다양한 포맷의 데이터가 추가 가능<ul>
<li>폼(form)에 기입한 이름 혹은 주소</li>
<li>첨부 파일과 같은 바이너리 파일(Binary File) 등</li>
</ul>
</li>
<li>본문의 형식은 Content-Type 헤더에 따름</li>
</ul>
<hr />
<h2 id="22-http-응답-메시지">2.2 HTTP 응답 메시지</h2>
<h3 id="http-응답-메시지-전송">HTTP ‘응답 메시지’ 전송</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d20bf5ac-ca40-42f1-bf9f-0e0dfbd1397e/image.png" /></p>
<hr />
<h3 id="-응답-메시지의-구성--5가지">• 응답 메시지의 구성 : 5가지</h3>
<ul>
<li>구성요소 1 : 프로토콜 버전 - 서버가 사용하는 HTTP 버전</li>
<li>구성요소 2 와 3 : 상태 코드 및 상태 코드 설명</li>
<li>구성요소 4 : 응답 헤더 - 전달할 데이터의 형식과 길이 등의 메타 정보</li>
<li>구성요소 5 : 응답 바디 - 클라이언트의 요청에 대한 결과</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/794e795e-3c23-483a-b128-70fb4e81d47d/image.png" /></p>
<h3 id="📊-http-응답-상태-코드">📊 HTTP 응답 상태 코드</h3>
<table>
<thead>
<tr>
<th>값의 범위</th>
<th>구분</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td>100~199</td>
<td>정보 전송 (Information)</td>
<td>요청을 받아 처리가 계속되고 있음 (프로토콜 전환 등)</td>
</tr>
<tr>
<td>200~299</td>
<td>성공 (Success)</td>
<td>요청이 정상적으로 처리됨<br />200: OK<br />201: Created<br />202: Accepted<br />204: No content</td>
</tr>
<tr>
<td>300~399</td>
<td>리다이렉션 (Redirection)</td>
<td>요청을 처리하기 위해 클라이언트가 다른 URL로 이동해야 함</td>
</tr>
<tr>
<td>400~499</td>
<td>클라이언트 오류 (Client error)</td>
<td>클라이언트 요청에 문제 발생<br />400: Bad request<br />401: Unauthorized<br />403: Forbidden<br />404: Not found</td>
</tr>
<tr>
<td>500~599</td>
<td>서버 오류 (Server error)</td>
<td>서버에서 오류 발생<br />500: Internal server error<br />501: Not implemented<br />503: Service unavailable</td>
</tr>
</tbody></table>
<hr />
<h2 id="-http-의-특징">• HTTP 의 특징</h2>
<h3 id="-http는-비연결지향connectionless-프로토콜">• HTTP는 비연결지향(Connectionless) 프로토콜</h3>
<ul>
<li>클라이언트가 요청을 서버에 보내면 서버는 클라이언트에게 요청에 맞는 응답을 보내고 접속을 끊는다</li>
<li>성능상 비효율적<ul>
<li>클라이언트가 새로운 요청을 보낼 때마다 접속을 새로 해야 함</li>
</ul>
</li>
<li>프로토콜 상의 개선<ul>
<li>HTTP/1.0 버전: 한 번의 접속으로 여러 개의 요청과 응답을 반복 가능</li>
<li>HTTP/1.1 버전: 특정 시간동안 접속을 계속 열어두고(연결을 유지하고) 요청을 보낼 수 있도록 하는 기능 추가
→ Keep-alive 기본 사용 되었다<ul>
<li>요청 헤더의 Keep-alive라는 필드 값 : ‘얼마 동안 접속을 열어 둘 것인가?<h3 id="-http는-상태-정보-유지안함stateless-프로토콜">• HTTP는 상태 정보 유지안함(Stateless) 프로토콜</h3>
</li>
</ul>
</li>
</ul>
</li>
<li>‘상태 정보’를 저장해야 할 경우에 대한 대안 : 쿠키와 세션</li>
</ul>
<hr />
<h3 id="-쿠키cookie">• 쿠키(Cookie):</h3>
<ul>
<li>클라이언트에 저장되는 키와 값이 들어있는 작은 데이터 파일<ul>
<li>클라이언트의 상태 정보를 로컬에 저장했다가 참조</li>
<li>클라이언트의 컴퓨터에 작은 파일로 저장<ul>
<li>응답메시지를 보낼 때 헤더에 Set-Cookie 값을 설정하면 클라이언트에 쿠키 생성됨</li>
<li>이름, 값, 경로 정보뿐 아니라 만료 날짜(쿠키 저장기간)가 설정됨</li>
<li>사용자마다 다르게 적절한 페이지를 보여줄 수 있음 ex) 쇼핑몰, 검색내역, “다시 보지 않기“ 팝업창 체크 등</li>
<li>C:\Users&lt;username&gt;\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c737074f-9963-41e0-bee6-e5589b91459c/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6d35de87-6220-400a-8db9-2339fd83f6b2/image.png" /></p>
<hr />
<h3 id="-세션session">• 세션(Session):</h3>
<ul>
<li>서버는 일정 시간 동안 같은 클라이언트로부터 전달되는 요청들을 하나의 그룹으로
보고, 하나의 세션으로 식별함<ul>
<li>클라이언트가 서버로 최초 요청을 보내면, 유일한 식별자(ID)인 세션 ID를 부여</li>
<li>서버의 메모리에 저장(객체) → 세션이 생길 때마다 서버의 리소스 차지</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/57ae5e3c-4b15-437d-b06a-7262d20a94a4/image.png" /></p>
<hr />
<h1 id="3-하이퍼텍스트-및-uri">3. 하이퍼텍스트 및 URI</h1>
<h2 id="31-html-및-스크립트">3.1 HTML 및 스크립트</h2>
<h3 id="-html-문서-생성">• HTML 문서 생성</h3>
<ul>
<li>정적인(Static) 콘텐트 : 내용의 변경 없음 → 웹 서버는 파일을 읽어서 그 내용을 전송</li>
<li>동적(Dynamic) 콘텐트 : 사용자의 상황에 혹은 요청에 따라 내용이 달라짐<ul>
<li>서버 사이드 스크립트 언어(SSL: Server-side Script Language)<ul>
<li>JSP(Java Server Page), ASP(Active Server Page), PHP(Personal Home Page) 등</li>
</ul>
</li>
<li>웹 서버가 SSL로 작성된 페이지를 내부적으로 실행 → 실행 결과 HTML문서 전송<ul>
<li>예) select.jsp라는 웹 페이지를 호출 : 입력 파라미터(parameter) id=100</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d0d920ea-90c1-4916-b027-e43981a00c6f/image.png" /></p>
<hr />
<h3 id="-클라이언트-사이드-스크립트-csl-client-side-script-language">• 클라이언트 사이드 스크립트 (CSL: Client-side Script Language)</h3>
<ul>
<li>정적 혹은 동적 방식으로 구해진 HTML 문서는 웹 브라우저로 전달<ul>
<li>클라이언트인 웹 브라우저에서 실행되는 스크립트<ul>
<li>동적으로 화면 내용을 만들거나 혹은 다양한 UI(User Interface) 제공</li>
</ul>
</li>
<li>JS(Java Script), VBS(Visual Basic Script) 등</li>
</ul>
</li>
<li>HTML 문서에 포함되어 동작</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9fad597a-08ca-46a1-8897-5dcad77bb3b3/image.png" /></p>
<hr />
<h3 id="-입력-파라미터의-전달">• 입력 파라미터의 전달</h3>
<ul>
<li>GET 메소드 사용 : 보안적으로 권장되지 않음<ul>
<li>요청 파라미터가 요청 URI에 포함 → 사용자에게 노출</li>
<li>select.jsp?id=100</li>
</ul>
</li>
<li>POST 메소드 사용 : 보안적으로 우수<ul>
<li>파라미터 정보가 요청 바디(Body)에 포함 → 사용자에게 노출되지 않음</li>
<li>주소창에 select.jsp로 노출되며, id=100은 요청바디(Body)에 포함</li>
</ul>
</li>
</ul>
<hr />
<h2 id="32-uri">3.2 URI</h2>
<h3 id="-uriuniform-resource-identifier">• URI(Uniform Resource Identifier):</h3>
<ul>
<li>인터넷의 특정 자원(Resource)에 접근하기 위해 사용하는 식별자</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/732c8149-fb2d-4568-8427-e1b43f98b350/image.png" /></p>
<ul>
<li>URL은 URI의 하위 집합: <a href="http://www.infinitybooks.co.kr%EA%B3%BC">www.infinitybooks.co.kr과</a> 같이 특정 서버를 표시
→ 일반적으로 URI를 URL로 부른다</li>
</ul>
<hr />
<h3 id="-uri-형식">• URI 형식</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3410eba5-a9bf-4e65-aab4-4d614e6233ab/image.png" /></p>
<ul>
<li>스키마 이름 : 어떤 프로토콜을 사용할지 지정 (http, https, mailto, ws, file 등)</li>
<li>자격(인증) 정보 : 서버에서 자원을취득하는데 필요한사용자이름과패스워드등의자격(인증) 정보, 생략가능</li>
<li>서버의 호스트 이름(FQDN) 혹은 IP 주소</li>
<li>서버 포트 번호 : 네트워크의 포트 번호, 생략될 경우 기본 포트 번호 사용</li>
<li>계층적 파일 경로 : 요청하는 자원의 경로</li>
<li>질의 문자열(Query String) : 임의의 매개변수를 전달하기 위한 목적, 생략 가능</li>
<li>단편 식별자 : 취득한 자원에서 그 하위에 있는 특정 부분을 # 등으로 가리키는 것으로 선택 사항</li>
</ul>
<hr />
<h3 id="-퍼센트-인코딩">• 퍼센트 인코딩</h3>
<h4 id="🧪-javascript-encodeuri-사용-예">🧪 JavaScript: <code>encodeURI()</code> 사용 예</h4>
<pre><code class="language-javascript">const uri = &quot;https://mozilla.org/?x=шеллы&quot;;
const encoded = encodeURI(uri);
console.log(encoded);
// Expected output: &quot;https://mozilla.org/?x=%D1%88%D0%B5%D0%BB%D0%BB%D1%8B&quot;

try {
  console.log(decodeURI(encoded));
  // Expected output: &quot;https://mozilla.org/?x=шеллы&quot;
} catch (e) {
  // Catches a malformed URI
  console.error(e);
}</code></pre>
<ul>
<li>URI에서 사용할 수 없는 문자를 표현할 때 사용되는 인코딩 방식</li>
<li>URL 인코딩이라고도 함(RFC3986에 정의)</li>
<li>대상이 되는 문자는 바이트 단위로 나뉘어 16진수 형태로 표시<ul>
<li>예: ‘웹보안’ 이라는 문자열을 UTF-8 문자열로 인코딩
%EC%9B%B9%EB%B3%B4%EC%95%88</li>
<li><a href="https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/encodeURI">https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/encodeURI</a></li>
</ul>
</li>
<li>예외 : HTTP의 POST 메소드를 사용하여 웹 폼 문자열을 전송할 때 MIME의 Content-Type에 ‘application/xxxx-form-urlencoded’가 사용되면 공백이 ‘%20’이 아니라 ‘+’로 변경</li>
</ul>
<h4 id="🔡-url-인코딩-예">🔡 URL 인코딩 예</h4>
<table>
<thead>
<tr>
<th>문자</th>
<th>인코딩 값</th>
</tr>
</thead>
<tbody><tr>
<td><code>=</code></td>
<td><code>%3D</code></td>
</tr>
<tr>
<td><code>%</code></td>
<td><code>%25</code></td>
</tr>
<tr>
<td>공백</td>
<td><code>%20</code> 또는 <code>+</code></td>
</tr>
</tbody></table>
<blockquote>
<p>문맥에 따라 문자 <code>' '</code>는 <code>application/x-www-form-urlencoded</code> 메시지에서 퍼센트 인코딩처럼 <code>'+'</code>로 변환되며, URL에서는 <code>'%20'</code>으로 변환됩니다.</p>
</blockquote>
<hr />
<h1 id="4-웹-취약점-정보-수집">4. 웹 취약점 정보 수집</h1>
<h2 id="-웹-취약점-스캐너">• 웹 취약점 스캐너</h2>
<ul>
<li>웹 사이트의 취약점을 점검해주는 프로그램</li>
<li>점검 대상이 되는 웹 사이트의 문제점에 대한 해결 방안을 제시</li>
<li>오픈VAS(OpenVAS), 레티나 CS 커뮤니티(Retina CS Community), MBSA(Microsoft Baseline Security Analyzer) 등<ul>
<li>우리나라 대표 분석 도구 스패로우
<a href="https://api.velog.io/rss/(https:/sparrow.im/kr/)">링크텍스트</a></li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e65c3068-235d-4427-bcc0-0cacfd4819d1/image.png" /></p>
<hr />
<h2 id="-acunetix">• Acunetix</h2>
<ul>
<li><a href="http://www.acunetix.com">http://www.acunetix.com</a><h3 id="데모trial-버전">데모(Trial) 버전</h3>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/591529cd-16d4-40bf-97dc-a107e477d490/image.png" /></p>
<h3 id="메인-화면">메인 화면</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fccd30d9-76b5-4418-a63f-16bf2bfcea35/image.png" /></p>
<h3 id="스캔-시작">스캔 시작</h3>
<ul>
<li>크롤링(Crawling): 시작 주소 페이지에 연결된 링크들을 이용하여 연결된 홈페이지들을 모두 검사하는 방법</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1c633f83-3f58-4287-a7d4-d4eab296cf00/image.png" /></p>
<h3 id="점검-대상-사이트-정보-입력ippw">점검 대상 사이트 정보 입력(IP/PW)</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4350015f-e9bf-4197-ba4d-9793728e8064/image.png" /></p>
<h3 id="취약점-검사-결과">취약점 검사 결과</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4ec00589-c520-40c8-ac59-44cc14f9063c/image.png" /></p>
<hr />
<h1 id="5-웹-취약점-및-보안-대책">5. 웹 취약점 및 보안 대책</h1>
<h2 id="owaspthe-open-web-application-security-project">OWASP(The Open Web Application Security Project)</h2>
<ul>
<li>비영리 국제 단체, 웹 서버 보안과 관련하여 공신력 있는 기관</li>
<li><a href="https://www.owasp.org">https://www.owasp.org</a></li>
<li>OWASP TOP 10<ul>
<li>웹 관련 보안 취약점 중 많이 발생하고 영향도가 큰 이슈 10가지 선정</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b2817a4a-a14d-4f34-b069-f46708e93d54/image.png" /></p>
<hr />
<h2 id="51-sql-인젝션">5.1 SQL 인젝션</h2>
<ul>
<li>데이터베이스와 관련된 보안 취약점: 사용자가 입력하는 입력 값에 대한 유효성을 검증하지 않고
그대로 사용할 때 발생 가능<ul>
<li>SQL 질의(Query)가 악의적으로 변조(악용) → 사용자 인증을 우회하거나 데이터베이스에 저장된 데이터가
변조되거나 파괴될 수 있음</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/011ac399-3cfc-4f1e-8206-4dd5977dd17a/image.png" /></p>
<h3 id="보안-대책-1--매개변수-바인딩-기법-사용">보안 대책 1 : 매개변수 바인딩 기법 사용</h3>
<ul>
<li>질의문 변조가 발생하지 않음<h4 id="🔐-매개변수-사용-예">🔐 매개변수 사용 예</h4>
</li>
</ul>
<table>
<thead>
<tr>
<th>항목</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td>매개변수 사용</td>
<td><code>SELECT * FROM member WHERE ID = ? AND PW = ?</code><br />사용자가 입력한 ID와 PW 값은 별도의 매개변수로 전달</td>
</tr>
</tbody></table>
<h4 id="⚠️-취약한-코드-sql-injection-위험">⚠️ 취약한 코드 (SQL Injection 위험)</h4>
<pre><code class="language-python">from sqlalchemy.orm import Session
from models import Member  # Member는 SQLAlchemy 모델이라고 가정합니다.

def find_by_name(name: str, session: Session):
    query = f&quot;SELECT * FROM members WHERE name = '{name}'&quot;
    return session.execute(query).fetchall()</code></pre>
<blockquote>
<p>위 코드는 사용자 입력값을 직접 SQL 쿼리에 삽입하므로 SQL Injection 공격에 취약합니다.</p>
</blockquote>
<h4 id="✅-안전한-코드-parameter-binding-사용">✅ 안전한 코드 (Parameter Binding 사용)</h4>
<pre><code class="language-python">from sqlalchemy.orm import Session
from models import Member  # Member는 SQLAlchemy 모델이라고 가정합니다.

def find_by_name(name: str, session: Session):
    query = &quot;SELECT * FROM members WHERE name = :name&quot;
    return session.execute(query, {&quot;name&quot;: name}).fetchall()</code></pre>
<blockquote>
<p>위 코드는 SQLAlchemy의 parameter binding을 사용하여 SQL Injection 공격을 방지합니다.</p>
</blockquote>
<hr />
<h3 id="보안-대책-2--입력-값에-대한-특수문자-검증">보안 대책 2 : 입력 값에 대한 특수문자 검증</h3>
<ul>
<li>사용자 입력에서 특수문자<code>(' &quot; / \ (공백 space) ; : -- # 등)</code>가 포함되어 있는지 검사</li>
<li>허용되지 않은 문자열이나 문자가 포함된 경우에는 제거<ul>
<li>MS SQL Server와 Oracle에서 주석문 :<code>--</code></li>
<li>MySQL의 주석문 : <code>#</code></li>
</ul>
</li>
</ul>
<h4 id="🧹-사용자-입력-값에서-특수문자-제거-후-문자열-조합">🧹 사용자 입력 값에서 특수문자 제거 후 문자열 조합</h4>
<pre><code class="language-java">String name = request.getProperty(&quot;user&quot;);
if (name != null &amp;&amp; !&quot;&quot;.equals(name)) {
    name = name.replaceAll(&quot;/&quot;, &quot;&quot;);
    name = name.replaceAll(&quot;\\\\&quot;, &quot;&quot;);  // 백슬래시는 이스케이프 필요
    name = name.replaceAll(&quot;\\.&quot;, &quot;&quot;);
    name = name.replaceAll(&quot;&amp;&quot;, &quot;&quot;);
    name = name + &quot;-report&quot;;
}</code></pre>
<blockquote>
<p>입력값 <code>name</code>에서 <code>/</code>, <code>\</code>, <code>.</code>, <code>&amp;</code> 특수문자를 제거하고, <code>&quot;report&quot;</code>를 뒤에 붙여 처리합니다.<br />보안과 무결성 확보를 위한 전처리 방식입니다.</p>
</blockquote>
<hr />
<h2 id="52-경로-조작">5.2 경로 조작</h2>
<ul>
<li>사용자가 입력하는 입력 값에 대한 유효성을 검증하지 않고 그대로 사용할 때 발생할 수 있는 서버
시스템 자원 접근에 대한 보안 취약점</li>
<li>사용자가 접근해서는 안 되는 서버의 중요 파일을 내려받거나 혹은 삭제(상대경로 활용)</li>
<li>보안 대책 : 입력 값 특수문자<code>(‘, “, /, \, ;, :, --, +, 공백)</code> 검사, 해당 문자 제거</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/10e37168-7d0e-4905-9fd1-c61cf656624e/image.png" /></p>
<hr />
<h2 id="53-위험한-형식-파일-업로드">5.3 위험한 형식 파일 업로드</h2>
<ul>
<li>유효성 점검의 대상이 사용자가 업로드 하려는 파일</li>
<li>웹 셸(Web Shell) : 사용자가 올린 파일이 웹 서버에서 실행되면서 보안 공격자가 외부에서 웹
서버를 통해 서버를 원격 조종 하게 하는 파일<ul>
<li>파일 확장자 : <code>.asp, .jsp, .php</code> 등</li>
<li>지속적으로 다양한 보안 공격 시도가 가능해짐</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/99df4451-b0f3-45b2-bdec-515938450221/image.png" /></p>
<hr />
<h3 id="보안-대책">보안 대책</h3>
<ul>
<li>화이트리스트 방식의 허용된 확장자(*.jpg, *.doc 등)만 업로드 허용</li>
<li>서버에 파일을 저장할 때 파일 이름과 경로를 임의의 문자열로 변경하여 저장<ul>
<li><code>my.doc → 459123.tmp</code></li>
</ul>
</li>
<li>파일 저장 경로가 웹 서버의 문서 디렉터리 아래가 아니라 전혀 다른 곳으로 설정<ul>
<li><code>c:\apache/htdocs → d:\file_root</code></li>
</ul>
</li>
<li>파일이 서버에서 실행될 수 없도록 실행 속성을 제거</li>
</ul>
<hr />
<h2 id="54-크로스사이트-스크립트xss-cross-site-script">5.4 크로스사이트 스크립트(XSS: Cross-Site Script)</h2>
<ul>
<li>웹 브라우저에서 사용자가 입력하는 입력 값에 대한 유효성을 검증하지 않고 그대로 웹 서버로
전송했을 때 발생할 수 있는 보안 취약점</li>
<li>악성 스크립트를 웹 서버에 저장 → 같은 웹 서버에 접속한 다른 사용자들에게 배포되어 추가 보안 사고 발생</li>
<li>일반적으로 자바스크립트에서 주로 발생</li>
<li>VB 스크립트, ActiveX 등 클라이언트에서 실행되는 동적 데이터를 생성하는 모든 언어에서 발생 가능</li>
<li>보안 대책 : 사용자 입력 값에 대한 특수문자 검증</li>
</ul>
<h4 id="🔒-xss-대비-문자열-대체">🔒 XSS 대비 문자열 대체</h4>
<table>
<thead>
<tr>
<th>원본 문자(기호)</th>
<th>대체 문자열</th>
</tr>
</thead>
<tbody><tr>
<td><code>&lt;</code></td>
<td><code>&amp;lt;</code></td>
</tr>
<tr>
<td><code>&gt;</code></td>
<td><code>&amp;gt;</code></td>
</tr>
<tr>
<td><code>'</code></td>
<td><code>&amp;amp;</code></td>
</tr>
<tr>
<td><code>&quot;</code></td>
<td><code>&amp;quot;</code></td>
</tr>
</tbody></table>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8f186dd5-edc9-4e96-abfd-ca280b777d49/image.png" /></p>
<hr />
<h2 id="55-적절한-인증-없는-중요-기능-허용">5.5 적절한 인증 없는 중요 기능 허용</h2>
<h4 id="🔐-인증-점검-로직-비교">🔐 인증 점검 로직 비교</h4>
<h4 id="안전하지-않은-코드">안전하지 않은 코드</h4>
<ul>
<li>인증 점검 로직이 없이 비즈니스 로직을 호출함  </li>
</ul>
<pre><code class="language-jsp">&lt;%
……
ShowAccountInfo();
……
%&gt;</code></pre>
<h4 id="인증-점검이-포함된-안전한-코드">인증 점검이 포함된 안전한 코드</h4>
<ul>
<li>인증 점검 로직을 먼저 호출한 다음 비즈니스 로직을 호출함   </li>
</ul>
<pre><code class="language-jsp">&lt;%
……
if (CheckAuthentication()) { // 🔴 인증 여부 확인
    ShowAccountInfo();
} else {
    // 인증 오류 처리
    // ex) 로그인 페이지로 리다이렉트
    ……
}
……
%&gt;</code></pre>
<blockquote>
<p>🔴 <code>CheckAuthentication()</code> : 인증 여부를 판단하는 핵심 함수로, 반드시 먼저 호출해야 함.</p>
</blockquote>
<hr />
<h2 id="56-부적절한-인가">5.6 부적절한 인가</h2>
<h3 id="적절한-인가authorization">적절한 인가(Authorization)</h3>
<ul>
<li>점검 없이 비즈니스 로직 수행<h3 id="인가-">인가 :</h3>
</li>
<li>사용자의 자원에 대한 접근 또는 사용을 허용하는 과정<ul>
<li>로그인에 성공한 사용자가 어떠한 행위를 하려 할 때 이것을 허용할지 결정</li>
<li>어떤 객체를 대상으로 어떤 사용자/그룹에게 어떤 권한을 부여할지 결정(설계)</li>
<li>ex) guest로 로그인했음에도 불구하고 관리자의 기능을 정상적으로 수행하면 안됨</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/77d8eb51-891f-4221-90fc-c62436ecca47/image.png" /></p>
<hr />
<h4 id="🔐-인증·인가-점검-로직-비교">🔐 인증·인가 점검 로직 비교</h4>
<h4 id="안전하지-않은-코드-1">안전하지 않은 코드</h4>
<ul>
<li>인가 점검 로직 없이 비즈니스 로직을 호출함  </li>
</ul>
<pre><code class="language-jsp">&lt;%
……
if (CheckAuthentication()) {
    ShowAdminInfo();
} else {
    // 인증 오류 처리
}
……
%&gt;</code></pre>
<h4 id="인증과-인가-점검이-포함된-안전한-코드">인증과 인가 점검이 포함된 안전한 코드</h4>
<ul>
<li>인증 → 인가 순으로 점검 후 비즈니스 로직을 호출함  </li>
</ul>
<pre><code class="language-jsp">&lt;%
……
if (CheckAuthentication()) { // 🔴 인증 여부 확인
    if (CheckAuthorization()) { // 🔵 인가 여부 확인
        ShowAdminInfo();
    } else {
        // 인가 오류 처리
    }
} else {
    // 인증 오류 처리
}
……
%&gt;</code></pre>
<blockquote>
<p>🔴 <code>CheckAuthentication()</code> : 사용자의 로그인 여부를 확인<br />🔵 <code>CheckAuthorization()</code> : 권한이 있는 사용자만 접근 가능하도록 제한</p>
</blockquote>
<hr />
<h2 id="57-중요-정보-평문-저장전송과-취약한-암호화-알고리즘-사용">5.7 중요 정보 평문 저장/전송과 취약한 암호화 알고리즘 사용</h2>
<ul>
<li>파일, 데이터베이스 또는 메모리에 중요 데이터(주민번호, 여권번호 등) 저장
→ 반드시 암호화해서 저장해야 됨</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/150850c6-4668-49eb-9fa8-189388a3c972/image.png" /></p>
<hr />
<h4 id="🔐-파일-저장-시-암호화-여부-비교">🔐 파일 저장 시 암호화 여부 비교</h4>
<h4 id="안전하지-않은-코드-2">안전하지 않은 코드</h4>
<ul>
<li>파일에 중요한 데이터를 저장할 때 암호화하지 않고 저장함  </li>
</ul>
<pre><code class="language-jsp">&lt;%
……
file.write(password);
……
%&gt;</code></pre>
<h4 id="암호화를-적용한-안전한-코드">암호화를 적용한 안전한 코드</h4>
<ul>
<li>파일에 중요한 데이터를 저장할 때 암호화하여 저장함  </li>
</ul>
<pre><code class="language-jsp">&lt;%
……
file.write(EncryptString(password));
……
%&gt;</code></pre>
<blockquote>
<p>🔒 <code>EncryptString()</code> : 민감한 데이터를 암호화하는 함수로, 저장 전 반드시 적용해야 함</p>
</blockquote>
<hr />
<h3 id="안전한-암호화-알고리즘">안전한 암호화 알고리즘</h3>
<ul>
<li><a href="https://seed.kisa.or.kr/kisa/index.do">https://seed.kisa.or.kr/kisa/index.do</a></li>
<li>길이가 짧은 암호키는 보안 측면에서 취약<ul>
<li>공격자가 짧은 시간 안에 키를 찾을 수 있음</li>
</ul>
</li>
</ul>
<h4 id="🔐-안전한-암호화-알고리즘-암호화-알고리즘-검증기준-ver-20">🔐 안전한 암호화 알고리즘 (암호화 알고리즘 검증기준 Ver 2.0)</h4>
<table>
<thead>
<tr>
<th>분류</th>
<th>안전한 알고리즘</th>
<th>키 길이</th>
</tr>
</thead>
<tbody><tr>
<td>대칭키(블록 암호)</td>
<td>ARIA</td>
<td>128 / 192 / 256</td>
</tr>
<tr>
<td></td>
<td>SEED</td>
<td>128</td>
</tr>
<tr>
<td>비대칭키(공개키)</td>
<td>RSA</td>
<td>2048 / 3072</td>
</tr>
<tr>
<td>해시 함수</td>
<td>SHA-2</td>
<td>224 / 256 / 384 / 512 <em>(해시 결과 크기)</em></td>
</tr>
</tbody></table>
<blockquote>
<p>※ 해시 함수는 '키 길이'가 아니라 <strong>해시 결과의 크기</strong>를 뜻함.</p>
</blockquote>
<hr />
<h4 id="-인터넷-등과-같은-통신-채널을-통해서-민감한-정보-전송">• 인터넷 등과 같은 통신 채널을 통해서 민감한 정보 전송</h4>
<p>→ 반드시 암호화해서 전송(SSL/TLS) (스니핑 대비)</p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ef93e592-cbb0-45d0-ba28-cd98099c8dfe/image.png" /></p>
<hr />
<h4 id="🔐-평문-vs-암호화-통신-비교">🔐 평문 vs 암호화 통신 비교</h4>
<table>
<thead>
<tr>
<th>구분</th>
<th>안전하지 않은 코드 / 평문으로 통신</th>
<th>안전한 코드 / 암호화하여 통신</th>
</tr>
</thead>
<tbody><tr>
<td><strong>서버</strong></td>
<td><code>java&lt;br&gt;Socket s = new ServerSocket(8899).accept();&lt;br&gt;</code></td>
<td><code>java&lt;br&gt;SSLServerSocketFactory f = (SSLServerSocketFactory) SSLServerSocketFactory.getDefault();&lt;br&gt;SSLServerSocket s = (SSLServerSocket) f.createServerSocket(8899);&lt;br&gt;</code></td>
</tr>
<tr>
<td><strong>클라이언트</strong></td>
<td><code>java&lt;br&gt;Socket s = new Socket(server_ip, 8899);&lt;br&gt;</code></td>
<td><code>java&lt;br&gt;SSLSocketFactory f = (SSLSocketFactory) SSLSocketFactory.getDefault();&lt;br&gt;SSLSocket s = (SSLSocket) f.createSocket(server_ip, 8899);&lt;br&gt;</code></td>
</tr>
</tbody></table>
<blockquote>
<p>🔐 평문 전송은 도청 및 정보 유출 위험이 있으며, SSL을 사용한 암호화 통신으로 반드시 보호해야 함.</p>
</blockquote>
<hr />
<h2 id="58-부적절한-오류-처리">5.8 부적절한 오류 처리</h2>
<h3 id="오류-메시지를-통한-정보-노출">오류 메시지를 통한 정보 노출</h3>
<ul>
<li>웹서버의 종류</li>
<li>스택 트레이스를 통한 내부 로직 정보</li>
<li>데이터베이스 종류</li>
<li>운영체제 종류</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/51b9dd8f-08f0-4b71-aff5-9ff0b1432ee1/image.png" /></p>
<blockquote>
<p>노출된 오류 메세지의 예</p>
</blockquote>
<hr />
<h4 id="🔐-예외-처리-시-메시지-출력-방식-비교">🔐 예외 처리 시 메시지 출력 방식 비교</h4>
<table>
<thead>
<tr>
<th>구분</th>
<th>안전하지 않은 코드 / 필요 없는 오류 메시지 내용까지 출력</th>
<th>안전한 코드 / 최소한의 오류 메세지 내용만 출력</th>
</tr>
</thead>
<tbody><tr>
<td>예외 처리 방식</td>
<td><code>java&lt;br&gt;catch(Exception e) {&lt;br&gt; e.printStackTrace();&lt;br&gt;}</code></td>
<td><code>java&lt;br&gt;catch(Exception e) {&lt;br&gt; System.out.println(&quot;내부 오류가 발생하였습니다&quot;);&lt;br&gt;}</code></td>
</tr>
</tbody></table>
<blockquote>
<p>⚠️ <code>printStackTrace()</code>는 시스템 내부 정보까지 노출될 수 있어 보안상 위험.<br />✅ 사용자에게는 최소한의 메시지만 제공하고, 상세 정보는 로그에만 기록하도록 구성해야 함.</p>
</blockquote>
<hr />
<h3 id="오류-상황-대응-부재와-부적절한-예외-처리">오류 상황 대응 부재와 부적절한 예외 처리</h3>
<ul>
<li>공격자는 일부러 오류상황 또는 예외 상황을 발생시킴
→ 오류 처리 로직이 없거나 적절하지 않으면 해당 취약점을 통해 공격 시도</li>
</ul>
<h4 id="🔐-예외-처리-로직-유무-비교">🔐 예외 처리 로직 유무 비교</h4>
<table>
<thead>
<tr>
<th>구분</th>
<th>안전하지 않은 코드     / 오류 처리 로직이 없음</th>
<th>안전한 코드 / 적절한 오류 처리 로직이 있음</th>
</tr>
</thead>
<tbody><tr>
<td>예외 처리 누락 여부</td>
<td><code>java&lt;br&gt;catch(Exception e) {&lt;br&gt;}&lt;br&gt;</code></td>
<td><code>java&lt;br&gt;catch(Exception e) {&lt;br&gt; System.out.println(&quot;내부 오류가 발생하였습니다&quot;);&lt;br&gt; // 예외 처리 로직&lt;br&gt;}</code></td>
</tr>
</tbody></table>
<blockquote>
<p>⚠️ 예외를 무시하면 문제의 원인을 파악하거나 정상적인 복구가 어려움<br />✅ 예외 로그 출력과 함께 처리 로직을 반드시 작성해야 함</p>
</blockquote>
<hr />
<h1 id="6-웹-서버의-계정-관리">6. 웹 서버의 계정 관리</h1>
<h2 id="개요">개요</h2>
<h3 id="웹-서버의-보안-중요성">웹 서버의 보안 중요성</h3>
<ul>
<li>웹 서버의 역할 : 각 기업들의 중요 정보를 접근하기 위한 진입점, 실제 서비스를 제공하는 서비스 주체<h3 id="보안-공격자들의-공격-대상이-되는-보안-취약점">보안 공격자들의 공격 대상이 되는 보안 취약점</h3>
</li>
<li>웹 서버 자체가 가지고 있는 약점</li>
<li>웹 서버가 동적 콘텐트를 만드는 부분</li>
<li>클라이언트 사이트에서 실행되는 스크립트 등<h3 id="대표적인-웹-서버">대표적인 웹 서버</h3>
</li>
<li>아파치(Apache) 웹 서버<ul>
<li>제조사 : 비영리 단체인 아파치 소프트웨어 재단</li>
</ul>
</li>
<li>IIS(Internet Information Services)<ul>
<li>제조사 : 마이크로소프트 사</li>
</ul>
</li>
</ul>
<hr />
<h2 id="61-웹-서비스는-최소-권한-사용자로-운영되어야-한다">6.1 웹 서비스는 최소 권한 사용자로 운영되어야 한다</h2>
<ul>
<li>웹 서버는 아직 알려지지 않은 보안 취약점으로 공격 당할 가능성 존재</li>
<li>웹 서버를 실행시키는 운영체제 상의 사용자는 최소 권한을 가져야 한다<ul>
<li>탈취 당하더라도 권한이 없어 시스템 설정을 변경할 수 없음</li>
<li>Apache : 환경 설정 파일 httpd.conf의 사용자 그룹에 root가 아닌 다른 사용자 계정을 사용
(예: apache 라는 사용자 및 그룹)</li>
<li>IIS : 서비스 관리자에서 IIS 서비스를 시작하는 계정을 새로 추가한 사용자로 재지정
(예: IIS_NOBODY라는 새로 생성한 사용자 계정)</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/24a652f3-0412-4852-b456-881a05c5e563/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d75414c7-21f9-452a-9d8e-098192223eae/image.png" /></p>
<hr />
<h1 id="7-웹-서버의-파일-관리">7. 웹 서버의 파일 관리</h1>
<h2 id="71-디렉터리-검색은-막아야-한다">7.1 디렉터리 검색은 막아야 한다</h2>
<h3 id="디렉터리-검색directory-listing">디렉터리 검색(Directory listing)</h3>
<ul>
<li>웹 브라우저가 웹 서버로 디렉터리의 정보를 요청했을 때 디렉터리 내의 모든 파일 목록을 보여주는 기능</li>
<li>디렉터리에 index.htm과 같은 기본 문서가 없을 경우, 기본 동작으로 보여줌</li>
<li>보안 위험성<ul>
<li>외부의 보안 공격자가 내부 디렉터리의 내용을 확인</li>
<li>서버의 내부 구조 및 백업 파일 혹은 소스 파일들이 공개</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7f5adb7a-e89c-4e8c-aaba-a920f62d3844/image.png" /></p>
<hr />
<h3 id="대응책">대응책</h3>
<ul>
<li>Apache : 환경 설정 파일 httpd.conf에 설정되어 있는 디렉터리 검색 기능 제거<ul>
<li>Options Indexes라는 부분에서 Indexes를 제거</li>
</ul>
</li>
</ul>
<h4 id="🔐-apache-설정에서-indexes-옵션-제거">🔐 Apache 설정에서 <code>Indexes</code> 옵션 제거</h4>
<h4 id="제거-전-설정">제거 전 설정</h4>
<pre><code class="language-apache">&lt;Directory&gt;
    Options Indexes FollowSymLinks AllowOverride None
    Order allow, deny
    Allow from all
&lt;/Directory&gt;</code></pre>
<h4 id="제거-후-설정">제거 후 설정</h4>
<pre><code class="language-apache">&lt;Directory&gt;
    Options FollowSymLinks AllowOverride None
    Order allow, deny
    Allow from all
&lt;/Directory&gt;</code></pre>
<blockquote>
<p>⚠️ <code>Indexes</code> 옵션이 설정되어 있으면 디렉터리 내 파일 목록이 노출될 수 있음<br />✅ <code>Indexes</code> 옵션 제거를 통해 디렉터리 리스팅을 차단해야 함</p>
</blockquote>
<hr />
<ul>
<li>IIS : IIS 관리자 화면에서 ‘디렉터리 검색’ 을 ‘사용 안 함’으로 설정</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5527aa09-3817-4cdf-afeb-6feff5942467/image.png" /></p>
<hr />
<h2 id="72-불필요하게-설치된-파일을-제거하라">7.2 불필요하게 설치된 파일을 제거하라</h2>
<ul>
<li>불필요하게 설치된 파일<ul>
<li>웹 서버를 설치할 때 기본적으로 제공되는 매뉴얼 파일 및 예제 스크립트 파일 등<ul>
<li>매뉴얼 파일과 예제 스크립트 등은 웹 서버의 정보 및 운영체제에 대한 정보 제공</li>
</ul>
</li>
<li>아파치 웹 서버<ul>
<li>설치 디렉터리 바로 밑에 있는 매뉴얼 파일<code>( /htdocs/manual 혹은 /manual ) 등</code></li>
</ul>
</li>
<li>IIS 5.0 혹은 IIS 6.0의 경우<ul>
<li>예제 스크립트 파일들<ul>
<li><code>C:\inetpubs\iissamples</code></li>
<li><code>C:\winnt\help\iishelp</code></li>
<li><code>C:\Program files\common files\system\msadc\sample 등</code></li>
</ul>
</li>
</ul>
</li>
<li>☞ IIS 7.0 이상에서는 위의 예제 파일들이 기본적으로 제공되지 않음</li>
</ul>
</li>
</ul>
<hr />
<h1 id="8-웹-서버의-서비스-관리">8. 웹 서버의 서비스 관리</h1>
<h2 id="81-파일-업로드-및-다운로드의-최대-크기를-설정하라">8.1 파일 업로드 및 다운로드의 최대 크기를 설정하라</h2>
<ul>
<li>파일 최대 크기 설정의 필요성<ul>
<li>부주의한 사용자 혹은 악의적 사용자에 의해 서비스 중지</li>
<li>소수의 대용량 사용자 때문에 다른 사용자들의 피해 발생(시스템이 느려짐)</li>
<li>보안 공격자에 의해 내부의 중요 자료가 대량으로 외부로 유출될 가능성</li>
</ul>
</li>
<li>Apache: <code>httpd.conf</code>의 각 디렉터리 내에 <code>LimitRequestBody</code> 설정(최대 파일 크기 지정)<pre><code>&lt;Directory&gt;
LimitRequestBody 5242880
&lt;/Directory&gt;</code></pre></li>
<li>IIS: (7.0 환경) 설정 파일 applicationhost.config에 있는 속성 값<ul>
<li><code>%windir%\system32\inetsrv\config\applicationhost.config</code><pre><code></code></pre></li>
</ul>
</li>
</ul>
<p>&lt;system.webServer&gt;
 
  
 
&lt;/system.webServer&gt;</p>
<pre><code>
---
## 8.2 IIS의 WebDAV 서비스를 비활성화하라
- WebDAV(Web Distributed Authoring and Versioning) 및 관리 필요성
  - 웹 상에서 여러 명의 사용자가 공동 개발을 지원하기 위해 제안된 국제 표준
  - 철저하게 관리되지 않으면 보안 공격자의 손쉬운 공격 대상
    - 악의적인 요청으로 인증 우회 혹은 버퍼 오버플로우 오류를 통한 관리자 권한 획득 등
- 비활성화 방법(7.0 기준): ISAPI 및 CGI 제한을 선택 → WebDAV 서비스 제거

![](https://velog.velcdn.com/images/kyk02405/post/fea21106-61d3-435c-b0bc-b515b622b490/image.png)

![](https://velog.velcdn.com/images/kyk02405/post/27f12203-0421-4f2e-8879-3c9e4e8cd9ac/image.png)

---
# 9. 웹 서버의 로그 관리
## IIS에서의 로그 관리
- 개요 : IIS 관리 도구에서 설정이 가능
  - 로그 파일의 롤오버 : 로그 파일이 일정 크기에 도달했을 때 새로운 로그 파일을 생성하도록 설정
    - 매 시간, 일, 주 혹은 월 단위 → 보안적 중요성 및 로그 발생 양에 따라 결정
    - (예) 중요하고 서비스 양이 많은 경우, 대용량의 로그가 생성되므로 매시간마다 새로운 로그 파일을 생성하도록 설정
- 로그 정보는 보안 감사 및 보안 공격에 대한 분석의 용도로 활용
- 기본 로그 파일 저장 포맷 : W3C 형식


![](https://velog.velcdn.com/images/kyk02405/post/9b6ea36a-6c69-49e4-a1a9-fc6dd00fc03e/image.png)

---
## W3C 형식의 구성 요소
- 날짜와 시간
- 서버 IP, HTTP 접근 방법(`GET` 또는 `POST` 등), 접근 `URL`, `서버 포트`
- 클라이언트 IP, 클라이언트의 웹 브라우저
- 실행 결과 코드
- 서버에서 클라이언트로 전송한 데이터 크기
- 클라이언트에서 서버로 전송한 데이터의 크기 및 처리 소요 시간
---
## W3C 형식 로그의 예
- `2014-07-25 12:21:31` 날짜와 시간
- `192.168.104.191` 서버 IP
- `GET HTTP 요청(접근) 메소드`(`GET` 또는 `POST` 등)
- `/ 요청 UR`L
- `80 서버 포트`
- `192.168.104.1` 클라이언트 IP

![](https://velog.velcdn.com/images/kyk02405/post/ccbf64b6-c0cf-46a1-b759-07eca67f141f/image.png)

---
## 아파치에서의 로그 관리
- 로그의 형식 설정
  - 아파치환경설정파일`httpd.conf`파일에서지정된`Combined` 로그형식(`Combined Log Format`, `결합된 로그형식`)



#### 📄 Apache 로그 포맷에서 사용되는 예약어 정리

| 항목     | 설명 |
|----------|------|
| `%h`     | 접속한 클라이언트 IP |
| `%l`     | 클라이언트의 사용자 이름 |
| `%u`     | 인증이 요청된 원격 사용자 이름 |
| `%t`     | 요청한 시간과 날짜 (영어권 표준 시간과 날짜 포맷) |
| `&quot;%r&quot;`   | HTTP 접근 방법(GET 또는 POST 등)을 포함한 요청의 첫 라인 |
| `%&gt;s`    | HTTP 상태 코드 |
| `%b`     | HTTP 헤더를 제외하고 전송된 바이트 수 |
| `&quot;%{Referer}i&quot;` | 요청한 URL이 참조되거나 링크된 URL |
| `&quot;%{User-Agent}i&quot;` | 접속한 클라이언트의 OS 및 브라우저 버전 등 |
| `%T`     | 요청을 처리하는 데 걸린 시간(초) |

---</code></pre>