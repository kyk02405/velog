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
<li><code>Terraform</code>의 <code>HCL</code>을 이용해서 <code>AWS</code>의 <code>EC2</code> <code>Instance</code>를 구성하는 예제<pre><code class="language-bash">resource &quot;aws_instance&quot; &quot;web&quot; {
ami           = &quot;ami-0abc123&quot;
instance_type = &quot;t3.micro&quot;
}</code></pre>
</li>
</ul>