# Cloud DX - 32 DHCP(Dynamic Host Configuration Protocol) Server

- 📅 Published: Wed, 12 Nov 2025 01:45:01 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-32-DHCPDynamic-Host-Configuration-Protocol-Server)

<hr />
<h1 id="dhcpdynamic-host-configuration-protocol-server">DHCP(Dynamic Host Configuration Protocol) Server</h1>
<h2 id="windows-server-2022-환경에서의-dhcp-server">Windows Server 2022 환경에서의 DHCP Server</h2>
<h3 id="개요">개요</h3>
<hr />
<h3 id="매우-중요한-내용">매우 중요한 내용</h3>
<ul>
<li><code>한 개의 망(Network)</code>에는 <code>DHCP Server(Router)</code>가 반드시 한 개만 존재해야 한다.</li>
<li><code>DHCP</code> 특성상 다른 망으로의 <code>Broadcasting</code>을 할 수가 없다. 즉 <code>외부망(WAN)</code> 에 있는 시스템에는 <code>IP</code>등을 부여할 수가 없다는 말인데 <code>LAN</code>환경에서만 설정하고 적용할 수가 있다.</li>
<li><code>DHCP</code>는 <code>IP</code> 대역을 정하고 <code>Client</code>들에게 <code>IP</code>를 부여하기 때문에 <code>Router</code>와 같은 역할을 한다. (<code>OSI 7 Layer</code>의 <code>3계층</code>((<code>Network Layer</code>, <code>Internet Layer</code>))</li>
</ul>
<hr />
<h3 id="임대-생성-과정">임대 생성 과정</h3>
<ul>
<li><code>Discover Packet (Client)</code></li>
<li><code>Offer Packet (DHCP)</code></li>
<li><code>Request Packet (Client)</code></li>
<li><code>ACK Packet (DHCP Server)</code></li>
</ul>
<hr />
<h3 id="작업-환경">작업 환경</h3>
<ul>
<li><code>DHCP Server</code> <code>(SRV100)</code></li>
<li><code>DHCP Client</code> <code>(Client100)</code></li>
</ul>
<hr />
<h3 id="실습-1-로컬-상태에서의-dhcp-설정">실습 1. 로컬 상태에서의 DHCP 설정</h3>
<ul>
<li><p>예약 주소를 사용하지 않은 상태에서의 임대생성</p>
<ul>
<li><p><code>Step 1.</code> <code>DHCP Server</code> <code>(SRV100)</code></p>
<ul>
<li><p><code>DHCP Server</code> 기능 설치</p>
<ul>
<li><code>서버관리자</code> - <code>DHCP</code> 체크 - <code>다시시작</code> 체크 - <code>설치</code> - <code>노란색 깃발</code>에서 - <code>커밋</code></li>
</ul>
</li>
<li><p><code>범위 지정</code></p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4b1e4dca-11f8-4a9b-a753-b5a1520860ab/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e1908534-1a71-4f08-b2d4-e87723a5fe47/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7f557c9d-8851-4116-b4db-35feafb3030e/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8849394b-2f56-4999-a492-b979f0083270/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6675d649-75c1-4257-af06-42fed5a96161/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/dff76990-f003-4bed-86a8-b9bd83107f20/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/42046ec0-6db5-4d4c-b319-6a1624c9c6a6/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e859401c-0c76-45bd-859f-4bae5b18cb38/image.png" /></li>
</ul>
</li>
<li><p><code>세부 설정</code></p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/704d87f7-7d96-4e5f-9094-25460adaf5ef/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e45ed52e-fde2-468b-83fb-afab2e45cbe7/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a3500288-0167-4b2b-aa12-0f242b8af9dd/image.png" /></li>
</ul>
</li>
<li><p><code>주소 임대</code> 영역 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/54437ff0-1474-42ec-91a5-92815b7c3422/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p><code>Step 2.</code> <code>DHCP Client</code> <code>(Clinet100)</code></p>
<ul>
<li><p><code>IP</code> 주소를 할당 받기 위한 작업</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f74c8125-c2bc-4431-9a5b-ccf1a6e37723/image.png" /></li>
</ul>
</li>
<li><p><code>IP</code> 주소 할당 받기</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/304ffb6f-71c2-4e97-949e-beb45c9d843c/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4d9fd679-0797-4818-b6e7-683ae212c4a5/image.png" /></li>
</ul>
</li>
<li><p>받아온 <code>IP</code> 주소 확인</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="실습-2-원격-상태에서의-dhcp-설정">실습 2. 원격 상태에서의 DHCP 설정</h3>