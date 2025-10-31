# Cloud DX - 16 phpmyadmin & Zeroboard

- 📅 Published: Tue, 21 Oct 2025 12:00:13 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-16-phpmyadmin-Zeroboard)

<hr />
<h1 id="phpmyadmin--zeroboard">phpmyadmin &amp; Zeroboard</h1>
<h2 id="phpmyadmin">phpmyadmin</h2>
<h3 id="개요">개요</h3>
<ul>
<li>DB Server를 웹상에서 관리해주는 툴을 말한다.<ul>
<li><span style="color: red;">(매우 중요)</span></li>
</ul>
</li>
</ul>
<h2 id="프로그램파일-다운로드">프로그램(파일) 다운로드</h2>
<ul>
<li><code>https://www.phpmyadmin.net</code><ul>
<li>다운로드 받은 파일을 서버에 업로드 하기 위한 FTP Server 구축</li>
<li>서버 구축</li>
<li>파일 업로드</li>
<li>압축 해제</li>
<li>디렉토리 명 변경(phpmyadmin)</li>
</ul>
</li>
</ul>
<hr />
<h2 id="실습-1-웹에서의-db-관리-페이지phpmyadmin-출력">실습 1. 웹에서의 `DB 관리 페이지(phpmyadmin) 출력</h2>
<h3 id="사이트-출력-1-ip를-이용한-출력">사이트 출력 1. <code>IP</code>를 이용한 출력</h3>
<ul>
<li>개요<ul>
<li>웹 브라우저를 실행한 후 <code>IP</code>를 이용해서 출력한다.</li>
<li>계정<code>(main)</code>을 이용해서 사용자 지정 파일<code>(index.html)</code>를 출력한다.</li>
<li>이 때 문서 파일은 <code>FTP Server</code>를 구축한 후 업로드 하도록 한다.  </li>
</ul>
</li>
</ul>
<ul>
<li><p>Step 1. 패키지 설치</p>
<ul>
<li><code>Apache Web Server</code></li>
<li><code>FTP Server</code></li>
</ul>
</li>
<li><p>Step 2. 방화벽 수정</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/76f692f5-8a9b-4642-a016-f4d7399211d1/image.png" /></li>
</ul>
</li>
<li><p>Step 3. 사용자 생성</p>
<pre><code class="language-bash">[root@localhost samadal]# useradd -d /export/home/main main
[root@localhost samadal]# chmod 701 /export/home/main/
[root@localhost samadal]#
[root@localhost samadal]# password main</code></pre>
</li>
<li><p>Step 4. 환경 설정</p>
<pre><code class="language-bash">     (cent79)# vi /etc/httpd/conf/httpd.conf
    # DocumentRoot &quot;/var/www/html&quot;
    DocumentRoot &quot;/export/home/main&quot;
    ...
    # &lt;Directory &quot;/var/www/html&quot;&gt;
    &lt;Directory &quot;/export/home/main&quot;&gt;</code></pre>
<ul>
<li>Step 5. 데몬 실행<pre><code class="language-bash">   (cent79)# systemctl enable httpd
   (cent79)# systemctl enable vsftpd
   (cent79)# systemctl restart httpd
   (cent79)# systemctl restart vsftpd</code></pre>
-&gt; Step 6. 파일 생성 및 업로드
-&gt; Step 7. 사이트 출력</li>
</ul>
</li>
</ul>
<hr />
<h2 id="실습-1-엡에서의-db-관리-페이지phpmyadmin출력">실습 1. 엡에서의 <code>DB 관리 페이지</code>(phpmyadmin)`출력</h2>
<h3 id="사이트-출력-1-ip를-이용한-출력-1">사이트 출력 1. <code>ip</code>를 이용한 출력</h3>
<h3 id="사이트-출력-2-도메인gusiyacom을-이용한-출력">사이트 출력 2. <code>도메인(gusiya.com)</code>을 이용한 출력</h3>
<h3 id="사이트-출력-3-디렉토리-또는-계정을-이용한-출력">사이트 출력 3. 디렉토리 또는 계정을 이용한 출력</h3>
<h3 id="사이트-출력-4-phpmyadmin을-이용한-출력">사이트 출력 4. <code>phpmyadmin</code>을 이용한 출력</h3>
<ul>
<li><p>개요</p>
<ul>
<li>앞에서 다운로드하고 업로드 및 압축해제 했던 것들을 모두 삭제한다.</li>
</ul>
</li>
<li><p><code>wget</code>응 이용한 파일 다운로드</p>
<ul>
<li>다운로드 받고자 하는 URL 주소를 통해 다운로드를 할 수가 있다.
<code>phpMyAdmin-4.0.10.20-all-languages.zip</code> 링크복사</li>
</ul>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e0a676ea-bc99-45e3-ba73-1e784313bb8f/image.png" /></p>
</li>
</ul>
<h3 id="출력-1-패키지php-설치-전-출력">출력 1. 패키지(php) 설치 전 출력</h3>
<ul>
<li>압축 해제<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0b927485-8b16-44bc-875f-dd147e0e8d83/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bdc47a4b-477a-48a7-900f-338f930413d5/image.png" /></li>
</ul>
</li>
</ul>
<ul>
<li>디렉토리 이름 변경</li>
<li>Apache 데몬 재실행</li>
<li>사이트 출력 시 디렉토리 구조 형태로 출력된다.</li>
</ul>
<hr />
<h3 id="출력-2-패키지php-설치-후-출력">출력 2. 패키지(php) 설치 후 출력</h3>
<ul>
<li>패키지 설치(확인용)</li>
<li>저장소에서 php 버전 확인 1. 저장소 추가 전에 기존에 설치된 버전 확인<pre><code class="language-bash">[root@localhost named]# yum list php
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
Available Packages
php.x86_64                                      5.4.16-48.el7                                 base</code></pre>
</li>
</ul>
<hr />
<ul>
<li>저장소(repository) 추가 <ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d27be861-54cc-448f-8d12-56a3910ae42a/image.png" /></li>
</ul>
</li>
</ul>
<pre><code class="language-bash">yum -y install https://rpms.remirepo.net/enterprise/remi-release-7.rpm
yum -y epel-release yum-utils</code></pre>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/abd4a1f1-bd66-457b-a06d-a27ff261f8ff/image.png" /></li>
</ul>
<hr />
<ul>
<li>php 패키지 관련 저장소 활성화<pre><code class="language-bash">[root@localhost yum.repos.d]# yum-config-manager --enable remi-php74</code></pre>
</li>
</ul>
<hr />
<ul>
<li><p>저장소에서 php 버전 확인 2. 저장소를 통한 버전 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c92c162f-4716-443e-b502-787e97e28258/image.png" /></li>
</ul>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/734088b0-f997-47a3-87f1-9c0da3ab74de/image.png" /></p>
<blockquote>
<p>버젼 바뀜</p>
</blockquote>
</li>
</ul>
<hr />
<ul>
<li>php 패키지 설치</li>
</ul>
<hr />
<ul>
<li>php 패키지 관련 기타 패키지 설치<pre><code class="language-bash">yum -y install php-fpm
</code></pre>
</li>
</ul>
<p>yum -y install php-cli  php-redis  php-brotli php-intl php-gd php-gmp php-imap php-bcmath php-interbase php-json php-mbstring</p>
<p>yum -y install php-mysqlnd php-odbc php-opcache php-memcached php-tidy php-pdo php-pdo-dblib php-pear php-pgsql php-process</p>
<p>yum -y install php-pecl-apcu php-pecl-geoip php-pecl-imagick php-pecl-hrtime php-pecl-json php-pecl-memcache php-pecl-mongodb</p>
<p>yum -y install php-pecl-rar php-pecl-pq php-pecl-redis4 php-pecl-yaml php-pecl-zip --skip-broken</p>
<pre><code>
---
- 저장소에서 php 버전 확인 3. 패키지 설치 후에 버전 확인
  - ![](https://velog.velcdn.com/images/kyk02405/post/c92c162f-4716-443e-b502-787e97e28258/image.png)

---
- php 패키지 동작 상태 확인
  - `phpinfo.php` 파일 생성
    - ![](https://velog.velcdn.com/images/kyk02405/post/62a3bcfa-fbcb-4fba-a9fb-6a63d8750a45/image.png)

  - `'http://www.gusiya.com/phpinfo.php'`
  - 정상적인 사이트가 출력된다.
---
## 실습 1. 웹에서의 DB 관리자 페이지(phpmyadmin) 출력



---
## 실습 2. `Alter` 명령
### 준비 작업
### phpmyadmin 사이트 접속

### 실습 1.
- 왼쪽에 있는 `dbsamadal` 클릭 
- `새 테이블 만들기`에서 다음과 같이 입력하고 실행을 클릭한다
  - ![](https://velog.velcdn.com/images/kyk02405/post/37e81126-7ac9-4a3d-959f-ec7a4b1cd182/image.png)
  - ![](https://velog.velcdn.com/images/kyk02405/post/941aac3f-e8aa-4fa2-9a17-700a20621381/image.png)
- 터미널 창에서 확인
  - ![](https://velog.velcdn.com/images/kyk02405/post/826b20fd-caf3-4511-b45c-41cbc89b13d1/image.png)

---
### 실습 2. Alter 명령



---
# Zeroboard
## 개요
- 홈페이지 제작 및 관리를 도와주는 틀을 말한다.


---
## 실습 1. 게시판 출력
### 준비 작업
- DB 작업
- 제로보드 다운로드 및 업로드 

---
### 사이트 출력
- Step 1.설치 언어 선택
  - 한국어
- Step 2.사용권 동의
- Step 3.설치 조건 확인
  - chmod 707 xe/
- Step 4.FTP 정보 입력
- Step 5.DB 선택
  - `mysqli`
- Step 6.DB 정보 입력
  - ![](https://velog.velcdn.com/images/kyk02405/post/dda78421-2970-46e1-8e69-522c6683485f/image.png)

- Step 7.환경 설정
  - `Korea Standard`
- Step 8.관리자 정보 입력
  - ![](https://velog.velcdn.com/images/kyk02405/post/835ec975-5464-40b2-937b-16642e3ddc5b/image.png)
- ![](https://velog.velcdn.com/images/kyk02405/post/2b2055d3-a3ac-4b9c-83bb-1765dfb385d0/image.png)

---
## 실습 2. 팀 구성 ()
## 서버 구성 (DNS, DB, Web1, Web2)

## HDD 추가 (타입, 용량은 알아서) 

---
# DB
```bash
DNS: 김정호
SRV200
내부망: 192.168.78.100 / C클래스 / X / X
외부망: 10.10.10.78 / C클래스 / X / X
CentOs
내부망: 192.168.78.200 / C클래스 / 192.168.78.100 / 192.168.78.200

DB: 김경윤
SRV200
내부망: 192.168.77.100 / C클래스 / X / X
외부망: 10.10.10.77 / C클래스 / X / X
CentOs
내부망: 192.168.77.200 / C클래스 / 192.168.77.100 / 192.168.77.200

Web1: 유강현
SRV200
내부망: 192.168.76.100 / C클래스 / X / X
외부망: 10.10.10.76 / C클래스 / X / X
CentOs
내부망: 192.168.76.200 / C클래스 / 192.168.76.100 / 192.168.76.200

Web2: 채유진
SRV200
내부망: 192.168.75.100 / C클래스 / X / X
외부망: 10.10.10.75 / C클래스 / X / X
CentOs
내부망: 192.168.75.200 / C클래스 / 192.168.75.100 / 192.168.75.200</code></pre><hr />
<h3 id="패키지-설치">패키지 설치</h3>
<pre><code class="language-bash">yum install -y mariadb-server nfs-utils vsftpd httpd php php-mysqli</code></pre>
<hr />
<h3 id="서비스-활성화">서비스 활성화</h3>
<pre><code class="language-bash">systemctl enable --now mariadb
systemctl enable --now nfs-server rpcbind
systemctl enable --now vsftpd
systemctl enable --now httpd</code></pre>
<hr />
<h3 id="서비스-활성화-확인">서비스 활성화 확인</h3>
<pre><code class="language-bash">systemctl status mariadb nfs-server vsftpd httpd</code></pre>
<hr />
<h3 id="방화벽-설정">방화벽 설정</h3>
<pre><code class="language-bash">firewall-cmd --permanent --add-service=mysql
firewall-cmd --permanent --add-service=nfs
firewall-cmd --permanent --add-service=mountd
firewall-cmd --permanent --add-service=rpc-bind
firewall-cmd --permanent --add-service=ftp
firewall-cmd --permanent --add-service=http
firewall-cmd --reload</code></pre>
<pre><code class="language-bash">?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;zone&gt;
  &lt;short&gt;Public&lt;/short&gt;
  &lt;description&gt;For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.&lt;/description&gt;
  &lt;service name=&quot;ssh&quot;/&gt;
  &lt;service name=&quot;dhcpv6-client&quot;/&gt;
  &lt;service name=&quot;nfs&quot;/&gt;
  &lt;service name=&quot;http&quot;/&gt;
  &lt;service name=&quot;mountd&quot;/&gt;
  &lt;service name=&quot;rpc-bind&quot;/&gt;
  &lt;service name=&quot;ftp&quot;/&gt;
  &lt;service name=&quot;mysql&quot;/&gt;
  &lt;port protocol=&quot;tcp&quot; port=&quot;22&quot;/&gt;
  &lt;port protocol=&quot;tcp&quot; port=&quot;80&quot;/&gt;
  &lt;port protocol=&quot;tcp&quot; port=&quot;21&quot;/&gt;
  &lt;port protocol=&quot;tcp&quot; port=&quot;20&quot;/&gt;
  &lt;port protocol=&quot;tcp&quot; port=&quot;2049&quot;/&gt;
&lt;/zone&gt;</code></pre>
<hr />
<h3 id="폴더-생성-및-권한">폴더 생성 및 권한</h3>
<pre><code class="language-bash">mkdir /himedia
chmod 777 /himedia</code></pre>
<hr />
<h3 id="공유-폴더himedia-설정-nfs">공유 폴더(/himedia) 설정 (NFS)</h3>
<pre><code class="language-bash">/himedia 192.168.76.200(rw,no_root_squash,sync) 192.168.75.200(rw,no_root_squash,sync)</code></pre>
<hr />
<h3 id="적용">적용</h3>
<pre><code class="language-bash">exportfs -arv
rpcinfo -p</code></pre>
<hr />
<h3 id="zeroboard-및-phpmyadmin-파일-준비">Zeroboard 및 phpMyAdmin 파일 준비</h3>
<p><code>FTP</code>로 xe 파일 업로드</p>
<pre><code class="language-bash">cd /himedia
unzip xe.zip
chmod -R 707 xe</code></pre>
<hr />
<h3 id="php-테스트-파일-생성">PHP 테스트 파일 생성</h3>
<pre><code class="language-bash">echo &quot;&lt;?php phpinfo(); ?&gt;&quot; &gt; /himedia/phpinfo.php</code></pre>
<hr />
<h3 id="mariadb-초기-보안-설정">MariaDB 초기 보안 설정</h3>
<pre><code class="language-bash">mysql_secure_installation</code></pre>
<hr />
<h2 id="외부에서-db-server에-접근-허용">외부에서 DB Server에 접근 허용</h2>
<pre><code class="language-sql">MariaDB [mysql]&gt; grant all on dbsamadal.* to usersamadal@'localhost' identified by 'pwsamadal';
Query OK, 0 rows affected (0.00 sec)

MariaDB [mysql]&gt; grant all on dbsamadal.* to usersamadal@'%' identified by 'pwsamadal';
Query OK, 0 rows affected (0.00 sec)

MariaDB [mysql]&gt; grant all on dbsamadal.* to usersamadal@'192.168.77.200' identified by 'pwsamadal';
Query OK, 0 rows affected (0.00 sec)

MariaDB [mysql]&gt; select host, password, user from user;
+-----------------------+-------------------------------------------+-------------+
| host                  | password                                  | user        |
+-----------------------+-------------------------------------------+-------------+
| localhost             | *6F7FFFC8B3DA149E49312BC3090DAEA06CF8FC0E | root        |
| localhost.localdomain | *6F7FFFC8B3DA149E49312BC3090DAEA06CF8FC0E | root        |
| 127.0.0.1             | *6F7FFFC8B3DA149E49312BC3090DAEA06CF8FC0E | root        |
| ::1                   | *6F7FFFC8B3DA149E49312BC3090DAEA06CF8FC0E | root        |
| localhost             | *522D20E8BA620760F96F52AE32AD91F8F22BEC57 | usersamadal |
| %                     | *522D20E8BA620760F96F52AE32AD91F8F22BEC57 | usersamadal |
| 192.168.77.200        | *522D20E8BA620760F96F52AE32AD91F8F22BEC57 | usersamadal |
+-----------------------+-------------------------------------------+-------------+</code></pre>
<hr />
<h2 id="web에서-www1himediacom-접속-후-설치">Web에서 www1.himedia.com 접속 후 설치</h2>
<p><code>가입한 사용자 확인</code>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/878b8e28-25cd-4e7e-a94a-fdc41d973f83/image.png" /></p>