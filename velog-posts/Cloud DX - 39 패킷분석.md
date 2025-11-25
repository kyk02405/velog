# Cloud DX - 39 패킷분석

- 📅 Published: Wed, 19 Nov 2025 04:11:09 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-39-%ED%8C%A8%ED%82%B7%EB%B6%84%EC%84%9D-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%ED%95%B4%ED%82%B9-%EC%A0%88%EC%B0%A8-%EB%B0%8F-%ED%98%B8%EC%8A%A4%ED%8A%B8-%EC%8B%9D%EB%B3%84-Port-Scanning)

<hr />
<h1 id="span-style--colorskyblue02-패킷-분석-with-wiresharkspan"><span style="color: skyblue;">02. 패킷 분석 (with WireShark)</span></h1>
<h2 id="wireshark를-이용한-패킷-분석">WireShark를 이용한 패킷 분석</h2>
<h2 id="실습-1-데이터-링크2계층-패킷-분석">실습 1. 데이터 링크(2계층) 패킷 분석</h2>
<h3 id="실습-환경">실습 환경</h3>
<ul>
<li><p>Windows 10</p>
<ul>
<li><code>192.168.10.131</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
<li><p>Windows Server 2002 with IIS 웹서버</p>
<ul>
<li><code>192.168.10.132</code> / <code>C Class</code> / <code>192.168.10.2</code> / <code>192.168.10.2</code></li>
</ul>
</li>
<li><p><code>IIS</code> 다운 후에 <code>Host-only</code>로 변경</p>
<h3 id="통신-테스트">통신 테스트</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b7039d87-3553-41f8-b26d-dfa6c5dec279/image.png" /></p>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a783942d-1886-42eb-b629-239c4abce07f/image.png" /></p>
<h3 id="패킷-캡쳐-준비">패킷 캡쳐 준비</h3>
<ul>
<li><code>Windows Server 2022</code>에서 <code>IIS 웹서버</code> 추가 후 활성화</li>
<li>각 시스템에서 웹 브라우저를 통한 사이트 출력(IIS Test Page)
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ca088a48-56f7-4601-986f-1f041241a923/image.png" /></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e562c2ed-1a64-4ed0-9775-8a2b617ce1a2/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b97647b2-8727-4f92-b360-844da9d4ad8f/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d1536b82-e76e-46db-95de-70c5969e1b8f/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ad3fae71-1209-4b73-80a8-4e7e13edf6da/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0ed6f45a-a97e-4216-a4a4-9bf5139c162e/image.png" /></p>
<ul>
<li><p><code>Wireshark</code> 설치 및 실행</p>
</li>
<li><p>패킷 캡처</p>
<ul>
<li><p>각 시스템 별 <code>MAC Address</code> 확인</p>
<ul>
<li><code>Server</code> <code>00-0C-29-48-1A-CC</code></li>
<li><code>Client</code> <code>00-0C-29-B9-16-EA</code></li>
</ul>
</li>
<li><p>각 시스템에서 샥스핀을 실행</p>
<ul>
<li><code>Ethernet</code> 접속 후 중지</li>
<li>이 창 띄우고 대기<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d4c7384a-0e69-4e72-833e-b8e08005a933/image.png" /></li>
</ul>
</li>
<li><p><code>Client</code>에서 웹브라우저를 통해서 <code>Server</code>의 주소로 접속 시도</p>
<ul>
<li><code>Clinet</code> , <code>Server</code> 에서 <code>저장하지 않고 계속</code> 클릭 후 웹 접속</li>
<li>이후 <code>패킷 수집</code> 중지</li>
</ul>
</li>
</ul>
</li>
<li><p>패킷 분석</p>
<ul>
<li><p>일반 분석</p>
<ul>
<li><p>캡처</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/80200f7c-d9e3-41fe-aee8-3e07600fe6ad/image.png" /></li>
</ul>
</li>
<li><p>라인별 분석</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/abdcdd7d-bd5a-41cf-ba72-b623fcb5b71c/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="실습-2-네트워크-계층3계층-ip-address-패킷-분석">실습 2. 네트워크 계층(3계층, IP Address) 패킷 분석</h2>
<h3 id="실습-환경-1">실습 환경</h3>
<ul>
<li>Windows Server 시스템 4대 로딩</li>
<li>로딩 후 <code>Client100</code>과 <code>Client200</code>끼리 통신되는지 확인</li>
<li>패킷 분석은 라우터 역할을 하는 <code>SRV100</code>과 <code>SRV200</code>에서만 하면된다.</li>
</ul>
<h3 id="작업-순서">작업 순서</h3>
<ul>
<li><code>SRV100</code>과 <code>SRV200</code>을 <code>wireshark</code> 실행할 때 <code>I/F</code> <code>외부망</code>으로 </li>
<li><code>Clinet100</code>에서 <code>Client200</code>으로 <code>ping</code> 테스트 (with <code>-t</code> 옵션)</li>
</ul>