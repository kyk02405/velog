# Cloud DX - 61 Terraform (2)

- 📅 Published: Wed, 31 Dec 2025 08:46:15 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-61-Terraform-2)

<hr />
<h2 id="1011-단일-웹-서버-배포">10.11 단일 웹 서버 배포</h2>
<h3 id="개요">개요</h3>
<ul>
<li><p>단일 웹 서버 배포는 <code>EC2 Instance</code>에서 웹 서버를 실행하는 것을 말한다.</p>
</li>
<li><p>실제 사용하는 환경에서는 <code>루비 온 레일즈(Ruby on Rails)</code>나 <code>장고(Django)</code>와 같은 <code>웹 프레임워크(서버용 프레임워크)</code>를 사용하여 웹 서버를 구축하는 것이 일반적이다.</p>
<h3 id="실습-리눅스-환경">실습 (리눅스 환경)</h3>
<h4 id="step-1-웹-서버를-위한-script-준비">Step 1. 웹 서버를 위한 Script 준비</h4>
<h4 id="개요-1">개요</h4>
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
<hr />
<blockquote>
<h3 id="변수-사용-예">변수 사용 예</h3>
</blockquote>
<ul>
<li>코드에 기입할 때는 반드시 <code>겹따옴표(&quot; ~ &quot;)</code>로 값을 입력해야 한다. description = &quot;우측에는 반드시 문자열로 기입해야 한다.&quot;<h4 id="전달-값이-number숫자인지-먼저-확인">전달 값이 number(숫자)인지 먼저 확인</h4>
<pre><code class="language-bash">variable &quot;number_example&quot; {
      description = &quot;An example of a number variable in Terraform&quot;
      type = number
      default = 42
}</code></pre>
<h4 id="전달-값이-list리스트인지-먼저-확인">전달 값이 list(리스트)인지 먼저 확인</h4>
<pre><code class="language-bash">variable &quot;number_example&quot; {
      description = &quot;An example of a number variable in Terraform&quot;
      type = list(number)
      default = [1, 2, 3]
}</code></pre>
</li>
<li>제약조건도 결합해서 사용할 수 있다.<h4 id="모든-값이-string문자열인-map">모든 값이 string(문자열)인 map</h4>
<pre><code class="language-bash">variable &quot;number_example&quot; {
      description = &quot;An example of a number variable in Terraform&quot;
      type = map(string)
      default = {
          key1 = &quot;value1&quot;
          key2 = &quot;value2&quot;
          key3 = &quot;value3&quot;
      }
}</code></pre>
<h3 id="map은-python에서의-dirctionary와-동일한-기능을-한다"><code>map</code>은 <code>Python</code>에서의 <code>Dirctionary</code>와 동일한 기능을 한다.</h3>
<code>map</code> → <code>키(key) = 값(value)</code>
<code>dictionary</code> → <code>{키(key):값(value)}</code></li>
</ul>
<hr />
<h3 id="실습-1-object객체-또는-tuple-제약-조건의-구조적-형태로-작성">실습 1. Object(객체) 또는 Tuple 제약 조건의 구조적 형태로 작성</h3>
<h4 id="소스코드-작성">소스코드 작성</h4>
<pre><code class="language-bash">variable &quot;number_example&quot; {
        description = &quot;An example of a number variable in Terraform&quot;
        type = map(string)
        default = {
            key1 = &quot;value1&quot;
            key2 = &quot;value2&quot;
            key3 = &quot;value3&quot;
        }
}
variable &quot;number_example&quot; {
        description = &quot;An example of a number variable in Terraform&quot;
        type = number
        default = 42
}</code></pre>
<h4 id="실행-1-오류가-발생하지-않는다">실행 1. 오류가 발생하지 않는다.</h4>
<h4 id="결과확인">결과확인</h4>
<ul>
<li>소스에 오류가 없기 때문에 즉, 이 소스는 변수에 대한 설정만 되어 있고 클릭에 대한 내용은 없기 때문에 아무런 내용도 출력되지 않는다.<h4 id="수정">수정</h4>
</li>
<li>변수를 선언했을 때는 값도 반드시 있어야 한다. </li>
</ul>