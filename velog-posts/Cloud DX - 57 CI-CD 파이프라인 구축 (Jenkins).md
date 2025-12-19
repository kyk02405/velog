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
<h2 id="82-컨테이너-인프라-환경에서의-cicd">8.2 컨테이너 인프라 환경에서의 CI/CD</h2>
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
<h2 id="83-jenkins젠킨스">8.3 Jenkins(젠킨스)</h2>
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
<h2 id="84-jenkins로-kubernetes-운영-환경-개선">8.4 Jenkins로 Kubernetes 운영 환경 개선</h2>