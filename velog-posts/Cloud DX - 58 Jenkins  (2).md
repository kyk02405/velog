# Cloud DX - 58 Jenkins  (2)

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
<li>'2.zip' 업로드 후 압축 파일 해제 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2d6cc626-24ee-4d27-b241-95aeafac6fc6/image.png" /> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d8ad564b-9965-4756-a1d4-889cb8343e2c/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# ls -l
   -rw-r--r--. 1 root root 835 Jun 24 16:13 create-registry.sh
   -rw-r--r--. 1 root root 334 Jun 24 16:13 remover.sh
   -rw-r--r--. 1 root root 355 Jun 24 16:13 tls.csr</code></pre>
<ol start="14">
<li>'사설 도커 Registry' 만들기 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a3b8dc79-0299-447b-b7a1-90fd8808d09d/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# chmod 700 create-registry.sh remover.sh
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
<ol start="15">
<li>생성한 'Registry Container' 정상 동작여부를 확인한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c21e268b-0bfa-4119-b191-60fdb626b6c3/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# docker ps -f name=registry
   CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                             NAMES
   3fd87ac9be6a        registry:2          &quot;/entrypoint.sh /etc…&quot;   2 minutes ago       Up 2 minutes        5000/tcp, 0.0.0.0:8443-&gt;443/tcp   registry</code></pre>
<ol start="16">
<li>'사설 도커 Registry'에 등록 가능하도록 컨테이너 이미지의 이름을 변경한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/da10f1b5-6fee-4d4c-bbac-36c850fc71b6/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# docker tag multistage-img 192.168.1.10:8443/multistage-img
  (m-k8s)# docker images 192.168.1.10:8443/multistage-img
   REPOSITORY                         TAG                 IMAGE ID            CREATED             SIZE
   192.168.1.10:8443/multistage-img   latest              0a7639c896a5        About an hour ago   148MB</code></pre>
<ol start="17">
<li>'multistage-img'를 '사설 도커 Registry'에 등록한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4f473ead-06da-45b0-9a95-2ce2348f3b49/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# docker push 192.168.1.10:8443/multistage-img
   The push refers to repository [192.168.1.10:8443/multistage-img]
   ed44fba380ef: Pushed
   1d834f05c29e: Pushed
   b29380a5a354: Pushed
   231bdbae9aea: Pushed
   ba16d454860a: Pushed
   1a5ede0c966b: Pushed
   latest: digest: sha256:c08fee58e378fd0750c4ba618f76d8920fffa3d525b9b91cf17176d0e4ea3dd7 size: 1583</code></pre>
<ol start="18">
<li>이미지가 정상 동작하는지 확인한다. ('-k'는 '--insecure'로써 자체 서명 인증서를 사용한다는 말이다.) <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f702724e-1e66-4714-85ae-50a31c10be2a/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# curl https://192.168.1.10:8443/v2/_catalog -k
   {&quot;repositories&quot;:[&quot;multistage-img&quot;]}</code></pre>
<ol start="19">
<li>동일한 이미지임을 확인한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/323413d4-16de-4bfd-84e4-faa7905ed7eb/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# docker images | grep multi
   192.168.1.10:8443/multistage-img     latest              0a7639c896a5        About an hour ago   148MB
   multistage-img                       latest              0a7639c896a5        About an hour ago   148MB</code></pre>
<ol start="20">
<li><p>'19'의 결과</p>
<ul>
<li>'호스트(m-k8s)'에 '다운로드(pull)' 한 '이미지(multistage-img)'와 'Registry'에 등록한 '이미지(192.168.1.10:8443/multistage-img)'는
동일한 이미지에 즉, 한 개의 이미지에 두 개의 이름이 지정되어 있다는 것을 알 수 있다.</li>
<li>이렇게 이미지를 'Registry'에 등록하게 되면 인터넷이 안 되어도 사용할 수 있는 환경을 구성할 수가 있다.</li>
</ul>
</li>
<li><p>호스트에 생성한 이미지를 삭제한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e9935bbc-5f74-4a54-aa67-99bc34192c21/image.png" /></p>
</li>
</ol>
<pre><code class="language-bash">  (m-k8s)# docker rmi -f 0a76
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
<h2 id="kustomize를-이용한-metallbload-balancer-만들기">'Kustomize'를 이용한 'MetalLB(Load Balancer)' 만들기</h2>
<ol start="22">
<li>'b.zip' 파일을 압축해제한 후 작업한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/25416140-b7a5-4bc6-b3f3-fc25c06ab315/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7acfa9f6-cb0e-4939-8535-9b69dbd570dd/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# ls -l
   -rw-r--r--. 1 root root  261 Jun 24 17:01 kustomize-install.sh
   -rw-r--r--. 1 root root  223 Jun 24 17:01 metallb-l2config.yaml
   -rw-r--r--. 1 root root 5384 Jun 24 17:01 metallb.yaml
   -rw-r--r--. 1 root root   90 Jun 24 17:01 namespace.yaml</code></pre>
<ol start="23">
<li>'Kustomize' 명령 실행 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/03607a38-732b-420b-a5de-e508d35d6033/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# chmod 700 kustomize-install.sh
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
<ol start="24">
<li>'커스터마이징'을 위한 'yaml' 파일을 생성한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f13504ad-5110-4cc5-a343-77f426b422aa/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# kustomize create --namespace=metallb-system --resources namespace.yaml,metallb.yaml,metallb-l2config.yaml
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
<ol start="25">
<li>설치된 이미지를 안정적인 버전으로 유지하기 위해 'Controller'와 'Speaker'의 이미지 태그를 'v0.8.2'로 지정한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/84abda46-1e81-4645-804e-bc3679221676/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# kustomize edit set image metallb/controller:v0.8.2
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
<ol start="26">
<li>'MetalLB' 설치를 위한 '메니페스트(스펙)'를 생성한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3dd5c2d6-b54b-475a-9d85-30c01e8f46b9/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# kustomize build
      ...
   addresses:
         - 192.168.1.11-192.168.1.19
      ...
        image: quay.io/metallb/controller:v0.8.2
      ...
   image: quay.io/metallb/speaker:v0.8.2
      ...</code></pre>
<ol start="27">
<li>빌드한 결과를 'kubectl apply'에 인자로 전달한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/083b0986-d9e8-4b20-ac04-6b3065d8c050/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# kustomize build | kubectl apply -f -
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
<ol start="28">
<li>'MetalLB'가 정상적으로 배포되었는지 확인한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0e55253f-f82d-4fb9-9ffd-3af426c33e48/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# kubectl get pods -n metallb-system
   NAME                          READY   STATUS    RESTARTS   AGE
   controller-5d48db7f99-crb2n   1/1     Running   0          58s
   speaker-99nvm                 1/1     Running   0          58s
   speaker-djfn6                 1/1     Running   0          58s
   speaker-f4v9f                 1/1     Running   0          58s
   speaker-swk2x                 1/1     Running   0          58s
  (m-k8s)# kubectl get configmap -n metallb-system
   NAME     DATA   AGE
   config   1      96s</code></pre>
<ol start="29">
<li>'Kustomize'를 통해 고정한 'MetalLB'의 태그를 확인한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/91f86a28-f1bd-43a0-9732-2f02cd9e77b0/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# kubectl describe pods -n metallb-system | grep Image:
    Image:         quay.io/metallb/controller:v0.8.2
    Image:         quay.io/metallb/speaker:v0.8.2
    Image:         quay.io/metallb/speaker:v0.8.2
    Image:         quay.io/metallb/speaker:v0.8.2
    Image:         quay.io/metallb/speaker:v0.8.2</code></pre>
<ol start="30">
<li>테스트를 위한 'Deployment Pod' 1개를 배포하고 'LoadBalancer' 타입으로 노출하고 IP가 정상적으로 할당되었는지 확인한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5b8cc587-3657-4c09-9cbb-765b4dec828d/image.png" /></li>
</ol>
<pre><code class="language-bash">  (m-k8s)# kubectl create deployment echo-ip --image=sysnet4admin/echo-ip
   deployment.apps/echo-ip created
  (m-k8s)# kubectl expose deployment echo-ip --type=LoadBalancer --port=80
   service/echo-ip exposed</code></pre>
<ol start="31">
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
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8f619d05-bd72-436c-924d-b9bb69ed4ad8/image.png" /></p>
</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/13ac6d1d-38d0-4616-afb3-cdd3a28d2256/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d1403e51-2c5d-4344-a65b-b514ae1b2b4d/image.png" /></p>
<hr />
<h2 id="84-jenkins-plug-in을-통해-구현되는-gioops">8.4 ‘Jenkins Plug-in’을 통해 구현되는 ‘GioOps’</h2>
<h3 id="개요">개요</h3>
<ul>
<li>지금까지의 우리는 <code>Jenkins</code>를 이용해 <code>CI/CD</code>를 구성하는 방법을 알아봤다.  이러한 거의 모든 기능은 사실 <code>Jenkins</code>의 <code>Plug-in</code>을 통해 이루어진 것이다.</li>
<li>예를 들면 가장 많이 쓰였던 <code>Kubernetes Plug-in</code>은 <code>CI/CD</code>를 실제로 수행하는 <code>Jenkins Agent Pod</code>를 사용자가 신경쓰지 않아도 자동으로 배포 관리하게 해준다.<code>맥도날드</code>, <code>버거킹</code>에서의 <code>햄버거</code>를 생각하면 된다.</li>
<li>현업에서는 <code>Jenkins</code>의 단일 플러그인으로 <code>CI/CD</code>를 구성 하는 것이 아니라 여러 플러그인을 조합해 현재 업무에 맞는 형태로 만들어서 사용한다. <code>Subway 샌드위치</code>를 생각하면 된다.</li>
<li><code>Jenkins Plug-in</code>은 사용자에게 필요한 기능을 주로 <code>Jenkins 플러그인</code> <code>홈페이지(https://plugins.jenkins.io/)</code>에서 검색하고 내용을 살펴본 후 이를 조합하는 방식을 취한다.</li>
</ul>
<h3 id="jenkins-플러그인-browse-categories-종류">Jenkins 플러그인 Browse Categories` 종류</h3>
<ul>
<li><p>Platforms (OS)</p>
<ul>
<li><code>웹 애플리케이션</code>이 아닌 <code>다른 플랫폼</code>에서 작동하는 <code>애플리케이션 빌드</code>를 위한 플러그인</li>
</ul>
</li>
<li><p>User interface (기능이 보강된 대시보드)</p>
<ul>
<li><code>Jenkins</code>의 <code>기본 UI</code> 이외의 <code>확장  UI</code>를 적용하기 위한 플러그인</li>
</ul>
</li>
<li><p>Administration</p>
<ul>
<li><code>LDAP(조직 등에서 정보를 볼 수 있게 해주는 프로토콜, Lightweight Directory Access Protocol)</code>, <code>Jenkins 클러스터</code> 관리 등 Jenkins 자체 관리에 필요한 플러그인</li>
</ul>
</li>
<li><p>Build management</p>
<ul>
<li><code>CI/CD</code> 단계에서 추가적으로 사용할 수 있는 플러그인</li>
</ul>
</li>
<li><p>Source Code Management</p>
<ul>
<li>GitHub, GitLab과 같은 <code>소스 코드 저장소</code>의 연결이나 관리를 위한 플러그인</li>
</ul>
</li>
</ul>
<hr />
<h2 id="실습">실습</h2>
<h3 id="step-1-github-사이트에서-github-저장소repository-생성">Step 1. GitHub 사이트에서 GitHub 저장소(Repository) 생성</h3>
<h4 id="개요-1">개요</h4>
<ul>
<li>주기적으로 변화를 감지해야 하는 <code>GitHub 저장소</code>는 모드 같은 저장소를 공유할 수 없기 때문에 필요할 때마다 생성해야 한다.<ul>
<li><code>https://github.com/</code>에 로그인 후 화면 상단에 있는 <code>Repositories</code>를 클릭한다.</li>
<li>우측에 있는 <code>New</code>를 클릭한다.</li>
<li><code>Create a new repository</code> 화면에 있는 <code>Repository name</code>에 <code>GitOps</code>를 입력한다.</li>
<li><code>Choose visibility</code>에서 <code>Public</code>를 선택한다.</li>
<li>하단에 있는 <code>Create repository</code>를 클릭한다.</li>
</ul>
</li>
</ul>
<hr />
<h3 id="step-2-github-저장소-주소-복사">Step 2. 'GitHub 저장소 주소' 복사</h3>
<h4 id="개요-2">개요</h4>
<ul>
<li><p><code>GitHub 저장소 주소</code>는 뒤에 생성할 <code>Manifest(상세 설명 또는 Spec)</code>를 <code>Push</code>하기 위한 주소이다.</p>
<ul>
<li><code>git</code> 명령어</li>
</ul>
</li>
<li><p>init (초기화) - 현재 디렉터리를 <code>Git</code> 작업할 수 있도록 선언한다.</p>
</li>
<li><p>remote (원격) - <code>GitHub 저장소</code>와 같은 원격 저장소를 지정한다.</p>
</li>
<li><p>add (추가) - 파일 또는 디렉터리를 <code>Git</code>을 통해 추적하도록 설정한다.</p>
</li>
<li><p>commit (저장) - <code>Git</code>을 통해 추적하는 파일의 변경 사항을 저장한다.</p>
</li>
<li><p>Push (전송) - 변경 사항이 기록된 <code>Local Git</code>의 파일들을 원격 저장소로 전송한다.</p>
<ul>
<li><code>GitOps</code> 화면 하단의 <code>Quick setup</code>에 <code>주소(https://github.com/kyk02405/GitOps.git)</code>를 복사한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b2d73eff-8808-419b-ba34-7f72d6364571/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="step-3-gitops의-내용-저장을-위한-디렉터리-생성">Step 3. 'GitOps'의 내용 저장을 위한 디렉터리 생성</h3>
<pre><code class="language-bash">[root@m-k8s ~]# mkdir ~/gitops
[root@m-k8s ~]# cd ~/gitops/
[root@m-k8s gitops]# pwd
/root/gitops</code></pre>
<ul>
<li><code>GitOps</code>의 내용을 저장할 <code>디렉터리(gitops)</code>를 <code>Master Node(m-k8s)</code>의 <code>홈 디렉터리(/root)</code>에 생성한다.<ul>
<li>생성이 완료되면 해당 디렉터리로 이동</li>
</ul>
</li>
</ul>
<hr />
<h3 id="step-4-git-관련-작업을-위한-초기화">Step 4. 'Git' 관련 작업을 위한 초기화</h3>
<ul>
<li>명령을 실행한 후 <code>Git</code> 작업 내용을 저장하는 <code>.git</code> 디렉터리가 생성되는 것을 확인한다.</li>
</ul>
<hr />
<h3 id="step-5-자격-증명-헬퍼를-이용한-영구적인-자격증명-설정">Step 5. '자격 증명 헬퍼'를 이용한 '영구적인 자격증명' 설정</h3>
<ul>
<li><code>Git</code>을 통해서 원격 저장소에 파일들을 저장할 때는 <code>작업자 이름</code>, <code>작업자 이메일 주소</code> 등을 설정하는게 좋다.
b - 현재 환경에서 <code>GitHub 저장소</code>로 여러 번 <code>Push(전송)</code>하게 되면 <code>Push</code>할 때마다 <code>GitHub</code> <code>사용자 이름</code>과 <code>비밀번호</code>를 요구하기 때문에 <code>자격 증명 저장소(Credential Store)</code>를 이용해서 번거로은 상태가 발생하지 않도록 <code>자격 증명 헬퍼(Credential Helper)</code>를 설정해서 자격증명이 영구적으로 저장되도록 한다.<pre><code class="language-bash">[root@m-k8s gitops]# git config --global user.name &quot;kyk02405&quot;
[root@m-k8s gitops]# git config --global user.email &quot;kyk02405@gmail.com&quot;
[root@m-k8s gitops]# git config --global credential.helper &quot;store --file ~/.git-cred&quot;</code></pre>
</li>
</ul>
<hr />
<h3 id="step-6-step-6-github-저장소에-파일-업로드">Step 6. Step 6. 'GitHub 저장소'에 파일 업로드</h3>
<ul>
<li>원격 저장소에 작업한 파일들을 <code>GitHub 저장소</code>에 업로드할 수 있도록 저장소의 주소를 추가한다.</li>
<li><code>origin</code>은 사용자의 'GitHub 저장소'에 대한 <code>또 다른 이름(별칭, Alias)</code>이다.<pre><code class="language-bash">[root@m-k8s gitops]# git remote add origin https://github.com/kyk02405/GitOps.git</code></pre>
</li>
</ul>
<hr />
<h3 id="step-7-kubernetes-오브젝트-배포">Step 7. Kubernetes 오브젝트 배포</h3>
<ul>
<li><code>Jenkins</code>에서 선언적으로 <code>Kubernetes 오브젝트</code>를 배포하기 위해서 사전에 구성해 둔 파일들을 홈 디렉터리 밑에 <code>gitops</code> 디렉터리로 복사한다. <pre><code class="language-bash">[root@m-k8s 5.5.1]# cp ~/_Book_k8sInfra/ch5/5.5.1/* ~/gitops/</code></pre>
</li>
</ul>
<hr />
<h3 id="step-8-kubernetes-오브젝트-배포를-위한-jenkinsfile-내용-수정">Step 8. <code>Kubernetes 오브젝트</code> 배포를 위한 <code>Jenkinsfile</code> 내용 수정</h3>
<ul>
<li><code>Jenkinsfile</code>에는 <code>Kubernetes 오브젝트 배포</code>를 위한 설정이 이미 구현되어 있다.</li>
<li><code>GitHub 저장소</code>는 개별 사용자에 맞는 설정이 필요하기 때문에 <code>sed</code> 명령을 이용해서 <code>GitHub 저장소</code>를 변경한다.</li>
<li><code>sed</code> 명령은 기존에 사용했던 방식인 <code>s/변경대상/변경할내용/g</code>로 사용했는데 <code>변경할 내용</code>에 <code>/</code>가 포함되어 있기 때문에 <code>GitHub 저장소</code>로 변환되지 않는다.</li>
<li>따라서 <code>/</code>를 <code>,</code>로 대치하게 되면 <code>GitHub 저장소</code>가 정상적으로 변화된다. 단, 빈 공백이 있어서는 안된다.<pre><code class="language-bash">[root@m-k8s gitops]# sed -i 's,Git-URL,https://github.com/kyk02405/GitOps.git,g' Jenkinsfile
</code></pre>
</li>
</ul>
<p>[root@m-k8s gitops]# cat Jenkinsfile
pipeline {
  agent any
  stages {
    stage('git pull') {
      steps {
        // <a href="https://github.com/kyk02405/GitOps.git">https://github.com/kyk02405/GitOps.git</a> will replace by sed command before RUN
        git url: '<a href="https://github.com/kyk02405/GitOps.git'">https://github.com/kyk02405/GitOps.git'</a>, branch: 'main'
      }
    }
    stage('k8s deploy'){
      steps {
        kubernetesDeploy(kubeconfigId: 'kubeconfig',
                         configs: '*.yaml')
      }
    }
  }</p>
<pre><code>---
### Step 9. 'add(추가)'를 이용한 파일 등록
- `Git`이 파일들을 추적할 수 있도록 다음의 명령을 이용해서 파일들을 등록한다.
```bash
[root@m-k8s gitops]# git add .</code></pre><hr />
<h3 id="step-10-추가한-내용-확인">Step 10. 추가한 내용 확인</h3>
<ul>
<li>추가한 내용을 'Commit' 하기 전에 설정값들이 제대로 설정되어 있는지 확인한다.<pre><code class="language-bash">[root@m-k8s gitops]# git config --list
user.name=kyk02405
user.email=kyk02405@gmail.com
credential.helper=store --file ~/.git-cred
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
remote.origin.url=https://github.com/kyk02405/GitOps.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*</code></pre>
</li>
</ul>
<hr />
<h3 id="step-11-변경-사항-저장">Step 11. 변경 사항 저장</h3>
<ul>
<li>추가한 파일들을 <code>Push(전송)</code>하기 위해서 이 명령을 통해 변경 사항을 저장한다.</li>
<li><code>-m</code>은 <code>Push(전송)</code>하는 내용 등을 파악하기 위한 <code>주석</code>이라고 생각하면 된다.<pre><code class="language-bash">[root@m-k8s gitops]# git commit -m &quot;init commit&quot;
[master (root-commit) 1900297] init commit
3 files changed, 37 insertions(+)
create mode 100644 Jenkinsfile
create mode 100644 README.md
create mode 100644 deployment.yaml</code></pre>
</li>
</ul>
<hr />
<h3 id="step-12-github-저장소로-push전송로-업로드-되는-branch-설정">Step 12. 'GitHub 저장소'로 'Push(전송)'로 업로드 되는 'Branch' 설정</h3>
<ul>
<li><code>GitHub 저장소</code>로 <code>Push(전송)</code>하기 위해서 업로드 되는 <code>Branch</code>를 <code>git branch</code>로 설정해야 한다.</li>
<li><code>Branch(작업의 흐름)</code>는 <code>Code</code>를 보관할 수 있는 단위로 상황에 따랏 여러 <code>Branch</code>를 구성하고 작업 내용을 분리, 저장할 수 있다.</li>
<li><code>-M(Move)</code>은 <code>Branch</code> 이름을 바꾸는 옵션이고 <code>main</code>은 <code>기본 Branch 이름</code>이다.</li>
</ul>
<hr />
<h3 id="step-13-github-저장소로-push전송">Step 13. <code>GitHub 저장소</code>로 <code>Push(전송)</code></h3>
<ul>
<li>명령 실행 시 <code>비밀번호 입력</code>할 때 오류가 발생하면 <code>GitHub</code>에서의 <code>Token(비밀번호 로그인 방식)</code> 문제이다.</li>
<li><code>GitHub</code>에서는 <code>HTTP를 이용한 기존의 비밀번호 로그인 방식</code>을 더 이상 지원하지 않는다.</li>
<li>따라서 <code>HTTPS</code> 환경에서의 <code>새로운 비밀번호 로그인 방식(Token)</code>을 이용해서 접속하도록 설정해 줘야 한다.</li>
</ul>
<pre><code class="language-bash">[root@m-k8s gitops]# git branch -M main
[root@m-k8s gitops]# git branch
[root@m-k8s gitops]# git push -u origin main
Username for 'https://github.com': kyk02405
Password for 'https://kyk02405@github.com': (토큰키입력)</code></pre>
<h4 id="token은-auth-token인증-토큰이라고도-하는데-사용자가-로그인-후-server가-발급해준다">Token은 Auth Token(인증 토큰)이라고도 하는데 사용자가 로그인 후 'Server'가 발급해준다.</h4>
<ul>
<li>즉, <code>GitHub</code> 사이트에 접속을 시도하는 사용자에게 <code>너 누구냐?</code>라고 물었을 때 인증된 사용자 임을 확인 시키기 위한 용도로 사용된다<h4 id="토큰-생성-방법">토큰 생성 방법</h4>
<blockquote>
<p><code>Github 프로필 아이콘</code> -&gt; <code>Settings</code> -&gt; <code>Developer Settings</code> -&gt; <code>Personal access tokens</code> -&gt; <code>tokens (classic)</code>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4d11bb6d-b3e9-4afb-afac-26b4648f1158/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9951a26d-97ec-479d-a706-f6bb590e2fd7/image.png" /></p>
</blockquote>
</li>
<li>토큰은 한번만 뜸 따로 저장하기</li>
</ul>
<hr />
<h3 id="step-14-github-저장소로-전송된-내용-확인">Step 14. 'GitHub 저장소'로 전송된 내용 확인</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3e54bdeb-f0d6-4e75-9c5f-fe15917dda6b/image.png" /></p>
<ul>
<li><code>m-k8s</code>의 <code>/root/gitops/</code> 디렉터리에 있는 파일들이 모두 생성되었는지 확인한다.</li>
<li><code>GitHub</code> 사이트에서 우측 상단에 있는 <code>접속 사용자 아이콘</code>을 클릭한 후 <code>Repositories</code>를 클릭한다.</li>
<li><code>Repositories</code> 하단에 있는 <code>GitOps</code>를 클릭한다.</li>
<li><code>kyk02405/GitOps</code> 하단에 생성된 파일들을 확인할 수 있다.</li>
</ul>
<hr />
<h3 id="step-15-kubernetes에서의-관리를-위한-kubernetes용-plug-in-설치">Step 15. <code>Kubernetes</code>에서의 관리를 위한 <code>Kubernetes용 Plug-in</code> 설치</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/68e1d1fd-d556-4f2e-9c33-d6f8b8a42518/image.png" /></p>
<ul>
<li><code>Jenkins</code>의 <code>대시보드</code>에서 <code>Jenkins 관리</code>를 클릭한다.</li>
<li><code>플러그인 관리</code>를 클릭한 후 <code>설치 가능</code>탭을 클릭한다.</li>
<li>검색창에 <code>kubernetes</code>를 입력한다.</li>
<li><code>Kubernetes Continuous Deploy</code>를 체크한 후 하단에 있는 <code>지금 다운로드하고 재시작 후 설치하기</code>를 클릭한다.</li>
</ul>
<hr />
<h3 id="step-16-kubernetes-continuous-deploy-플러그인-설치">Step 16. <code>Kubernetes Continuous Deploy</code> 플러그인 설치</h3>
<ul>
<li><code>Kubernetes Continuous Deploy(쿠버네티스용 지속적 배포)</code> 플러그인이 설치되는 것을 확인한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/64f04ef4-cc68-4964-8024-f7c3ce7e0927/image.png" /></li>
<li>이 때 <code>설치가 끝나고 실행중인 작업이 없으면 Jenkins 재시작</code>을 체크한다.</li>
<li>플러그인 설치 후에 <code>Jenkins</code>가 자동으로 재시작이 안 될 수가 있는데 <code>Jenkins</code> 출력창에서 새로고침(F5)하면 된다. </li>
</ul>
<hr />
<h3 id="step-17-kubernetes-continuous-deploy쿠버네티스용-지속적-배포-플러그인-설정">Step 17. <code>Kubernetes Continuous Deploy(쿠버네티스용 지속적 배포)</code> 플러그인 설정</h3>
<ul>
<li><code>Kubernetes Continuous Deploy(쿠버네티스용 지속적 배포)</code> 플러그인은 <code>Kubernetes</code> 설정 파일을 관리할 수 있게 <code>자격 증명 정보</code>를 별도로 관리하는데 다수의 <code>Kubernetes Cluster</code>를 안전하게 관리할 수가 있다.</li>
<li><code>Jenkins</code>의 <code>대시보드</code>에서 <code>Jenkins 관리</code>를 클릭한 후 <code>Manage Credentials</code>을 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f550d530-3f70-431e-860e-fa6548b0191b/image.png" /></li>
</ul>
<hr />
<h3 id="step-18-새로운-자격증명-추가">Step 18. 새로운 자격증명 추가</h3>
<ul>
<li><code>Stores scoped to Jenkins</code> 하단에 있는 <code>global</code>을 클릭하면 된다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/eda68794-311f-4384-831b-d8bb081d036e/image.png" /></li>
</ul>
<hr />
<h3 id="step-19-master-node에-접근-가능한-권한-부여">Step 19. 'Master Node'에 접근 가능한 권한 부여</h3>
<ul>
<li><code>Kubernetes</code> 설정 파일에 대한 <code>자격 증명</code>을 가져오려면 현재 설정 파일이 있는 <code>Master Node(m-k8s, 192.168.1.10)</code>에 접속 권한이 있어야 한다.</li>
<li>왼쪽에 있는 <code>Add Credentials</code>를 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0ddef38f-7d82-4dc8-b2ab-408dd0832c77/image.png" /></li>
</ul>
<hr />
<h3 id="step-20-다음과-같이-입력한-후-ok를-클릭한다">Step 20. 다음과 같이 입력한 후 'OK'를 클릭한다.</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2eddf774-3c53-4445-af35-fded3e3d84da/image.png" /></p>
<p>   -&gt; Kind      : Username with password
   -&gt; Scope   : Global (Jenkins, nodes, items, all child items, etc)
   -&gt; Username   : root
   -&gt; Password   : vagrant
   -&gt; ID      : m-k8s-ssh
   -&gt; Description   : m-k8s ssh credential</p>
<hr />
<h3 id="step-21-m-k8s-ssh-이름의-노드-자격-증명-확인">Step 21. ‘m-k8s-ssh’ 이름의 ‘노드 자격 증명’ 확인</h3>
<ul>
<li>설정을 통한 등록을 확인한 후 ‘Kubernetes’ 설정 파일에 대한 자격증명을 추가한다.</li>
<li>왼쪽에 있는 ‘Add Credentials’를 클릭한다.</li>
</ul>
<hr />
<h3 id="step-22-kubernetes-접속-자격-증명을-다음과-같이-입력한-후-ok를-클릭한다">Step 22. 'Kubernetes' 접속 자격 증명을 다음과 같이 입력한 후 'OK'를 클릭한다.</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/dd860122-0a26-4b7f-8fae-580e1e1f86cd/image.png" />
   -&gt; Kind      : Kubernetes configuration (kubeconfig)
   -&gt; Scope   : Global (Jenkins, nodes, items, all child items, etc)
   -&gt; ID      : kubeconfig
   -&gt; Description   : kubeconfig get from master node
   -&gt; Kubeconfig   : From a file on the Kubernetes master node
   -&gt; Server   : 192.168.1.10
   -&gt; SSH Credentials   : root/<strong>**</strong> (m-k8s ssh credential)
    -&gt; File         : .kube/config</p>
<hr />
<h3 id="step-23-kubernetes-접속-자격-증명이-kubeconfig된-것을-확인한다">Step 23. 'Kubernetes' 접속 자격 증명이 'kubeconfig'된 것을 확인한다.</h3>
<hr />
<h3 id="step-24-선언적인-배포-환경을-프로젝트-설정">Step 24. 선언적인 배포 환경을 프로젝트 설정</h3>
<ul>
<li><code>Jenkins</code>의 <code>대시보드</code>의 왼쪽에 있는 <code>새로운 Item</code>을 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1d588e51-b553-4b15-95aa-80c9c8f927f4/image.png" /></li>
<li>'Pipeline' 아이템을 선택한 후 'dpy-pl-gitops'를 입력한 후 하단에 있는 'OK'를 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/def4cb38-8e2f-4e00-80b6-b7a8721fc81b/image.png" /></li>
</ul>
<hr />
<h3 id="step-25-github-저장소에-변경-내용을-감시하기-위한-poll-scm-설정">Step 25. ‘GitHub 저장소’에 변경 내용을 감시하기 위한 ‘Poll SCM’ 설정</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/85715632-33de-4152-8d5a-2f32077ebef3/image.png" /></p>
<ul>
<li><code>Poll SCM</code>은 주기적으로 <code>GitHub 저장소</code>의 변경을 인식하게 한다.</li>
<li><code>Build Triggers</code> 탭에서 하단에 있는 <code>Poll SCM</code>을 체크한 후 <code>Schedule</code>은 <code>*/10 * * * *</code>로 입력한다.</li>
<li><code>*/10 * * * *</code>은 <code>Cron Expression(크론 표현식)</code>이라고 하며 <code>10분마다 변화가 있는지 체크</code>하라는 말이다.</li>
<li>참고로 <code>Crontab</code>에서의 표현 방식과 동일하다. 즉, <code>분 시 일 월 요일</code>을 뜻한다.</li>
<li>하단에 있는 <code>Apply</code>를 클릭한다.</li>
</ul>
<hr />
<h3 id="step-26-pipeline-프로젝트에서-사용할-소스-저장소-구성">Step 26. 'Pipeline' 프로젝트에서 사용할 소스 저장소 구성</h3>
<ul>
<li>'Pipeline' 탭을 클릭하고 다음과 같이 입력한 후 하단에 있는 'Apply'를 클릭한다.<ul>
<li>Definition      → Pipeline script from SCM</li>
<li>SCM         → Git</li>
<li>Repository URL   → <a href="https://github.com/samadalwho/GitOps.git">https://github.com/samadalwho/GitOps.git</a></li>
<li>Branch Specifier (blank for 'any')   → */main</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7fd7151f-68c8-4906-98b9-73026a5c52b7/image.png" /></p>
<hr />
<h3 id="step-27-dpy-pl-gitops-프로젝트의-배포-진행-상태-확인">Step 27. 'dpy-pl-gitops' 프로젝트의 배포 진행 상태 확인</h3>
<ul>
<li>'*/10 * * * *'로 설정했기 때문에 '10분'을 기다린 후 'Build History' 항목에서 진행되는 것을 확인할 수 있다.</li>
</ul>
<hr />
<h3 id="step-28-배포-작업-완료">Step 28. 배포 작업 완료</h3>
<ul>
<li>‘Build History’ 항목에서 ‘#1’, ‘#2’를 클릭하면서 확인하면 된다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/17721e1b-4363-4279-a232-c5f628722bc1/image.png" /></li>
</ul>
<hr />
<h3 id="step-29-deployment-확인">Step 29. Deployment 확인</h3>
<ul>
<li>배포 작업이 완료됨에 따라 ‘GitHub 저장소’에 ‘Push’한 ‘Yaml’ 파일이 ‘Kubernetes Cluster’에 적용이 되었는지 확인한다.<pre><code class="language-bash">[root@m-k8s gitops]# sed -i 's/replicas: 2/replicas: 5/' deployment.yaml
[root@m-k8s gitops]#
[root@m-k8s gitops]# git add . ; git commit -m &quot;change replicas count&quot; ; git push -u origin main
[main d686e89] change replicas count
1 file changed, 1 insertion(+), 1 deletion(-)
Counting objects: 5, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 283 bytes | 0 bytes/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/kyk02405/GitOps.git
 1900297..d686e89  main -&gt; main
Branch main set up to track remote branch main from origin.</code></pre>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/30c8df3e-da9f-43dd-8f0e-343a9614104e/image.png" /></li>
</ul>
<hr />
<h3 id="step-30-최종-확인">Step 30. 최종 확인</h3>
<ul>
<li>Deployment(배포) 상태 확인</li>
<li><code>Jenkins</code>의 <code>Pipeline dpy-pl-gitops</code> 프로젝트에서 <code>Build History</code>를 통해서 변화된 내용을 확인한다.</li>
<li><code>GitHub 저장소</code>의 <code>Code</code>에서 <code>deployment.yaml</code> 파일의 변화된 내용을 확인한다.</li>
</ul>