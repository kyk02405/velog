# Cloud DX - 60 IaC Terraform

- 📅 Published: Mon, 29 Dec 2025 03:17:22 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-60-IaC-Terraform)

<hr />
<h1 id="10-iac-terraform">10. IaC Terraform</h1>
<h2 id="101-iacinfrastructure-as-code-도구-terraform">10.1 IaC(Infrastructure as Code) 도구, Terraform</h2>
<hr />
<h3 id="개요">개요</h3>
<ul>
<li><code>자원(Server, Storage, Network, ...)</code>을 <code>IaC (Infrastructure as Code, 프로그래밍 코드를 이용해서 인프라 환경을 구축)</code> 할 수 있는 <code>도구(컴퓨터 언어)</code>를 말한다.</li>
<li>이 때 사용되는 프로그래밍 코드는 <code>HashiCorp Language (HCL)</code>을 이용하는데 <code>Terraform</code>은 <code>하시코(Hashicorp)</code>에서 오픈 소스로 개발 중인 <code>Infrastructure 관리 도구</code>를 말한다.</li>
<li>프로그래밍 코드를 이용하여 <code>가상 머신(EC2)</code>, <code>클라우드 자원</code>, <code>보안 그룹</code>, 네트워크 인터페이스(VPC)<code>등을 자동으로 할당하거나 관리할 수 있는 것이</code>IaC`이다.</li>
</ul>
<hr />
<h3 id="terraform-에서-자주-사용되는-주요-용어">Terraform 에서 자주 사용되는 주요 용어</h3>
<ul>
<li><p>Provisioning (프로비저닝, 공급)</p>
</li>
<li><p>Provider (프로바이더, 공급자)</p>
</li>
<li><p>Resource (리소스, 자원)</p>
</li>
<li><p>Plan (계획)</p>
<ul>
<li><code>Apply</code> 명령 전에 꼭 실행해서 발생할 수 있는 문제점 즉, 오류 등을 미리 확인할 수 있다.</li>
<li><code>Terraform</code> 프로젝트 디렉터리 아래의 모든 <code>.tf</code> 파일의 내용을 실제로 적용 가능한지 확인하는 작업을 말한다.</li>
<li><code>Terraform</code>은 이를 <code>terraform plan</code> 명령어로 제공하며, 이 명령어를 실행하면 어떤 리소스가 생성되고, 수정되고, 삭제될지 계획을 보여준다.</li>
<li><code>Terraform</code> 프로젝트 디렉터리 아래의 모든 <code>.tf</code> 파일의 내용대로 리소스를 생성, 수정, 삭제하는 일을 말한다.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="terraform-단계별-진행">Terraform 단계별 진행</h3>
<ul>
<li>Step 1. init</li>
<li>Step 2. init -update</li>
<li>Step 3. validate</li>
<li>Step 4. plan</li>
<li>Step 5. apply</li>
</ul>
<hr />
<h3 id="terraform의-언어-hclhashicorp-configuration-language">Terraform의 언어, HCL(Hashicorp Configuration Language)</h3>
<h4 id="개요-1">개요</h4>
<ul>
<li>HCL은 <code>Terraform</code>에서 사용하는 설정 언어를 말한다.</li>
<li><code>Terraform</code>에서 모든 설정과 리소스 선언은 HCL을 사용해 이루어진다.</li>
<li><code>Terraform</code>에서 HCL 파일의 확장자는 <code>.tf</code>를 사용한다.</li>
<li><code>Terraform</code> 자체는 <code>Go 프로그래밍 언어</code>로 개발 되었다. 즉, <code>Terraform</code> 도구의 핵심 코드 및 로직은 <code>Go 언어</code>로 작성되어 있다.</li>
<li>반면에, <code>Terraform</code>을 사용하는 사용자는 인프라를 정의하고 관리하기 위해 <code>HCL(HashiCorp Configuration Language)</code>을 사용한다.</li>
<li>(개발자와 사용자) 사용자는 HCL을 이용하여 자신의 클라우드 인프라, 서버 구성, 기타 관리해야 할 리소스들을 선언적으로 기술하게 된다. 따라서, <code>Terraform</code>을 개발하는 개발자와 <code>Terraform</code>을 사용하는 사용자 사이에는 사용하는 언어가 다르다.</li>
<li>(중요) <code>Terraform</code> 사용자는 <code>HCL 언어</code>로 <code>클라우드 리소스를 정의</code>하고 이 내용을 <code>Terraform CLI 애플리케이션(terraform)</code>으로 자신의 클라우드 계정에 실제로 반영할 수 있다.</li>
</ul>
<hr />
<h3 id="hcl의-간단한-예제">HCL의 간단한 예제</h3>
<h4 id="개요-2">개요</h4>
<ul>
<li>기본 구조는 블록, 식별자, 속성 및 값으로 구성된다.</li>
<li><code>Terraform</code>의 <code>HCL</code>을 이용해서 <code>AWS</code>의 <code>EC2</code> <code>Instance</code>를 구성하는 예제<pre><code class="language-bash">provider &quot;aws&quot; {                            -&gt; AWS Provider를 설정한다.
              region = &quot;us=west-2&quot;
}
resource &quot;aws_instance&quot; &quot;example&quot; {         -&gt; EC2 Instance를 생성한다.
              ami = &quot;ami-xxx...&quot;                  -&gt; 속성으로 각각 사용할 AMI와 인스턴스의 유형을 지정한다.
              instance_type = &quot;t2.micro&quot;
              tags = {                            -&gt; 인스턴스에 대한 추가 'Metadata(세부 속성)'를 제공한다.
                              Name = &quot;MyExampleInstance&quot;
              }
}</code></pre>
</li>
</ul>
<hr />
<h3 id="terraform을-사용한-웹-애플리케이션-인프라스트럭처infrastructure-프로비저닝provisioning-진행-순서">Terraform을 사용한 웹 애플리케이션 인프라스트럭처(infrastructure) 프로비저닝(Provisioning) 진행 순서</h3>
<ul>
<li>Step 1. AWS 계정을 준비하고 <code>API키</code> 를설정한다.</li>
<li>Step 2. <code>프라스트럭처</code>를 정의하는 HCL 언어로 필요한 리소스를 선언한다.</li>
<li>Step 3. 선언된 리소스들이 생성 가능에 대한 여부를 <code>lan</code>명령어를 통해서 확인한다.<ul>
<li>이 명령을 실행하면 <code>클라우드(AWS의 서비스)</code>에 적용되어 변화될 내용들을 보여준다.</li>
<li>생성하고자 하는 리소스 수만큼 반복하면서 Terraform 정의 파일을 조금씩 완성시켜 나간다.</li>
</ul>
</li>
<li>Step 4.선언된 리소스들을 <code>AWS</code>에 적용을 위해 <code>Apply</code> 명령을 실행한다</li>
<li>Step 5. 웹 애플리케이션을 배포한다.</li>
</ul>
<hr />
<h2 id="102-terraform-설치">10.2 Terraform 설치</h2>
<h3 id="시스템-구성">시스템 구성</h3>
<ul>
<li><code>램 8GB</code></li>
<li><code>추가 HDD 128GB</code></li>
</ul>
<hr />
<h3 id="aws-cli-설치-및-업데이트">AWS CLI 설치 및 업데이트</h3>
<ul>
<li><p>다운로드 및 설치</p>
<ul>
<li>방법 1. <code>Windows(64bit)</code>용 설치 관리자를 이용한 다운로드<ul>
<li><a href="https://awscli.amazonaws.com/AWSCLIV2.msi">https://awscli.amazonaws.com/AWSCLIV2.msi</a></li>
</ul>
</li>
<li>방법 2. <code>실행창(cmd)</code>에서 <code>msiexec</code>를 이용한 MSI 설치 관리자를 실행<ul>
<li><code>msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi</code></li>
</ul>
</li>
</ul>
</li>
<li><p>설치는 기본값으로 설치한다</p>
</li>
<li><p>AWS CLI 버전 확인</p>
</li>
</ul>
<h3 id="terraform-설치">Terraform 설치</h3>
<ul>
<li><p>설치 경로</p>
<ul>
<li><a href="https://developer.hashicorp.com/terraform">https://developer.hashicorp.com/terraform</a>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7792acb5-0eae-4b12-befc-75f85865efd1/image.png" /> 가급적 최신 버전을 다운로드 한다.</li>
</ul>
</li>
<li><p>지정된 경로로 이동 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/daba4cf0-f2ee-46d1-9428-48e078b1183d/image.png" /></p>
</li>
<li><p>환경 변수 편집 </p>
<ul>
<li><code>sysdm.pl</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3f2de292-f139-41a2-9ce9-4d7e315605b2/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d6c6733b-7312-499c-a877-59a02599ad8b/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h2 id="103-aws-콘솔-관리자와-terraform과의-연동을-위한-초기-작업">10.3 AWS 콘솔 관리자와 Terraform과의 연동을 위한 초기 작업</h2>
<h3 id="aws-콘솔-관리자-초기-작업">AWS 콘솔 관리자 초기 작업</h3>
<ul>
<li><code>AWS user1 사용자 생성</code></li>
</ul>
<h3 id="매우-중요-aws-iam-계정-사용을-위한-key-등록">(매우 중요) AWS IAM 계정 사용을 위한 Key 등록</h3>
<h4 id="step-1-key-확인-1">Step 1. Key 확인 1. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f5b51ee6-e41b-4940-bb7f-7c09d01bbb6f/image.png" /></h4>
<h4 id="step-2-key-등록">Step 2. Key 등록 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a5290ea6-d58a-40f1-9fd2-9735ca2009be/image.png" /></h4>
<h4 id="step-3-key-확인-2">Step 3. Key 확인 2. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8f5f44ce-979c-4e57-9856-e03e7fb4f52c/image.png" /></h4>
<hr />
<h2 id="104-실습">10.4 실습</h2>
<h3 id="실습-1-공급자와-리소스-구성을-위한-maintf-코드">실습 1. 공급자와 리소스 구성을 위한 main.tf 코드</h3>
<h4 id="ami">ami</h4>
<ul>
<li><p><code>EC2 Instance</code>를 생성하는 <code>Amazon Machine Image</code>를 말한다.</p>
</li>
<li><p><code>AMI 카탈로그</code> 확인</p>
<ul>
<li><p><code>(주의)</code> 여기서는 <code>EC2 Instatnce</code>를 생성하는 것이 아니라 <code>AMI</code> 검색에 대한 설명만 한다.</p>
</li>
<li><p><code>EC2</code> 서비스 하단에 있는 <code>인스턴스</code>를 클릭한다.</p>
</li>
<li><p>우측에서 <code>인스턴스 시작</code>을 클릭한다.</p>
</li>
<li><p><code>애플리케이션 및 OS 이미지(Amazon Machine Image)  정보</code> 하단에 있는  <code>더 많은 AMI 찾아보기</code>를 클릭한다.</p>
</li>
<li><p><code>AWS Marketplace AMI(5617)</code> 탭을 클릭한다.</p>
</li>
<li><p>상단의 <code>검색</code>란에 <code>rocky</code>를 입력한 후 검색한다.</p>
</li>
<li><p>하단에 출력된 것들 중에서 <code>Rocky Linux 9 (Official) - x86_64</code> 옆에 있는 <code>선택</code>을 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0e9f9730-1ba8-49d8-a194-84825783b51f/image.png" /></p>
</li>
<li><p><code>개요</code> 하단에 있는 <code>인스턴스 시작 시 구독</code>을 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3376870f-04a5-4ab6-83ba-d9ce997683c6/image.png" /></p>
</li>
<li><p><code>카탈로그의 AMI</code> 항목 하단에 있는 <code>이미지 ID</code> 하단의 <code>ami-06b18c6a9a323f75f</code>를 확인한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e8a44f8e-7743-495f-be28-25fdde75539b/image.png" /></p>
</li>
<li><p><code>(매우 중요)</code> <code>Terraform</code> 특성상 코드로 입력한 훟 <code>Apply</code> 명령을 실행하면 <code>AWS</code>에서 즉시 반영이 되기 때문에 <code>유료 AMI</code>를 사용하는 것이 아니라면 <code>무료 AMI</code>와 <code>프리티어</code>를 꼭 확인 후 코드에 입력해야 한다.</p>
</li>
</ul>
</li>
</ul>
<h4 id="instance_type">Instance_type</h4>
<ul>
<li><p>실행할 <code>EC2 Instance</code>의 유형을 말한다.</p>
</li>
<li><p>각각의 <code>EC2 Instance</code>가 제공하는 <code>CPU</code>, <code>메모리</code>, <code>디스크 공간</code> 및 <code>네트워크</code>는 용량이 서로 다르다.</p>
<h4 id="코드main_01tf-생성">코드(main_01.tf) 생성</h4>
</li>
<li><p>개요</p>
<ul>
<li><p><code>Region</code>을 <code>아시아 태평양 서울(ap-northeast-2)</code>로 되어 있을 것을 확인한다.</p>
</li>
<li><p><code>EC2 서비스</code> 하단에 있는 <code>AMI 카탈로그</code>를 클릭한다.</p>
</li>
<li><p><code>커뮤니티 AMI(500)</code>에 나와 있는 대부분의 <code>AMI</code>들은 <code>유료</code>인 경우가 많이 때문에 꼭 확인해야 한다.</p>
</li>
<li><p>검색란에 <code>ubuntu 18.04</code>를 입력하고 검색된 화면 하단에 있는 항목에서 <code>AMI</code>를 확인만한다.</p>
</li>
<li><p><code>AWS Marketplace AMI(82)</code> 영역을 다시 선택한 후 검색을 다시 하도록 한다.</p>
</li>
<li><p>만약, 현재 <code>Region</code>에 없다면 <code>다른 Region(us-east-2)</code>에서 검색을 하면 된다.</p>
<ul>
<li>여기서는 <code>us-east-2</code> <code>Region</code>에서 제공하고 있던 <code>ami-0c55b159cbfafe1f0</code>를 사용하도록 한다.</li>
</ul>
</li>
<li><p>따라서 <code>ami 매개변수</code>는 이 <code>AMI</code>를 복사해서 넣으면 된다.</p>
</li>
<li><p>(주의사항) 가급적 <code>AWS Marketplace AMI(82)</code>에서 검색할 것을 권장한다.</p>
</li>
<li><p><code>instance_type</code>은 <code>프리티어</code>에서 사용 가능한 <code>t2.micro</code> 인스턴스이고 <code>가상 CPU 1개</code>, <code>메모리 1GB</code>를 제공하고 있다.</p>
</li>
</ul>
</li>
<li><p>작업 </p>
<ul>
<li>Step 1. init <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7299f0bb-7495-4398-a8a2-0dbc92114586/image.png" /></li>
</ul>
</li>
</ul>