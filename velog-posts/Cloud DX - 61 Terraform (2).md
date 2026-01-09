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
<li>변수를 선언했을 때는 값도 반드시 있어야 한다. 
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9933ef5f-d278-48aa-bd31-9b1e85e7ac81/image.png" /></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e45a60d0-8fb9-4651-927f-0915fd048556/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/433f98a2-0544-4e8f-9e47-97be84d2034f/image.png" /></p>
<hr />
<h3 id="실습-2-enable에-문자열을-설정하면-오류가-발생한다-즉-boolean은-참true-1과-거짓false-0만을-구분하고-입력할-때는-이중-따옴표를-삽입하지-않아도-된다된다">실습 2. ‘enable’에 문자열을 설정하면 오류가 발생한다. 즉, ‘Boolean’은 ‘참(true, 1)’과 ‘거짓(false, 0)’만을 구분하고 입력할 때는 ‘이중 따옴표’를 삽입하지 않아도 된다된다.</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/990ae633-d306-4fb9-af6e-a59465912bfc/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/97d45dff-eb80-4352-aebe-ea567c4d6521/image.png" /></p>
<hr />
<h3 id="실습-3-기본-값이-없으면-사용자에게-변수에-대한-정보값를-묻는다">실습 3. ‘기본 값이 없으면’ 사용자에게 변수에 대한 ‘정보(값)’를 묻는다.</h3>
<ul>
<li>실행 시 ‘Enter a value:’가 출력되고 해당 값(Port)을 입력
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e0c4d4e5-97bd-4247-9582-5defe71f8676/image.png" /></li>
</ul>
<hr />
<h3 id="실습-4-대화식으로-명령어를-처리하지-않으려면-명령-줄의--var-옵션으로-변수값을-제공할-수-있다">실습 4. 대화식으로 명령어를 처리하지 않으려면 명령 줄의 ‘-var’ 옵션으로 변수값을 제공할 수 있다.</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/acbfcddc-ed1d-4486-9009-fdd62648e917/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/06475342-c431-4093-97af-c4ddfc107a2b/image.png" /></p>
<hr />
<h3 id="실습-5-환경-변수">실습 5. 환경 변수</h3>
<h4 id="개요-2">개요</h4>
<ul>
<li><code>TF_VAR_&lt;name&gt;</code>이라는 <code>환경 변수</code>를 통해서 변수를 설정할 수도 있다.</li>
<li><code>&lt;name&gt;</code>는 설정하려는 환경 변수 등록할 때 <code>export</code> 사용
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5c123943-fa72-4f1b-92b0-6c6c22afd5ac/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a823929c-f5cc-44e8-b9e3-6990a3ed35e2/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e2a49dab-f0b4-4445-8c42-1987b2567db1/image.png" /></li>
<li>명령 실행 시 <code>포트 번호</code>를 물어보지도 않고 정상적으로 실행 된다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5ab2c5d1-f1bd-4298-b3e4-1999aec20c7d/image.png" /></li>
</ul>
<hr />
<h3 id="실습-6-default-값을-지정해두면-plan이나-apply-명령어를-실행할-때마다-명령-줄-인수를-일일이-기억해서-처리하지-않아도-된다">실습 6. 'default 값'을 지정해두면 'plan'이나 'apply' 명령어를 실행할 때마다 명령 줄 인수를 일일이 기억해서 처리하지 않아도 된다.</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/defd891e-0bc9-41c1-9b62-550fb48b98c7/image.png" /></p>
<hr />
<h3 id="실습-7-변수-참조variable-reference">실습 7. 변수 참조(Variable Reference)</h3>
<h4 id="개요-3">개요</h4>
<ul>
<li><code>Terraform Code</code>에서 <code>입력 변수의 값</code>을 사용하려면 <code>변수 참조(Variable Reference)</code>라는 새로운 유형의 표현식을 사용한다.</li>
<li>이 소스는 <code>보안 그룹</code>의 <code>from_port</code> 및 <code>to_port</code>라는 매개 변수를 <code>server_port</code>라는 변수의 값으로 설정하는 방법을 표현한 것이다.
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/aa01d216-79b8-4c5b-975b-fbff9c8a11db/image.png" /></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7deaa4ac-9e71-406a-8858-f1eef26a91db/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/11cce57a-8a22-4591-ad59-2e9825c91475/image.png" /></p>
<p>주의 사항
→ AWS관리 콘솔에서 확인해야 한다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e63ba09f-f535-441b-8741-6d46b90780fd/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5843d149-2da4-41b9-8d2c-7c3bc6a09e82/image.png" /></p>
<h4 id="내용-1-사용자-데이터-스크립트에서-포트를-설정할-때도-동일한-변수를-사용하는-것이-좋다">내용 1. 사용자 데이터 스크립트에서 포트를 설정할 때도 동일한 변수를 사용하는 것이 좋다.</h4>
<ul>
<li><p>개요
→ 문자열 Literal(리터럴, 변수에 넣은 값이 변하지 않는 데이터, <code>상수(Constant)</code>와 유사) 내에서 참조를 사용하려면 <code>보간</code>이라는 새로운 유형의 표현식을 사용해야 한다.</p>
</li>
<li><p><code>보간</code>은 주어진 값을 특정 기준을 적용해서 새로운 값으로 지정하는 것을 말한다.</p>
</li>
<li><p><code>PHP</code>에서 변수를 표현하는 방법과 유사하다.</p>
</li>
<li><p><code>중괄호({. . .})</code>안에 참조를 넣을 수 있으며 <code>Terraform</code>은 이를 <code>문자열로 변환</code>한다.</p>
</li>
<li><p>표현식</p>
</li>
</ul>
<pre><code class="language-bash">“${. . .}”</code></pre>
<ul>
<li>예시</li>
</ul>
<pre><code class="language-bash">user_date = &lt;&lt;-EOF
    # !/bin/bash
    echo “Hello, World!” &gt; index.html
    nohup busybox httpd -f -p ${var.server_port} &amp;
    EOF</code></pre>
<h4 id="내용-2-terraform에서는-입력-변수-뿐만-아니라-출력-변수도-정의할-수-있다">내용 2. <code>Terraform</code>에서는 <code>입력 변수</code> 뿐만 아니라 <code>출력 변수</code>도 정의할 수 있다.</h4>
<ul>
<li><p><code>NAME</code>은 출력 변수의 이름이며 <code>VALUE</code>는 출력하려는 <code>Terraform</code> 표현식일 수 있다.</p>
</li>
<li><p>예시</p>
<pre><code class="language-bash">    output &quot;&lt;NAME&gt;&quot; {\
       value = &lt;VALUE&gt;
       [CONFIG ...]
    }</code></pre>
</li>
<li><p><code>CONFIG</code>는 다음의 2가지 선택적 매개 변수를 추가로 포함할 수 있다.</p>
</li>
<li><p><code>description</code></p>
<ul>
<li>출력 변수에 어떤 유형의 데이터가 포함되어 있는지를 알려준다.</li>
</ul>
</li>
<li><p><code>sensitive</code></p>
<ul>
<li><code>terraform apply</code>의 실행이 끝날 때 출력을 기록하지 않도록 <code>Terraform</code>에 지시하려면
<code>sensitive</code> 매개 변수를 <code>true</code>로 설정한다.</li>
<li>(핵심) 이는 <code>출력 변수</code>에 패스워드나 개인 키와 민감한 자료 또는 <code>시크릿(secret)</code>이 포함되어 있는 경우 유용하다.</li>
</ul>
</li>
</ul>
<h4 id="내용-3-새로운-결과-값-출력">내용 3. 새로운 결과 값 출력</h4>
<ul>
<li><code>apply 명령어</code>를 다시 실행하면 <code>Terraform</code>은 변경 사항을 적용하지는 않지만(리소스를 변경하지 않았기 때문에) 맨 끝에 새로운 결과값을 출력한다.</li>
<li><code>terraform apply</code> 명령어를 실행하면 <code>콘솔(터미널 창)</code>에 출력 변수가 표시되는데 이 변수에는 <code>Terraform</code> 코드 사용자에게 유용한 정보가 포함되어 있다.</li>
</ul>
<hr />
<h2 id="1018-실습">10.18 실습</h2>
<h3 id="실습-1-vpc-배포">실습 1. VPC 배포</h3>
<h4 id="개요-4">개요</h4>
<ul>
<li>실제 운영 환경에서 서버가 하나 뿐인 경우는 거의 없다.</li>
<li>단일 장애점을 피하기 위해 단일 서버가 아닌 서버 클러스터를 구성하여 트래픽을 분산시키고, 트래픽 양에 따라 클러스터 크기를 늘리거나 줄여야 한다.</li>
<li>AWS에서는 오토스케일링 그룹(Auto Scaling Group, ASG)를 사용하면 EC2 인스턴스 클러스터 시작, 각 인스턴스 상태 모니터링, 실패한 인스턴스 교체, 로드에 따른 클러스터 사이즈 조정 등 많은 작업을 자동으로 처리할 수 있다.</li>
<li>여기서는 사용되는 리눅스는 'Amazon Linux'이다.<h4 id="작업-개요-1">작업 개요</h4>
</li>
<li>Terraform 구성 파일을 사용해서 ‘ASG’ 뿐만 아니라 사용자 VPC, 보안그룹(SG), EC2 Instance, ELB를 배포하는 과정을 진행한다.</li>
</ul>
<h4 id="step-1-vpc-생성">Step 1. ‘VPC’ 생성</h4>
<ul>
<li>코딩(main.tf) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7bb1e79a-fd79-47b7-905e-8470e098dd1a/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b2c2ea93-d381-4a48-8e55-867072012ee8/image.png" /></li>
<li>실행
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2a5a5d50-985d-491a-9a01-af1671da7ea8/image.png" /></li>
<li>확인</li>
</ul>