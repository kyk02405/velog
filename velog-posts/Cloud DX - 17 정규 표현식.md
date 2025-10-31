# Cloud DX - 17 정규 표현식

- 📅 Published: Wed, 22 Oct 2025 05:35:10 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-17-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D)

<hr />
<h1 id="span-style--colororange정규-표현식-1-grep-span"><span style="color: orange;">정규 표현식 1. <code>grep</code> </span></h1>
<h3 id="개요">개요</h3>
<ul>
<li>특정 조건에 맞는 문자열의 패턴을 검색(필터링)한다.</li>
<li>(특징) 줄(행) 단위로 출력된다.</li>
</ul>
<hr />
<h2 id="실습-1-특정-문자열-검색">실습 1. 특정 문자열 검색</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/34f7c669-e703-4bc9-b557-fd8758f1c9a7/image.png" /></p>
<h3 id="예제-1">예제 1.</h3>
<ul>
<li><code>grep '^samadal' /etc/passwd</code><ul>
<li>특정 라인에서 라인의 맨 앞에 <code>samadal</code>인 문자열을 검색</li>
</ul>
</li>
<li><code>grep 'samadal$' /etc/passwd</code><ul>
<li>특정 라인에서 라인의 맨 뒤에 <code>samadal</code>인 문자열을 검색</li>
</ul>
</li>
<li><code>grep '\&lt;samadal' /etc/passwd</code><ul>
<li>특정 라인에서 라인의 임의의 위치에 <code>첫 문자</code>가 <code>samadal</code>인 문자열을 검색</li>
</ul>
</li>
<li><code>grep 'samadal\&gt;' /etc/passwd</code><ul>
<li>특정 라인에서 라인의 임의의 위치에 <code>끝 문자</code>가 <code>samadal</code>인 문자열을 검색</li>
</ul>
</li>
</ul>
<hr />
<h3 id="예제-2-특정-라인에서-맨-앞에-sam으로-시작하는-모든-문자열-검색">예제 2. 특정 라인에서 맨 앞에 <code>sam</code>으로 시작하는 모든 문자열 검색</h3>
<pre><code class="language-bash">
[root@localhost sda2gb]# grep 'sam.*' /etc/passwd
samadal:x:1000:1000:samadal:/export/home/samadal:/bin/bash
[root@localhost sda2gb]#
[root@localhost sda2gb]# grep '^sam.*' /etc/passwd
samadal:x:1000:1000:samadal:/export/home/samadal:/bin/bash</code></pre>
<hr />
<h3 id="에제-3-연속되지-않는-문자일-경우">에제 3. 연속되지 않는 <code>문자</code>일 경우</h3>
<ul>
<li><code>grep '^[sam].*' /etc/passwd | nl</code><ul>
<li>특정 라인에서 임의로 시작된 첫 문자<code>(s, a, m 문자로 시작하는 모든것)</code>에 해당하는 모든 문자열 검색<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cb536ec8-c85d-4c79-a0be-093657493d66/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li><code>grep '^[^sam].*' /etc/passwd | nl</code><ul>
<li>특정 라인에서 임의로 시작된 첫 문자<code>(s, a, m 문자로 시작하는 모든것)</code>에 해당하지 않는 모든 문자열 검색</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d1b462f1-403d-4330-a6b5-55b576eb95ce/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="예제-4-연속되는-문자일-경우">예제 4. 연속되는 <code>문자</code>일 경우</h3>
<ul>
<li><p><code>grep '^[l-s]' /etc/passwd | nl</code></p>
<ul>
<li>특정 라인에서 임의로 시작된 첫 문자가 연속된 문자<code>(l, m, n, o, p, q, r, s)</code>에 해당하는 모든 문자열 검색</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/32245204-b1dc-40b4-89cb-6943f52b450e/image.png" /></li>
</ul>
</li>
<li><p><code>grep '^[^l-s]' /etc/passwd | nl</code></p>
<ul>
<li><ul>
<li>특정 라인에서 임의로 시작된 첫 문자가 연속된 문자<code>(l, m, n, o, p, q, r, s)</code>에 해당하지 않는 모든 문자열 검색</li>
</ul>
</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1e7e5728-f555-44f1-8a2f-37ba31e04a41/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="예제-5">예제 5.</h3>
<ul>
<li><p>특정 라인에서 임의의 문자로 끝나는 모든 문자열 검색</p>
<ul>
<li><p><code>grep '\bash$' /etc/passwd | nl</code> &gt; 안나옴</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f1054b20-339b-4569-91f5-7dfedde71ca0/image.png" /></li>
</ul>
</li>
<li><p><code>grep '\nologin$' /etc/passwd | nl</code></p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9a36ceb9-4cce-4dea-abaf-d65265ac76f3/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p>특정 라인에서 임의의 문자로 끝나지 않는 모든 문자열 검색</p>
<ul>
<li><code>grep '[^:$]' /etc/passwd | nl</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d2d04224-0c1e-4745-984e-30020d759663/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="예제-6">예제 6.</h3>
<ul>
<li><p>특정 라인에서 첫 문자가 <code>s-u</code> 범위 안에서  시작하고 다음 문자가 <code>a-z</code>로 시작하는 문자열 검색</p>
<ul>
<li><code>grep '^[s-u][a-z]'  /etc/passwd | nl</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/05e2eb44-c954-48a6-baf4-12cd74b8795d/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p>특정 라인에서 첫 문자가 <code>s-u</code> 범위 안에서  시작하지 않고 다음 문자가 <code>a-z</code>로 시작하는 문자열 검색</p>
<ul>
<li><code>grep '^[^s-u][a-z]'  /etc/passwd | nl</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/80762e4d-7883-4778-aa48-362a909e75eb/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li>특정 문자열로 검색하고 싶지 않은 문자열 검색<ul>
<li><code>grep -v 'samadal' /etc/passwd | nl</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a93e87b4-3134-4431-a734-8bcdcac3d200/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="실습-2-패턴-검색">실습 2. 패턴 검색</h2>
<h3 id="예제-1-1">예제 1.</h3>
<ul>
<li><p>특정 디렉토리 안에 <code>daemon</code> 명령어를 포함하는 파일 검색</p>
<ul>
<li><code>grep 'daemon' /etc/init.d/* | nl</code></li>
</ul>
</li>
<li><p>특정 디렉토리 안에 <code>daemon</code> 명령어를 포함하는 파일의 목록 검색</p>
<ul>
<li><code>grep 'daemon' -l /etc/init.d/* | nl</code></li>
</ul>
</li>
</ul>
<hr />
<h3 id="예제-2">예제 2.</h3>
<ul>
<li><p>임의의 문자(.)를 포함하는 라인 검색</p>
<ul>
<li><code>grep '\.' /etc/passwd | nl</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/df41fa87-81bf-4cf0-a001-c18b7378f2ef/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p>임의의 문자열(samadal)을 포함하는 라인 검색</p>
<ul>
<li><code>grep 'samadal' /etc/passwd | nl</code></li>
<li><code>문자열</code> 검색은 <code>/</code> 빼야함 <ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/05a8b908-238c-4706-b6e9-ee3e165857b8/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p>결과값 중에서 <code>/</code>로 끝나는 라인 검색</p>
<ul>
<li><code>df -h | grep '\/$' | nl</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0d7c2346-4ae4-469c-807e-a3391e1b335e/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="span-style--colororange-정규-표현식-2-awk-span"><span style="color: orange;"> 정규 표현식 2. awk </span></h1>
<h3 id="개요-1">개요</h3>
<ul>
<li>특정 조건에 맞는 문자열의 패턴을 검색(필터링)한다.</li>
<li>(특징) 열 단위로 출력된다.</li>
</ul>
<h3 id="문법">문법</h3>
<ul>
<li><p>awk로 시작하는 경우</p>
<pre><code class="language-bash">(rocky96)# awk 'PATTERN' 파일명             → 'patern'은 찾으려는 문자열 (grep와 동일)
(rocky96)# awk '{ACTION}' 파일명            → '{ action }'은 nawk의 명령어
(rocky96)# awk '/PATTERN/ { ACTION } ' 파일명         → patern이 문자열일 경우 반드시 앞, 뒤에 ‘/’을 사용</code></pre>
</li>
<li><p>명령어의 결과를 이용하는 경우</p>
<pre><code class="language-bash">(rocky96)# COMMAND | awk 'PATTERN'
(rocky96)# COMMAND | awk '{ACTION}'
(rocky96)# COMMAND | awk '/PATTERN/ {ACTION}'</code></pre>
</li>
</ul>
<hr />
<h2 id="실습-1-패턴-출력">실습 1. 패턴 출력</h2>
<ul>
<li><p>임의의 필드(열)을 출력</p>
<ul>
<li><code>df -h | awk '{print $6, $5}'</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e3670d00-4d47-4ec3-97fb-058bb6f20d1e/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p>해당 파일에서 특정 문자열을 출력하되 <code>첫 번째 열</code>만 출력</p>
<ul>
<li><code>grep 'samadal' /sda2gb/passwd | awk '{print $1}'</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/dfc95553-e182-43ec-a453-126c45a7aa66/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li><p><code>/sda2gb/passwd</code> 안에서 명령실행</p>
<ul>
<li><code>grep 'samadal' `find /sda2gb -name passwd -type f` | awk '{print $1}'</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0dcb03ba-5573-4ae7-9077-024c6bf69350/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p>특정 문서 (/sda2gb/passwd)의 맨 뒤에 <code>halt</code>로 끝나는 라인을 출력 </p>
<ul>
<li><code>cat</code> ,<code>grep</code><ul>
<li><code>cat /sda2gb/passwd | grep '\halt$'</code></li>
</ul>
</li>
<li><code>grep</code><ul>
<li><code>grep '\halt' /sda2gb/passwd</code></li>
</ul>
</li>
<li><code>awk</code><ul>
<li><code>awk '/\halt/ {print}' /sda2gb//passwd</code></li>
<li><code>awk '/\halt/ {print $0}' /sda2gb//passwd</code></li>
</ul>
</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0db6c4af-4315-43f8-a649-d2e2a38cd75d/image.png" /></li>
</ul>
</li>
</ul>
<ul>
<li>마운트 정보의 <code>6번째 필드</code> 내용 중 <code>/</code>뒤에 <code>s</code>가 포함된 것을 출력<ul>
<li><code>df -h | grep '/s' | awk '{print $6}'</code></li>
<li><code>df -h | awk '{print $6}' | grep '\/s'</code></li>
<li><code>df -h | awk '/\/s/ {print $6}'</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c66cd4b2-07a0-4eb0-92d4-f45ff5e0eb7b/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="span-style--colororange-정규-표현식-3-sedspan"><span style="color: orange;"> 정규 표현식 3. sed</span></h2>
<h3 id="개요-2">개요</h3>
<ul>
<li>저장이 안되는 결과값(39%) 등을 저장하기 위해 <code>%</code>를 제거해주는 유틸리티이다.</li>
<li><code>메모리 버퍼(Memory Buffer)</code>에서 문자열을 편집하는 기능을 한다</li>
</ul>
<h2 id="실습">실습</h2>
<ul>
<li><p>마운트 정보 중 마운트 포인트가 <code>/</code>에서 다섯번 째 필드의 값을 기호(%)를 제거하고 출력</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1a6da043-b2d6-4f24-931e-afb0df198fb0/image.png" /></li>
</ul>
</li>
<li><p>변수로 치환 후 출력</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/90e4154e-8814-46ee-87e8-65f61328d5d0/image.png" /></li>
</ul>
</li>
<li><p>시스템의 사용자 정보 중 'samadal' 계정명만 출력</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/975a3c32-67fe-4003-83c6-10f7ae8ec12d/image.png" /></li>
</ul>
</li>
</ul>