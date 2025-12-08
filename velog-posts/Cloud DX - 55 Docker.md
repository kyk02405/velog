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
- 방법 2. 이미지 다운로드와 컨테이너 생성을 한번에 동작시키는 방법
  - 이미지를 자동으로 다운로드 받은 후 컨테이너를 생성만 하고 안으로 들어가지는 않는다.
- `방법 2`에서 생성한 이미지를 이용한 컨테이너

---
## 6.5 도커 컨테이너와 도커 허브 연동
## 6.5.1 사용자가 생성한 컨테이너를 이용한 이미지 생성
- 앞에서 작업했던 모든 것들을 제거
### 사전 작업 
- `6.4.1 작업 참고`
- 이미지 검색하고 다운로드
- 컨테이너를 생성한다.
- 도커로 들어간 후 필요한 패키지(커널) 모두 설치한다.
- 확인
### 이미지 생성
```bash
docker run -it --name hmcloud centos:7.samadal /bin/bash</code></pre><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5f79ff79-0955-4459-a563-ae6d9572d48b/image.png" /></p>
<hr />
<h2 id="652-도커-허브에-이미지-업로드하기-위한-작업">6.5.2 도커 허브에 이미지 업로드하기 위한 작업</h2>
<ul>
<li><p>도커 허브 사이트에 회원가입</p>
</li>
<li><p>터미널에서 도커 허브 사이트 접속 테스트</p>
<pre><code class="language-bash">root@CloudDX:~# docker login -u kyk02405</code></pre>
<ul>
<li>이미지 한 개만 두고 나머지 모두 제거 (컨테이너 포함)</li>
<li>도커 허브에 로그인</li>
</ul>
</li>
<li><p>대표 컨테이너 이미지를 이용해서 컨테이너를 생성하고 컨테이너 이미지를 생성한다.</p>
<ul>
<li><p>도커 허브에 로그인</p>
<pre><code class="language-bash">root@CloudDX:~# docker login -u kyk02405</code></pre>
</li>
<li><p>컨테이너 생성</p>
</li>
<li><p>컨테이너를 이미지로 생성 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/19cc8dcd-db2f-4ab8-aa8e-8b0ab8c30c7b/image.png" /></p>
<ul>
<li><p>작업 1. 오류</p>
<ul>
<li><p>컨테이너 이미지 생성 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/718411b8-a997-4028-af2d-b82411c6bc5d/image.png" /></p>
</li>
<li><p>생성한 컨테이너 이미지 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/527cb988-df1c-45bc-8ef5-bc29171e62ce/image.png" /></p>
</li>
<li><p>도커 허브에 컨테이너 이미지 업로드 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ed466a81-33a6-42ba-b90a-e5c7c4963667/image.png" /></p>
</li>
</ul>
</li>
<li><p>작업 2. 정상</p>
<ul>
<li><p>잘못 만든 컨테이너 이미지 삭제</p>
</li>
<li><p>컨테이너 이미지 생성</p>
<pre><code class="language-bash">docker container commit dockersam (컨테이너명)samadalwho(도커허브계정명)/hmcloud</code></pre>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><p>생성된 컨테이너 이미지를 도커 허브에 업로드</p>
<ul>
<li>도커 허브에 업로드<pre><code class="language-bash">sudo docker push kyk02405(식별자)/hmcloud(이미지명)</code></pre>
</li>
<li>도커 허브에서 업로드된 이미지 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5db123a8-ec4c-443a-b5dc-fafdedaa6153/image.png" /></li>
</ul>
</li>
<li><p>도커 허브에서 컨테이너 이미지 다운로드 하기</p>
<ul>
<li>도커 허브에서 다운로드 받고자 하는 이미지를 미리 삭제</li>
<li>도커 허브에서 이미지를 다운로드 한다<pre><code class="language-bash">docker pull kyk02405/hmcloud</code></pre>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/13ba95ef-4469-4c6c-95d2-3421d95639b4/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h2 id="66-실전-테스트">6.6 실전 테스트</h2>
<h2 id="661-실전-테스트-1">6.6.1 실전 테스트 1.</h2>
<hr />
<h3 id="step-1-작업-개요">Step 1. 작업 개요</h3>
<ul>
<li>임의의 서비스<code>(mariadb)</code>가 동작되는 컨테이너를 생성한다.<ul>
<li>패키지를 설치하고 <code>usersamadal</code>를 생성</li>
<li>관리자와 사용자로 로그인이 잘 되는지 테스트한다.</li>
<li>이 컨테이너를 이미지로 생성한 후 도커 허브에 업로드한다.</li>
<li>로컬에 있는 컨테이너 및 이미지를 모두 삭제한다.</li>
<li>도커 허브에 올려놓은 이미지를 다운로드 한 후 컨테이너를 활성화한다.</li>
<li>앞에서 작업한 관리자(root), 사용자(usersamadal)로 로그인이 잘 되는지 테스트한다.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="step-2-도커-컨테이너-작업-1">Step 2. 도커 컨테이너 작업 1.</h3>
<ul>
<li><p>작업 환경</p>
<ul>
<li>컨테이너에<code>CentOS 7</code>이 설치된 경우에는 데몬 실행 시 오류가 발생한다.</li>
</ul>
</li>
<li><p>초기상태</p>
<ul>
<li>도커 이미지 삭제하고 추가</li>
<li>도커 활성화/비활성화 되어 있는 모든 컨테이너 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ad8a1654-477a-4ac4-85e2-be4de41cf43a/image.png" /></li>
</ul>
</li>
<li><p>컨테이너 생성 (데몬 실행 오류)</p>
<ul>
<li>도커 컨테이너 생성<pre><code class="language-bash">docker run -it --name mariadb_server centos:7 /bin/bash</code></pre>
</li>
<li>도커 컨테이너에 접속<pre><code class="language-bash">docker start mariadb_server
docker attach mariadb_server</code></pre>
</li>
<li>시스템 업데이트<pre><code class="language-bash">sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
yum -y install epel-release
yum -y update
yum -y install firewalld
</code></pre>
</li>
</ul>
<pre><code></code></pre></li>
<li><p>데몬 재실행</p>
</li>
</ul>
<hr />
<h3 id="step-3-도커-컨테이너-작업-2">Step 3. 도커 컨테이너 작업 2.</h3>
<ul>
<li><p>작업 환경</p>
<ul>
<li>컨테이너에 <code>Rocky Linux 8.10</code>이 설치된 경우에는 정상적으로 동작한다.</li>
</ul>
</li>
<li><p><span style="color: red;"><strong>매우 중요</strong></span></p>
<ul>
<li><p><code>컨테이너(mariadb_server)</code> 생성 시 생성되는 컨테이너에 <code>커널(init)까지 접근 가능</code>하도록 <code>권한(--privileged)</code>을 부여한다.
왜? 명령을 실행하면 오류 메시지와 동시에 화면이 멈추는데 <code>privileged</code>와 <code>init</code>는 백그라운드에서 동작이 되어야 하는 것이기 때문이다.</p>
</li>
<li><p><code>centos:latest</code>로 하지 않고 <code>centos:7</code> 또는 <code>centos:7.9.2007</code>로 하면 <code>D-bus</code> 오류가 발생한다. <code>latest</code>는 <code>CentOS 8.x</code>가 적용된다.</p>
</li>
<li><p>그러나 <code>centos:latest</code>, <code>centos:7</code>, <code>centos:7.9.2007</code> 등 3가지 모두 <code>D-Bus</code> 오류가 발생한다.</p>
</li>
<li><p>따라서 <code>Rocky Linux 8</code>으로 설치를 진행한다.</p>
</li>
<li><p>(중요) 따라서 멈춘 화면은 <code>작업 표시줄</code>로 내리고 <code>신규 터미널창</code>을 하나 더 열고 작업하면 된다. </p>
</li>
<li><p>앞에서 작업했던 모든 것을 다 제거한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f01699ca-8e77-4b33-adb6-d3d1f90268be/image.png" /></p>
</li>
<li><p>명령 실행 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f9bd43ff-6000-4262-b61d-693a993ae931/image.png" /> </p>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo docker run -it --privileged --name mariadb_server rockylinux:8 init</code></pre>
</li>
<li><p>신규 터미널을 새로 띄우고 컨테이너에 접속 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ebb014a0-6ceb-47c0-a938-4ac110524a78/image.png" /></p>
</li>
<li><p>기타 작업</p>
<ul>
<li><code>저장소 업데이트</code><pre><code class="language-bash">[root@1c9f908a1987 /]# dnf -y install epel-release
[root@1c9f908a1987 /]# dnf -y update</code></pre>
</li>
<li><code>방화벽</code><pre><code class="language-bash">[root@1c9f908a1987 /]# dnf -y install firewalld
[root@1c9f908a1987 /]# systemctl enable firewalld
[root@1c9f908a1987 /]# systemctl restart firewalld
[root@1c9f908a1987 /]# firewall-cmd --permanent --add-port=3306/tcp
[root@1c9f908a1987 /]# firewall-cmd --permanent --add-port=22/tcp
[root@1c9f908a1987 /]# firewall-cmd --permanent --add-service=mysql
[root@1c9f908a1987 /]# firewall-cmd --reload</code></pre>
</li>
<li><code>DB 패키지 설치</code><pre><code class="language-bash">[root@1c9f908a1987 /]# dnf -y install mariadb-*
[root@1c9f908a1987 /]# systemctl enable mariadb
[root@1c9f908a1987 /]# systemctl restart mariadb
[root@1c9f908a1987 /]# mysql -u root -p mysql</code></pre>
</li>
</ul>
</li>
<li><p><code>Database Server 작업 1. 사용자(usersamadal) 생성</code></p>
<pre><code class="language-bash">MariaDB [mysql]&gt; CREATE USER 'usersamadal'@'%' IDENTIFIED BY 'pwsamadal';</code></pre>
</li>
<li><p><code>Database Server 작업 2. 사용자(usersamadal) 접속 테스트</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/afaef6f7-0a4d-4c24-b7ac-cbf16aacf533/image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="step-4-도커-허브에-도커-컨테이너-이미지-업로드">Step 4. 도커 허브에 도커 컨테이너 이미지 업로드</h3>
<ul>
<li><p>컨테이너 생성하기 전에 확인할 내용 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/85e6bfc1-38e7-4c6f-ab52-aac649b5e606/image.png" /></p>
</li>
<li><p>도커 허브에 접속 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/10c013a2-cab1-41a0-ba47-fee227bdd157/image.png" /></p>
</li>
<li><p>도커 허브에 생성 및 업로드 1. without TAG</p>
<ul>
<li><p>이미지 생성 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7ec25961-9ed1-485e-958f-845c89b5622e/image.png" /></p>
</li>
<li><p>업로드 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/435177ba-4ee3-49cd-8bbe-b6d285f4bf8b/image.png" /></p>
</li>
<li><p>사이트에서 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/54e8a189-6b84-4551-8e36-60d6accc937e/image.png" /></p>
</li>
</ul>
</li>
<li><p>도커 허브에 생성 및 업로드 2. with TAG</p>
<ul>
<li><p>이미지 생성 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0a5befb7-a550-4c8c-9d4d-81febc10900c/image.png" /></p>
</li>
<li><p>업로드 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1ccfe3db-eb20-4142-b30e-f8987cafb222/image.png" /></p>
</li>
<li><p>사이트에서 확인<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6b4fafd0-2c23-4ae1-a34f-81b3d9c5543d/image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="step-5-도커-허브에-업로드-한-도커-컨테이너-이미지를-다운로드-한-후-컨테이너-활성화">Step 5. 도커 허브에 업로드 한 도커 컨테이너 이미지를 다운로드 한 후 컨테이너 활성화</h3>
<ul>
<li>로컬에 있는 이미지 및 컨테이너 모두 제거 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/eb51c160-4873-4524-9568-155bf3cb8247/image.png" /></li>
<li>다운로드 후 활성화 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0d76a7ef-f79a-440f-9aa2-2e6f95f1888c/image.png" /><pre><code class="language-bash">samadal@CloudDX:~$ sudo docker run -it --name mariadb_server kyk02405/mariadb:1.0 /bin/bash</code></pre>
</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0e348dfb-c266-423c-b52a-e62d7e5dcedd/image.png" /></li>
</ul>
<hr />
<h2 id="662-실전테스트-2-도커에서-ssh-접속">6.6.2 실전테스트 2. 도커에서 SSH 접속</h2>
<h3 id="접속-1-호스트-시스템에서-도커-컨테이너로-ssh를-이용한-접속-1-기본-포트22">접속 1. 호스트 시스템에서 도커 컨테이너로 SSH를 이용한 접속 1. 기본 포트(22)</h3>
<ul>
<li>Step 1. 도커 컨테이너 확인 후 제거<pre><code class="language-bash">samadal@CloudDX:~$ sudo docker stop mariadb_server
samadal@CloudDX:~$ sudo docker rm mariadb_server</code></pre>
</li>
<li>Step 2. 도커 컨테이너 등록<pre><code class="language-bash">samadal@CloudDX:~$ sudo docker pull centos:7
samadal@CloudDX:~$ sudo docker create -it --privileged --name mdb kyk02405/mariadb:1.0 init
9251eb815b46f027c5c5ba5085f6825e5876222f4a9e29cd04a7ed6bb63ab596
</code></pre>
</li>
</ul>
<pre><code>- Step 3. 도커 컨테이너 접속
```bash
samadal@CloudDX:~$ sudo docker start mdb
mdb
samadal@CloudDX:~$ sudo docker exec -it mdb /bin/bash
[root@9251eb815b46 /]#</code></pre><blockquote>
<ul>
<li><code>init</code>으로 생성한 컨테이너 접속시에는 <code>exec</code> 사용</li>
</ul>
</blockquote>
<pre><code class="language-bash">sudo docker exec -it mdb /bin/bash</code></pre>
<ul>
<li><p>그외는 <code>attach</code> 사용</p>
<pre><code class="language-bash">sudo docker attach mdb</code></pre>
</li>
<li><p>Step 4. 도커 컨테이너 IP 확인</p>
<pre><code class="language-bash">[root@9251eb815b46 /]# yum -y install net-tools</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/727b81aa-483a-48ff-b531-6a95f10d70e9/image.png" /></p>
</li>
<li><p>Step 51. <code>호스트 시스템(Ubuntu)</code>에서 SSH를 이용한 컨테이너 접속 1. 신규 터미널 창(호스트 시스템) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c47fdbf7-a0ed-4a0e-8b8d-4c4d459ee671/image.png" /></p>
<ul>
<li>시스템간 통신 확인</li>
<li>도커 컨테이너에 접속 (접속 거부 오류 발생)<ul>
<li><code>ping</code>은 되지만 접속 거부 됨</li>
</ul>
</li>
</ul>
</li>
<li><p>Step 52. <code>호스트 시스템(Ubuntu)</code>에서 SSH를 이용한 컨테이너 접속 2. 기존 터미널창(도커 컨테이너 터미널 창)</p>
<ul>
<li>패키지 설치 (<code>openssh-*</code>)<pre><code class="language-bash">[root@9251eb815b46 /]# yum -y install openssh-*</code></pre>
</li>
<li>방화벽 해제 (<code>vi /etc/selinux/config</code> 수정) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1df05d6e-4acb-4a01-bc04-55128ba5f71b/image.png" /></li>
<li>서비스 및 데몬 재실행<pre><code class="language-bash">[root@9251eb815b46 /]# systemctl enable sshd
[root@9251eb815b46 /]# systemctl restart sshd</code></pre>
</li>
</ul>
</li>
<li><p>Step 53. <code>호스트 시스템(Ubuntu)</code>에서 SSH를 이용한 컨테이너 접속 3. 신규 터미널창(호스트 시스템)</p>
<ul>
<li>도커 컨테이너에 접속 (관리자 접속 거부 오류 발생) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/974a6854-62c9-468f-a6a9-6fb88a8b23c0/image.png" /></li>
</ul>
</li>
<li><p>Step 54. <code>호스트 시스템(Ubuntu)</code>에서 SSH를 이용한 컨테이너 접속 4. 기존 터미널창(도커 컨테이너 터미널 창)</p>
<ul>
<li><code>관리자(root)</code>의 비밀번호 지정과 <code>신규 사용자(samadal)</code>를 생성하고 비밀번호를 지정<pre><code class="language-bash">[root@9251eb815b46 /]# yum -y install passwd
[root@9251eb815b46 /]# passwd
[root@9251eb815b46 /]# useradd samadal
[root@9251eb815b46 /]# passwd samadal</code></pre>
</li>
</ul>
</li>
<li><p>Step 55. <code>호스트 시스템(Ubuntu)</code>에서 SSH를 이용한 컨테이너 접속 5. 신규 터미널창(호스트 시스템)</p>
<ul>
<li>도커 컨테이너에 접속 (접속 허가 거부 오류 발생) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/50eebce2-8c88-42b3-8bd2-f1a0530579c6/image.png" /></li>
</ul>
</li>
<li><p>Step 56. <code>호스트 시스템(Ubuntu)</code>에서 SSH를 이용한 컨테이너 접속 6. 기존 터미널창(도커 컨테이너 터미널 창)</p>
<ul>
<li><code>vi /etc/ssh/sshd_confing</code>접속<ul>
<li><code>PAM(pluggable Authentication Modules)</code>은 <code>접속허용</code>을 위한 사용 여부를 묻는다. <code>yes(허용)</code>, <code>no(거부)</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0695edde-d038-4903-86db-e17f1eb5de83/image.png" /></li>
<li>주석 처리하고 데몬 재실행</li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li><p>Step 57. <code>호스트 시스템(Ubuntu)</code>에서 SSH를 이용한 컨테이너 접속 7. 신규 터미널창(호스트 시스템)</p>
<ul>
<li>도커 컨테이너에 접속(성공) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e8c0dde0-eacb-4228-be62-e757f23ba6d1/image.png" /><h3 id="접속-2-호스트-시스템에서-도커-컨테이너로-ssh를-이용한-접속-2-전용-포트22-이외의-포트로-접속">접속 2. 호스트 시스템에서 도커 컨테이너로 SSH를 이용한 접속 2. 전용 포트(22) 이외의 포트로 접속</h3>
</li>
</ul>
</li>
<li><p>Step 1. 기본 작업</p>
<ul>
<li>포트(8081/tcp) 추가 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/abc69ed1-df57-4d2f-89ab-9f1fae375a66/image.png" /></li>
</ul>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo ufw allow 8081/tcp
samadal@CloudDX:~$ sudo ufw reload</code></pre>
<ul>
<li>도커 확인 이미지 및 컨테이너 확인 후 활성 상태가 있으면 중지 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f38d5ff8-b39e-4d7e-a9f9-77f185488ed7/image.png" /></li>
</ul>
</li>
<li><p>Step 2. 도커 컨테이너 생성 후 접속 </p>
<ul>
<li>생성 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f7695bf8-8a86-4d8c-b68f-76f9c0fe8ff3/image.png" /></li>
</ul>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo docker create -it --privileged -p 8081:22 --name cloudsamadal rockylinux:8 init</code></pre>
<ul>
<li><p>확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e58575ab-b7e0-4ab4-85b1-6968767cbc8e/image.png" /></p>
</li>
<li><p>접속  <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/14e70e3d-4cec-4940-9214-065dcd66b7c7/image.png" /></p>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo docker start cloudsamadal
samadal@CloudDX:~$ sudo docker exec -it cloudsamadal /bin/bash</code></pre>
</li>
<li><p>네트워크 활성화</p>
<pre><code class="language-bash">[root@83bcb5ed1a83 /]# yum -y install net-tools</code></pre>
</li>
<li><p><code>SSH</code> 패키지 설치</p>
<pre><code class="language-bash">[root@83bcb5ed1a83 /]# yum -y install openssh-*</code></pre>
</li>
<li><p>서비스 및 데몬 실행</p>
<pre><code class="language-bash">[root@83bcb5ed1a83 /]# systemctl enable sshd
[root@83bcb5ed1a83 /]# systemctl restart sshd</code></pre>
</li>
<li><p>포트 확인</p>
<pre><code class="language-bash">[root@83bcb5ed1a83 /]# netstat -atunp | grep ssh
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      303/sshd
tcp6       0      0 :::22                   :::*                    LISTEN      303/sshd</code></pre>
</li>
<li><p>관리자 비번 지정 및 사용자 생성</p>
<pre><code class="language-bash">yum -y install passwd
useradd samadal
passwd
passwd samadal</code></pre>
</li>
<li><p>실행 상태에서 빠져 나온다. </p>
<ul>
<li><code>^ + p + q</code></li>
</ul>
</li>
<li><p><code>SSH</code> 접속</p>
<ul>
<li>다른 포트로 접속할 때는 <code>IP</code>가 아닌 <code>localhost</code>로 접속해야 한다.<pre><code class="language-bash">samadal@CloudDX:~$ sudo ssh -p 8081 root@localhost</code></pre>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="접속-3-도커-컨테이너에서-호스트-시스템에-ssh를-이용한-접속">접속 3. 도커 컨테이너에서 호스트 시스템에 SSH를 이용한 접속</h3>
<ul>
<li><p>Step 1. 기본 작업</p>
<ul>
<li>등록된 이미지 및 컨테이너 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a4047dc2-47a7-441f-af35-8eea24a83de7/image.png" /></li>
<li>호스트와의 통신 상태 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7ad3ac77-56c7-4017-9384-e91d069324d0/image.png" /></li>
</ul>
</li>
<li><p>Step 2. 도커 컨테이너 생성 후 접속 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e25e1e50-8980-458f-9789-de34fe468380/image.png" /></p>
</li>
</ul>
<ul>
<li>Step 3. 호스트 시스템에 접속한 상태에서 컨테이너 상태 확인<pre><code class="language-bash">ssh samadal@192.168.10.128</code></pre>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/14188377-b11d-4993-b08c-70ce91147a5d/image.png" /></li>
</ul>
<hr />
<h2 id="663-실전테스트-3-docker에서의-apache-web-server">6.6.3 실전테스트 3. Docker에서의 Apache Web Server</h2>
<h3 id="실습-1-osrocky-linux-810에서-지원하는-기능httpd-패키지을-이용한-도커-컨테이너">실습 1. OS(Rocky Linux 8.10)에서 지원하는 기능(httpd 패키지)을 이용한 도커 컨테이너</h3>
<h3 id="apache-webe-server-접속을-위한-설정-커널-모드-사용">Apache Webe Server 접속을 위한 설정 (커널 모드 사용)</h3>
<ul>
<li><p>Step 1. 도커 이미지 및 컨테이너 확인 <code>(UP 상태 확인)</code><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/82c57526-f6ab-45e7-8ddc-19c6cced011c/image.png" /></p>
</li>
<li><p>Step 2.방화벽 포트 추가</p>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo ufw allow 8014/tcp</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/02ef2b1b-1a97-4b3f-ab67-df4ba8bd8634/image.png" /></p>
</li>
<li><p>Step 3. 도커 컨테이너 생성</p>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo docker create -it --privileged -p 8014:80 --name websamadal rockylinux:8 init</code></pre>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/70ea74ec-8f24-4949-9de4-fde4da645e15/image.png" /></p>
<ul>
<li><p>Step 4. 도커 컨테이너 접속</p>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo docker start websamadal
websamadal
samadal@CloudDX:~$ sudo docker exec -it websamadal /bin/bash
[root@e82d7900f0ec /]#</code></pre>
<h3 id="도커-컨테이너-접속-후-기본-작업">도커 컨테이너 접속 후 기본 작업</h3>
</li>
<li><p>시스템 업데이트</p>
<pre><code class="language-bash">[root@e82d7900f0ec /]# dnf -y update</code></pre>
</li>
<li><p>네트워크 확인</p>
<pre><code class="language-bash">[root@e82d7900f0ec /]# dnf -y install net-tools
[root@e82d7900f0ec /]# dnf -y install iproute</code></pre>
</li>
<li><p>방화벽 관련 작업</p>
<pre><code class="language-bash">[root@e82d7900f0ec /]# dnf -y install firewalld</code></pre>
</li>
<li><p>패키지 관련 작업</p>
<pre><code class="language-bash">[root@e82d7900f0ec /]# dnf -y install httpd-*
[root@e82d7900f0ec /]# systemctl enable httpd
[root@e82d7900f0ec /]# systemctl restart httpd</code></pre>
</li>
<li><p>포트 활성 상태 확인</p>
<pre><code class="language-bash">&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;zone&gt;
&lt;short&gt;Public&lt;/short&gt;
&lt;description&gt;For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.&lt;/description&gt;
&lt;service name=&quot;ssh&quot;/&gt;
&lt;service name=&quot;http&quot;/&gt;
&lt;service name=&quot;dhcpv6-client&quot;/&gt;
&lt;service name=&quot;cockpit&quot;/&gt;
&lt;port port=&quot;80&quot; protocol=&quot;tcp&quot;/&gt;
&lt;port port=&quot;22&quot; protocol=&quot;tcp&quot;/&gt;
&lt;/zone&gt;</code></pre>
<h3 id="사이트-출력-1">사이트 출력 1.</h3>
</li>
<li><p><code>Host OS</code>인 <code>Ubuntu</code>에서 불여시를 실행한 후 <code>[root@e82d7900f0ec /]# systemctl restart httpd</code>를 입력, 출력 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/40842c82-a1bd-473d-948e-c6988bb94bc4/image.png" /></p>
</li>
</ul>
<h3 id="도커-컨테이너-상태-확인">도커 컨테이너 상태 확인</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/30c2ddc8-b185-4fab-a21b-66ee41eccdd0/image.png" /></p>
<h3 id="사이트-출력-2">사이트 출력 2.</h3>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo docker exec -it websamadal /bin/bash
[root@e82d7900f0ec /]# vi /var/www/html/index.html</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f0668244-a45a-4224-8a19-c58eb0363735/image.png" /></p>
<h3 id="사이트-출력-3-host-osubuntu의-host-oswindows-10의-웹브라우저에서-출력">사이트 출력 3. Host OS(Ubuntu)의 Host OS(Windows 10)의 웹브라우저에서 출력</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cc84b008-1a0f-4c30-bda8-097843fd88c1/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2baca9e7-78a4-4434-a59a-4637d757eae4/image.png" /></p>
<hr />
<h3 id="실습-2-apache-web-server-이미지를-이용한-도커-컨테이너">실습 2. Apache Web Server 이미지를 이용한 도커 컨테이너</h3>
<ul>
<li><p>준비 작업 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/35a425f0-7f49-4dbf-a93e-914f46b7c49b/image.png" /></p>
</li>
<li><p>도커 이미지 검색 후 다운로드 </p>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo docker search httpd
samadal@CloudDX:~$ sudo docker pull httpd</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/af306b98-8b9e-40bc-a196-c13410fe62e8/image.png" /></p>
</li>
<li><p>컨테이너 삭제 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e91d1b78-f567-42b2-bd38-bef44a1f9372/image.png" /></p>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo docker rm websamadal</code></pre>
</li>
<li><p>도커 컨테이너 생성(다운로드 한 이미지를 사용하지 않고 생성)</p>
<pre><code class="language-bash">samadal@CloudDX:~$ sudo docker run -itd --name websamadal -p 8014:80 httpd</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c05e6581-b81d-4118-9051-65a733946002/image.png" /></p>
</li>
</ul>
<ul>
<li>사이트 출력 1.</li>
</ul>