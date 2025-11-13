# Cloud DX - 33 Nginx

- 📅 Published: Thu, 13 Nov 2025 00:51:33 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-33-Nginx)

<hr />
<h1 id="18-nginx">18. Nginx</h1>
<h2 id="개요">개요</h2>
<ul>
<li>경량 웹 서버를 말한다.</li>
<li>웹에서의 출력이 동일한(시스템으로는 유사한) 서비스를 하고 있는 <code>Apache Web Server</code>와 충돌이 발생할 수 있기 때문에 개별적으로 운영하는 것을 권장한다.</li>
<li><code>CentOS</code> <code>1_Update</code></li>
</ul>
<hr />
<h2 id="step-1-저장소-repository">Step 1. 저장소 (Repository)</h2>
<h3 id="저장소-형태">저장소 형태</h3>
<pre><code class="language-bash">[root@localhost ~]# ls -l /etc/yum.repos.d
합계 40
-rw-r--r-- 1 root root 1665 10월 16  2024 CentOS-Base.repo
-rw-r--r-- 1 root root 1310 10월 16  2024 CentOS-CR.repo
-rw-r--r-- 1 root root  649  5월 21  2024 CentOS-Debuginfo.repo
-rw-r--r-- 1 root root  630  5월 21  2024 CentOS-Media.repo
-rw-r--r-- 1 root root 1332 10월 16  2024 CentOS-Sources.repo
-rw-r--r-- 1 root root 9454  5월 21  2024 CentOS-Vault.repo
-rw-r--r-- 1 root root  314 10월 16  2024 CentOS-fasttrack.repo
-rw-r--r-- 1 root root  616 10월 16  2024 CentOS-x86_64-kernel.repo</code></pre>
<h3 id="저장소-내용">저장소 내용</h3>
<pre><code class="language-bash">    12  [base]
    13  name=CentOS-$releasever - Base
    14  #mirrorlist=http://#mirrorlist.centos.org/?release=$releasever&amp;arch=$basearch&amp;repo=os&amp;infra=$infra
    15  baseurl=http://vault.centos.org/centos/$releasever/os/$basearch/
    16  gpgcheck=1
    17  gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7</code></pre>
<h3 id="저장소-추가-방법">저장소 추가 방법</h3>
<ul>
<li>자동 추가 (저장소 주소가 자동으로 인식될 때 사용)<pre><code class="language-bash">[root@localhost ~]# yum -y install epel-release
[root@localhost ~]# yum repolist</code></pre>
</li>
</ul>
<pre><code class="language-bash">[root@localhost ~]# ls -l /etc/yum.repos.d/
합계 48
-rw-r--r-- 1 root root 1665 10월 16  2024 CentOS-Base.repo
-rw-r--r-- 1 root root 1310 10월 16  2024 CentOS-CR.repo
-rw-r--r-- 1 root root  649  5월 21  2024 CentOS-Debuginfo.repo
-rw-r--r-- 1 root root  630  5월 21  2024 CentOS-Media.repo
-rw-r--r-- 1 root root 1332 10월 16  2024 CentOS-Sources.repo
-rw-r--r-- 1 root root 9454  5월 21  2024 CentOS-Vault.repo
-rw-r--r-- 1 root root  314 10월 16  2024 CentOS-fasttrack.repo
-rw-r--r-- 1 root root  616 10월 16  2024 CentOS-x86_64-kernel.repo
-rw-r--r-- 1 root root 1050 10월  3  2017 epel-testing.repo # 추가됨
-rw-r--r-- 1 root root  951 10월  3  2017 epel.repo # 추가됨</code></pre>
<ul>
<li>수동 추가 (저장소 주소가 자동으로 인식 안될 때 사용)<ul>
<li><code>Index of /packages/centos/7/x86_64/RPMS/</code></li>
</ul>
</li>
</ul>
<hr />
<h2 id="step-2-저장소-추가">Step 2. 저장소 추가</h2>
<ul>
<li>기본적으로 저장소에는 <code>Nginx</code>가 없기 때문에 추가해줘야 한다.<pre><code class="language-bash"># vi /etc/yum.repos.d/nginx.repo
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/x86_64/
gpgcheck=0
enabled=1</code></pre>
</li>
</ul>
<pre><code class="language-bash">[root@localhost yum.repos.d]# yum repolist</code></pre>
<h3 id="시스템-저장소-확인">시스템 저장소 확인</h3>
<pre><code class="language-bash">[root@localhost yum.repos.d]# ls -l
합계 52
-rw-r--r-- 1 root root 1665 10월 16  2024 CentOS-Base.repo
-rw-r--r-- 1 root root 1310 10월 16  2024 CentOS-CR.repo
-rw-r--r-- 1 root root  649  5월 21  2024 CentOS-Debuginfo.repo
-rw-r--r-- 1 root root  630  5월 21  2024 CentOS-Media.repo
-rw-r--r-- 1 root root 1332 10월 16  2024 CentOS-Sources.repo
-rw-r--r-- 1 root root 9454  5월 21  2024 CentOS-Vault.repo
-rw-r--r-- 1 root root  314 10월 16  2024 CentOS-fasttrack.repo
-rw-r--r-- 1 root root  616 10월 16  2024 CentOS-x86_64-kernel.repo
-rw-r--r-- 1 root root 1050 10월  3  2017 epel-testing.repo
-rw-r--r-- 1 root root  951 10월  3  2017 epel.repo
-rw-r--r-- 1 root root   96 11월 12 16:57 nginx.repo</code></pre>
<hr />
<h2 id="step-3-nginx-패키지-설치">Step 3. Nginx 패키지 설치</h2>
<h3 id="패키지-설치">패키지 설치</h3>
<pre><code class="language-bash">[root@localhost yum.repos.d]# yum -y install nginx-*</code></pre>
<ul>
<li><code>yum</code>으로 설치 안될 시 아래 두개 명령 실행<pre><code class="language-bash">sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
</code></pre>
</li>
</ul>
<p>sed -i 's|#baseurl=<a href="http://mirror.centos.org%7Cbaseurl=http://vault.centos.org%7Cg'">http://mirror.centos.org|baseurl=http://vault.centos.org|g'</a> /etc/yum.repos.d/CentOS-*</p>
<pre><code>- 그래도 안되면 아래 명령 실행
```bash
[root@localhost yum.repos.d]# yum -y install nginx-* --skip-broken</code></pre><h3 id="패키지-버전-확인">패키지 버전 확인</h3>
<pre><code class="language-bash">[root@localhost yum.repos.d]# nginx -v
nginx version: nginx/1.26.1
[root@localhost yum.repos.d]# rpm -qa | grep nginx | nl
     1  nginx-debug-1.8.0-1.el7.ngx.x86_64
     2  nginx-module-xslt-debuginfo-1.26.1-2.el7.ngx.x86_64
     3  nginx-module-image-filter-1.26.1-2.el7.ngx.x86_64
     4  nginx-module-geoip-debuginfo-1.26.1-2.el7.ngx.x86_64
     5  nginx-module-njs-1.26.1+0.8.5-2.el7.ngx.x86_64
     6  nginx-module-image-filter-debuginfo-1.26.1-2.el7.ngx.x86_64
     7  nginx-debuginfo-1.26.1-2.el7.ngx.x86_64
     8  nginx-1.26.1-2.el7.ngx.x86_64
     9  nginx-nr-agent-2.0.0-12.el7.ngx.noarch
    10  nginx-module-xslt-1.26.1-2.el7.ngx.x86_64
    11  nginx-filesystem-1.20.1-10.el7.noarch
    12  nginx-module-njs-debuginfo-1.26.1+0.8.5-2.el7.ngx.x86_64
    13  nginx-module-geoip-1.26.1-2.el7.ngx.x86_64
    14  nginx-module-perl-debuginfo-1.26.1-2.el7.ngx.x86_64
    15  nginx-module-perl-1.26.1-2.el7.ngx.x86_64</code></pre>
<hr />
<h2 id="step-4-방화벽-포트8080-추가">Step 4. 방화벽 포트(8080) 추가</h2>
<ul>
<li>포트 추가<pre><code class="language-bash">&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;zone&gt;
&lt;short&gt;Public&lt;/short&gt;
&lt;description&gt;For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.&lt;/description&gt;
&lt;service name=&quot;ssh&quot;/&gt;
&lt;service name=&quot;dhcpv6-client&quot;/&gt;
&lt;port protocol=&quot;tcp&quot; port=&quot;22&quot;/&gt;
&lt;port protocol=&quot;tcp&quot; port=&quot;8080&quot;/&gt;
&lt;/zone&gt;</code></pre>
</li>
<li>적용<pre><code class="language-bash">[root@localhost yum.repos.d]# firewall-cmd --reload</code></pre>
</li>
</ul>
<hr />
<h2 id="실습-1-기본-경로-및-경로-변경을-이용한-사이트-출력">실습 1. 기본 경로 및 경로 변경을 이용한 사이트 출력</h2>
<h3 id="step-1-dns-server-설정-gusiyacom">Step 1. DNS Server 설정 (gusiya.com)</h3>
<h3 id="step-1-기본-경로를-이용한-사이트-출력">Step 1. 기본 경로를 이용한 사이트 출력</h3>
<ul>
<li>포트 설정<pre><code class="language-bash">[root@localhost conf.d]# cp -p default.conf default.conf.samadal
[root@localhost conf.d]#
[root@localhost conf.d]# vi default.conf</code></pre>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b749c3ce-cc11-4c4f-ba81-87af64744cbb/image.png" /></li>
</ul>
</li>
</ul>
<ul>
<li>데몬 실행<pre><code class="language-bash">[root@localhost conf.d]# systemctl enable nginx
Created symlink from /etc/systemd/system/multi-user.target.wants/nginx.service to /usr/lib/systemd/system/nginx.service.
[root@localhost conf.d]# systemctl restart nginx</code></pre>
</li>
<li>사이트 출력<code>(firefox)</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ceabda77-39be-4ec7-88a2-a7225aade79a/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="step-2-기본-경로-변경을-통한-사이트-출력">Step 2. 기본 경로 변경을 통한 사이트 출력</h3>
<ul>
<li><p>기본 경로 확인 및 기본 문서 변경
```bash
[root@localhost conf.d]# cd /usr/share/nginx/html/
[root@localhost html]# ls -l
합계 8</p>
</li>
<li><p>rw-r--r-- 1 root root 497  5월 30  2024 50x.html</p>
</li>
<li><p>rw-r--r-- 1 root root 615  5월 30  2024 index.html
[root@localhost html]# mv index.html index.html.samadal
[root@localhost html]#
[root@localhost html]# ls -l
합계 8</p>
</li>
<li><p>rw-r--r-- 1 root root 497  5월 30  2024 50x.html</p>
</li>
<li><p>rw-r--r-- 1 root root 615  5월 30  2024 index.html.samadal
[root@localhost html]# vi index.html</p>
<pre><code> - ![](https://velog.velcdn.com/images/kyk02405/post/f39e16a5-257d-48a2-b159-d3c4d84a985a/image.png)</code></pre></li>
<li><p>기본 경로 변경</p>
<pre><code class="language-bash">[root@localhost html]# vi /etc/nginx/conf.d/default.conf</code></pre>
<pre><code class="language-bash">    1 server {
    2     listen       8080;
    3     server_name  localhost;
    4
    5     #access_log  /var/log/nginx/host.access.log  main;
    6
    7     location / {
    8         # root   /usr/share/nginx/html;
    9         root   /export/home/samadal;
   10         index  index.html index.htm;
   11     }</code></pre>
<pre><code class="language-bash">[root@localhost html]# vi /export/home/samadal/index.html</code></pre>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f9c31ae0-d019-46a3-a81b-a54244bba78c/image.png" /></p>
</li>
</ul>
<pre><code class="language-bash">[root@localhost html]# chmod 701 /export/home/samadal/

[root@localhost html]# systemctl restart nginx</code></pre>
<ul>
<li><code>firefox</code>에서 <code>F5</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d5d48094-7dcd-4131-9bc7-a6ac99bf72f6/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h2 id="실습-2-php">실습 2. php</h2>
<ul>
<li>Step 1. php 패키지 설치<pre><code class="language-bash">yum -y install php-fpm
</code></pre>
</li>
</ul>
<p>yum -y install php-cli  php-redis  php-brotli php-intl php-gd php-gmp php-imap php-bcmath php-interbase php-json php-mbstring</p>
<p>yum -y install php-mysqlnd php-odbc php-opcache php-memcached php-tidy php-pdo php-pdo-dblib php-pear php-pgsql php-process</p>
<p>yum -y install php-pecl-apcu php-pecl-geoip php-pecl-imagick php-pecl-hrtime php-pecl-json php-pecl-memcache php-pecl-mongodb</p>
<p>yum -y install php-pecl-rar php-pecl-pq php-pecl-redis4 php-pecl-yaml php-pecl-zip --skip-broken</p>
<pre><code>- ![](https://velog.velcdn.com/images/kyk02405/post/206fb386-c5b5-46ce-ae81-56f6cd7395cf/image.png)

- 패키지 설치
  - `Nginx` 설정 파일에서 `php` 파일 인식을 위한 설정

```bash
[root@localhost html]# vi /etc/nginx/conf.d/default.conf
      2     listen       8080;
      3     server_name  localhost;
      4
      5     #access_log  /var/log/nginx/host.access.log  main;
      6
      7     location / {
      8         # root   /usr/share/nginx/html;
      9         root   /export/home/samadal;
     10         index  index.html index.htm index.php;
     11     }
     12
     13     #error_page  404              /404.html;
     14
     15     # redirect server error pages to the static page /50x.html
     16     #
     17     error_page   500 502 503 504  /50x.html;
     18     location = /50x.html {
     19         root   /usr/share/nginx/html;
     20     }
     21
     22     # proxy the PHP scripts to Apache listening on 127.0.0.1:80
     23     #
     24     #location ~ \.php$ {
     25     #    proxy_pass   http://127.0.0.1;
     26     #}
     27
     28     # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
     29     #
     30     location ~ \.php$ {
     31         root           html;
     32         fastcgi_pass   127.0.0.1:9000;
     33         fastcgi_index  index.php;
     34         # fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
     35         fastcgi_param  SCRIPT_FILENAME  /export/home/samadal$fastcgi_script_name;
     36         include        fastcgi_params;
     37     }
     38
     39     # deny access to .htaccess files, if Apache's document root
     40     # concurs with nginx's one
     41     #
     42     #location ~ /\.ht {
     43     #    deny  all;
     44     #}
     45 }</code></pre><pre><code class="language-bash">[root@localhost html]# systemctl restart nginx
[root@localhost html]# systemctl restart php-fpm</code></pre>
<pre><code class="language-bash">[root@localhost html]# vi /export/home/samadal/index.php

&lt;?php
        phpinfo();
?&gt;</code></pre>
<ul>
<li><p>사이트 출력</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e7a1e5d5-9927-4307-8509-596e5eb5e893/image.png" /></li>
</ul>
</li>
<li><p>사이트 출력 시 <code>5.4.16</code> 버전으로 나올 경우 삭제하고 다시 설치</p>
</li>
</ul>
<pre><code class="language-bash">[root@localhost html]# yum -y remove php-*
[root@localhost html]# yum list php
[root@localhost html]# yum -y install https://rpms.remirepo.net/enterprise/remi-release-7.rpm
[root@localhost html]# yum-config-manager --enable remi-php74
[root@localhost html]# yum -y install php php-fpm

[root@localhost html]# yum -y install php-cli  php-redis  php-brotli php-intl php-gd php-gmp php-imap php-bcmath php-interbase php-json php-mbstring

[root@localhost html]# yum -y install php-mysqlnd php-odbc php-opcache php-memcached php-tidy php-pdo php-pdo-dblib php-pear php-pgsql php-process

[root@localhost html]# yum -y install php-pecl-apcu php-pecl-geoip php-pecl-imagick php-pecl-hrtime php-pecl-json php-pecl-memcache php-pecl-mongodb

[root@localhost html]# yum -y install php-pecl-rar php-pecl-pq php-pecl-redis4 php-pecl-yaml php-pecl-zip --skip-broken

[root@localhost html]# yum list php
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * epel: d2lzkl7pfhq30w.cloudfront.net
 * remi-php74: ftp.riken.jp
 * remi-safe: ftp.riken.jp
Installed Packages
php.x86_64                                7.4.33-15.el7.remi                                 @remi-php74

[root@localhost html]# systemctl restart nginx
[root@localhost html]# systemctl restart php-fpm
</code></pre>
<ul>
<li><code>firefox</code>에서 <code>F5</code> 후 버젼 바뀐 것을 확인<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0960c76e-6fbb-4220-9579-96e0104f0bc4/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h2 id="실습-3-제로보드">실습 3. 제로보드</h2>
<h3 id="파일-다운로드">파일 다운로드</h3>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/dd80795b-4048-4787-acf5-a26d7f8b893c/image.png" />
```bash
[root@localhost samadal]# cd /export/home/samadal/
[root@localhost samadal]# wget <a href="http://download.xpressengine.com/download/18325662/22756225">http://download.xpressengine.com/download/18325662/22756225</a></li>
<li>-2025-11-13 09:53:28--  <a href="http://download.xpressengine.com/download/18325662/22756225">http://download.xpressengine.com/download/18325662/22756225</a>
Resolving download.xpressengine.com (download.xpressengine.com)... 222.239.166.120
Connecting to download.xpressengine.com (download.xpressengine.com)|222.239.166.120|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 11240720 (11M) [application/zip]
Saving to: ‘22756225’</li>
</ul>
<p>100%[==============================================================&gt;] 11,240,720  3.12MB/s   in 3.4s   =</p>
<p>2025-11-13 09:53:32 (3.13 MB/s) - ‘22756225’ saved [11240720/11240720]</p>
<p>[root@localhost samadal]# ls -l
합계 10988
-rw-r--r-- 1 root root 11240720 10월 22  2019 22756225
-rw-r--r-- 1 root root        8 11월 12 17:39 index.html
-rw-r--r-- 1 root root       21 11월 12 18:02 index.php
[root@localhost samadal]#</p>
<pre><code>### 사이트 출력
```bash
[root@localhost samadal]# mv 22756225 xe.zip
[root@localhost samadal]# unzip xe.zip
[root@localhost samadal]# chmod 707 xe
[root@localhost samadal]# systemctl restart nginx
[root@localhost samadal]# systemctl restart php-fpm</code></pre><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9ef61c88-1edc-4662-8bb0-7393f1290fb4/image.png" /></li>
</ul>
<hr />
<h2 id="실습-4-cafe24에-있는-web-hosting-구성">실습 4. Cafe24에 있는 Web Hosting 구성</h2>