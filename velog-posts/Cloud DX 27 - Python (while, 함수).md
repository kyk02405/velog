# Cloud DX 27 - Python (while, 함수)

- 📅 Published: Wed, 05 Nov 2025 09:21:35 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-27-Python-while)

<hr />
<h1 id="span-style--colorskyblue54-while문span"><span style="color: skyblue;">5.4 while문</span></h1>
<h2 id="541-개요">5.4.1 개요</h2>
<ul>
<li>프로그램 실행 후 종속 문장 등의 실행을 계속 진행할 수 있도록 한다.</li>
<li><span style="color: red;">(매우 중요)</span> 조건문이 부정확할 경우 <code>무한루프</code>에 빠질 수가 있다.</li>
<li>계속되는 무한 반복일 경우에는 <code>^ + C</code>를 누르면 빠져 나올 수가 있다.</li>
<li>일반적으로 break문과 함께 사용한다.</li>
<li><code>break</code>는 조건문 안에서만 동작한다.</li>
</ul>
<hr />
<h2 id="542-주의할-점">5.4.2 주의할 점</h2>
<ul>
<li><code>for i in range(1, 11, 1):</code>을 while문으로 변경할 때는 다음과 같이 한다.<ul>
<li>초기값은 while문 <code>밖에</code> 위치시키고</li>
<li>조건식은 while문 <code>옆에</code> 위치시키고</li>
<li>증감식은 while문 <code>안에</code> 위치시키면 된다</li>
</ul>
</li>
</ul>
<hr />
<h2 id="543-문법">5.4.3 문법</h2>
<pre><code class="language-python">while 조건문:
    수행할 문장 1
    수행할 문장 2
    ...</code></pre>
<h2 id="544-실습">5.4.4 실습</h2>
<h3 id="▪-예제-1-무한-루프">▪ 예제 1. 무한 루프</h3>
<pre><code class="language-python">while True:
    print(&quot;조건문이 참이라면... 이란 말이다.&quot;)
    print(&quot;뭐가 참인지 알 수가 없기 때문에 즉, 조건이 없어서 무한루프에 빠진다.&quot;)
    print(&quot;무한루프를 빠져나오려면 '^ + c'를 누른다.&quot;)</code></pre>
<pre><code>뭐가 참인지 알 수가 없기 때문에 즉, 조건이 없어서 무한루프에 빠진다.
무한루프를 빠져나오려면 '^ + c'를 누른다.
조건문이 참이라면... 이란 말이다.
뭐가 참인지 알 수가 없기 때문에 즉, 조건이 없어서 무한루프에 빠진다.
무한루프를 빠져나오려면 '^ + c'를 누른다.
조건문이 참이라면... 이란 말이다.
...
---</code></pre><h3 id="▪-예제-2-1부터-10까지의-숫자-출력">▪ 예제 2. 1부터 10까지의 숫자 출력</h3>
<pre><code class="language-python">a = 0
while a &lt; 10:
    a += 1
    print(&quot;%d&quot; % a)
    if a == 10: break
print(&quot;프로그램이 종료되었습니다.&quot;)</code></pre>
<pre><code>1
2
3
4
5
6
7
8
9
10
프로그램이 종료되었습니다.</code></pre><ul>
<li>for문과 while문을 이용한 출력<pre><code class="language-python">for i in range(1, 11, 1):
  print(&quot;i = %d&quot; % i)
print(&quot;-------------------&quot;)
j = 1
while j &lt; 11:
  print(&quot;j = %d&quot; % j)
  j += 1
  if j == 11: break</code></pre>
</li>
</ul>
<hr />
<h3 id="▪-예제-3-1부터-10까지의-합을-구하면서-출력-1">▪ 예제 3. 1부터 10까지의 합을 구하면서 출력 1.</h3>
<ul>
<li>while문을 이용한 출력(합)<pre><code class="language-python">a = 0
sum = 0
</code></pre>
</li>
</ul>
<p>while a &lt; 10:
    a += 1
    sum += a
    print(&quot;%d | %d &quot; % (a, sum))
    if a == 10: break</p>
<pre><code>---
### ▪ 예제 4. 임의의 값을 입력 받을 때 까지 출력
```python
number = 0
while number != 4:
    number = int(input(&quot;1. Add | 2. Del | 3. List | 4. Quit | 5. Name : &quot; ))
    print(&quot;선택한 번호 : %d&quot; % number)</code></pre><hr />
<h3 id="▪-예제-5-준비된-커피는-5잔이고-한-잔의-가격은-300원이라고-할-때-한-잔씩-뽑았을-때-준비된-커피의-수량이-남지-않도록-하려면">▪ 예제 5. 준비된 커피는 5잔이고 한 잔의 가격은 300원이라고 할 때 한 잔씩 뽑았을 때 준비된 커피의 수량이 남지 않도록 하려면?</h3>
<pre><code class="language-python">coffee, money = 5, 300
print(&quot;1. 남은 커피 수량 : %d잔&quot; % coffee)
while money:
    print(&quot;커피 한 잔을 뽑습니다.&quot;)
    coffee -= 1
    print(&quot;2. 남은 커피 수량 : %d잔&quot; % coffee)
    if not coffee: break
print(&quot;오늘 준비된 수량은 모두 소진되었습니다. 판매를 중지합니다.&quot;)</code></pre>
<h3 id="▪-예제-6-1부터-10까지의-숫자-중-짝수-홀수를-판단해서-출력">▪ 예제 6. 1부터 10까지의 숫자 중 짝수. 홀수를 판단해서 출력</h3>
<pre><code class="language-python">for a in range(1, 11, 1):
    if a % 2 == 0: 
        print(&quot;짝수 : %d &quot; % a)
    else: 
        print(&quot;짝수 : %d &quot; % a)
print(&quot;-------------------&quot;)
b = 0
while a &lt; 10:
    b += 1
    if b % 2 == 0: print(&quot;짝수 : %d &quot; % b)
    else: print(&quot;홀수 : %d&quot; % b)</code></pre>
<h3 id="▪-예제-7-1부터-100까지의-숫자-중-3의-배수의-합을-출력">▪ 예제 7. 1부터 100까지의 숫자 중 3의 배수의 합을 출력</h3>
<pre><code class="language-python">i , sum = 1, 0

while i &lt;= 100:
    if i % 3 == 0:
        print(&quot;%d + %d = %d&quot; % (i, sum, i+sum))
        sum += i
    i += 1
    if i == 100: break 
print(&quot;최종합 : %d &quot; % (sum))</code></pre>
<h3 id="▪-예제-8-커피-한-잔의-값은-300원이고-오늘-판매할-수량은-전체-10잔이-준비되어-있다-커피-한-잔을-뽑을-때마다-판매할-수량은-1잔씩-차감이-되고-투입된-금액은-차감된-금액을-제하고-나머지는-잔돈으로-되돌려-준다">▪ 예제 8. 커피 한 잔의 값은 300원이고 오늘 판매할 수량은 전체 10잔이 준비되어 있다. 커피 한 잔을 뽑을 때마다 판매할 수량은 1잔씩 차감이 되고 투입된 금액은 차감된 금액을 제하고 나머지는 잔돈으로 되돌려 준다.</h3>
<pre><code class="language-python">coffee = 10

while True:
  money = int(input(&quot;돈을 넣어주세요 : &quot;))
  if money == 300:
    print(&quot;한 잔만 가능한 돈이므로 커피를 줍니다.&quot;)
    coffee -= 1
    print(&quot;남은 커피의 수량은 %d잔입니다.\n&quot; % coffee)    
  elif money &gt; 300:
    print(&quot;거스름돈 %d원을 주고 커피는 줍니다.&quot; % (money-300))
    coffee -= 1
    print(&quot;남은 커피의 수량은 %d잔입니다.\n&quot; % coffee)
  else:
    print(&quot;투입한 돈은 %d원이므로 돈을 다시 돌려주고 커피는 안 줍니다.&quot; % money)
    print(&quot;남은 커피의 수량은 %d잔입니다.\n&quot; % coffee)
  if not coffee: 
    print(&quot;준비된 10잔의 커피가 다 소진되었습니다. 판매를 중지합니다.&quot;)
    break</code></pre>
<hr />
<h1 id="span-style--colororange6-함수span"><span style="color: orange;">6. 함수</span></h1>
<h2 id="61-일반">6.1 일반</h2>
<ul>
<li>어떤 내용이 소스 내에서 <code>지속적으로 반복</code>될 경우 소스의 길이가 늘어나게 되는데 이 때 반복되는 소스의 내용을 <code>임의의 형태로 묶어두고</code> 필요할 때 호출해서 사용한다면 편리하게 코딩을 할 수가 있다. 즉, <code>(핵심)</code> 소스의 형태를 보다 <code>간결</code>하게 할 수 있는 기능이 바로 <code>함수</code>이다.</li>
<li><code>함수</code>는 반복적으로 사용되는 코드 블록에 이름을 붙여놓은 형태이다.</li>
<li><code>함수</code>를 한 번 정의해 두면 지정해 둔 함수 이름을 통해 언제든 해당 코드 블록을 <code>재사용</code>할 수 있다.</li>
</ul>
<blockquote>
<ul>
<li>함수를 정의할 때는 <code>def(ine)</code>라는 키워드를 사용한다.</li>
</ul>
</blockquote>
<ul>
<li>정의해 둔 함수를 사용하는 것을 <code>호출(call)</code>이라고 부른다.</li>
<li><span style="color: red;">(매우중요) <code>Python</code></span>에서는 함수를 호출하려면 반드시 호출문 위에 함수가 먼저 정의되어 있어야 한다.</li>
</ul>
<hr />
<h2 id="612-함수의-표현">6.1.2 함수의 표현</h2>
<h3 id="일반적인-표현">일반적인 표현</h3>
<pre><code class="language-python">def 함수명(매개변수):
    수행할 문장 1 
    수행할 문장 2
    ...
함수명(매개변수)</code></pre>
<h3 id="입력값이-몇-개-인지-모를때의-표현">입력값이 몇 개 인지 모를때의 표현</h3>
<pre><code class="language-python">def 함수명(*매개변수):
    수행할 문장1
    수행할 문장2
    ...</code></pre>
<hr />
<h2 id="613-함수-작성시-요령">6.1.3 함수 작성시 요령</h2>
<ul>
<li>출력문은 가급적 함수 안에 포함되지 않도록 한다.</li>
<li>변수는 특별한 경우를 제외하고 함수 안에 정의하지 말고 밖에 정의한다.<h2 id="함수-정의시-다음의-순서대로-작업한다">함수 정의시 다음의 순서대로 작업한다.</h2>
<h3 id="▪-step-1-기본식without-함수">▪ Step 1. 기본식(without 함수)</h3>
<h3 id="▪-step-2-단일-함수로-구성">▪ Step 2. 단일 함수로 구성</h3>
<h3 id="▪-step-3-다중-함수로-구성">▪ Step 3. 다중 함수로 구성</h3>
</li>
</ul>
<hr />
<h1 id="62-기본-실습">6.2 기본 실습</h1>
<h2 id="span-stylecolorlightgreen실습-1-사칙연산span"><span style="color: lightgreen;">실습 1. 사칙연산</span></h2>
<h2 id="함수식-1-매개변수-유무에-따른-예제">함수식 1. 매개변수 유무에 따른 예제</h2>
<h3 id="▪-예제-1-매개변수가-없는-경우">▪ 예제 1. 매개변수가 없는 경우</h3>
<pre><code class="language-python">def calc():    # 함수 선언부
    a, b= 4, 2
    print(&quot;더하기 :%d&quot; % (a+b))
    print(&quot;빼기 :%d&quot; % (a-b))
    print(&quot;곱하기 :%d&quot; % (a*b))
    print(&quot;나누기 :%d&quot; % (a/b))
calc()    # 함수 호출부</code></pre>
<pre><code>더하기 :6
빼기 :2
곱하기 :8
나누기 :2</code></pre><hr />
<h3 id="▪-예제-2-매개변수가-있는-경우함수-한개로-묶어서-출력">▪ 예제 2. 매개변수가 있는 경우(함수 한개로 묶어서 출력)</h3>
<pre><code class="language-python">a, b= 4, 2

def calc(x, y): # 1. 매개변수로 사용할 변수 2개를 선언하고 초기값 부여

    print(f&quot;더하기 : {x+y}&quot;)    # 호출될 때 넘어온 변수 2개를 임의의 변수명으로 대체
    print(f&quot;뺴기 : {x-y}&quot;)
    print(f&quot;곱하기 : {x*y}&quot;)
    print(f&quot;나누기 : {x/y}&quot;)

calc(a, b)  # 2. 매개 변수를 이용해서 함수를 호출</code></pre>
<pre><code>더하기 : 6
뺴기 : 2
곱하기 : 8
나누기 : 2.0</code></pre><hr />
<h2 id="함수식-2-개별함수">함수식 2. 개별함수</h2>
<h3 id="▪-예제-1-함수-안에-출력문이-포함된-경우">▪ 예제 1. 함수 '안'에 출력문이 포함된 경우</h3>
<pre><code class="language-python">x, y = 4, 2

def num1(a, b):
    ab = a + b
    print(ab)

def num2(a, b):
    print(a - b)

def num3(a, b):
    print(a * b)

def num4(a, b):
    print(a / b)

num1(x, y)
num2(x, y)
num3(x, y)
num4(x, y)</code></pre>
<pre><code>6
2
8
2.0</code></pre><h3 id="▪-예제-2-함수-밖에-출력문이-포함된-경우">▪ 예제 2. 함수 '밖'에 출력문이 포함된 경우</h3>
<pre><code class="language-python">def num1(a, b):
    ab = a + b
    return ab

def num2(a, b):
    return a-b

def num3(a, b):
    return a*b

def num4(a, b):
    return a/b
x, y = 4, 2
c = num1(x, y)
print(c)
print(num2(x, y))
print(num3(x, y))
print(num4(x, y))</code></pre>
<hr />
<h2 id="span-stylecolorlightgreen실습-2반환값return-valuespan"><span style="color: lightgreen;">실습 2.반환값(Return Value)</span></h2>
<ul>
<li>반환값은 함수를 호출한 곳으로 함수의 최종실행 결과를 전달하는 값을 말한다.</li>
<li>(매우 중요) 인수 및 인수값은 여러 개가 존재할 수 있지만 반환값은 언제나 한 개만 존재해야 한다.<pre><code class="language-python">def multi(n1, n2):
  result = n1 + n2
  print(&quot;%d + %d = %d&quot; % (n1,n2,result))
multi(3, 4)
print(&quot;--------------------------&quot;)
</code></pre>
</li>
</ul>
<p>def add(n1, n2):
    n12 = n1 + n2
    return n12</p>
<p>a, b = 10, 5
ab = add(a,b)
print(ab)</p>
<pre><code>

### 예제 2. 결과값 유무에 따른 변화
- 입력값(매개변수)이 없는 함수
```python
def samadal():
    return &quot;madal&quot;
a = samadal()
print(a)
print(samadal())</code></pre><ul>
<li>결과값이 없는 함수<ul>
<li>함수를 사용하지 않은 경우</li>
<li>함수를 사용한 경우<pre><code class="language-python">def sum(x, y):
z = x + y
return z
</code></pre>
</li>
</ul>
</li>
</ul>
<p>a, b = 3, 4
ab = sum(a,b)
print(&quot;%d + %d = %d&quot; % (a, b, ab))
print(&quot;--------------------------&quot;)
def sum(a, b):
    c = a + b
    return c</p>
<p>a, b = 3, 4
print(&quot;%d + %d = %d&quot; % (a, b, sum(3,4)))
print(&quot;--------------------------&quot;)
def sum(a, b):
    return a + b
print(&quot;%d + %d = %d&quot; % (a, b, sum(3,4)))</p>
<pre><code>---
## &lt;span style=&quot;color:lightgreen&quot;&gt;실습 3. 입력값 갯수의 유무에 따른 함수&lt;/span&gt;
- 입력값의 갯수를 알고 있는 경우
- 입력값의 갯수를 모르고 있는 경우

```python
def s1(a, b, c):
  sum = a + b + c
  return sum
x1, y1, z1 = 1, 2, 3
print(s1(x1, y1, z1))
print(&quot;----------------------------&quot;)
def s2(*args):
  sum = 0
  for i in args:
    sum += i
  return sum
x2, y2, z2 = 4, 5, 6
xyz = s2(x2, y2, z2)
print(xyz)</code></pre><hr />
<h1 id="63-응용-실습">6.3 응용 실습</h1>
<h2 id="실습-1-함수-안에서-처리된-결과는-반드시-한-개만-반환한다">실습 1. 함수 안에서 처리된 결과는 반드시 한 개만 반환한다.</h2>
<h3 id="기본식">기본식</h3>
<pre><code class="language-python">a = &quot;HiMedia20251105&quot;
b, c, d, e, f = a[:2], a[2:7], a[7:11], a[-4:-2], a[-2:]
print(&quot;%s %s %s년 %s월 %s일&quot; % (b, c, d, e, f))</code></pre>
<h3 id="함수식">함수식</h3>
<ul>
<li><p>함수 1개만 사용한 경우(비권장)</p>
<ul>
<li><p>반환값이 여러개 있을 경우에는 <code>Tuple</code>로 반환된다.</p>
<pre><code class="language-python">def py1(a):

b1, c1, d1, e1, f1 = a[:2], a[2:7], a[7:11], a[-4:-2], a[-2:]
return b1, c1 ,d1, e1, f1
a = &quot;HiMedia20251105&quot;
p1 = py1(a)
print(type(p1))
print(&quot;%s %s %s년 %s월 %s일&quot; % (p1[0], p1[1], p1[2], p1[3], p1[4]))</code></pre>
<pre><code>&lt;class 'tuple'&gt;
Hi Media 2025년 11월 05일</code></pre></li>
</ul>
</li>
<li><p>함수 5개를 사용한 경우</p>
<pre><code class="language-python">a = &quot;HiMedia20251105&quot;
def py1(a):
  return a[:2]
def py2(a):
  return a[2:7]
def py3(a):
  return a[7:11]
def py4(a):
  return a[-4:-2]
def py5(a):
  return a[-2:]
p1, p2, p3, p4, p5 = py1(a), py2(a), py3(a), py4(a), py5(a)
print(&quot;%s %s %s년 %s월 %s일&quot; % (p1, p2, p3, p4 ,p5))</code></pre>
<pre><code>Hi Media 2025년 11월 05일</code></pre></li>
</ul>
<hr />
<h2 id="실습-2-함수를-이용해서-다음과-같은-결과가-나올-수-있도록-하는-소스">실습 2. 함수를 이용해서 다음과 같은 결과가 나올 수 있도록 하는 소스</h2>
<h3 id="출력">출력</h3>
<ul>
<li>1 ~ 5까지의 합계 : xx</li>
<li>1 ~ 10까지의 합계 : xx</li>
<li>1 ~ 100까지의 합계 : xx<pre><code class="language-python">sum = 0
for i1 in range(1, 6): sum += i1
print(&quot;1 ~ 5까지의 합계 : %d&quot; % sum)
print(&quot;===========================&quot;)
sum = 0
for i2 in range(1, 11): sum += i2
print(&quot;1 ~ 10까지의 합계 : %d&quot; % sum)
print(&quot;===========================&quot;)
sum = 0
for i3 in range(1, 101): sum += i3
print(&quot;1 ~ 100까지의 합계 : %d&quot; % sum)
print(&quot;===========================&quot;)</code></pre>
<pre><code>1 ~ 5까지의 합계 : 15
===========================
1 ~ 10까지의 합계 : 55
===========================
1 ~ 100까지의 합계 : 5050
===========================</code></pre></li>
</ul>
<hr />
<h3 id="기본식-1">기본식</h3>
<pre><code class="language-python">sum5, sum10, sum100 = 0, 0, 0
for i1 in range(1, 6): sum5 += i1
for i2 in range(1, 11): sum10 += i2
for i3 in range(1, 101): sum100 += i3

print(&quot;1 ~ 5까지의 합계 : %d&quot; % sum5)
print(&quot;1 ~ 10까지의 합계 : %d&quot; % sum10)
print(&quot;1 ~ 100까지의 합계 : %d&quot; % sum100)</code></pre>
<h3 id="함수식-1">함수식</h3>
<pre><code>def cal(v):
    sum = 0
    for i1 in range(1, v+1): sum5 += i1
    return sum

print(&quot;1 ~ 5까지의 합계 : %d&quot; % sum5)
print(&quot;1 ~ 10까지의 합계 : %d&quot; % sum10)
print(&quot;1 ~ 100까지의 합계 : %d&quot; % sum100)</code></pre><hr />
<h1 id="64-이중-함수">6.4 이중 함수</h1>
<h2 id="개요">개요</h2>
<ul>
<li>함수 안에 함수가 포함된 형태를 말한다.</li>
<li>단순하게 함수를 순서대로 나열한 것(다중함수)이 아니라 함수 안에 또 다른 함수를 호출 하는 것이다.</li>
</ul>
<h2 id="실습-1-이중함수의-이해">실습 1. 이중함수의 이해</h2>
<h3 id="기본식-2">기본식</h3>
<h3 id="단일-함수-표현">단일 함수 표현</h3>
<pre><code class="language-python">num = int(input(&quot;1. 기본급 | 2. 일 한 일수 : &quot;))
day, time, pay = 30, 8, 10030
if num == 1:
    result1 = day * time * pay
    print(f&quot;1. 당신의 급여는 {result1:,.0f}원입니다.&quot;)
elif num == 2:
    day = int(input(&quot;몇 일동안 일했는데? : &quot;))
    result2 = day * time * pay
    print(&quot;2. 당신의 급여는 {result2:,.0f}원입니다.&quot;)</code></pre>
<h3 id="이중-함수-표현">이중 함수 표현</h3>
<pre><code class="language-python">num = int(input(&quot;1. 기본급 | 2. 일 한 일수 : &quot;))
def alba1():
  if num == 1:
    result1 = alba2()
    print(&quot;1. 당신의 급여는 %d원입니다.&quot; % result1)
    print(&quot;1. 당신의 급여는 {0:,.0f}원입니다.&quot; .format(result1))
  elif num == 2:
    day = int(input(&quot;몇 일동안 일했는데? : &quot;))
    result2 = alba2(day)
    print(&quot;2. 당신의 급여는 %d원입니다.&quot; % result2)
    print(&quot;2. 당신의 급여는 {0:,.0f}원입니다.&quot; .format(result2))
def alba2(day=30, time=8, pay=10030):
   return day * time * pay

alba1() </code></pre>
<hr />
<p>물론이에요 👍
아래는 요청하신 내용을 <strong>Velog 포스트 형식</strong>(마크다운)으로 정리한 버전입니다.
기존 6.5 구조와 맞추어 통일감 있게 구성했어요 👇</p>
<hr />
<h1 id="65-입력과-출력">6.5 입력과 출력</h1>
<h2 id="651-파일-읽고-쓰기">6.5.1 파일 읽고 쓰기</h2>
<h3 id="▪-일반적인-입출력">▪ 일반적인 입출력</h3>
<ul>
<li>프로그램에서 파일을 읽고 쓰는 과정은 <strong>입출력(I/O)</strong>이라고 한다.</li>
<li>Python에서는 내장함수 <code>open()</code>을 통해 파일을 열고,
<code>read()</code>, <code>readline()</code>, <code>readlines()</code>, <code>write()</code> 등의 함수를 이용해 내용을 처리한다.</li>
<li>모든 작업이 끝나면 반드시 <code>close()</code>를 호출하여 파일을 닫는다. (자원 반환 목적)</li>
</ul>
<hr />
<h3 id="▪-파일-생성">▪ 파일 생성</h3>
<ul>
<li><p><strong>특징</strong></p>
<ul>
<li>파일 생성은 <code>JAVA</code>에서의 <code>객체=메서드()</code> 형태와 유사하다.</li>
<li>파일이 존재하면 <strong>내용을 덮어쓴다.</strong></li>
<li>파일이 존재하지 않으면 <strong>지정한 경로에 새로 생성한다.</strong></li>
</ul>
</li>
<li><p><strong>문법</strong></p>
<pre><code class="language-python">파일객체 = open(&quot;경로명\\파일명&quot;, 파일열기모드)</code></pre>
<ul>
<li><p>파일 열기 모드 종류</p>
<table>
<thead>
<tr>
<th>모드</th>
<th>의미</th>
</tr>
</thead>
<tbody><tr>
<td><code>'r'</code></td>
<td>읽기(Read)</td>
</tr>
<tr>
<td><code>'w'</code></td>
<td>쓰기(Write, 새로 생성)</td>
</tr>
<tr>
<td><code>'a'</code></td>
<td>추가(Append, 기존 내용 뒤에 추가)</td>
</tr>
</tbody></table>
</li>
<li><p>파일 작업이 끝나면 반드시 <code>파일객체.close()</code>로 닫는다. (단, 생략 가능)</p>
</li>
</ul>
</li>
<li><p><strong>실습</strong></p>
<pre><code class="language-python">a = open(&quot;samadal.txt&quot;, 'w')       # 이렇게는 사용하지 않는다.
a.close()

b = open(&quot;d:\\samadal.txt&quot;, 'w')   # 경로와 함께 사용하는 것이 일반적이다.
b.close()</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6346d2c7-4c60-4354-8ca8-02f00c9cd41f/image.png" /></p>
</li>
</ul>
<hr />
<h3 id="▪-readline-함수">▪ readline() 함수</h3>
<h4 id="🔹-개요">🔹 개요</h4>
<ul>
<li>파일의 내용을 <strong>한 줄만</strong> 읽어오는 함수.</li>
<li>파일이 존재하지 않으면 <code>FileNotFoundError</code> 발생.</li>
<li>실행할 때마다 커서가 한 줄씩 이동한다.</li>
</ul>
<h4 id="🔹-실습">🔹 실습</h4>
<p><strong>1) 한 줄만 읽기</strong></p>
<pre><code class="language-python">d = open(&quot;g:\\pysamadal.txt&quot;, 'r')  # 파일을 읽기 모드로 열기
line = d.readline()
print(line)
d.close()</code></pre>
<p><strong>2) 모든 줄 읽기</strong></p>
<pre><code class="language-python">e = open(&quot;g:\\pysamadal.txt&quot;, 'r')

while True:
    line = e.readline()
    print(line)
    if not line: break   # 더 이상 읽을 내용이 없으면 종료

e.close()</code></pre>
<hr />
<h3 id="▪-readlines-함수">▪ readlines() 함수</h3>
<h4 id="🔹-개요-1">🔹 개요</h4>
<ul>
<li>파일의 <strong>모든 줄을 한꺼번에 리스트 형태로</strong> 읽는다.</li>
<li>각 줄은 리스트의 한 요소(<code>str</code>)로 저장된다.</li>
</ul>
<h4 id="🔹-실습-1">🔹 실습</h4>
<pre><code class="language-python">f = open(&quot;g:\\pysamadal.txt&quot;, 'r')

lines = f.readlines()   # 모든 줄을 리스트로 반환

for line in lines:
    print(line)

f.close()</code></pre>
<hr />
<h3 id="▪-read-함수">▪ read() 함수</h3>
<h4 id="🔹-개요-2">🔹 개요</h4>
<ul>
<li>파일의 <strong>전체 내용을 한 번에 문자열 형태로 읽어옴</strong>.</li>
<li>줄 구분 없이 모든 내용을 그대로 읽는다.</li>
</ul>
<h4 id="🔹-실습-2">🔹 실습</h4>
<pre><code class="language-python">g = open(&quot;g:\\pysamadal.txt&quot;, 'r')
data = g.read()
print(data)
g.close()</code></pre>
<hr />
<h3 id="▪-write-함수">▪ write() 함수</h3>
<h4 id="🔹-개요-3">🔹 개요</h4>
<ul>
<li>파일에 <strong>새로운 내용을 작성하거나 추가</strong>할 때 사용한다.</li>
<li><code>'w'</code> 모드는 기존 내용을 덮어쓰며,
<code>'a'</code> 모드는 기존 내용 뒤에 새로운 내용을 이어 붙인다.</li>
</ul>
<h4 id="🔹-실습-3">🔹 실습</h4>
<pre><code class="language-python">h = open(&quot;g:\\pysamadal.txt&quot;, 'a')

for i in range(11, 21):     # 11 ~ 20번째 줄 추가
    data = &quot;%d번째 줄입니다.\n&quot; % i
    h.write(data)

h.close()</code></pre>
<hr />
<h3 id="📌-정리표">📌 정리표</h3>
<table>
<thead>
<tr>
<th>함수</th>
<th>기능</th>
<th>반환 형태</th>
<th>특징</th>
</tr>
</thead>
<tbody><tr>
<td><code>readline()</code></td>
<td>한 줄씩 읽기</td>
<td>문자열</td>
<td>커서가 한 줄씩 이동</td>
</tr>
<tr>
<td><code>readlines()</code></td>
<td>모든 줄 읽기</td>
<td>리스트</td>
<td>줄 단위로 저장됨</td>
</tr>
<tr>
<td><code>read()</code></td>
<td>전체 내용 읽기</td>
<td>문자열</td>
<td>파일 전체를 한 번에 읽음</td>
</tr>
<tr>
<td><code>write()</code></td>
<td>내용 쓰기/추가</td>
<td>없음</td>
<td><code>'w'</code>: 새로쓰기 / <code>'a'</code>: 추가</td>
</tr>
</tbody></table>
<hr />
<h3 id="💡-tip">💡 TIP</h3>
<ul>
<li>파일 경로 지정 시 <code>\</code> 대신 <code>/</code>를 사용해도 된다.
예: <code>&quot;g:/pysamadal.txt&quot;</code></li>
<li><code>with open(...) as f:</code> 구문을 사용하면 <code>close()</code>를 생략할 수 있다.</li>
</ul>
<hr />