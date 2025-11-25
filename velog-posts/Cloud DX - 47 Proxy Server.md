# Cloud DX - 47 Proxy Server

- 📅 Published: Mon, 24 Nov 2025 08:48:13 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-47-Proxy-Server)

<hr />
<h1 id="span-style--colorskyblue10-proxy-serverspan"><span style="color: skyblue;">10. Proxy Server</span></h1>
<h3 id="웹을-통해-나타나는-일반적인-유형">웹을 통해 나타나는 일반적인 유형</h3>
<ul>
<li><code>Request</code> 와 <code>Response</code>를 판단할 수 있는 요령이니까 꼭 암기하도록 한다.</li>
<li><code>HTTP Request</code><ul>
<li><code>GET/HTTP/1.1</code></li>
</ul>
</li>
<li><code>HTTP Reponse</code><ul>
<li><code>HTTP/1.1 200 OK</code></li>
</ul>
</li>
</ul>
<h2 id="102-web-proxy">10.2 Web Proxy</h2>
<h3 id="개요">개요</h3>
<ul>
<li><code>Client</code>가 <code>Server</code>로 접속할 때 <code>Proxy Server</code>를 통하게 되면 <code>Server</code>에서는 <code>Client</code>의 <code>IP</code>는 모르고 <code>Proxy Server의 IP</code>만 알기 때문에 변조가 가능하다.</li>
<li><code>IP</code>를 변조하고자 할 때 많이 사용한다.</li>
<li>일반적으로 '방화벽'이라고 많이 부르기도 한다.</li>
<li>PC와 인터넷 사이의 통신을 할 때 중개인 역할을 한다.</li>
</ul>
<h3 id="📌-proxy-server">📌 Proxy Server</h3>
<ul>
<li>다른 네트워크 서비스에 <strong>간접적으로 접속</strong>할 수 있게 해주는 서버.</li>
<li>원래 목적: <strong>캐시(Cache)</strong>를 사용해 <strong>리소스(Resource) 접근 속도 향상</strong>.</li>
<li>현재는 <strong>보안, 통제</strong>, 그리고 웹 요청/응답을 <strong>감시 및 수정</strong>하는 용도로도 활용.</li>
</ul>
<h3 id="🌐-web-proxy">🌐 Web Proxy</h3>
<ul>
<li><p>웹 요청을 <strong>임시 저장소(Cache)</strong>를 통해 전달하는 <strong>중개자 역할</strong>.</p>
</li>
<li><p><strong>브라우저(Client)</strong>와 <strong>서버(Server)</strong> 간 통신 시, 중간에 위치하여 데이터를 <strong>재전송</strong>.</p>
</li>
<li><p>프록시 사용 시, <strong>Client–Server 간의 패킷 내용을 중간에서 확인</strong> 가능.</p>
</li>
<li><p>(핵심) <code>Web Proxy</code>는 프로그램을 의미하는데 이 프로그램이 설치된 컴퓨터를 <code>Proxy Server</code>라고 한다.</p>
</li>
</ul>
<hr />
<h2 id="102-web-proxy-1-odysseus">10.2 Web Proxy 1. Odysseus</h2>
<h3 id="실습-1-로컬-without-db-server">실습 1. 로컬 without DB Server</h3>
<ul>
<li><p>작업 </p>
<ul>
<li><p>악성코드를 심어서 보낸 후 실행해 놓고 로그 파일을 편취한다.</p>
</li>
<li><p>해킹 도구에 대한 강의 후 진행</p>
<blockquote>
<ul>
<li>작업환경 구성(NAT)</li>
</ul>
</blockquote>
</li>
<li><p>테스트용 시스템</p>
<ul>
<li><code>CentOS</code> / <code>Rocky</code></li>
<li><code>Server</code> 설치<code>(DNS, Web Server, FTP Server, DB Server)</code></li>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li><p><code>Web Proxy</code></p>
<ul>
<li><code>Windows 10</code>에 설치한다.</li>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
</ul>
</li>
<li><p><code>Odysseus</code> 다운로드</p>
</li>
<li><p><code>Proxy</code> 실행 시 특히 신경 쓸 내용</p>
<ul>
<li><code>Proxy Tools</code>을 실행하면 웹 브라우저의 프록시에 설정 내용 그대로 반영이 된다. 즉, 변경된다.</li>
<li>따라서 시스템 트레이에서 종료가 되더라도 변경된 Proxy가 적용된 상태가 된다.</li>
<li>따라서 웹브라우저를 실행하고 사이트를 입력해도 정상적으로 출력되던 사이트도 뜨질 않는다.</li>
<li>이럴 때는 시스템을 재부팅하지 말고 <code>Odysseus</code>에서 우클릭 후 <code>IE Proxy Settings</code>을 <code>None</code>으로 변경하면 된다.</li>
</ul>
</li>
<li><p>작업 1. 기본 웹 문서 출력</p>
<ul>
<li><p>네임서버 조회</p>
</li>
<li><p>기본 웹 문서 파일 생성</p>
<ul>
<li><code>chmod 701 /export/home/samadal/</code></li>
<li><code>vi /etc/httpd/conf/httpd.conf</code></li>
<li><code>vi index.html</code></li>
</ul>
</li>
<li><p>사이트 출력 1. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ff8903b8-6b44-4d1b-b71c-ea2ba45967ce/image.png" /></p>
</li>
<li><p><code>Odysseus</code> 실행 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1059e784-cb2a-4859-b9ee-7c14703cc669/image.png" /></p>
</li>
<li><p><code>Odysseus</code> 옵션 체크 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0b8b39dd-593c-4794-bb49-24cfc3a58da3/image.png" /></p>
</li>
<li><p>사이트 출력 2. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ef3a809f-06e3-467b-acff-1bec41122953/image.png" /></p>
</li>
<li><p>로그 확인</p>
<ul>
<li>2가지 방법<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7a0696b6-59ce-4c97-9299-7067b74f8f9b/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d8e4f8a3-4575-4b83-8182-64771c35f3ad/image.png" /></li>
</ul>
</li>
</ul>
<blockquote>
<ul>
<li><code>HTTP Request</code></li>
</ul>
</blockquote>
<ul>
<li><code>GET/HTTP/1.1</code><ul>
<li><code>HTTP Reponse</code></li>
</ul>
</li>
<li><code>HTTP/1.1 200 OK</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li><p>작업 2. <code>login.html</code>을 기본 경로에 <code>index.html</code>로 변경</p>
<ul>
<li><p>소스 파일 업로드 </p>
</li>
<li><p>로그 분석 하기 전에 가장 먼저 할 일</p>
<ul>
<li>사이트에 히스토리 정보 모두 삭제</li>
<li><code>Odysseus</code>의 체크 항목 모두 해제 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/85f42d87-cfc2-4a90-8909-eb19d982f67c/image.png" /></li>
<li>작업 관리자에서 <code>Odysseus</code> 종료 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8ac85d7c-7e5d-4479-8edf-961d11f0bb16/image.png" /></li>
<li>윈도우 탐색기에서 로그 파일 삭제 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/240764bf-1f63-4017-b098-f3c65d406f59/image.png" /></li>
</ul>
</li>
<li><p>로그 분석 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1217ae09-ceb5-4303-88c1-77ae36e61239/image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="실습-2-로컬-with-db-server">실습 2. 로컬 with DB Server</h3>
<blockquote>
<ul>
<li>작업환경 구성(NAT)</li>
</ul>
</blockquote>
<ul>
<li>테스트용 시스템<ul>
<li><code>CentOS</code> / <code>Rocky</code></li>
<li><code>Server</code> 설치<code>(DNS, Web Server, FTP Server, DB Server)</code></li>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
</ul>
<ul>
<li><p>선수 작업</p>
<ul>
<li><code>Odysseus</code> 관련 모드 서비스를 종료</li>
<li><code>DB Server</code> 구축</li>
<li><code>Apache Web Server</code> 구축</li>
<li><code>FTP Server</code> 구축</li>
<li>방화벽에서 포트 추가 및 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/57efaa80-a386-4e18-b2fc-5a1a5171786c/image.png" /></li>
<li><u><a href="https://velog.io/@kyk02405/Cloud-DX-16-phpmyadmin-Zeroboard"><strong><code>php 7.4 설치 링크</code></strong></a></u> </li>
<li>테스트 페이지 출력 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f2322dca-1dab-492b-8437-e1953c1948e8/image.png" /></li>
</ul>
</li>
<li><p><code>zeroboard</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2b8c04eb-7e19-48b4-9ed7-e8925f00d1d4/image.png" /></p>
</li>
<li><p><code>Odysseus</code></p>
<ul>
<li>제로보드 로그인 방식 변경 <ul>
<li><code>설정</code> -&gt; <code>동의</code> -&gt; <code>회원</code> -&gt; <code>회원가입</code> -&gt; <code>설정 변경</code> -&gt; <code>검색 기록</code>, <code>로그 파일</code> 삭제 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a2c53ee4-1fc6-4722-99fe-231c3a7a1665/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p><strong><code>302의 의미</code></strong></p>
<ul>
<li><p><strong>302 리다이렉트</strong>라고 하며, 요청한 <em>리소스가 임시적으로 새로운 URL로 이동했음(Temporarily Moved)</em>을 나타낸다.</p>
</li>
<li><p>따라서 <strong>브라우저 주소창의 URL은 변경되지 않고</strong>, <em>기존 URL</em>을 그대로 유지한다.</p>
</li>
<li><p>이는 <strong>기존 URL을 유지하면서</strong>, 실제 콘텐츠는 <em>새로운 URL</em>에서 조회되고 있음을 의미한다.</p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/718203c9-985c-4f8b-af7d-d660977792e6/image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="103-web-proxy-paros">10.3 Web Proxy: Paros</h2>
<h3 id="개요-1">개요</h3>
<ul>
<li><span style="color: red;">(핵심)</span> <strong>Paros</strong>는 <em>웹 사이트의 취약점 분석</em>뿐만 아니라 <em>웹 해킹 도구</em>로도 활용된다.  </li>
<li><em>Web Server*와 *Client</em> 사이에 위치하여 통신을 가로챈다.</li>
<li><em>HTTP</em>, <em>HTTPS</em> 데이터는 물론 <em>Cookies</em>, <em>Form 필드</em> 등을 중간에서 <strong>모니터링</strong>하거나 <strong>변조</strong>하여 서버로 전송할 수 있다.</li>
<li>Paros로 유입된 패킷은 <strong>일시 정지</strong> 후 <strong>변조</strong>되어 나가며, 이 과정에서 잠시 멈출 수 있다.</li>
<li><span style="color: red;">(특징)</span> <strong>GUI 환경(GUI Mode)</strong> 전용 도구로, <strong>CLI 환경(CLI Mode)</strong>에서는 실행되지 않는다.  </li>
<li><span style="color: red;">(중요)</span> <strong>32bit 전용 도구</strong>로, 사용을 위해 <strong>32bit 설치 파일</strong>이 필요하다.</li>
</ul>
<hr />
<blockquote>
<h3 id="작업환경-구성nat">작업환경 구성(NAT)</h3>
</blockquote>
<ul>
<li>테스트용 시스템<ul>
<li><code>CentOS</code> / <code>Rocky</code></li>
<li><code>Server</code> 설치<code>(DNS, Web Server, FTP Server, DB Server)</code></li>
<li><code>192.168.10.128</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li>웹 프록시용 시스템<ul>
<li><code>Windows 10</code>에 <code>Web Proxy</code>를 설치한다.</li>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.128</code></li>
</ul>
</li>
<li>필요한 프로그램<ul>
<li><code>Paros</code>, <code>Wireshark</code>, <code>JRE</code></li>
</ul>
</li>
</ul>
<hr />
<h3 id="일반">일반</h3>
<ul>
<li>필수사항<ul>
<li><code>Windows</code>에서 사용되는 <code>Paros</code>는 <code>32bit</code> 전용이기 때문에 반드시 모든 소프트웨어를 <code>32bit</code>로 설치해야 한다.</li>
</ul>
</li>
<li>설정 전에 확인할 내용</li>
</ul>
<h3 id="java-관련">Java 관련</h3>
<ul>
<li><p><code>Java</code> 설치</p>
<ul>
<li><code>JDK</code> 다운로드 및 설치<ul>
<li>다운로드</li>
<li>설치</li>
<li>확인</li>
</ul>
</li>
<li>시스템 환경 변수 설정 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/490c03a6-8ee3-40aa-9ece-d74dd03a7df7/image.png" /></li>
</ul>
</li>
<li><p><code>Apache ANT</code> 설치</p>
<ul>
<li>개요<ul>
<li>'Apache ANT'는 '자바 프로그래밍 언어'에서 사용하는 '자동화 된 소프트웨어 빌드(소스파일을 사용할 수 있도록 해주는 과정) 도구'를 말한다.</li>
<li>자바 프로젝트들을 '빌드(코드 분석, 동작할 수 있는 파일로 만들어 주는 과정)'하는데 표준으로 사용된다.</li>
<li>'Unix, Linux'의 'make'와 비슷하나 자바언어로 구현되어 있어 자바 실행환경이 필요하다.</li>
<li>'make'와 다른 점은 빌드를 위한 환경구성을 'XML 파일을 사용'한다는 것이다.</li>
<li>기본적인 빌드 파일명은, 'build.xml'이다.</li>
</ul>
</li>
<li>프로그램 다운로드 및 설치<ul>
<li><code>apache-ant-1.10.15-bin.zip</code></li>
</ul>
</li>
<li>시스템 환경 변수 설정 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cef9d4d6-081d-47c0-8c1c-0384fae187ca/image.png" /></li>
</ul>
</li>
</ul>
<h3 id="paros-설치">Paros 설치</h3>
<ul>
<li>다운로드 <code>Paros 3.2.13</code></li>
<li>설치</li>
<li>실행 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0cc14216-baab-4cef-b303-13b35ca031e4/image.png" /></li>
</ul>
<h3 id="실습">실습</h3>
<ul>
<li><p><code>테스트 1. without DB</code></p>
<ul>
<li><code>Windows 10</code>에서의 <code>Proxy</code> 설정<ul>
<li>수정 전 <code>(http=127.0.0.1:50000;https=127.0.0.1:50000 / x )</code></li>
<li>수정 후 <code>(127.0.0.1 / 8080 )</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1ebe4739-4ded-43c1-88f4-11133f8b9a1e/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p><code>테스트 2.</code></p>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/042c6881-479a-4373-987b-91cae2fe1b23/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/70a2d7b8-33c3-45d3-91e9-ef72ce4ae2b5/image.png" /></p>
</li>
</ul>
</li>
</ul>