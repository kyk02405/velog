# Cloud DX - 36 AWS

- 📅 Published: Fri, 14 Nov 2025 06:01:53 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-36-AWS)

<h1 id="21-aws-amazon-web-service">21. AWS (Amazon Web Service)</h1>
<hr />
<h2 id="span-style--colorskyblueaws-free-tier-프리티어span"><span style="color: skyblue;">AWS Free Tier (프리티어)</span></h2>
<h2 id="-span-style--colorred해결-방법span-aws-프리-티어-기간이-만료되면-다음-두-가지-조치-중-하나를-수행할-수-있습니다">** <span style="color: red;">(해결 방법)</span> AWS 프리 티어 기간이 만료되면 다음 두 가지 조치 중 하나를 수행할 수 있습니다.**</h2>
<ul>
<li>AWS 서비스를 계속 사용하는 경우 계정의 모든 리소스에 온디맨드 요금이 청구됩니다.</li>
<li>AWS 서비스 사용을 중단하는 경우 추가 조치를 취해야 요금이 부과되지 않습니다.</li>
</ul>
<hr />
<h3 id="해결-방법-1-aws-서비스-계속-사용">해결 방법 1. AWS 서비스 계속 사용</h3>
<ul>
<li>Step 1. 먼저 월별로 사용하는 리소스를 검토한다.</li>
<li>Step 2. 월별 요금을 보려면 다음 단계를 완료하면 된다.<ul>
<li><code>AWS 결제 및 비용 관리 콘솔</code>을 연다.</li>
<li><code>탐색</code> 창에서 <strong>청구서</strong>를 선택한다.</li>
<li><code>날짜</code>에서 <strong>월</strong>을 선택한다.</li>
</ul>
</li>
<li>Step 3. 그런 다음 리소스의 <u><a href="https://aws.amazon.com/ko/pricing/?aws-products-pricing.sort-by=item.additionalFields.productNameLowercase&amp;aws-products-pricing.sort-order=asc&amp;awsf.Free%20Tier%20Type=*all&amp;awsf.tech-category=*all#Pricing_for_AWS_products"><strong><code>AWS 요금</code></strong></a></u>을 확인하여 무엇을 유지할지 결정한다.</li>
<li>Step 4. <code>온디맨드 요금</code>(AWS 서비스를 사용한 만큼만 비용 지불)으로 계정의 리소스를 계속 사용하려면 추가 조치를 취하지 않아도 된다.</li>
<li>Step 5. <u><a href="https://calculator.aws/#/"><strong><code>AWS 요금 계산기</code></strong></a></u>를 사용하여 'AWS 프리 티어'가 만료된 후 월별 청구액을 추정할 수 있다.</li>
</ul>
<hr />
<h3 id="해결-방법-2-aws-서비스-사용-중지">해결 방법 2. AWS 서비스 사용 중지</h3>
<ul>
<li><strong>이 방법을 권장한다.</strong></li>
<li><code>요금이 청구</code>(과금)되지 않도록 하려면 다음 단계를 완료하십시오.<ul>
<li>더 이상 필요하지 않은 활성 리소스를 제거합니다.<ul>
<li>필요하면 다시 만들어서 사용하면 된다.</li>
</ul>
</li>
<li>(선택 사항) 계정을 해지합니다.<ul>
<li>계정을 해지 하지 않아도 <code>1년</code>이 경과되면 계정은 <code>비활성 상태</code>가 된다.</li>
</ul>
</li>
<li>또한 <code>AWS 프리티어</code>의 사용 기간이 <code>1년</code>이기 때문에 <code>활성 상태</code>로 만들면 이 때 부터 사용되는 모든 <code>서비스</code> 들은 무조건 <code>온디맨드 요금</code>이 청구 된다. </li>
<li>결론은 <code>1년</code>이 경과된 후 서비스를 사용할 때의 요금은 무조건 청구된다.</li>
<li>활성 리소스나 구독이 없는 경우 요금이 청구되지 않고 계정을 활성 상태로 유지할 수 있습니다.</li>
</ul>
</li>
<li><strong>꼭 기억하자!</strong><ul>
<li>모든 서비스를 사용하고 테스트한 후에는 반드시 사용했던 서비스를 삭제하도록 한다. 그리고 필요한 경우 다시 생성해서 사용하면 된다.</li>
<li>'750시간' 동안만 사용할 수 있다.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="span-style--colorskyblueaws-프리티어를-계속-사용하기-위한-계정-생성-with-gmailspan"><span style="color: skyblue;">AWS 프리티어를 계속 사용하기 위한 계정 생성 with Gmail</span></h2>
<h3 id="개요">개요</h3>
<ul>
<li><code>2023.12.10</code>에 <code>samadal@gmail.com</code>으로 신규 가입을 했다고 하면 <code>AWS Free Tier</code> 기간은 <code>2024.12.09</code>에 만료가 된다.</li>
<li><span style="color: red;">(핵심)</span>이 때 기존에 사용하던 계정(samadal)을 사용하지 말고 즉, <code>탈퇴</code>를 하거나 <code>계정 사용 중지</code>를 한 후 신규로 계정을 생성한다.</li>
<li><code>samadal202411@gmail.com</code>, <code>samadalaws@gmail.com</code>, ... 등과 같이 신규로 가입, 생성하면 된다.<ul>
<li>Amazon에서는 </li>
</ul>
</li>
</ul>
<hr />
<h3 id="google-계정-만들기">Google 계정 만들기</h3>
<p><code>clouddxkyk@gmail.com</code>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/838d88f3-c8b6-45b6-bd63-c4190052d7ca/image.png" /></p>
<hr />
<h2 id="span-style--colorskyblueaws-iamidentity-and-access-management-사용자-계정-생성span"><span style="color: skyblue;">AWS IAM(Identity and Access Management, 사용자 계정) 생성</span></h2>
<h3 id="aws-계정과-iam-계정-차이점">AWS 계정과 IAM 계정 차이점</h3>
<h4 id="aws-계정">AWS 계정</h4>
<ul>
<li><code>E-Mail</code>을 통해 처음으로 만든 계정을 말하고 <code>루트 계정(Root Account)</code>이라고도 한다.<ul>
<li><code>Linux</code>에서의 <code>root</code>와 동일한 계정이다.</li>
</ul>
</li>
<li>AWS의 <code>자원(Resource, 리소스)</code>에 모두 접근 가능하기 때문에 <code>공용으로 사용하고자 하는 계정</code>에는 절대 추천하지 않는다.</li>
</ul>
<h4 id="iam-계정-identity--access-management-사용자-계정-및-그룹-관리">IAM 계정 (Identity &amp; Access Management, 사용자 계정 및 그룹 관리)</h4>
<ul>
<li>루트 계정 하위에서 동작 가능한 일반 사용자를 말하고 필요할 때마다 여러 개를 생성할 수도 있다.<ul>
<li><code>Linux</code>에서의 <code>samadal</code>과 동일한 계정이다.</li>
</ul>
</li>
<li>루트 계정을 사용하지 않고 <code>각각의 사용자들</code>이 AWS 자원에 직접 접근 가능하다.</li>
<li>필요에 따라 <code>사용자 계정 및 그룹 관리 권한을 부여</code>한다.</li>
</ul>
<hr />
<h3 id="iam의-특징">IAM의 특징</h3>
<ul>
<li>각 <code>AWS 서비스</code> 및 자원별 사용 권한을 지정한다.</li>
<li>역할 및 정책을 통한 쉬운 권한을 관리한다.</li>
<li>사내의 사용자 관리 시스템과 연동 관리가 가능하다.</li>
</ul>
<hr />
<h3 id="로그인-방법">로그인 방법</h3>
<ul>
<li><code>루트 계정 로그인</code> (일반적으로 ID가 이메일 계정 형태)<ul>
<li><code>https://console.aws.amazon.com/iam/home</code></li>
</ul>
</li>
<li><code>일반 사용자 계정 로그인</code> (IAM 사용자 로그인으로 링크되는 형태)<ul>
<li><code>https://567448487869.signin.aws.amazon.com/console</code></li>
</ul>
</li>
</ul>
<hr />
<h2 id="aws-회원-가입">AWS 회원 가입</h2>
<ul>
<li><u><a href="https://aws.amazon.com/ko/">AWS 홈페이지</a> </u>접속</li>
<li>우측 상단에 있는 <u><a href="https://signin.aws.amazon.com/signup?request_type=register">계정 생성 링크</a></u> 클릭</li>
<li>우측 상단에 있는 <code>Language</code> 클릭한 후 출력되는 언어를 <code>한국어</code>로 변경</li>
<li>AWS 가입 하단에 있는<ul>
<li>루트 사용자 이메일 주소 에는 앞에서 생성한 <code>Gmail</code> 계정 입력</li>
<li>AWS 계정 이름은 <code>Gmail</code>계정의 <code>아이디</code>만 입력한다</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/53c93912-716a-43c1-9789-99ee948db3e6/image.png" /></li>
</ul>
</li>
<li><code>보안 확인</code>은 화면에 나온 숫자를 입력한 후 제출을 클릭한다.</li>
<li><code>AWS 가입</code>의 <code>사용자 자격 증명</code> 확인에 <code>이메일</code>로 전송된 <code>확인 코드</code>를 입력한다</li>
<li><code>AWS 가입</code>의 5단계는 다음과 같이 입력하고 진행한다.<ul>
<li>Step 1. 암호 생성<ul>
<li>관리자(root)의 암호를 생성한다.</li>
<li>계정 플랜 선택은 무료 플랜 선택을 클릭한다.</li>
</ul>
</li>
<li>Step 2. 연락처 정보는 알아서 잘 입력한다.<ul>
<li><code>AWS를 어떻게 사용할 계획이신가요?</code> 는 <code>개인</code>을 체크한다</li>
<li>Step 3. <code>결제 정보</code> 및 <code>카드 정보 입력</code></li>
<li>Step 4. <code>자격 증명 확인</code> 및 <code>보안 확인</code></li>
<li>Step 5. <code>인증 과정</code>을 거치면 완료된다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="aws-management-console-모드를-이용한-iam-사용자-생성">AWS Management Console 모드를 이용한 IAM 사용자 생성</h2>
<h3 id="개요-1">개요</h3>
<ul>
<li><p><code>관리자 계정</code>인 <code>root</code> 하위에 <code>일반 사용자</code>를 생성하는 것을 말한다.</p>
</li>
<li><p><code>root</code>로 로그인</p>
<ul>
<li>우측 상단 콘솔 로그인<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b2df525b-d9b7-4601-9c2a-a3603185a352/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ef3ce09d-522d-4102-84e7-8a31becd0125/image.png" /></li>
<li><code>보안 자격 증명 및 구성 요소</code> -&gt; <code>IAM</code></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a2855e6f-f9a4-41a0-9048-fc66cf96dd98/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p><code>관리자 로그인</code> 시 보안을 위해 <code>2차 인증</code>을 설정한다.</p>
</li>
<li><p>우측의 <code>IAM 대시보드</code> 하단에 있는 <code>보안 권장 사항</code>을 확인한다.</p>
</li>
<li><p><code>루트 사용자에 대해 MFA 추가</code> 우측에 있는 <code>MFA추가</code> 를 클릭</p>
<ul>
<li><code>MFA(MultiFactor Authentication)</code>는 <code>다중 인증</code> 또는 <code>다단계 인증</code>이라는 뜻을 가지고 있는데 네이버에서의 <code>2차 인증</code>과 동일하다.</li>
<li>MFA 디바이스 선택 하단에서 인증 관리자 앱을 체크 한 후 <code>다음</code>을 클릭한다.<ul>
<li>이 때 <code>디바이스 이름</code>은 clouddx1501`로 입력한다.</li>
<li><code>앱(Authenticaor)</code>은 <code>Amazon Services</code>을 검색한 후 설치하면 된다.</li>
</ul>
</li>
<li><code>디바이스 설정</code>은 다음과 같이 진행한다.<ul>
<li>Step 1. <code>Google Authenticator</code> 앱을 검색하고 설치한다.</li>
<li>Step 2. <code>QR 코드 표시</code>를 클릭하고 휴대폰으로 <code>QR 코드</code>를 촬영한다.</li>
<li>Step 3. 하단에 두 개의 연속된 'MFA 코드를 입력'하고 <code>MFA 추가</code>를 클릭한다.</li>
</ul>
</li>
<li><code>멀티 팩터 인증(MFA) (1)</code>에 등록된 것을 확인할 수 있다.</li>
</ul>
</li>
</ul>