<hr />
<h1 id="restful">RESTful</h1>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Representational_state_transfer">REST (REpresentational State Transfer)</a></li>
<li>REST는 HTTP 기반의 <strong>소프트웨어 아키텍처 스타일</strong></li>
<li>**로이 필딩(Roy Fielding)**이 2000년 UC 어바인에서 박사학위 논문 <em>“Architectural Styles and the Design of Network-based Software Architectures”</em> 에서 REST 정의</li>
<li>REST 설계 지침을 따르는 웹 서비스를 <strong>RESTful</strong>이라고 함</li>
</ul>
<hr />
<h1 id="rest-representational-state-transfer">REST (REpresentational State Transfer)</h1>
<h3 id="개요">개요</h3>
<ul>
<li>웹에서 정보를 주고받는 방법, 즉 <strong>아키텍처 스타일</strong></li>
<li>웹 상에서 컴퓨터들이 데이터를 주고받는 <strong>규칙</strong></li>
</ul>
<h3 id="rest의-주요-개념">REST의 주요 개념</h3>
<ul>
<li><p><strong>리소스 (Resource)</strong></p>
<ul>
<li><p>인터넷에 존재하는 모든 정보 (예: 회원, 게시글 등)</p>
</li>
<li><p>예시:</p>
<ul>
<li><code>/users/1</code> → 1번 회원</li>
<li><code>/posts</code> → 게시글 전체 목록</li>
</ul>
</li>
</ul>
</li>
<li><p><strong>주소 (URI, URL)</strong></p>
<ul>
<li><p>각 리소스는 고유한 주소(URI)를 가짐</p>
</li>
<li><p>예시:</p>
<ul>
<li><code>https://site.com/users/1</code></li>
</ul>
</li>
</ul>
</li>
<li><p><strong>행동 (HTTP 메서드)</strong></p>
<ul>
<li><p>리소스에 어떤 작업을 할지 정의하는 방식</p>
</li>
<li><p>주요 메서드:</p>
<ul>
<li><code>GET</code> – 가져오기</li>
<li><code>POST</code> – 생성</li>
<li><code>PUT</code> – 수정</li>
<li><code>DELETE</code> – 삭제</li>
</ul>
</li>
<li><p>예시:</p>
<ul>
<li><code>GET /users/1</code> → 1번 유저 정보 가져오기</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="restful-api-와-http-전송방식">RESTful API 와 HTTP 전송방식</h1>
<ul>
<li><p>일반적으로 서버에 요청하는 정보의 타입은 <span style="color: blue;"><strong>쓰기(Create), 읽기(Read), 수정(Update), 삭제(Delete)</strong></span>로 구분되고,
네 가지의 첫 글자를 합쳐서 <strong>CRUD</strong>라고 부름</p>
</li>
<li><p>URI 구성 권고에 따르면 RESTful API 구성을 위한 URI에는 <span style="color: red;"><strong>정보의 분류 체계만 포함되어야지</strong></span>, <span style="color: red;"><strong>정보를 어떻게 다룰 것인가 하는 동작에 관한 명세는 포함하지 않을 것을 권고함</strong></span></p>
<ul>
<li>URI에 어떤 계층의 어떤 데이터라는 정보만 기재할 뿐,
그 데이터를 읽을지 쓸지 등에 대한 액션 구분은 URI에 나타내지 않음</li>
</ul>
</li>
<li><p><span style="color: green;"><strong>권고안에서는 HTTP 메소드를 사용하여 이같은 액션을 구분해 줄 것을 권고함</strong></span></p>
</li>
<li><p><span style="color: teal;"><strong>RESTful API 형식으로 데이터를 제공하면</strong></span>,
서버에서 작성해 놓은 URI 명세에 따라
원하는 요청을 식별할 수 있도록 URI를 구성하여 보내면 됨</p>
</li>
</ul>
<hr />
<h1 id="restful-api-에서-http-메소드의-종류">RESTful API 에서 HTTP 메소드의 종류</h1>
<table>
<thead>
<tr>
<th>메서드(전송방식)</th>
<th>목적</th>
</tr>
</thead>
<tbody><tr>
<td>POST</td>
<td>리소스를 create</td>
</tr>
<tr>
<td>GET</td>
<td>리소스 정보 read</td>
</tr>
<tr>
<td>PUT</td>
<td>리소스 update</td>
</tr>
<tr>
<td>DELETE</td>
<td>리소스 delete</td>
</tr>
</tbody></table>
<hr />
<h1 id="rest-vs-soap">REST vs SOAP</h1>
<h3 id="목적">목적</h3>
<p>특정 일자의 상영작 박스오피스 정보를 영화 구분(다양성/상업), 국가(한국/외국), 상영 지역 등의 조건으로 조회</p>
<h3 id="✅-rest-방식">✅ REST 방식</h3>
<ul>
<li><p><strong>요청 URL</strong>
<code>http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml</code>
또는
<code>http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json</code></p>
</li>
<li><p><strong>요청 방식</strong></p>
<ul>
<li><code>GET</code> 방식 사용</li>
<li>요청 파라미터는 <em>3번 항의 인터페이스 정보</em> 참고</li>
</ul>
</li>
<li><p><strong>응답 포맷</strong></p>
<ul>
<li>XML 또는 JSON</li>
<li>**URI 확장자(.xml, .json)**로 포맷 구분</li>
</ul>
</li>
</ul>
<hr />
<h3 id="✅-soap-방식">✅ SOAP 방식</h3>
<ul>
<li><p><strong>요청 URL</strong>
<code>http://www.kobis.or.kr/kobisopenapi/webservice/soap/boxoffice</code></p>
</li>
<li><p><strong>WSDL URL</strong>
<code>http://www.kobis.or.kr/kobisopenapi/webservice/soap/boxoffice?wsdl</code></p>
</li>
<li><p><strong>Operation</strong>
<code>searchDailyBoxOfficeList</code></p>
</li>
</ul>
<hr />
<h1 id="xml-extensible-markup-language">XML (Extensible Markup Language)</h1>
<h3 id="기본-구조">기본 구조</h3>
<ul>
<li><strong>시작 태그</strong>: <code>&lt;element&gt;</code></li>
<li><strong>끝 태그</strong>: <code>&lt;/element&gt;</code></li>
<li><strong>빈 요소 태그</strong>: <code>&lt;element/&gt;</code></li>
</ul>
<h3 id="파싱-parsing">파싱 (Parsing)</h3>
<ul>
<li>XML 데이터에서 정보를 <strong>추출하고 분석</strong>하는 과정</li>
<li>파싱을 처리하는 모듈을 **파서(parser)**라고 함</li>
</ul>
<h3 id="장점">장점</h3>
<ul>
<li><strong>플랫폼 독립적</strong>
(운영체제나 언어에 관계없이 사용 가능)</li>
</ul>
<h3 id="단점">단점</h3>
<ul>
<li><strong>마크업 태그 사용</strong>으로 인해 <strong>데이터 양이 많아짐</strong>
(같은 데이터를 표현할 때 JSON보다 무겁고 복잡함)</li>
</ul>
<hr />
<h1 id="json-javascript-object-notation">JSON (JavaScript Object Notation)</h1>
<ul>
<li>XML의 단점을 극복하기 위해 만들어진 <strong>경량의 데이터 교환 형식</strong></li>
<li>공식 사이트: <a href="http://www.json.org/json-ko.html">http://www.json.org/json-ko.html</a></li>
</ul>
<hr />
<h3 id="특징">특징</h3>
<ul>
<li>사람이 <strong>읽고 쓰기 쉽고</strong>,
기계가 <strong>분석하고 생성하기도 용이함</strong></li>
<li><strong>프로그래밍 언어에 독립적</strong>이기 때문에 다양한 시스템 간 <strong>데이터 교환</strong>에 활용됨</li>
</ul>
<hr />
<h3 id="json의-주요-데이터-구조">JSON의 주요 데이터 구조</h3>
<ol>
<li><p><strong>집합 구조 (<code>{}</code>)</strong></p>
<ul>
<li><p>다양한 속성을 정의할 수 있는 <strong>키-값 쌍의 집합</strong></p>
</li>
<li><p>예시:</p>
<pre><code class="language-json">{
  &quot;name&quot;: &quot;홍길동&quot;,
  &quot;age&quot;: 30
}</code></pre>
</li>
</ul>
</li>
<li><p><strong>리스트 구조 (<code>[]</code>)</strong></p>
<ul>
<li><p><strong>비슷한 형식의 데이터가 반복</strong>될 때 사용</p>
</li>
<li><p>예시:</p>
<pre><code class="language-json">[
  &quot;사과&quot;,
  &quot;바나나&quot;,
  &quot;포도&quot;
]</code></pre>
</li>
</ul>
</li>
</ol>
<table>
<thead>
<tr>
<th>구분</th>
<th>형식</th>
<th>명칭</th>
</tr>
</thead>
<tbody><tr>
<td>여러 속성을 정의하는 순서 없는 집합</td>
<td><code>{ 키: 값, 키: 값, ... }</code></td>
<td>JSON 객체</td>
</tr>
<tr>
<td>비슷한 객체가 반복 나열되는 순서 있는 리스트</td>
<td><code>[ 객체1, 객체2, ... ]</code></td>
<td>JSON 배열</td>
</tr>
</tbody></table>
<hr />
<h1 id="json-javascript-object-notation-1">JSON (JavaScript Object Notation)</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/96058cc1-c2f3-4000-806b-0d4f620fd112/image.png" /></p>
<ul>
<li>XML의 단점을 극복하기 위해 만들어진 <strong>경량의 데이터 교환 형식</strong></li>
<li>공식 사이트: <a href="http://www.json.org/json-ko.html">http://www.json.org/json-ko.html</a></li>
</ul>
<h3 id="특징-1">특징</h3>
<ul>
<li>사람이 읽고 쓰기 쉽고, 기계가 분석하고 생성하기 용이</li>
<li><strong>프로그래밍 언어에 독립적</strong>이므로 데이터 교환에 널리 사용</li>
</ul>
<h3 id="json의-기본-구조">JSON의 기본 구조</h3>
<ul>
<li><p>모든 데이터는 <strong>name/value 쌍</strong>으로 구성됨</p>
</li>
<li><p>사용되는 두 가지 주요 구조:</p>
<ol>
<li><p><strong>집합 구조 (Collection)</strong></p>
<ul>
<li>객체(object), 레코드(record), 구조체(struct), 딕셔너리(dictionary), 해시 테이블(hash table), 키가 있는 리스트 등</li>
</ul>
</li>
<li><p><strong>리스트 구조 (Ordered list)</strong></p>
<ul>
<li>배열(array), 벡터(vector), 리스트(list), 시퀀스(sequence)</li>
</ul>
</li>
</ol>
</li>
</ul>
<h3 id="json-객체-object">JSON 객체 (object)</h3>
<ul>
<li><strong>name/value 쌍들의 순서 없는 집합 (SET)</strong></li>
<li><code>&quot;{&quot;</code>로 시작하고 <code>&quot;}&quot;</code>로 끝남</li>
<li>각 name 뒤에는 <code>&quot;:&quot;</code>을 붙이며, 쌍들은 <code>&quot;, &quot;</code>로 구분</li>
</ul>
<h4 id="예시-1-단순-객체">예시 1: 단순 객체</h4>
<pre><code class="language-json">{
  &quot;이름&quot;: &quot;김컴소&quot;,
  &quot;나이&quot;: 20,
  &quot;성별&quot;: &quot;남&quot;
}</code></pre>
<h4 id="예시-2-중첩된-객체">예시 2: 중첩된 객체</h4>
<pre><code class="language-json">{
  &quot;이름&quot;: &quot;김컴소&quot;,
  &quot;나이&quot;: 20,
  &quot;성별&quot;: &quot;남&quot;,
  &quot;전화&quot;: {
    &quot;휴대&quot;: &quot;010-1111-2222&quot;,
    &quot;집&quot;: &quot;02-1111-2345&quot;
  }
}</code></pre>
<h3 id="json-데이터-구조-요약">JSON 데이터 구조 요약</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>형식</th>
<th>명칭</th>
</tr>
</thead>
<tbody><tr>
<td>여러 속성을 정의하는 순서 없는 집합</td>
<td><code>{ 키: 값, 키: 값, ... }</code></td>
<td>JSON 객체</td>
</tr>
<tr>
<td>비슷한 객체가 반복 나열되는 순서 있는 리스트</td>
<td><code>[ 객체1, 객체2, ... ]</code></td>
<td>JSON 배열</td>
</tr>
</tbody></table>
<hr />
<h1 id="json-javascript-object-notation-2">JSON (JavaScript Object Notation)</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c09993f2-ee3c-45da-8fa5-2192d6927f6f/image.png" /></p>
<ul>
<li>XML의 단점을 극복하기 위해 만들어진 <strong>경량의 데이터 교환 형식</strong></li>
<li>공식 사이트: <a href="http://www.json.org/json-ko.html">http://www.json.org/json-ko.html</a></li>
</ul>
<h3 id="특징-2">특징</h3>
<ul>
<li>사람이 읽고 쓰기 쉽고, 기계가 분석하고 생성하기 용이</li>
<li><strong>프로그래밍 언어에 독립적</strong>이므로 데이터 교환에 널리 사용</li>
</ul>
<hr />
<h3 id="json의-기본-구조-1">JSON의 기본 구조</h3>
<ul>
<li><p>모든 데이터는 <strong>name/value 쌍</strong>으로 구성됨</p>
</li>
<li><p>사용되는 두 가지 주요 구조:</p>
<ol>
<li><p><strong>집합 구조 (Collection)</strong></p>
<ul>
<li>객체(object), 레코드(record), 구조체(struct), 딕셔너리(dictionary), 해시 테이블(hash table), 키가 있는 리스트 등</li>
</ul>
</li>
<li><p><strong>리스트 구조 (Ordered list)</strong></p>
<ul>
<li>배열(array), 벡터(vector), 리스트(list), 시퀀스(sequence)</li>
</ul>
</li>
</ol>
</li>
</ul>
<hr />
<h3 id="json-객체-object-1">JSON 객체 (object)</h3>
<ul>
<li><strong>name/value 쌍들의 순서 없는 집합 (SET)</strong></li>
<li><code>{</code>로 시작하고 <code>}</code>로 끝남</li>
<li>각 name 뒤에는 <code>:</code>을 붙이며, 쌍들은 <code>,</code>로 구분</li>
</ul>
<h4 id="예시-단순-객체">예시: 단순 객체</h4>
<pre><code class="language-json">{
  &quot;이름&quot;: &quot;김컴소&quot;,
  &quot;나이&quot;: 20,
  &quot;성별&quot;: &quot;남&quot;
}</code></pre>
<h4 id="예시-중첩된-객체">예시: 중첩된 객체</h4>
<pre><code class="language-json">{
  &quot;이름&quot;: &quot;김컴소&quot;,
  &quot;나이&quot;: 20,
  &quot;성별&quot;: &quot;남&quot;,
  &quot;전화&quot;: {
    &quot;휴대&quot;: &quot;010-1111-2222&quot;,
    &quot;집&quot;: &quot;02-1111-2345&quot;
  }
}</code></pre>
<hr />
<h3 id="json-배열-array">JSON 배열 (array)</h3>
<ul>
<li><strong>순서가 있는 값의 모음 (collection)</strong></li>
<li><code>[</code>로 시작하고 <code>]</code>로 끝남</li>
<li>요소들은 <code>,</code>로 구분됨</li>
</ul>
<h4 id="예시-배열-포함-객체">예시: 배열 포함 객체</h4>
<pre><code class="language-json">{
  &quot;name&quot;: &quot;김컴소&quot;,
  &quot;age&quot;: 30,
  &quot;cars&quot;: [&quot;아반떼&quot;, &quot;쏘나타&quot;, &quot;그랜저&quot;]
}</code></pre>
<hr />
<h3 id="json-데이터-구조-요약-1">JSON 데이터 구조 요약</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>형식</th>
<th>명칭</th>
</tr>
</thead>
<tbody><tr>
<td>여러 속성을 정의하는 순서 없는 집합</td>
<td><code>{ 키: 값, 키: 값, ... }</code></td>
<td>JSON 객체</td>
</tr>
<tr>
<td>비슷한 객체가 반복 나열되는 순서 있는 리스트</td>
<td><code>[ 객체1, 객체2, ... ]</code></td>
<td>JSON 배열</td>
</tr>
</tbody></table>
<hr />
<h1 id="api-application-programming-interface">API (Application Programming Interface)</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/28a32a6f-2ceb-4296-87a7-f0c05ea85d44/image.png" /></p>
<h3 id="정의">정의</h3>
<ul>
<li><strong>두 개 이상의 컴퓨터 프로그램이 서로 통신하는 방법</strong></li>
<li>다른 소프트웨어에 <strong>기능이나 서비스를 제공하는 소프트웨어 인터페이스</strong></li>
<li>**UI(User Interface)**가 사람과 컴퓨터를 연결한다면,
<strong>API는 컴퓨터와 컴퓨터(또는 소프트웨어 간)를 연결</strong></li>
</ul>
<h3 id="예시">예시</h3>
<ul>
<li><code>printf</code> (C 언어 표준 라이브러리)</li>
<li>Java SE APIs</li>
<li>Windows API</li>
<li>SQLite API</li>
<li>OpenGL API</li>
<li>Open API (공개된 인터넷 API)</li>
</ul>
<hr />
<h1 id="open-api-오픈-api">Open API (오픈 API)</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c65b4434-ff5f-46dd-a492-4e2acc3424b7/image.png" /></p>
<h3 id="정의-1">정의</h3>
<ul>
<li>일부 웹사이트나 기관에서 <strong>SOAP 프로토콜</strong>이나 <strong>RESTful 형식</strong>을 사용하여
<strong>공공 콘텐츠나 기능을 외부에 제공</strong>하는 API</li>
<li>누구나 접근 가능하며, 인증키(API Key) 등을 통해 사용할 수 있음</li>
</ul>
<h3 id="주요-특징">주요 특징</h3>
<ul>
<li><strong>공공 데이터</strong> 및 <strong>민간 서비스</strong>의 자동화된 접근 지원</li>
<li>주로 <strong>정부기관, 공공기관, 민간 플랫폼</strong> 등에서 제공</li>
</ul>
<h3 id="예시-링크">예시 링크</h3>
<ul>
<li>📦 <a href="https://github.com/dl0312/open-apis-korea">한국 공개 API 모음 (GitHub)</a></li>
<li>🌐 <a href="https://rapidapi.com/blog/most-popular-api/">인기 API 리스트 (RapidAPI)</a></li>
<li>🏙️ <a href="https://data.seoul.go.kr/datasetRanking/popular.do">서울 열린데이터 광장 – 인기 데이터셋</a></li>
</ul>
<hr />
<h1 id="공공데이터포털-open-api">공공데이터포털 Open API</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a8ed1cd4-7c43-48bc-836c-ae90b661c041/image.png" /></p>
<ul>
<li>대한민국 정부가 운영하는 <strong>공공데이터 통합 플랫폼</strong></li>
<li>다양한 행정·생활 정보를 <strong>Open API 형식</strong>으로 외부에 제공</li>
<li>공식 웹사이트: <a href="https://www.data.go.kr">https://www.data.go.kr</a></li>
</ul>
<h3 id="주요-제공-데이터-예시">주요 제공 데이터 예시</h3>
<ul>
<li>지역별 운행 시내버스 정보</li>
<li>지역별 축제 및 문화관광지 안내 정보</li>
<li>실시간 약국 운영 정보</li>
<li>도서관 좌석 정보</li>
<li>지역별 공공 와이파이 제공 위치</li>
<li>쇠고기 이력 정보</li>
<li>공공기관 채용 및 행사/이벤트 정보</li>
<li>예금·대출 금리 비교 정보</li>
<li>GPS 기반 날씨 및 미세먼지 정보</li>
<li>아파트 실거래 가격 지수</li>
</ul>
<hr />
<p>아래는 <strong>서울 열린데이터광장</strong>에 대한 내용을 기존 형식에 맞춰 정리한 Markdown입니다:</p>
<hr />
<h1 id="서울-열린데이터광장">서울 열린데이터광장</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f9722e60-bb09-4999-895c-4fa18245c6c7/image.png" /></p>
<ul>
<li>서울시에서 운영하는 <strong>공공 데이터 포털</strong></li>
<li>공식 사이트: <a href="https://data.seoul.go.kr">https://data.seoul.go.kr</a></li>
<li><strong>오픈 API</strong>, <strong>시각화 자료</strong>, <strong>파일 데이터</strong> 등 다양한 형식으로 정보 제공</li>
<li>활용사례 갤러리 제공을 통해 실제 적용 예시도 확인 가능</li>
</ul>
<h3 id="주요-제공-데이터-예시-1">주요 제공 데이터 예시</h3>
<ul>
<li>지하철역별 승하차 인원 및 시간대별 승객 현황</li>
<li>보관 분실물 목록 조회</li>
<li>미분양 주택 현황</li>
<li>개별 공시지가</li>
<li>공영주차장 정보 및 주차 가능 대수 현황</li>
<li>서울 안심먹거리 목록</li>
<li>버스 도착 정보 조회</li>
<li>시장·마트 정보</li>
<li>지역 시장 및 마트별 생필품 가격 정보</li>
<li>일별 기상 관측 정보</li>
</ul>
<hr />
<h1 id="함수-c언어-vs-swift">함수: C언어 vs. Swift</h1>
<h3 id="✅-c언어에서의-함수">✅ C언어에서의 함수</h3>
<pre><code class="language-c">int add(int x, int y) {  // 함수 정의
    return (x + y);
}

add(10, 20);             // 함수 호출</code></pre>
<ul>
<li><strong>자료형 명시</strong>: <code>int</code></li>
<li><strong>함수 호출 시</strong>: 순서대로 인자 전달</li>
<li><strong>매개변수 이름 없음</strong> (호출 시)</li>
</ul>
<hr />
<h3 id="✅-swift에서의-함수">✅ Swift에서의 함수</h3>
<pre><code class="language-swift">func add(x: Int, y: Int) -&gt; Int {
    return x + y
}

add(x: 10, y: 20) // 외부 매개변수명 필요</code></pre>
<ul>
<li><strong>함수 자료형</strong>: <code>(Int, Int) -&gt; Int</code></li>
<li>함수 자체도 값처럼 취급 가능</li>
</ul>
<pre><code class="language-swift">print(type(of: add))  
// 출력: (Int, Int) -&gt; Int</code></pre>
<ul>
<li><strong>외부 매개변수명</strong>을 함께 사용해야 함 (<code>x:</code>, <code>y:</code>)</li>
</ul>
<hr />
<h3 id="주요-차이점-요약">주요 차이점 요약</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th>C 언어</th>
<th>Swift</th>
</tr>
</thead>
<tbody><tr>
<td>정의 형식</td>
<td><code>int add(int, int)</code></td>
<td><code>func add(x: Int, y: Int) -&gt; Int</code></td>
</tr>
<tr>
<td>호출 방식</td>
<td><code>add(10, 20)</code></td>
<td><code>add(x: 10, y: 20)</code></td>
</tr>
<tr>
<td>함수 자료형</td>
<td>명시적으로 표현 어려움</td>
<td><code>(Int, Int) -&gt; Int</code></td>
</tr>
<tr>
<td>매개변수 이름</td>
<td>내부에서만 사용</td>
<td>외부+내부 구분 또는 생략 가능</td>
</tr>
<tr>
<td>1급 객체 여부</td>
<td>제한적 (함수 포인터)</td>
<td>함수는 완전한 1급 객체 (변수 저장 가능)</td>
</tr>
</tbody></table>
<hr />
<h1 id="swift-함수-외부-매개변수-vs-내부-매개변수">Swift 함수: 외부 매개변수 vs 내부 매개변수</h1>
<h3 id="개념-정리">개념 정리</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>외부 매개변수명</strong> (argument label)</td>
<td>함수 <strong>호출 시 사용</strong>하는 이름</td>
</tr>
<tr>
<td><strong>내부 매개변수명</strong> (parameter name)</td>
<td>함수 <strong>정의 내부에서 사용</strong>되는 이름</td>
</tr>
</tbody></table>
<hr />
<h3 id="예시-1-외부-매개변수와-내부-매개변수-분리">예시 1: 외부 매개변수와 내부 매개변수 분리</h3>
<pre><code class="language-swift">func add(first x: Int, second y: Int) -&gt; Int {
    return x + y // 내부 매개변수 x, y 사용
}

// 함수 호출 시 외부 매개변수 사용
add(first: 10, second: 20)</code></pre>
<blockquote>
<p>❌ <code>return(first + second)</code> → 오류 (내부 매개변수는 <code>x</code>, <code>y</code>)</p>
</blockquote>
<blockquote>
<p>❌ <code>add(x:10, y:20)</code> → 오류 (외부 매개변수는 <code>first</code>, <code>second</code>)</p>
</blockquote>
<hr />
<h3 id="예시-2-외부-매개변수-생략-기본형">예시 2: 외부 매개변수 생략 (기본형)</h3>
<pre><code class="language-swift">func add(x: Int, y: Int) -&gt; Int {
    return x + y
}

add(x: 10, y: 20) // 외부/내부 매개변수명이 같음</code></pre>
<ul>
<li>외부 매개변수 생략 시, 내부 매개변수명이 <strong>외부 매개변수명도 겸함</strong></li>
</ul>
<hr />
<h3 id="예시-3-외부-매개변수-생략-지정-_-사용">예시 3: 외부 매개변수 생략 지정 (<code>_</code> 사용)</h3>
<pre><code class="language-swift">func add(_ x: Int, _ y: Int) -&gt; Int {
    return x + y
}

add(10, 20)</code></pre>
<ul>
<li>외부 매개변수명을 완전히 생략</li>
<li>C 언어 스타일 호출 방식처럼 사용할 수 있음</li>
</ul>
<hr />
<h3 id="결론">결론</h3>
<ul>
<li><strong>정의할 때</strong>: 외부/내부 매개변수를 구분해 선언 가능</li>
<li><strong>호출할 때</strong>: 외부 매개변수명을 정확히 사용해야 함 (단, 생략 지정 가능)</li>
</ul>
<hr />
<h1 id="함수명이-궁금해요--function-리터럴">함수명이 궁금해요 : <code>#function</code> 리터럴</h1>
<ul>
<li>공식 문서: <a href="https://docs.swift.org/swift-book/documentation/the-swift-programming-language/expressions/">Swift Documentation – Expressions</a></li>
<li><code>#function</code>은 <strong>현재 실행 중인 함수의 이름</strong>을 문자열로 반환하는 <strong>리터럴(literal)</strong></li>
</ul>
<hr />
<h3 id="사용-예시">사용 예시</h3>
<pre><code class="language-swift">func add(first x: Int, second y: Int) -&gt; Int {
    print(#function)  // 출력: add(first:second:)
    return x + y
}

print(add(first: 10, second: 20))</code></pre>
<blockquote>
<p><code>#function</code>은 호출한 함수의 **전체 함수명(외부 매개변수 포함 서명)**을 출력함</p>
</blockquote>
<hr />
<h3 id="함수-이름의-4가지-형태-add-예시">함수 이름의 4가지 형태 (add 예시)</h3>
<table>
<thead>
<tr>
<th>형태</th>
<th>예시</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>함수 이름만</td>
<td><code>add</code></td>
<td>기본 식별자</td>
</tr>
<tr>
<td>전체 시그니처</td>
<td><code>add(first:second:)</code></td>
<td>외부 매개변수까지 포함된 이름</td>
</tr>
<tr>
<td>외부 이름 생략 버전</td>
<td><code>add(_:_: )</code></td>
<td>외부 이름을 <code>_</code>으로 생략한 경우</td>
</tr>
<tr>
<td>Objective-C 스타일</td>
<td><code>add(_:with:)</code></td>
<td>일부 외부 이름만 남기는 형식</td>
</tr>
</tbody></table>
<hr />
<h3 id="요약">요약</h3>
<ul>
<li><code>#function</code>은 <strong>디버깅, 로깅, 추적</strong> 등에서 유용하게 활용됨</li>
<li>함수 정의의 <strong>정확한 호출 형태를 문자열로 확인</strong> 가능</li>
</ul>
<hr />
<h1 id="1급-객체-first-class-object--first-class-citizen">1급 객체 (First-Class Object / First-Class Citizen)</h1>
<ul>
<li>위키백과: <a href="https://en.wikipedia.org/wiki/First-class_citizen">https://en.wikipedia.org/wiki/First-class_citizen</a></li>
<li>Swift에서는 **함수(Function)**도 1급 객체이다.</li>
</ul>
<hr />
<h3 id="✅-1급-객체의-조건">✅ 1급 객체의 조건</h3>
<p>다음 3가지를 모두 만족하면 <strong>1급 객체</strong>라고 함:</p>
<ol>
<li><strong>변수에 저장할 수 있다</strong></li>
<li><strong>함수의 매개변수로 전달할 수 있다</strong></li>
<li><strong>함수의 반환값으로 사용할 수 있다</strong></li>
</ol>
<hr />
<h3 id="✅-swift-함수는-1급-객체">✅ Swift 함수는 1급 객체</h3>
<h4 id="1-변수에-저장-가능">1) 변수에 저장 가능</h4>
<pre><code class="language-swift">func add(x: Int, y: Int) -&gt; Int {
    return x + y
}

let sum = add
print(sum(3, 4))  // 출력: 7</code></pre>
<h4 id="2-매개변수로-전달-가능">2) 매개변수로 전달 가능</h4>
<pre><code class="language-swift">func operate(_ a: Int, _ b: Int, using op: (Int, Int) -&gt; Int) -&gt; Int {
    return op(a, b)
}

let result = operate(5, 6, using: add)
print(result)  // 출력: 11</code></pre>
<h4 id="3-반환값으로-사용-가능">3) 반환값으로 사용 가능</h4>
<pre><code class="language-swift">func getAddFunction() -&gt; (Int, Int) -&gt; Int {
    return add
}

let f = getAddFunction()
print(f(2, 3))  // 출력: 5</code></pre>
<hr />
<h3 id="요약-1">요약</h3>
<ul>
<li>Swift의 함수는 <strong>완전한 1급 시민</strong>으로서,
다른 값처럼 <strong>변수에 저장</strong>, <strong>전달</strong>, <strong>반환</strong>이 자유롭다.</li>
<li>이러한 특성은 <strong>클로저</strong>, <strong>고차 함수</strong>, <strong>함수형 프로그래밍</strong> 구현의 기반이 된다.</li>
</ul>
<hr />
<h1 id="클로저-표현식-closure-expression">클로저 표현식 (Closure Expression)</h1>
<ul>
<li>위키백과: <a href="https://en.wikipedia.org/wiki/Closure_%28computer_programming%29">https://en.wikipedia.org/wiki/Closure_(computer_programming)</a></li>
<li>클로저(Closure)는 **익명 함수(Anonymous Function)**의 일종으로,
**코드 블록 + 실행 당시의 변수 상태(환경)**를 함께 저장</li>
</ul>
<hr />
<h3 id="✅-언어별-유사-개념">✅ 언어별 유사 개념</h3>
<table>
<thead>
<tr>
<th>언어</th>
<th>개념</th>
</tr>
</thead>
<tbody><tr>
<td>C, C++, Objective-C</td>
<td>block</td>
</tr>
<tr>
<td>Java</td>
<td>lambda function</td>
</tr>
<tr>
<td>C#</td>
<td>delegate</td>
</tr>
<tr>
<td>Swift</td>
<td>closure</td>
</tr>
</tbody></table>
<hr />
<h3 id="✅-함수와-클로저-비교">✅ 함수와 클로저 비교</h3>
<h4 id="일반-함수">일반 함수</h4>
<pre><code class="language-swift">func add(x: Int, y: Int) -&gt; Int {
    return x + y
}
print(add(x: 10, y: 20))  // 출력: 30</code></pre>
<h4 id="클로저-표현식-익명-함수">클로저 표현식 (익명 함수)</h4>
<pre><code class="language-swift">let add1 = { (x: Int, y: Int) -&gt; Int in
    return x + y
}
print(add1(10, 20))       // 출력: 30</code></pre>
<blockquote>
<p>❗ <code>add1(x:10, y:20)</code> → 오류 발생
클로저는 <strong>외부 매개변수명을 사용하지 않음</strong></p>
</blockquote>
<hr />
<h3 id="✅-클로저의-타입-확인">✅ 클로저의 타입 확인</h3>
<pre><code class="language-swift">print(type(of: add1))
// 출력: (Int, Int) -&gt; Int</code></pre>
<hr />
<h3 id="✅-클로저의-정의">✅ 클로저의 정의</h3>
<blockquote>
<p><strong>클로저는 특정 작업(함수)과 그 작업이 일어난 장소(환경)를 함께 저장하는 구조</strong></p>
</blockquote>
<ul>
<li>독립적인 코드 블록이지만 주변 컨텍스트(변수 상태)를 <strong>기억</strong>함</li>
</ul>
<hr />
<h1 id="클로저-표현식-closure-expression-1">클로저 표현식 (Closure Expression)</h1>
<ul>
<li>클로저 표현식은 <strong>매개변수를 받거나 값을 반환하는 형태</strong>로 작성 가능</li>
<li>일반적인 문법 형식:</li>
</ul>
<pre><code class="language-swift">{ (&lt;매개변수 이름&gt;: &lt;매개변수 타입&gt;, ...) -&gt; &lt;반환 타입&gt; in
    // 실행할 코드
}</code></pre>
<hr />
<h3 id="✅-함수와-클로저-비교-예제">✅ 함수와 클로저 비교 예제</h3>
<h4 id="1-일반-함수-사용">1. 일반 함수 사용</h4>
<pre><code class="language-swift">func mul(val1: Int, val2: Int) -&gt; Int {
    return val1 * val2
}

let result = mul(val1: 10, val2: 20)
print(result) // 출력: 200</code></pre>
<h4 id="2-클로저-표현식으로-동일한-동작-구현">2. 클로저 표현식으로 동일한 동작 구현</h4>
<pre><code class="language-swift">let multiply = { (val1: Int, val2: Int) -&gt; Int in
    return val1 * val2
}

let result = multiply(10, 20) // 상수를 함수처럼 호출
print(result) // 출력: 200</code></pre>
<blockquote>
<p><code>multiply</code>의 타입은 <code>(Int, Int) -&gt; Int</code>
함수처럼 <code>multiply(10, 20)</code> 형태로 호출 가능</p>
</blockquote>
<hr />
<h3 id="✅-요약">✅ 요약</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td>정의 형식</td>
<td><code>{ (매개변수) -&gt; 반환형 in 실행 코드 }</code></td>
</tr>
<tr>
<td>변수 저장</td>
<td><code>let multiply = { ... }</code></td>
</tr>
<tr>
<td>호출 방식</td>
<td><code>multiply(10, 20)</code></td>
</tr>
<tr>
<td>자료형</td>
<td><code>(Int, Int) -&gt; Int</code></td>
</tr>
</tbody></table>
<hr />
<h1 id="후행-클로저-trailing-closure">후행 클로저 (Trailing Closure)</h1>
<ul>
<li>공식 문서: <a href="https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures/">Swift Closures</a></li>
<li>클로저가 **함수의 마지막 인자(argument)**일 경우,
매개변수 이름 없이 <strong>함수 소괄호 외부에 클로저 블록</strong>을 작성할 수 있음</li>
</ul>
<hr />
<h3 id="✅-기본-형식">✅ 기본 형식</h3>
<pre><code class="language-swift">func someFun(cl: () -&gt; Void) {
    cl()
}</code></pre>
<h4 id="일반-클로저-전달-방식">일반 클로저 전달 방식</h4>
<pre><code class="language-swift">someFun(cl: {
    print(&quot;일반 방식 클로저 호출&quot;)
})</code></pre>
<h4 id="후행-클로저-방식">후행 클로저 방식</h4>
<pre><code class="language-swift">someFun() {
    print(&quot;후행 클로저 호출&quot;)
}</code></pre>
<blockquote>
<p>⚠️ 괄호 생략은 함수에 <strong>클로저 하나만 인자일 때</strong> 가능
예: <code>someFun { ... }</code></p>
</blockquote>
<hr />
<h3 id="✅-후행-클로저는-이런-곳에-자주-쓰여요">✅ 후행 클로저는 이런 곳에 자주 쓰여요</h3>
<pre><code class="language-swift">let numbers = [1, 2, 3]

let doubled = numbers.map { number in
    return number * 2
}
print(doubled) // [2, 4, 6]</code></pre>
<hr />
<h3 id="✅-요약-1">✅ 요약</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>언제 사용?</td>
<td>클로저가 <strong>함수의 마지막 인자</strong>일 때</td>
</tr>
<tr>
<td>어떻게 쓰나?</td>
<td>함수 소괄호 외부 <code>{ ... }</code>에 클로저 작성</td>
</tr>
<tr>
<td>장점</td>
<td>코드 간결성, 함수형 스타일 강조</td>
</tr>
</tbody></table>
<hr />
<h1 id="후행-클로저-trailing-closure-예제">후행 클로저 (Trailing Closure) 예제</h1>
<pre><code class="language-swift">// 일반 함수 정의
func mul(a: Int, b: Int) -&gt; Int {
    return a * b
}

// 클로저를 변수에 저장
let multiply = { (a: Int, b: Int) -&gt; Int in
    return a * b
}

print(mul(a: 10, b: 20))        // 200
print(multiply(10, 20))         // 200

// 다른 클로저 예시
let add = { (a: Int, b: Int) -&gt; Int in
    return a + b
}
print(add(10, 20))              // 30

// 함수에 클로저 전달
func math(x: Int, y: Int, cal: (Int, Int) -&gt; Int) -&gt; Int {
    return cal(x, y)
}

// 1. 변수로 정의된 클로저 전달
var result = math(x: 10, y: 20, cal: add)
print(result)                   // 30

result = math(x: 10, y: 20, cal: multiply)
print(result)                   // 200

// 2. 클로저를 매개변수에 직접 작성
result = math(x: 10, y: 20, cal: { (a: Int, b: Int) -&gt; Int in
    return a + b
})
print(result)                   // 30

// 3. **후행 클로저(Trailing Closure)** 사용
result = math(x: 10, y: 20) { (a: Int, b: Int) -&gt; Int in
    return a + b
}
print(result)                   // 30</code></pre>
<hr />
<h3 id="✅-후행-클로저란">✅ 후행 클로저란?</h3>
<ul>
<li>클로저가 <strong>함수의 마지막 인자</strong>일 경우,</li>
<li>함수 괄호 <strong>외부에 클로저 블록</strong>을 두어 더 읽기 쉽게 표현 가능</li>
</ul>
<pre><code class="language-swift">// 일반 방식
math(x: 10, y: 20, cal: { ... })

// 후행 클로저 방식
math(x: 10, y: 20) { ... }</code></pre>
<hr />
<h3 id="✅-요약-2">✅ 요약</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td>사용 조건</td>
<td>클로저가 <strong>마지막 매개변수</strong>일 때</td>
</tr>
<tr>
<td>문법 형태</td>
<td>함수 소괄호 <strong>밖</strong>에 <code>{ ... }</code> 작성</td>
</tr>
<tr>
<td>장점</td>
<td>코드 가독성이 높아지고 간결해짐</td>
</tr>
</tbody></table>
<hr />
<h1 id="후행-클로저-trailing-closure-1">후행 클로저 (Trailing Closure)</h1>
<p><img alt="업로드중.." src="blob:https://velog.io/8d554e92-5af8-4306-a95d-8acf8d9f1324" /></p>
<ul>
<li>공식 문서:
<a href="https://docs.swift.org/swift-book/LanguageGuide/Closures.html">Swift 언어 가이드 – Closures</a>
<a href="https://developer.apple.com/documentation/uikit/uialertaction/1620097-init">UIAlertAction 생성자 문서</a></li>
</ul>
<hr />
<h3 id="✅-개념">✅ 개념</h3>
<ul>
<li>**클로저가 함수의 마지막 매개변수(argument)**일 경우,
해당 매개변수 이름(예: <code>handler:</code>)을 생략하고
<strong>함수 소괄호 외부에 클로저를 작성</strong>할 수 있음</li>
</ul>
<hr />
<h3 id="✅-uikit-예시-uialertaction">✅ UIKit 예시: <code>UIAlertAction</code></h3>
<h4 id="1-후행-클로저-사용">1. 후행 클로저 사용</h4>
<pre><code class="language-swift">let onAction = UIAlertAction(title: &quot;On&quot;, style: .default) { action in
    self.lampImg.image = self.imgOn
    self.isLampOn = true
}</code></pre>
<h4 id="2-일반-클로저-방식">2. 일반 클로저 방식</h4>
<pre><code class="language-swift">let removeAction = UIAlertAction(title: &quot;제거&quot;, style: .destructive, handler: { action in
    self.lampImg.image = self.imgRemove
    self.isLampOn = false
})</code></pre>
<hr />
<h3 id="✅-요약-3">✅ 요약</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>언제 사용?</td>
<td>클로저가 <strong>함수의 마지막 인자</strong>일 때</td>
</tr>
<tr>
<td>문법</td>
<td><code>handler: { ... }</code> → <code>{ ... }</code> (매개변수명 생략)</td>
</tr>
<tr>
<td>장점</td>
<td><strong>가독성 향상</strong>, 특히 클로저가 길어질 때 코드 구조가 명확해짐</td>
</tr>
</tbody></table>
<hr />
<h1 id="클로저의-축약-표현-closure-shorthand-syntax">클로저의 축약 표현 (Closure Shorthand Syntax)</h1>
<h3 id="기본-함수-정의">기본 함수 정의</h3>
<pre><code class="language-swift">func math(x: Int, y: Int, cal: (Int, Int) -&gt; Int) -&gt; Int {
    return cal(x, y)
}</code></pre>
<hr />
<h3 id="✅-1-전체-형태-타입-in-return-모두-포함">✅ 1. 전체 형태 (타입, <code>in</code>, <code>return</code> 모두 포함)</h3>
<pre><code class="language-swift">let result = math(x: 10, y: 20, cal: { (val1: Int, val2: Int) in
    return val1 + val2
})
print(result) // 30</code></pre>
<hr />
<h3 id="✅-2-후행-클로저--리턴형-생략">✅ 2. 후행 클로저 + 리턴형 생략</h3>
<pre><code class="language-swift">let result = math(x: 10, y: 20) { (val1: Int, val2: Int) in
    return val1 + val2
}
print(result) // 30</code></pre>
<hr />
<h3 id="✅-3-단축-인자명-사용-0-1">✅ 3. 단축 인자명 사용 (<code>$0</code>, <code>$1</code>)</h3>
<pre><code class="language-swift">let result = math(x: 10, y: 20, cal: {
    return $0 + $1
})
print(result) // 30</code></pre>
<hr />
<h3 id="✅-4-후행-클로저--단축-인자-사용">✅ 4. 후행 클로저 + 단축 인자 사용</h3>
<pre><code class="language-swift">let result = math(x: 10, y: 20) {
    return $0 + $1
}
print(result) // 30</code></pre>
<hr />
<h3 id="✅-5-return-생략-한-줄-클로저">✅ 5. <code>return</code> 생략 (한 줄 클로저)</h3>
<pre><code class="language-swift">let result = math(x: 10, y: 20, cal: {
    $0 + $1
})
print(result) // 30</code></pre>
<hr />
<h3 id="✅-6-후행-클로저--return-생략">✅ 6. 후행 클로저 + <code>return</code> 생략</h3>
<pre><code class="language-swift">let result = math(x: 10, y: 20) {
    $0 + $1
}
print(result) // 30</code></pre>
<hr />
<h3 id="📌-요약-축약-순서">📌 요약: 축약 순서</h3>
<ol>
<li>매개변수 타입 생략</li>
<li><code>in</code> 사용 생략</li>
<li><code>return</code> 생략</li>
<li><code>$0</code>, <code>$1</code> 사용</li>
</ol>
<hr />
<h1 id="디폴트-매개변수-default-parameter">디폴트 매개변수 (Default Parameter)</h1>
<h3 id="✅-개념-1">✅ 개념</h3>
<ul>
<li>함수 호출 시 **특정 인자(argument)**를 전달하지 않으면,</li>
<li>함수 선언 시 설정한 **기본값(default value)**이 사용됨</li>
</ul>
<hr />
<h3 id="✅-함수-정의-예">✅ 함수 정의 예</h3>
<pre><code class="language-swift">func sayHello(count: Int, name: String = &quot;길동&quot;) -&gt; String {
    return &quot;\(name) 번호는 \(count)&quot;
}</code></pre>
<ul>
<li><code>name</code> 인자를 생략하면 <code>&quot;길동&quot;</code>이 기본값으로 사용됨</li>
</ul>
<hr />
<h3 id="✅-함수-호출-예">✅ 함수 호출 예</h3>
<pre><code class="language-swift">var message = sayHello(count: 10, name: &quot;철수&quot;)
print(message)
// 출력: 철수 번호는 10

message = sayHello(count: 100) // name 생략
print(message)
// 출력: 길동 번호는 100</code></pre>
<hr />
<h3 id="✅-요약-4">✅ 요약</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>기본값 지정 위치</td>
<td>함수 선언부의 매개변수 옆</td>
</tr>
<tr>
<td>생략 가능한 인자</td>
<td>디폴트 값을 가진 매개변수</td>
</tr>
<tr>
<td>호출 시 인자 생략</td>
<td>생략된 인자에는 기본값이 자동 적용됨</td>
</tr>
</tbody></table>
<hr />
<h1 id="present_animatedcompletion"><code>present(_:animated:completion:)</code></h1>
<ul>
<li>공식 문서: <a href="https://developer.apple.com/documentation/uikit/uiviewcontroller/1621380-present">UIViewController.present(_:animated:completion:)</a></li>
</ul>
<pre><code class="language-swift">func present(
    _ viewControllerToPresent: UIViewController,
    animated flag: Bool,
    completion: (() -&gt; Void)? = nil
)</code></pre>
<hr />
<h3 id="✅-기능">✅ 기능</h3>
<ul>
<li><strong>모달 방식</strong>으로 새로운 뷰 컨트롤러를 현재 뷰 컨트롤러 <strong>위에 표시</strong></li>
<li>모달 방식이란? → <strong>새로운 뷰를 닫기 전에는 아래 뷰를 볼 수 없음</strong></li>
</ul>
<hr />
<h3 id="✅-매개변수-설명">✅ 매개변수 설명</h3>
<ol>
<li><p><strong><code>viewControllerToPresent</code></strong></p>
<ul>
<li>새로 띄울 뷰 컨트롤러 객체</li>
<li>예: <code>UIAlertController</code>, <code>UIViewController()</code> 등</li>
</ul>
</li>
<li><p><strong><code>animated</code></strong></p>
<ul>
<li><code>true</code>: 애니메이션과 함께 표시</li>
<li><code>false</code>: 즉시 표시</li>
</ul>
</li>
<li><p><strong><code>completion</code></strong></p>
<ul>
<li><strong>뷰가 나타난 이후 실행할 클로저</strong></li>
<li>매개변수와 반환값이 없는 클로저</li>
<li>특별히 처리할 일이 없다면 <code>nil</code> 또는 생략 가능 (기본값이 <code>nil</code>)</li>
</ul>
</li>
</ol>
<hr />
<h3 id="✅-예제">✅ 예제</h3>
<pre><code class="language-swift">present(alert, animated: true, completion: nil)
// 또는
present(alert, animated: true)</code></pre>
<ul>
<li><code>alert</code> 창을 애니메이션 효과와 함께 화면에 띄우고,</li>
<li>표시 후 별도 동작은 없음</li>
</ul>
<hr />
<h3 id="✅-요약-5">✅ 요약</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>목적</td>
<td>모달 방식으로 뷰 컨트롤러 표시</td>
</tr>
<tr>
<td>completion</td>
<td>뷰가 <strong>보여진 후에 실행할 작업</strong>을 정의</td>
</tr>
<tr>
<td>기본값</td>
<td><code>completion</code>은 디폴트 인자이므로 생략 가능</td>
</tr>
<tr>
<td>예시 호출</td>
<td><code>present(alert, animated: true)</code></td>
</tr>
</tbody></table>
<hr />