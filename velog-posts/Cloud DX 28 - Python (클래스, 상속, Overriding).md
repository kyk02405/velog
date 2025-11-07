# Cloud DX 28 - Python (클래스, 상속, Overriding)

- 📅 Published: Thu, 06 Nov 2025 05:40:53 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-28-Python-%ED%81%B4%EB%9E%98%EC%8A%A4-%EC%83%81%EC%86%8D-Overriding)

<hr />
<h1 id="span-style--colorred7-클래스classspan"><span style="color: red;">7. 클래스(Class)</span></h1>
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
<ul>
<li>사용자에게 입력받아 단을 출력<pre><code class="language-python">class Dan:
  def sam5(self, odan5):
      self.odan5 = odan5
  def sam6(self):
      for i5 in range(1, 10):
          print(&quot;%d x %d = %d&quot; % (odan5, i5 ,odan5*i5))
odan5 = int(input(&quot;단 입력 : &quot;))
a = Dan()
a.sam6()</code></pre>
</li>
</ul>
<hr />
<h1 id="span-style--colorred8-클래스class의-상속inheritancespan"><span style="color: red;">8. 클래스(Class)의 상속(Inheritance)</span></h1>
<h2 id="81-일반">8.1 일반</h2>
<h3 id="811-개요">8.1.1 개요</h3>
<ul>
<li>임의의 어떤 클래스를 생성할 때 다른 클래스의 기능을 물려받을 수 있게 만든느 것을 말한다.</li>
<li>(특징) <code>상속 받는 클래스</code>는 형태가 함수 형태를 보인다.</li>
<li><code>기존 클래스(부모 클래스)</code>는 그대로 두고 클래스의 기능을 확장하고자 할 떄 사용한다.</li>
</ul>
<h3 id="812-클래스">8.1.2 클래스</h3>
<ul>
<li>상속해 주는 클래스(Base Class, 부모 클래스)</li>
<li>상속 받는 클래스(Child Class, 자식 클래스, 파생 클래스)</li>
</ul>
<hr />
<h2 id="82-실습">8.2 실습</h2>
<h3 id="821-실습-1-상속의-이해">8.2.1 실습 1. 상속의 이해</h3>
<pre><code class="language-python"># 상속해 주는 클래스
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second

a = FourCal(4, 2)
caf = a.first
cas = a.second
caa = a.add()
print(&quot;%d + %d = %d &quot; % (caf, cas, caa))

# 상속받는 클래스
class MoreFourCal(FourCal):
    pass        # 수행할 것이 없다.
                # 상속받는 클래스가 수행할 내용이 없다.
b = MoreFourCal(8, 5)
cafb = b.first
casb = b.second
caab = b.add()
print(&quot;%d + %d = %d&quot; %(cafb, casb, caab))</code></pre>
<hr />
<h3 id="822-실습-2-상속의-확장">8.2.2 실습 2. 상속의 확장</h3>
<pre><code class="language-python">class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second

a = FourCal(4, 2)
caf = a.first
cas = a.second
caa = a.add()
print(&quot;%d + %d = %d &quot; % (caf, cas, caa))
# 클래스 확장
class Samadal(FourCal):     # 상속받는 클래스 안에 별도로 추가되는
    def pow(self):          # 내용을 상속 확장이라고 한다.
        return self.first ** self.second
c = Samadal(2, 3)
print(c.pow())

# 상속받는 클래스
class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second

d = MoreFourCal(4, 2)
print(&quot;%d&quot; % (d.pow()))</code></pre>
<hr />
<h3 id="823-실습-3-부모-클래스-자식-클래스-상속-확장-모두-포함">8.2.3 실습 3. 부모 클래스, 자식 클래스, 상속 확장 모두 포함</h3>
<ul>
<li>예제 1. 부모 클래스, 자식 클래스, 상속 확장<pre><code class="language-python">class Animal:       # 부모 클래스
  def __init__(self, name):
      self.name = name
  def move(self):
      print(&quot;Move&quot;)
  def speak(self):
      pass
</code></pre>
</li>
</ul>
<p>class Dog(Animal):      # 자식 클래스
    def speak(self):    # 상속 확장( 파생 클래스 안에 기능이 추가된 것)
        print(&quot;Bark&quot;)</p>
<p>class Duck(Animal):
    def speak(self):
        print(&quot;Quack&quot;)</p>
<p>dog = Dog(&quot;puppy&quot;)      # 인스턴스 객체
duck = Duck(&quot;ori&quot;)      # </p>
<p>dog.move()<br />dog.speak()</p>
<p>duck.move()
duck.speak()</p>
<pre><code>- 예제 2. 홍길동씨의 과목(3과목)별 점수를 입력 받은 후 평균 점수를 출력
```python
kor = int(input(&quot;국어 :&quot;))
eng = int(input(&quot;영어 :&quot;))
mat = int(input(&quot;수학 :&quot;))

class Hong:
    def __init__(self, x, y ,z):
        self.x = x
        self.y = y
        self.z = z
class Gil:
    def sum(self):
        self.result = self.x + self.y + self.z
        return self.result

class Dong(Hong, Gil):
    def avg(self):
        return self.result / 3

val = Dong(kor , eng, mat)
s = val.sum()
a = val.avg()
print(f&quot;합계 {s} | 평균 {a:.2f}&quot;) </code></pre><hr />
<h2 id="83-overriding오버라이딩-메서드-재성성">8.3 Overriding(오버라이딩, 메서드 재성성)</h2>
<h3 id="831-개요">8.3.1 개요</h3>
<ul>
<li>부모 클래스(상속해 준 클래스)에 있는 메서드를 동일한 이름으로 다시 생성하는 것을 말한다.</li>
<li>오버라이딩이 되면 상속해 준 클래스의 메서드 대신 상속 받은 클래스의 메서드를 호출한다. 즉, '전역변수보다 지역변수가 우선한다'와 동일한 내용이다.</li>
<li>(특징) 오버라이딩이 적용되는 경우는 대부분 <code>return</code>값이 <code>0</code>일 경우에 사용한다.</li>
<li>파생클래스와 모두 동일하고 단지 부모 클래스의 메서드를 재생성한다는 것이다.</li>
</ul>
<hr />
<h3 id="832-실습">8.3.2 실습</h3>
<ul>
<li>예제 1. 전역변수보다 지역변수가 우선한다.<ul>
<li>부모 클래스의 메서드가 무시되고 자식 클래스의 메서드가 사용된다.</li>
<li>즉, 전역변수보다 지역변수가 우선한다와 같은 개념으로 보면 된다.</li>
<li>자식 클래스는 <code>second</code>가 <code>0</code>일때만 동작하고 <code>0</code>이 아닌 경우에는 </li>
<li>부모 클래스의 값을 통해 실행된다.<pre><code class="language-python">class FourCal:
def __init__(self, first, second):
    self.first = first
    self.second = second
def div(self):
    return self.first / self.second
</code></pre>
</li>
</ul>
</li>
</ul>
<p>a = FourCal(4, 2)
print(a.div())
print(&quot;-------------------&quot;)
class madal(FourCal):
    def div(self):
        if self.second == 0: return 0 
        else: 
            return self.first / self.second</p>
<p>b = madal(5, 3)
print(b.div())</p>
<pre><code>- 예제 2.
  - 오버라이딩을 위해 설정되어 있지만 `return`값이 `0`이 아니거나 없기 때문에 오버라이딩이 적용되지 않는다.
  - 따라서 오버라이딩이 적용되지 않을 때는 그냥 일반적인 파생 클래스로 생각하면 된다.
```python
class Himedia:
    lastname = &quot;사&quot;
    def __init__(self, name): 
        self.fullname = self.lastname + name

    def travel(self, where):
        print(&quot;%s, %s&quot; % (self.fullname, where))

class Ed(Himedia):
    lastname = &quot;김&quot;
    def __init__(self, name): 
        self.fullname = self.lastname + name
a = Himedia(&quot;마달&quot;)
b = Ed(&quot;달이&quot;)
a.travel(&quot;제주도&quot;)
a.travel(&quot;독도&quot;)
</code></pre><hr />
<h1 id="span-style--colorred9-module모듈span"><span style="color: red;">9. Module(모듈)</span></h1>
<h2 id="91-일반">9.1 일반</h2>
<h3 id="911-개요">9.1.1 개요</h3>
<ul>
<li>함수나 변수 또는 클래스를 모아 놓은 파일이다.</li>
<li><code>Python</code> 프로그램에서 불러온 후 사용할 수 있게 만든 파일이다.</li>
<li><code>Python</code> 관련 소스들은 매우 많은 모듈을 사용한다.</li>
<li>직접 만들어서 사용할 수도 있고 다른 사람들이 미리 만들어 놓은 모듈을 사용할 수도 있다.</li>
<li><span style="color: red;">(특징)</span> 확장자가 <code>*.py</code>인 파일은 모두 모듈이 될 수가 있다.</li>
<li><span style="color: red;">(주의)</span> 기본적으로 <code>모듈 파일</code>과 모듈 파일을 불러오는 '주 파일'은 같은 경로에 둬야 한다.</li>
</ul>
<h3 id="912-문법">9.1.2 문법</h3>
<pre><code class="language-python">Import &lt;모듈로 사용할 확장자가 `*.py`인 파일&gt;</code></pre>
<h3 id="913-예시">9.1.3 예시</h3>
<ul>
<li><p>모듈 둘러보기(모듈로 매개변수)</p>
<ul>
<li>소스 코드 (01.py)<pre><code class="language-python">import sys  # Python 시스템의 내장 모듈 호출
        # '컴퓨터 언어'에서의 'Header File'과 유사하다.
        # 즉, 'C언어'에서의 최상단에 선언하는 'stdio.h'
args = sys.argv[1:] # 실행 순서 하단에 있는 터미널 영역에 다음과 같이 
for i in args: print(i) # 입력한다.       </code></pre>
</li>
<li>실행 순서<ul>
<li>'cmd' 창을 실행한 후 현재 작업하고 있는 'D:\3_VMs\Python\vcode'로 이동한다.</li>
<li>위의 '01.py' 파일을 생성한다.</li>
<li>'python 01.py samadal madalgyo 0WonHara'을 입력, 실행하면 된다.</li>
</ul>
</li>
</ul>
</li>
<li><p>모듈 생성 방법</p>
<ul>
<li>작업 개요<ul>
<li>모듈로 사용할 파일<code>(m2.py)</code>과 <code>주 파일(m1.py)</code>을 생성하고 테스트한다.</li>
</ul>
</li>
</ul>
</li>
<li><p><code>m2.py</code></p>
<pre><code class="language-python"># 모듈로 사용할 파일
def add(a, b):
  return a + b
def sub(a, b):
  return a - b </code></pre>
</li>
<li><p><code>m1.py</code></p>
<pre><code class="language-python"># 모듈로 사용할 파일을 불러와서 실행하는 주 파일
import m2   # 주 파일에서 사용할 모듈 파일을 입력할 때는 `py`는 뺀다.
print(m2.add(4, 3))
print(m2.sub(4, 3)) </code></pre>
</li>
<li><p>테스트</p>
<ul>
<li><code>Visual Studio Code</code>에서 실행하거나 실행창(cmd)에서 <code>python m1.py</code>를 실행하면 된다.</li>
</ul>
</li>
<li><p>모듈 호출 방법</p>
<ul>
<li>문법<pre><code class="language-python">from &lt;모듈 파일명&gt; improt &lt;모듈 함수&gt;</code></pre>
</li>
<li>예시<ul>
<li>작업 개요<ul>
<li>모듈 파일<code>(m2.py)</code>는 그대로 두고 주 파일<code>(m1.py)</code>만 수정</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="92-실습">9.2 실습</h2>