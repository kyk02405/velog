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
<h3 id="step-1-가상-시스템-환경-설정">Step 1. 가상 시스템 환경 설정</h3>
<ul>
<li>첫 화면에서 <code>인벤토리</code>를 클릭한 후 <code>vSphere Client</code>로 들어간다.</li>
<li>좌측에 있는 <code>인벤토리</code>의 <code>IP</code>를 확인하고 클릭한다.</li>
<li>우측에 있는 <code>시작</code> 탭 하단의 <code>새 가상 시스템 생성</code>을 클릭한다.</li>
<li><code>구성</code>에서는 <code>표준 설치</code>를 선택한다.</li>
<li><code>이름 및 위치</code>에서 이름은 그냥 기본값으로 둔다.</li>
<li><code>스토리지</code>는 확인만 하고 넘어간다.</li>
<li><code>게스트 운영 체제</code>에서는 <code>Linux</code>를 선택하고 <code>CentOS 4/5/6/7/(64bit)</code>를 선택한다.</li>
<li><code>네트워크</code>는 확인만 하고 넘어간다.</li>
<li><code>디스크 생성</code>는 확인만 하고 넘어간다.</li>
<li><code>완료 준비</code>는 앞에서 설정한 내용들 중에서 변경할 사항이 있는지 확인하고, 만약 변경할 내용이 있는 경우 <code>뒤로</code>를 클릭한 후 수정하면 된다. 없다면 <code>완료</code>를 클릭한다.</li>
<li><code>인벤토리</code>에 조금 전에 추가한 <code>가상 머신(새 가상 시스템)</code>이 추가 된 것을 확인하다.</li>
</ul>
<h3 id="step-2-가상-시스템에-운영체제-설치를-위한-iso-파일-로딩">Step 2. 가상 시스템에 운영체제 설치를 위한 ISO 파일 로딩</h3>
<ul>
<li><code>인벤토리</code>에 있는 <code>가상 머신(새 가상 시스템)</code>을 클릭한다.</li>
<li>우측에 있는 <code>시작</code> 탭을 클릭한 후 하단에 있는 <code>가상 시스템 설정 편집</code>을 클릭한다.</li>
<li><code>ISO</code> 이미지 파일을 이용해서 운영체제를 설치하기 위해 <code>CD/DVD 드라이브1</code>을 클릭한다.</li>
<li>우측의 <code>디바이스 유형</code>에는 <code>3가지</code>의 유형이 있는데 <code>데이터 스토어 ISO 파일</code>을 클릭한다.</li>
<li><code>찾아보기</code>를 클릭한 후 하단에 있는 <code>vmimages</code> 폴더를 더블 클릭한다.</li>
<li><code>tools-isoimages</code> 폴더를 더블 클릭한 후 <code>linux.iso</code> 파일을 선택한 후 <code>확인</code>을 클릭한다.</li>
<li><code>데이터 스토어 ISO 파일</code>에 <code>/vmimages/tools-isoimages/linux.iso</code>이 추가된 것을 확인한 후 <code>확인</code>을 클릭한다.</li>
</ul>
<h3 id="step-3-가상-시스템에-운영체제-설치">Step 3. 가상 시스템에 운영체제 설치</h3>
<ul>
<li>우측에 있는 <code>시작</code> 탭 하단에 있는 <code>가상 시스템 전원 켜기</code>를 클릭한다.</li>
<li>이 때 <code>인벤토리</code> 하단에 있는 <code>새 가상 시스템</code>이 <code>녹색</code>으로 바뀐 것을 확인할 수 있다.</li>
<li><code>VirtualBox</code>와 같이 <code>관리자</code> 화면과 별도로 <code>동작 중인 창</code>이 보이지 않는다.</li>
<li>상단에 있는 <code>콘솔</code> 탭을 클릭하면 설치가 진행되는 것을 볼 수 있다.</li>
<li>그런데 정상적인 설치 화면이 아닌 <code>ISO 파일</code>을 인식하지 못했을 때 나타나는 화면이 보인다.</li>
<li>이 이유는, <code>ISO 파일</code>만 삽입했고 <code>부팅과 동시에 자동 인식</code>을 하지 않았기 때문에 발생하는 현상이다.</li>
<li><code>요약</code> 탭을 클릭한 후 하단에 있는 <code>전원 끄기</code>를 클릭하고 <code>예</code>를 클릭한다.</li>
<li><code>요약</code> 탭 하단에 있는 <code>설정 편집</code>을 클릭한다.</li>
<li><code>CD/DVD 드라이브1</code>을 클릭한 후 우측 상단의 <code>디바이스 상태</code>에서 <code>전원을 켤 때 연결</code>을 체크한다.</li>
<li><code>확인</code>을 클릭한 후 <code>전원 켜기</code>를 클릭하고 <code>콘솔</code> 탭을 클릭한다.<h3 id="결론">결론</h3>
</li>
<li>기본으로 제공하고 있는 <code>ISO 파일</code>인 <code>linux.iso</code> 파일은 <code>운영체제 설치</code>를 위한 파일이 아니고
<code>VMTools</code>를 설치하기 위한 파일이기 때문에 설치가 안 되고 오류가 출력되는 것이 정상적인 화면이다.</li>
<li>결론적으로 <code>정상적인 운영체제 설치</code>를 위한 <code>ISO 파일</code>은 별도로 <code>vSphere</code>에 올려야만 사용할 수 있다.</li>
</ul>
<hr />
<h2 id="가상-시스템-생성-2-정상">가상 시스템 생성 2. 정상</h2>
<h3 id="step-1-가상-시스템-생성을-위한-스토리지-등록">Step 1. 가상 시스템 생성을 위한 스토리지 등록</h3>
<ul>
<li><p><code>저장소 추가</code></p>
<ul>
<li>현재 동작 중인 가상 시스템을 종료한다.</li>
<li><code>인벤토리</code> 항목에 있는 <code>가상 머신(새 가상 시스템)</code>에서 우클릭한 후 <code>디스크에서 삭제</code>를 클릭한다.</li>
<li><code>vSphere Client</code> 창은 닫는다.</li>
<li><code>VMWare</code>에서 동작 중인 <code>Server System</code>에서 <code>F12</code>를 누른 후 종료한다.</li>
<li><code>SCSI</code> 타입의 <code>HDD</code>를 2개 추가한다.</li>
</ul>
</li>
<li><p><code>128GB</code>는 <code>ISO 파일</code>을 저장하기 위한 저장소이다.</p>
</li>
<li><p><code>256GB</code>는 <code>가상 시스템</code>을 설치하고 저장하기 위한 저장소이다.</p>
<ul>
<li>장착이 완료되면 <code>Server System</code>을 다시 켜고 <code>vSphere Client</code>에 로그인한다.</li>
</ul>
</li>
<li><p>데이터 스토어에 ISO 파일 업로드하고 가상머신 설치를 위한 스토리지 등록 </p>
<ul>
<li>좌측에 있는 '인벤토리'의 'IP'를 클릭한 후 우측에 있는 '요약'탭을 클릭한다.</li>
<li>구성 탭 클릭 후 좌측에 스토리지 클릭</li>
<li>좌측 상단에 스토리지 추가 선택</li>
<li>디스크 선택</li>
<li>우선 <code>ISO 파일</code>을 위해 추가한 <code>HDD</code>의 <code>128GB</code>선택한다.</li>
<li>다음으로 가상 시스템 설치를 위한 HDD인 256GB도 같은 방법으로 작업</li>
</ul>
</li>
</ul>
<hr />
<h3 id="step-2-가상-시스템-생성">Step 2. 가상 시스템 생성</h3>
<ul>
<li>폴더 생성<ul>
<li>데이터 스토어에 ISO파일 등록을 위한 폴더 생성</li>
<li>데이터 스토어에 <code>가상 머신 생성</code>을 위한 폴더 생성</li>
</ul>
</li>
<li>가상 머신 생성</li>
<li>가상 머신 설치</li>
</ul>
<h3 id="가상-시스템-접속">가상 시스템 접속</h3>
<ul>
<li><p><strong>네트워크 활성화</strong></p>
<ul>
<li><p><code>root</code>로 로그인한 후 바탕화면에서 우클릭하고 <code>터미널 열기</code>를 클릭한다.</p>
</li>
<li><p>다음 두 명령을 실행했을 때 모두 오류가 발생한다.</p>
<ul>
<li><code>ifconfig</code> (IP가 표시되지 않는다.)</li>
<li><code>ping 8.8.8.8</code> (외부 네트워크 통신이 되지 않는다.)</li>
</ul>
</li>
<li><p>우측 상단의 <code>전원</code> 아이콘을 클릭한다.</p>
</li>
<li><p><code>유선 꺼짐</code>을 클릭한 후 <code>유선 네트워크 설정</code>을 선택한다.</p>
</li>
<li><p><code>네트워크</code> 항목 우측의 <code>유선</code> 옆 <code>톱니바퀴</code> 아이콘을 클릭한다.</p>
</li>
<li><p>하단의 <code>자세히 보기</code> 메뉴에서 <code>자동으로 연결</code>을 체크한다.</p>
</li>
<li><p><code>IPv4</code>를 클릭한 후 <code>수동</code>을 선택하고 다음과 같이 입력한다.</p>
</li>
</ul>
</li>
<li><p>주소: <code>192.168.10.128 / 255.255.255.0 / 192.168.10.2</code></p>
</li>
<li><p>네임서버: <code>192.168.10.2</code></p>
<ul>
<li>설정 후 <code>끔</code> 상태를 <code>켬</code>으로 변경한다.</li>
</ul>
</li>
</ul>