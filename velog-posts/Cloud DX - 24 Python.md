# Cloud DX - 24 Python

- 📅 Published: Fri, 31 Oct 2025 06:53:58 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-24-Python)

<hr />
<h1 id="span-style--coloryellowpythonspan"><span style="color: yellow;">Python</span></h1>
<h2 id="설치">설치</h2>
<h3 id="python">Python</h3>
<ul>
<li>프로그램 다운로드 <code>(python-3.13.9-amd64.exe)</code></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/dc73b59e-4354-45e7-9195-fa4f1a693a37/image.png" /></p>
<hr />
<h3 id="editor-microsoft-visual-studio-code">Editor (Microsoft Visual Studio Code)</h3>
<ul>
<li><p>프로그램 다운로드</p>
</li>
<li><p>설치</p>
</li>
<li><p>설치 후 테스트</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1d673271-66b1-4a17-9eee-b50578dd8e25/image.png" /></li>
</ul>
</li>
<li><p>(매우 중요)설치 후 필수 패키지 설치 </p>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/835c7e21-3448-4661-a5c1-a4e840db6562/image.png" /></p>
</li>
<li><p><code>Python</code></p>
</li>
<li><p><code>Code runner</code></p>
</li>
<li><p><code>Korean Language Pack</code></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/dceddc0f-a2de-4271-91ed-2b575d48b6bd/image.png" /></p>
</li>
<li><p>파일이 저장될 폴더 지정</p>
</li>
<li><p>소스 파일 자동 저장 및 색 테마 지정(ctrl + k + t</p>
</li>
<li><p>에디팅할 때의 기본 폼 설정</p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9aa3521a-2734-4ee3-87d3-3e8ddf06630a/image.png" /></p>
</li>
<li><p>파일 생성 및 실행 테스트 </p>
</li>
</ul>
</li>
</ul>
<hr />
<h1 id="🐍-python-둘러보기">🐍 Python 둘러보기</h1>
<hr />
<h2 id="1-주석">1. 주석</h2>
<pre><code class="language-python"># 한 줄 주석

&quot;&quot;&quot;
여러 줄 주석
&quot;&quot;&quot;</code></pre>
<hr />
<h2 id="2-사칙연산">2. 사칙연산</h2>
<pre><code class="language-python">print(1 + 2)       # 덧셈
print(4 - 2)       # 뺄셈
print(&quot;4 - 2&quot;)     # 문자열 출력
print(3 / 2.4)     # 나눗셈 (실수)
print(3 * 9)       # 곱셈</code></pre>
<hr />
<h2 id="3-변수에-숫자를-대입하고-연산하기">3. 변수에 숫자를 대입하고 연산하기</h2>
<pre><code class="language-python">a = 1
b = 2
print(a + b)</code></pre>
<hr />
<h2 id="4-변수에-문자를-대입하고-출력하기">4. 변수에 문자를 대입하고 출력하기</h2>
<pre><code class="language-python">print(&quot;samadal&quot;)
print(&quot;Python&quot;) 

a = &quot;Python&quot;
print(a)

print(&quot;=&quot; * 40)   # 구분선 출력</code></pre>
<hr />
<h1 id="📘-2-자료형">📘 2. 자료형</h1>
<h2 id="21-숫자형">2.1 숫자형</h2>
<h3 id="211-정수형">2.1.1 정수형</h3>
<pre><code class="language-python">a = 123
b = -178

print(a, b)
print(123 - 178)
print(a + b)

c, d = 123, -178
print(c - d)
print(c * d)
print(c / d)
print(a, b, c, d)
print(a + b, a - b, c * d, c / d)</code></pre>
<hr />
<h3 id="212-실수형">2.1.2 실수형</h3>
<pre><code class="language-python">a, b, c, d = 123, -178, 123, -178
a, b, c, d = 1.2, -3.45, 4.24E10, 4.24e10

print(a, b, c, d)
print(a + b + c + d)</code></pre>
<hr />
<h3 id="213-진법-변환">2.1.3 진법 변환</h3>
<ul>
<li><strong>2진수</strong>: <code>0b</code>, <strong>8진수</strong>: <code>0o</code>, <strong>10진수</strong>: 기본, <strong>16진수</strong>: <code>0x</code></li>
</ul>
<pre><code class="language-python">e, f, g, h, i = 0b1011, 0o177, 256, 0x8ff, 0xABC
print(e, f, g, h, i)
print(e + f + g)</code></pre>
<hr />
<h3 id="214-연산-기호">2.1.4 연산 기호</h3>
<h4 id="사칙연산-실습">사칙연산 실습</h4>
<pre><code class="language-python">a, b, c, d = 3, 4, 7, 3
print(a + b, c + d)
print(a - b, c - d)
print(a * b, c * d)
print(a / b, c / d)
print(a ** b)</code></pre>
<h4 id="몫과-나머지">몫과 나머지</h4>
<pre><code class="language-python">print(a % b)
print(b % a)
print(a // b)
print(b // a)

print(c % d)
print(d % c)
print(c // d)
print(d // c)</code></pre>
<h4 id="문자열과-함께-출력">문자열과 함께 출력</h4>
<pre><code class="language-python">e, f = 14, 15
g = e % 2

print('주어진 값의 나머지는', g, '가(이) 되므로 짝수이다')
print(&quot;주어진 값의 나머지는&quot;, g, &quot;가(이) 되므로 짝수이다&quot;)</code></pre>
<hr />
<h2 id="22-문자형과-문자열형">2.2 문자형과 문자열형</h2>
<h3 id="221-문자열-표현">2.2.1 문자열 표현</h3>
<ul>
<li>Python은 문자/문자열 구분 없음</li>
<li>큰따옴표 <code>&quot;</code>, 작은따옴표 <code>'</code>, 삼중 따옴표 <code>&quot;&quot;&quot;</code>, <code>'''</code> 모두 사용 가능</li>
</ul>
<pre><code class="language-python">a = &quot;Himedia's samadal&quot;
b = 'Himedia&quot;s samadal'</code></pre>
<hr />
<h3 id="222-문자열-실습">2.2.2 문자열 실습</h3>
<h4 id="따옴표-포함">따옴표 포함</h4>
<pre><code class="language-python">a = &quot;Himedia's, samadal&quot;
# b = 'Himedia's, samadal'  # 에러 발생
print(a)

a = 'Himedia&quot;s, samadal'
b = &quot;Himedia's, samadal&quot;
print(a)
print(b)</code></pre>
<h4 id="문자열-연산">문자열 연산</h4>
<pre><code class="language-python">hi = &quot;Python&quot;
media = &quot;Cloud&quot;
print(hi + media)
print(hi * 2)
print('=' * 50)

var1, var2 = '=', 50
print(var1 * var2)</code></pre>
<hr />
<h3 id="이스케이프-코드">이스케이프 코드</h3>
<pre><code class="language-python">print('1다음 라인으로\\이동')  # 그냥 문자열
print('2다음 라인으로\n이동')  # 줄바꿈
print('3다음 라인으로\r이동')  # 커서 맨 앞으로
print('4다음 라인으로\t이동')  # 탭
print('5다음 라인으로\'이동')  # 작은따옴표
print('6다음 라인으로\&quot;이동')  # 큰따옴표
print('7다음 라인으로\\이동')  # 역슬래시

a = 20
print('나의 나이는', a, '살입니다.')
print('나의 나이는', a, '\b살입니다.')

info = &quot;나의 이름은 사마달 입니다\n나이는 20살입니다.\n주소는 바닷가입니다.&quot;
print(info)</code></pre>
<hr />
<h2 id="23-문자열-인덱싱과-슬라이싱">2.3 문자열 인덱싱과 슬라이싱</h2>
<h3 id="231-문자열-인덱싱">2.3.1 문자열 인덱싱</h3>
<pre><code class="language-python">a = &quot;Himedia, Samadal, Python&quot;

print(a[0])
print(a[8])
print(a[-1])
print(a[-6])

b = a[3]
print('b =', b)

# 출력 구분
print(&quot;SAM&quot;, &quot;samadal&quot;, sep=' = ')

c, d = a[10], a[-1]
print(c, d, sep=', ')</code></pre>
<h4 id="경로-출력-실습">경로 출력 실습</h4>
<pre><code class="language-python">print(&quot;C:\\program Files\\Python313\\&quot;)
print(&quot;C:&quot;, &quot;program Files&quot;, &quot;Python313&quot;, sep=&quot;\\&quot;, end=&quot;\\&quot;)</code></pre>
<hr />
<h3 id="232-문자열-슬라이싱">2.3.2 문자열 슬라이싱</h3>
<pre><code class="language-python">a = &quot;Hi_Me_dia&quot;

print(a[2:5])    # _Me
print(a[3:])     # Me_dia
print(a[:3])     # Hi_
print(a[3:-1])   # Me_di

a = &quot;HiMedia20251031&quot;
company = a[:7]
day = a[7:]
print(company + '\n' + day)</code></pre>
<h4 id="실습-pithon-→-python">실습: 'Pithon' → 'Python'</h4>
<pre><code class="language-python">a = 'Pithon'
b, c, d = a[0], 'y', a[2:]
print(b + c + d)</code></pre>
<hr />
<h1 id="24-출력-formatting-3가지">2.4 출력 Formatting 3가지</h1>
<h2 id="241--문자열-포맷">2.4.1 <code>%</code> 문자열 포맷</h2>
<pre><code class="language-python">print(&quot;%유형1, %유형2, ...&quot; % (값1, 값2, ...))

name = &quot;사마달&quot;
age = 20
print(&quot;이름: %s, 나이: %d살&quot; % (name, age))</code></pre>
<ul>
<li><code>%d</code>: 정수 (Decimal)</li>
<li><code>%s</code>: 문자열 (String)</li>
<li><code>%c</code>: 문자 (Character)</li>
<li><code>%f</code>: 실수 (Float)</li>
<li><code>%o</code>: 8진수 (Octal)</li>
<li><code>%x</code>: 16진수 (Hexadecimal)</li>
</ul>
<h2 id="예제-1-2진수를-10진수로-표현">예제 1. 2진수를 10진수로 표현</h2>
<h3 id="실습">실습</h3>
<pre><code class="language-python">print(11010100001110001) #그냥숫자
print(0b11010100001110001) #그냥숫자

bin1 = 0b11010100001110001
bin2 = 11010100001110001

print(&quot;%d&quot; % bin1)
print(&quot;%d&quot; % bin2)
print(&quot;%d, %d&quot; % (bin1, bin2))</code></pre>
<hr />
<h3 id="예제-2-16진수3d5f를-10진수로-표현">예제 2. 16진수(3D5F)를 10진수로 표현</h3>
<pre><code class="language-python">print(0x3d5f)

hexa = 0x3d5f

print(&quot;%d&quot; % hexa)

print(&quot;16진수 값(%x)을 10진수(%d)로 표현&quot; % (hexa, hexa))
</code></pre>
<hr />
<h3 id="예제-3-10진수1024를-16진수로-표현">예제 3. 10진수(1024)를 16진수로 표현</h3>
<pre><code class="language-python">print(1024)

decimal = 1024

print(&quot;%x&quot; % 1024)

print(&quot;10진수 값(%d)을 16진수(%x)로 표현&quot; % (decimal, decimal))
</code></pre>
<hr />
<h3 id="예제-4-10진수1024-5786의-합을-16진수로-표현">예제 4. 10진수(1024, 5786)의 합을 16진수로 표현</h3>
<pre><code class="language-python">dec1 = 1024 
dec2 = 5786

sum = dec1 + dec2
print(&quot;%x&quot; %sum)
# 1a9a</code></pre>
<hr />
<h3 id="예제-5-16진수5c90와-8진수652의-합을-10진수로-표현">예제 5. 16진수(5c90)와 8진수(652)의 합을 10진수로 표현</h3>
<pre><code class="language-python">hexa, oct = 0x5c90, 0o652
ho = hexa + oct
print(&quot;%d&quot; % (0x5c90 + 0o652))
print(&quot;%d&quot; % (hexa + oct))
print(&quot;%d&quot; % ho)
# 24122</code></pre>
<h2 id="자료형-확인-함수-type">자료형 확인 함수 type()</h2>
<pre><code class="language-python">dh = (&quot;%d % 0x5C90&quot;)
do = (&quot;%d % 0x652&quot;)

print(dh + do)
print(type(dh) , type(do))
</code></pre>
<h3 id="실습-2-예제-6-의-내용을-각-요소들변수치환-인덱싱-슬라이싱-문자열을-모두-포함해서-출력">실습 2. 예제 6. 의 내용을 각 요소들(변수치환, 인덱싱, 슬라이싱, %문자열)을 모두 포함해서 출력</h3>
<pre><code class="language-python">a, b, c, d = &quot;Himedia&quot;, 2025, &quot;10&quot;, 31
print(type(a), type(b), type(c), type(d))
print(&quot;%s %d년 %s월 %d일 &quot; % (a, b, c, d))
print(&quot;%s %d년 %s월 %d일 &quot; % (a[:], b, c[:2], d))
c1, c2 = c[0], c[1]
print(&quot;%s | %s&quot; % (c1,c2))
print(&quot;%s %d년 %s월 %d일 &quot; % (a[:], b, c[:2], d))</code></pre>
<h3 id="예제-6-문자열을-직접-받아서-출력">예제 6. 문자열을 직접 받아서 출력</h3>
<pre><code class="language-python">a = &quot;Himedia 2025년 10월 31일&quot;
print(&quot;Himedia %d년 10월 31일&quot; % 2025)
print(&quot;Himedia %s년 10월 31일&quot; % 20f25)
print(&quot;Himedia %s년 10월 31일&quot; % &quot;2025&quot;)</code></pre>
<hr />
<h2 id="기타">기타</h2>
<h3 id="특수-기호가붙은-문자열">특수 기호가붙은 문자열</h3>
<pre><code class="language-python">print(&quot;%d%%&quot; % 54)</code></pre>
<h3 id="정렬">정렬</h3>
<pre><code class="language-python">print(&quot;1234567890123456789&quot;)
print(&quot;%+15s&quot; % &quot;samadal&quot;)    # 자리 확보하고 우측 정렬
print(&quot;%15s&quot; % &quot;samadal&quot;)    # '+' 기호는 생략 가능
print(&quot;%-15s&quot; % &quot;samadal&quot;)    # 자리 확보하고 좌측 정렬</code></pre>
<pre><code class="language-python">print(&quot;%f&quot; % 3.14) # 3.140000
print(&quot;%0.2f&quot; % 3.14) # 3.14
print(&quot;%.2f&quot; % 3.14) # 3.14

print(&quot;1234567890123456789&quot;)
print(&quot;%9.2f&quot; % 3.14) # .좌측(자리확보) / .우측(소수이하자릿수)

print(&quot;%.2f&quot; % 3.146) # 3.15  (5 이상은 반올림)
print(&quot;%.2f&quot; % 3.144) # 3.14  (5 미만은 반올림 불가)</code></pre>
<hr />
<h2 id="242-formatting-2-format-함수">2.4.2 Formatting 2. .format() 함수</h2>
<ul>
<li>특징
<code>%문자열은</code> <code>서식 지정자</code>를 이용해서 출력하지만
<code>.format()함수</code>는 <code>인덱스 넘버</code>를 이용해서 출력한다.</li>
<li>문법<pre><code class="language-python">print(&quot;{0}, {1}, ...&quot; .format(값1, 값2, ...))</code></pre>
</li>
</ul>
<h3 id="실습-1">실습</h3>
<ul>
<li>예제 1.<code>%문자열</code>과 <code>.format() 함수</code>의 비교<pre><code class="language-python">print(&quot;Himedia %d년 10월 31일&quot; % 2025)
print(&quot;Himedia {0}년 10월 31일&quot; .format(2025))
print(&quot;Himedia {}년 10월 31일&quot; .format(2025))
</code></pre>
</li>
</ul>
<p>a = &quot;Himedia {}년 10월 31일&quot;
print(a .format(2025))</p>
<p>b, c, d = 2025, 10, 31
print(&quot;Himedia %d년 %d월 %d일&quot; % (b, c, d))
print(&quot;Himedia {0}년 {1}월 {2}일&quot; .format(b, c, d))
print(&quot;Himedia {}년 {}월 {}일&quot; .format(b, c, d))</p>
<pre><code>- 예제 2.`&quot;%사마달님의 나이는 200살입니다.&quot;`를 `%문자열`과 `.format()함수로` 표현


```python
b, c = &quot;사마달&quot;, 200
print(&quot;%s님의 나이는 %d살 입니다.&quot; % (b, c))
print(&quot;{0}님의 나이는 {1}살 입니다.&quot; .format(b, c))

name, age = &quot;사마달&quot;, 200
str1 = &quot;%s님의 나이는 %d살입니다.&quot;
str2 = &quot;{0}님의 나이는 {1}살 입니다.&quot;
print(str1 % (name, age))
print(str2 .format(name, age))</code></pre><ul>
<li><p>인덱싱에서는 <code>한글 1자</code>를 그냥 <code>문자 1개</code>로 인식한다</p>
<pre><code class="language-python">na = &quot;사마달, 200&quot;
a, b = na[:3], na[5:]
print(&quot;%s님의 나이는 %s살입니다.&quot; % (a, b)) # 사마달님의 나이는 200살입니다.
print(&quot;{0}님의 나이는 {1}살입니다.&quot; .format(a, b)) # 사마달님의 나이는 200살입니다.</code></pre>
</li>
<li><p>예제 3. 앞에서 했던 <code>%문자열</code> 예제를 <code>.format()함수</code>로 표현</p>
</li>
</ul>
<h2 id="기타-1">기타</h2>
<h3 id="특수-기호가-붙은-문자열">특수 기호가 붙은 문자열</h3>
<pre><code class="language-python">print(&quot;{}%&quot; .format(54))</code></pre>
<h3 id="출력문에-이름-넣기-값-대신-변수명으로-치환한-후-대입">출력문에 이름 넣기 (값 대신 변수명으로 치환한 후 대입)</h3>
<h3 id="문자열-정렬">문자열 정렬</h3>
<h3 id="소수점-표현">소수점 표현</h3>
<ul>
<li>실수는 기본적으로 <code>6자리</code> 표현<pre><code class="language-python">print(&quot;{}&quot; .format(3.14124234)) # 3.14124234
print(&quot;{0:f}&quot; .format(3.14124234)) # 3.14124234
print(&quot;{0:.2f}&quot; .format(3.14124234)) # 3.14
print(&quot;{:.2f}&quot; .format(3.14124234)) # 인덱스넘버 생략 가능 # 3.14</code></pre>
<h3 id="통화-단위-구분">통화 단위 구분</h3>
<pre><code class="language-python">print(&quot;{}원&quot; .format(20000000)) # 20000000원
print(&quot;{:,}원&quot; .format(20000000)) # 20,000,000원</code></pre>
</li>
</ul>
<hr />
<h2 id="243-formatting-3-f-string">2.4.3 Formatting 3. <code>f-String</code></h2>
<h3 id="문법">문법</h3>
<pre><code class="language-python">print(f&quot;{값1}, {값2}, ...&quot;)</code></pre>
<h3 id="실습-2">실습</h3>
<h3 id="예제-1-문자열과-format-함수-f-string의-비교">예제 1. <code>%문자열</code>과 <code>.format() 함수</code>, <code>f-String</code>의 비교</h3>
<pre><code class="language-python">name, age = &quot;사마달&quot;, 30
print(&quot;%s, %d&quot; %(name, age))
print(&quot;{}, {}&quot; .format(name, age))
print(f&quot;{name}, {age}&quot;)</code></pre>
<h3 id="예제-2">예제 2.</h3>
<blockquote>
<p> 홍길동씨의 과목별 점수는 다음과 같다고 할 때 합계와 평균 점수를 구하는 소스 코드를 작성하시오.<br />국어(85.56), 영어(79.34), 수학(95.47)
 '%문자열', '.format()함수', 'f-String'으로 모두 표현한다.
 소수이하 1자리까지 표현한다.
 출력 결과는 몇 줄이 되어도 무관하고 출력문은 반드시 한 줄로 표현해야 한다.</p>
</blockquote>
<pre><code class="language-python">a, b, c = 85.56, 79.34, 95.47
sum = a + b + c
avg = sum / 3

print(&quot;합계(%.1f) | 평균(%.1f)&quot; % (sum, avg))
print(&quot;합계({0:.1f}) | 평균({1:.1f})&quot;  .format(sum, avg))
print(f&quot;합계({sum:.1f}) | 평균({avg:.1f})&quot; )</code></pre>
<h3 id="예제-3">예제 3.</h3>
<blockquote>
<p>놀이공원을 가기 위해 11개의 지하철 역을 지나왔다. 출발역에서 도착역까지 37분이 걸렸다면 한 역을 지나는데 걸리는 시간은 얼마인가 
단, 소수 이하 2자리까지만 출력한다.</p>
</blockquote>
<pre><code class="language-python">sta = 11 
time = 37
print(&quot;한 역을 지나는데 걸리는 시간 %.2f분&quot; %(time/sta))
print(&quot;한 역을 지나는데 걸리는 시간({-:.2f})&quot; .format(time/sta))
print(f&quot;한 역을 지나는데 걸리는 시간 {time/sta:.2f}분&quot;)</code></pre>
<h3 id="예제-4">예제 4.</h3>
<blockquote>
<p>호텔 한 층의 높이는 260cm이다.
총 14개의 층을 사용하고 있으며 1층의 높이만
500.23cm라고 할 때 이 건물의 높이는 총 몇 m인가? 
단, 소수 이하 2자리까지만 출력한다. </p>
</blockquote>
<pre><code class="language-python">floor = 13
oneheight = 500.23
height = 260

total = (floor * height +  oneheight) / 100

print(&quot;이 건물의 높이는 %.2fm&quot; % (total)) # 이 건물의 높이는 38.80m
print(&quot;이 건물의 높이는 {0:.2f}m&quot; .format(total)) # 이 건물의 높이는 38.80m
print(f&quot;이 건물의 높이는 {(total):.2f}m&quot;) # 이 건물의 높이는 38.80m</code></pre>
<h3 id="예제-5">예제 5.</h3>
<blockquote>
<p> 홍길동씨의 주민등록번호는 881120-1068234이다.'-'을 기준으로 좌측과 우측으로 분리하고 작업한 후 원래 형태로 출력  </p>
</blockquote>
<pre><code class="language-python">num = &quot;881120&quot;
num2 = &quot;068234&quot;

print(num[:6],&quot;-&quot;,num2[:6])

id = &quot;881120-1068234&quot;
id1, id2 = id[:6], id[-7:] # 881120 - 1068234
print(id1 + '-' + id2) # 881120-1068234
print(&quot;%s-%s&quot; % (id1, id2)) # 881120-1068234
print(&quot;{0}-{1}&quot; .format(id1, id2)) # 881120-1068234
print(f&quot;{id1}-{id2}&quot;) # 881120-1068234</code></pre>
<hr />
<h1 id="25-기타">2.5 기타</h1>
<h2 id="251-문자열-관련-함수-내장-함수">2.5.1 문자열 관련 함수 (내장 함수)</h2>
<h3 id="count">count</h3>
<ul>
<li>문자의 갯수를 센다.<pre><code class="language-python">변수.count('문자')
</code></pre>
</li>
</ul>
<p>a = &quot;samadal&quot;
print(a.count('a')) # 3</p>
<pre><code>### find, index
- 문자의 위치를 알려준다.
```python
변수.find('문자') / 변수.(index('문자')

b = &quot;Himedia Samadal&quot;
print(b.find('S')) # 8
print(b.index('S'))  # 8</code></pre><h3 id="join">join</h3>
<ul>
<li>문자열을 삽입한다.<pre><code class="language-python">변수.jotin('문자(열)')
</code></pre>
</li>
</ul>
<p>print(&quot;,,&quot;.join('samadal')) # s,,a,,m,,a,,d,,a,,l
print(&quot;, &quot;.join('samadal')) # s, a, m, a, d, a, l</p>
<pre><code>
### upper, lower
- 대문자(또는 소문자)를 소문자(또는 대문자)로 치환한다.

```python
변수.upper() / 변수.lower()

c, d = 'SAMADAL', 'samadal'
print(c.lower()) #samadal
print(d.upper()) #SAMADAL</code></pre><h3 id="replace">replace</h3>
<ul>
<li>문자열을 교체한다.<pre><code class="language-python">변슈.replace(&quot;교체 전&quot;, &quot;교체 후&quot;)
</code></pre>
</li>
</ul>
<p>e = &quot;Samadal Himedia&quot;
print(e.replace(&quot;Samadal&quot;, 'Sam')) # Sam Himedia
print(e.replace(&quot;Himedia&quot;, 'Hm')) # Samadal Hm</p>
<pre><code>
### split
- 문자열을 나눈다.
- 공백을 기준으로 분리되는데 '리스트(List)' 형태로 분리

```python
변수,split()

f ,g = &quot;Himedia Saamadal&quot;, &quot;a : b:c:d&quot;
print(f.split)
#&lt;built-in method split of str object at 0x000002E4C54C55F0&gt;
print(g.split)
#&lt;built-in method split of str object at 0x000002E4C54C57F0&gt;</code></pre><hr />
<h2 id="252-cast-연산-강제-형-변환">2.5.2 Cast 연산( 강제 형 변환)</h2>
<h3 id="개요">개요</h3>
<ul>
<li>변수에 정의된 유형(또는 자료형)</li>
</ul>