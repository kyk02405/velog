<hr />
<h1 id="와이어샤크wireshark-개요">와이어샤크(Wireshark) 개요</h1>
<h2 id="1-와이어샤크란">1. 와이어샤크란?</h2>
<ul>
<li><strong>와이어샤크(Wireshark)</strong>는 대표적인 네트워크 패킷 분석 도구입니다.</li>
<li>1998년 <strong>Gerald Combs</strong>가 개발했으며, 현재까지 지속적으로 업데이트되고 있음.</li>
<li>원래 이름은 <strong>Ethereal</strong>이었으나, 2006년 <strong>상표 문제</strong>로 인해 현재의 이름인 Wireshark로 변경됨.</li>
<li><strong>유선 및 무선 네트워크 트래픽을 실시간 캡처</strong>하여 모니터링하고 분석 가능.</li>
</ul>
<hr />
<h2 id="2-와이어샤크의-사용-목적">2. 와이어샤크의 사용 목적</h2>
<ul>
<li><strong>네트워크 트래픽 실시간 분석</strong>을 통해 다음과 같은 용도로 사용됨:</li>
</ul>
<h3 id="🔧-네트워크-문제-해결">🔧 네트워크 문제 해결</h3>
<ul>
<li>네트워크 연결 문제 진단</li>
<li>성능 저하 원인 분석</li>
<li>보안 위협 탐지 및 대응</li>
</ul>
<h3 id="🔐-보안-분석">🔐 보안 분석</h3>
<ul>
<li>침입 탐지 및 비정상적인 활동 모니터링</li>
<li>보안 위협에 대한 상세한 트래픽 로그 분석</li>
</ul>
<h3 id="🧪-개발-및-테스트">🧪 개발 및 테스트</h3>
<ul>
<li>네트워크 기반 애플리케이션 개발 시, 통신 흐름 테스트</li>
<li>프로토콜 구현 검증 및 디버깅</li>
</ul>
<p>다음은 요청하신 <strong>주요 기능</strong>만을 마크다운 형식으로 정리한 내용입니다:</p>
<hr />
<h2 id="3-주요-기능">3. 주요 기능</h2>
<ul>
<li><p><strong>📡 실시간 패킷 캡처</strong>  </p>
<ul>
<li>네트워크 인터페이스에서 실시간으로 패킷을 캡처하고 분석</li>
</ul>
</li>
<li><p><strong>🧩 프로토콜 디코딩</strong>  </p>
<ul>
<li>다양한 네트워크 프로토콜을 해석하고 디코딩하여 상세한 정보 제공</li>
</ul>
</li>
<li><p><strong>🔍 필터링 및 검색</strong>  </p>
<ul>
<li>특정 패킷이나 프로토콜을 쉽게 찾을 수 있도록 강력한 필터링 기능 제공</li>
</ul>
</li>
<li><p><strong>📈 네트워크 흐름 분석</strong>  </p>
<ul>
<li>트래픽의 흐름을 시각적으로 분석하여 네트워크 성능을 진단</li>
</ul>
</li>
<li><p><strong>📝 보고서 생성</strong>  </p>
<ul>
<li>분석 결과를 바탕으로 다양한 형태의 보고서 자동 생성 가능</li>
</ul>
</li>
</ul>
<hr />
<h1 id="와이어샤크-구조">와이어샤크 구조</h1>
<h2 id="패킷-스니퍼sniffer">패킷 스니퍼(sniffer)</h2>
<ul>
<li>Packet capture<ul>
<li>컴퓨터가 보내거나 받은 모든 링크 레이어의 프레임을 복사하여 가져옴(무차별 모드)</li>
</ul>
</li>
<li>Packet analyzer<ul>
<li>프로토콜 메시지 안에 있는 모든 필드 내용을 보여줌</li>
<li>패킷의 헤더 구조를 이해하고 있으면 도움이 됨</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/75aed9d3-8b97-4480-bdfc-0d290fd87cd4/image.png" /></p>
<hr />
<h2 id="와이어샤크의-한계와-주의사항">와이어샤크의 한계와 주의사항</h2>
<ul>
<li>보안 문제<ul>
<li>민감한 데이터를 캡처할 수 있으므로 사용시 적절한 보안 조치가 필요</li>
</ul>
</li>
<li>성능 이슈<ul>
<li>대량의 패킷을 캡처할 경우 성능 저하 발생 가능</li>
</ul>
</li>
<li>법적 이슈<ul>
<li>네트워크 트래픽 캡처는 스니핑(Sniffing)과 동일한 과정이므로 법적 문제가 될 수 있음</li>
</ul>
</li>
</ul>
<hr />
<h1 id="와이어샤크-설치">와이어샤크 설치</h1>
<h2 id="와이어샤크-설치-1">와이어샤크 설치</h2>
<ul>
<li><a href="https://www.wireshark.org/">https://www.wireshark.org/</a></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7faae30a-f119-4dd9-b97c-ab97c3e815fb/image.png" /></p>
<hr />
<h2 id="pcappacket-capture">PCAP(Packet Capture)</h2>
<ul>
<li>네트워크 데이터 패킷을 캡처하고 분석하는데 사용되는 파일 포맷 및 API</li>
<li>네트워크 트래픽을 모니터링하고 분석하는데 사용</li>
</ul>
<h2 id="npcap-vs-winpcap-비교">Npcap vs WinPcap 비교</h2>
<table>
<thead>
<tr>
<th>항목</th>
<th>Npcap</th>
<th>WinPcap</th>
</tr>
</thead>
<tbody><tr>
<td><strong>지원 플랫폼</strong></td>
<td>Windows 10 및 최신 버전 지원</td>
<td>Windows 10에서 공식 지원 없음</td>
</tr>
<tr>
<td><strong>성능 및 안정성</strong></td>
<td>최신 드라이버 모델로 성능 및 안정성 우수</td>
<td>오래된 드라이버 모델로 성능 저하</td>
</tr>
<tr>
<td><strong>기능</strong></td>
<td>루프백 캡처 기능 지원</td>
<td>루프백 캡처 기능 없음</td>
</tr>
<tr>
<td><strong>보안</strong></td>
<td>최신 보안 패치 반영, 보안성 강화</td>
<td>업데이트 중단으로 보안 취약</td>
</tr>
<tr>
<td><strong>개발 및 지원</strong></td>
<td>적극적인 개발과 지원</td>
<td>개발 중단, 공식 지원 없음</td>
</tr>
</tbody></table>
<p>※ 루프백 캡처 : 컴퓨터의 네트워크 인터페이스에서 내부적으로 발생하는 트래픽을 캡처하는 기능.
(시스템 내부의 통신을 분석할 수 있게 해 줌)</p>
<hr />
<h1 id="와이어샤크-ui">와이어샤크 UI</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c36ee533-05e0-4eb7-8251-2b810f74921e/image.png" /></p>
<hr />
<h2 id="캡처-필터">캡처 필터</h2>
<ul>
<li>대용량 파일 캡처는 성능을 느리게 함</li>
<li>필터를 통해 원하는 패킷만 캡처 가능 (ex) TCP, UDP 등</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8223ab76-0559-468c-9476-a9067e65b460/image.png" /></p>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/84b91587-7553-4c9c-b693-682f82908e48/image.png" /></p>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7f579168-73c7-4450-bc2f-5ffc3859ef1c/image.png" /></p>
<hr />
<h2 id="패킷-목록">패킷 목록</h2>
<ul>
<li>패킷 번호(No.)<ul>
<li>캡처된 패킷의 식별 번호</li>
</ul>
</li>
<li>시간(Time)<ul>
<li>패킷이 캡처된 시간(상대시간) cf) 절대시간은 프레임 헤더 확인!!</li>
<li>요청 메시지를 보낸 후 응답 메시지를 받을 때까지 몇 초 걸렸는지 확인 가능</li>
</ul>
</li>
<li>송수신 주소</li>
<li>프로토콜</li>
<li>패킷 길이</li>
<li>패킷의 정보</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/376fa50c-fe64-4ad5-9b94-5b0d2da619ff/image.png" /></p>
<hr />
<h2 id="패킷-상세">패킷 상세</h2>
<ul>
<li>캡처된 패킷의 캡슐화(Encapsulation)된 상태를 표시<ul>
<li>(예) TCP 패킷의 경우, Frame header, IP header, TCP header 정보를 표시</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/78f3e481-3d33-42b2-9862-0afdb529b096/image.png" /></p>
<hr />
<h2 id="패킷-바이트">패킷 바이트</h2>
<ul>
<li>네트워크를 통해 실제로 전송되는 값</li>
<li>각 헤더의 값이 어느 위치에서, 어떤 값으로 표현(16진수 값)되는지 확인</li>
<li>편집 &gt; 설정 &gt; 모양 &gt; 레이아웃 에서 “패킷 다이어그램”으로 변경하면,
각 헤더의 어느 부분의 값인지 쉽게 확인 가능</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cb6b25e2-c7cb-4e21-ac3b-6208d6b231e7/image.png" /></p>
<hr />
<h1 id="패킷-마크-설정">패킷 마크 설정</h1>
<ul>
<li>마크 설정<ul>
<li>마우스 우클릭을 통해, 선택 항목 마크/해제 선택(ctrl+M)<ul>
<li>다음 마크로 이동 : ctrl + shift + N</li>
<li>이전 마크로 이동 : ctrl + shift + B</li>
</ul>
</li>
</ul>
</li>
<li>마킹한 패킷만 별도 인쇄 가능<ul>
<li>파일 &gt; 프린트 &gt; 마크한 패킷만 옵션 선택</li>
</ul>
</li>
<li>기본적으로 패킷 종류에 따라 색깔이 지정되어 있음</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a95a3d9e-4034-4856-b65b-85d3b6e5f9d3/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d96d41ef-86d7-4fa6-bd07-5aa796e9d556/image.png" /></p>
<hr />
<h1 id="패킷-필터링">패킷 필터링</h1>
<ul>
<li>표시 필터 적용<ul>
<li>사용자가 원하는 조건을 와이어샤크 상단에 입력<ul>
<li>(예) http, tcp, udp, dns 등</li>
</ul>
</li>
</ul>
</li>
<li>기본 문법에 대한 학습이 필요함(맨 뒤 참고)<ul>
<li>자동완성 적극 활용 필요!</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e7649ae4-4514-40ca-b5e2-481097409ce5/image.png" /></p>
<hr />
<h1 id="패킷-필터링-문법">패킷 필터링 문법</h1>
<ul>
<li><span style="color: red;">연산자 활용</span><ul>
<li>사용자가 원하는 패킷을 추출하기 위해 연산자 활용</li>
<li>ip.src == 192.168.0.1 or ip.src eq  192.168.0.1</li>
<li>tcp.port != 80 or tcp.port ne 80</li>
<li>tcp.seq &lt;= 1000 or tcp.seq le 1000</li>
<li>ip.src == 192.168.0.1 &amp;&amp; tcp.port == 80</li>
</ul>
</li>
</ul>
<h3 id="와이어샤크-필터-연산자-정리">와이어샤크 필터 연산자 정리</h3>
<table>
<thead>
<tr>
<th>연산자</th>
<th>키워드</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>==</code></td>
<td>eq</td>
<td>조건을 만족하는 패킷을 선택</td>
</tr>
<tr>
<td><code>!=</code></td>
<td>ne</td>
<td>조건을 만족하지 않는 패킷을 선택</td>
</tr>
<tr>
<td><code>&amp;&amp;</code></td>
<td>and</td>
<td>조건을 모두 만족하는 패킷을 선택</td>
</tr>
<tr>
<td>`</td>
<td></td>
<td>`</td>
</tr>
<tr>
<td><code>!</code></td>
<td>not</td>
<td>조건에 부합하지 않는 패킷을 선택</td>
</tr>
<tr>
<td><code>&gt;</code></td>
<td>gt</td>
<td>지정한 값을 초과하는 패킷을 선택</td>
</tr>
<tr>
<td><code>&lt;</code></td>
<td>lt</td>
<td>지정한 값보다 작은 패킷을 선택</td>
</tr>
<tr>
<td><code>&gt;=</code></td>
<td>ge</td>
<td>지정한 값보다 크거나 같은 패킷을 선택</td>
</tr>
<tr>
<td><code>&lt;=</code></td>
<td>le</td>
<td>지정한 값보다 작거나 같은 패킷을 선택</td>
</tr>
</tbody></table>
<hr />
<h1 id="캡처-파일-저장-및-열기">캡처 파일 저장 및 열기</h1>
<ul>
<li>파일 저장<ul>
<li>현재 캡처된 상태를 저장 or 사용자에 의해 추출된 상태를 저장</li>
<li>일반적으로 확장자가 pcapng로 저장</li>
<li>저장 &amp; 다른 이름으로 저장<ul>
<li>현재 캡처된 모든 패킷들을 저장</li>
</ul>
</li>
<li>지정한 패킷 내보내기</li>
<li>사용자가 필터를 통해 필요한 패킷만 추출한 것을 저장</li>
</ul>
</li>
<li>파일 열기<ul>
<li>캡처 파일(pcapng 등)을 언제든지 열 수 있음<ul>
<li>파일 &gt; 열기를 선택해 파일 열기</li>
<li>캡처 파일 더블클릭</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/83c67213-e455-4b33-86ce-eb9af1292ac6/image.png" /></p>
<hr />
<h1 id="프로토콜-분석">프로토콜 분석</h1>
<h2 id="tcpip-프로토콜">TCP/IP 프로토콜</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3e3bd9ce-4318-432e-b72a-e9e2441e2bfb/image.png" /></p>
<hr />
<h1 id="프로토콜-분석---http">프로토콜 분석 - HTTP</h1>
<ul>
<li><ol>
<li>http로 필터 설정</li>
</ol>
</li>
<li><ol start="2">
<li><a href="http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html">http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html</a></li>
</ol>
</li>
<li><ol start="3">
<li>http 요청/응답 메시지 확인</li>
</ol>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1dd0bb34-194c-4750-97f2-2d385908113d/image.png" /></p>
<hr />
<h2 id="따라가기">따라가기</h2>
<ul>
<li>분석 원하는 패킷을 선택 후,
마우스 우측 버튼 눌러 HTTP 스트림 따라가기</li>
<li>HTTP 요청 / 응답 내용을 한 눈에 확인 가능</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/688e7c41-5d1b-4094-ac0e-a5f0d0ce3352/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/da0cfb87-f67c-4dd8-a7ce-bb28cb6e72bd/image.png" /></p>
<hr />
<h2 id="http-vs-https">HTTP vs. HTTPS</h2>
<ul>
<li>HTTP는 평문으로 전송</li>
<li>HTTPS는 TLS 프로토콜로 암호화해서 전송</li>
<li>TLS는 대칭키/비대칭키 모두 사용<ul>
<li>HTTP의 데이터는 대칭키로 암호화</li>
<li>TLS는 비대칭키(공개키, 비공개키)를 이용해 암호화</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8b4d142d-db72-470a-9a00-0ebacb4addfc/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/83f1a909-4f53-49bc-b1d4-80587201c02c/image.png" /></p>
<hr />
<h2 id="tcp의-동작">TCP의 동작</h2>
<ul>
<li>연결 / 데이터 전송 / 종료과정 확인</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1c2c57c4-f5f4-46a4-aca7-8d6f565103a6/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/eb09807c-3a20-4aca-97b2-7ad1b0b2467a/image.png" /></p>
<hr />
<h2 id="tcp-컨트롤-플래그control-flag">TCP 컨트롤 플래그(Control Flag)</h2>
<ul>
<li>URG : 긴급 데이터 플래그</li>
<li>ACK : 응답 플래그</li>
<li>PSH : 넣기 플래그<ul>
<li>버퍼링 되지 않고 즉시 전달하는 데이터</li>
</ul>
</li>
<li>RST : 연결 재설정 플래그<ul>
<li>비정상적인 상황에서 연결을 즉시 종료(강제종료)</li>
</ul>
</li>
<li>SYN : 연결요청 플래그</li>
<li>FIN : 연결 종료 플래그</li>
<li>ECN-Echo<ul>
<li>수신측이 네트워크 혼잡 상태를 감지 했음을 송신측에 알림</li>
</ul>
</li>
<li>CWR<ul>
<li>송신측이 혼잡 상황을 인지하고 송신 윈도 크기를
줄였음을 수신측에 알림</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/29736ce4-8ced-4767-a084-5831c265c10d/image.png" /></p>
<hr />
<h2 id="따라가기-1">따라가기</h2>
<ul>
<li><a href="http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html">http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html</a></li>
<li>해당 HTTP 패킷에 마우스 우측 버튼 &gt; TCP 스트림 따라가기</li>
<li>패킷 상세 정보에서 포트 번호, 시퀀스 번호, 플래그 확인</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8c3e8426-04c9-414b-b9f7-57ed5579c08d/image.png" /></p>
<hr />
<h2 id="tcp-재전송">TCP 재전송</h2>
<ul>
<li>SEQ와 ACK 관계 확인<ul>
<li>확인 응답번호(ACK)를 통해 메시지 수신 여부 확인</li>
<li>수신한 확인 응답 번호를 확인 후,
그 번호를 일련번호로 설정하여 전송</li>
<li>TCP에서는 메시지를 수신하지 못하면 재전송</li>
<li>빠른 재전송(Fast Retransmit)<ul>
<li>3개의 중복 ACK를 수신할 경우 문제의 패킷을 즉시 전송</li>
<li>자신이 설정한 타임 아웃 전에 재전송하므로 빠르게 보냄</li>
<li>혼잡 현상이 발생한 것이므로 데이터 전송을 위한
윈도우 크기를 줄임</li>
</ul>
</li>
<li>tcp-retransmission.pcapng 파일</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/12e6f8f9-eb5a-42c7-ad64-40e3d7c12208/image.png" /></p>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e54c4e95-c861-434b-8dfa-a478f6545192/image.png" /></p>
<hr />
<h1 id="프로토콜-분석---ip">프로토콜 분석 - IP</h1>
<ul>
<li>IP 단편화(Fragmentation)<ul>
<li>IP 프로토콜에서 패킷을 몇 개의 작은 패킷으로 나누어 전송하고, 수신측에서 재조합하는 과정</li>
<li>식별자(Identification) : 어떤 패킷에서 단편화가 발생했는지 나타내는 값</li>
<li>단편화 플래그(flag) : 조각난 플래그가 더 있는지 표시</li>
<li>단편화 오프셋(offset) : 각 패킷은 1480의 단위로 떨어져 있음</li>
<li>ipv4-fragmentation.pcapng 파일</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/69fc5efa-5cd1-4fba-a7cb-8708d7a32ae8/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4e575326-fc0e-424b-ad4b-e95f8df7e045/image.png" /></p>
<blockquote>
<p>★ MSS(Maximum Segment Size)</p>
</blockquote>
<ul>
<li>사용자 데이터를 분할하지 않고 한 번에 보내는
최대 크기(MTU 값에 의해 결정)
★ MTU(maximum Transmission Unit)</li>
<li>네트워크에서 전송할 수 있는 최대 크기의 패킷</li>
</ul>
<hr />
<h1 id="프로토콜-분석---icmp">프로토콜 분석 - ICMP</h1>
<h2 id="ping">ping</h2>
<ul>
<li>와이어샤크에 icmp로 필터 설정</li>
<li>ping <a href="http://www.google.com">www.google.com</a> (혹은 교수컴)</li>
<li>에코 요청 타입 : 8</li>
<li>에코 응답 타입 : 0</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6e552912-e585-4917-9628-d11075d978d6/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/06f1b087-6f3e-4558-b4be-abceec508d1e/image.png" /></p>
<hr />
<h2 id="tracert">tracert</h2>
<ul>
<li>와이어샤크에 icmp로 필터 설정</li>
<li>tracert <a href="http://www.google.com">www.google.com</a></li>
<li>ping을 사용하는 것 확인</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/44d79d05-4586-4607-bd72-a9bfe99f0a4f/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fb765955-5efb-4719-bd07-76778d2863cd/image.png" /></p>
<hr />
<h1 id="프로토콜-분석---arp">프로토콜 분석 - ARP</h1>
<h2 id="arp">ARP</h2>
<ul>
<li>동일한 네트워크 대역에서 통신하기 위해
IP주소로 MAC 주소를 알아내는 프로토콜<ul>
<li>요청(Request) : Broadcast로 전송</li>
<li>응답(Reply) : 해당 IP가 unicast로 전송</li>
</ul>
</li>
<li>만약, ARP 요청한 IP가 동일한 네트워크 대역이 아니라면,
게이트웨이의 IP로 변경하여 게이트웨이의 MAC 주소 등록</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/35d18286-ad09-4392-9972-7112d0f168e4/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/895020ec-e56b-4f69-a02b-667ea58eccd6/image.png" /></p>
<hr />
<h2 id="arp-request">ARP request</h2>
<ul>
<li>220.67.174.1의 MAC 주소 확인<ul>
<li>MAC 주소가 00:00:00_00:00:00인을 확인!!</li>
<li>앞 3부분은 제조사, 뒤 3부분은 주소를 나타냄</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0f76ab48-7dfb-4afa-80f2-a8b22e5dd010/image.png" /></p>
<hr />
<h2 id="arp-reply">ARP Reply</h2>
<ul>
<li>MAC 주소가 채워져서 응답 오는 것을 확인!</li>
<li>arp -a를 통해 확인</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/04e14b7a-fd40-41a1-998f-7374a79f7566/image.png" /></p>
<hr />
<h1 id="프로토콜-분석---dns">프로토콜 분석 - DNS</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fa9f7148-ffb8-4245-828d-ee789cc8cf59/image.png" /></p>
<hr />
<h2 id="dns에-등록된-도메인의-ip-확인">DNS에 등록된 도메인의 IP 확인</h2>
<ul>
<li>nslookup <a href="http://www.youtube.com">www.youtube.com</a> [다른 DNS 주소]</li>
<li>내 컴퓨터가 등록한 DNS 서버 IP 주소 확인<ul>
<li>ipconfig /all</li>
</ul>
</li>
<li>DNS 서버에 등록된 도메인의 IP 확인</li>
<li>내가 사용하는 DNS 서버 이외에 다른 DNS 사용 가능<ul>
<li>구글 : 8.8.8.8</li>
<li>KT : 168.126.63.1</li>
<li>SKB : 210.220.163.82</li>
<li>LGU+ : 164.124.101.2</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b3c550a9-4ebc-4e20-b528-75f7ac20ba59/image.png" /></p>
<hr />
<h1 id="패킷-필터링-문법-1">패킷 필터링 문법</h1>
<hr />
<h2 id="기본-프로토콜">기본 프로토콜</h2>
<table>
<thead>
<tr>
<th>필터</th>
<th>설명 (한글 요약)</th>
</tr>
</thead>
<tbody><tr>
<td><strong>eth</strong></td>
<td>이더넷 프레임 분석</td>
</tr>
<tr>
<td><strong>ip</strong></td>
<td>IPv4 패킷 분석</td>
</tr>
<tr>
<td><strong>ipv6</strong></td>
<td>IPv6 패킷 분석</td>
</tr>
<tr>
<td><strong>arp</strong></td>
<td>MAC 주소 확인을 위한 ARP 패킷</td>
</tr>
<tr>
<td><strong>dhcp</strong></td>
<td>IP 자동 할당 관련 DHCP 트래픽</td>
</tr>
<tr>
<td><strong>rip</strong></td>
<td>거리 벡터 기반 라우팅 프로토콜</td>
</tr>
<tr>
<td><strong>ospf</strong></td>
<td>링크 상태 기반 라우팅 프로토콜</td>
</tr>
<tr>
<td><strong>bgp</strong></td>
<td>경로 벡터 기반, 인터넷 백본 라우팅 프로토콜</td>
</tr>
<tr>
<td><strong>icmp</strong></td>
<td>핑(ping)이나 트레이서트에서 사용되는 메시지 제어 프로토콜</td>
</tr>
<tr>
<td><strong>tcp</strong></td>
<td>연결 지향 통신 프로토콜 (3-way handshake 등)</td>
</tr>
<tr>
<td><strong>udp</strong></td>
<td>비연결형 통신 프로토콜 (빠르지만 신뢰성 낮음)</td>
</tr>
<tr>
<td><strong>dns</strong></td>
<td>도메인 이름을 IP로 변환하는 프로토콜</td>
</tr>
<tr>
<td><strong>http</strong></td>
<td>웹 통신의 기본 프로토콜</td>
</tr>
<tr>
<td><strong>http2</strong></td>
<td>HTTP의 속도 개선 버전 (멀티플렉싱 등 지원)</td>
</tr>
<tr>
<td><strong>http3</strong></td>
<td>QUIC 기반의 최신 HTTP 버전</td>
</tr>
<tr>
<td><strong>tls</strong></td>
<td>암호화된 보안 통신(HTTPS 등에서 사용)</td>
</tr>
</tbody></table>
<hr />
<h2 id="이더넷2계층-관련-필터">이더넷(2계층) 관련 필터</h2>
<hr />
<table>
<thead>
<tr>
<th>필터</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>eth.addr</strong></td>
<td>수신지 또는 송신지 MAC 주소 전체를 검색할 때 사용</td>
</tr>
<tr>
<td><strong>eth.dst</strong></td>
<td>수신지(Destination) MAC 주소 필터링</td>
</tr>
<tr>
<td><strong>eth.src</strong></td>
<td>송신지(Source) MAC 주소 필터링</td>
</tr>
<tr>
<td><strong>eth.len</strong></td>
<td>이더넷 페이로드의 길이 (16비트 양의 정수)</td>
</tr>
<tr>
<td><strong>eth.type</strong></td>
<td>이더넷 프레임 내 상위 프로토콜 식별 (예: IPv4는 0x0800)</td>
</tr>
</tbody></table>
<h3 id="✅-예시-사용법">✅ 예시 사용법</h3>
<ul>
<li><code>eth.src == aa:bb:cc:dd:ee:ff</code><br />→ 해당 MAC 주소에서 송신된 패킷 필터링  </li>
<li><code>eth.type == 0x0806</code><br />→ ARP 패킷만 필터링</li>
</ul>
<hr />
<h2 id="ip3계층-관련-필터">ip(3계층) 관련 필터</h2>
<hr />
<h3 id="✅-ipv4-필터-목록-요약">✅ IPv4 필터 목록 요약</h3>
<table>
<thead>
<tr>
<th>필터</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>ip.addr</strong></td>
<td>송신지 또는 수신지 IPv4 주소</td>
</tr>
<tr>
<td><strong>ip.dst</strong></td>
<td>수신지 IPv4 주소</td>
</tr>
<tr>
<td><strong>ip.src</strong></td>
<td>송신지 IPv4 주소</td>
</tr>
<tr>
<td><strong>ip.flags</strong></td>
<td>플래그 값 전체 (8비트 정수)</td>
</tr>
<tr>
<td><strong>ip.flags.df</strong></td>
<td>DF(조각 금지) 플래그</td>
</tr>
<tr>
<td><strong>ip.flags.mf</strong></td>
<td>MF(더 많은 조각 있음) 플래그</td>
</tr>
<tr>
<td><strong>ip.frag_offset</strong></td>
<td>단편화 오프셋 (16비트 정수)</td>
</tr>
<tr>
<td><strong>ip.hdr_len</strong></td>
<td>IP 헤더 길이 (8비트 정수)</td>
</tr>
<tr>
<td><strong>ip.id</strong></td>
<td>패킷 식별자 (16비트 정수)</td>
</tr>
<tr>
<td><strong>ip.len</strong></td>
<td>전체 IP 패킷 길이</td>
</tr>
<tr>
<td><strong>ip.opt.mtu</strong></td>
<td>MTU 옵션 값</td>
</tr>
<tr>
<td><strong>ip.ttl</strong></td>
<td>TTL(Time to Live, 생존 시간) 값</td>
</tr>
</tbody></table>
<h3 id="📌-실전-필터-사용-예시">📌 실전 필터 사용 예시</h3>
<ul>
<li><code>ip.src == 192.168.0.10</code><br />→ 해당 IP가 <strong>출발지인 패킷</strong>만 보기  </li>
<li><code>ip.dst == 8.8.8.8</code><br />→ <strong>구글 DNS 서버로 향하는 트래픽</strong> 확인  </li>
<li><code>ip.ttl &lt; 10</code><br />→ TTL이 낮은 패킷만 필터링 (루프 가능성 진단 등)</li>
</ul>
<hr />
<h2 id="udp4계층-관련-필터">udp(4계층) 관련 필터</h2>
<hr />
<h3 id="✅-udp-필터-정리">✅ UDP 필터 정리</h3>
<table>
<thead>
<tr>
<th>필터</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>udp.port</strong></td>
<td>수신지 또는 송신지 포트 번호 (16비트 정수)</td>
</tr>
<tr>
<td><strong>udp.dstport</strong></td>
<td>수신지 포트 번호</td>
</tr>
<tr>
<td><strong>udp.srcport</strong></td>
<td>송신지 포트 번호</td>
</tr>
<tr>
<td><strong>udp.length</strong></td>
<td>UDP 데이터그램 전체 길이 (헤더 + 데이터, 16비트 정수)</td>
</tr>
</tbody></table>
<h3 id="📌-예시-필터-사용법">📌 예시 필터 사용법</h3>
<ul>
<li><code>udp.port == 53</code><br />→ DNS 요청 및 응답 패킷 확인 (UDP 53 포트 사용)</li>
<li><code>udp.srcport == 123</code><br />→ NTP 서버로부터 전송된 패킷 필터링</li>
<li><code>udp.length &gt; 100</code><br />→ 100바이트 이상인 UDP 데이터그램 확인</li>
</ul>
<hr />
<h2 id="tcp4계층-관련-필터">tcp(4계층) 관련 필터</h2>
<hr />
<h3 id="✅-tcp-필터-정리">✅ TCP 필터 정리</h3>
<table>
<thead>
<tr>
<th>필터</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>tcp.port</strong></td>
<td>송신지 또는 수신지 포트 번호</td>
</tr>
<tr>
<td><strong>tcp.dstport</strong></td>
<td>수신지 포트 번호</td>
</tr>
<tr>
<td><strong>tcp.srcport</strong></td>
<td>송신지 포트 번호</td>
</tr>
<tr>
<td><strong>tcp.seq</strong></td>
<td>순서 번호 (Sequence Number, 32비트)</td>
</tr>
<tr>
<td><strong>tcp.seq_raw</strong></td>
<td>실제 순서 번호 (32비트 음이 아닌 정수)</td>
</tr>
<tr>
<td><strong>tcp.nxtseq</strong></td>
<td>다음 순서 번호</td>
</tr>
<tr>
<td><strong>tcp.ack</strong></td>
<td>확인 응답 번호 (ACK Number)</td>
</tr>
<tr>
<td><strong>tcp.ack_raw</strong></td>
<td>실제 ACK 번호</td>
</tr>
<tr>
<td><strong>tcp.flags</strong></td>
<td>TCP 플래그 필드 전체</td>
</tr>
<tr>
<td><strong>tcp.flags.ack</strong></td>
<td>ACK 플래그 (확인 응답 여부)</td>
</tr>
<tr>
<td><strong>tcp.flags.fin</strong></td>
<td>FIN 플래그 (연결 종료 요청)</td>
</tr>
<tr>
<td><strong>tcp.flags.syn</strong></td>
<td>SYN 플래그 (연결 요청)</td>
</tr>
<tr>
<td><strong>tcp.hdr_len</strong></td>
<td>TCP 헤더 길이</td>
</tr>
<tr>
<td><strong>tcp.len</strong></td>
<td>TCP 세그먼트 데이터 길이</td>
</tr>
<tr>
<td><strong>tcp.window_size_value</strong></td>
<td>윈도 크기 (수신 측의 버퍼 크기)</td>
</tr>
<tr>
<td><strong>tcp.options.mss_val</strong></td>
<td>MSS(Maximum Segment Size) 값</td>
</tr>
<tr>
<td><strong>tcp.analysis.ack_rtt</strong></td>
<td>세그먼트에 대한 ACK까지의 RTT</td>
</tr>
<tr>
<td><strong>tcp.analysis.out_of_order</strong></td>
<td>순서가 어긋난 세그먼트</td>
</tr>
<tr>
<td><strong>tcp.analysis.retransmission</strong></td>
<td>재전송된 세그먼트</td>
</tr>
<tr>
<td><strong>tcp.analysis.fast_retransmission</strong></td>
<td>빠른 재전송</td>
</tr>
<tr>
<td><strong>tcp.analysis.duplicate_ack</strong></td>
<td>중복된 ACK</td>
</tr>
<tr>
<td><strong>tcp.analysis.duplicate_ack_num</strong></td>
<td>중복 ACK 수 (정수)</td>
</tr>
</tbody></table>
<h3 id="📌-실전-예시">📌 실전 예시</h3>
<ul>
<li><code>tcp.flags.syn == 1 &amp;&amp; tcp.flags.ack == 0</code><br />→ <strong>TCP 3-way handshake의 시작(SYN 요청)</strong> 필터링  </li>
<li><code>tcp.analysis.retransmission</code><br />→ <strong>재전송된 패킷 확인</strong>, 네트워크 품질 분석 시 유용  </li>
<li><code>tcp.port == 443</code><br />→ HTTPS(SSL/TLS) 트래픽 확인  </li>
</ul>
<hr />
<h2 id="http-관련-필터">http 관련 필터</h2>
<hr />
<h3 id="✅-wireshark---http-필터-통합표-최종">✅ Wireshark - HTTP 필터 통합표 (최종)</h3>
<table>
<thead>
<tr>
<th>필터</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>http.request</code></td>
<td>HTTP 요청 여부</td>
</tr>
<tr>
<td><code>http.request.line</code></td>
<td>요청 라인 전체</td>
</tr>
<tr>
<td><code>http.request.method</code></td>
<td>요청 메서드 (GET, POST 등)</td>
</tr>
<tr>
<td><code>http.request.uri</code></td>
<td>전체 URI</td>
</tr>
<tr>
<td><code>http.request.uri.path</code></td>
<td>URI 경로 (/path/only)</td>
</tr>
<tr>
<td><code>http.request.uri.query</code></td>
<td>전체 쿼리 문자열</td>
</tr>
<tr>
<td><code>http.request.uri.query.parameter</code></td>
<td>쿼리 파라미터 값</td>
</tr>
<tr>
<td><code>http.request.version</code></td>
<td>HTTP 요청 버전</td>
</tr>
<tr>
<td><code>http.response</code></td>
<td>HTTP 응답 여부</td>
</tr>
<tr>
<td><code>http.response.code</code></td>
<td>HTTP 응답 코드 (예: 200, 404)</td>
</tr>
<tr>
<td><code>http.response.phrase</code></td>
<td>응답 문구 (OK, Not Found 등)</td>
</tr>
<tr>
<td><code>http.response.line</code></td>
<td>응답 라인 전체</td>
</tr>
<tr>
<td><code>http.response.version</code></td>
<td>HTTP 응답 버전</td>
</tr>
<tr>
<td><code>http.accept</code></td>
<td>Accept 헤더</td>
</tr>
<tr>
<td><code>http.accept_encoding</code></td>
<td>Accept-Encoding 헤더</td>
</tr>
<tr>
<td><code>http.accept_language</code></td>
<td>Accept-Language 헤더</td>
</tr>
<tr>
<td><code>http.cache_control</code></td>
<td>Cache-Control 헤더</td>
</tr>
<tr>
<td><code>http.connection</code></td>
<td>Connection 헤더</td>
</tr>
<tr>
<td><code>http.content_encoding</code></td>
<td>Content-Encoding 헤더</td>
</tr>
<tr>
<td><code>http.content_length</code></td>
<td>Content-Length 헤더</td>
</tr>
<tr>
<td><code>http.content_type</code></td>
<td>Content-Type 헤더</td>
</tr>
<tr>
<td><code>http.date</code></td>
<td>Date 헤더</td>
</tr>
<tr>
<td><code>http.host</code></td>
<td>Host 헤더</td>
</tr>
<tr>
<td><code>http.location</code></td>
<td>Location 헤더</td>
</tr>
<tr>
<td><code>http.last_modified</code></td>
<td>Last-Modified 헤더</td>
</tr>
<tr>
<td><code>http.server</code></td>
<td>Server 헤더</td>
</tr>
<tr>
<td><code>http.set_cookie</code></td>
<td>Set-Cookie 헤더</td>
</tr>
<tr>
<td><code>http.cookie</code></td>
<td>Cookie 헤더</td>
</tr>
<tr>
<td><code>http.user_agent</code></td>
<td>User-Agent 헤더</td>
</tr>
<tr>
<td><code>http.referer</code></td>
<td>Referer 헤더</td>
</tr>
<tr>
<td><code>http.authorization</code></td>
<td>Authorization 헤더</td>
</tr>
<tr>
<td><code>http.www_authenticate</code></td>
<td>WWW-Authenticate 헤더</td>
</tr>
</tbody></table>
<hr />
<h3 id="📌-필터-예시-몇-가지">📌 필터 예시 몇 가지</h3>
<ul>
<li><p><code>http.user_agent contains &quot;Chrome&quot;</code><br />→ 크롬 브라우저에서 요청한 패킷만 보기</p>
</li>
<li><p><code>http.set_cookie</code><br />→ 서버가 Set-Cookie를 포함한 응답만 보기</p>
</li>
<li><p><code>http.authorization</code><br />→ Authorization 헤더를 포함한 인증 요청 필터링</p>
</li>
<li><p><code>http.referer contains &quot;naver.com&quot;</code><br />→ 네이버에서 유입된 트래픽만 보기</p>
</li>
<li><p><code>http.server contains &quot;Apache&quot;</code><br />→ Apache 서버가 응답한 HTTP 트래픽만 보기</p>
</li>
</ul>
<hr />