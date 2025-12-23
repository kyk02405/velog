# Cloud DX - 57 CI-CD 파이프라인 구축 (Jenkins)

- 📅 Published: Fri, 19 Dec 2025 09:20:00 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-57-CICD-%ED%8C%8C%EC%9D%B4%ED%94%84%EB%9D%BC%EC%9D%B8-%EA%B5%AC%EC%B6%95-Jenkins)

<hr />
<h1 id="8-cicd-파이프라인-구축">8. CI/CD 파이프라인 구축</h1>
<h2 id="81-일반">8.1 일반</h2>
<h2 id="pipeline-파이프라인">Pipeline (파이프라인)</h2>
<h3 id="개요">개요</h3>
<ul>
<li><code>Container</code>로 구동하는 <code>Application</code>을 배포하는 <code>가장 효율적인 진행 과정</code>을 말한다.</li>
</ul>
<h3 id="kubernetes에서의-진행-과정">Kubernetes에서의 진행 과정</h3>
<h4 id="docker-build">Docker Build</h4>
<ul>
<li><code>GitHub</code> 등의 지장소에 저장해 둔 <code>Application</code> 소스 코드를 내려받아 <code>Docker Container Image</code>로 <code>Build</code> 한다.</li>
<li><code>Docker Image</code>를 만들어서 사용할 수 있게 해주기 위한 것을 말한다.</li>
</ul>
<h4 id="docker-push">Docker Push</h4>
<ul>
<li><code>Build</code> 한 <code>Docker Container Image</code>를 <code>Kubernetes</code>에서 사용할 수 있도록 레지스트리에 등록한다.</li>
</ul>
<h4 id="kubectl-create">Kubectl Create</h4>
<ul>
<li>레지스트리에 등록된 이미지를 기반으로 <code>Kubernetes Object</code>를 생성한다.</li>
</ul>
<h4 id="docker-expose">Docker Expose</h4>
<ul>
<li>생성한 <code>Objectb(Pod / Deployment)를 외부에서 접속한 수 있도록</code>서비스 형태로 노출`한다.</li>
</ul>
<hr />
<h3 id="cicontinuous-integration-지속적-통합과-cdcontinuous-deployment-지속적-배포">CI(Continuous Integration, 지속적 통합)과 CD(Continuous Deployment, 지속적 배포)</h3>
<ul>
<li><code>CI/CD</code>는 실무적인 환정에서 변경 사항을 계속 추적해 좀 더 안정화된 <code>Application</code>을 만들고, 이를 배포하는 과정을 자동화해서 안정적으로 운영하는 데 가장 많이 쓰이는 개념이다.</li>
</ul>
<hr />
<h2 id="컨테이너-인프라-환경에서의-cicd">컨테이너 인프라 환경에서의 CI/CD</h2>
<h3 id="개요-1">개요</h3>
<ul>
<li>컨테이너 인프라 환경에서는 주로 <code>CD</code>를 강조하지만, <code>CI</code>와 <code>CD</code>는 대부분 함께 사용되기 때문에 우선 <code>CI/CD</code>의 개념을 정확히 이해해야 한다.</li>
<li>일반적으로 <code>CI</code>는 코드를 커밋하고 빌드했을 때 정상적으로 작동하는지 반복적으로 검증해 <code>Application</code>의 신뢰성을 높이는 작업이다.</li>
<li><code>CI</code> 과정을 마친 <code>Application</code>은 신뢰할 수 있는 상태가 된다.</li>
<li><code>CD</code>는 <code>CI</code> 과정에서 생성된 신뢰할 수 있는 <code>Application</code>을 실제 상용 환경에 자동으로 배포 하는 것을 의미한다.</li>
<li><code>Application</code>을 상용 환경에 배포할 때 고려해야 할 사항이 여러 가지 있는데, 이를 <code>CD</code>에 미리 정의하면 실수를 줄이고, 실제 적용 시간</li>
</ul>
<hr />
<h3 id="컨테이너-인프라-관점에서의-cicd-application-개발-과정에서의-cicd">컨테이너 인프라 관점에서의 'CI/CD' ('Application' 개발 과정에서의 'CI/CD')</h3>
<ul>
<li>개발자가 소스를 <code>커밋(Commit)</code>하고 <code>푸시(Push)하면</code>CI` 단계로 들어간다.</li>
<li><code>CI</code> 단계에서는 <code>Application</code>이 자동 빌드되고 테스트를 거처 배포할 수 있는 <code>Application</code>인지 확인한다.</li>
<li>테스트를 통과하면 신뢰할 수 있는 <code>Application</code>으로 간주하고 <code>CD</code> 단계로 넘어간다..</li>
<li><code>CD</code> 단계에서는 <code>Application</code>을 <code>컨테이너 이미지</code>로 만들어서 <code>Pod</code>, <code>Deployment</code>, <code>StateFullSet</code> 등
다양한 <code>Object</code> 조건에 맞춰 미리 설정한 파일을 통해 배포한다.</li>
</ul>
<hr />
<h2 id="jenkins젠킨스">Jenkins(젠킨스)</h2>
<h3 id="개요-2">개요</h3>
<ul>
<li><code>Jenkins</code>는 사용자가 직접 <code>UI</code>에서 작업을 구성하거나 작업 순서를 코드로 정의할 수 있다.</li>
<li>특정 언어나 환경에 구애받지 않고 범용적인 목적으로 무난하게 쓸 수 있다.</li>
</ul>
<h3 id="plug-in">Plug-in</h3>
<ul>
<li><code>Plug-in</code>은 특정 기능을 호스트 프로그램에 추가하는 소프트웨어 구성 요소를 말한다.</li>
<li>즉, 기존 프로그램의 기능을 확장하거나 사용자 정의할 수 있도록 도와주는 도구이다.</li>
<li><code>웹 브라우저, 음악 제작, 워드프레스</code> 등 다양한 분야에서 사용된다.</li>
</ul>
<hr />
<h3 id="jenkins로-kubernetes-운영-환경-개선">Jenkins로 Kubernetes 운영 환경 개선</h3>
<ul>
<li>개요<ul>
<li>'Application' '배포(Deployment)' 영역에 'Kubernetes'를 사용하면 개발자는 'Application' 개발에만 집중할 수 있게 된다.</li>
<li>기존에는 환경이 다른 곳에 빌드한 'Application'을 배포하게 되면 개발자가 개별 환경 에 맞춰 'Application' 코드를 일일이 수정해야 했었다.</li>
<li>(핵심) 모든 배포 환경을 컨테이너 인프라로 일원화하고, 'CI/CD(자동화)' 도구를 사용하면 'Application'에 맞는 환경을 적용해 자동으로 배포할 수 있다.</li>
<li>개발자가 작성한 'Application' 코드를 소스 코드 저장소에 푸시하면. 'Kubernetes' 내부에 설치된 'Jenkins'는 'Application' 코드를 빌드하고 레지스트리에 푸시한 후에 'Kubernetes'에서 사용 가능한 형태로 배포한다.</li>
<li>컨테이너 인프라 환경에서 'Jenkins'를 사용하는 주된 이유는 'Application'을 컨테이너로 만들고 배포하는 과정을 자동화하기 위해서이다.</li>
<li>하지만 자동화 환경은 단순히 'Jenkins'용 'Pod'만을 배포해서는 만들어지지 않는다.</li>
<li>'Jenkins'는 컨트롤러와 에이전트 형태로 구성한 다음 배포해야 하며 여기에 필요한 설정을 모두 넣어야 한다.</li>
<li>'Application'을 배포하기 위한 환경을 하나하나 구성 하는 것은 매우 복잡하고 번거로운 일이며, 고정된 값이 아니기 때문에 'Manifest File'로 작성해 그대로 사용할 수가 없고 구성 환경에 따라 많은 부분을 동적으로 변경해야 한다.</li>
<li>동적인 변경 사항을 간편하고 빠르게 적용할 수 있도록 도와주는 도구가 다음과 같은 두 가지 있다.<ul>
<li>'Kustomize (커스터마이즈)'이고, 다른 하나는 'Helm (헬름)'이다.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h1 id="82-jenkins-설치를-위한-간편화-도구-살펴보기">8.2 Jenkins 설치를 위한 간편화 도구 살펴보기</h1>
<h3 id="일반">일반</h3>
<ul>
<li>개요<ul>
<li>지난 실습에서 'Nginx 'Application''을 사용하려면 디플로이먼트를 생성하고 이를 서비스로 노출 하는 'Object' 생성 과정을 총 두 번 진행해야 했었다.</li>
<li>그런데 이런 적은 수의 'Object'로 모든 종류의 'Application'을 사용자가 사용할 수 있는 형태로 구현할 수는 없다.</li>
<li>필요에 따라서는 다수의 'Object'를 사용해야 하는데, 우리는 이미 3장에서 수많은 'Object'를 한 번에 생성하는 'Metadata'를 실행한 적이 있다.</li>
<li>'MetalLB'를 구동하는 데 필요한 수많은 'Object'를 미리 정의된 하나의 'Manifest'에 넣고 바로 실행했다.</li>
<li>모든 환경에서 단순히 'Object'를 정의한 대로만 사용한다면 'Jenkins'나 'Kustomize', 헬륨 등은 알 필요가 없다.</li>
<li>그러나 사용자마다 필요한 환정적 요소가 모두 다르므로 이를 요구 사항에 맞게 바꾸어야 한다.</li>
</ul>
</li>
<li>배포 간편화 도구 비교하기<ul>
<li>그동안 사용한 'kubectl'은 사실 바이너리 실행 파일로 짜인 배포 도구이다.</li>
<li>'kubectl'이 없다면 직접 코드를 짜서 API 서버에 명령을 내려야 한다.</li>
<li>'Kustomize와 헬름은 kubeatl을 좀 더 확장해서 복잡한 'Object'와 구성 환경을 자동으로 맞추는 도구이다.</li>
</ul>
</li>
<li>배포 도구<ul>
<li>배포 도구 비교<ul>
<li>'kubectl’<ul>
<li>설치 방법 ('Kubernetes'에 기본 탑재)</li>
<li>배포 대상 (정적인 'YAML' 파일)</li>
<li>주 용도 ('Object' 관리 및 배포)</li>
<li>가변적 환경 ('YAML' 파일이 일일이 수정해야 하기 때문에 대응이 힘들다.)</li>
<li>기능 복잡도 (단순하다.)</li>
<li>'Kubernetes'에 기본으로 포합된 커맨드라인 도구로, 추가 설치 없이 바로 사용할 수 있다.</li>
<li>'Object' 생성과 'Kubernetes' 클러스터에 존재하는 'Object', 이베트 등의 정보를 확인하는데 사용하는 활용도 높은 도구이다.</li>
<li>또한 'Object'의 명세가 정의된 야뮬 파일을 인자로 입력받아 파일 내용에 따라 'Object'를 배포할 수도 있다.</li>
<li>‘kubectl’은 정의된 'Manifest' 파일을 그대로 배포하기 때문에 개별적인 'Object'를 관리 하거나 배포할 때 사용하는 것이 좋다.</li>
</ul>
</li>
<li>'kustomize’<ul>
<li>설치 방법 (별도 실행 파일 또는 'Kubernetes'에 통합)</li>
<li>배포 대상 ('Kustomize 파일)</li>
<li>주 용도 ('Object'의 가변적 배포)</li>
<li>가변적 환경 (간단한 대응이 가능하다.)</li>
<li>기능 복잡도 (보통이다.)</li>
<li>'Object'를 사용자의 의도에 따라 유동적으로 배포할 수 있다.</li>
<li>별도의 'Kustomize' 실행 파일을 활용해 'Kustomize' 명세를 따르는 야물 파일을 생성합 수 있다.</li>
<li>'YAML' 파일이 이미 존재한다면 'kubect1'로도 배포할 수 있는 '옵선(-k)'이 있을 정도로 'kubectl'과 매우 밀접하제 동작한다.</li>
<li>'Kustomize'는 명세와 관련된 'YAML' 파일에 번수나 템플릿을 사용하지는 않지만 명링이로 배포 대상 'Object'의 이미지 대그와 레이블 같은 같은 명세를 변경하거나 일반 파일을 이용해 'ConfigMap'과 시크릿을 생성하는 기능을 지원한다.</li>
</ul>
</li>
<li>'Helm’<ul>
<li>설치 방법 (별도 설치)</li>
<li>배포 대상 (패키지 차트)</li>
<li>주 용도 (패키지 단위 'Object' 배포 및 관리)</li>
<li>가변적 환경 (복잡한 대응이 가능하다.)</li>
<li>기능 복잡도 (복잡하다.)</li>
<li>'Kubernetes' 사용자의 '70%' 이상이 사용하고 있어 정도로 널리 알려진 도구로, 'Object' 배포에 필요한 사양이 이미 정의된 '차트(Chart)'라는 패키지를 활용한다.</li>
<li>앞선 두 가지 도구와 달리 'Helm Chart' 저장소가 온라인에 있기 때문에 패키지를 검색하고 내려받아 사용하기가 매우 간편하다.</li>
<li>'Helm Chart'는 자체적인 템플릿 문법을 사용하므로 가번적인 인자를 배포한 때 적용해 다양한 배포 환경에 맞추거나 원하는 조건을 적용할 수 있다.</li>
<li>'Helm'은 'Object'를 뮤어 패키지 단위로 관리하므로 단순한 1개의 명령어로 'Application'에 필요한 'Object'들을 구성한 수 있다.</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="kustomize로-배포-간편화하기">‘kustomize’로 배포 간편화하기</h3>
<ul>
<li><p>개요</p>
<ul>
<li>'kustomize'를 통한 배포는 'Kubectl'에 구성되어 있는 'Manifest'를 고정적으로 이용해야 하는 기존 방식을 유연하게 만든다.</li>
</ul>
</li>
<li><p>'kustomize'의 작동 원리</p>
<ul>
<li>'kustomize'는 'YAML' 파일에 정의된 값을 사용자가 원하는 값으로 변경할 수 있다.</li>
<li>'Kubernetes'에서 'Object'에 대한 수정 사항을 반영하려면 사용자가 직접 'YAML' 파일을 편집기 프로그램으로 수정해야 한다.</li>
<li>일반적으로 이런 방식으로 수정했을 때 큰 문제가 발생하지 않는다.</li>
<li>그런데 만약 수정해야하는 'YAML' 파일이 매우 많거나 하나의 'YAML' 파일로 환경이 다른 여러 개의 'Kubernetes' 클러스터에 배포해야 해서 'LABEL'이나 'NANE' 같은 일부 항목을 수정해야 한다면 매번 일일이 고치는데 많은 노력이 드는데 'kustomize'는 이를 위해 'kustomize' 명령을 제공한다.</li>
<li>'kustomize' 명령과 'create 읍션'으로 'kustomization.yam'이라는 기본 'Manifest'를 만들고. 이 파일에 변경해야 하는 값들을 적용한다.</li>
<li>그리고 'build' 옵션으로 변경할 내용이 적용된 최종 'YAML' 파일을 저장하거나 변경된 내용이 바로 실행되도록 지정한다.</li>
<li>예를 들어 'MetallB 0.9' 버전부터는 'Kubernetes'에서 'MetalLB'를 구성할 때 컨트롤러와 에이전트인 스피커가 통신할 때 보안을 위해 쿠비네티스의 시크릿(secrct) 'Object'를 한다.</li>
<li>이에 따라서 기존에는 'Manifest' 방법만 안내됐지만, '0.9 버전'부터는 복잡한 설치 과정을 간편화할수 있도록 'Kustomize 방법을 추가로 안내하고 있다.</li>
<li>이 책에서는 편의성을 위해서 '시크릿을 사용하지 않은 0.8 버전'을 사용한다.</li>
<li>그러면 'Kustomize'로 'MetalLB'를 구성해 보도록 한다.</li>
</ul>
</li>
<li><p>실습 1. ‘kustomize’로 ‘MetalLB’ 한 번에 만들기</p>
<ul>
<li><p>개요</p>
</li>
<li><p>Step 0. 초기 작업</p>
<ul>
<li>앞에서 작업했던(<a href="https://onedrive.live.com/?redeem=aHR0cHM6Ly8xZHJ2Lm1zL2YvcyFBZ0NMQUlVXzQ3UFZoVkFWeWFYNTh2LVFWNDRV&amp;id=D5B3E33F85008B00%21720&amp;cid=D5B3E33F85008B00">https://onedrive.live.com/?redeem=aHR0cHM6Ly8xZHJ2Lm1zL2YvcyFBZ0NMQUlVXzQ3UFZoVkFWeWFYNTh2LVFWNDRV&amp;id=D5B3E33F85008B00%21720&amp;cid=D5B3E33F85008B00</a>) 버츄얼 박스 파일을 삭제하고 새로 준 vagrant file을 이용하여 설치한다.</li>
</ul>
</li>
<li><p>Step 1. ‘kustomize-install.sh’ 명령어를 이용한 ‘Kustomize’ 실행 파일 다운로드</p>
<p>```
[root@m-k8s 5.2.2]# ls -l
total 20</p>
</li>
<li><p>rwx------. 1 root root  261 Dec 22 11:12 kustomize-install.sh</p>
</li>
<li><p>rw-r--r--. 1 root root  223 Dec 22 11:12 metallb-l2config.yaml</p>
</li>
<li><p>rw-r--r--. 1 root root 5384 Dec 22 11:12 metallb.yaml</p>
</li>
<li><p>rw-r--r--. 1 root root   90 Dec 22 11:12 namespace.yaml
[root@m-k8s 5.2.2]#
[root@m-k8s 5.2.2]# ./kustomize-install.sh
 % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current</p>
<pre><code>                            Dload  Upload   Total   Spent    Left  Speed</code></pre><p> 0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 12.4M  100 12.4M    0     0  26.0M      0 --:--:-- --:--:-- --:--:-- 26.0M
kustomize install successfully</p>
<pre><code></code></pre></li>
<li><p>Step 2. 'Kustomize'에서 '리소스 및 주소 할당 영역(Pool)'을 구성할 때 사용할 '파일들(yaml)' 확인</p>
<p>```
[root@m-k8s 5.2.2]# cd /usr/local/bin
[root@m-k8s bin]#
[root@m-k8s bin]# ls -l
total 46708</p>
</li>
<li><p>rwxr-xr-x. 1 root root  7229744 Jan  3  2021 bpytop</p>
</li>
<li><p>rwxr-xr-x. 1 root root 40595456 May 28  2020 kustomize</p>
<pre><code></code></pre></li>
<li><p>Step 3. 'Kustomize'로 변경될 작업을 정의</p>
<ul>
<li><p>'Kustomize'로 변경될 작업을 정의하기 위해서 다음과 같은 명령으로 'kustomization.yaml' 생성한다.</p>
</li>
<li><p>'--resources'는 'Kustomize' 명령을 이용해서 'kustomization.yaml'를 만들기 위한 소스 파일을 정의한다.</p>
<ul>
<li>'--namespace'는 작업의 'Namespace'를 설정한다.</li>
</ul>
<p>```
[root@m-k8s 5.2.2]# kustomize create --namespace=metallb-system --resources namespace.yaml,metallb.yaml,metallb-l2config.yaml
[root@m-k8s 5.2.2]#
[root@m-k8s 5.2.2]# ls -l
total 24</p>
</li>
<li><p>rw-r--r--. 1 root root  157 Dec 22 11:58 kustomization.yaml</p>
</li>
<li><p>rwx------. 1 root root  261 Dec 22 11:12 kustomize-install.sh</p>
</li>
<li><p>rw-r--r--. 1 root root  223 Dec 22 11:12 metallb-l2config.yaml</p>
</li>
<li><p>rw-r--r--. 1 root root 5384 Dec 22 11:12 metallb.yaml</p>
</li>
<li><p>rw-r--r--. 1 root root   90 Dec 22 11:12 namespace.yaml
[root@m-k8s 5.2.2]#
[root@m-k8s 5.2.2]# kubectl get namespace
NAME              STATUS   AGE
default           Active   44m
kube-node-lease   Active   44m
kube-public       Active   44m
kube-system       Active   44m</p>
<pre><code></code></pre></li>
</ul>
</li>
<li><p>Step 4. 생성한 파일 'kustomization.yaml' 내용 확인</p>
<pre><code class="language-yaml">[root@m-k8s 5.2.2]# cat kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- namespace.yaml
- metallb.yaml
- metallb-l2config.yaml
namespace: metallb-system</code></pre>
</li>
<li><p>Step 5. 설치된 이미지를 안정적인 버전으로 유지</p>
<ul>
<li>설치된 이미지를 안정적인 버전으로 유지하기 위해서 태그를 ‘v0.8.2’로 지정한다.</li>
</ul>
<pre><code>[root@m-k8s 5.2.2]# kustomize edit set image metallb/controller:v0.8.2
[root@m-k8s 5.2.2]#
[root@m-k8s 5.2.2]# kustomize edit set image metallb/speaker:v0.8.2</code></pre></li>
<li><p>Step 6. 'kustomization.yaml' 내용 확인</p>
<pre><code class="language-yaml">[root@m-k8s 5.2.2]# cat kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- namespace.yaml
- metallb.yaml
- metallb-l2config.yaml
namespace: metallb-system
images:
- name: metallb/controller
newTag: v0.8.2
- name: metallb/speaker
newTag: v0.8.2</code></pre>
</li>
<li><p>Step 7. 'MetalLB' 설치를 위한 'Manifest' 생성</p>
<ul>
<li><p><code>kustomize build</code></p>
<pre><code>  [root@m-k8s 5.2.2]# nl metallb-l2config.yaml
       1  apiVersion: v1
       2  kind: ConfigMap
       3  metadata:
       4    namespace: metallb-system
       5    name: config
       6  data:
       7    config: |
       8      address-pools:
       9      - name: metallb-ip-range
      10        protocol: layer2
      11        addresses:
      12        - 192.168.1.11-192.168.1.19
  [root@m-k8s 5.2.2]#
  [root@m-k8s 5.2.2]# kustomize build
  apiVersion: v1
  kind: Namespace
  metadata:
    labels:
      app: metallb
    name: metallb-system
  ---
  apiVersion: v1
  kind: ServiceAccount
  metadata:
    labels:
      app: metallb
    name: controller
    namespace: metallb-system
  ---
  apiVersion: v1
  kind: ServiceAccount
  metadata:
    labels:
      app: metallb
    name: speaker
    namespace: metallb-system
  ---
  apiVersion: policy/v1beta1
  kind: PodSecurityPolicy
  metadata:
    labels:
      app: metallb
    name: speaker
    namespace: metallb-system
  spec:
    allowPrivilegeEscalation: false
    allowedCapabilities:
    - NET_ADMIN
    - NET_RAW
    - SYS_ADMIN
    fsGroup:
      rule: RunAsAny
    hostNetwork: true
    hostPorts:
    - max: 7472
      min: 7472
    privileged: true
    runAsUser:
      rule: RunAsAny
    seLinux:
      rule: RunAsAny
    supplementalGroups:
      rule: RunAsAny
    volumes:
    - '*'
  ---
  apiVersion: rbac.authorization.k8s.io/v1
  kind: Role
  metadata:
    labels:
      app: metallb
    name: config-watcher
    namespace: metallb-system
  rules:
  - apiGroups:
    - &quot;&quot;
    resources:
    - configmaps
    verbs:
    - get
    - list
    - watch
  ---
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRole
  metadata:
    labels:
      app: metallb
    name: metallb-system:controller
  rules:
  - apiGroups:
    - &quot;&quot;
    resources:
    - services
    verbs:
    - get
    - list
    - watch
    - update
  - apiGroups:
    - &quot;&quot;
    resources:
    - services/status
    verbs:
    - update
  - apiGroups:
    - &quot;&quot;
    resources:
    - events
    verbs:
    - create
    - patch
  ---
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRole
  metadata:
    labels:
      app: metallb
    name: metallb-system:speaker
  rules:
  - apiGroups:
    - &quot;&quot;
    resources:
    - services
    - endpoints
    - nodes
    verbs:
    - get
    - list
    - watch
  - apiGroups:
    - &quot;&quot;
    resources:
    - events
    verbs:
    - create
    - patch
  - apiGroups:
    - extensions
    resourceNames:
    - speaker
    resources:
    - podsecuritypolicies
    verbs:
    - use
  ---
  apiVersion: rbac.authorization.k8s.io/v1
  kind: RoleBinding
  metadata:
    labels:
      app: metallb
    name: config-watcher
    namespace: metallb-system
  roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: Role
    name: config-watcher
  subjects:
  - kind: ServiceAccount
    name: controller
    namespace: metallb-system
  - kind: ServiceAccount
    name: speaker
    namespace: metallb-system
  ---
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRoleBinding
  metadata:
    labels:
      app: metallb
    name: metallb-system:controller
  roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: ClusterRole
    name: metallb-system:controller
  subjects:
  - kind: ServiceAccount
    name: controller
    namespace: metallb-system
  ---
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRoleBinding
  metadata:
    labels:
      app: metallb
    name: metallb-system:speaker
  roleRef:
    apiGroup: rbac.authorization.k8s.io
    kind: ClusterRole
    name: metallb-system:speaker
  subjects:
  - kind: ServiceAccount
    name: speaker
    namespace: metallb-system
  ---
  apiVersion: v1
  data:
    config: |
      address-pools:
      - name: metallb-ip-range
        protocol: layer2
        addresses:
        - 192.168.1.11-192.168.1.19
  kind: ConfigMap
  metadata:
    name: config
    namespace: metallb-system
  ---
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    labels:
      app: metallb
      component: controller
    name: controller
    namespace: metallb-system
  spec:
    revisionHistoryLimit: 3
    selector:
      matchLabels:
        app: metallb
        component: controller
    template:
      metadata:
        annotations:
          prometheus.io/port: &quot;7472&quot;
          prometheus.io/scrape: &quot;true&quot;
        labels:
          app: metallb
          component: controller
      spec:
        containers:
        - args:
          - --port=7472
          - --config=config
          image: quay.io/metallb/controller:v0.8.2
          imagePullPolicy: IfNotPresent
          name: controller
          ports:
          - containerPort: 7472
            name: monitoring
          resources:
            limits:
              cpu: 100m
              memory: 100Mi
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              drop:
              - all
            readOnlyRootFilesystem: true
        nodeSelector:
          beta.kubernetes.io/os: linux
        securityContext:
          runAsNonRoot: true
          runAsUser: 65534
        serviceAccountName: controller
        terminationGracePeriodSeconds: 0
  ---
  apiVersion: apps/v1
  kind: DaemonSet
  metadata:
    labels:
      app: metallb
      component: speaker
    name: speaker
    namespace: metallb-system
  spec:
    selector:
      matchLabels:
        app: metallb
        component: speaker
    template:
      metadata:
        annotations:
          prometheus.io/port: &quot;7472&quot;
          prometheus.io/scrape: &quot;true&quot;
        labels:
          app: metallb
          component: speaker
      spec:
        containers:
        - args:
          - --port=7472
          - --config=config
          env:
          - name: METALLB_NODE_NAME
            valueFrom:
              fieldRef:
                fieldPath: spec.nodeName
          - name: METALLB_HOST
            valueFrom:
              fieldRef:
                fieldPath: status.hostIP
          image: quay.io/metallb/speaker:v0.8.2
          imagePullPolicy: IfNotPresent
          name: speaker
          ports:
          - containerPort: 7472
            name: monitoring
          resources:
            limits:
              cpu: 100m
              memory: 100Mi
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              add:
              - NET_ADMIN
              - NET_RAW
              - SYS_ADMIN
              drop:
              - ALL
            readOnlyRootFilesystem: true
        hostNetwork: true
        nodeSelector:
          beta.kubernetes.io/os: linux
        serviceAccountName: speaker
        terminationGracePeriodSeconds: 0
        tolerations:
        - effect: NoSchedule
          key: node-role.kubernetes.io/master
</code></pre></li>
</ul>
</li>
<li><p>Step 8. 명령을 위한 배포</p>
<ul>
<li><p><code>kustomize build | kubectl apply -f -</code></p>
<pre><code>  [root@m-k8s 5.2.2]# kustomize build | kubectl apply -f -
  namespace/metallb-system created
  serviceaccount/controller created
  serviceaccount/speaker created
  podsecuritypolicy.policy/speaker created
  role.rbac.authorization.k8s.io/config-watcher created
  clusterrole.rbac.authorization.k8s.io/metallb-system:controller created
  clusterrole.rbac.authorization.k8s.io/metallb-system:speaker created
  rolebinding.rbac.authorization.k8s.io/config-watcher created
  clusterrolebinding.rbac.authorization.k8s.io/metallb-system:controller created
  clusterrolebinding.rbac.authorization.k8s.io/metallb-system:speaker created
  configmap/config created
  deployment.apps/controller created
  daemonset.apps/speaker created</code></pre></li>
</ul>
</li>
<li><p>Step 9. 'MetalLB'가 정상적으로 배포되었는지 확인</p>
<pre><code>[root@m-k8s 5.2.2]# kubectl get namespaces
NAME              STATUS   AGE
default           Active   62m
kube-node-lease   Active   62m
kube-public       Active   62m
kube-system       Active   62m
metallb-system    Active   2m11s
[root@m-k8s 5.2.2]# kubectl get pods -n metallb-system
NAME                          READY   STATUS    RESTARTS   AGE
controller-5d48db7f99-m2sxd   1/1     Running   0          3m19s
speaker-2hlwj                 1/1     Running   0          3m19s
speaker-r59lm                 1/1     Running   0          3m19s
speaker-v6zdh                 1/1     Running   0          3m19s
speaker-w6hmv                 1/1     Running   0          3m19
[root@m-k8s 5.2.2]# kubectl get configmap -n metallb-system
NAME     DATA   AGE
config   1      4m55
[root@m-k8s 5.2.2]# kubectl get pods -o wide -n metallb-system
NAME                          READY   STATUS    RESTARTS   AGE     IP               NODE     NOMINATED NODE   READINESS GATES
controller-5d48db7f99-m2sxd   1/1     Running   0          5m46s   172.16.103.129   w2-k8s   &lt;none&gt;           &lt;none&gt;
speaker-2hlwj                 1/1     Running   0          5m46s   192.168.1.101    w1-k8s   &lt;none&gt;           &lt;none&gt;
speaker-r59lm                 1/1     Running   0          5m46s   192.168.1.102    w2-k8s   &lt;none&gt;           &lt;none&gt;
speaker-v6zdh                 1/1     Running   0          5m46s   192.168.1.10     m-k8s    &lt;none&gt;           &lt;none&gt;
speaker-w6hmv                 1/1     Running   0          5m46s   192.168.1.103    w3-k8s   &lt;none&gt;           &lt;none&gt;</code></pre></li>
<li><p>Step 10. 'Kustomize'를 통해 고정 값으로 적용한 'MetalLB'의 태그 확인</p>
<pre><code>[root@m-k8s 5.2.2]# kubectl describe pods -n metallb-system | grep Image:
  Image:         quay.io/metallb/controller:v0.8.2
  Image:         quay.io/metallb/speaker:v0.8.2
  Image:         quay.io/metallb/speaker:v0.8.2
  Image:         quay.io/metallb/speaker:v0.8.2
  Image:         quay.io/metallb/speaker:v0.8.2</code></pre></li>
<li><p>Step 11. 테스트</p>
<ul>
<li>‘Deployment 1개’를 배포한 다음 ‘LoadBalancer’ 타입으로 노출하고 IP가 정상적으로 할당되었는지 확인</li>
</ul>
<pre><code>[root@m-k8s 5.2.2]# kubectl create deployment echo-ip --image=sysnet4admin/echo-ip
deployment.apps/echo-ip created
[root@m-k8s 5.2.2]#
[root@m-k8s 5.2.2]# kubectl expose deployment echo-ip --type=LoadBalancer --port=80
service/echo-ip exposed
[root@m-k8s 5.2.2]# kubectl get deployment
NAME      READY   UP-TO-DATE   AVAILABLE   AGE
echo-ip   1/1     1            1           5m24s
[root@m-k8s 5.2.2]#
[root@m-k8s 5.2.2]# kubectl get deployment -A
NAMESPACE        NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
default          echo-ip                   1/1     1            1           5m45s
kube-system      calico-kube-controllers   1/1     1            1           90m
kube-system      coredns                   2/2     2            2           90m
metallb-system   controller                1/1     1            1           29m
[root@m-k8s 5.2.2]# kubectl get service echo-ip
NAME      TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)        AGE
echo-ip   LoadBalancer   10.108.76.151   192.168.1.11   80:30986/TCP   15m
[root@m-k8s 5.2.2]# kubectl get deployment echo-ip
NAME      READY   UP-TO-DATE   AVAILABLE   AGE
echo-ip   1/1     1            1           38m
[root@m-k8s 5.2.2]# kubectl get pods -o wide
NAME                       READY   STATUS    RESTARTS   AGE    IP             NODE     NOMINATED NODE   READINESS GATES
echo-ip-7b59cf5f9d-78zbs   1/1     Running   0          151m   172.16.132.1   w3-k8s   &lt;none&gt;           &lt;none&gt;
</code></pre></li>
<li><p>Step 12. 웹브라우저를 통한 ‘echo-ip’ 응답 확인</p>
<ul>
<li><p>‘<a href="http://192.168.1.11%E2%80%99">http://192.168.1.11’</a> 입력 후 응답 확인</p>
<ul>
<li><p>'Host OS'의 웹 브라우저에서 출력되는 화면의 'ip_dest'의 'IP'를 보면 'kubectl get pods -o wide'에서의 'IP'와 동일하다는 것을 알 수 있다.</p>
</li>
<li><p>즉, 'echo-ip-7b59cf5f9d-78zbs' Pod에 정상적으로 접속을 하고 있다는 것을 알 수 있다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/43d28e74-981e-48b3-926f-bce3480dcd41/image.png" /></p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code>        ![](https://velog.velcdn.com/images/kyk02405/post/6edf97db-616b-432b-a4a9-35d56da89a11/image.png)


- Step 13. 다음 작업을 위해 ‘MetalLB’와 ‘Deployment’를 모두 삭제한다.
    - 코드

        ```
        [root@m-k8s 5.2.2]# kustomize build | kubectl delete -f -
        namespace &quot;metallb-system&quot; deleted
        serviceaccount &quot;controller&quot; deleted
        serviceaccount &quot;speaker&quot; deleted
        podsecuritypolicy.policy &quot;speaker&quot; deleted
        role.rbac.authorization.k8s.io &quot;config-watcher&quot; deleted
        clusterrole.rbac.authorization.k8s.io &quot;metallb-system:controller&quot; deleted
        clusterrole.rbac.authorization.k8s.io &quot;metallb-system:speaker&quot; deleted
        rolebinding.rbac.authorization.k8s.io &quot;config-watcher&quot; deleted
        clusterrolebinding.rbac.authorization.k8s.io &quot;metallb-system:controller&quot; deleted
        clusterrolebinding.rbac.authorization.k8s.io &quot;metallb-system:speaker&quot; deleted
        configmap &quot;config&quot; deleted
        deployment.apps &quot;controller&quot; deleted
        daemonset.apps &quot;speaker&quot; deleted
        [root@m-k8s 5.2.2]#
        [root@m-k8s 5.2.2]# kubectl delete service echo-ip
        service &quot;echo-ip&quot; deleted
        [root@m-k8s 5.2.2]#
        [root@m-k8s 5.2.2]# kubectl delete deployment echo-ip
        deployment.apps &quot;echo-ip&quot; deleted

        ```</code></pre><h3 id="helm으로-배포-간편화하기">‘Helm’으로 배포 간편화하기</h3>
<ul>
<li><p>개요</p>
<ul>
<li>'Kustomize'를 이용하면 'MetalLB'의 다양한 설정을 '사용자의 입맛에 맛게' 변경하고 구성, 구현할 수 있다.</li>
<li>그러나 'Kustomize'는 여러 가지 변경할 부분을 사용자가 직접 'kustomization.yaml'에 추가하고 최종적으로 필요한 'Manifest'를 만들어 배포해야 한다.</li>
<li>이러한 다소 수동적인 작성 방식이 아닌 선언적으로 필요한 내용을 제공하고 이에 맞게 바로 배포하려면 어떻게 해야 할까요?</li>
<li>그리고 'Kustomize'를 뚱해서 변경할 수 없었던 주소 할당 영역과 같은 값도 배포 시에 같이 변경하려면 어떻게 할까요?</li>
<li>'Helm'은 이러한 제약 사항들을 없애고 편리성을 높일 수 있다.</li>
</ul>
</li>
<li><p>‘Helm’의 작동 원리</p>
<ul>
<li>컨테이너 인프라 환경에서 'Application'을 배포하려면 'ConfigMap', 'ServiceAccount', 'PV', 'PVC', 'Secret' 등 'Application' 배포 구성에 필요한 모든 'Kubernetes' 'Object'를 작성하고, 'kubectl' 명령을 실행해서 'Kubernetes' 클러스터에 설치해야 한다.</li>
<li>이때 'Kustomize'를 사용하면 많은 부분을 환경에 맞춰 변경할 수 있지만, 주소 할당 영역과 같은 정보는 값의 형태가 아니라서 변경할 수가 없다.</li>
<li>이런 경우에 'Helm'을 사용하면 주소 할당 영역도 변경이 가능하다.</li>
</ul>
</li>
<li><p>실습 2. ‘Helm’으로 ‘MetalLB’ 한 번에 만들기</p>
<ul>
<li><p>Step 1. ‘Helm’ 설치</p>
<pre><code>[root@m-k8s 5.2.3]# export DESIRED_VERSION=v3.2.1; ./helm-install.sh
Downloading https://get.helm.sh/helm-v3.2.1-linux-amd64.tar.gz
Verifying checksum... Done.
Preparing to install helm into /usr/local/bin
helm installed into /usr/local/bin/helm
[root@m-k8s 5.2.3]# echo $DESIRED_VERSION
v3.2.1</code></pre></li>
<li><p>Step 2.  'MetalLB' 설치를 위한 'Helm Chart' 등록을 위한 주소 확인</p>
<ul>
<li>'MetlLB'를 설치하려면 'Helm Chart'를 '등록할 주소'를 알아야 한다</li>
<li>'아티팩트허브'의 주소 '<a href="https://artifacthub.io/">https://artifacthub.io</a>'에서 'metallb'를 검색해 주소를 확인한다.</li>
</ul>
</li>
<li><p>Step 3. ‘MetalLB’ 설치를 위한 헬름 차트 확인</p>
<p>  <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/401db513-5c16-44fb-a059-0d593f3eb4cb/image.png" /></p>
</li>
</ul>
</li>
</ul>
<pre><code>- Step 4. ‘차트 저장소(helm-charts)’ 확인
    - 'MetalLB'의 상세 페이지에는 '차트 저장소(helm-charts)' 등록하는 방법과 차트에 대한 다양한 정보를 함께 제공하고 있다.
    - 상세 페이지를 통해서 추가해야 하는 차트 주소 및 등록하는 방법도 함께 확인할 수 있다

![](https://velog.velcdn.com/images/kyk02405/post/cf1d7cc2-2cb1-473d-a03f-1a11384d1134/image.png)


- Step 5. 저장소 등록

```
[root@m-k8s 5.2.3]# helm repo add edu https://iac-source.github.io/helm-charts
&quot;edu&quot; has been added to your repositories
```

- Step 6. 정상적으로 등록된 ‘helm-chart’ 저장소를 확인한다.

```
[root@m-k8s 5.2.3]# helm repo list
NAME    URL
edu     https://iac-source.github.io/helm-charts
```

- Step 7. 최신 Chart. 정보로 동기화

```
[root@m-k8s 5.2.3]# helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the &quot;edu&quot; chart repository
Update Complete. ⎈ Happy Helming!⎈
```

- Step 8. 등록 및 업데이트한 저장소인 ‘edu’를 통해 ‘MetalLB’ 설치

```
[root@m-k8s 5.2.3]# helm install metallb edu/metallb \
&gt; --namespace=metallb-system \
&gt; --create-namespace \
&gt; --set controller.tag=v0.8.3 \
&gt; --set speaker.tag=v0.8.3 \
&gt; --set configmap.ipRange=192.168.1.11-192.168.1.29
NAME: metallb
LAST DEPLOYED: Mon Dec 22 16:36:49 2025
NAMESPACE: metallb-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
MetalLB load-balancer is successfully installed.
1 IP Address range 192.168.1.11-192.168.1.29 is available.
2 You can create a LoadBalancer service with following command below.
kubectl expose deployment [deployment-name] --type=LoadBalancer --name=[LoadBalancer-name] --port=[external port]   
```   

- Step 9. 설치된 ‘MetalLB’가 정상적인 상태인지 확인

```
[root@m-k8s 5.2.3]# kubectl get pods -n metallb-system
NAME                          READY   STATUS    RESTARTS   AGE
controller-56dbbb9fd8-845mm   1/1     Running   0          41s
speaker-jvb66                 1/1     Running   0          41s
speaker-psh9l                 1/1     Running   0          41s
speaker-rsj5r                 1/1     Running   0          41s
speaker-xjqx7                 1/1     Running   0          40s
```

- Step 10. 'Helm' 'set' 옵션을 통해서 변경된 'MetalLB'의 태그 버전을 확인

```
[root@m-k8s 5.2.3]# kubectl describe pods -n metallb-system | grep Image:
    Image:         quay.io/metallb/controller:v0.8.3
    Image:         quay.io/metallb/speaker:v0.8.3
    Image:         quay.io/metallb/speaker:v0.8.3
    Image:         quay.io/metallb/speaker:v0.8.3
    Image:         quay.io/metallb/speaker:v0.8.3
```

- Step 11. 테스트를 위해 ‘Deployment’ 1개’를 배포한 다음 ‘LoadBalancer’ 타입으로 노출하고 IP가 정상적으로 할당되었는지 확인한다.

```
[root@m-k8s 5.2.3]# kubectl create deployment echo-ip --image=sysnet4admin/echo-ip
deployment.apps/echo-ip created
[root@m-k8s 5.2.3]#
[root@m-k8s 5.2.3]# kubectl expose deployment echo-ip --type=LoadBalancer --port=80
service/echo-ip exposed
[root@m-k8s 5.2.3]#
[root@m-k8s 5.2.3]# kubectl get service echo-ip
NAME      TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)        AGE
echo-ip   LoadBalancer   10.107.85.129   192.168.1.11   80:30629/TCP   9s
```

- Step 12. 테스트

```
[root@m-k8s 5.2.3]# curl 192.168.1.11
request_method : GET | ip_dest: 172.16.103.130
```

![업로드중..](blob:https://velog.io/70085b08-a224-4259-9b3e-a86106229538)


- Step 13. 다음 작업을 위해 ‘MetalLB’만 남겨두고 ‘Deployment’, ‘Service’를 모두 삭제한다.

```
[root@m-k8s 5.2.3]# kubectl delete service echo-ip
service &quot;echo-ip&quot; deleted
[root@m-k8s 5.2.3]# kubectl delete deployment echo-ip
deployment.apps &quot;echo-ip&quot; deleted
```</code></pre><h3 id="helm으로-jenkins-설치하기">‘Helm’으로 ‘Jenkins’ 설치하기</h3>
<ul>
<li><p>개요</p>
<ul>
<li>'Helm' 실습 때 사용했던 차트 저장소 'edu'에는 앞으로 사용할 모든 'Application'이 차트로 등록돼 있다.</li>
<li>따라서 지금부터 진행하는 실습에서는 '차트 저장소'를 새로 등록하지 않고 바로 'Application'을 설치한다.</li>
</ul>
</li>
<li><p>Step 1. ‘레지스트리 Push’</p>
<ul>
<li><p>개요</p>
<ul>
<li><p>‘Jenkins’로 지속적인 통합을 진행하는 경우에는 컨테이너 이미지를 레지스트리에 Push를 해야 한다.</p>
</li>
<li><p>즉, 레지스트리에 등록해야 한다.</p>
</li>
<li><p>‘Docker’ 또는 ‘Kubernetes’에서의 레지스트리(Regisrty)’는 ‘Container Image’를 저장하는 위치 즉, ‘서버’를 말한다.</p>
</li>
<li><p><code>./create-registry.sh</code></p>
<pre><code>  [root@m-k8s 4.4.2]# ./create-registry.sh
  Generating a 4096 bit RSA private key
  ...................................................................................................++
  ....................................................................................................................................................++
  writing new private key to 'tls.key'
  -----
  Loaded plugins: fastestmirror
  Loading mirror speeds from cached hostfile
  epel/x86_64/metalink                                                 | 4.5 kB  00:00:00
   * epel: d2lzkl7pfhq30w.cloudfront.net
  base                                                                 | 3.6 kB  00:00:00
  docker-ce-stable                                                     | 3.5 kB  00:00:00
  extras                                                               | 2.9 kB  00:00:00
  kubernetes                                                           | 1.4 kB  00:00:00
  updates                                                              | 2.9 kB  00:00:00
  Resolving Dependencies
  --&gt; Running transaction check
  ---&gt; Package sshpass.x86_64 0:1.06-2.el7 will be installed
  --&gt; Finished Dependency Resolution

  Dependencies Resolved

  ============================================================================================
   Package              Arch                Version                 Repository           Size
  ============================================================================================
  Installing:
   sshpass              x86_64              1.06-2.el7              extras               21 k

  Transaction Summary
  ============================================================================================
  Install  1 Package

  Total download size: 21 k
  Installed size: 38 k
  Downloading packages:
  sshpass-1.06-2.el7.x86_64.rpm                                        |  21 kB  00:00:00
  Running transaction check
  Running transaction test
  Transaction test succeeded
  Running transaction
    Installing : sshpass-1.06-2.el7.x86_64                                                1/1
    Verifying  : sshpass-1.06-2.el7.x86_64                                                1/1

  Installed:
    sshpass.x86_64 0:1.06-2.el7

  Complete!
  Warning: Permanently added '192.168.1.101' (ECDSA) to the list of known hosts.
  Warning: Permanently added '192.168.1.102' (ECDSA) to the list of known hosts.
  Warning: Permanently added '192.168.1.103' (ECDSA) to the list of known hosts.
  Unable to find image 'registry:2' locally
  2: Pulling from library/registry
  44cf07d57ee4: Pull complete
  bbbdd6c6894b: Pull complete
  8e82f80af0de: Pull complete
  3493bf46cdec: Pull complete
  6d464ea18732: Pull complete
  Digest: sha256:a3d8aaa63ed8681a604f1dea0aa03f100d5895b6a58ace528858a7b332415373
  Status: Downloaded newer image for registry:2
  1ea9a2bc4ac9ef17e82e492c173376afb2828a918c2da1f049a2d79fbccd4a07
</code></pre></li>
</ul>
</li>
</ul>
</li>
<li><p>Step 2. 'NFS', 'PV(PersistentVolume)', 'PVC(PersistentVolumeClaim)’</p>
<ul>
<li>'Helm'으로 설치되는 'Jenkins'는 'Pod'에서 동작하는 'Application'이기 때문에 'PV'를 'Mount'하지 않으면 'Pod'가 다시 시작될 때 내부 불륨에 저장하는 모든 데이터가 삭제된다.</li>
<li>이를 방지하기 위해서 'Application'의 'PV'가 'NFS'를 통해 프로비저닝될 수 있게 'NFS' 디렉터리를 '/nfs_shared/jenkins'에 만들겠다.</li>
<li>미리 정의된 'nfs-exporter.sh jenkins'를 실행한다. 이 스크립트에는 'NFS'용 디벡터리률 만들고 이를 'NFS 서비스'로 생성하는 과정이 담겨 있다.</li>
<li>'Kubernetes'는 필요할 때 'PVC(PersistentVolumeClaim, 지속적으로 사용 가능한 불품 요청)'를 요청해 사용한다.</li>
<li>'PVC'를 사용하려면 'PV(PersistentVolumc, 지속적으로 사용 가능한 부품)'로 볼륨을 선언해아 한다.</li>
<li>간단하게 'PV'는 볼륨을 사용할 수 있게 준비하는 단계이고, 'PVC'는 준비된 볼륨에서 일정 공간을 할당받는 것을 말한다.</li>
<li>비유하면 'PV'는 요리사(관리자)가 피자를 굽는 것이고, 'PVC'는 손님(사용자)가 원하는 만큼의 피자를 접시에 담아 가져오는 것이다.</li>
</ul>
</li>
<li><p>Step 3. ‘UID’, ‘GID’</p>
</li>
</ul>
<pre><code>[root@m-k8s 5.3.1]# ls -n /nfs_shared
total 0</code></pre><ul>
<li>Step 4. 소유권 변경</li>
</ul>
<pre><code>[root@m-k8s 5.3.1]# chown 1000:1000 /nfs_shared/jenkins/</code></pre><ul>
<li>Step 5. ‘PV’와 ‘PVC’ 구성</li>
</ul>
<pre><code>[root@m-k8s 5.3.1]# kubectl apply -f ./jenkins-volume.yaml
persistentvolume/jenkins created
persistentvolumeclaim/jenkins created</code></pre><ul>
<li><p>Step 6. 젠킨스 설치</p>
<ul>
<li><p><code>./jenkins-install.sh</code></p>
<pre><code>  [root@m-k8s 5.3.1]# ./jenkins-install.sh
  NAME: jenkins
  LAST DEPLOYED: Mon Dec 22 18:01:15 2025
  NAMESPACE: default
  STATUS: deployed
  REVISION: 1
  NOTES:
  1. Get your 'admin' user password by running:
    printf $(kubectl get secret --namespace default jenkins -o jsonpath=&quot;{.data.jenkins-admin-password}&quot; | base64 --decode);echo
  2. Get the Jenkins URL to visit by running these commands in the same shell:
    NOTE: It may take a few minutes for the LoadBalancer IP to be available.
          You can watch the status of by running 'kubectl get svc --namespace default -w jenkins'
    export SERVICE_IP=$(kubectl get svc --namespace default jenkins --template &quot;{{ range (index .status.loadBalancer.ingress 0) }}{{ . }}{{ end }}&quot;)
    echo http://$SERVICE_IP:80/login

  3. Login with the password from step 1 and the username: admin

  4. Use Jenkins Configuration as Code by specifying configScripts in your values.yaml file, see documentation: http:///configuration-as-code and examples: https://github.com/jenkinsci/configuration-as-code-plugin/tree/master/demos

  For more information on running Jenkins on Kubernetes, visit:
  https://cloud.google.com/solutions/jenkins-on-container-engine
  For more information about Jenkins Configuration as Code, visit:
  https://jenkins.io/projects/jcasc/
</code></pre></li>
</ul>
</li>
<li><p>Step 7. 배포된 ‘Jenkins’가 외부에 접속할 수 있는 상태인지 확인</p>
</li>
</ul>
<pre><code>[root@m-k8s 5.3.1]# kubectl get deployments
NAME      READY   UP-TO-DATE   AVAILABLE   AGE
jenkins   1/1     1            1           2m16s
[root@m-k8s 5.3.1]# kubectl get service jenkins
NAME      TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)        AGE
jenkins   LoadBalancer   10.101.88.130   192.168.1.11   80:31869/TCP   3m59s</code></pre><ul>
<li>Step 8. Pod 상태 확인</li>
</ul>
<pre><code>[root@m-k8s 5.3.1]# kubectl get pod -o wide
NAME                       READY   STATUS    RESTARTS   AGE     IP              NODE    NOMINATED NODE   READINESS GATES
jenkins-76496d9db7-lnwrf   2/2     Running   0          4m49s   172.16.171.68   m-k8s   &lt;none&gt;           &lt;none&gt;
</code></pre><ul>
<li><p>Step 9. ‘yaml’ 파일 분석</p>
<ul>
<li><p><code>kubectl get node m-k8s -o yaml | nl</code></p>
<pre><code>     [root@m-k8s 5.3.1]# kubectl get node m-k8s -o yaml | nl
       1  apiVersion: v1
       2  kind: Node
       3  metadata:
       4    annotations:
       5      kubeadm.alpha.kubernetes.io/cri-socket: /var/run/dockershim.sock
       6      node.alpha.kubernetes.io/ttl: &quot;0&quot;
       7      projectcalico.org/IPv4Address: 192.168.1.10/24
       8      projectcalico.org/IPv4IPIPTunnelAddr: 172.16.171.64
       9      volumes.kubernetes.io/controller-managed-attach-detach: &quot;true&quot;
      10    creationTimestamp: &quot;2025-12-22T02:14:13Z&quot;
     ...
     290      kubeletVersion: v1.18.4
     291      machineID: d0cc7f8f61e348aba24d3920bbe02ce5
     292      operatingSystem: linux
     293      osImage: CentOS Linux 7 (Core)
     294      systemUUID: 887E87E2-95DA-4B0D-8794-9D25C61BBF22
</code></pre></li>
</ul>
</li>
</ul>