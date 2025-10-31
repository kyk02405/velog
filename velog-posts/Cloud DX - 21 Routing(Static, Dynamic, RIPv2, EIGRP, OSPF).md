# Cloud DX - 21 Routing(Static, Dynamic, RIPv2, EIGRP, OSPF)

- 📅 Published: Fri, 24 Oct 2025 09:09:36 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-21-Routing)

<hr />
<h1 id="modular-interface">Modular Interface</h1>
<h2 id="개요">개요</h2>
<ul>
<li>Interface의 수를 결정하는 <code>장비</code>(장치)를 말한다.</li>
<li>Module을 장착할 수 있는 공간을 <code>Slot(슬롯)</code>이라고 한다.</li>
</ul>
<h2 id="종류">종류</h2>
<ul>
<li>NM (Network Module, 큰 슬롯, LAN용)</li>
<li>WIC (WAN Interface Card, 작은 슬롯, WAN용)</li>
<li>T (Serial, WAN)</li>
<li>E (Ethernet, LAN)</li>
<li>숫자 (Interface 갯수, 포트의 갯수)</li>
</ul>
<hr />
<h2 id="cisco-router-cable">Cisco Router Cable</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f1b902c7-f3ec-4417-ae33-485845be3b3e/image.png" /></p>
<ul>
<li>DCE = 출발점</li>
<li>DTE = 도착점</li>
</ul>
<hr />
<h1 id="routing">Routing</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5a35ca67-b375-4363-a56f-898d0931df63/image.png" /></p>
<ul>
<li>여기서 말하는 <code>최적의 경로</code>는 일반적으로 근거리에 있는 장비들 즉, 적은 수의 라우터를 거칠 때를 말한다</li>
</ul>
<h2 id="매우-중요-라우팅-설정할-때는-다음과-같이-3단계만-기억하면-된다">(매우 중요) 라우팅 설정할 때는 다음과 같이 3단계만 기억하면 된다.</h2>
<ul>
<li>Static Routing과 Dynamic Routing은 1단계, 2단계는 모두 동일하고 3단계부터 달라진다.<h2 id="step-1-기본-설정라우팅-설정할-때-가장-먼저-해야-할-일들">Step 1. 기본 설정(라우팅 설정할 때 가장 먼저 해야 할 일들)</h2>
</li>
</ul>
<h2 id="step-2-라우팅-테이블pc들이-인터넷을-할-수-있게-ip를-설정">Step 2. 라우팅 테이블(PC들이 인터넷을 할 수 있게 IP를 설정)</h2>
<h2 id="step-3-라우팅-프로토콜서로-다른-망에-있는-장비들-연결">Step 3. 라우팅 프로토콜(서로 다른 망에 있는 장비들 연결)</h2>
<hr />
<h2 id="static-routing">Static Routing</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/039aa7a3-38c2-46a7-91be-04b104828e3c/image.png" /></p>
<hr />
<h2 id="01pkt"><code>01.pkt</code></h2>
<h3 id="초기-작업">초기 작업</h3>
<ul>
<li><code>토폴로지</code>(Topology, 장비 배치도)를 구성한다.</li>
<li><code>PC</code>에 이름을 지정한 후 <code>IP</code>를 설정한다.
이 때 <code>IP</code> 주소와 <code>Subnet Mask</code>만 입력하면 된다.</li>
</ul>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/88ae4457-ef76-4957-8a75-d89bb582097d/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a367be41-033a-4e03-9b8b-37753c0f36a7/image.png" /></p>
</li>
</ul>
<hr />
<ul>
<li>테스트 1. <code>PC</code>들끼리 통신<ul>
<li><code>ping</code> 명령어를 이용해서 <code>PC</code>에서 <code>PC</code>로 패킷을 전송한다.<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2d879bce-0a3c-4f68-860e-77cb05a28904/image.png" /></li>
</ul>
</li>
<li>모두 문제없이 통신이 잘 되는 것을 알 수 있다.</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>테스트 2. <code>PC</code>들에서 라우터의 내부망으로 통신<ul>
<li><code>Request timed out</code> 오류가 발생하는데 그 이유는 라우터의 내부망 설정을 하지 않았기 때문이다.<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f05762fa-c1d8-4953-9311-4330ad3aef56/image.png" /></li>
</ul>
</li>
<li>토폴로지를 확인해보면외부로의 통신을 위한 연결이 되어 있지 않기 때문에 설정할 필요가 없다.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="02pkt"><code>02.pkt</code></h2>
<ul>
<li>초기 작업<ul>
<li><code>토폴로지</code>(Topology, 장비 배치도)를 구성한다.</li>
<li><code>PC</code>에 이름을 지정한 후 <code>IP</code>를 설정한다.
이 때 <code>IP</code> 주소와 <code>Subnet Mask</code>만 입력하면 된다.</li>
<li>라우터들의 외부망을 연결할 때는 <code>WIC-2T</code> 선택해야 한다.</li>
</ul>
</li>
</ul>
<h3 id="단계별-진행">단계별 진행</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/260bfe20-3e69-4f6a-aec6-bdc478530239/image.png" /></p>
<ul>
<li><p><code>Test 1.</code>과 <code>Serial Cable</code>이 모두 연결된 상태에서의 테스트 1. </p>
<ul>
<li><code>PC1</code> -&gt; <code>PC2</code> (O)</li>
<li><code>PC1</code> -&gt; <code>R1의 이더넷</code> (X) </li>
<li><code>PC3</code> -&gt; <code>PC4</code> (O) </li>
<li><code>PC3</code> -&gt; <code>R2의 이더넷</code> (X) </li>
</ul>
</li>
<li><p><code>Test 2.</code>과 <code>Serial Cable</code>이 모두 연결된 상태에서의 테스트 2. </p>
<ul>
<li><code>PC1</code> -&gt; <code>PC3</code> (X)</li>
</ul>
</li>
</ul>
<hr />
<h2 id="span-style--color--skybluestep-1-기본-설정r1-r2span"><span style="color: skyblue;">Step 1. 기본 설정(R1, R2)</span></h2>
<pre><code class="language-swift">Router&gt;enable  
# 사용자(User) 모드에서 관리자(Privileged EXEC) 모드로 전환  
# 관리자 모드에 들어가야 설정 변경 명령어 사용 가능

Router#configure terminal  
# 전역 설정(Global Configuration) 모드 진입  
# hostname, interface, line 설정 등 주요 설정 가능

Router(config)#hostname R1  
# 라우터의 이름(호스트명)을 'R1'으로 변경  
# 이후 프롬프트가 R1(config)# 형태로 바뀜

R1(config)#no ip domain lookup  
# 오타 명령어 입력 시 자동으로 DNS 질의하지 않도록 설정  
# (오타 시 수 초간 멈추는 현상 방지)

R1(config)#line console 0  
# 콘솔(물리적 접속 포트) 설정 모드로 진입  
# 콘솔 로그인, 시간 제한, 메시지 설정 등 가능

R1(config-line)#exec-timeout 0 0  
# 콘솔 접속 시 자동 로그아웃 시간(Idle Timeout) 비활성화  
# 기본값은 10분이지만, 0 0으로 설정 시 무제한 유지

R1(config-line)#logging synchronous  
# 콘솔 창에서 로그 메시지가 입력 중간에 끼어드는 것을 방지  
# 즉, 명령어 입력 중 로그가 출력되어도 커서가 깨지지 않음

R1(config-line)#exit  
# 콘솔 설정 모드 종료 후 전역 설정 모드(config)로 복귀  </code></pre>
<ul>
<li><code>R2</code>도 같은 방법으로 설정  </li>
</ul>
<blockquote>
<table>
<thead>
<tr>
<th>단계</th>
<th>명령어</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>1</td>
<td><code>enable</code></td>
<td>관리자 모드 진입</td>
</tr>
<tr>
<td>2</td>
<td><code>configure terminal</code></td>
<td>전역 설정 모드 진입</td>
</tr>
<tr>
<td>3</td>
<td><code>hostname R1</code></td>
<td>장비 이름 설정</td>
</tr>
<tr>
<td>4</td>
<td><code>no ip domain lookup</code></td>
<td>오타 시 DNS 질의 방지</td>
</tr>
<tr>
<td>5</td>
<td><code>line console 0</code></td>
<td>콘솔 설정 모드 진입</td>
</tr>
<tr>
<td>6</td>
<td><code>exec-timeout 0 0</code></td>
<td>콘솔 세션 무제한 유지</td>
</tr>
<tr>
<td>7</td>
<td><code>logging synchronous</code></td>
<td>로그 출력 시 커서 깨짐 방지</td>
</tr>
<tr>
<td>8</td>
<td><code>exit</code></td>
<td>상위 모드로 복귀</td>
</tr>
</tbody></table>
</blockquote>
<hr />
<h2 id="step-2-라우팅-테이블pc들이-인터넷을-할-수-있게-ip를-설정-1">Step 2. 라우팅 테이블(PC들이 인터넷을 할 수 있게 IP를 설정)</h2>
<h3 id="r1">R1</h3>
<ul>
<li><code>Ethernet(LAN 구간)</code> 설정</li>
</ul>
<pre><code class="language-swift">R1(config)#interface fastEthernet0/0
# FastEthernet 0/0 인터페이스 설정 모드 진입
# 실제 물리적 포트에 IP, 상태 설정 등을 적용할 수 있음
# 내부망과 연결된 인터페이스 선택

R1(config-if)#ip address 192.168.10.254 255.255.255.0
# FastEthernet0/0 인터페이스에 IP 주소 192.168.10.254 /24 설정

R1(config-if)#no shutdown
# 기본적으로 Cisco 라우터의 인터페이스는 'shutdown' 상태로 비활성화되어 있음  
# 'no shutdown' 명령을 통해 해당 포트를 활성화시킴
# (활성화 시 콘솔에 “Interface FastEthernet0/0, changed state to up” 메시지 출력)

R1(config)#exit</code></pre>
<ul>
<li><code>Serial(WAN 구간)</code> 설정</li>
</ul>
<pre><code class="language-swift">R1(config)#interface s0/0
# 

R1(config-if)#ip address 201.100.10.1 255.255.255.252

R1(config-if)#no shutdown 

R1(config-if)#exit</code></pre>
<p>R2도 같은 방법으로 설정</p>
<ul>
<li><p>Test 3. - <code>Ethernet Cable</code>과 <code>Serial Cable</code>이 모두 연결된 상태에서의 테스트 3. </p>
<ul>
<li>PC1 → R1의 Ethernet (O)</li>
<li>PC3 → R2의 Ethernet (O)</li>
<li>PC1 → PC3 (X)</li>
<li>PC3 → PC1 (X)</li>
</ul>
</li>
</ul>
<hr />
<h2 id="step-3-라우팅-프로토콜서로-다른-망에-있는-장비들-연결-1">Step 3. 라우팅 프로토콜(서로 다른 망에 있는 장비들 연결)</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9cabde18-fed1-4ed3-a30e-67cd83e9d78a/image.png" /></p>
<h3 id="문법">문법</h3>
<pre><code class="language-swift">R1(config)# ip route &lt;R2의 내부망 대역의 Network ID&gt; &lt;그 대역의 Subnet Mask&gt; &lt;R1과 연결된 R2의 외부망 IP주소&gt;</code></pre>
<h3 id="설정">설정</h3>
<pre><code class="language-swift">R1(config)# ip route 10.100.1.0 255.255.255.0 201.100.10.2

R2(config)# ip route 192.168.10.0 255.255.255.0 201.100.10.1</code></pre>
<ul>
<li><p>Test 4. - <code>Ethernet Cable</code>과 <code>Serial Cable</code>이 모두 연결된 상태에서의 테스트 4. </p>
<ul>
<li><code>PC1</code> -&gt; <code>R2의 이더넷</code> (O) </li>
<li><code>PC3</code> -&gt; <code>R2의 이더넷</code> (O)</li>
<li><code>PC1</code> -&gt; <code>PC3</code> (X) </li>
<li><code>PC3</code> -&gt; <code>PC1</code> (X) </li>
</ul>
</li>
</ul>
<ul>
<li><p>오류가 발생하는데<code>PC</code>들끼리 통신이 안된다.</p>
<ul>
<li><code>PC별로 IP를 설정할 때 IP Address</code>와 <code>Subnet Mask</code>만 입력했기 때문이다.</li>
<li>즉, <code>PC</code>별로 <code>Gateway</code>의 <code>IP Address</code> 까지만 도달하고 외부로 나가지 않기 때문이다.</li>
<li>따라서 <code>PC</code>별로 <code>Default Gateway</code>에 <code>Gateway</code>의 <code>IP Address</code>를 입력해야한다.</li>
</ul>
</li>
<li><p>Test 5. - <code>Ethernet Cable</code>과 <code>Serial Cable</code>이 모두 연결된 상태에서의 테스트 5. </p>
<ul>
<li><code>PC1</code> -&gt; <code>R2의 이더넷</code> (O) </li>
<li><code>PC3</code> -&gt; <code>R2의 이더넷</code> (O)</li>
<li><code>PC1</code> -&gt; <code>PC3</code> (O) </li>
<li><code>PC3</code> -&gt; <code>PC1</code> (O)   </li>
</ul>
</li>
</ul>
<hr />
<h3 id=""></h3>
<ul>
<li>정상 동작 상태 확인한 후 파일을 복사</li>
<li>오류 만들기</li>
<li>정상 동작 하도록 재구성</li>
</ul>
<hr />
<h2 id="기타-필수-기능들">기타 필수 기능들</h2>
<h3 id="기능-1-show-명령어-관리자-모드에서-실행해야-한다">기능 1. <code>Show</code> 명령어 (관리자 모드에서 실행해야 한다.)</h3>
<ul>
<li><p>I/F별 설정한 IP주소와 Routing Table과 Routing Protocol을 확인</p>
</li>
<li><p>명령 실행</p>
<pre><code class="language-swift">show ip route</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6660d520-a0dd-48bb-81e1-877b80b03141/image.png" /></p>
</li>
<li><p><code>Gateway of last resort is not set?</code></p>
<ul>
<li>정상동작하는 상태를 백업하지 않은 상태에서의 라우터 </li>
<li>라우터 설정을 완료한 후 에는 반드시<code>RAM</code>에 있는 내용을 <code>NVRAM</code>에 저장해야 한다.</li>
</ul>
</li>
</ul>
<hr />
<pre><code class="language-swift">show running-config</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9d7b5f30-6998-4276-b0c2-a4103d99b7bb/image.png" /></p>
<ul>
<li><code>RAM</code>에 들어 있는 내용을 출력</li>
<li>라우터가 꺼졌다가 켜지면 모든 설절 내용이 삭제된다.</li>
<li>즉, <code>RAM</code>에 저장된 작업한 내용(1단계 ~ 3단계) 내용을 확인</li>
</ul>
<hr />
<pre><code class="language-swift">show startup-config</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/29070cfd-a71e-4201-93f9-99df51034b5e/image.png" /></p>
<ul>
<li><code>NVRAM</code>에 들어 있는 내용을 출력</li>
<li>초기값이 없는 상태 출력</li>
</ul>
<hr />
<pre><code class="language-swift">copy</code></pre>
<ul>
<li><p><code>RAM</code>의 특성상 라우터의 전원이 꺼지면 설정한 내용들 또한 모두 삭제된다.</p>
</li>
<li><p><code>copy</code>를 이용해서 <code>RAM</code>의 내용을 <code>NVRAM</code>에 저장하면 전원이 꺼져도 그대로 유지된다.</p>
</li>
<li><p>백업</p>
</li>
<li><p>복구</p>
</li>
</ul>
<hr />
<pre><code class="language-swift">show ip interface brief</code></pre>
<ul>
<li>라우터에 연결된(되어있는) I/F의 <code>IP</code>와 장비의 동작 상태를 확인</li>
</ul>
<hr />
<pre><code class="language-swift">show interfaces / show interfaces serial 0/0</code></pre>
<ul>
<li>라우터에 연결된(되어있는) I/F의 <code>IP</code>와 장비의 동작 상태를 확인</li>
</ul>
<hr />
<h2 id="기능-2-simulation을-이용한-통신-상태-확인">기능 2. simulation을 이용한 통신 상태 확인</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4997d9c4-818f-4233-b4a4-a45e9ab49d10/image.png" /></p>
<ul>
<li>실제 장비 사이에 데이터(패킷)의 전송 상태를 실시간으로 확인</li>
</ul>
<hr />
<h2 id="기능-3-잘못-작업한-것들을-수정하고자-할-때">기능 3. 잘못 작업한 것들을 수정하고자 할 때</h2>
<ul>
<li><p>라우터 초기화</p>
<ul>
<li><p>경우에 따라서 라우터에 설정 및 저장된 모든 내용을 제거하고 재구성해야 할 경우가 발생하는데 초기화는 이런 것들을 해결하는데 도움이 된다.</p>
</li>
<li><p>반드시 파일 복사본을 생성한 후 작업해야 한다.</p>
</li>
<li><p><code>작업</code>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/77497378-ebba-4d9d-a002-4461f1509a41/image.png" /></p>
</li>
</ul>
<pre><code class="language-swift">show running-config 

show startup-config

copy running-config startup-config 

erase startup-config

reload</code></pre>
</li>
</ul>
<hr />
<h3 id="2단계에서-ip-주소를-잘못-입력한-경우">2단계에서 IP 주소를 잘못 입력한 경우</h3>
<ul>
<li>작업 전 (잘못 입력되어 있다고 가정)<pre><code class="language-swift">R1(config-if)#no ip address
</code></pre>
</li>
</ul>
<p>R1(config-if)#shutdown</p>
<pre><code>  - ![](https://velog.velcdn.com/images/kyk02405/post/f078cefc-02ce-4f36-aff4-e7b940c286c9/image.png)

- 작업 후 

```swift
R1#config terminal 

R1(config)#interface fastEthernet 0/0

R1(config-if)#ip address 192.168.10.254 255.255.255.0

R1(config-if)#no shutdown</code></pre><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a73282da-5273-484f-b973-bb94fb7fcbb7/image.png" /></li>
</ul>
<hr />
<h3 id="3단계에서-routing-protocol을-잘못-입력한-경우">3단계에서 Routing Protocol을 잘못 입력한 경우</h3>
<ul>
<li>작업 전 (잘못 입력되어 있다고 가정)</li>
</ul>
<pre><code class="language-swift">R2(config)#no ip route 192.168.10.0 255.255.255.0 201.100.10.1</code></pre>
<hr />
<h2 id="기능-4-라우터-비밀번호-설정">기능 4. 라우터 비밀번호 설정</h2>
<h3 id="console-password">Console Password</h3>
<ul>
<li>개요<ul>
<li><code>Console Cable</code> 연결을 사용해서 장비에 접근하는 것을 제한한다.</li>
<li>관리자 접근 제어 즉, 사용자 모드로 진입하는 것을 제한한다.</li>
<li>라우터 부팅 후 <code>User Mode</code>로 진입할 때 비밀번호를 물어본다.</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/65a8de70-163e-4014-8567-f9e1a8cf8650/image.png" /></p>
<ul>
<li>작업<pre><code class="language-swift">R1#conf t
</code></pre>
</li>
</ul>
<p>R1(config)#line console 0</p>
<p>R1(config-line)#login</p>
<p>R1(config-line)#password cisco1</p>
<pre><code>
---
### VTY Password

![](https://velog.velcdn.com/images/kyk02405/post/6908592b-0684-45f7-9cb3-5895c1055126/image.png)
</code></pre><p>R1(config)#line vty 0 4
R1(config-line)#login
% Login disabled on line 66, until 'password' is set
% Login disabled on line 67, until 'password' is set
% Login disabled on line 68, until 'password' is set
% Login disabled on line 69, until 'password' is set
% Login disabled on line 70, until 'password' is set
R1(config-line)#pass
R1(config-line)#password cisco2</p>
<pre><code>- 개요
  - 원격 접속(Telnet. SSH)을 통한 장비로 접근하는 것을 제한한다.
  - 가상 터미널 접근 제어를 위한 비밀번호이다.
- 작업
- 테스트
  - 추후 원격 접속 테스트시 진행

---
### Enable Password

![](https://velog.velcdn.com/images/kyk02405/post/09450d8e-95ae-413b-9c28-3e30564e82b0/image.png)</code></pre><p>enable password cisco3</p>
<pre><code>- 개요
  - 사용자 모드에서 관리자 모드로 접근하는 것을 제한한다.

---
### Secret Password


- 개요
  - 암호화 형식으로 관리자 실행 모드로 접근하는 것을 제한한다.
  - (중요) Secret Password가 설정된 경우에는 Enable Password보다 우선된다.

- 작업</code></pre><p>enable secret cisco4</p>
<pre><code>
![](https://velog.velcdn.com/images/kyk02405/post/8fc24122-733a-46c2-aea4-202d0d9b9c6d/image.png)


---
## 기능 5. 원격으로 라우터 접속 및 관리

### Telnet을 이용한 통신 (R1에서 작업)
- 개요
   - `linux`에서의 `Telnet` 참고
- 라우터 설정

![](https://velog.velcdn.com/images/kyk02405/post/bcb5b4c0-375f-4052-9ce7-e5b55b5f0159/image.png)


&gt;- `R1#conf t`: 라우터를 전역 구성 모드로 전환.
- `R1(config)#hostname R1`: 라우터 이름 설정.
- `R1(config)#enable password cisco1`: 관리자 모드 비밀번호 설정.
- `R1(config)#line vty 0 4`: 원격 접속(VTY) 라인 0-4 구성.
- `R1(config-line)#password cisco2`: VTY 비밀번호 설정.
- `R1(config-line)#login`: VTY 접속 시 비밀번호 확인 활성화.
- `R1(config-line)#exit` &amp; `R1(config)#exit`: 모드 종료.
- `%SYS-5-CONFIG_I`: 설정 콘솔 적용 완료 메시지.


- 테스트
`PC1`에서 접속
![](https://velog.velcdn.com/images/kyk02405/post/db9c6c5a-ae9a-4bea-9486-7ef0788a9f8a/image.png)


---
### SSH을 이용한 통신 (R2에서 작업)
- 개요
  - `linux`에서의 `SSH` 참고
- 라우터 설정

![](https://velog.velcdn.com/images/kyk02405/post/0061249b-b3bd-47c1-a6fe-ae945d05ffc1/image.png)



&gt;
- `R2&gt;en` &amp; `R2#conf t`: 프리빌리지 모드로 전환 후 전역 구성 모드 진입.
- `R2(config)#username samadal privilege 15 secret cisco3`: 사용자 &quot;samadal&quot;을 생성, 특권 수준 15(최고 관리자)로 설정, 비밀번호 &quot;cisco3&quot;을 비공개 방식으로 설정.
- `R2(config)#ip domain-name samadal.com`: 도메인 이름 &quot;samadal.com&quot;으로 설정.
- `R2(config)#crypto key generate rsa`: RSA 키를 생성, 1024비트 모듈러스를 선택하여 R2.samadal.com 키 이름으로 생성 완료.
- `R2(config)#
*Mar 1 0:17:35.206: %SSH-5-ENABLED: SSH 1.99 has been enabled R2(config)#`: R2 라우터에서 SSH(보안 셸)가 활성화되었음을 나타냅니다.

- 원격 접속을 위한 `SSH` 기능 활성화

![](https://velog.velcdn.com/images/kyk02405/post/3d7b1be3-c9b5-4f67-8970-3aa566a20ed6/image.png)

&gt;- `R2(config)#line vty 0 4`: VTY 라인 0~4(5개 세션) 구성 모드 진입.
- `R2(config-line)#login local`: 로컬 사용자(예: username samadal)로 인증 활성화.
- `R2(config-line)#transport input ssh`: SSH만 입력 프로토콜로 허용(텔넷 등 차단).
- `R2(config-line)#exit`: VTY 모드 종료.
- `R2(config)#ip ssh version 2`: SSH 버전 2만 사용(보안 강화).

- 테스트
`PC2`에서 접속
![](https://velog.velcdn.com/images/kyk02405/post/816a47ff-0c59-4cdf-9903-48c8a81ba816/image.png)

---
# Dynamic Routing

![](https://velog.velcdn.com/images/kyk02405/post/9ca1fc99-cd9d-469e-82f1-1974a8b70deb/image.png)

## 개요



- `Dynamic Routing`은 라우터에 의해 `(핵심)자동적으로 학습`한 원격 네트워크로 향하는 경로를 말한다.
- `Dynamic Routing Protocol`은 네트워크 
정보를 교환하여 `최적의 경로`를 결정하고, 
라우팅 테이블을 지속적으로 `유지`한다

## 프로토콜 종류
- `Routed Protocol` : `IP`, `IPX`, `Apple Talk`
- `Routing Protocol` : `RIP`, `IGRP`, `EIGRP`, `OSPF`, `IS-IS`, `BGP`, `DBMRP`, `MOSPF`, `PIM Dense &amp; Sparse` 


---
# &lt;span style = &quot;color:orange&quot;&gt;RIPv2 &lt;/span&gt;(Routing Internet Protocol version 2, 인접 라우터)

## 개요
- 속도와는 무관하고 `가장 가까운 라우터까지의 거리를 최적의 경로`로 인식하고 선택하고 통신을 한다.

&gt;## 사용법
### `Static Routing`에서의 `1단계`와 `2단계`는 모두 동일하고 `3단계`만 변경
### `3단계` `(Routing Protocol)`
- **Step 1**. `IP Routing Protocol`을 정의
  - **개요**
    - `RIP Routing Process`를 시작한다.
  - **문법**
    ```swift
    Router(config)# router &lt;PROTOCOL&gt; [keyword]
    Router(config-router)# version 2
    ```
    - 설정 예시
    ```swift
    Router(config)# router rip
    Router(config-router)# version 2
    ```
- **Step 2**. 각각의 `IP Routing Process`에 반드시 설정해야 하는 명령어
  - **개요**
    - 자신이 가진 `Network`를 알리고, 이 `Network`에서 파생된 `IP Address`가 할당된  `Interface`로 `Routing` 정보를 전송
    - 참여할 연결된 네트워크들을 선택해야 한다.
    - `NETWORK-NUMBER`는 반드시 `Major Classful Network Number` 로 설정
  - **문법**
  ```swift
  Router(config-router)# network &lt;NETWORK-NUMBER&gt; [options]</code></pre><ul>
<li><strong>설정 예시</strong><pre><code class="language-swift">Router(config-router)# network 12.168.10.0</code></pre>
<ul>
<li><code>NETWORK-NUMBER</code> 계산 요령</li>
</ul>
</li>
<li><strong>개요</strong><ul>
<li><code>Static Routing</code>에서의 작업과 달리 <code>Class</code>를 직접 적용해야 한다.</li>
</ul>
</li>
<li><strong>요령</strong><ul>
<li><code>IP Address</code> + 기본 <code>Subnet Mask</code></li>
</ul>
</li>
<li><strong>예시</strong><ul>
<li><code>192.168.10.1</code> + <code>255.255.255.0</code> = <code>192.168.10.0</code></li>
<li><code>10.100.1.1</code> + <code>255.0.0.0</code> = <code>10.0.0.0</code></li>
</ul>
</li>
</ul>
<hr />
<h3 id="01pkt-1">01.pkt</h3>
<ul>
<li>선수 작업<ul>
<li><code>Static Routing</code>에서의 <code>02.pkt</code>를 <code>01.pkt</code>로 복사한다.</li>
<li>정상적으로 통신이 되는지 먼저 확인한다</li>
<li>기존에 설정되어 있는 2단계, 3단계만 내용을 제거한다.</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f8df6a79-9817-47f1-9bf7-7f92dd96d79f/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/744482e5-7ef9-4e77-9a76-a7b8a448f1fc/image.png" /></p>
<pre><code class="language-bash">      ; 설정
   -&gt; R1
Router&gt; enable
Router# conf t
Router(config)# no ip domain lookup
Router(config)# line console 0
Router(config-line)# exec-timeout 0 0
Router(config-line)# logging sync
Router(config-line)# exit
Router(config)# 
-----------------------------------
Router(config)# int f0/0
Router(config-if)# ip addr 192.168.10.254 255.255.255.0
Router(config-if)# no shut
Router(config-if)# exit
Router(config)# 

Router(config)# int s0/0
Router(config-if)# ip addr 201.100.10.1 255.255.255.252
Router(config-if)# no shut
Router(config-if)# exit
Router(config)#
-----------------------------------
Router(config)# router rip
Router(config-router)# version 2
Router(config-router)# network 192.168.10.0
Router(config-router)# network 201.100.10.0</code></pre>
<hr />
<h2 id="용어">용어</h2>
<blockquote>
<h3 id="span-style--colorskybluebandwidth대역폭span"><span style="color: skyblue;">Bandwidth(대역폭)</span></h3>
</blockquote>
<ul>
<li><code>Serial</code> 구간의 대역폭을 지정한다</li>
<li>라우터끼리의 속도를 개선하고자 할 때 사용된다.</li>
<li>단위는 <code>kbps</code>이고 설정할 때는 <code>숫자</code>만 입력한다.</li>
<li>대부분 <code>DCE(끝점과 끝점을 연결할 떄의 시작점)</code>에서 설정하면 된다.</li>
<li>기입 위치는 <code>no shutdown</code> 이전에 입력하면 된다.</li>
</ul>
<hr />
<h4 id="문법-1">문법</h4>
<pre><code class="language-swift">bandwidth [kbps] 1024kbps</code></pre>
<ul>
<li>만약 <code>bandwidth</code>를 <code>1024kbps</code>로 설정한다고 가정하면
<code>bandwidth 1024</code>로 입력하면 된다.</li>
<li><code>1Mbps, T1 회선이라고도 한다</code><h4 id="입력">입력</h4>
<pre><code class="language-bash">int s0/0
ip addr ...
bw 1024
no shutdown</code></pre>
</li>
</ul>
<blockquote>
<h3 id="span-style--colorskyblueencapsulation캡슐화span"><span style="color: skyblue;">Encapsulation(캡슐화)</span></h3>
</blockquote>
<ul>
<li><code>Serial</code> 구간 (WAN 구간, 라우터와 라우터 사이)에서의 프로토콜을 지정한다.</li>
<li><code>bit</code>방식의 프로토콜을 말한다.</li>
</ul>
<hr />
<h4 id="문법-2">문법</h4>
<pre><code class="language-bash">encapsulation &lt;PROTOCOL&gt;</code></pre>
<h4 id="입력-1">입력</h4>
<pre><code class="language-bash">int s0/0
ip addr ...
bw 1024
encapsultaion HDLC
no shutdown</code></pre>
<blockquote>
<h3 id="span-style--colorskybluehdlcspanhigh-level-data-link-control"><span style="color: skyblue;">HDLC</span>(High-Level Data Link Control)</h3>
</blockquote>
<ul>
<li><code>PC</code>와 <code>PC</code>사이의 데이터를 전송할 때 서로 연결된 링크를 통해서 즉, <code>Frame</code>단위로 전송되는 bit방식의 프로토콜을 말한다.</li>
<li>일반적으로 <code>encapsulation</code>이라는 명령을 이용해서 전송한다.</li>
</ul>
<hr />
<h4 id="문법-3">문법</h4>
<pre><code class="language-bash">encapsulation &lt;PROTOCOL&gt;</code></pre>
<h4 id="입력-2">입력</h4>
<pre><code class="language-bash">int s0/0
ip addr ...
bw 1024
encapsultaion HDLC
no shutdown</code></pre>
<blockquote>
<h3 id="span-style--colorskybluedcespandistributed-computing-environmetn--span-style--colorskybluedtespan-data-terminal-equipmentspan"><span style="color: skyblue;">DCE</span>(Distributed Computing Environmetn) &amp; <span style="color: skyblue;">DTE</span> (Data Terminal Equipment)</span></h3>
</blockquote>
<ul>
<li><code>DCE</code>는 <code>WAN</code>구간에서의 두 점을 연결할 때의 출발점을 말한다.</li>
<li>임의의 라우터의 <code>DCE</code>에서 출발하면 도착점은 자동으로 <code>DTE</code>로 정해진다.</li>
<li><code>DCE</code>의 경우 <code>clock rate(지연시간)</code>을 함께 지정해준다.</li>
</ul>
<hr />
<h4 id="문법-4">문법</h4>
<pre><code class="language-bash">encapsulation &lt;PROTOCOL&gt;</code></pre>
<h4 id="입력-3">입력</h4>
<pre><code class="language-bash">int s0/0
ip addr ...
bw 1024
encapsultaion HDLC
no shutdown</code></pre>
<blockquote>
<h3 id="span-style--colorskyblueclock-rate지연시간span"><span style="color: skyblue;">clock rate(지연시간)</span></h3>
</blockquote>
<ul>
<li>라우터간의 동기화를 설정한다.</li>
<li>일반적으로 <code>DCE</code> 장비인 CSU(모뎀)에서 처리한다.</li>
<li>각 <code>Serial I/F</code>별 <code>no shutdown</code>이전에 입력한다.</li>
<li>정해진 값을 사용하는데 <code>clock rate ?</code>을 입력하면 값을 확인할 수가 있다.</li>
</ul>
<hr />
<h4 id="문법-5">문법</h4>
<pre><code class="language-bash">clcok rate &lt;bps 단위로 입력&gt;</code></pre>
<h4 id="입력-4">입력</h4>
<pre><code class="language-bash">int s0/0
ip addr ...
bw 1024
encapsultaion HDLC
clock rate &lt;bps 단위로 입력&gt;
no shutdown</code></pre>
<blockquote>
<h3 id="span-style--colorskyblueno-auto-summaryspan"><span style="color: skyblue;">no auto-summary</span></h3>
</blockquote>
<ul>
<li><code>Dynamic Routing</code>에서 <code>Classless</code>를 사용하기 위해서 필요하다.</li>
<li><code>Classless</code> 방식으로 라우팅 정보를 교환하고표시하기 위해서는 <code>자동 축약</code>을 <code>중지</code> 해야한다.</li>
<li>입력위치는 <code>RIPv2</code>를 예를 들면 version 2 다음, <code>network</code> 이전에 입력</li>
</ul>
<hr />
<h4 id="문법-6">문법</h4>
<pre><code class="language-swift">R1(config)# router rip
R1(config-router)# version 2
R1(config-router)# no auto-summary
R1(config-router)# network ...</code></pre>
<h4 id="입력-5">입력</h4>
<pre><code class="language-bash">R1(config)# router rip
R1(config-router)# version 2
R1(config-router)# no auto-summary
R1(config-router)# network ...</code></pre>
<hr />
<h1 id="span-style--colororangeeigrpspanenhanced-interior-gateway-routing-protocol-빠른-수렴-시간"><span style="color: orange;">EIGRP</span>(Enhanced Interior Gateway Routing Protocol, 빠른 수렴 시간)</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/711d3882-856c-46e4-a731-41ae535aa9da/image.png" /></p>
<h2 id="개요-1">개요</h2>
<ul>
<li>(핵심) Network Topology 변화에 수렴 시간이 빠르다.</li>
<li>네트워크 상에 어떤 변화(제거, 추가 등)가 발생했을 때 그 변화를 적용하는데 걸리는 시간이 짧다.</li>
</ul>
<h2 id="eigrp-packets">EIGRP Packets</h2>
<ul>
<li><p>Hello</p>
</li>
<li><p>Update</p>
</li>
<li><p>Query</p>
</li>
<li><p>Reply</p>
</li>
<li><p>ACK</p>
</li>
</ul>
<blockquote>
<h3 id="사용법">사용법</h3>
</blockquote>
<ul>
<li>IP Routing Protocol을 위한 EIGRP 설정하기 <pre><code class="language-swift">Router(config)#router eigrp autonomous-system number
Router(config-router)# 
Router(config-router)# </code></pre>
</li>
<li>연결된 Network 설정하기 (Classful Network Address를 할당한다) <pre><code class="language-swift">Router(config-router)#network network-number 
Router(config-router)# 
Router(config-router)# </code></pre>
</li>
</ul>
<hr />
<h1 id="span-style--colororangeospfspan-open-shortest-path-first-링크-상태를-광고"><span style="color: orange;">OSPF</span> (Open Shortest Path First, 링크 상태를 광고)</h1>
<h2 id="개요-2">개요</h2>
<ul>
<li><p><code>OSPF</code>는 IETF(국제 인터넷 표준화 기구) 표준이다 (RFC 2328) </p>
<ul>
<li><code>Internet Engineering Task Force</code></li>
<li>표준 프로토콜로 대부분의 라우터들이 이 OSPF 라우팅 프로토콜을 지원한다.</li>
</ul>
</li>
<li><p><code>Shortest Path First(SPF)</code> 알고리즘을 사용한다.</p>
<ul>
<li>알고리즘(또는 SPF)을 통해서 가장 cost가 적게 드는 경로를 최적의 경로로 계산하고 계산된 값을 라우팅 테이블에 적용한다.</li>
</ul>
</li>
<li><p><code>(핵심)Link-State Routing Protocol</code> 이다.</p>
<ul>
<li><code>Routing Table</code>을 구성할 때 <code>Routing</code> 정보를 전달받지 않고(서로를 인식해서 각 라우터의 라우팅 테이블을 업데이트 하지 않고
라우터 간의 <code>LSA(링크 상태 광고, Link-State Advertisement)</code> 패킷을 통해서 <code>Link-State Database(링크 상태에 대한 정보가 기록된 것)</code>를 구축하여 SPF알고리즘을 통해서 최적경로를 계산하고 이 값을 <code>Routing Table</code>에 등록, 사용하는 방식으로 동작하는 <code>Protocol</code>이다.</li>
</ul>
</li>
</ul>
<h2 id="사용법-1">사용법</h2>
<pre><code class="language-swift">Router(config)#router ospf process-id 
Router(config-router)#network address wildcard-mask area area-id 
Router(config-router)#</code></pre>
<h2 id="wlidcard-mask-module-07">Wlidcard Mask (Module 07.)</h2>
<h3 id="개요-3">개요</h3>
<ul>
<li><code>Subnet Mask</code> <code>11111111</code>.<code>11111111</code>.<code>11111111</code>.<code>00000000</code> <code>(255.255.255.0)</code></li>
<li><code>Wlidcard Mask</code>
<code>00000000</code>.<code>00000000</code>.<code>00000000</code>.<code>11111111</code> <code>(0.0.0.255)</code></li>
<li>체크 포인트 </li>
<li><code>Wlid mask bit 0</code>은 대응 bit값을 검사하라는 것을 의미한다.</li>
<li><code>Wlid mask bit 1</code>은 대응 bit값을 검사하지 말고 무시하라는 것을 의미한다.</li>
</ul>
<h3 id="예제">예제</h3>
<ul>
<li><p>하나의 <code>IP</code>만을 지정할 경우의 <code>WM</code></p>
<ul>
<li>모든 <code>bit</code>를 검사해서 해당 <code>IP</code>만 지정해라 </li>
<li><code>192.168.1.5</code> <code>0.0.0.0</code></li>
</ul>
</li>
<li><p><code>192.168.1.0/24</code> 서브넷의 모든 <code>IP</code>를 지정할 경우의 <code>WM</code></p>
<ul>
<li>네 번째 옥텟에 대응되는 모든 호스트를 대상으로 하겠다!</li>
<li><code>192.168.1.0</code> <code>0.0.0.255</code></li>
</ul>
</li>
<li><p>모든 <code>IP</code> 주소를 지정할 경우의 <code>WM</code></p>
<ul>
<li>모든 <code>bit</code>를 대상으로 검사하겠다!</li>
<li><code>0.0.0.0</code> <code>255.255.255.255</code></li>
</ul>
</li>
<li><p><code>Module 07. 15페이지 풀이</code></p>
<ul>
<li><code>172.30.16.0/24</code>에서 <code>172.30.31.0/24</code>까지의 IP Subnet 검사하기</li>
</ul>
</li>
<li><p>Step 1. 주어진 대역(<code>172.30.16.0/24</code> ~ <code>172.30.31.0/24</code>)은 <code>172.30.0.0/16</code>를 서브넷팅 했을 때의 <code>2번째</code> 대역이다.</p>
</li>
</ul>
<pre><code class="language-bash">        &lt;서브넷갯수&gt;      &lt;호스트갯수&gt;
      8 + 8 + 128 64 32 16 | 8 4 2 1 . 128 64 32 16 8 4 2 1

      0000    0000 00000000 ~ 1111 11111111   172.30.0.0 ~ 172.30.15.255
      0001                                            172.30.16.0 ~ 172.30.31.255
      0010   255.255.240.0  /20               172.30.32.0 ~ 172.30.31.255
      ...    
      1110                           172.30.224.0 ~ 172.30.239.255
      1111                            172.30.240.0 ~ 172.30.255.255
</code></pre>
<ul>
<li>Step 2. 따라서 각 대역별 호스트 갯수는 16개이다.</li>
<li>Step 3. 각 대역별 호스트가 16개일 때 <code>Subnet Mask</code> 는 <code>255.255.240.0</code>가 된다.</li>
<li>Step 4. <code>WM</code>는 <code>SM</code>를 뒤집으면 되니까 다음과 같이 계산된다.</li>
</ul>
<p><code>11111111</code>.<code>11111111</code>.<code>11110000</code>.<code>00000000</code> <code>(255.255.240.0)</code></p>
<p><code>00000000</code>.<code>00000000</code>.<code>00001111</code>.<code>11111111</code> <code>(0.0.15.255)</code></p>
<hr />
<h1 id="01pkt-2">01.pkt</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a7dfcb3d-a7f7-4d3d-873b-9b3b9300fc6f/image.png" /></p>
<pre><code class="language-bash">   : HQ

      hostname HQ

        int s0/0
      ip addr 10.1.10.5 255.255.255.248
      no shut

        int s0/1
      ip addr 10.1.20.5 255.255.255.248
      no shut

        int s0/2
      ip addr 10.1.30.5 255.255.255.248
      no shut

        int s0/3
      ip addr 10.1.40.5 255.255.255.248
      no shut

      router ospf 1
      network 10.1.10.0 0.0.0.7 area 0   network 10.1.10.5 0.0.0.0 area 0
      network 10.1.20.0 0.0.0.7 area 0   network 10.1.20.5 0.0.0.0 area 0
      network 10.1.30.0 0.0.0.7 area 10   network 10.1.30.5 0.0.0.0 area 10
      network 10.1.40.0 0.0.0.7 area 10   network 10.1.40.5 0.0.0.0 area 10</code></pre>
<pre><code class="language-bash">   : R1

      hostname R1

        int loopback 1
      ip addr 199.1.1.1 255.255.255.0

        int loopback 2
      ip addr 199.1.2.1 255.255.255.0

        int s0/0
      ip addr 10.1.10.1 255.255.255.248
      no shut

        int s0/0
      ip addr 10.1.12.1 255.255.255.248
      no shut

      router ospf 1
      router-id 199.1.1.1
      network 199.1.1.0 0.0.0.255 area 0   network 199.1.1.1 0.0.0.0 area 0
      network 199.1.2.0 0.0.0.255 area 0   network 199.1.2.1 0.0.0.0 area 0
      network 10.1.10.0 0.0.0.7 area 10   network 10.1.10.1 0.0.0.0 area 0
      network 10.1.12.0 0.0.0.7 area 10   network 10.1.12.1 0.0.0.0 area 0</code></pre>
<h3 id="개요-4">개요</h3>
<ul>
<li><p>경계라우터</p>
</li>
<li><p>용어</p>
<ul>
<li><p>process-id</p>
<ul>
<li>하나의 라우터에서 여러 개의 'OSPF' 프로세스를 설정할 경우 서로 구분하기
   위해서 사용하는 하나의 '인식자'라고 할 수 있다.</li>
<li>일반적으로 '1 ~ 65335' 사이에서 사용하면 된다.</li>
</ul>
</li>
<li><p>router-id</p>
<ul>
<li>'OSPF'에서 'router-id'는 매우 중요하다.</li>
<li>(핵심) 어떤 라우터가 정보를 생성했는지 또는 정보를 전달했는지에 대한 내용을 알려준다. 즉, 라우터가 '식별자 역할'을 한다</li>
<li>(핵심) 'Loopback Address'가 있는 경우에는 무조건 입력한다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="02pkt-재분배">02.pkt (재분배)</h1>
<h2 id="재분배">재분배</h2>
<ul>
<li>토폴로지상에 있는 라우터들이 모두 통신이 되려면 <code>다른 프로토콜(EIGRP)</code>을 사용하는 <code>I/F</code>와 <code>OSPF</code>를 사용하는 <code>I/F</code> 모두 재분배를 해야만 양방향 통신이 가능하다.</li>
<li>재분배는 <code>경계 라우터</code>에서 설정해야 한다.<ul>
<li>한 개의 라우터에 동일한 <code>Protocol</code>이 있는 경우에는 해당되지 않는다.</li>
<li>한 개의 라우터에 서로 다른 <code>Protocol</code>이 있는 경우에만 <code>경계 라우터</code>라고 한다.</li>
</ul>
</li>
<li><code>ABR(Area Border Router, 경계 라우터)</code><ul>
<li>3단계 설정할 때 진행한다.</li>
<li>두 개 이상의 <code>Area</code>에 소속된 라우터를 말한다.</li>
<li>각 <code>Area</code>의 <code>Backbone Area</code>간을 연결 시켜주는 라우터를 말한다.</li>
<li><code>Backbone Area (Distribution Area, 분배영역)</code><ul>
<li>라우터에 서로 다른 Area들이 연결되어 있는 영역을 말한다.</li>
<li>각 Area는 BA에 물리적으로 직접 연결되어 있다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="핵심-키포인트">핵심 키포인트</h3>
<ul>
<li><code>ospf</code>와 <code>eigrp</code>가 섞여 있는 망에서는 서로가 다른 당을 인식해줘야 한다.</li>
</ul>
<hr />
<h2 id="실습">실습</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/92bade55-718b-4ed2-94a0-78357cb83ff0/image.png" /></p>
<h3 id="2단계-설정">2단계 설정</h3>
<pre><code class="language-bash">########################################
# R1 설정
########################################
hostname R1

interface loopback 0
 ip address 1.1.1.1 255.255.255.0

interface serial 0/0
 ip address 201.120.3.1 255.255.255.252   ! R1 ↔ R2
 clock rate 64000
 no shutdown

interface serial 0/1
 ip address 192.168.10.1 255.255.255.252   ! R1 ↔ R4
 no shutdown


########################################
# R2 설정
########################################
hostname R2

interface loopback 0
 ip address 2.2.2.2 255.255.255.0

interface serial 0/0
 ip address 201.120.3.2 255.255.255.252   ! R2 ↔ R1
 no shutdown

interface serial 0/1
 ip address 198.21.14.1 255.255.255.252   ! R2 ↔ R3
 clock rate 64000
 no shutdown

interface fastethernet 1/0
 ip address 192.168.11.1 255.255.255.0
 no shutdown


########################################
# R3 설정
########################################
hostname R3

interface loopback 0
 ip address 3.3.3.3 255.255.255.0

interface loopback 1
 ip address 132.31.16.2 255.255.255.0

interface serial 0/0
 ip address 198.21.14.2 255.255.255.252   ! R3 ↔ R2
 no shutdown

interface fastethernet 1/0
 ip address 192.168.12.1 255.255.255.0
 no shutdown


########################################
# R4 설정
########################################
hostname R4

interface loopback 0
 ip address 4.4.4.4 255.255.255.0

interface serial 0/0
 ip address 192.168.10.2 255.255.255.252   ! R4 ↔ R1
 clock rate 64000
 no shutdown</code></pre>
<h3 id="3단계-설정">3단계 설정</h3>
<pre><code class="language-bash">: R1
  router ospf 1
    router-id 1.1.1.1
    network 1.1.1.0 0.0.0.255 area 0
    network 201.120.3.0 0.0.0.3 area 0

  router eigrp 10
    no auto-summary
    network 192.168.10.0


: R2
  router ospf 1
    router-id 2.2.2.2
    network 2.2.2.0 0.0.0.255 area 0
    network 201.120.3.0 0.0.0.3 area 0
    network 192.168.11.0 0.0.0.255 area 1
    network 198.21.14.0 0.0.0.3 area 1


: R3
  router ospf 1
    router-id 3.3.3.3
    network 3.3.3.0 0.0.0.255 area 1
    network 132.31.16.0 0.0.0.255 area 1
    network 192.168.12.0 0.0.0.255 area 1
    network 198.21.14.0 0.0.0.3 area 1


: R4
  router eigrp 10
    no auto-summary
    network 4.4.4.0
    network 192.168.10.0
</code></pre>
<blockquote>
<h3 id="테스트-1">테스트 1.</h3>
</blockquote>
<ul>
<li>R4 -&gt; R3 3.3.3.3으로 ping 테스트 (x)</li>
<li>R3 -&gt; R4 4.4.4.4으로 ping 테스트 (x)</li>
</ul>
<blockquote>
<h3 id="테스트-2">테스트 2.</h3>
</blockquote>
<ul>
<li>R1 -&gt; R3 3.3.3.3으로 ping 테스트 (o)</li>
<li>R1 -&gt; R4 4.4.4.4으로 ping 테스트 (x)</li>
</ul>
<hr />
<h3 id="재분배-설정-1-ospf가-eigrp를-인식할-수-있도록-ospf가-설정되어-있는-라우터r1에-재분배-설정">재분배 설정 1. OSPF가 EIGRP를 인식할 수 있도록 OSPF가 설정되어 있는 라우터(R1)에 재분배 설정</h3>
<ul>
<li>작업 개요<ul>
<li><code>R4(EIGRP AS 10)</code>에 속한 네트워크를<code>OSPF</code> 내부로 재분배 (redistribute)</li>
<li><code>subnets</code><ul>
<li>서브넷팅 된 <code>Subnet Mask</code>의 정보까지 받아와라!</li>
<li>만약 사용을 안 하면 <code>Classful(Class 환경이 적용)</code>하게 인식한다.</li>
</ul>
</li>
</ul>
</li>
<li>문법<pre><code class="language-swift">R1(router-config)# router ospf &lt;process-id&gt;
R1(router-config)# redistribute &lt;연결할 프로토콜&gt; &lt;ASN&gt; subnets</code></pre>
</li>
<li>설정<pre><code class="language-swift">R1(router)# router ospf 1
R1(router-config)# redistribue eigrp 10 subnets</code></pre>
</li>
</ul>
<blockquote>
<h3 id="테스트-3">테스트 3.</h3>
</blockquote>
<ul>
<li>R1 -&gt; R3 3.3.3.3으로 ping 테스트 (o)</li>
<li>R1 -&gt; R4 4.4.4.4으로 ping 테스트 (x)</li>
</ul>
<hr />
<h3 id="재분배-설정-2-eigrp가-ospf를-인식할-수-있도록-eigrp가-설정되어-있는-라우터r4에-재분배-설정">재분배 설정 2. EIGRP가 OSPF를 인식할 수 있도록 EIGRP가 설정되어 있는 라우터(R4)에 재분배 설정</h3>
<ul>
<li>작업 개요<ul>
<li><code>OSPF</code>에 속한 망을 R4(EIGRP AS 10) 내부로 재분배 (redistribute)</li>
</ul>
</li>
<li>문법<pre><code class="language-swift">R1(router-config)# router eigrp &lt;ASN&gt;
R1(router-config)# redistribute &lt;연결할 프로토콜&gt; &lt;process-id&gt; 
metric             : 계산 체계가 다르기 때문에 Metric 계산에 필요한
&lt;BW&gt;             : 대역폭
&lt;Delay&gt;         : 지연속도(값)
&lt;Reliability&gt;     : 신뢰성(TCP/TP 환경에서 작업이 이루어지기 때문에 )
&lt;Load&gt;             : 부하도(1이 최적)
&lt;MTU&gt;             : 최대 전송 속도</code></pre>
</li>
<li>설정<pre><code class="language-swift">R1(router)# router eigrp 10
R1(router-config)# redistribue ospf 1 metric 1544 2000 255 1 1500</code></pre>
<blockquote>
<h3 id="테스트-4">테스트 4.</h3>
</blockquote>
</li>
<li>R1 -&gt; R3 3.3.3.3으로 ping 테스트 (o)</li>
<li>R1 -&gt; R4 4.4.4.4으로 ping 테스트 (o)
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/eddc0d4d-13fb-4745-af65-fa8a504e709a/image.png" /></li>
</ul>
<blockquote>
<p>🔑 요약 한 줄
👉 “OSPF랑 EIGRP 사이를 이어주는 라우터(경계 라우터)에서 재분배를 해야, 서로 다른 프로토콜 영역끼리 핑이 통한다.”    </p>
</blockquote>
<blockquote>
</blockquote>
<ul>
<li>백본(Area 0)은 OSPF의 중심 통신망</li>
<li>모든 Area는 반드시 Area 0을 통해 통신</li>
<li>경계라우터(ABR)는 Area 0과 다른 Area를 둘 다 연결</li>
<li>그래서 경계라우터에는 Area 0(백본) 설정이 꼭 필요함</li>
</ul>