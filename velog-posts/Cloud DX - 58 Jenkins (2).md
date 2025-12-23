# Cloud DX - 58 Jenkins (2)

- 📅 Published: Tue, 23 Dec 2025 03:43:32 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-58-Jenkins-2)

<hr />
<h1 id="jenkins-agent-설정하기">‘Jenkins Agent’ 설정하기</h1>
<h2 id="시스템-구성">시스템 구성</h2>
<ol>
<li><p>이전에 실습했던 시스템 4대를 모두 삭제한다.
<code>(win10)# vagrant -f destroy</code></p>
</li>
<li><p>배포한 'a.zip' 파일을 'HashiCorp' 폴더 안에 압축해제한다.</p>
</li>
<li><p>'Vagrantfile'을 이용한 'Provisioning'을 진행하고 시스템을 구성한다.
<code>(win10)# vagrant up</code></p>
</li>
<li><p>도커 버전을 확인한다.</p>
<pre><code class="language-bash">(m-k8s)#kubectl get nodes -o wide
NAME     STATUS   ROLES    AGE   VERSION   INTERNAL-IP     EXTERNAL-IP   OS-IMAGE                KERNEL-VERSION                CONTAINER-RUNTIME
m-k8s    Ready    master   21m   v1.18.4   192.168.1.10    &lt;none&gt;        CentOS Linux 7 (Core)   3.10.0-1160.90.1.el7.x86_64   docker://18.9.9
w1-k8s   Ready    &lt;none&gt;   19m   v1.18.4   192.168.1.101   &lt;none&gt;        CentOS Linux 7 (Core)   3.10.0-1160.90.1.el7.x86_64   docker://18.9.9
w2-k8s   Ready    &lt;none&gt;   16m   v1.18.4   192.168.1.102   &lt;none&gt;        CentOS Linux 7 (Core)   3.10.0-1160.90.1.el7.x86_64   docker://18.9.9
w3-k8s   Ready    &lt;none&gt;   14m   v1.18.4   192.168.1.103   &lt;none&gt;        CentOS Linux 7 (Core)   3.10.0-1160.90.1.el7.x86_64   docker://18.9.9</code></pre>
</li>
</ol>
<h2 id="이미지-빌드">이미지 빌드</h2>
<ol start="5">
<li><p>배포한 'Dockerfile'의 내용을 확인한다.
<code>(m-k8s)# cat Dockerfile</code></p>
</li>
<li><p>'Dockerfile'로 컨테이너 이미지를 빌드한다.</p>
<pre><code class="language-bash">(m-k8s)# docker build -t multistage-img .
   ...
Successfully built 0a7639c896a5         → 빌드된 'multistage-img'의 'ID'
Successfully tagged multistage-img:latest</code></pre>
</li>
<li><p>빌드 이미지 용량을 확인한다.</p>
<pre><code class="language-bash">(m-k8s)# docker images | head -n 3
REPOSITORY                           TAG                 IMAGE ID            CREATED             SIZE
multistage-img                       latest              0a7639c896a5        2 minutes ago       148MB
&lt;none&gt;                               &lt;none&gt;              beec99834c08        2 minutes ago       615MB</code></pre>
</li>
<li><p>'댕글링 이미지'를 삭제한다. ('Dangling 이미지'는 'REPOSITORY' 필드에 'none'으로 되어 있는 이미지를 말한다.)</p>
<pre><code class="language-bash">(m-k8s)# docker rmi $(docker images -f dangling=true -q)
Deleted: sha256:beec99834c086e5da60836fa0cb904e5cc18b0960b97699862354e4529b0305f
Deleted: sha256:72cb995b76af943e1451ade35149adc60d763ef37a9e9a45574318762dc806eb
Deleted: sha256:d1f75a690ddef0d9a159da6bd4a9d2decba1fef35c80588574a90e7d6c0ec62b
Deleted: sha256:d7c5fb65092b241efe3c89bd08faf69c9c9e2f973433368e4e6507d5a07a63dc
Deleted: sha256:e37d0e1be9eef3988c38e5cd03310c1afa8d000a02a5d2d936d5ce8fd0d0ee0e
Deleted: sha256:32606ad9ad163004eb01d0775af6d0425712d9aa54987259f60385d7a5f5ede0
Deleted: sha256:32081055ef9959383f44f075d60435cf417df6e1225043f74dcc38c7b8492c48
Deleted: sha256:0555a197210ed5d35956fc5e791e094224bb35d7410282f9fbccd7695524e6ec</code></pre>
</li>
<li><p>'multistage-img'를 이용한 컨테이너 생성하고 빌드한 컨테이너가 잘 동작하는지 확인한다.</p>
<pre><code class="language-bash">(m-k8s)# docker run -d -p 60434:80 --name multistage-run --restart always multistage-img
512de55164ce6611e9ad505ffe63049c68cb0d81a0d8bb17989008b360e85340
(m-k8s)# curl 127.0.0.1:60434
src: 172.17.0.1 / dest: 127.0.0.1</code></pre>
<h2 id="kubernetes에서-컨테이너-이미지를-구동한다">'Kubernetes'에서 '컨테이너 이미지'를 구동한다.</h2>
</li>
<li><p>'Deployment Pod'를 생성한다.</p>
<pre><code class="language-bash">(m-k8s)# docker images multistage-img
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
multistage-img      latest              0a7639c896a5        16 minutes ago      148MB
(m-k8s)# kubectl create deployment failure1 --image=multistage-img
deployment.apps/failure1 created</code></pre>
</li>
<li><p>'호스트 시스템(m-k8s)'에 이미지가 있는데도 외부에서 이미지를 다운로드 하려고 하기 때문에 오류가 발생한다.</p>
<pre><code class="language-bash">(m-k8s)# [root@m-k8s ~]# kubectl get pods -w
NAME                        READY   STATUS             RESTARTS   AGE
failure1-6dc55db9d4-jpddx   0/1     ImagePullBackOff   0          2m42s
failure1-6dc55db9d4-jpddx   0/1     ErrImagePull       0          3m17s</code></pre>
</li>
<li><p>오류가 발생한 'Deployment Pod'를 삭제한다.</p>
<pre><code class="language-bash">(m-k8s)# kubectl delete deployment failure1
deployment.apps &quot;failure1&quot; deleted</code></pre>
</li>
</ol>
<h2 id="레지스트리registry-사설-이미지-생성-구성하기">레지스트리(Registry, 사설 이미지 생성) 구성하기</h2>
<ol start="13">
<li><p>'2.zip' 업로드 후 압축 파일 해제</p>
<pre><code class="language-bash">(m-k8s)# ls -l
-rw-r--r--. 1 root root 835 Jun 24 16:13 create-registry.sh
-rw-r--r--. 1 root root 334 Jun 24 16:13 remover.sh
-rw-r--r--. 1 root root 355 Jun 24 16:13 tls.csr</code></pre>
</li>
<li><p>'사설 도커 Registry' 만들기</p>
<pre><code class="language-bash">(m-k8s)# chmod 700 create-registry.sh remover.sh
(m-k8s)# ls -l
-rwx------. 1 root root 835 Jun 24 16:13 create-registry.sh
-rwx------. 1 root root 334 Jun 24 16:13 remover.sh
-rw-r--r--. 1 root root 355 Jun 24 16:13 tls.csr
(m-k8s)# [root@m-k8s ~]# ./create-registry.sh
Generating a 4096 bit RSA private key
...
6d464ea18732: Pull complete
Digest: sha256:a3d8aaa63ed8681a604f1dea0aa03f100d5895b6a58ace528858a7b332415373
Status: Downloaded newer image for registry:2
3fd87ac9be6a45b0ae6b850f068f8b9a5d92cffa0a81863062579e1883640d37</code></pre>
</li>
<li><p>생성한 'Registry Container' 정상 동작여부를 확인한다.</p>
<pre><code class="language-bash">(m-k8s)# docker ps -f name=registry
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                             NAMES
3fd87ac9be6a        registry:2          &quot;/entrypoint.sh /etc…&quot;   2 minutes ago       Up 2 minutes        5000/tcp, 0.0.0.0:8443-&gt;443/tcp   registry</code></pre>
</li>
<li><p>'사설 도커 Registry'에 등록 가능하도록 컨테이너 이미지의 이름을 변경한다.</p>
<pre><code class="language-bash">(m-k8s)# docker tag multistage-img 192.168.1.10:8443/multistage-img
(m-k8s)# docker images 192.168.1.10:8443/multistage-img
REPOSITORY                         TAG                 IMAGE ID            CREATED             SIZE
192.168.1.10:8443/multistage-img   latest              0a7639c896a5        About an hour ago   148MB</code></pre>
</li>
<li><p>'multistage-img'를 '사설 도커 Registry'에 등록한다.</p>
<pre><code class="language-bash">(m-k8s)# docker push 192.168.1.10:8443/multistage-img
The push refers to repository [192.168.1.10:8443/multistage-img]
ed44fba380ef: Pushed
1d834f05c29e: Pushed
b29380a5a354: Pushed
231bdbae9aea: Pushed
ba16d454860a: Pushed
1a5ede0c966b: Pushed
latest: digest: sha256:c08fee58e378fd0750c4ba618f76d8920fffa3d525b9b91cf17176d0e4ea3dd7 size: 1583</code></pre>
</li>
<li><p>이미지가 정상 동작하는지 확인한다. ('-k'는 '--insecure'로써 자체 서명 인증서를 사용한다는 말이다.)</p>
<pre><code class="language-bash">(m-k8s)# curl https://192.168.1.10:8443/v2/_catalog -k
{&quot;repositories&quot;:[&quot;multistage-img&quot;]}</code></pre>
</li>
<li><p>동일한 이미지임을 확인한다.</p>
<pre><code class="language-bash">(m-k8s)# docker images | grep multi
192.168.1.10:8443/multistage-img     latest              0a7639c896a5        About an hour ago   148MB
multistage-img                       latest              0a7639c896a5        About an hour ago   148MB</code></pre>
</li>
<li><p>'19'의 결과</p>
<ul>
<li>'호스트(m-k8s)'에 '다운로드(pull)' 한 '이미지(multistage-img)'와 'Registry'에 등록한 '이미지(192.168.1.10:8443/multistage-img)'는
동일한 이미지에 즉, 한 개의 이미지에 두 개의 이름이 지정되어 있다는 것을 알 수 있다.</li>
<li>이렇게 이미지를 'Registry'에 등록하게 되면 인터넷이 안 되어도 사용할 수 있는 환경을 구성할 수가 있다.</li>
</ul>
</li>
<li><p>호스트에 생성한 이미지를 삭제한다.</p>
<pre><code class="language-bash">(m-k8s)# docker rmi -f 0a76
Error response from daemon: conflict: unable to delete 0a7639c896a5 (cannot be forced) - image is being used
by running container 512de55164ce
(m-k8s)# docker ps -a | grep 512d
512de55164ce        multistage-img                      &quot;java -jar app-in-im…&quot;   About an hour ago   Up About an hour        
60434/tcp, 0.0.0.0:60434-&gt;80/tcp   multistage-run
(m-k8s)# docker ps | grep 512d
512de55164ce        multistage-img                    &quot;java -jar app-in-im…&quot;   About an hour ago   Up About an hour
60434/tcp, 0.0.0.0:60434-&gt;80/tcp   multistage-run
(m-k8s)# docker stop 512de55164ce
512de55164ce
(m-k8s)# docker ps | grep 512d
(m-k8s)# docker rmi -f 0a76
Untagged: 192.168.1.10:8443/multistage-img:latest
Untagged: 192.168.1.10:8443/multistage-   img@sha256:c08fee58e378fd0750c4ba618f76d8920fffa3d525b9b91cf17176d0e4ea3dd7
Untagged: multistage-img:latest
Deleted: sha256:0a7639c896a5b3bbb5fd584986568058303bf31aeeba1611a29c695c8f2f85f4
Deleted: sha256:afa0b83343cda2cca373ab372f87b8d89086592f2895abf5d42d2dd6a925a60a
Deleted: sha256:046e08f52a8a4156ca05162f4fc751be565612197378fcdf91269602d929432a
Deleted: sha256:58a3b3a88640ba45397413b52f76d36943db0e2f1e1485e6c79124e15b8c1c89
Deleted: sha256:8f689c228f75fea4f52cb8e61e79332f498d3b9ee9b9047499588a3c68895fc3
(m-k8s)# docker images | grep multistage
(m-k8s)# docker images | grep multi
(m-k8s)# rm -rf *</code></pre>
</li>
</ol>
<h2 id="kustomize를-이용한-metallbload-balancer-만들기">'Kustomize'를 이용한 'MetalLB(Load Balancer)' 만들기</h2>
<ol start="22">
<li>'b.zip' 파일을 압축해제한 후 작업한다.<pre><code class="language-bash">(m-k8s)# ls -l
-rw-r--r--. 1 root root  261 Jun 24 17:01 kustomize-install.sh
-rw-r--r--. 1 root root  223 Jun 24 17:01 metallb-l2config.yaml
-rw-r--r--. 1 root root 5384 Jun 24 17:01 metallb.yaml
-rw-r--r--. 1 root root   90 Jun 24 17:01 namespace.yaml</code></pre>
</li>
<li>'Kustomize' 명령 실행<pre><code class="language-bash">(m-k8s)# chmod 700 kustomize-install.sh
(m-k8s)# ls -l
-rwx------. 1 root root  261 Jun 24 17:01 kustomize-install.sh
-rw-r--r--. 1 root root  223 Jun 24 17:01 metallb-l2config.yaml
-rw-r--r--. 1 root root 5384 Jun 24 17:01 metallb.yaml
-rw-r--r--. 1 root root   90 Jun 24 17:01 namespace.yaml
(m-k8s)# ./kustomize-install.sh
 % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                Dload  Upload   Total   Spent    Left  Speed
 0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 12.4M  100 12.4M    0     0  9717k      0  0:00:01  0:00:01 --:--:-- 72.5M
kustomize install successfully
(m-k8s)# ls -l /usr/local/bin/ (사용자에 의해 설치된 프로그램들은 모두 이 경로에서 동작되도록 설정해야 한다.)
-rwxr-xr-x. 1 root root  7229744 Jan  3  2021 bpytop
-rwxr-xr-x. 1 root root 40595456 May 28  2020 kustomize</code></pre>
</li>
<li>'커스터마이징'을 위한 'yaml' 파일을 생성한다.<pre><code class="language-bash">(m-k8s)# kustomize create --namespace=metallb-system --resources namespace.yaml,metallb.yaml,metallb-l2config.yaml
(m-k8s)# ls -l
-rw-r--r--. 1 root root  157 Jun 24 17:08 kustomization.yaml
-rwx------. 1 root root  261 Jun 24 17:01 kustomize-install.sh
-rw-r--r--. 1 root root  223 Jun 24 17:01 metallb-l2config.yaml
-rw-r--r--. 1 root root 5384 Jun 24 17:01 metallb.yaml
-rw-r--r--. 1 root root   90 Jun 24 17:01 namespace.yaml
(m-k8s)# cat kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- namespace.yaml
- metallb.yaml
- metallb-l2config.yaml
namespace: metallb-system</code></pre>
</li>
<li>설치된 이미지를 안정적인 버전으로 유지하기 위해 'Controller'와 'Speaker'의 이미지 태그를 'v0.8.2'로 지정한다.<pre><code class="language-bash">(m-k8s)# kustomize edit set image metallb/controller:v0.8.2
(m-k8s)# kustomize edit set image metallb/speaker:v0.8.2
(m-k8s)# cat kustomization.yaml
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
<li>'MetalLB' 설치를 위한 '메니페스트(스펙)'를 생성한다.<pre><code class="language-bash">(m-k8s)# kustomize build
  ...
addresses:
     - 192.168.1.11-192.168.1.19
  ...
    image: quay.io/metallb/controller:v0.8.2
  ...
image: quay.io/metallb/speaker:v0.8.2
  ...</code></pre>
</li>
<li>빌드한 결과를 'kubectl apply'에 인자로 전달한다.<pre><code class="language-bash">(m-k8s)# kustomize build | kubectl apply -f -
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
daemonset.apps/speaker created</code></pre>
</li>
<li>'MetalLB'가 정상적으로 배포되었는지 확인한다.<pre><code class="language-bash">(m-k8s)# kubectl get pods -n metallb-system
NAME                          READY   STATUS    RESTARTS   AGE
controller-5d48db7f99-crb2n   1/1     Running   0          58s
speaker-99nvm                 1/1     Running   0          58s
speaker-djfn6                 1/1     Running   0          58s
speaker-f4v9f                 1/1     Running   0          58s
speaker-swk2x                 1/1     Running   0          58s
(m-k8s)# kubectl get configmap -n metallb-system
NAME     DATA   AGE
config   1      96s</code></pre>
</li>
<li>'Kustomize'를 통해 고정한 'MetalLB'의 태그를 확인한다.<pre><code class="language-bash">(m-k8s)# kubectl describe pods -n metallb-system | grep Image:
Image:         quay.io/metallb/controller:v0.8.2
Image:         quay.io/metallb/speaker:v0.8.2
Image:         quay.io/metallb/speaker:v0.8.2
Image:         quay.io/metallb/speaker:v0.8.2
Image:         quay.io/metallb/speaker:v0.8.2</code></pre>
</li>
<li>테스트를 위한 'Deployment Pod' 1개를 배포하고 'LoadBalancer' 타입으로 노출하고 IP가 정상적으로 할당되었는지 확인한다.<pre><code class="language-bash">(m-k8s)# kubectl create deployment echo-ip --image=sysnet4admin/echo-ip
deployment.apps/echo-ip created
(m-k8s)# kubectl expose deployment echo-ip --type=LoadBalancer --port=80
service/echo-ip exposed</code></pre>
</li>
<li>사이트를 출력하고 'echo-ip'가 정상적으로 응답하는지 확인한다.<pre><code class="language-bash">(m-k8s)# curl http://192.168.1.11
request_method : GET | ip_dest: 172.16.221.129</code></pre>
</li>
<li>'MetalLB'를 삭제하고 배포했던 'echo-ip'관련 'Object'들도 삭제한다.<pre><code class="language-bash">(m-k8s)# kustomize build | kubectl delete -f -
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
(m-k8s)# kubectl get services
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP    PORT(S)        AGE
echo-ip      LoadBalancer   10.104.148.146   192.168.1.11   80:32662/TCP   12m
kubernetes   ClusterIP      10.96.0.1        &lt;none&gt;         443/TCP        143m
(m-k8s)# kubectl delete service echo-ip
service &quot;echo-ip&quot; deleted
(m-k8s)# kubectl get services
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    &lt;none&gt;        443/TCP   145m
(m-k8s)# kubectl delete deployment echo-ip
deployment.apps &quot;echo-ip&quot; deleted
(m-k8s)# ls -l
-rw-r--r--. 1 root root  250 Jun 24 17:11 kustomization.yaml
-rwx------. 1 root root  261 Jun 24 17:01 kustomize-install.sh
-rw-r--r--. 1 root root  223 Jun 24 17:01 metallb-l2config.yaml
-rw-r--r--. 1 root root 5384 Jun 24 17:01 metallb.yaml
-rw-r--r--. 1 root root   90 Jun 24 17:01 namespace.yaml
(m-k8s)# rm -rf *</code></pre>
</li>
</ol>
<h2 id="helm으로-배포-간편화하기">'Helm'으로 배포 간편화하기</h2>
<ol start="33">
<li><p>'c.zip' 파일을 압축 해제한 후 'Helm'을 설치한다.</p>
<pre><code class="language-bash">(m-k8s)# ls -l
-rw-r--r--. 1 root root 11212 Jun 24 17:48 helm-install.sh
(m-k8s)# chmod 700 helm-install.sh
(m-k8s)# ls -l
-rwx------. 1 root root 11212 Jun 24 17:48 helm-install.sh
(m-k8s)# ./helm-install.sh
Downloading https://get.helm.sh/helm-true-linux-amd64.tar.gz
Verifying checksum... SHA sum of /tmp/helm-installer-guhSFM/helm-true-linux-amd64.tar.gz does not match. Aborting.
Failed to install helm
       For support, go to https://github.com/helm/helm.
(m-k8s)# export DESIRED_VERSION=v3.2.1; ./helm-install.sh
Downloading https://get.helm.sh/helm-v3.2.1-linux-amd64.tar.gz
Verifying checksum... Done.
Preparing to install helm into /usr/local/bin
helm installed into /usr/local/bin/helm</code></pre>
</li>
<li><p>'33'설명</p>
<ul>
<li>실행 파일을 실행하면 항상 최신 버전을 다운로드한 후 설치를 하게 된다.</li>
<li>오류를 최소화 하기 위해 'DESIRED_VERSION' 환경변수를 이용해서 특정 버전을 다운로드 한 후 설치하기 위함이다.</li>
</ul>
</li>
<li><p>'Helm Chart' 저장소 등록 및 저장소 목록을 확인한다.</p>
<pre><code class="language-bash">(m-k8s)# helm repo add edu https://iac-source.github.io/helm-charts
&quot;edu&quot; has been added to your repositories
(m-k8s)# helm repo list
NAME    URL
edu     https://iac-source.github.io/helm-charts</code></pre>
</li>
<li><p>'최신 Chart 정보를 동기화'를 진행한다.</p>
<pre><code class="language-bash">(m-k8s)# helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the &quot;edu&quot; chart repository
Update Complete. ⎈ Happy Helming!⎈</code></pre>
</li>
<li><p>스크립트를 이용해서 'Chart'를 설치한다.</p>
<pre><code class="language-bash">(m-k8s)# helm install metaolb edu/metallb \
&gt; --namespace=metallb-system \
&gt; --create-namespace \
&gt; --set controller.tag=v0.8.3 \
&gt; --set speaker.tag=v0.8.3 \
&gt; --set configmap.ipRange=192.168.1.11-192.168.1.29

NAME: metaolb
LAST DEPLOYED: Tue Jun 24 18:06:29 2025
NAMESPACE: metallb-system                  → 이것을 확인한다.
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
MetalLB load-balancer is successfully installed.
1. IP Address range 192.168.1.11-192.168.1.29 is available.      → 이것을 확인한다.
2. You can create a LoadBalancer service with following command below.
kubectl expose deployment [deployment-name] --type=LoadBalancer --name=[LoadBalancer-name] --port=[external port]</code></pre>
</li>
<li><p>'MetalLB'가 정상적인 상태인지 배포 상태를 확인한다.</p>
<pre><code class="language-bash">(m-k8s)# kubectl get pods -n metallb-system
NAME                          READY   STATUS    RESTARTS   AGE
controller-56dbbb9fd8-5dwk2   1/1     Running   0          2m51s
speaker-7qfqz                 1/1     Running   0          2m51s
speaker-c7vlb                 1/1     Running   0          2m51s
speaker-fwphp                 1/1     Running   0          2m51s
speaker-k2w5r                 1/1     Running   0          2m51s
(m-k8s)# kubectl get configmap -n metallb-system
NAME     DATA   AGE
config   1      3m17s</code></pre>
</li>
<li><p>'MetalLB' 태그 버전을 확인한다.</p>
<pre><code class="language-bash">(m-k8s)#  kubectl describe pods -n metallb-system | grep Image:
Image:         quay.io/metallb/controller:v0.8.3
Image:         quay.io/metallb/speaker:v0.8.3
Image:         quay.io/metallb/speaker:v0.8.3
Image:         quay.io/metallb/speaker:v0.8.3
Image:         quay.io/metallb/speaker:v0.8.3</code></pre>
</li>
<li><p>테스트를 위한 'Deployment Pod' 1개를 배포하고 'LoadBalancer' 타입으로 노출하고 IP가 정상적으로 할당되었는지 확인한다.</p>
<pre><code class="language-bash">(m-k8s)# kubectl create deployment echo-ip --image=sysnet4admin/echo-ip
deployment.apps/echo-ip created
(m-k8s)# kubectl expose deployment echo-ip --type=LoadBalancer --port=80
service/echo-ip exposed
(m-k8s)# kubectl get service echo-ip
NAME      TYPE           CLUSTER-IP       EXTERNAL-IP    PORT(S)        AGE
echo-ip   LoadBalancer   10.110.226.148   192.168.1.11   80:32264/TCP   13s   → 'IP'를 확인한다.</code></pre>
</li>
<li><p>사이트를 출력하고 'echo-ip'가 정상적으로 응답하는지 확인한다.</p>
<pre><code class="language-bash">(m-k8s)# curl http://192.168.1.11
request_method : GET | ip_dest: 172.16.221.130</code></pre>
</li>
</ol>
<h2 id="helm으로-jankins-설치하기">'Helm'으로 'Jankins' 설치하기</h2>
<ol start="42">
<li><p>컨테이너 이미지가 저장된 'Registry'에 등록된 내용을 확인한다.</p>
<pre><code class="language-bash">(m-k8s)# docker ps -f name=registry
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                             NAMES
3fd87ac9be6a        registry:2          &quot;/entrypoint.sh /etc…&quot;   2 hours ago         Up 2 hours          5000/tcp, 0.0.0.0:8443-&gt;443/tcp   registry</code></pre>
</li>
<li><p>'e.zip' 파일을 압축 해제한 후 'NFS' 관련 작업을 한다.</p>
<pre><code class="language-bash">(m-k8s)# rm -rf *
(m-k8s)# ls -l
-rw-r--r--. 1 root root 3419 Jun 25 09:31 jenkins-config.yaml
-rw-r--r--. 1 root root  905 Jun 25 09:31 jenkins-install.sh
-rw-r--r--. 1 root root  402 Jun 25 09:31 jenkins-volume.yaml
-rw-r--r--. 1 root root  332 Jun 25 09:31 nfs-exporter.sh
(m-k8s)# chmod 700 *.sh
(m-k8s)# ls -l
-rw-r--r--. 1 root root 3419 Jun 25 09:31 jenkins-config.yaml
-rwx------. 1 root root  905 Jun 25 09:31 jenkins-install.sh
-rw-r--r--. 1 root root  402 Jun 25 09:31 jenkins-volume.yaml
-rwx------. 1 root root  332 Jun 25 09:31 nfs-exporter.sh
(m-k8s)# ./nfs-exporter.sh jenkins
Created symlink from /etc/systemd/system/multi-user.target.wants/nfs-server.service to /usr/lib/systemd/system/nfs-server.service.</code></pre>
</li>
<li><p>생성된 디렉터리의 상태를 확인한다.</p>
<pre><code class="language-bash">(m-k8s)# ls -n /nfs_shared/
drwxr-xr-x. 2 0 0 6 Jun 25 09:44 jenkins</code></pre>
</li>
<li><p>접근 권한 부여한다.</p>
<pre><code class="language-bash">(m-k8s)# ls -ld /nfs_shared/jenkins/
drwxr-xr-x. 2 root root 6 Jun 25 09:44 /nfs_shared/jenkins/
(m-k8s)# chown 1000:1000 /nfs_shared/jenkins/
(m-k8s)# ls -n /nfs_shared/
drwxr-xr-x. 2 1000 1000 6 Jun 25 09:44 jenkins</code></pre>
</li>
<li><p>'Jenkins' 'PV(Persistent Volume), PVC(Persistent Volume Claim)'를 구성하고 'Bound' 상태인지 확인한다.</p>
<pre><code class="language-bash">(m-k8s)# kubectl apply -f ./jenkins-volume.yaml
persistentvolume/jenkins created
persistentvolumeclaim/jenkins created
(m-k8s)# kubectl get pv jenkins
NAME      CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM             STORAGECLASS   REASON   AGE
jenkins   10Gi       RWX            Retain           Bound       default/jenkins                         43s
(m-k8s)# kubectl get pvc jenkins
NAME      STATUS   VOLUME    CAPACITY   ACCESS MODES   STORAGECLASS   AGE
jenkins   Bound    jenkins   10Gi       RWX                           49s</code></pre>
</li>
<li><p>'PV(Persistent(지속성) Volume), PVC(Persistent Volume Claim(요구))'</p>
<ul>
<li>'데이터(Conainer 기반의 'Deployment Pod')'를 저장하고 만약에 'Deployment Pod'가 재시작했을 때도 데이터를
정상적으로 즉, '지속적(Persistent)'으로 동작할 수 있도록 해 주는 기능</li>
</ul>
</li>
<li><p>'Jenkins'를 설치한다.</p>
<pre><code class="language-bash">(m-k8s)# ./jenkins-install.sh
NAME: jenkins
LAST DEPLOYED: Wed Jun 25 10:06:44 2025
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES:
...
(m-k8s)# kubectl get namespaces
NAME              STATUS   AGE
default           Active   18h
kube-node-lease   Active   18h
kube-public       Active   18h
kube-system       Active   18h
metallb-system    Active   16h</code></pre>
<p>49-1. (오류)'Jenkins'를 외부에 노출시키고 사이트에서 접속할 수 있도록 설정한다.</p>
<pre><code class="language-bash">(m-k8s)# kubectl get deployment
NAME      READY   UP-TO-DATE   AVAILABLE   AGE
echo-ip   0/1     1            0           15h
jenkins   0/1     1            0           3m12s
(m-k8s)# kubectl get service jenkins
NAME      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
jenkins   LoadBalancer   10.99.140.234   &lt;pending&gt;     80:32600/TCP   3m22s
(m-k8s)# kubectl get services
NAME            TYPE           CLUSTER-IP       EXTERNAL-IP    PORT(S)        AGE
echo-ip         LoadBalancer   10.110.226.148   192.168.1.11   80:32264/TCP   15h
jenkins         LoadBalancer   10.99.140.234    &lt;pending&gt;      80:32600/TCP   4m34s
jenkins-agent   ClusterIP      10.106.200.159   &lt;none&gt;         50000/TCP      4m34s
kubernetes      ClusterIP      10.96.0.1        &lt;none&gt;         443/TCP        18h
(m-k8s)# kubectl get deployment
NAME      READY   UP-TO-DATE   AVAILABLE   AGE
echo-ip   0/1     1            0           15h
jenkins   0/1     1            0           5m3s

(m-k8s)# kubectl get deployment
NAME      READY   UP-TO-DATE   AVAILABLE   AGE
echo-ip   0/1     1            0           16h
jenkins   0/1     1            0           7m18s
(m-k8s)# kubectl get pods
NAME                       READY   STATUS     RESTARTS   AGE
echo-ip-7b59cf5f9d-6gd7l   1/1     Running    0          16h
jenkins-76496d9db7-flkhh   0/2     Init:0/1   0          7m25s</code></pre>
<p>49-2. (해결) 'Jenkins'를 삭제하고 재설치한다.</p>
<pre><code class="language-bash">(m-k8s)# helm uninstall jenkins
release &quot;jenkins&quot; uninstalled
(m-k8s)# rm -rf /nfs_shared/jenkins/*
(m-k8s)# ls -l
-rw-r--r--. 1 root root 3419 Jun 25 09:31 jenkins-config.yaml
-rwx------. 1 root root  905 Jun 25 09:31 jenkins-install.sh
-rw-r--r--. 1 root root  402 Jun 25 09:31 jenkins-volume.yaml
-rwx------. 1 root root  332 Jun 25 09:31 nfs-exporter.sh
(m-k8s)# ./jenkins-install.sh</code></pre>
<p>49-3. (정상)'Jenkins'를 외부에 노출시키고 사이트에서 접속할 수 있도록 설정한다.</p>
<pre><code class="language-bash">(m-k8s)# kubectl get deployment
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
jenkins        1/1     1            1           2d16h
(m-k8s)# kubectl get services
NAME               TYPE           CLUSTER-IP       EXTERNAL-IP    PORT(S)          AGE
jenkins            LoadBalancer   10.107.207.103   192.168.1.11   80:30577/TCP     2d16h
jenkins-agent      ClusterIP      10.104.207.3     &lt;none&gt;         50000/TCP        2d16h
kubernetes         ClusterIP      10.96.0.1        &lt;none&gt;         443/TCP          3d10h</code></pre>
</li>
<li><p>'Jenkins' 사이트 출력</p>
<ul>
<li>'<a href="http://192.168.1.11/login'">http://192.168.1.11/login'</a></li>
</ul>
</li>
<li><p>'Pipeline Project' 생성을 위한 'Item' 추가</p>
<ul>
<li>'Jenkins' 메인 화면 상단에 있는 '새로운 Item'을 클릭한다.</li>
<li>'Enter an item name'에는 'dpy-pl-bulk-prod'라고 입력한다.</li>
<li>하단에 있는 'Pipeline'을 클릭한 후 'Ok'를 클릭한다.</li>
</ul>
</li>
<li><p>'구성'을 설정한다.</p>
<ul>
<li>생성된 'Pipeline Project' 목록에서 'dpy-pl-bulk-prod'을 클릭한다.</li>
<li>왼쪽에서 '구성'을 클릭한다.</li>
<li>'General'의 하단에 있는 '이 빌드는 매개변수가 있습니다'를 체크해제한다.</li>
<li>'Pipeline'에서 'Definition'을 'Pipeline Script'에서 'Pipeline script from SCM'으로 변경한다.</li>
<li>'SCM'을 'Git'으로 변경한다.</li>
<li>'Repository URL'에 '<a href="https://github.com/iac-source/echo-ip'%EB%A5%BC">https://github.com/iac-source/echo-ip'를</a> 입력한다.</li>
<li>'Branch Specifier (blank for 'any')'에서 '<em>/master'으로 '</em>/main'으로 변경한다.</li>
<li>하단에 있는 'Apply'와 '저장'을 순서대로 클릭한다.</li>
</ul>
</li>
<li><p>'Pipeline Project'를 빌드한다.</p>
<ul>
<li>'Pipeline Project' 화면 왼쪽에 있는 'Build Now'를 클릭한다.</li>
<li>'Build History' 하단에 '빌드 작업 중' 형태로 막대기가 움직이는 것을 확인한다.</li>
<li>'파란색' '#1'이 출력될 때까지 기다린다.</li>
</ul>
</li>
<li><p>'Pipeline Project'가 정상적으로 로딩되는지 확인한다.</p>
<pre><code class="language-bash">(m-k8s)# kubectl get deployment
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
jenkins        1/1     1            1           2d16h
pl-bulk-prod   1/1     1            1           2d14h
(m-k8s)# kubectl get services
NAME               TYPE           CLUSTER-IP       EXTERNAL-IP    PORT(S)          AGE
jenkins            LoadBalancer   10.107.207.103   192.168.1.11   80:30577/TCP     2d16h
jenkins-agent      ClusterIP      10.104.207.3     &lt;none&gt;         50000/TCP        2d16h
kubernetes         ClusterIP      10.96.0.1        &lt;none&gt;         443/TCP          3d10h
pl-bulk-prod-svc   LoadBalancer   10.107.241.78    192.168.1.12   8080:32335/TCP   2d14h</code></pre>
</li>
</ol>