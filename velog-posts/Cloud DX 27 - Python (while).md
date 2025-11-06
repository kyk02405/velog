# Cloud DX 27 - Python (while)

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
<h1 id="7-클래스class">7. 클래스(Class)</h1>
<h2 id="71-일반">7.1 일반</h2>
<hr />
<h3 id="711-개요">7.1.1 개요</h3>
<ul>
<li>함수들과 변수들의 <strong>집합체</strong>를 말한다.</li>
<li>클래스 안에는 <code>Instance(인스턴스, 객체)</code>를 만들어서 사용할 수 있다.</li>
</ul>
<h4 id="▪-형태">▪ 형태</h4>
<ul>
<li><strong>Class가 적용되지 않은 상태</strong></li>
</ul>
<pre><code class="language-python">변수 = 값
변수 = 함수()</code></pre>
<ul>
<li><strong>Class가 적용된 상태</strong></li>
</ul>
<pre><code class="language-python">객체 = 값
객체 = 함수()</code></pre>
<hr />
<h4 id="▪-클래스class-인스턴스instance-객체object-메소드method의-비교">▪ 클래스(Class), 인스턴스(Instance), 객체(Object), 메소드(Method)의 비교</h4>
<ul>
<li>인스턴스는 <strong>클래스에 의해 만들어진 객체</strong>를 말한다.</li>
<li><code>a = Samadal()</code>
→ <code>a</code> 자체는 <strong>객체(Object)</strong>이며, 클래스 <code>Samadal</code>의 <strong>인스턴스(Instance)</strong>이다.</li>
<li>일반적으로 사용할 때 <code>a</code>는 <strong>변수(Variable)</strong>이고, <code>Samadal</code>은 <strong>값(Value)</strong>이 된다.</li>
<li>클래스 안에서 사용할 때 <code>a</code>는 <strong>객체(Object)</strong>이며, <code>Samadal</code>의 <strong>인스턴스(Instance)</strong>로 작동한다.</li>
<li>클래스 안에서 만들어진 함수는 <strong>메소드(Method)</strong>라고 한다.</li>
</ul>
<hr />
<h3 id="712-문법">7.1.2 문법</h3>
<pre><code class="language-python">class 클래스명:
    클래스변수1
    클래스변수2
    ...
    함수정의()    # 클래스 밖에서는 '함수', 안에서는 '메서드'</code></pre>
<hr />
<h3 id="713-일반식-함수식-클래스식">7.1.3 일반식, 함수식, 클래스식</h3>
<h4 id="▪-일반식">▪ 일반식</h4>
<ul>
<li>맨 앞에서부터 작성하면 된다.</li>
</ul>
<pre><code class="language-python">변수 = 값
print(변수)</code></pre>
<h4 id="▪-함수식">▪ 함수식</h4>
<ul>
<li>일반식을 <strong>들여쓰기</strong> 하면 된다.</li>
</ul>
<pre><code class="language-python">def 함수명():
    일반식</code></pre>
<h4 id="▪-클래스식">▪ 클래스식</h4>
<ul>
<li>함수식을 <strong>들여쓰기</strong> 하면 된다.</li>
</ul>
<pre><code class="language-python">class 클래스명:
    def 함수명():
        일반식</code></pre>
<hr />
<h3 id="714-클래스-관련-용어">7.1.4 클래스 관련 용어</h3>
<hr />
<h4 id="▪-클래스-멤버">▪ 클래스 멤버</h4>
<ul>
<li>클래스 내부에서 정의되는 구성요소 전체를 말하며,
<strong>메서드(Method)</strong>, <strong>클래스 변수(Class Variable)</strong>, <strong>초기자(Initializer)</strong>,
<strong>인스턴스 변수(Instance Variable)</strong>, <strong>소멸자(Destructor)</strong> 등이 있다.</li>
</ul>
<hr />
<h4 id="▪-클래스-변수-class-variable">▪ 클래스 변수 (Class Variable)</h4>
<ul>
<li><strong>핵심:</strong> 클래스 안에 존재하지만 <strong>메서드 밖에 있는 변수</strong>를 말한다.</li>
<li>해당 클래스를 사용하는 모든 인스턴스에서 <strong>공유</strong>된다.</li>
<li><strong>클래스명.변수명</strong>으로 내부·외부 모두 접근 가능하다.</li>
</ul>
<p>예시:</p>
<pre><code>KG.KGE.Kgitbank.강남점.1101호.사마달  
himedia.취업반.종로점.1501호.사마달</code></pre><hr />
<h4 id="▪-인스턴스-변수-instance-variable">▪ 인스턴스 변수 (Instance Variable)</h4>
<ul>
<li>하나의 클래스로부터 여러 <strong>객체 인스턴스</strong>를 생성해서 사용한다.</li>
<li><strong>핵심:</strong> 클래스 안의 메서드 안에서 사용되며, <code>self.변수명</code> 형태로 선언된다.</li>
<li><strong>중요:</strong> 클래스 밖에서는 <code>객체변수.인스턴스변수</code>로 접근한다.</li>
</ul>
<hr />
<h4 id="▪-변수-접근자-access-modifier">▪ 변수 접근자 (Access Modifier)</h4>
<ul>
<li>Python은 <code>public</code>, <code>protected</code>, <code>private</code>과 같은 접근 제한자를 <strong>별도로 사용하지 않는다.</strong></li>
<li>기본적으로 모든 멤버는 <strong>public</strong>이다.</li>
<li>특정 변수나 메서드를 private으로 만들고 싶을 때는 <strong>이름 앞에 밑줄 두 개(__)</strong>를 붙인다.</li>
</ul>
<p>예시:</p>
<pre><code class="language-python">self.__name = &quot;Samadal&quot;</code></pre>
<hr />
<h4 id="▪-초기자-initializer">▪ 초기자 (Initializer)</h4>
<ul>
<li><strong>핵심:</strong> 클래스로부터 새 객체를 생성할 때마다 실행되는 <code>__init__()</code> 메서드.</li>
<li>객체 생성 시 <strong>인스턴스 변수를 초기화</strong>하거나, <strong>초기 상태를 설정</strong>한다.</li>
</ul>
<p>예시:</p>
<pre><code class="language-python">class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age</code></pre>
<hr />
<h4 id="▪-메서드-method">▪ 메서드 (Method)</h4>
<ul>
<li><p>클래스 안에 정의된 함수를 말한다.</p>
</li>
<li><p><code>Class</code> 안에 정의된 메서드는 <strong>첫 번째 매개변수로 <code>self</code></strong>를 반드시 포함한다.</p>
</li>
<li><p>종류:</p>
<ul>
<li><strong>인스턴스 메서드 (Instance Method)</strong></li>
<li><strong>정적 메서드 (Static Method)</strong></li>
<li><strong>클래스 메서드 (Class Method)</strong></li>
</ul>
</li>
</ul>
<hr />
<h4 id="▪-self">▪ self</h4>
<ul>
<li><code>self</code>는 <strong>클래스 인스턴스 자신을 참조하는 변수</strong>이다.</li>
<li><code>self</code>를 통해 인스턴스 변수에 접근하거나 메서드를 호출할 수 있다.</li>
<li>Python이 자동으로 인스턴스를 전달해 주기 때문에, 메서드 정의 시 반드시 첫 번째 인자로 사용한다.</li>
</ul>
<p>예시:</p>
<pre><code class="language-python">class Calc:
    def __init__(self, first, second):
        self.first = first      # self가 객체 자신을 가리킴
        self.second = second

    def add(self):
        return self.first + self.second</code></pre>
<p>💬 즉,</p>
<blockquote>
<p><code>self</code>는 객체 자신을 가리키는 포인터 같은 역할을 하며,
클래스 내부에서 <strong>자신의 속성과 메서드에 접근하기 위해 반드시 필요하다.</strong></p>
</blockquote>
<hr />
<p>✅ <strong>요약 정리</strong></p>
<table>
<thead>
<tr>
<th>구분</th>
<th>의미</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td>클래스 변수</td>
<td>모든 인스턴스가 공유하는 변수</td>
<td><code>ClassName.variable</code></td>
</tr>
<tr>
<td>인스턴스 변수</td>
<td>각 객체가 개별로 가지는 변수</td>
<td><code>self.variable</code></td>
</tr>
<tr>
<td>초기자</td>
<td>객체 생성 시 실행되는 메서드</td>
<td><code>__init__()</code></td>
</tr>
<tr>
<td>메서드</td>
<td>클래스 안에서 정의된 함수</td>
<td><code>def func(self):</code></td>
</tr>
<tr>
<td>self</td>
<td>인스턴스 자신을 가리키는 참조자</td>
<td><code>self.name = name</code></td>
</tr>
</tbody></table>
<hr />
<h2 id="72-실습">7.2 실습</h2>
<h3 id="721-클래스를-이용하기-쉬운-예제">7.2.1 클래스를 이용하기 쉬운 예제</h3>
<ul>
<li>예제 1. 함수를 이용한 경우<pre><code class="language-python">result1 = result2 = 0
def add1(num):
global result1    # 함수 외부에 선언된 변수를 사용할 때 사용
result1 += num
return result1
def add2(num):
global result2    # 함수 외부에 선언된 변수를 사용할 때 사용
result2 += num
return result2
</code></pre>
</li>
</ul>
<p>print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))</p>
<pre><code>- 예제 2. 클래스를 이용한 경우
```python
class Calculator:       # 클래스 정의

    def __init__(self):     # Method(초기자 메서드)
        self.result = 0     # self. Class 안에 정의되는 함수는 맨 앞에
    def add(self, num):
        self.result += num
        return self.result

    result, num = 0, 5
    print(add(result, num))

cal = Calculator()
print(cal.add(4))</code></pre><h3 id="722-진법-변환을-이용한-예제">7.2.2 진법 변환을 이용한 예제</h3>
<ul>
<li>예제 1. <code>2진수</code>를 <code>10진수</code>로 출력<pre><code class="language-python">bin1 = 0b1101010001110001
bin2 = 1101010001110001
</code></pre>
</li>
</ul>
<p>class bin12():</p>
<pre><code>def b1(self, bb, cc):
    self.bb = bb
    self.cc = cc

def b2(self):
    return self.bb

def b3(self):
    return self.cc</code></pre><pre><code>- 예제 2. 16진수 값(3D5F)을 10진수로 출력
```python
class _H:
    def a(self, hx):
        self.hx = hx
    def b(self):
        return self.hx

h = _H() 
hexa = 0x3D5F
h.a(hexa)
print(&quot;%d&quot; % hexa)</code></pre><ul>
<li><p>예제 3. 10진수 값(1024)를 10진수로 출력</p>
<pre><code class="language-python">class _D:
  def __init__(self):
      self.result = 0
  def b(self, d):
      self.d = d
      return self.d
h = _D()
dec = 1024
print(&quot;%x&quot; % dec)</code></pre>
</li>
<li><p>예제 4. 16진수(5C90)와 8진수(652)의 합을 10진수로 출력</p>
<pre><code class="language-python">class _H:
  def h1(self.h11):
      self.h11 = h11
  def h2(self):
      return self.h11
</code></pre>
</li>
</ul>
<p>class _O:
    def o1(self.o11):
        self.o11 = o11
    def o2(self):
        return self.o11</p>
<p>h = _H()
o = _O()</p>
<p>hexa, oct = 0x5C90, 0o652
h.h1(hexa)
o.o1(oct)
result = h.h2() + o.o2()
print(&quot;%d&quot; % result)</p>
<pre><code>
---
### 7.2.3 응용
- 예제 1. 계산기
  - 한 개의 클래스에 모든 메서드들을 위치시키고 외부로 부터 초기값을 받아오는 메서드(madal)를 통해서 외부로부터 초기값을 받아와서 각 메서드별로 반환값을 반환하고 출력
  - 한 개의 클래스에서 초기값을 받아오는 메서드없이  초기값을 직접 받아와서 계산 후 반환 호출한 곳으로 반환값을 반환하고 

```python
class FourCal:
  def add(self, first, second):
    self.first = first
    self.second = second
    self.result = self.first + self.second
    return self.result
  def mul(self, first, second):
    self.first = first
    self.second = second    
    self.result = self.first - self.second
    return self.result
  def sub(self, first, second):
    self.first = first
    self.second = second    
    self.result = self.first * self.second
    return self.result
  def div(self, first, second):
    self.first = first
    self.second = second    
    self.result = self.first / self.second
    return self.result        

a, b = 7, 4

fc = FourCal()

print(&quot;%d&quot; % fc.add(a, b))
print(&quot;%d&quot; % fc.mul(a, b))
print(&quot;%d&quot; % fc.sub(a, b))
print(&quot;%d&quot; % fc.div(a, b))</code></pre><pre><code class="language-python"># 개선 버전
class Base:
    def data(self, first, second):
        self.first = first
        self.second = second

class ADD(Base):
    def calc(self):
        return self.first + self.second

class MIN(Base):
    def calc(self):
        return self.first - self.second

class MUL(Base):
    def calc(self):
        return self.first * self.second

class DIV(Base):
    def calc(self):
        return self.first / self.second

# 사용
a = ADD(); a.data(4, 2); print(a.calc())
b = MIN(); b.data(4, 2); print(b.calc())
c = MUL(); c.data(4, 2); print(c.calc())
d = DIV(); d.data(4, 2); print(d.calc())
</code></pre>
<hr />
<h1 id="73-클래스의-인자값-self">7.3 클래스의 인자값 'self'</h1>
<h2 id="731-개요">7.3.1 개요</h2>
<ul>
<li>클래스 밖에서 값을 받아들일 때는 'self'인자를 사용한다.</li>
<li>클래스 안에 있는 함수(메서드)에 인자를 입력할 때는 첫 항목에 'self'를 입력한다.<h2 id="732-self를-사용할-때의-두-가지-유형">7.3.2 'self'를 사용할 때의 두 가지 유형</h2>
</li>
<li>외부에서 받아들인 값을 그냥 사용할 경우 메스드 안에만 'self'를 입력한다.</li>
<li>외부에서 받아들인 값을 변수로 <code>치환해서 사용</code>할 경우 모든 변수에 'self'를 함께 입력한다.</li>
</ul>
<h2 id="733-실습">7.3.3 실습</h2>
<pre><code class="language-python">odan4 = 5 # 5단으로 사용할 값을 전역변수로 선언
class Dan:
    def sam4(self):
        for i4 in range(1, 10):
                print(&quot;%d x %d = %d&quot; % (odan4, i4, odan4*i4))

a = Dan()
# print(a.sam4())   # 클래스의 메서드 안에 이미 출력문이 있기 떄문에
                    # 호출만 해야 한다. 만약 입력했을 경우에는
                    # 메서드의 출력문은 정상적으로 출력되고 이 출력은
                    # 'None'으로 출력된다.
a.sam4()</code></pre>