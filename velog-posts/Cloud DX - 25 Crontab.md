# Cloud DX - 25 Crontab

- 📅 Published: Mon, 03 Nov 2025 08:37:06 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-25-Crontab)

<hr />
<h1 id="span-style--colorskybluecrontabspan"><span style="color: skyblue;">Crontab</span></h1>
<h2 id="개요">개요</h2>
<ul>
<li><code>시스템</code>에서 특정 시간에 원하는 작업을 수행할 수 있도록 해주는 <code>스케쥴링</code></li>
<li><code>(목적)</code> <code>시스템 백업</code>, <code>점검</code> 등과 같은 주로 새벽 시간대에 해야 하는 작업들을 자동적으로 해 주는 용도로 사용된다.</li>
<li>실무에서는 <code>Shell Scripting</code>과 함께 많이 사용된다.</li>
</ul>
<h2 id="주의-사항">주의 사항</h2>
<ul>
<li><code>현재 시간</code>을 기준으로 적용되기 때문에 작업할 때는 시스템의 시간을 정확하게 설정해야만 한다. </li>
<li>시간 설정은, KST(한국 표준시, Korea Standard Time)의 <code>타임서버</code>의 정보를 적용<code>(rate -s time.bora.net)</code> 하면 된다.</li>
</ul>
<h2 id="사용법">사용법</h2>
<h3 id="명령어">명령어</h3>
<pre><code class="language-bash">crontab -u &lt;사용자명&gt; &lt;옵션&gt;</code></pre>
<h3 id="옵션">옵션</h3>
<ul>
<li><p>예약된 작업 생성, 수정</p>
<pre><code class="language-bash">crontab -e</code></pre>
</li>
<li><p>예약된 작업 리스트 확인</p>
<pre><code class="language-bash">crontab -l </code></pre>
</li>
<li><p>예약된 작업 삭제</p>
<pre><code class="language-bash">crontab -r</code></pre>
<h3 id="입력-형태">입력 형태</h3>
<pre><code class="language-bash">&lt;분&gt; &lt;시&gt; &lt;일&gt; &lt;월&gt; &lt;요일&gt; &lt;명령어&gt;</code></pre>
</li>
<li><p><code>분</code> :         <code>0</code> ~ <code>59</code></p>
</li>
<li><p><code>시</code>:        <code>0</code> ~ <code>23</code></p>
</li>
<li><p><code>일</code> :        <code>1</code> ~ <code>31</code></p>
</li>
<li><p><code>월</code> :        <code>1</code> ~ <code>12</code></p>
</li>
<li><p><code>요일</code> :        <code>0(일요일)</code> ~<code>6(토요일)</code></p>
</li>
<li><p><code>명령어</code> :         <code>리눅스</code>에서 사용 가능한 모든 명령어</p>
</li>
<li><p>명령어 필드를 제외한 나머지 5개 필드에 <code>*</code>가 있는 경우에는 모든 것을 의미한다.</p>
</li>
<li><p>즉, 매분, 매일, 매월, 매주를 의미 한다.</p>
</li>
</ul>
<hr />
<h3 id="실습-1-기본-실습">실습 1. 기본 실습</h3>
<ul>
<li>예제 1. 다음의 조건으로 작업  <ul>
<li>매분, 매시, 매일, 매월, 매주마다 <code>/export/home/samadal</code>에 빈 문서 파일을 생성한다.</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1511e0bd-f27e-40e5-b207-d235dd4c9041/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>예제 2. 매주 화요일 새벽 1시 20분'에 '접속한 사용자 목록'을 '파일(/cloud/who.log)'로 저장한다.
단, '1시 19분'에 '디렉터리(/cloud)'를 먼저 생성하도록 한다.</li>
</ul>
<pre><code class="language-bash">19 1 * * 2 mkdir /cloud
20 1 * * 2 who &gt; /cloud/who.log</code></pre>
<hr />
<ul>
<li>예제 3. 매주 화요일 새벽 1시 21분'에 '접속한 사용자 목록'을 '/tmp/'로 이동한 후 '디렉토리(/cloud)'를 삭제한다. <pre><code class="language-bash">19 1 * * 2 mkdir /cloud
20 1 * * 2 who &gt; /cloud/who.log
21 1 * * 2 mv /cloud/who.log /tmp; rmdir /cloud</code></pre>
</li>
</ul>
<hr />
<ul>
<li>예제 4. 매일 새벽 6시 정각에 접속한 사용자 목록을 파일(/cloud/who.log)로 저장하고 '/tmp'로 이동한 후 디렉터리(/cloud)를 삭제한다.
단, 모든 내용(디렉터리 생성, 생성되는 파일)은 'Shell Scripting'으로 설정한다.<pre><code class="language-bash"># w.bash
mkdir /cloud
who &gt; /cloud/who.log
mv /cloud/who.log /tmp
rm -rf /cloud</code></pre>
<pre><code class="language-bash">chmod 700 /export/home/samadal/w.bash
</code></pre>
</li>
</ul>
<p>0 6 * * * /export/home/samadal/w.bash</p>
<pre><code>---
- 예제 5. 다음의 조건으로 작업 
2025년 10월 27일 오후 5시 25분에 사용자 정보 중 'samadal'에 대한 정보만 파일로 저장한다.
단, 출력된 내용의 저장은 /export/home/samadal'에'samadal_102717252025.txt' 파일로 저장하고 이 때 '시간정보는 자동으로 입력'되도록 한다.
```bash
grep samadal /etc/passwd &gt; samadal_`date +'%m%d%H%M%Y'`.txt</code></pre><pre><code class="language-bash">25 17 27 10 * grep samadal /etc/passwd &gt; /export/home/samadal/samadal_`date +'\%m\%d\%H\%M\%Y'`.txt</code></pre>
<hr />
<blockquote>
<h2 id="date의-특수-기능">date의 특수 기능</h2>
</blockquote>
<pre><code class="language-bash">date +'%@'</code></pre>
<table>
<thead>
<tr>
<th>옵션</th>
<th>설명</th>
<th>예시 출력</th>
</tr>
</thead>
<tbody><tr>
<td><code>+%Y</code></td>
<td>연도 (4자리)</td>
<td><code>2025</code></td>
</tr>
<tr>
<td><code>+%y</code></td>
<td>연도 (2자리)</td>
<td><code>25</code></td>
</tr>
<tr>
<td><code>+%m</code></td>
<td>월 (2자리)</td>
<td><code>11</code></td>
</tr>
<tr>
<td><code>+%d</code></td>
<td>일 (2자리)</td>
<td><code>02</code></td>
</tr>
<tr>
<td><code>+%H</code></td>
<td>시 (24시간제)</td>
<td><code>14</code></td>
</tr>
<tr>
<td><code>+%I</code></td>
<td>시 (12시간제)</td>
<td><code>02</code></td>
</tr>
<tr>
<td><code>+%M</code></td>
<td>분</td>
<td><code>30</code></td>
</tr>
<tr>
<td><code>+%S</code></td>
<td>초</td>
<td><code>15</code></td>
</tr>
<tr>
<td><code>+%A</code></td>
<td>요일 이름 (전체)</td>
<td><code>Sunday</code></td>
</tr>
<tr>
<td><code>+%a</code></td>
<td>요일 이름 (약어)</td>
<td><code>Sun</code></td>
</tr>
<tr>
<td><code>+%w</code></td>
<td>요일 번호 (0:일요일 ~ 6:토요일)</td>
<td><code>0</code></td>
</tr>
<tr>
<td><code>+%W</code></td>
<td>올해의 주차 (월요일 시작)</td>
<td><code>43</code></td>
</tr>
<tr>
<td><code>+%j</code></td>
<td>올해의 몇 번째 날</td>
<td><code>306</code></td>
</tr>
<tr>
<td><code>+%s</code></td>
<td>1970년 1월 1일 이후 경과 초 (Unix Time)</td>
<td><code>1762032310</code></td>
</tr>
<tr>
<td><code>+%D</code></td>
<td>미국식 날짜 (MM/DD/YY)</td>
<td><code>11/02/25</code></td>
</tr>
<tr>
<td><code>+%F</code></td>
<td>날짜 (YYYY-MM-DD) *****</td>
<td><code>2025-11-02</code></td>
</tr>
<tr>
<td><code>+%T</code></td>
<td>시간 (HH:MM:SS) *****</td>
<td><code>14:30:15</code></td>
</tr>
<tr>
<td><code>+%R</code></td>
<td>시간 (HH:MM, 초 제외)</td>
<td><code>14:30</code></td>
</tr>
<tr>
<td><code>+%c</code></td>
<td>현재 날짜와 시간 (로컬 형식)</td>
<td><code>Sun Nov  2 14:30:15 2025</code></td>
</tr>
<tr>
<td><code>+%Z</code></td>
<td>시간대</td>
<td><code>KST</code></td>
</tr>
</tbody></table>
<hr />
<ul>
<li>예제 6. 다음의 조건으로 작업
'129번' 시스템에서 CD-ROM을 마운트 한 후 mariadb로 시작하는 모든 페키지를 /cloud 디렉터리에 복사한 후 '130번' 시스템의 '/export/home/samadal/mariadb.tar.gz'라는 파일로 복사할 것이 작업은 매일 새벽 5시 30분에 실행되도록 할 것</li>
</ul>