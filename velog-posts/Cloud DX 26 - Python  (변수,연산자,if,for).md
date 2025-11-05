# Cloud DX 26 - Python  (변수,연산자,if,for)

- 📅 Published: Tue, 04 Nov 2025 09:05:24 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-26-Python-%EB%B3%80%EC%88%98%EC%A0%9C%EC%96%B4%EB%AC%B8)

<h1 id="4-span-style--colorskyblue변수variablespan">4. <span style="color: skyblue;">변수(Variable)</span></h1>
<h2 id="411-변수-선언과-호출사용">4.1.1 변수 선언과 호출(사용)</h2>
<h3 id="선언">선언</h3>
<pre><code class="language-python">변수명 = (초기)값</code></pre>
<h3 id="호출">호출</h3>
<ul>
<li>print(변수명)을 이용해서 변수명이 가지고 있는 값을 출력한다.</li>
<li>변수명의 <code>값</code>을 <code>변경</code>할 수도 있다.</li>
<li>다른 변수의 <code>초기값</code>으로 지정할 수도 있다.</li>
<li><code>...</code></li>
</ul>
<h3 id="변수의-종류">변수의 종류</h3>
<ul>
<li><code>고정 변수</code><ul>
<li><code>값</code>을 미리 정해 놓고 사용하는 <code>변수</code>를 말한다.</li>
</ul>
</li>
<li><code>가변 변수</code><ul>
<li><code>값</code>을 받아와서 처리하는 <code>변수</code>를 말한다.</li>
</ul>
</li>
</ul>
<hr />
<h2 id="42-실습">4.2 실습</h2>
<h3 id="421-고정-변수">4.2.1 고정 변수</h3>
<ul>
<li>예제 1. 현재 원달러 환율은 1,287.34원이고 엔화 환율은 9.11원이다. 500달러를 엔화로 환전하면 몇 엔이 되는가?</li>
</ul>
<pre><code class="language-python">wpd, wpy, fh = 1287.34, 9.11, 500
fiveh = fh * wpd # 500달러를 원화로 환전
result = fiveh / wpy # 비례식 (1:wpy = x:5h)
print(&quot;Result : %.2f엔&quot; % result)
print(&quot;Result : {:.2f}엔&quot; .format(result))
print(f&quot;Result : {result:.2f}엔&quot;)</code></pre>
<pre><code>Result : 70655.32엔
Result : 70655.32엔
Result : 70655.32엔</code></pre><ul>
<li>예제 2. X극장 영화표는 11,000원이고 Y극장 영화표는 9,500원일 때 각각 극장 수익이 X극장(5,390,000,000), Y극장(7,521,245,000)이라고 한다.<ul>
<li>위와 같은 조건일 때 다음의 내용으로 값을 구하도록 한다.</li>
<li>각 극장의 관람객수는 얼마인가?</li>
<li>두 극장의 총 관람객 수는 얼마인가?</li>
<li>각 극장의 점유율은 얼마인가?<pre><code class="language-python">x, y = 11000, 9500
</code></pre>
</li>
</ul>
</li>
</ul>
<p>xm, ym = 5390000000, 7521245000</p>
<p>xcon = xm // x
ycon = ym // y</p>
<p>total = xcon + ycon</p>
<p>xper = xcon / total * 100
yper = ycon / total * 100</p>
<p>print(&quot;x 극장 : %s명 | y 극장 : %s명&quot; % (format(xcon, &quot;,&quot;), format(ycon, &quot;,&quot;)))
print(&quot;x 극장 : {:,}명 | y 극장 : {:,}명&quot;.format(xcon, ycon))
print(f&quot;x 극장 : {xcon:,}명 | y 극장 : {ycon:,}명&quot;)</p>
<p>print(&quot;총 관람객 수 : %s명&quot; % format(total, &quot;,&quot;))
print(&quot;총 관람객 수 : {:,}명&quot;.format(total))
print(f&quot;총 관람객 수 : {total:,}명&quot;)</p>
<p>print(&quot;x 극장 : %.2f%% | y 극장 : %.2f%%&quot; % (xper, yper))
print(&quot;x 극장 : {:.2f}% | y 극장 : {:.2f}%&quot;.format(xper, yper))
print(f&quot;x 극장 : {xper:.2f}% | y 극장 : {yper:.2f}%&quot;)</p>
<pre><code></code></pre><p>x 극장 : 490,000명 | y 극장 : 791,710명
x 극장 : 490,000명 | y 극장 : 791,710명
x 극장 : 490,000명 | y 극장 : 791,710명
총 관람객 수 : 1,281,710명
총 관람객 수 : 1,281,710명
총 관람객 수 : 1,281,710명
x 극장 : 38.23% | y 극장 : 61.77%
x 극장 : 38.23% | y 극장 : 61.77%
x 극장 : 38.23% | y 극장 : 61.77%</p>
<pre><code>
---
- 예제 3. 담배 1갑의 가격이 4,500원이고 하루에 1갑 반씩 담배를 피우는 사람의 경우 5000만원 가량의 차량을 구입하기 위해서는 몇 년동안 금연을 해야 하는가

```python
smo = 4500
harpsmo = 1.5 * smo
car = 50000000

day = car / harpsmo
year = 365

total = day / year

print(f&quot;{harpsmo:,.0f}원&quot;)
print(f&quot;{day:.0f}일&quot;)
print(f&quot;{total:.1f}년&quot;)</code></pre><pre><code>6,750원
7407일
20.3년</code></pre><hr />
<h2 id="422-가변-변수-input함수">4.2.2 가변 변수 (input()함수)</h2>
<blockquote>
<h3 id="개요">개요</h3>
</blockquote>
<ul>
<li>실행시 에러 구문이 다음과 같이 나타날 때
<code>TypeError: %d format: a real number is required, not str</code></li>
<li><code>input()</code> 함수로 받아들이는 모든 값은 문자열이다.</li>
</ul>
<h3 id="사용법">사용법</h3>
<pre><code class="language-python">변수명 = input()</code></pre>
<h3 id="실습-1-가변-변수의-이해">실습 1. 가변 변수의 이해</h3>
<pre><code class="language-python">var = input('값을 입력하세요 :')
print(&quot;{}을 입력받았다.&quot; .format(var))
print(&quot;%d을 입력받았다.&quot; % var)
print(type(var))</code></pre>
<h3 id="실습-2-input-함수로-받아들이는-모든-값은-문자열이다">실습 2. input() 함수로 받아들이는 모든 값은 문자열이다.</h3>
<pre><code class="language-python">var1 = input('문자열 입력:')
var2 = input('정수 입력:')
print(type(var1), type(var2))

print(&quot;문자열(%s) | 정수(%s)&quot; % (var1,var2))</code></pre>
<pre><code>문자열 입력:s
정수 입력:1
&lt;class 'str'&gt; &lt;class 'str'&gt;
문자열(s) | 정수(1)</code></pre><h3 id="실습-3-두-개의-정수값을-입력받은-후-사칙연산을-하는-소스">실습 3. 두 개의 정수값을 입력받은 후 사칙연산을 하는 소스</h3>
<pre><code class="language-python">var1 = int(input('숫자1 입력:'))
var2 = int(input('숫자2 입력:'))

plus = var1 + var2
minus = var1 - var2
multi = var1 * var2
div = var1 / var2

print(f&quot;{var1} + {var2} = {plus}&quot;)
print(f&quot;{var1} - {var2} = {minus}&quot;)
print(f&quot;{var1} * {var2} = {multi}&quot;)
print(f&quot;{var1} / {var2} = {div:.2f}&quot;)</code></pre>
<pre><code>숫자1 입력:5
숫자2 입력:3
8
5 + 3 = 8
5 - 3 = 2
5 * 3 = 15
5 / 3 = 1.67</code></pre><h3 id="실습-4-홍길동-씨의-과목3과목별-점수를-입력받은-후-합계와-평균을-구하는-소스">실습 4. 홍길동 씨의 과목(3과목)별 점수를 입력받은 후 합계와 평균을 구하는 소스</h3>
<pre><code class="language-python">mat = int(input('국어 점수 입력:'))
eng = int(input('영어 점수 입력:'))
kor = int(input('수학 점수 입력:'))

sum = mat + eng + kor 
avg = sum / 3

print(f&quot;과목 총합 점수 : {sum}점, 과목 평균 점수 : {avg:.1f}점&quot;)</code></pre>
<pre><code>국어 점수 입력:97
영어 점수 입력:76
수학 점수 입력:76
과목 총합 점수 : 249점, 과목 평균 점수 : 83.0점</code></pre><hr />
<h1 id="5-span-style--colorskyblue제어문span">5. <span style="color: skyblue;">제어문</span></h1>
<h2 id="51-연산자">5.1 연산자</h2>
<h3 id="511-개요">5.1.1 개요</h3>
<ul>
<li>제어문에서는 필수이다.</li>
<li>연산 시 사용되는 문자 등을 이용해서 다양한 형태를 표현할 수가 있다.</li>
</ul>
<h3 id="512-연산자의-종류">5.1.2 연산자의 종류</h3>
<h3 id="🔹-1-산술-연산자-arithmetic-operators">🔹 1. 산술 연산자 (Arithmetic Operators)</h3>
<blockquote>
<p>숫자끼리의 계산을 수행하는 연산자</p>
</blockquote>
<table>
<thead>
<tr>
<th align="center">연산자</th>
<th align="center">의미</th>
<th align="center">예시</th>
<th align="center">결과</th>
</tr>
</thead>
<tbody><tr>
<td align="center"><code>+</code></td>
<td align="center">더하기</td>
<td align="center"><code>7 + 3</code></td>
<td align="center">10</td>
</tr>
<tr>
<td align="center"><code>-</code></td>
<td align="center">빼기</td>
<td align="center"><code>7 - 3</code></td>
<td align="center">4</td>
</tr>
<tr>
<td align="center"><code>*</code></td>
<td align="center">곱하기</td>
<td align="center"><code>7 * 3</code></td>
<td align="center">21</td>
</tr>
<tr>
<td align="center"><code>/</code></td>
<td align="center">나누기</td>
<td align="center"><code>7 / 3</code></td>
<td align="center">2.333...</td>
</tr>
<tr>
<td align="center"><code>//</code></td>
<td align="center">나눗셈의 몫</td>
<td align="center"><code>7 // 3</code></td>
<td align="center">2</td>
</tr>
<tr>
<td align="center"><code>%</code></td>
<td align="center">나머지</td>
<td align="center"><code>7 % 3</code></td>
<td align="center">1</td>
</tr>
<tr>
<td align="center"><code>**</code></td>
<td align="center">제곱(거듭제곱)</td>
<td align="center"><code>7 ** 3</code></td>
<td align="center">343</td>
</tr>
</tbody></table>
<pre><code class="language-python">print(7 % 3)   # 7을 3으로 나눈 나머지 → 1
print(7 ** 3)  # 7의 3제곱 → 343</code></pre>
<hr />
<h3 id="🔹-2-비교-연산자-comparison-operators">🔹 2. 비교 연산자 (Comparison Operators)</h3>
<blockquote>
<p>두 값을 비교하여 <strong>True(참)</strong> 또는 <strong>False(거짓)</strong>을 반환</p>
</blockquote>
<table>
<thead>
<tr>
<th align="center">연산자</th>
<th align="center">의미</th>
<th align="center">예시</th>
<th align="center">결과</th>
</tr>
</thead>
<tbody><tr>
<td align="center"><code>==</code></td>
<td align="center">같다</td>
<td align="center"><code>a == b</code></td>
<td align="center">True / False</td>
</tr>
<tr>
<td align="center"><code>!=</code></td>
<td align="center">같지 않다</td>
<td align="center"><code>a != b</code></td>
<td align="center">True / False</td>
</tr>
<tr>
<td align="center"><code>&gt;</code></td>
<td align="center">크다</td>
<td align="center"><code>a &gt; b</code></td>
<td align="center">True / False</td>
</tr>
<tr>
<td align="center"><code>&lt;</code></td>
<td align="center">작다</td>
<td align="center"><code>a &lt; b</code></td>
<td align="center">True / False</td>
</tr>
<tr>
<td align="center"><code>&gt;=</code></td>
<td align="center">크거나 같다</td>
<td align="center"><code>a &gt;= b</code></td>
<td align="center">True / False</td>
</tr>
<tr>
<td align="center"><code>&lt;=</code></td>
<td align="center">작거나 같다</td>
<td align="center"><code>a &lt;= b</code></td>
<td align="center">True / False</td>
</tr>
</tbody></table>
<pre><code class="language-python">samadal = 1

if samadal != 1:
    print(&quot;False&quot;)
else:
    print(&quot;True&quot;)
# 결과 → True</code></pre>
<hr />
<h3 id="🔹-3-대입-연산자-assignment-operators">🔹 3. 대입 연산자 (Assignment Operators)</h3>
<blockquote>
<p>변수를 <strong>초기화</strong>하거나 기존 값에 <strong>연산 후 다시 저장</strong>할 때 사용</p>
</blockquote>
<table>
<thead>
<tr>
<th align="center">연산자</th>
<th align="center">의미</th>
<th align="center">예시</th>
<th align="center">같은 표현</th>
</tr>
</thead>
<tbody><tr>
<td align="center"><code>=</code></td>
<td align="center">대입</td>
<td align="center"><code>a = 3</code></td>
<td align="center">a에 3 저장</td>
</tr>
<tr>
<td align="center"><code>+=</code></td>
<td align="center">더해서 대입</td>
<td align="center"><code>a += 3</code></td>
<td align="center"><code>a = a + 3</code></td>
</tr>
<tr>
<td align="center"><code>-=</code></td>
<td align="center">빼서 대입</td>
<td align="center"><code>a -= 3</code></td>
<td align="center"><code>a = a - 3</code></td>
</tr>
<tr>
<td align="center"><code>*=</code></td>
<td align="center">곱해서 대입</td>
<td align="center"><code>a *= 3</code></td>
<td align="center"><code>a = a * 3</code></td>
</tr>
<tr>
<td align="center"><code>/=</code></td>
<td align="center">나눠서 대입</td>
<td align="center"><code>a /= 3</code></td>
<td align="center"><code>a = a / 3</code></td>
</tr>
<tr>
<td align="center"><code>%=</code></td>
<td align="center">나머지 대입</td>
<td align="center"><code>a %= 3</code></td>
<td align="center"><code>a = a % 3</code></td>
</tr>
<tr>
<td align="center"><code>//=</code></td>
<td align="center">몫 대입</td>
<td align="center"><code>a //= 3</code></td>
<td align="center"><code>a = a // 3</code></td>
</tr>
</tbody></table>
<pre><code class="language-python">a = 0
a += 3
print(a)  # 3

a = 3
a = a * 10  # 30
a *= 20     # 600
print(a)</code></pre>
<blockquote>
<p>⚠️ 대입 연산자는 반드시 <strong>초기값이 있어야 함</strong>
(예: <code>a += 1</code> 전에 <code>a</code>가 정의되어 있어야 함)</p>
</blockquote>
<hr />
<h3 id="🔹-4-논리-연산자-logical-operators">🔹 4. 논리 연산자 (Logical Operators)</h3>
<blockquote>
<p><code>True</code>, <code>False</code> 값으로 <strong>조건을 결합</strong>하거나 <strong>부정</strong>할 때 사용</p>
</blockquote>
<table>
<thead>
<tr>
<th align="center">연산자</th>
<th align="center">의미</th>
<th align="center">예시</th>
<th align="center">결과</th>
</tr>
</thead>
<tbody><tr>
<td align="center"><code>and</code></td>
<td align="center">둘 다 참이면 참</td>
<td align="center"><code>True and True</code></td>
<td align="center">True</td>
</tr>
<tr>
<td align="center"><code>or</code></td>
<td align="center">하나라도 참이면 참</td>
<td align="center"><code>True or False</code></td>
<td align="center">True</td>
</tr>
<tr>
<td align="center"><code>not</code></td>
<td align="center">참/거짓 반전</td>
<td align="center"><code>not True</code></td>
<td align="center">False</td>
</tr>
</tbody></table>
<pre><code class="language-python">x, y = True, False

if x and y:
    print(&quot;OK&quot;)
else:
    print(&quot;Fail&quot;)
# 결과 → Fail</code></pre>
<hr />
<h2 id="✳️-정리-요약">✳️ 정리 요약</h2>
<table>
<thead>
<tr>
<th align="left">구분</th>
<th align="left">주요 연산자</th>
<th align="left">설명</th>
</tr>
</thead>
<tbody><tr>
<td align="left"><strong>산술 연산자</strong></td>
<td align="left"><code>+ - * / // % **</code></td>
<td align="left">수학적 계산 수행</td>
</tr>
<tr>
<td align="left"><strong>비교 연산자</strong></td>
<td align="left"><code>== != &lt; &gt; &lt;= &gt;=</code></td>
<td align="left">두 값 비교 (True/False 반환)</td>
</tr>
<tr>
<td align="left"><strong>대입 연산자</strong></td>
<td align="left"><code>= += -= *= /= //=</code></td>
<td align="left">변수에 값 저장 또는 갱신</td>
</tr>
<tr>
<td align="left"><strong>논리 연산자</strong></td>
<td align="left"><code>and or not</code></td>
<td align="left">조건문에서 논리 판단</td>
</tr>
</tbody></table>
<hr />
<h1 id="span-style--colorskyblue52-if-문span"><span style="color: skyblue;">5.2 if 문</span></h1>
<h3 id="521-개요">5.2.1 개요</h3>
<blockquote>
<ul>
<li>조건식이 참이면 문장이 처리되고 거짓이면 아무것도 실행하지 않고 종료</li>
</ul>
</blockquote>
<ul>
<li>조건식은 연산자를 이용해서 표현한다.</li>
</ul>
<h3 id="522-단일-if문">5.2.2 단일 if문</h3>
<ul>
<li>문법<pre><code class="language-python">if 조건식:
  수행할 문장1
  수행할 문장2
  ...</code></pre>
</li>
<li>주의사항<ul>
<li>들여쓰기 내여쓰기에 따른 오류를 항상 신경쓰도록 한다.</li>
</ul>
</li>
</ul>
<h3 id="실습">실습</h3>
<ul>
<li><p>매개변수를 이용한 출력</p>
<pre><code class="language-python">x, y = 15, 10
if x &gt; y:
  print(&quot;15는 10보다 크다&quot;)
  print(f&quot;{x}는 {y}보다 크다&quot;)</code></pre>
<pre><code>15는 10보다 크다
15는 10보다 크다</code></pre></li>
<li><p>인수값을 이용한 출력</p>
<pre><code class="language-python">x = 15
if x in (10, 11, 15):
  print(&quot;주어진 값과 비교값 %d는 동일하다&quot; % x)
  print(&quot;주어진 값과 비교값 {}는 동일하다&quot; .format(x))
  print(f&quot;주어진 값과 비교값 {x}는 동일하다&quot;)</code></pre>
<pre><code>주어진 값과 비교값 15는 동일하다
주어진 값과 비교값 15는 동일하다
주어진 값과 비교값 15는 동일하다</code></pre></li>
<li><p>유형 알아보기</p>
<pre><code class="language-python">x = 15 
if type(x) is int:
  print(&quot;주어진 값과 정수이다.&quot;, type(x))
y = 'type(x) is int'
if y:
  print(&quot;주어진 값과 정수이다.&quot;, type(x))</code></pre>
<pre><code>주어진 값과 정수이다. &lt;class 'int'&gt;
주어진 값과 정수이다. &lt;class 'int'&gt;</code></pre></li>
</ul>
<hr />
<h3 id="523-단일-if문--else">5.2.3 단일 if문 (~ else)</h3>
<ul>
<li>문법<pre><code class="language-python">if 조건식:
  수행할 문장1
  수행할 문장2
  ...
else:
    수행할 문장 A
  수행할 문장 B
  ...</code></pre>
<h3 id="실습-1">실습</h3>
</li>
<li>예제 1. 논리연산자 <code>and</code>, <code>not(!)</code>, 비교연산자 <code>&gt;</code><pre><code class="language-python">x = 15 
if x &gt; 10 and x != 15: 
  print(&quot;Samadal&quot;)
else: print(&quot;Madal&quot;)</code></pre>
<pre><code>Madal</code></pre></li>
</ul>
<hr />
<ul>
<li>예제 2. 비교연산자 <code>=</code>, 비교연산자 <code>&gt;</code><pre><code class="language-python">x = 15 
if x &gt; 10 or x == 15: 
  print(&quot;True&quot;)
else: print(&quot;False&quot;)</code></pre>
<pre><code>True</code></pre></li>
</ul>
<hr />
<ul>
<li>예제 3. 논리연산자 <code>or</code>, <code>not(!)</code>, 비교연산자 <code>&gt;</code><pre><code class="language-python">x = 15 
if x &gt; 10 or x == 15: 
  print(&quot;True&quot;)
else: print(&quot;False&quot;)</code></pre>
<pre><code>True</code></pre></li>
</ul>
<hr />
<ul>
<li>예제 4. <code>Boolean</code>(부울대수)<pre><code class="language-python">money = 4000
card = False
</code></pre>
</li>
</ul>
<p>if money &gt;= 4000 or card: 
    print(&quot;집에 갈 수 있다.&quot;)
else: 
    print(&quot;신문 덮고 노숙&quot;)</p>
<pre><code></code></pre><p>집에 갈 수 있다.</p>
<pre><code>---
- 예제 5. 자료형과 매개변수의 사용 유무에 따른 출력
  - 리스트 자료형
  - 튜플 자료형
  - 딕셔너리 
```python
lotto_number = 23
if lotto_number in (1, 9, 23, 46): 
    print(&quot;세계여행&quot;)
else: print(&quot;다음 기회에&quot;)

print(&quot;-----------------&quot;)

lotto_number = 23
lucky_list = [1, 9, 23, 46]
if lotto_number in lucky_list: 
    print(&quot;세계여행&quot;)
else: 
    print(&quot;다음 기회에&quot;)

print(&quot;-----------------&quot;)

lotto_number = 23
lucky_list = {'n1':1, 'n2':9, 'n3':23, 'n4':46}
ln1 = lucky_list['n1']
ln2 = lucky_list['n2']
ln3 = lucky_list['n3']
ln4 = lucky_list['n4']
if lotto_number in [ln1, ln2, ln3, ln4]:
    print(&quot;세계여행&quot;)
else: 
    print(&quot;다음 기회에&quot;)</code></pre><pre><code>세계여행
-----------------
세계여행
-----------------
세계여행</code></pre><hr />
<ul>
<li>예제 6. <code>예제 5</code>에서 값을 입력받은 후 처리할 수 있도록 수정<pre><code class="language-python">lotto_number = int(input('값 입력 :'))
lucky_list = [1, 9, 23, 46]
if lotto_number in lucky_list: print(&quot;세계여행&quot;)
else: 
  print(&quot;다음 기회에&quot;)
</code></pre>
</li>
</ul>
<p>print(&quot;-----------------&quot;)</p>
<p>lotto_number = input('값 입력 :')
lucky_list = [1, 9, 23, 46]
if int(lotto_number) in lucky_list: print(&quot;세계여행&quot;)
else: 
    print(&quot;다음 기회에&quot;)</p>
<pre><code></code></pre><p>값 입력 :3
다음 기회에
값 입력 :1
세계여행</p>
<pre><code>---
- 예제 7. 한 개의 정수를 받아들인 후 짝수인지 홀수인지를 판별
```python
num = int(input(&quot;값 입력: &quot;))
if num % 2 == 0: 
    print('짝수')
else: 
    print('홀수')</code></pre><pre><code>값 입력: 4
짝수</code></pre><hr />
<ul>
<li>예제 8. 받아들인 3개의 값(기호 1개, 숫자 2개)을 이용한 사칙연산<pre><code class="language-python">num1 = int(input(&quot;숫자를 입력하세요 :&quot;))
num2 = (input(&quot;기호를 입력하세요 :&quot;))
num3 = int(input(&quot;숫자를 입력하세요 :&quot;))
</code></pre>
</li>
</ul>
<p>if num2 == '+':
    total = num1 + num3
elif num2 == '-':
    total = num1 - num3
elif num2 == '*':
    total = num1 * num3
elif num2 == '/':
    total = num1 / num3<br />print(f&quot;{num1} {num2} {num3} = {total:.2f}&quot;)</p>
<pre><code></code></pre><p>숫자를 입력하세요 :7
기호를 입력하세요 :/
숫자를 입력하세요 :2
7 / 2 = 3.50</p>
<pre><code>---
- 예제 9. 리스트를 사용해서 예제 8. 구성
```python
# 연산자 리스트
ops = ['+', '-', '*', '/']

# 입력
num1 = int(input(&quot;숫자를 입력하세요 :&quot;))
num2 = input(&quot;기호를 입력하세요 :&quot;)
num3 = int(input(&quot;숫자를 입력하세요 :&quot;))

# 연산
if num2 == ops[0]:      # '+'
    total = num1 + num3
elif num2 == ops[1]:    # '-'
    total = num1 - num3
elif num2 == ops[2]:    # '*'
    total = num1 * num3
elif num2 == ops[3]:    # '/'
    total = num1 / num3
else:
    total = &quot;잘못된 연산자입니다.&quot;

# 출력
print(f&quot;{num1} {num2} {num3} = {total if isinstance(total, str) else f'{total:.2f}'}&quot;)</code></pre><pre><code>숫자를 입력하세요 :52
기호를 입력하세요 :- 
숫자를 입력하세요 :42
52 - 42 = 10.00</code></pre><hr />
<ul>
<li>예제 10. 한 개의 문자열에 '2개의 값(나이:30, 키:180)'이 들어있다.이를 분리하고 분리된 각 값들에서 문자와 숫자를 또 한 번 분리한 후 하단의 조건문을 이용해서 코딩 조건문은 30보다 작거나 같고 180보다 크거나 같다고 할 때 임의의 내용을 출력</li>
</ul>
<pre><code class="language-python"># 슬라이싱 사용
hm = '나이:30, 키:180'
n1, n2 = hm[:5], hm[7:]
print(&quot;1차 분리 =&gt; %s, %s&quot; % (n1, n2))
print('---------------------------')
age, height = n1[3:], n2[2:]
print(&quot;2차 분리 =&gt; %s, %s&quot; % (age, height))
print('---------------------------')
print(type(age), type(height))
if int(age) &lt;= 30 and int(height) &gt;= 180: print(&quot;Yes&quot;)
else: print('No')</code></pre>
<pre><code>1차 분리 =&gt; 나이:30, 키:180
---------------------------
2차 분리 =&gt; 30, 180
---------------------------
&lt;class 'str'&gt; &lt;class 'str'&gt;
Yes</code></pre><pre><code class="language-python"># 인덱싱 사용
print('---------------------------')  # 주어진 값
hi = '나이:30, 키:180'
media = hi.split(&quot;,&quot;)
print(hi)
print(media)
print('---------------------------')  # 주어진 값을 ','를 이용해서 분리
print(media[0], media[1])
print('---------------------------')  # ':'을 이용해서 문자열과 숫자를 분리
age1 = media[0].split(':')
height1 = media[1].split(':')
print(age1, height1)
print('---------------------------')  # 연산에 사용될 값 도출
age2 = media[0].split(':')[0]
height2 = media[1].split(':')[0]
print(age2, height2)
age3 = media[0].split(':')[1]
height3 = media[1].split(':')[1]
print(age3, height3)
print('---------------------------')  # 조건문에 맞는 출력
if int(age3) &lt;= 30 and int(height3) &gt;= 180: print(&quot;Yes&quot;)
else: print(&quot;No&quot;)</code></pre>
<pre><code>---------------------------
나이:30, 키:180
['나이:30', ' 키:180']
---------------------------
나이:30  키:180
---------------------------
['나이', '30'] [' 키', '180']
---------------------------
나이  키
30 180
---------------------------
Yes</code></pre><hr />
<h3 id="524-다중-if문">5.2.4 다중 if문</h3>
<ul>
<li>문법 1. 일반적인 다중 if문<pre><code class="language-python">if 조건식1:
  수행할 문장1
  수행할 문장2
  ...
elif 조건식2:
    수행할 문장 A
  수행할 문장 B
  ... 
elif 조건식3:
    수행할 문장 A
  수행할 문장 B
  ...
else
  수행할 문장 A
  수행할 문장 B
  ...</code></pre>
<h3 id="525-실습">5.2.5 실습</h3>
</li>
<li>예제 1. 서로 다른 3개의 정수값을 입력 받은 후 비교하고 가장 큰 값과 가장 작은 값만을 출력<ul>
<li>출력문이 조건식 안에 있는 경우</li>
</ul>
</li>
<li>문법 2. 중첩 if문 (if문 안에 if문이 포함된 상태)<ul>
<li>임의의 정수 값(날짜)을 입력 받고 이에 해당하는 요일을 출력하는 코드 (중첩 if문)<pre><code class="language-python">day = int(input(&quot;날짜 입력 : &quot;))
</code></pre>
</li>
</ul>
</li>
</ul>
<p>if 1 &lt;= day &lt;= 31:
  if day % 7 == 1: 
      print(&quot;{}일은 {}요일&quot; .format(day, '월요일'))
  elif day % 7 == 2: 
      print(&quot;화요일&quot;)
  elif day % 7 == 3: 
      print(&quot;수요일&quot;)
  elif day % 7 == 4: 
      print(&quot;목요일&quot;)
  elif day % 7 == 5: 
      print(&quot;금요일&quot;)
  elif day % 7 == 6: 
      print(&quot;토요일&quot;)
  #elif day % 7 == 0: print(&quot;일요일&quot;)<br />  else: 
      print(&quot;일요일&quot;)
else: 
    print(&quot;다시 입력하세요&quot;)</p>
<pre><code>
### 전역변수
- 소스 코드 전반에 영향을 주는 변수를 말한다.
- 소스 코드 최상단에 선언해 준다.
### 지역변수
- 해당 변수가 선언된 영역에만 영향을 주는 변수를 말한다.
- 해당 영역에서 필요에 따라 선언해서 사용하면 된다.
- (매우 중요) 전역변수보다 지역변수가 우선권을 가진다.

- 예제 3. 사용자로 부터 임의의 정수 (1 ~ 24)를 입력 받아서 시간을 출력
```python
time = int(input(&quot;시간력 : &quot;))

if 1 &lt;= time &lt;= 24:
    if time == 12:
        print(&quot;정오 입니다.&quot;)
    elif 1 &lt;= time &lt;= 11:
        print(&quot;오전입니다.&quot;)
    elif 13 &lt;= time &lt;= 23: 
        print(&quot;오후입니다.&quot;)
else: print(&quot;제대로 입력해주세요.&quot;)</code></pre><ul>
<li>예제 4. 임의의 값(이름, 키, 체중)을 입력 받은 후 비만도(BMI, Body Mass Index, 신체질량지수) 출력<ul>
<li>100미만이면 저체중</li>
<li>100이상 110 미만 정상</li>
<li>110이상 120 미만 과체중</li>
<li>120 이상 130 미만 비만 </li>
<li>130이상 고도비만</li>
</ul>
</li>
<li>표준 체중 = (현재 키 - 100) * 0.9</li>
<li>비만도(%) = 현재 체중 / 표준 체중 * 100</li>
</ul>
<pre><code class="language-python">name = input(&quot;이름 : &quot;)
height = float(input(&quot;키 : &quot;))
weight = float(input(&quot;몸무게 : &quot;))

std_weigth = (height - 100) * 0.9
bmi = weight / std_weigth * 100
print(&quot;---------------------&quot;)
if bmi &lt; 100: 
    print(&quot;비만도(%.1f) : 상태(저체중)&quot; % bmi)
elif bmi &lt; 110: 
    print(&quot;비만도(%.1f) : 상태(정상)&quot; % bmi)
elif bmi &lt; 120: 
    print(&quot;비만도(%.1f) : 상태(과체중)&quot; % bmi)
elif bmi &lt; 130: 
    print(&quot;비만도(%.1f) : 상태(비만)&quot; % bmi)    
elif bmi &lt; 140: 
    print(&quot;비만도(%.1f) : 상태(고도비만)&quot; % bmi) </code></pre>
<ul>
<li>예제 5. 임의의 값을 입력 받은 후 윤년을 구하는 코드<pre><code class="language-python">year = int(input(&quot;알고 싶은 연도를 입력하세요 : &quot;))
if year % 4 == 0:
  if year % 100 == 0:
      if year % 400 == 0: yu = &quot;윤년&quot;
      else: yu = '평년'
  else: yu = '윤년'
else: yu ='평년'
print(f&quot;입력한 {year}년은 {yu}입니다.&quot;)</code></pre>
<pre><code>알고 싶은 연도를 입력하세요 : 2025
입력한 2025년은 평년입니다.</code></pre></li>
</ul>
<hr />
<h1 id="span-style--colorskyblue53-for문span"><span style="color: skyblue;">5.3 for문</span></h1>
<h2 id="531-개요">5.3.1 개요</h2>
<ul>
<li>데이터를 순차적으로 꺼내서 반복, 처리하는 작업을 한다.</li>
<li>일반적으로 <code>if</code>문과 함께 많이 사용된다.</li>
</ul>
<h2 id="532-문법">5.3.2 문법</h2>
<h3 id="▪-단일-for문">▪ 단일 for문</h3>
<pre><code class="language-python">for [매개]변수 in range(초기값, 끝값(출력시 '-1'), 증감값):
    종속문장 1 실행
    종속문장 2 실행
    ...
for [매개]변수 in 리시트(문자열 또는 튜플):
    종속문장 A 실행
    종속문장 B 실행
    ...</code></pre>
<hr />
<h3 id="▪-예제-1-range">▪ 예제 1. range</h3>
<pre><code class="language-python"># for문
i = 1101
for i in range(0, 10, 2):
  print(i)
print('-------------------')
for j in range(1, 11, 1):
  print(j)
print('-------------------') 
for k in range(1, 10):      # range(초기값, 끝값, x). 증감식은 없는 경우 '1'
  print(&quot;k = %d&quot; % k)
print('-------------------') 
for l in range(10):         # range(x, 끝값, x). 초기값이 없는 경우 '0'
  print(&quot;l = %d&quot; % l)
print('-------------------')
for m in range(10, 2):      # range(x초기값, 끝값, x). 출력은 안된다.
  print(&quot;m = %d&quot; % m)       # 조건에 맞지 않기 때문에 오류가 발생</code></pre>
<h3 id="▪-예제-2-매우중요-누적-합계등을-구할-때는-반드시-초기값을-지정해야-한다">▪ 예제 2. (매우중요) 누적, 합계등을 구할 때는 반드시 초기값을 지정해야 한다</h3>
<ul>
<li>실습 1<pre><code class="language-python">sum = 0
for i in range(1, 11, 1):
  sum += i
  print(&quot;진행 : i(%d) | sum(%d)&quot; % (i, sum))
print(&quot;1부터 10까지의 합은 %d&quot; % sum)</code></pre>
</li>
<li>실습 2. 1부터 10까지 1씩 증가하면서 <pre><code class="language-python">for i in range(1, 11, 1):
  if 1 % 2 == 0: print(&quot;짝수 =&gt; %d&quot; %i)
else: print(&quot;홀수 =&gt; %d&quot; % i)</code></pre>
</li>
</ul>
<h3 id="▪-예제-3-list">▪ 예제 3. List</h3>
<h3 id="▪-예제-4-1--50까지의-숫자-중에서-7의-배수인-경우는-출력하지-않는-소스">▪ 예제 4. '1 ~ 50'까지의 숫자 중에서 7의 배수인 경우는 출력하지 않는 소스</h3>
<h3 id="▪-예제-5-3개의-요소에-받아들인-값까지-합을-구하는-소스누적에-따른-값의-합산-with-합산이-되는-과정도-출력">▪ 예제 5. 3개의 요소에 받아들인 값까지 합을 구하는 소스(누적에 따른 값의 합산) with 합산이 되는 과정도 출력</h3>
<pre><code class="language-python">a, b, c = int(input(&quot;시작 : &quot; )), int(input(&quot;끝 : &quot;)), int(input(&quot;증감 : &quot;))
sum = 0

for i in range(a, b+1, c):
    sum += i
    print(&quot;I(%d) : sum(%d)&quot; % (i, sum))
print(&quot;시작(%d) | 끝(%d) | 증감(%d) |합(%d)&quot; % (a, b, c, sum))</code></pre>
<pre><code>시작 : 5
끝 : 10
증감 : 2
I(5) : sum(5)
I(7) : sum(12)
I(9) : sum(21)
시작(5) | 끝(10) | 증감(2) |합(21)</code></pre><hr />
<h3 id="예제-6-학생별-국어-과목의-취득점수를-이용한-합력-불합격-여부-출력-60점-미만인-학생은-불합격입니다를-그-이외는-합격입니다를-출력">예제 6. 학생별 국어 과목의 취득점수를 이용한 합력, 불합격 여부 출력 60점 미만인 학생은 '불합격입니다.'를 그 이외는 '합격입니다.'를 출력</h3>
<pre><code class="language-python">a = [95, 25, 67, 45, 80]

count = 0
for i in range(5):
    count += 1
    b = a[i]
    if b &gt;= 60: print(&quot;%d번째 학생은 %d점이므로 합격&quot; % (count, b))
    else:
        print(&quot;%d번째 학생은 %d점이므로 불합격&quot; % (count, b))</code></pre>
<pre><code>1번째 학생은 95점이므로 합격
2번째 학생은 25점이므로 불합격
3번째 학생은 67점이므로 합격
4번째 학생은 45점이므로 불합격
5번째 학생은 80점이므로 합격</code></pre><hr />
<h3 id="▪-다중-for문-for문안에-for문이-있는-경우">▪ 다중 for문 (for문안에 for문이 있는 경우)</h3>
<pre><code class="language-python">for 변수1 in range(초기값1, 끝값1, 증감값1):
    종속문장 1실행
    for 변수2 in range(초기값2, 끝값2, 증감값2):
    ...</code></pre>
<hr />
<h3 id="예제-1-3행-4열짜리-배열-출력">예제 1. 3행 4열짜리 배열 출력</h3>
<pre><code class="language-python">for i in range(0, 3, 1):
    for j in range(0, 5, 1):
        print(&quot;다중for문 : i({}), j({})&quot; .format(i, j))
    print(&quot;\n&quot;)</code></pre>
<pre><code>다중for문 : i(0), j(0)
다중for문 : i(0), j(1)
다중for문 : i(0), j(2)
다중for문 : i(0), j(3)
다중for문 : i(0), j(4)


다중for문 : i(1), j(0)
다중for문 : i(1), j(1)
다중for문 : i(1), j(2)
다중for문 : i(1), j(3)
다중for문 : i(1), j(4)


다중for문 : i(2), j(0)
다중for문 : i(2), j(1)
다중for문 : i(2), j(2)
다중for문 : i(2), j(3)
다중for문 : i(2), j(4)</code></pre><hr />
<h3 id="예제-2-구구단">예제 2. 구구단</h3>
<ul>
<li>단 구분 없이 세로로 모두 출력<pre><code class="language-python">for i in range(2, 10, 1):
  for j in range(1, 10, 1):
      print(&quot;%d x %d = %d&quot; % (i, i, i*j))
  print(&quot;\n&quot;)</code></pre>
</li>
<li>단 별로 구분해서 가로로 모두 출력<pre><code class="language-python">for i in range(1, 10, 1):
  for j in range(2, 10, 1):
      print(j, 'x', i, '=' , i*j, end='\t')
  print(&quot;\n&quot;)</code></pre>
</li>
<li>입력된 단수에 해당하는 값만 출력<pre><code class="language-python">a = int(input(&quot;단 수를 입력해주세요 : &quot;))
</code></pre>
</li>
</ul>
<p>for i in range(a, a+1):
    for j in range(1, 10):
        print(&quot;%d x %d = %d&quot; % (i, i, i*j))
    print(&quot;\n&quot;)</p>
<pre><code>
---</code></pre>