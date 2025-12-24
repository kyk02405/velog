# Cloud DX - 59 Grafana & Prometheus

- 📅 Published: Wed, 24 Dec 2025 09:05:37 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-59-Grafana-Prometheus)

<hr />
<h1 id="91-컨테이너-인프라-환경-모니터링하기">9.1 컨테이너 인프라 환경 모니터링하기</h1>
<h2 id="안정적인-운영을-완성하는-모니터링-개요">안정적인 운영을 완성하는 모니터링 개요</h2>
<ul>
<li><code>Jenkins</code>는 <code>Kubenetes</code>의 애플리케이션 빌드와 배포를 자동화해 컨테이너 환경에서
애플리케이션을 효율적으로 관리한다.</li>
<li>일반적으로 배포된 또는 배포되는 애플리케이션은 충분한 검증을 거친 상태이다.
예를 들어 노드에서 하드웨어(HW)적으로 문제가 생기거나 컨테이너 관점에서 가용하는
리소스보다 많은 요청이 발생해 문제가 생기는 경우 등이 있다.</li>
<li><code>상용 환경</code>에서는 다양한 <code>예외 상황</code>이 발생할 수 있기 때문에 오류가 발생한 경우 모니터링을 통해 빠르고 적절한 조치를 취해야 한다.</li>
<li>쿠버네티스 환경에서 이와 같은 모니터링 기능은 필수적인 내용이라 할 수 있다.</li>
<li>컨테이너 인프라 환경에서 가장 권장하는 모니터링 도구는 <code>Prometheus</code>와 <code>그라파나</code>이다.</li>
</ul>
<h2 id="컨테이너-인프라-환경-모니터링하기">컨테이너 인프라 환경 모니터링하기</h2>
<ul>
<li>개요<ul>
<li>모니터링을 본격적으로 진행하기 전에 모니터링이 어떤 것인지 간단히 살펴보도록 하겠다.</li>
<li>'m-k8s' 노드에서 'bpytop' 명령을 실행하면 다음 그림과 같이 시스템 상태 정보가 보인다.</li>
<li>화면에서 리소스의 상태 및 문제가 될 가능성이 있는 정보를 한눈에 파악할 수 있다.</li>
<li>그러나 'bpytop' 명령은 현재 노드에 대한 정보를 보여주기 때문에 다수의 노드로 구성된 클러스터 정보를 모두 표현하기는 어렵다.</li>
<li>따라서 이러한 정보를 수집하고 분류해서 따로 저장해야 할 필요가 있다.</li>
<li>대부분의 모니터링 도구는 '수집 → 통합 → 시각화' 구조로 되어 있다.</li>
<li>(핵심) 구축한 컨테이너 인프라 환경에서는 '모니터링 데이터'를 'Prometheus'로 수집하고 '수집한 정보를 한곳에 모아(통합)', 그라파나로 시각화한다.</li>
</ul>
</li>
</ul>
<hr />
<h1 id="92-prometheus로-모니터링-데이터-수집과-통합하기">9.2 ‘Prometheus’로 모니터링 데이터 수집과 통합하기</h1>
<h3 id="step-1-시스템-재구성">Step 1. 시스템 재구성</h3>
<h3 id="step-2-kubernetes에-prometheus를-설치하는데-필요한-사전-구성">Step 2. 'Kubernetes'에 'Prometheus'를 설치하는데 필요한 사전 구성</h3>
<h4 id="커스터마이즈로-배포-간편화하기-구성-root_book_k8sinfrach5522">커스터마이즈로 배포 간편화하기 구성 (/root/_Book_k8sInfra/ch5/5.2.2)</h4>
<pre><code class="language-bash">[root@m-k8s 5.2.2]# ./kustomize-install.sh
[root@m-k8s 5.2.2]# kustomize create --namespace=metallb-system --resources namespace.yaml,metallb.yaml,metallb-l2config.yaml
[root@m-k8s 5.2.2]# kustomize build | kubectl apply -f -  </code></pre>
<pre><code class="language-bash">[root@m-k8s 5.2.2]# kubectl get pods -n metallb-system
NAME                          READY   STATUS    RESTARTS   AGE
controller-5d48db7f99-c2nrc   1/1     Running   0          98s
speaker-7h5dg                 1/1     Running   0          81s
speaker-fvfl7                 1/1     Running   0          76s
speaker-kmwcf                 1/1     Running   0          61s
speaker-nbnbq                 1/1     Running   0          90s</code></pre>
<pre><code class="language-bash">[root@m-k8s 5.2.2]# kubectl get configmap -n metallb-system
NAME     DATA   AGE
config   1      184d
[root@m-k8s 5.2.2]# kubectl describe pods -n metallb-system | grep Image:
    Image:         quay.io/metallb/controller:v0.8.2
    Image:         quay.io/metallb/speaker:v0.8.2
    Image:         quay.io/metallb/speaker:v0.8.2
    Image:         quay.io/metallb/speaker:v0.8.2
    Image:         quay.io/metallb/speaker:v0.8.2</code></pre>
<h4 id="헬름으로-배포-간편화하기-구성-root_book_k8sinfrach5523">헬름으로 배포 간편화하기 구성 (/root/_Book_k8sInfra/ch5/5.2.3)</h4>