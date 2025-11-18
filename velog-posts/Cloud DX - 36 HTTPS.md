# Cloud DX - 36 HTTPS

- 📅 Published: Fri, 14 Nov 2025 01:55:09 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-35-HTTPS)

<hr />
<h1 id="20-https">20. HTTPS</h1>
<ul>
<li><code>CentOS</code> <code>4 Snapshot</code><h2 id="개요">개요</h2>
</li>
<li>(핵심) 일반적으로 공인 인증서를 발급해 주는 발급기관에서 <span style="color: red;"><code>SSL인증서</code></span>를 발급받은 후 PC에 적용해서 사용한다.</li>
<li><code>http</code>(Hyper Text Transfer Protocol)는 데이터 전송(통신)할 때 평문으로 되어 있다.</li>
<li><code>https</code>(Hyper Text Transfer Protocol Secure)는 데이터 전송(통신)할 때 암호화된 상태로 되어 있다. (Telnet 과 SSH)</li>
<li>보안상 <code>https</code>를 사용해야 한다.</li>
<li>통신이 암호화되어 있기 때문에 불법 사이트 같은 경우에 도용되기도 한다.</li>
</ul>
<h2 id="https-운용-방식">HTTPS 운용 방식</h2>
<ul>
<li><code>HTTPS</code>를 적용하기 위해서는 <code>두 가지 필수 조건(키, 인증서)</code>이 있다.</li>
<li><code>키</code>를 발급받기 위해서는 <code>인증서</code>를 키로 암호화해서 보관하고 사용한다.</li>
</ul>
<h2 id="sslsecure-sockets-layer-보안-소켓-계층">SSL(Secure Sockets Layer, 보안 소켓 계층)</h2>
<ul>
<li><code>웹사이트</code>와 <code>웹브라우저</code> 사이에 전송된 데이터를 암호화하여 연결을 유지하는 표준 기술을 말한다.</li>
<li>개인 정보 및 기타 보안이 필요한 정보 등이 포함되어 전송되는 모든 정보를 <code>열람</code> 또는 <code>탈취</code> 를 방지한다.</li>
</ul>
<hr />
<h2 id="실습">실습</h2>
<h3 id="step-1-패키지-설치">Step 1. 패키지 설치</h3>
<pre><code class="language-bash">[root@ns ~]# yum -y install openssl*

[root@ns ~]# rpm -qa | grep openssl | nl
     1  openssl098e-0.9.8e-29.el7.centos.3.x86_64
     2  openssl-libs-1.0.2k-26.el7_9.x86_64
     3  openssl-1.0.2k-26.el7_9.x86_64
     4  openssl-perl-1.0.2k-26.el7_9.x86_64
     5  openssl-devel-1.0.2k-26.el7_9.x86_64
     6  xmlsec1-openssl-1.2.20-8.el7_9.x86_64
     7  openssl-static-1.0.2k-26.el7_9.x86_64

저장소 갱신 후 재설치
[root@ns ~]# yum -y install epel-release
[root@ns ~]# yum -y install openssl*

[root@ns ~]# rpm -qa | grep openssl | nl
     1  openssl098e-0.9.8e-29.el7.centos.3.x86_64
     2  openssl-libs-1.0.2k-26.el7_9.x86_64
     3  openssl-1.0.2k-26.el7_9.x86_64
     4  openssl11-libs-1.1.1k-7.el7.x86_64
     5  openssl-perl-1.0.2k-26.el7_9.x86_64
     6  openssl11-1.1.1k-7.el7.x86_64
     7  openssl11-static-1.1.1k-7.el7.x86_64
     8  openssl-devel-1.0.2k-26.el7_9.x86_64
     9  xmlsec1-openssl-1.2.20-8.el7_9.x86_64
    10  openssl11-devel-1.1.1k-7.el7.x86_64
    11  openssl-static-1.0.2k-26.el7_9.x86_64
    12  openssl-pkcs11-0.4.10-1.el7.x86_64
</code></pre>
<hr />
<h3 id="step-2-키-생성">Step 2. 키 생성</h3>
<pre><code class="language-bash">[root@ns ~]# cd /etc/pki/tls/certs/
[root@ns certs]# ls -l
합계 12
-rw-r--r-- 1 root root 2516  3월 21  2023 Makefile
lrwxrwxrwx 1 root root   49 10월 31  2024 ca-bundle.crt -&gt; /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
lrwxrwxrwx 1 root root   55 10월 31  2024 ca-bundle.trust.crt -&gt; /etc/pki/ca-trust/extracted/openssl/ca-bundle.trust.crt
-rwxr-xr-x 1 root root  610  3월 21  2023 make-dummy-cert
-rwxr-xr-x 1 root root  829  3월 21  2023 renew-dummy-cert

[root@ns certs]# openssl genrsa -out http.key 2048

[root@ns certs]# ls -l
합계 16
-rw-r--r-- 1 root root 2516  3월 21  2023 Makefile
lrwxrwxrwx 1 root root   49 10월 31  2024 ca-bundle.crt -&gt; /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
lrwxrwxrwx 1 root root   55 10월 31  2024 ca-bundle.trust.crt -&gt; /etc/pki/ca-trust/extracted/openssl/ca-bundle.trust.crt
-rw-r--r-- 1 root root 1679 11월 14 10:01 http.key
-rwxr-xr-x 1 root root  610  3월 21  2023 make-dummy-cert
-rwxr-xr-x 1 root root  829  3월 21  2023 renew-dummy-cert</code></pre>
<h3 id="step-3-인증서csr-생성">Step 3. 인증서(CSR) 생성</h3>
<pre><code class="language-bash">[root@ns certs]# openssl req -new -key http.key -out http.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:kr
State or Province Name (full name) []:Seoul
Locality Name (eg, city) [Default City]:Jongno
Organization Name (eg, company) [Default Company Ltd]:Himedia
Organizational Unit Name (eg, section) []:Edu
Common Name (eg, your name or your server's hostname) []:www.gusiya.com
Email Address []:samadal@mail.gusiya.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:</code></pre>
<hr />
<h3 id="step-4-생성된-키와-인증서-병합">Step 4. 생성된 키와 인증서 병합</h3>
<pre><code class="language-bash">[root@ns certs]# openssl x509 -req -days 365 -in http.csr -signkey http.key -out http.crt
Signature ok
subject=/C=kr/ST=Seoul/L=Jongno/O=Himedia/OU=Edu/CN=www.gusiya.com/emailAddress=samadal@mail.gusiya.com
Getting Private key</code></pre>
<hr />
<h3 id="step-5-ssl-module-설치-및-설정">Step 5. SSL Module 설치 및 설정</h3>
<pre><code class="language-bash">[root@ns certs]# yum -y install mod_ssl

[root@ns certs]# rpm -qa | grep ssl | nl
     1  openssl098e-0.9.8e-29.el7.centos.3.x86_64
     2  mod_ssl-2.4.6-99.el7.centos.1.x86_64
     3  openssl-libs-1.0.2k-26.el7_9.x86_64
     4  openssl-1.0.2k-26.el7_9.x86_64
     5  openssl11-libs-1.1.1k-7.el7.x86_64
     6  python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch
     7  openssl-perl-1.0.2k-26.el7_9.x86_64
     8  openssl11-1.1.1k-7.el7.x86_64
     9  openssl11-static-1.1.1k-7.el7.x86_64
    10  openssl-devel-1.0.2k-26.el7_9.x86_64
    11  xmlsec1-openssl-1.2.20-8.el7_9.x86_64
    12  openssl11-devel-1.1.1k-7.el7.x86_64
    13  openssl-static-1.0.2k-26.el7_9.x86_64
    14  openssl-pkcs11-0.4.10-1.el7.x86_64

[root@ns certs]# cd /etc/httpd/conf.d
[root@ns conf.d]# pwd
/etc/httpd/conf.d
[root@ns conf.d]# ls -l
합계 32
-rw-r--r-- 1 root root  366  5월 30  2023 README
-rw-r--r-- 1 root root 2926  5월 30  2023 autoindex.conf
-rw-r--r-- 1 root root  323  5월 30  2023 manual.conf
-rw-r--r-- 1 root root 9443  5월 30  2023 ssl.conf
-rw-r--r-- 1 root root 1252  5월 30  2023 userdir.conf
-rw-r--r-- 1 root root  824  5월 30  2023 welcome.conf

[root@ns conf.d]# cp -p /etc/httpd/conf.d/ssl.conf /etc/httpd/conf.d/ssl.conf.samadal

[root@ns conf.d]# ls -l
합계 44
-rw-r--r-- 1 root root  366  5월 30  2023 README
-rw-r--r-- 1 root root 2926  5월 30  2023 autoindex.conf
-rw-r--r-- 1 root root  323  5월 30  2023 manual.conf
-rw-r--r-- 1 root root 9443  5월 30  2023 ssl.conf
-rw-r--r-- 1 root root 9443  5월 30  2023 ssl.conf.samadal
-rw-r--r-- 1 root root 1252  5월 30  2023 userdir.conf
-rw-r--r-- 1 root root  824  5월 30  2023 welcome.conf

[root@ns conf.d]# vi ssl.conf

59 DocumentRoot &quot;/var/www/html&quot; # 주석되어 있으면 해제하기
...
100 SSLCertificateFile /etc/pki/tls/certs/localhost.crt
107 SSLCertificateKeyFile /etc/pki/tls/private/localhost.key</code></pre>
<hr />
<h3 id="step-6-데몬-및-기타-작업">Step 6. 데몬 및 기타 작업</h3>
<pre><code class="language-bash">[root@ns conf.d]# systemctl restart httpd
nets[root@ns conf.d]# netstat -natlp | grep httpd
tcp6       0      0 :::80                   :::*                    LISTEN      57379/httpd
tcp6       0      0 :::443                  :::*                    LISTEN      57379/httpd

[root@ns conf.d]# lsof -i tcp:443
COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
httpd   57379   root    6u  IPv6  94823      0t0  TCP *:https (LISTEN)
httpd   57380 apache    6u  IPv6  94823      0t0  TCP *:https (LISTEN)
httpd   57381 apache    6u  IPv6  94823      0t0  TCP *:https (LISTEN)
httpd   57382 apache    6u  IPv6  94823      0t0  TCP *:https (LISTEN)
httpd   57383 apache    6u  IPv6  94823      0t0  TCP *:https (LISTEN)
httpd   57384 apache    6u  IPv6  94823      0t0  TCP *:https (LISTEN)</code></pre>
<hr />
<h3 id="step-7-사이트-출력">Step 7. 사이트 출력</h3>
<ul>
<li><p>외부망 차단 (도메인 출력할 수 있도록)</p>
<pre><code class="language-bash">[root@ns conf.d]# vi /etc/resolv.conf
# Generated by NetworkManager
search gusiya.com
nameserver 192.168.10.128</code></pre>
</li>
<li><p>https 전용 포트 추가 <code>(443)</code></p>
<pre><code class="language-bash">[root@ns conf.d]# firewall-cmd --permanent --add-port=443/tcp
[root@ns conf.d]# firewall-cmd --permanent --add-service=https
[root@ns conf.d]# firewall-cmd --reload</code></pre>
</li>
<li><p>데몬 실행</p>
<pre><code class="language-bash">[root@ns conf.d]# systemctl restart httpd</code></pre>
</li>
<li><p>사이트 출력
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1cdb6393-0a1d-47d3-a65e-ebbe996dc54f/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3b2a95fa-e58d-45b1-a3fe-bde417325fd7/image.png" /></p>
</li>
</ul>