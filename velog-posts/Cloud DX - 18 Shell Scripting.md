# Cloud DX - 18 Shell Scripting

- 📅 Published: Wed, 22 Oct 2025 10:02:25 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-18-Shell-Scripting)

<hr />
<h1 id="span-style--colorred-shell-scriptingspan"><span style="color: red;"> Shell Scripting</span></h1>
<h2 id="개요">개요</h2>
<ul>
<li>CLI Mode에서 실행되는 명령어들을 <code>병합</code> 또는 <code>조합</code>을 통해 마치 <code>새로운 명령어</code>를 생성하는 것과 같다. </li>
<li>즉, 있는 명령어들을 한 개의 새로운 명령으로 만들고 그를 통해 한 개의 새로운 명령 안에 기록된 명령어들을 한 번에 실행할 수가 있다.</li>
</ul>
<hr />
<h2 id="실습-1-기본-예제">실습 1. 기본 예제</h2>
<h3 id="이해-1-shell-scripting-사용하지-않았을-경우의-출력">이해 1. <code>Shell Scripting</code> 사용하지 않았을 경우의 출력</h3>
<ul>
<li><p>소스코드</p>
<pre><code class="language-bash">[root@localhost ksh]# SAM=samadal
[root@localhost ksh]# echo SAM
SAM
[root@localhost ksh]# echo $SAM
samadal</code></pre>
</li>
<li><p><code>SAM=samadal</code></p>
<ul>
<li><code>변수=값</code> 형태에서 <code>=</code>는 <code>같다</code>라는 뜻이 아니라 우항의 값을 좌항에 대입해라.</li>
<li>변수 선언<code>SAM</code>이라는 변수에 <code>samadal</code>이라는 값을 대입해라</li>
</ul>
</li>
<li><p><code>echo SAM</code> </p>
<ul>
<li>변수의 값을 화면에 출력</li>
<li><code>SAM</code>이 그대로 출력 </li>
</ul>
</li>
</ul>
<ul>
<li><code>echo $SAM</code><ul>
<li><code>SAM</code>이라는 변수의 값을 화면에 출력</li>
<li>변수의 값을 출력할 때는 반드시 <code>$</code>를 붙여야 한다.</li>
</ul>
</li>
</ul>
<ul>
<li><p>이해 2. <code>Shell Scripting</code> 사용한 경우의 출력</p>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bc66ae23-4897-453f-b41f-f213328954ca/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3cbee3c1-3cb0-488f-94dd-bcc29df2059f/image.png" /></p>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="span-style--colorskybluefor문span"><span style="color: skyblue;">for문</span></h2>
<h3 id="for1bash-매개변수를-이용한-출력">for1.bash (매개변수를 이용한 출력)</h3>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1ea4b6f8-dd4b-4e20-8936-8c3adac80c69/image.png" /></li>
</ul>
<h3 id="for2bash-사용자-정보-중에서-samadal-필드만-출력">for2.bash (사용자 정보 중에서 <code>samadal</code> 필드만 출력</h3>
<ul>
<li><code>grep</code>, <code>sed</code>, <code>awk</code><pre><code class="language-bash">#!/bin/bash
</code></pre>
</li>
</ul>
<p>for i in <code>grep 'samadal' /etc/passwd | sed 's/:/ /' | awk '{print $1}'</code>
do
        echo &quot;$i&quot;
done</p>
<pre><code>- `cat`, `sed`, `awk`
- `cat`, `sed`, `awk` (변수 치환)
- `grep`, `sed`
```bash
#!/bin/bash

for i in $(grep 'samadal' /etc/passwd | sed 's/:.*//')
do
        echo &quot;$i&quot;
done</code></pre><hr />
<h2 id="span-style--colorskyblueif-문span"><span style="color: skyblue;">if 문</span></h2>
<ul>
<li><code>ksh</code>에서 <code>print</code> , <code>echo</code> 모두 동작</li>
<li><code>bash</code>에서는 <code>echo</code> 만 동작</li>
<li>문자열은 <code>공백 x</code> 숫자만 <code>공백 허용</code><h3 id="if1bash-숫자">if1.bash (숫자)</h3>
</li>
<li>공백 없어도 실행 가능</li>
<li>() 소괄호 사용<pre><code class="language-bash">#!/bin/bash
</code></pre>
</li>
</ul>
<p>A=40</p>
<p>if((A&gt;30)) # 공백 없어도 실행 가능, </p>
<h1 id="-소괄호-사용">() 소괄호 사용</h1>
<p>then
        echo &quot;True&quot;
else
        echo &quot;False&quot;
fi</p>
<pre><code>
### if2.bash (문자열)
- 문자열은 공백 있어야 실행 
- [] 대괄호 사용

```bash
#!/bin/bash

A=samadal

if [[ $A = samaadal ]] # 문자열은 공백 있어야 실행 
# [] 대괄호 사용
then
        echo &quot;Correct&quot;
else
        echo &quot;Incorrect&quot;
fi</code></pre><h3 id="if3bash-문자열-부정문">if3.bash (문자열) 부정문</h3>
<pre><code class="language-bash">#!/bin/bash

A=samadal

if [[ $A != samadal ]]
then
        echo &quot;Correct&quot;
else
        echo &quot;Incorrect&quot;
fi</code></pre>
<h3 id="if4bash">if4.bash</h3>
<ul>
<li>마운트 정보중 에서 맨 마지막이 <code>/</code>로 끝나느 부분의 <code>5th.</code> 필드의 값만 출력 (기호 제외)<pre><code class="language-bash">#!/bin/bash
</code></pre>
</li>
</ul>
<p>A=<code>df -h | grep '\/$' | awk '{print $5}' | sed 's/%//'</code>
A=<code>df -h | awk '/\/$/ {print $5}' | sed 's/%//'</code>
B=$A</p>
<p>if [[ $B = $A ]]
then
        echo $A
else
        echo &quot;Not Value&quot;
fi</p>
<pre><code>
### if5.bash 
- `컴퓨터 언어`에서의 `if문`
```python
if (조건문1) { ... }         → 단일 조건문
else { ... }</code></pre><pre><code class="language-python">if (조건문1) { ... }         →  다중 조건문
else if (조건문2) { ... }
else if (조건문3) { ... }
...
else { ... }</code></pre>
<pre><code class="language-python">#!/bin/bash

US=user1
A=`cat /etc/passwd | grep $US | awk '{print $1}' | sed 's/:.*//'`
B=`cat /etc/passwd | grep $US | sed 's/:/ /g' | awk '{print $5}'`

if [[ $A = $US ]]
then
        echo &quot;user is Alive&quot;
elif [[ -d $B ]]
then
        echo &quot;User is Directory&quot;
else
        echo &quot;User is not exist&quot;
        mkdir -p /export/home/
        useradd -d /export/home/$US $US
        cat /etc/passwd | grep $US
fi</code></pre>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4976dc3e-cdf9-4490-979b-cde3331f87cd/image.png" /></li>
</ul>
<hr />
<h2 id="case문">case문</h2>
<h3 id="case1bash">case1.bash</h3>
<pre><code class="language-bash">#!/bin/bash

case &quot;$1&quot; in
        start)
                echo &quot;START&quot;
                ;;
        stop)
                echo &quot;STOP&quot;
                ;;
        *)
                echo &quot;Usage : $0 [start | stop]&quot;
                ;;
esac</code></pre>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b2a7bb0f-a9a3-4415-83a0-a270edafe361/image.png" /></li>
</ul>
<h3 id="case2bash">case2.bash</h3>
<pre><code class="language-bash">#!/bin/bash

US=user2

case $US in
        user1)
                echo &quot;User1&quot;
                ;;
        user2)
                useradd -d /export/home/$US $US
                cat /etc/passwd | grep $US
                ;;
        *)
                echo &quot;None&quot;
                ;;
esac</code></pre>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4f70aa1e-f2e2-4951-ad51-88a6fd5c5cfe/image.png" /></li>
</ul>
<h3 id="case3bash">case3.bash</h3>
<pre><code class="language-bash">#!/bin/bash

read US

case $US in
        user1)
                echo &quot;Exist&quot;
                ;;
        user2)
                useradd -d /export/home/$US $US
                cat /etc/passwd | grep $US
                ;;
        *)
                echo &quot;Not insert&quot;
                ;;
esac</code></pre>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c251cbeb-fff8-4459-8aac-27e7118b6b7c/image.png" /></li>
</ul>
<hr />
<h2 id="실습-2-응용-예제">실습 2. 응용 예제</h2>
<h3 id="예제-1-사용자를-생성할-수-있는-쉘clouduserbash을-코딩">예제 1. 사용자를 생성할 수 있는 쉘(/cloud/user.bash)을 코딩</h3>
<hr />
<h3 id="예제-2-사용자-관련-모든-쉘을-메인-쉘에서-실행">예제 2. 사용자 관련 모든 쉘을 '메인' 쉘에서 실행</h3>
<ul>
<li><p>개요
 : 사용자 메인   → /cloud/user/user_main.bash
 : 사용자 생성   → /cloud/user/user_add.bash
 : 사용자 삭제   → /cloud/user/user_del.bash
 : 사용자 수정   → /cloud/user/user_mod.bash</p>
</li>
<li><p>작업
 : 단, 모든 작업 및 종료는 사용자 메인(user_main.bash)을 통해서만 실행되도록 할 것</p>
</li>
</ul>
<hr />
<h3 id="예제-3">예제 3.</h3>
<p>   -&gt; 개요
   : 최상위  메뉴            → /cloud/main.bash
   : 패키지, 포트, 서비스, 데몬      → /cloud/main_pd.bash
   : User               → /cloud/main_us.bash
   : HDD &amp; Partition         → /cloud/main_hp.bash
   -&gt; 작업
   : 단, 모든 작업 및 종료는 '최상위 메뉴(main.bash)'을 통해서만 실행되도록 할 것</p>