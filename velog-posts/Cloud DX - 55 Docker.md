# Cloud DX - 55 Docker

- 📅 Published: Thu, 04 Dec 2025 08:20:46 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-55-Docker)

<h1 id="6-🐳-span-style--colorskybluedocker-span">6. 🐳 <span style="color: skyblue;">Docker </span></h1>
<h2 id="1-docker-이미지는-패키징된-실행-환경">1. Docker 이미지는 패키징된 실행 환경</h2>
<ul>
<li>Docker에서 사용되는 모든 애플리케이션은 <strong>이미지(Image)</strong> 형태로 제공된다.</li>
<li>이미지는 애플리케이션 실행에 필요한 <strong>코드, 라이브러리, 설정 파일, 실행 명령</strong> 등이 포함된 패키지다.</li>
</ul>
<hr />
<h2 id="2-이미지는-생성·공유·배포가-가능">2. 이미지는 생성·공유·배포가 가능</h2>
<ul>
<li>사용자가 직접 만든 이미지도 Docker Hub 등 저장소를 통해 <strong>다른 사용자와 공유</strong>하거나
<strong>배포 서버(Kubernetes 등)</strong> 에 올려 운영 환경에서 실행할 수 있다.</li>
<li>즉, 이미지 하나로 개발/테스트/운영 환경을 완전히 동일하게 유지할 수 있다.</li>
</ul>
<hr />
<h2 id="3-host-os-위에서-컨테이너를-실행하는-구조">3. Host OS 위에서 컨테이너를 실행하는 구조</h2>
<ul>
<li>Host OS(예: Linux, Windows, macOS) 위에 <strong>Docker Engine(컨테이너 관리 소프트웨어)</strong> 를 설치한다.</li>
<li>Docker Engine이 이미지를 기반으로 <strong>컨테이너(Container)</strong> 를 생성하고 관리한다.</li>
<li>VM처럼 OS 전체를 올리는 것이 아니라, <strong>Host OS의 커널을 공유하는 방식</strong>으로 동작한다.</li>
</ul>
<hr />
<h2 id="4-docker-컨테이너는-최소-구성cli-중심">4. Docker 컨테이너는 최소 구성(CLI 중심)</h2>
<ul>
<li><p>Docker 이미지 대부분은 <strong>CLI 기반의 가벼운 OS 구조</strong>를 사용한다.
(예: Ubuntu-base, Alpine Linux 등)</p>
</li>
<li><p>이유:</p>
<ul>
<li>그래픽 환경(GUI)은 불필요한 리소스 낭비</li>
<li>서버 운영은 대부분 CLI로 충분</li>
<li>컨테이너는 “필요한 것만 넣는” 최소 환경을 지향</li>
</ul>
</li>
</ul>
<hr />
<h2 id="5-필요한-패키지는-관리자가-직접-구성">5. 필요한 패키지는 관리자가 직접 구성</h2>
<ul>
<li><p>컨테이너는 기본적으로 <strong>필수 구성요소만 포함</strong>되어 있다.</p>
</li>
<li><p>예:</p>
<ul>
<li><code>python</code> 이미지 → 파이썬만 있음</li>
<li><code>nginx</code> 이미지 → nginx만 있음</li>
<li><code>alpine</code> → 거의 빈 Linux 환경</li>
</ul>
</li>
<li><p>추가 라이브러리, 설정, 네트워크 구성 등은
<strong>관리자가 직접 Dockerfile을 통해 설치 및 설정</strong>해야 한다.</p>
</li>
</ul>
<hr />
<h3 id="📌-전체-요약">📌 전체 요약</h3>
<table>
<thead>
<tr>
<th>특징</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>이미지 기반 구조</td>
<td>실행 환경을 이미지로 패키징</td>
</tr>
<tr>
<td>공유 가능</td>
<td>직접 만든 이미지를 배포/공유 가능</td>
</tr>
<tr>
<td>Host OS 위에서 동작</td>
<td>Docker Engine이 컨테이너를 실행</td>
</tr>
<tr>
<td>최소 구성</td>
<td>CLI 기반의 가벼운 OS 사용</td>
</tr>
<tr>
<td>직접 설치 필요</td>
<td>필요한 패키지는 사용자가 구성</td>
</tr>
</tbody></table>
<hr />
<h2 id="61--컨테이너-인프라-환경-cic-container-infrastructure-configuration">6.1  컨테이너 인프라 환경 (CIC, Container Infrastructure Configuration)</h2>
<h3 id="개요">개요</h3>
<ul>
<li>컨테이너를 중심으로 구성된 인프라 환경을 말한다.</li>
<li><code>컨테이너(Container)</code>는 하나의 운영체제 커널에서 다른 프로세스에 영향을 받지 않고 '(핵심) 독립적으로 실행되는 프로세스 상태'를 말한다.</li>
</ul>
<hr />
<h2 id="🚀-cicd-지원-도구-정리">🚀 CICD 지원 도구 정리</h2>
<h2 id="1️⃣-docker도커--컨테이너-생성·실행-도구">1️⃣ <strong>Docker(도커)</strong> — <em>컨테이너 생성·실행 도구</em></h2>
<h3 id="✔-핵심-개념">✔ 핵심 개념</h3>
<blockquote>
<p>&quot;애플리케이션을 어떤 환경에서도 동일하게 실행할 수 있게 해주는 기술&quot;</p>
</blockquote>
<ul>
<li>앱이 실행되는 데 필요한 <strong>모든 환경(라이브러리, 설정)</strong> 을 하나의 컨테이너로 묶어줌</li>
<li>컨테이너는 <strong>OS 영향을 거의 받지 않아서</strong> 어디서 실행해도 결과가 동일함
→ 개발 → 테스트 → 운영 환경 불일치 문제 해결</li>
</ul>
<h3 id="✔-예시">✔ 예시</h3>
<p>“MySQL 8.0 설치해야 한다 → 서버마다 설치하지 않고 Docker로 컨테이너 하나 띄우면 끝”</p>
<hr />
<h2 id="2️⃣-kubernetes쿠버네티스--컨테이너-자동-관리-시스템">2️⃣ <strong>Kubernetes(쿠버네티스)</strong> — <em>컨테이너 자동 관리 시스템</em></h2>
<h3 id="✔-핵심-개념-1">✔ 핵심 개념</h3>
<blockquote>
<p>“수백~수천 개의 컨테이너를 자동으로 배포·확장·복구해주는 오케스트레이션 플랫폼”</p>
</blockquote>
<p>도커가 컨테이너 “하나” 실행용이라면,
쿠버네티스는 컨테이너 “수천 개”를 운영하는 자동화 시스템.</p>
<h3 id="✔-제공-기능">✔ 제공 기능</h3>
<ul>
<li>자동 배포 (Rolling Update)</li>
<li>자동 복구 (Self-Healing)</li>
<li>자동 확장 (Auto Scaling)</li>
<li>부하 분산 (Load Balancing)</li>
<li>서비스 디스커버리</li>
</ul>
<h3 id="✔-예시-1">✔ 예시</h3>
<p>“웹 서버 컨테이너 10개가 운영되는데 2개가 죽음 →
쿠버네티스가 자동으로 다시 2개 생성”</p>
<hr />
<h2 id="3️⃣-jenkins젠킨스--cicd-자동화-도구">3️⃣ <strong>Jenkins(젠킨스)</strong> — <em>CI/CD 자동화 도구</em></h2>
<h3 id="✔-핵심-개념-2">✔ 핵심 개념</h3>
<blockquote>
<p>“코드 빌드 → 테스트 → 패키징 → 배포 과정을 자동화해주는 서버”</p>
</blockquote>
<ul>
<li><p>개발자가 코드를 push하면</p>
<ul>
<li>자동 빌드</li>
<li>자동 테스트</li>
<li>이미지 생성(Docker)</li>
<li>자동 배포(Kubernetes)</li>
</ul>
</li>
</ul>
<p>이런 일련의 과정을 <strong>스스로 수행</strong>함.</p>
<p>즉, 사람이 수동으로 하던 반복 작업을 완전 자동화하여
<strong>개발 속도 상승 + 실수 감소</strong> 효과를 줌.</p>
<h3 id="✔-왜-컨테이너-환경에서-더-중요">✔ 왜 컨테이너 환경에서 더 중요?</h3>
<p>컨테이너는 빠르게 배포해야 의미 있음 → Jenkins가 자동화해줌.</p>
<hr />
<h2 id="4️⃣-prometheus--grafana--모니터링--시각화">4️⃣ <strong>Prometheus + Grafana</strong> — <em>모니터링 + 시각화</em></h2>
<h3 id="✔-prometheus">✔ Prometheus</h3>
<blockquote>
<p>“컨테이너, 서버, 애플리케이션의 상태 데이터를 수집하는 모니터링 도구”</p>
</blockquote>
<p>수집하는 예:</p>
<ul>
<li>CPU 사용량</li>
<li>메모리 사용량</li>
<li>컨테이너 수</li>
<li>에러 발생량</li>
<li>HTTP 요청 수</li>
</ul>
<p>쿠버네티스 환경에서 <strong>표준 모니터링 도구</strong>로 쓰임.</p>
<hr />
<h3 id="✔-grafana">✔ Grafana</h3>
<blockquote>
<p>“Prometheus로 수집한 데이터를 사람이 보기에 이해 쉬운 그래프·대시보드로 시각화하는 도구”</p>
</blockquote>
<ul>
<li>관리자용 대시보드 생성</li>
<li>오류/장애 상황을 한눈에 확인 가능</li>
</ul>
<hr />
<h3 id="📌-네-줄로-전체-요약">📌 네 줄로 전체 요약</h3>
<table>
<thead>
<tr>
<th>도구</th>
<th>역할</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Docker</strong></td>
<td>컨테이너를 만들고 실행하는 기술</td>
</tr>
<tr>
<td><strong>Kubernetes</strong></td>
<td>많은 컨테이너를 자동으로 운영·관리하는 시스템</td>
</tr>
<tr>
<td><strong>Jenkins</strong></td>
<td>빌드/테스트/배포 전체 과정을 자동화하는 CI/CD 서버</td>
</tr>
<tr>
<td><strong>Prometheus + Grafana</strong></td>
<td>모니터링(수집) + 시각화 대시보드</td>
</tr>
</tbody></table>
<hr />
<h2 id="62-설치">6.2 설치</h2>
<h3 id="621-docker-engine-설치를-위한-guest-os-설치">6.2.1 Docker Engine 설치를 위한 Guest OS 설치</h3>
<ul>
<li><p>신경 써야 할 내용</p>
</li>
<li><p><code>Ubuntu</code> 설치</p>
<ul>
<li><p>환경 설정 및 설치</p>
<pre><code class="language-bash">sudo apt update
sudo apt upgrade
sudo apt auto-remove
sudo ufw allow 22/tcp
sudo ufw reload</code></pre>
</li>
<li><p>설치 후 해야 할 기본 작업</p>
</li>
<li><p>네트워크 설정</p>
<ul>
<li><code>192.168.10.128</code></li>
</ul>
</li>
<li><p>원격 접속</p>
</li>
</ul>
</li>
<li><p><code>Docker Engine</code> 설치</p>
<ul>
<li><p><code>Docker</code> 설치를 위한 관련 패키지 설치</p>
<pre><code class="language-bash">sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -</code></pre>
</li>
<li><p><code>Docker</code>의 <code>공식 apt 저장소</code> 추가</p>
<pre><code class="language-bash">sudo add-apt-repository &quot;deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable&quot;</code></pre>
</li>
<li><p>시스템 패키지 업데이트</p>
<pre><code class="language-bash">sudo apt update
sudo apt upgrdae</code></pre>
</li>
<li><p>설치 및 확인</p>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo apt install docker-ce docker-ce-cli containerd.io
samadal@CloudDX:~$ sudo docker -v
Docker version 29.1.2, build 890dcca
samadal@CloudDX:~$ sudo ps -ef | grep docker
...
samadal@CloudDX:~$ sudo systemctl status docker
...
</code></pre>
</li>
</ul>
<pre><code>- `Docker Engine` 버전 확인
```bash
samadal@CloudDX:~$ sudo docker version
Client: Docker Engine - Community
...
Server: Docker Engine - Community
...</code></pre></li>
<li><p>테스트</p>
<ul>
<li><code>Docker</code> 이미지를 이용해서 컨테이너를 생성<pre><code class="language-bash">samadal@CloudDX:~$ sudo docker run hello-world
</code></pre>
</li>
</ul>
<p>samadal@CloudDX:~$ sudo docker images           </p>
<pre><code>![](https://velog.velcdn.com/images/kyk02405/post/ed1fb33e-8e71-45dd-a6e9-0b436b745b0f/image.png)
![](https://velog.velcdn.com/images/kyk02405/post/940ea429-2c3e-4dfa-89dc-f69d6f62941d/image.png)
</code></pre></li>
</ul>
<hr />
<h2 id="63-명령어">6.3 명령어</h2>
<h2 id="631-image-관련-명령어">6.3.1 Image 관련 명령어</h2>
<hr />
<h3 id="search">Search</h3>
<ul>
<li><p>개요</p>
<ul>
<li><code>Docker Hub</code>에서 이미지를 검색한다.</li>
</ul>
</li>
<li><p>문법</p>
<pre><code class="language-bash">docker search &lt;이미지명&gt;[:태그]</code></pre>
</li>
<li><p>실습 </p>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo docker search centos</code></pre>
<ul>
<li><p><code>CentOS</code> 관련 모든 이미지를 검색하고 출력</p>
</li>
<li><p>검색 1. 공식 이미지 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ed43f826-02d2-4981-91ce-ec22ca4bcf4e/image.png" /></p>
<pre><code class="language-bash">docker search centos</code></pre>
<ul>
<li>공식이미지는 <code>centos</code> 뒤에 아무것도 안써있음, <code>OFFICAIL</code> = <code>OK</code></li>
</ul>
</li>
<li><p>검색 2. <code>CentOS</code>의 버전이 <code>7</code>인 이미지를 검색 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c32ae4fa-4dd4-4566-b1e2-ea987a70227d/image.png" /></p>
<pre><code class="language-bash">docker search centos:7</code></pre>
</li>
<li><p>검색 3. <code>CentOS</code>의 마지막 버전의 이미지를 검색 with 태그 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8b46727f-5699-446d-ba69-72ff1dcb321c/image.png" /></p>
<pre><code class="language-bash">docker search centos:lastest</code></pre>
</li>
<li><p>검색 4. <code>Ubuntu</code>의 마지막 버전이 <code>24.04</code>인 이미지를 검색 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/81d335bf-2c02-4f71-87f0-8526c671c409/image.png" /></p>
<pre><code class="language-bash">docker search ubuntu:24.04</code></pre>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="images"><code>images</code></h3>
<ul>
<li>개요<ul>
<li>현재 다운로드한 이미지의 목록을 확인</li>
<li>필요할 때마다 한 개씩 불러와서 사용</li>
</ul>
</li>
<li>문법<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/15a28a23-4d91-489d-9dc7-d650fc684477/image.png" /></li>
</ul>
<pre><code class="language-bash">docker images</code></pre>
<hr />
<h3 id="pull">pull</h3>
<ul>
<li><p>개요</p>
<ul>
<li>도커 이미지를 다운로드</li>
</ul>
</li>
<li><p>문법</p>
<pre><code class="language-bash">docker pull &lt;이미지명&gt;[:태그]</code></pre>
</li>
<li><p>실습 </p>
<ul>
<li><p>버전을 지정해서 다운로드 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2eda8c06-2328-4d0f-bf4f-bcde5ab50ee7/image.png" /></p>
<pre><code class="language-bash">docker pull centos:7</code></pre>
</li>
<li><p>확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/828a328c-31d9-45b9-95ec-124cc5c26383/image.png" /></p>
</li>
<li><p>최정 버전을 지정해서 다운로드 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7389fb17-7e71-4f68-9648-9be8917528df/image.png" /></p>
<pre><code class="language-bash">docker pull centos:lastest</code></pre>
</li>
<li><p>(참고) 컨테이너 목록등을 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/04ea1112-1ab5-432b-9205-c85266d90bb9/image.png" /></p>
<pre><code class="language-bash">docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
df -h</code></pre>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="rmi">rmi</h3>
<ul>
<li>개요<ul>
<li>도커 이미지를 삭제</li>
<li>태그가 있는 상태로 다운로드 했다면 이미지를 태그와 함께 삭제</li>
<li>해당 이미지를 이용해서 생성된 컨테이너가 활성 또는 비활성 상태일 때는 삭제가 안되기 때문에 관련 컨테이너를 목록에서 제거</li>
</ul>
</li>
<li>문법<pre><code class="language-bash">docker rmi</code></pre>
</li>
<li>실습 <ul>
<li>이미지 삭제<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b125882d-0f7f-4ec8-aa9d-929c38e5a09a/image.png" /><pre><code class="language-bash">docker rmi centos:7
docker rmi ubuntu:24.04</code></pre>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="632-container-관련-명령어">6.3.2 Container 관련 명령어</h2>
<h3 id="run">run</h3>
<ul>
<li><p>개요 </p>
<ul>
<li>도커 이미지를 이용해서 컨테이너 생성</li>
<li>(특징) 기본적으로 컨테이너 생성과 동시에 컨테이너 안에 접속</li>
</ul>
</li>
<li><p>문법</p>
<pre><code class="language-bash">docker run &lt;옵션1&gt;&lt;서브옵션1&gt; ... --name &lt;컨테이너명&gt; &lt;이미지명&gt;[:태그] &lt;명령어&gt;</code></pre>
<ul>
<li>옵션
```bash</li>
<li>i (Interactive, 직접 타이핑해서 사용)</li>
<li>t (가상 터미널, Pseudo-tty)</li>
<li><ul>
<li>name (컨테이너 이름)
centos:7 (이미지명과 태그)
/bin/bash (일반적으로 Shell을 지정)
```</li>
</ul>
</li>
</ul>
</li>
<li><p>실습</p>
<ul>
<li>도커 이미지를 다운로드 및 확인<pre><code class="language-bash">docker pull centos:7</code></pre>
</li>
<li>이미지로 컨테이너 생성 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/935f816c-0656-44a7-a6fa-5831ae5cfd18/image.png" /></li>
</ul>
<pre><code class="language-bash">docker run -i -t --name samadal centos:7 /bin/bash</code></pre>
</li>
</ul>
<hr />
<h3 id="ps">ps</h3>
<ul>
<li>개요<ul>
<li>활성 또는 비활성 상태의 컨테이너를 모두 출력</li>
<li><code>옵션(a)</code> 사용 유무<ul>
<li>사용 (도커 컨테이너 <code>전체 목록(활성 및 비활성)</code>을 출력)</li>
<li>미사용 (도커 컨테이너 <code>활성 상태(동작중인)</code>목록을 출력)</li>
</ul>
</li>
</ul>
</li>
<li>문법<pre><code class="language-bash">docker ps -a
docker ps</code></pre>
</li>
<li>실습 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5aacc68f-695a-406a-baa5-29dcb8873d81/image.png" /></li>
</ul>
<hr />
<h3 id="create">create</h3>
<ul>
<li>개요<ul>
<li><code>run</code>과 달리 컨테이너만 생성</li>
</ul>
</li>
<li>문법<ul>
<li><code>run</code> 명령 실행 시 내용은 같고 <code>run</code> 대신 <code>create</code>만 사용하면 된다.</li>
</ul>
</li>
<li>실습 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e9eaaf67-8560-4127-bf0f-30ea72187235/image.png" /></li>
</ul>
<pre><code class="language-bash">docker create -it --name madal centos:7 /bin/bash</code></pre>
<hr />
<h3 id="rm">rm</h3>
<ul>
<li>개요<ul>
<li>컨테이너를 삭제</li>
</ul>
</li>
<li>문법<pre><code class="language-bash">docker rm &lt;CONTAINER ID&gt;
docker rm &lt;NAMES&gt;</code></pre>
</li>
<li>실습 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bfe93f84-83da-4387-bcb4-75f688bb68de/image.png" /></li>
</ul>
<pre><code class="language-bash">docker rm 0e8e3be7971e
docker rm samadal</code></pre>
<hr />
<h3 id="start--restart--stop">start / restart / stop</h3>
<ul>
<li>개요 <ul>
<li>컨테이너를 <code>실행</code>(활성화) / <code>재실행</code> /<code>중지</code>(비활성화)</li>
</ul>
</li>
<li>문법 <pre><code class="language-bash">docker start / restart / stop &lt;CONTAINER ID&gt;
docker start / restart / stop &lt;NAMES&gt;</code></pre>
</li>
<li>실습 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/63400dc2-3917-4b22-b735-7f9ee4d6a922/image.png" /></li>
</ul>
<hr />
<h3 id="attach">attach</h3>
<ul>
<li><p>개요</p>
<ul>
<li>컨테이너에 접속한다.</li>
</ul>
</li>
<li><p>문법</p>
<pre><code class="language-bash">docker attach &lt;CONTAINER ID&gt;
docker attach &lt;NAMES&gt;</code></pre>
</li>
<li><p>실습 </p>
<ul>
<li><p>기존 <code>eixt는</code> 비활성 상태로 만들고 빠져나옴 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d038cc01-6ef5-4670-be3d-76f0a5a6b8b6/image.png" /></p>
</li>
<li><p>활성상태를 유지하면서 빠져나오기   <code>^ + p + q</code><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/47b41282-0950-4b7b-86c0-b378cd3239bc/image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="exec">exec</h3>
<ul>
<li>개요<ul>
<li>현재 설정된 <code>/bin/bash/(로컬)</code>이 아닌 외부 접속으로 컨테이너 안의 명령 실행</li>
<li>호스트 시스템에서 컨테이너에 접속하지 않고 컨테이너 안의 명령 실행</li>
</ul>
</li>
<li>문법<pre><code class="language-bash">docker exec &lt;컨테이너 이름&gt; &lt;명령&gt; &lt;매개변수&gt;</code></pre>
</li>
<li>실습 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/db9d0111-6bad-4df7-8dc9-7f810ccb35b8/image.png" /></li>
</ul>
<pre><code class="language-bash">docker exec samadal echo &quot;Hi, Cloud...&quot;</code></pre>
<hr />
<h3 id="container-관련-통합-실습">Container 관련 통합 실습</h3>
<ul>
<li><p>커널 버전 확인</p>
<ul>
<li><p>호스트 OS에서 <code>Kernel</code> 버전 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/503607f7-0193-4521-ad6d-7707a16ebbae/image.png" /></p>
</li>
<li><p>컨테이너에서 <code>Kernel</code> 버전 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d72c98de-8ad1-4de2-b88d-54443d12320a/image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="64-컨테이너를-이용한-이미지">6.4 컨테이너를 이용한 이미지</h2>
<h2 id="641-image-관련-명령어">6.4.1 Image 관련 명령어</h2>
<h3 id="사용자가-생성한-컨테이너를-이용한-이미지-생성">사용자가 생성한 컨테이너를 이용한 이미지 생성</h3>
<ul>
<li><p>Step 1. 앞에서 작업했던 이미지, 컨테이너 모두 제거</p>
</li>
<li><p>Step 2. 사전 작업</p>
<ul>
<li>이미지를 검색하고 다운로드<pre><code class="language-bash">docker search centos
docker pull centos:7</code></pre>
</li>
<li>컨테이너 생성<pre><code class="language-bash">docker run -it --name samdocker centos:7 /bin/bash</code></pre>
</li>
<li>컨테이너에 들어간 후 필요한 패키지(kernel 업데이트)를 모두 설치한다.<pre><code class="language-bash">sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
yum -y install epel-release
yum -y update
^ + p + q</code></pre>
</li>
<li>확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b620eb3a-48d7-4e10-a230-9fa8e94b696e/image.png" /></li>
</ul>
</li>
<li><p>Step 3. 이미지 생성</p>
<ul>
<li>부모 이미지(centos:7)와 파생된 컨테이너의 파일 시스템 간의 변경 사항 확인</li>
<li>이미지 생성</li>
</ul>
<pre><code class="language-bash">docker diff beb787
docker commit beb787 centos:7.samadal</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f30cf663-b541-4531-9d4e-d7f03468b2d3/image.png" /></p>
<ul>
<li>생성한 이미지를 이용해서 컨테이너를 생성<pre><code class="language-bash">docker run -it --name hmcloud centos:7.samadal /bin/bash</code></pre>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/252b9406-0c20-4e66-8358-0755ad16aa8f/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h2 id="642-생성한-도커-이미지-관련-작업">6.4.2 생성한 도커 이미지 관련 작업</h2>
<h3 id="도커-루트-디렉토리-관련-확인할-사항">도커 루트 디렉토리 관련 확인할 사항</h3>
<ul>
<li>도커 구성 정보 확인<pre><code class="language-bash">root@CloudDX:~# docker info
...
Docker Root Dir: /var/lib/docker
...</code></pre>
</li>
<li>도커 이미지와 컨테이너 저장소 위치 확인
```bash
root@CloudDX:~# cd /var/lib/docker/
root@CloudDX:/var/lib/docker# ls -l
합계 40
drwx--x--x 4 root root 4096 12월  4 18:01 buildkit
drwx--x--- 4 root root 4096 12월  5 12:42 containers</li>
<li>rw------- 1 root root   36 12월  4 18:01 engine-id
drwxr-x--- 3 root root 4096 12월  4 18:01 network
drwx------ 3 root root 4096 12월  4 18:01 plugins
drwx--x--- 3 root root 4096 12월  4 18:13 rootfs
drwx------ 2 root root 4096 12월  4 18:01 runtimes
drwx------ 2 root root 4096 12월  4 18:01 swarm
drwx------ 2 root root 4096 12월  4 18:01 tmp
drwx-----x 2 root root 4096 12월  4 18:01 volumes
```</li>
<li><code>tree 구조 확인</code><pre><code>root@CloudDX:/var/lib/docker# tree -L 1
</code></pre></li>
</ul>
<p>root@CloudDX:/var/lib/docker# tree -L 1
.
├── buildkit
├── containers
├── engine-id
├── network
├── plugins
├── rootfs
├── runtimes
├── swarm
├── tmp
└── volumes</p>
<p>10 directories, 1 file</p>
<pre><code>---
## 6.4.3 도커 이미지와 컨테이너 생성 및 검사
### 이미지 다운로드 및 컨테이너 생성 방법
- 방법 1. 이미지 다운로드 후 컨테이너 생성
- 방법 2. 이미지 다운로드와 컨테이너 생성을 한번에 동작시키는 방법</code></pre>