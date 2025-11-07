# Cloud DX 29 ESXi

- 📅 Published: Fri, 07 Nov 2025 03:45:49 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-29-ESXi)

<hr />
<h1 id="일반">일반</h1>
<h2 id="시스템-설정-및-설치">시스템 설정 및 설치</h2>
<ul>
<li>가상머신 작업 (HDD는 64GB, 메모리는 8192MB)</li>
<li>설치는 기본값<h2 id="네트워크-설정">네트워크 설정</h2>
</li>
<li>server용 IP(192.168.10.160)
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cc624df9-c8ba-4e23-a134-5a26e0a674b0/image.png" /></li>
<li>나머지는 기본값 그대로둔다.</li>
</ul>
<h2 id="vclient-설치">VClient 설치</h2>
<ul>
<li>기본값으로 설치</li>
</ul>
<hr />
<h1 id="실습">실습</h1>
<h2 id="가상-시스템-생성-1-오류">가상 시스템 생성 1. 오류</h2>
<ul>
<li>첫 화면에서 <code>인벤토리</code>를 클릭한 후 <code>vSPhere Client</code>로 들어간다.</li>
<li>좌측에 있는 <code>인벤토리</code>의 <code>IP</code>를 확인하고 클릭한다.</li>
<li>우측에 있는 <code>시작</code> 탭 하단의 <code>새 가상 시스템 생성</code>을 클릭한다.</li>
<li><code>구성</code>에서는 <code>표준 설치</code>를 선택한다.</li>
<li>'이름 및 위치'에서 이름은 그냥 기본값으로 둔다.</li>
<li>'스토리지'는 확인만 하고 넘어간다.</li>
<li>'게스트 운영 체제'에서는 'Linux'를 선택하고 'CentOS 4/5/6/7/(64bit)'를 선택한다.</li>
</ul>