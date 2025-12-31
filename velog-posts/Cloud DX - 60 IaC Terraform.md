# Cloud DX - 60 IaC Terraform

- 📅 Published: Mon, 29 Dec 2025 03:17:22 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-60-IaC-Terraform)

<hr />
<h1 id="10-iac-terraform">10. IaC Terraform</h1>
<h2 id="101-iacinfrastructure-as-code-도구-terraform">10.1 IaC(Infrastructure as Code) 도구, Terraform</h2>
<h3 id="101--1010-terraform을-이용한-배포">10.1 ~ 10.10 Terraform을 이용한 배포</h3>
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
<h2 id="104-실습-1-local-상태에서의-실습">10.4 실습 1. Local 상태에서의 실습</h2>
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
</ul>
<h3 id="maintf1">main.tf1</h3>
<h4 id="코드-작성-교재-53p-3-1-예제">코드 작성 (교재 53p 3-1 예제)</h4>
<pre><code class="language-bash">resource &quot;local_file&quot; &quot;abc&quot; {
    content = &quot;abc!&quot;
    filename = &quot;${path.module}/abc.txt&quot;
}</code></pre>
<h4 id="provisioning">Provisioning</h4>
<ul>
<li><code>terraform init</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8a0e2d1c-254c-4435-9036-afc70fb570d9/image.png" /></li>
</ul>
<ul>
<li><code>terraform validate</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7ab4cbc0-83bf-4b5f-81ca-ee14b4647260/image.png" /></li>
</ul>
<ul>
<li><code>terraform plan</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/28213dec-0df1-44c0-8b2a-b1fa7d6be7dc/image.png" /></li>
</ul>
<ul>
<li><code>terraform apply</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0a802539-5ce2-45a2-902e-e4c24c6c231b/image.png" /></li>
</ul>
<hr />
<h3 id="maintf2">main.tf2</h3>
<h4 id="코드-작성-교재-53p-3-1-예제-1">코드 작성 (교재 53p 3-1 예제)</h4>
<pre><code class="language-bash">resource &quot;local_file&quot; &quot;abc&quot; {
    content = &quot;abc!&quot;
    filename = &quot;${path.module}/abc.txt&quot;
}
resource &quot;local_file&quot; &quot;dev&quot; {
  content  = &quot;def!&quot;
  filename = &quot;${path.module}/def.txt&quot;
}</code></pre>
<h4 id="provisioning-1">Provisioning</h4>
<ul>
<li>소스 코드가 수정이 된 상태이기 때문에 <code>terraform init -upgrade</code>를 한다.<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e7dce78d-0888-4b49-84f1-5dc42996e0db/image.png" /></li>
</ul>
<ul>
<li><code>terraform destroy</code><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8f6935ee-0577-49c5-9e15-ff884f104e37/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/701f6e4f-3d07-43cf-b14f-e21b6a8bee9d/image.png" /></li>
</ul>
<hr />
<h3 id="maintf3">main.tf3</h3>
<h4 id="코드-작성-교재-53p-3-1-예제-2">코드 작성 (교재 53p 3-1 예제)</h4>
<pre><code class="language-bash">resource &quot;local_file&quot; &quot;abc&quot; {
    content = &quot;abc!&quot;
    filename = &quot;${path.module}/abc.txt&quot;
}
resource &quot;local_file&quot; &quot;dev&quot; {
  content  = &quot;def!&quot;
  filename = &quot;${path.module}/def.txt&quot;
}</code></pre>
<h4 id="provisioning-2">Provisioning</h4>
<hr />
<h2 id="105-실습-2-공급자provider와-리소스resource-구성을-위한-maintf-코드">10.5 실습 2. 공급자(provider)와 리소스(resource) 구성을 위한 main.tf 코드</h2>
<ul>
<li><p>ami</p>
<ul>
<li>EC2 Instance를 생성하는 Amazon Machine Image를 말한다.</li>
<li>‘AMI 카탈로그’ 확인<ul>
<li>(주의사항) 여기서는 ‘EC2 Instance’를 생성하는 것이 아니라 AMI 검색에 대한 설명만 한다.</li>
<li>‘EC2’ 서비스 하단에 있는 ‘인스턴스’를 클릭한다.</li>
<li>‘애플리케이션 및 OS 이미지(Amazon Machine Image) 정보’ 하단에 있는 ‘더 많은 AMI 찾아보기’를 클릭한다.</li>
<li>‘AWS Marketplace AMI(5617)’ 탭을 클릭한다.</li>
<li>상단의 ‘검색’란에 ‘rocky’를 입력한 후 검색한다.</li>
<li>하단에 출력된 것들 중에서 ‘Rocky Linux 9 (Official) - x86_64’ 옆에 있는 ‘선택’을 클릭한다.</li>
<li>‘개요’ 하단에 있는 ‘인스턴스 시작 시 구독’을 클릭한다.</li>
<li>‘카탈로그의 AMI’ 항목 하단에 있는 ‘이미지 ID’ 하단의 'ami-06b18c6a9a323f75f'를 확인한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c559f2b3-b5f0-4ce6-a2e0-7d7c22781104/image.png" /></li>
<li>(매우 중요) Terraform 특성상 코드로 입력된 후 ‘Apply’ 명령을 실행하면 ‘AWS’에 즉시 반영이 되기 때문에 ‘유료 AMI’를 사용하는 것이 아니라면 '무료 AMI'와 '프리티어'를 꼭 확인 후 코드에 입력해야 한다.</li>
</ul>
</li>
</ul>
</li>
<li><p>instance_type</p>
<ul>
<li>실행할 ‘EC2 Instance’의 유형을 말한다.</li>
<li>각각의 ‘EC2 Instance’가 제공하는 ‘CPU, 메모리, 디스크 공간 및 네트워크’는 용량이 서로 다르다.</li>
<li><a href="https://aws.amazon.com/ko/ec2/instance-types/">https://aws.amazon.com/ko/ec2/instance-types/</a></li>
</ul>
</li>
</ul>
<hr />
<h3 id="코드main_01tf-생성-1">코드(main_01.tf) 생성</h3>
<ul>
<li>개요<ul>
<li>‘Region’을 ‘아시아 태평양 서울(ap-northeast-2)’로 되어 있을 것을 확인한다.</li>
<li>‘EC2 서비스’ 하단에 있는 ‘AMI 카탈로그’를 클릭한다.</li>
<li>‘커뮤니티 AMI(500)’에 나와있는 대부분의 ‘AMI’들은 ‘유료’인 경우가 많기 때문에 꼭 확인해야 한다.</li>
<li>‘AWS Marketplace AMI(82)’ 영역을 다시 선택한 후 검색을 다시 하도록 한다.</li>
<li>만약, 현재 ‘Region’에 없다면 ‘다른 Region(us-east-2)’에서 검색을 하면 된다.</li>
<li>‘ami 매개변수’는 위에서 확인된 ‘ami-0c55b159cbfafe1f0’을 복사해서 넣으면 된다.</li>
<li>따라서 'ami 매개변수'는 이 'AMI'를 복사해서 넣으면 된다.</li>
<li>(주의사항) 가급적 'AWS Marketplace AMI(82)'에서 검색할 것을 권장한다.</li>
<li>‘instance_type’은 ‘프리티어’에서 사용 가능한 ‘t2.micro’ 인스턴스이고 ‘가상 CPU 1개’, ‘메모리 1GB’를 제공하고 있다.<pre><code class="language-bash">provider &quot;aws&quot; {
region = &quot;us-east-2&quot;
}
</code></pre>
</li>
</ul>
</li>
</ul>
<p>resource &quot;aws_instance&quot; &quot;ubuntu1804&quot; {
   ami = &quot;ami-0c55b159cbfafe1f0&quot;
   instance_type = &quot;t3.micro&quot;
}</p>
<pre><code>
#### 작업
- Step 1. init
- `terraform init`
```HCL
E:\Terraform&gt;terraform init
Initializing the backend...
Initializing provider plugins...
- Finding latest version of hashicorp/aws...
- Installing hashicorp/aws v6.27.0...
- Installed hashicorp/aws v6.27.0 (signed by HashiCorp)
Terraform has made some changes to the provider dependency selections recorded
in the .terraform.lock.hcl file. Review those changes and commit them to your
version control system if they represent changes you intended to make.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running &quot;terraform plan&quot; to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.</code></pre><ul>
<li>Step 2. validate<pre><code class="language-HCL">E:\Terraform&gt;terraform validate
Success! The configuration is valid.</code></pre>
</li>
</ul>
<ul>
<li>Step 3. apply<pre><code class="language-bash">E:\Terraform&gt;terraform apply
</code></pre>
</li>
</ul>
<p>Terraform used the selected providers to generate the following execution plan. Resource actions are indicated
with the following symbols:</p>
<ul>
<li>create</li>
</ul>
<p>...</p>
<pre><code>
#### 인스턴스 확인 ![](https://velog.velcdn.com/images/kyk02405/post/de592620-7093-40ac-aa1c-b844610cc842/image.png)

---
### 코드 (main_02.tf)
- ‘ami Image’가 없는 ‘Region’일 경우에는 ‘EC2 Instance’를 생성할 수가 없다.
- 해당 문구를 확인한다. ![](https://velog.velcdn.com/images/kyk02405/post/88a5b08a-9c0c-415f-99d0-bdbf294f5aea/image.png)

---
### 코드 (main_03.tf)
#### Name 필드 내용 추가 ![](https://velog.velcdn.com/images/kyk02405/post/b88339dc-338d-4f38-87f3-c2e8e5a1e50b/image.png)
- 인스턴스에서 Name란에 해당 이름이 뜬다.
- (매우 중요) ‘hashicorp/aws’의 버전에 따른 구분
  - 코드 안에 ‘terraform {}’ 블록을 삽입하지 않은 경우
    - ‘hashicorp/aws’의 버전을 자동으로 인식하기 때문에 오류가 발생하지 않는다.
  - 코드 안에 ‘terraform {}’ 블록을 삽입한 경우
    - ‘hashicorp/aws’의 버전을 현재 설치되어 있는 버전과 반드시 일치시켜야 한다.
---
### 코드 (main_04.tf) 코드 안에 terraform {} 블록을 삽입한 경우
```bash
terraform {
   required_providers {
      aws = {
         source = &quot;hashicorp/aws&quot;
         version = &quot;~&gt; 4.67.0&quot;
      }
   }
required_version = &quot;&gt;= 1.4&quot;
}

provider &quot;aws&quot; {
   region = &quot;us-east-2&quot;
}

resource &quot;aws_instance&quot; &quot;app_server&quot; {
   ami = &quot;ami-0c55b159cbfafe1f0&quot;
   instance_type = &quot;t3.micro&quot;
   tags = {
      name = &quot;TerraformUserInstance&quot;
   }
}</code></pre><h4 id="세부-상태-확인-1-show">세부 상태 확인 1. show</h4>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e01d3b0a-43db-4b70-b537-112782e736bf/image.png" /></p>
<h4 id="제거">제거 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/594a3577-8355-4ce8-b462-0b5da8a1e2ad/image.png" /></h4>
<hr />
<h2 id="106-실습-3-ubuntu-최신-버전인-ubuntu-server-2404-lts-hvm-ssd-vol-type으로-instance-생성">10.6 실습 3. Ubuntu 최신 버전인 Ubuntu Server 24.04 LTS (HVM), SSD Vol Type으로 Instance 생성</h2>
<h3 id="개요-3">개요</h3>
<pre><code class="language-bash">E:\Terraform\local&gt;aws configure list
NAME       : VALUE                    : TYPE             : LOCATION
profile    : &lt;not set&gt;                : None             : None
access_key : ****************634V     : shared-credentials-file :
secret_key : ****************T1eV     : shared-credentials-file :
region     : ap-northeast-2           : config-file      : ~/.aws/config</code></pre>
<ul>
<li><code>ami</code>를 찾는 것이 목적이다.</li>
<li>검색 후 해당 버전의 <code>ami</code>를 확인한다.</li>
</ul>
<h3 id="작업-1-ubuntu-server-2404-검색-후-ec2-instance를-생성-확인-후-삭제">작업 1. Ubuntu server 24.04 검색 후 EC2 Instance를 생성, 확인 후 삭제</h3>
<pre><code class="language-bash">terraform {
   required_providers {
      aws = {
         source = &quot;hashicorp/aws&quot;
         version = &quot;~&gt; 4.67.0&quot;
      }
   }
required_version = &quot;&gt;= 1.4&quot;
}

provider &quot;aws&quot; {
   region = &quot;ap-northeast-2&quot;
}

resource &quot;aws_instance&quot; &quot;app_server&quot; {
   ami = &quot;ami-0a71e3eb8b23101ed&quot;
   instance_type = &quot;t3.micro&quot;
   tags = {
      name = &quot;TerraformUserInstance&quot;
   }
}</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d09feea2-bba3-4bcd-be5c-470af17655dc/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/80f5c083-0b67-41c2-b1ae-20f574219d51/image.png" /></p>
<hr />
<h2 id="107-실습-4">10.7 실습 4.</h2>
<h4 id="개요-두-개의-파일로-분리">개요 (두 개의 파일로 분리)</h4>
<ul>
<li><code>provider.tf</code><pre><code class="language-bash">terraform {
 required_providers {
    aws = {
       source = &quot;hashicorp/aws&quot;
       version = &quot;~&gt; 4.67.0&quot;
    }
 }
required_version = &quot;&gt;= 1.4&quot;
}
</code></pre>
</li>
</ul>
<p>provider &quot;aws&quot; {}</p>
<pre><code>- `main.tf`
```bash
resource &quot;aws_vpc&quot; &quot;main&quot; {
   cidr_block = &quot;10.0.0.0/16&quot;
   tags = {
      Name = &quot;Terraform VPC&quot;
   }
}</code></pre><ul>
<li><code>VPC</code> 생성 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ac59e924-f01f-4b97-b78f-95530238f57d/image.png" /></li>
</ul>
<hr />
<h2 id="108-실습-5-vpc-subnet-ec2를-단계별로-생성">10.8 실습 5. VPC, Subnet, EC2를 단계별로 생성</h2>
<h3 id="terraform의-module화">Terraform의 Module화</h3>
<ul>
<li>복잡한 인프라 구조를 보다 쉽게 관리하고 재사용할 수 있도록 만드는 핵심 기능이다.</li>
<li><code>Terraform 구성 파일(*.tf)</code></li>
</ul>
<h3 id="구조">구조</h3>
<ul>
<li>구조 2. <code>Terraform Module</code>의 기본 구조<pre><code class="language-bash">Terraform Module(루트 모듈)
└──main.tf
└──modules
└──ec2_instance
│    ├ ec2.tf
│    ├ variables.tf
│    ├ outputs.tf
└─ vpn (서브 모델2)  
   ├ vpc.tf
   ├ variables.tf
   └ outputs.tf</code></pre>
</li>
</ul>
<hr />
<h3 id="module-코드-생성-1-module-파일들-생성">Module 코드 생성 1. Module 파일들 생성</h3>
<ul>
<li><p>예시 상황 설정</p>
<ul>
<li>AWS 인프라를 관리하기 위한 테라폼 구성을 만들고 있다고 상상해 보자.</li>
<li>이 인프라에는 <code>VPC, 서브넷, 보안 그룹, EC2 인스턴스</code> 등이 포함되어 있다.</li>
<li>처음에는 모든 구성을 하나의 <code>*.tf</code> 파일에 넣을 수 있지만, 이 구성이 커지면서 관리하기 어려워지기 시작한다. 이때 모듈화가 도움이 된다.</li>
</ul>
</li>
<li><p><code>VPC</code> Module</p>
<ul>
<li><code>E:/Terraform/moduels/vpc/</code> 안에 <code>vpc.tf</code>, <code>variables.tf</code>, <code>outputs.tf;</code> 들을 생성한다.</li>
<li>Step 1. vpc.tf (이 코드에는 VPC와 서브넷을 생성하는 코드가 포함되어 있다.)</li>
<li>Step 2. variables.tf (VPC 크기, 서브넷 설정 등에 사용되는 변수들을 정의)</li>
<li>Step 3. outputs.tf (생성된 VPC와 서브넷의 ID와 같은 출력값을 정의)</li>
</ul>
</li>
</ul>
<hr />
<h2 id="109-실습-6-vpc-subnet-igw-routing-자동-생성main-vpctf">10.9 실습 6. VPC, Subnet, IGW, Routing 자동 생성(main-vpc.tf)</h2>
<pre><code class="language-bash">data &quot;aws_availability_zones&quot; &quot;available&quot; {
    state = &quot;available&quot;
}

# VPC 생성
resource &quot;aws_vpc&quot; &quot;new_vpc&quot; {
    cidr_block = &quot;192.168.0.0/16&quot;
    enable_dns_hostnames = true
    enable_dns_support = true
    instance_tenancy = &quot;default&quot;

    tags = {
        Name = &quot;NEW-VPC&quot;
    }
}

# Subnet 생성
resource &quot;aws_subnet&quot; &quot;new_public_subnet_2a&quot; {
  vpc_id = aws_vpc.new_vpc.id
  cidr_block = &quot;192.168.0.0/20&quot;
  map_public_ip_on_launch = true
  availability_zone = data.aws_availability_zones.available.names[0]
  tags = {
    Name = &quot;NEW-PUBLIC-SUBNET-2A&quot;
  }
}

resource &quot;aws_subnet&quot; &quot;new_public_subnet_2b&quot; {
  vpc_id = aws_vpc.new_vpc.id
  cidr_block = &quot;192.168.16.0/20&quot;
  map_public_ip_on_launch = true
  availability_zone = data.aws_availability_zones.available.names[1]
  tags = {
    Name = &quot;NEW-PUBLIC-SUBNET-2B&quot;
  }
}
resource &quot;aws_subnet&quot; &quot;new_public_subnet_2c&quot; {
  vpc_id = aws_vpc.new_vpc.id
  cidr_block = &quot;192.168.32.0/20&quot;
  map_public_ip_on_launch = true
  availability_zone = data.aws_availability_zones.available.names[2]
  tags = {
    Name = &quot;NEW-PUBLIC-SUBNET-2C&quot;
  }
}
resource &quot;aws_subnet&quot; &quot;new_public_subnet_2d&quot; {
  vpc_id = aws_vpc.new_vpc.id
  cidr_block = &quot;192.168.48.0/20&quot;
  map_public_ip_on_launch = true
  availability_zone = data.aws_availability_zones.available.names[3]
  tags = {
    Name = &quot;NEW-PUBLIC-SUBNET-2D&quot;
  }
}

# IGW 생성
resource &quot;aws_internet_gateway&quot; &quot;new_igw&quot; {
    vpc_id = aws_vpc.new_vpc.id
    tags = {
        Name = &quot;NEW-IGW&quot;
    }
}

# Routing 테이블 생성
resource &quot;aws_route_table&quot; &quot;new_public_rtb&quot; {
  vpc_id = aws_vpc.new_vpc.id

  route {
    cidr_block = &quot;0.0.0.0/0&quot;
    gateway_id = aws_internet_gateway.new_igw.id
  }
  tags = {
    Name = &quot;NEW-PUBLIC-RTB&quot;
  }
}

resource &quot;aws_route_table_association&quot; &quot;new_public_subnet_2a_association&quot; {
  subnet_id = aws_subnet.new_public_subnet_2a.id
  route_table_id = aws_route_table.new_public_rtb.id
}
resource &quot;aws_route_table_association&quot; &quot;new_public_subnet_2b_association&quot; {
  subnet_id = aws_subnet.new_public_subnet_2b.id
  route_table_id = aws_route_table.new_public_rtb.id
}
resource &quot;aws_route_table_association&quot; &quot;new_public_subnet_2c_association&quot; {
  subnet_id = aws_subnet.new_public_subnet_2c.id
  route_table_id = aws_route_table.new_public_rtb.id
}
resource &quot;aws_route_table_association&quot; &quot;new_public_subnet_2d_association&quot; {
  subnet_id = aws_subnet.new_public_subnet_2d.id
  route_table_id = aws_route_table.new_public_rtb.id
}</code></pre>
<hr />
<h2 id="1010-실습-7-terraform을-ec2-instance-생성">10.10 실습 7. Terraform을 EC2 Instance 생성</h2>
<ul>
<li><p>위의 10.9 실습 폴더를 압축해서 backup 해놓고, 
<code>D:\0_Samadal\Personal\Terraform\vpc_ec2.tar</code> 해당 경로에 있는 압축파일을 VMware의 Win10 안 Terraform 폴더 안에 압축 해제해준다(역시 기존의 exe파일과 LICENSE는 남겨주기) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/63aeded5-7e6d-48e1-b058-46ac9d5db64c/image.png" /></p>
</li>
<li><p><code>provider.tf</code></p>
<ul>
<li><code>version = &quot;4.67.0&quot;</code> 로 수정</li>
</ul>
</li>
<li><p><code>main-ec2.tf</code></p>
<ul>
<li><code>instance_type          = &quot;t3.micro&quot;</code></li>
<li><code>key_name  = &quot;key_name&quot;</code> 로 수정</li>
</ul>
</li>
</ul>
<h3 id="키페어-생성">키페어 생성 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4ff2422d-8aa0-4a01-9584-6a777c4d6e3d/image.png" /></h3>
<ul>
<li>생성한 키페어 파일로 대체 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/163545e3-3e92-434a-8c63-27a27ec2f99b/image.png" /></li>
</ul>
<hr />
<blockquote>
<h3 id="mobaxterm">MobaXterm</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/762bbfd6-7272-4cca-a257-b61107f91aab/image.png" /></p>
</blockquote>
<hr />
<h2 id="1011-단일-웹-서버-배포">10.11 단일 웹 서버 배포</h2>
<h3 id="개요-4">개요</h3>
<ul>
<li><p>단일 웹 서버 배포는 <code>EC2 Instance</code>에서 웹 서버를 실행하는 것을 말한다.</p>
</li>
<li><p>실제 사용하는 환경에서는 <code>루비 온 레일즈(Ruby on Rails)</code>나 <code>장고(Django)</code>와 같은 <code>웹 프레임워크(서버용 프레임워크)</code>를 사용하여 웹 서버를 구축하는 것이 일반적이다.</p>
<h3 id="실습-리눅스-환경">실습 (리눅스 환경)</h3>
<h4 id="step-1-웹-서버를-위한-script-준비">Step 1. 웹 서버를 위한 Script 준비</h4>
<h4 id="개요-5">개요</h4>
</li>
<li><p><code>Hello, World!</code> 출력하는 <code>Shell Script</code>를 사용</p>
</li>
<li><p>단순 응답만을 위해서 <code>Bash Script</code>를 사용한다.</p>
<h4 id="centos에서의-terraform">CentOS에서의 Terraform</h4>
</li>
<li><p><code>1_Updated</code>로 롤백하고 <code>64GB</code> HDD를 추가한 후 <code>/terraform</code> 생성 자동마운트를 설정한다.</p>
</li>
<li><p><code>AWS CLI</code> 설치
```bash
[root@localhost terraform]# curl &quot;<a href="https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip&quot;">https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip&quot;</a> -o &quot;awscliv2.zip&quot;
[root@localhost terraform]# ls -l
합계 61740
drwxr-xr-x 3 root root     4096 12월 30 19:13 aws</p>
</li>
<li><p>rw-r--r-- 1 root root 63198381 12월 31 10:25 awscliv2.zip
drwx------ 2 root root    16384 12월 31 10:23 lost+found
[root@localhost terraform]# cd aws/
[root@localhost aws]# ls -l
합계 80</p>
</li>
<li><p>rw-r--r-- 1 root root  1465 12월 30 19:03 README.md</p>
</li>
<li><p>rw-r--r-- 1 root root 66216 12월 30 19:03 THIRD_PARTY_LICENSES
drwxr-xr-x 8 root root  4096 12월 30 19:13 dist</p>
</li>
<li><p>rwxr-xr-x 1 root root  4047 12월 30 19:03 install
[root@localhost aws]# ./install
You can now run: /usr/local/bin/aws --version
[root@localhost aws]# /usr/local/bin/aws --version
aws-cli/2.32.26 Python/3.13.11 Linux/3.10.0-1160.119.1.el7.x86_64 exe/x86_64.centos.7
[root@localhost aws]# aws configure
AWS Access Key ID [None]: access Key 입력
AWS Secret Access Key [None]: Secret Access Key 입력
Default region name [None]: ap-northeast-2
Default output format [None]:
[root@localhost aws]# HISTSIZE=1000
[root@localhost aws]# aws configure list
NAME       : VALUE                    : TYPE             : LOCATION
profile    :                 : None             : None
access_key : <strong><strong><strong>****</strong></strong></strong>634V     : shared-credentials-file :
secret_key : <strong><strong><strong>****</strong></strong></strong>T1eV     : shared-credentials-file :
region     : ap-northeast-2           : config-file      : ~/.aws/config</p>
<pre><code></code></pre></li>
<li><p><code>Terraform</code> 설치</p>
<pre><code class="language-bash">[root@localhost Terraform]# wget https://releases.hashicorp.com/terraform/1.14.3/terraform_1.14.3_linux_amd64.zip
[root@localhost Terraform]# unzip terraform_1.14.3_linux_amd64.zip
[root@localhost Terraform]# mv terraform /usr/local/bin
[root@localhost Terraform]#
[root@localhost Terraform]# terraform --version
Terraform v1.14.3
on linux_amd64</code></pre>
</li>
<li><p><code>main.tf</code> 파일 생성</p>
<pre><code class="language-bash">[root@localhost terraform]# vi main.tf
terraform {
 required_providers {
    aws = {
       source = &quot;hashicorp/aws&quot;
       version = &quot;~&gt; 4.67.0&quot;
    }
 }
required_version = &quot;&gt;= 1.4&quot;
}
</code></pre>
</li>
</ul>
<p>provider &quot;aws&quot; {
   region = &quot;ap-northeast-2&quot;
}</p>
<p>resource &quot;aws_instance&quot; &quot;app_server&quot; {
   ami = &quot;ami-0a71e3eb8b23101ed&quot;
   instance_type = &quot;t3.micro&quot;
   tags = {
      name = &quot;TerraformUserInstance&quot;
   }
}</p>
<pre><code>- `terraform init` 
- `terraform validate`
- `terraform apply` ![](https://velog.velcdn.com/images/kyk02405/post/94794bdb-d78d-49de-94d8-90c9ff8e241f/image.png)
---
#### Step 1. 웹 서버를 위한 Script 준비
- 개요
  - 'Hello, World!' 출력하는 'Shell Script'를 사용
  - 단순 응답만을 위해서 'Bash Script'를 사용한다.
  ```bash
  #!/bin/bash
  echo &quot;Hello,World!&quot; &gt; index.html
  nohup busybox httpd -f -p 8080 &amp;</code></pre><ul>
<li><code>index.html</code>에 <code>Hello, World!</code>라는 문자열을 입력, 저장하고 <code>8080</code> 포트를 <code>LISTENING</code>하고 <code>busybox 유틸리티</code> 를 <code>Backgrond Mode(&amp;)</code>에서 <code>지속적으로 실행(nohup)</code>한다.</li>
</ul>
<ul>
<li><p><code>Busybox (비지박스) 유틸리티</code></p>
<ul>
<li>(핵심) <code>GPL 라이센스</code>로 개발되고 있는, 400개 여개의 리눅스 커맨드라인 명령어들을 모아 놓은 <code>단일 실행 파일</code>을 말한다.</li>
</ul>
</li>
<li><p>포트 번호</p>
<ul>
<li><code>기본 HTTP 포트</code>인 <code>80</code>이 아닌 <code>8080</code>을 사용하는 이유는 <code>1024</code>보다 숫자가 작은 포트에서 청취하려면 <code>루트 사용자 권한</code>이 필요하기 때문이다. 따라서 더 높은 번호의 포트를 수신해야 한다. 서버를 손상시키는 공격자가 루트 권한을 가질 수 있으므로 보안 위험이 있고 루트 사용자가 아닌 권한이 제한된 다른 사용자로 웹 서버를 실행하는 것이 바람직하다. 그러나 이 장의 뒷부분에서 볼 수 있듯이 <code>80</code>으로 수신한 트래픽을 높은 번호의 포트로 라우팅하도록 <code>로드 밸런서(포트 라우팅)</code>를 구성할 수 있다.</li>
</ul>
</li>
</ul>
<hr />
<h4 id="step-2-ec2-instance를-위한-구성-파일-maintf">Step 2. EC2 Instance를 위한 구성 파일 main.tf</h4>
<pre><code class="language-bash">provider &quot;aws&quot; {
  region = &quot;us-east-2&quot;
}

resource &quot;aws_instance&quot;  &quot;ubuntu1804&quot; {
  ami = &quot;ami-0c55b159cbfafe1f0&quot;
  instance_type = &quot;t3.micro&quot;
  vpc_security_group_ids = [aws_security_group.instance.id]
  user_data = &lt;&lt;-EOF
  #!/bin/bash
  echo &quot;Hello, World&quot; &gt; index.html
  nohup busybox httpd -f -p 8080 &amp;
  EOF
  tags = {
    Name = &quot;terraform-ubuntu1804&quot;
  }
}

resource &quot;aws_security_group&quot; &quot;instance&quot; {
  name = &quot;terraform-example-instance&quot;
  ingress {
    from_port = 8080
    to_port = 8080
    protocol = &quot;tcp&quot;
    cidr_blocks = [&quot;0.0.0.0/0&quot;]
  }
}</code></pre>
<hr />
<h4 id="step-3-실행">Step 3. 실행</h4>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/382d264e-4aaa-4064-94f6-8c4e14b2d3fe/image.png" /></p>
<hr />
<h4 id="step-4-확인-1-생성된-instanc와-sg-확인-및-출력-확인">Step 4. 확인 1. 생성된 Instanc와 SG 확인 및 출력 확인</h4>
<pre><code class="language-bash">[root@localhost terraform]# curl 3.16.46.185:8080
Hello, World
[root@localhost terraform]#</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b8129659-37fe-4f28-af30-dce7738aa2df/image.png" /></p>
<hr />
<h4 id="step-5-상태-목록-확인">Step 5. 상태 목록 확인</h4>
<ul>
<li><code>main.tf</code> 구성 파일에서의 <code>resource</code>의 목록을 출력한다.</li>
<li>이 명령어는 특히 상태 파일을 수동으로 관리할 필요가 있을 때 유용하다.</li>
</ul>
<hr />
<h4 id="step-6-삭제">Step 6. 삭제</h4>
<pre><code class="language-bash">[root@localhost terraform]# terraform destroy</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/67eaaff4-96e8-4f04-a85e-470a18dd6950/image.png" /></p>
<hr />
<h2 id="1012-단일-웹-서버-배포-2-ubuntu-2404">10.12 단일 웹 서버 배포 2. Ubuntu 24.04</h2>
<h2 id="1013-응용-실습-1">10.13 응용 실습 1.</h2>
<h3 id="작업-개요">작업 개요</h3>
<h4 id="step-1-aws-management-console-ec2-amc">Step 1. AWS Management Console (ec2-amc)</h4>
<pre><code>- ‘EC2 Instance(terraform-ubuntu2404)’를 ‘키페어’와 함께 생성한다.
- 생성된 EC2 Instance에 원격접속을 한다.
- Ubuntu에서 해야 할 기본 작업들을 모두 적용한다.
- Apache 2 Web Server를 활성화 시킨 후 사이트 출력이 되는지 확인한다.
    - 'EC2 Instance' 생성 with 키페어
    - Public Key를 이용한 Priavate Key 생성
    - 접속을 위한 Putty 설정
    - 접속
        - 정상적으로 접속이 되면 계정명과 비밀번호 입력 없이 자동 로그인된다.
    - Ubuntu에서 해야 할 기본 작업들
    - 사이트 출력</code></pre><h4 id="step-2-terraformec2-tf">Step 2. Terraform(ec2-tf)</h4>
<ul>
<li>작업 개요<pre><code>  - Terraform 코드를 이용해서 Busybox Bash Script 사이트를 출력한다.</code></pre></li>
<li>main.tf 파일 생성<pre><code class="language-bash">################################
# Provider (서울 리전)
################################
provider &quot;aws&quot; {
region = &quot;ap-northeast-2&quot;
}
</code></pre>
</li>
</ul>
<p>################################</p>
<h1 id="ubuntu-2404-ami-조회-서울">Ubuntu 24.04 AMI 조회 (서울)</h1>
<p>################################
data &quot;aws_ami&quot; &quot;ubuntu&quot; {
  most_recent = true
  owners      = [&quot;099720109477&quot;] # Canonical 공식 계정</p>
<p>  filter {
    name   = &quot;name&quot;
    values = [&quot;ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*&quot;]
  }</p>
<p>  filter {
    name   = &quot;virtualization-type&quot;
    values = [&quot;hvm&quot;]
  }
}</p>
<p>################################</p>
<h1 id="security-group">Security Group</h1>
<h1 id="--ssh22">- SSH(22)</h1>
<h1 id="--busybox-web8080">- Busybox Web(8080)</h1>
<p>################################
resource &quot;aws_security_group&quot; &quot;tf_sg&quot; {
  name        = &quot;tf-sg-seoul&quot;
  description = &quot;Allow SSH and 8080 (Busybox)&quot;</p>
<p>  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = &quot;tcp&quot;
    cidr_blocks = [&quot;0.0.0.0/0&quot;] # 실습용 (내 IP로 바꿔도 됨)
  }</p>
<p>  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = &quot;tcp&quot;
    cidr_blocks = [&quot;0.0.0.0/0&quot;]
  }</p>
<p>  egress {
    from_port   = 0
    to_port     = 0
    protocol    = &quot;-1&quot;
    cidr_blocks = [&quot;0.0.0.0/0&quot;]
  }
}</p>
<p>################################</p>
<h1 id="ec2-instance-terraform-실습용">EC2 Instance (Terraform 실습용)</h1>
<p>################################
resource &quot;aws_instance&quot; &quot;tf_ec2&quot; {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = &quot;t3.micro&quot;
  key_name               = &quot;terraform-key&quot;   # 서울 리전에서 만든 키페어
  vpc_security_group_ids = [aws_security_group.tf_sg.id]</p>
<p>  user_data = &lt;&lt;-EOF
    #!/bin/bash
    apt update -y
    apt install -y busybox
    echo &quot;Hello from Terraform Busybox (Seoul)&quot; &gt; index.html
    nohup busybox httpd -f -p 8080 &amp;
  EOF</p>
<p>  tags = {
    Name = &quot;ec2-tf-seoul&quot;
  }
}</p>
<pre><code>- 명령 실행
- 사이트 출력 ![](https://velog.velcdn.com/images/kyk02405/post/2c7afd34-81ad-45bb-ab4e-d41de848f858/image.png)

#### Step 3. Redirection
- ec2-amc 사이트 출력 시 ec2-tf 사이트로 자동으로 넘어가도록 한다.
---
## 10.14 응용 실습 2.
### 작업 개요
#### Cent OS에서 DNS Server, Web Server 구축
#### Windows 10 에서 사이트 출력
- 사이트 출력 without ‘Redirection’ (CentOS의 기본 문서 출력)

- 사이트 출력 with ‘Redirection’ (AWS의 ec2-amc로 접근 후 ex2-tf로 출력) 
```bash
$TTL 1D
@       IN SOA  ns.gusiya.com.  root.gusiya.com. (
                                        0       ; serial
                                        1D      ; refresh
                                        1H      ; retry
                                        1W      ; expire
                                        3H )    ; minimum
        IN      NS      ns.gusiya.com.
        IN      A       192.168.10.128

ns      IN      A       192.168.10.128
www     IN      A       43.201.20.34
</code></pre><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/dba2086a-037f-47a3-80a0-055e985c932a/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8a842464-d6c0-47bb-bd74-7c049e058a8b/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3d9b8652-67ed-4390-9d7a-5e95c4c2331c/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/10e3a91a-e292-4cb1-85d7-c1ce1b03bb48/image.png" /></p>
<p>도메인 저렴하게 판매하는 사이트(<a href="https://domain.gabia.com/">https://domain.gabia.com/</a>)
OR
amazon route 53에서 파는 도메인 사서 aws랑 연결시킬수도있다.</p>
<hr />
<h2 id="1015-응용실습-3-aws-route53-을-이용한-도메인-출력">10.15 응용실습 3. AWS Route53 을 이용한 도메인 출력</h2>
<h3 id="도메인-등록-종류">도메인 등록 종류</h3>
<ul>
<li>(추천) 'AWS'에서 도메인 구매 및 등록 후 'Ropute53'에서 서비스를 한 경우<ul>
<li>네임서버 설정이 매우 쉽다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/aec922d5-fc81-442a-b257-e1572a1f38b6/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/72f4654b-ad2d-40ea-b32f-0b8950ae4d7a/image.png" /></li>
</ul>
</li>
</ul>
<p>(기존에 가지고 있는 호스트 아이디가 있다, 옮길 때 (예를 들어 naver.com 기존 주소)) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d0687354-81f8-47a9-9b56-5a7c393960e6/image.png" /></p>
<p>(기존의 주소를 라우트 53과 연결할 때) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9c2bb00d-70ba-45c4-8802-4a3ec24bab41/image.png" /></p>
<ul>
<li>'Web Hosting'업체에서 도메인을 등록한 경우<ul>
<li>네임서버 설정이 매우 어렵다.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="1017-구성-가능한-웹-서버-배포변수">10.17 구성 가능한 웹 서버 배포(변수)</h2>
<h3 id="변수variable">변수(Variable)</h3>
<h4 id="특징">특징</h4>
<ul>
<li>변수 선언의 본문에는 '3개의 매개 변수'가 포함될 수 있고 나머지는 모두 '선택적 매개 변수'이다.</li>
<li>변수 선언의 본문에는 '3개의 매개 변수'가 포함될 수 있고 나머지는 모두 '선택적 매개 변수'이다.<h4 id="변수-선언">변수 선언</h4>
<pre><code class="language-bash">variable = &quot;NAME&quot; {
      [CONFIG ...]
}</code></pre>
</li>
</ul>
<hr />
<h3 id="3개의-매개-변수-사용-및-전달-방법">3개의 매개 변수 사용 및 전달 방법</h3>
<h4 id="description-변수의-문서화">description (변수의 문서화)</h4>
<ul>
<li><code>변수 사용 방법을 문서화</code>하려면 이 매개변수를 사용한다.</li>
<li>즉, 어떤 변수가 어떤 가지고 어디에 적용되는지 등을 설명을 통해 알아볼 수 있도록 한다.</li>
<li>만약 팀별로 프로젝트를 한다고 가정하면 팀원은 코드를 읽을 때문만 아니라 <code>plan</code> 또는 <code>apply</code> 등의 명령어를 실행할 때 이 설명을 볼 수가 있다.</li>
</ul>
<h4 id="type-변수">type (변수)</h4>
<ul>
<li><code>Type Constraint (유형 제약 조건)</code>으로 <code>사용자가 전달하는 변수의 유형을 지정</code> 할 수 있는 변수이다.</li>
<li><code>Terraform</code>에는 <code>string(문자열),</code> <code>number(숫자)</code>, <code>bool(대수, true, false)</code>, <code>list(리스트)</code>, <code>map(맵)</code>, <code>set(집합)</code>, <code>object(객체)</code>, <code>tuple(튜플)</code> 등의 제약 조건이 있다.</li>
<li>유형을 지정하지 않으면 <code>Terraform</code>은 <code>any</code>로 간주한다.</li>
</ul>
<h4 id="default-값">default (값)</h4>
<ul>
<li><p><code>변수에 값을 전달하는 방법으로 사용</code>되는 변수이다.</p>
</li>
<li><p>전달 방법</p>
<ul>
<li><code>명령 줄(--var 옵션 사용)</code>로 전달한다.</li>
<li><code>파일(-var~file 옵션 사용)</code>로 전달한다.</li>
<li><code>환경변수(</code>Terraform<code>은 이름이</code>TF_VAR_<code>인 환경변수를 찾는다)</code>를 변수에 값을 전달힌다.</li>
</ul>
</li>
<li><p>만약 값의 전달 유무에 따른 진행</p>
<ul>
<li>값이 전달되지 않으면 <code>기본값</code>이 전달된다.</li>
<li>기본값이 없으면 <code>Terraform</code>은 대화식으로 사용자에게 변수에 대한 정보를 묻는다.</li>
</ul>
</li>
</ul>