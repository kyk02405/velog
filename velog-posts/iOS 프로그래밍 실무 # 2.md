<hr />
<h2 id="구글링-실습-자료형의-종류와-크기가-궁금해요">구글링 실습: 자료형의 종류와 크기가 궁금해요</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/532751e1-1831-48c4-9fc7-2d3d95ab5d70/image.png" /></p>
<pre><code class="language-swfit">var x = 10
print(type(of:x))
let s = MemoryLayout.size(ofValue: x)//8
let t = MemoryLayout&lt;Int&gt;.size
print(s, t)
//swift memory size</code></pre>
<hr />
<h2 id="정수-데이터-타입--int">정수 데이터 타입 : Int</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c7a42121-da40-4326-8633-5288365d4499/image.png" /></p>
<pre><code class="language-swfit">var x = 10
print(type(of:x))
print(x)
print(&quot;x&quot;)
print(&quot;\(x)&quot;)
print(&quot;값은 \(x)입니다.&quot;)
print(&quot;Int32 Min = \(Int32.min) Int32 Max = \(Int32.max)&quot;)</code></pre>
<hr />
<h2 id="부동-소수점-데이터-타입-double-vs-float">부동 소수점 데이터 타입: Double vs Float</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3695e0cd-1c99-42ed-8a4e-50370dba7f3e/image.png" /></p>
<pre><code class="language-swift">var myWeight = 58.5 //무슨 형? 
print(type(of:myWeight))</code></pre>
<hr />
<h2 id="부울-데이터-타입--bool">부울 데이터 타입 : Bool</h2>
<pre><code class="language-swift">var orangesAreOrange : Bool</code></pre>
<hr />
<h2 id="문자-데이터-타입--character">문자 데이터 타입 : Character</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/73475977-2212-4897-807e-7322e0ba77a5/image.png" /></p>
<pre><code class="language-swift">var myChar1 : Character
var myChar2 : Character = &quot;:&quot;
var myChar3 : Character = &quot;X&quot; 
print(type(of: myChar3))</code></pre>
<hr />
<h2 id="문자열-데이터-타입--string">문자열 데이터 타입 : String</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7f45e4b4-dab1-4954-873c-40b597ac08af/image.png" /></p>
<pre><code class="language-swift">var userName : String = &quot;Kim&quot; // : String 생략하는 것이 일반적임
var age = 20
var message = &quot;\(userName)의 나이는 \(age)입니다.&quot;
print(message) // Kim의 나이는 20입니다. </code></pre>
<hr />
<h2 id="특수-문자이스케이프-시퀀스">특수 문자/이스케이프 시퀀스</h2>
<ul>
<li>\n ― 개행</li>
<li>\r ― 캐리지 리턴(carriage return)</li>
<li>\t ― 수평 탭</li>
<li>\ ― 역슬래시</li>
<li>&quot; ― 큰따옴표(문자열 선언부에 큰따옴표를 쓰고 싶을 경우에 사용됨)</li>
<li>' ― 작은따옴표(문자열 선언부에 작은따옴표를 쓰고 싶을 경우에 사용됨)</li>
<li>\u{nn} ― nn 위치에 유니코드 문자를 표현하는 두 개의 16진수가 배치되는 1바이트 유니코드 스칼라</li>
<li>\u{nnnn} ― nnnn 위치에 유니코드 문자를 표현하는 네 개의 16진수가 배치되는 2바이트 유니코드 스칼라</li>
<li>\U{nnnnnnnn} ― nnnnnnnn 위치에 유니코드 문자를 표현하는 네 개의 16진수가 배치되는 4바이트 유니코드 스칼라</li>
</ul>
<hr />
<h2 id="변수--var">변수 : var</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b3cae30e-f016-444c-9b78-f0e86b7ddec7/image.png" /></p>
<pre><code class="language-swift">var myVariable = 10 // :Int
var x = 0.0, y = 0.0, z = 0.0</code></pre>
<hr />
<h2 id="상수--let">상수 : let</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a2a897bd-6235-4882-8173-d59a02dfa080/image.png" /></p>
<pre><code class="language-swift">let maximumNumber = 10
let π = 3.14159
let 🐶🐮 = &quot;dogcow&quot; //[Edit]-[Emoji &amp; Symbols]</code></pre>
<hr />
<h2 id="타입-어노테이션과-타입-추론">타입 어노테이션과 타입 추론</h2>
<pre><code class="language-swift"> var signalStrength = 2.231 // var signalStrength : Double = 2.231
 let companyName = &quot;My Company&quot;
 signalStrength라는 변수를 Double 타입으로 간주
 companyName이라는 상수는 String 타입으로 간주</code></pre>
<hr />
<h2 id="상수의-값-할당">상수의 값 할당</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/30894961-d7cd-4dff-8448-6df20d3fb838/image.png" /></p>
<pre><code class="language-swift">let bookTitle: String
var book = true
if book {
bookTitle = &quot;iOS&quot;
} else {
bookTitle = &quot;Android&quot;
}
print(bookTitle)</code></pre>
<hr />
<h2 id="튜플tuple">튜플(Tuple)</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/47799d8b-4fdb-4195-add1-246a4fa838d9/image.png" /></p>
<pre><code class="language-swift">let myTuple = (10, 12.1, &quot;Hi&quot;)
var myString = myTuple.2
print(myString) //출력되는 값은? </code></pre>
<hr />
<h2 id="튜플tuple-실습">튜플(Tuple) 실습</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/be842154-cff8-42a7-bdd1-1eafd3306fc7/image.png" /></p>
<pre><code class="language-swift">print(myTuple.message, myTuple.2) 
let (myInt, myFloat, myString) = myTuple
print(type(of:myTuple))

let myTuple = (count: 10, length: 12.1, message:&quot;Hi&quot;) 
print(myTuple.message, myTuple.2) </code></pre>
<hr />
<h2 id="typealias-void--">typealias Void = ()</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b8831778-5882-4f9f-b01b-6ce2404ed6eb/image.png" /></p>
<pre><code class="language-swift">func logMessage(_ s: String) { // {앞에 -&gt;Void나 -&gt;() 생략
print(&quot;Message: \(s)&quot;)
}
let logger: (String)-&gt;Void = logMessage //여기서는 함수 자료형이라 -&gt;Void 생략 불가
logger(&quot;Hello&quot;)</code></pre>
<hr />
<h2 id="옵셔널-타입-강제-언래핑forced-unwrapping-1">옵셔널 타입 강제 언래핑(forced unwrapping) 1</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c2f26163-0b80-4314-88ee-97c1171f9e31/image.png" /></p>
<pre><code class="language-swift">var x : Int? //옵셔널 정수형 변수 x 선언
var y : Int = 0
x = 10 // 주석처리하면?
print(x) // Optional(10)
print(x!) // forced unwrapping해서 10이 나옴
print(y)</code></pre>
<hr />
<h2 id="forced-unwrapping">forced unwrapping</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4da8dd99-439d-4452-924c-2e1a5355a87f/image.png" /></p>
<pre><code class="language-swift">var x : Int?
x = 10
if x != nil {
print(x!)
}
else {
print(&quot;nil&quot;)
}
var x1 : Int?
if x1 != nil {
print(x1!)
}
else {
print(&quot;nil&quot;)
}</code></pre>
<hr />
<h2 id="옵셔널-타입-강제-언래핑forced-unwrapping-2--optional-binding">옵셔널 타입 강제 언래핑(forced unwrapping) 2 : optional binding</h2>
<pre><code class="language-swift">if let constantName = optionalName{
//옵셔널 변수가 값이 있다면 언래핑해서 일반 상수 constantName에 대입하고 if문 실행
//값이 없다면 if문의 조건이 거짓이 되어 if문을 실행하지 않음
}
if var variableName = optionalName {
//옵셔널 변수가 값이 있다면 언래핑해서 일반 변수 varibleName에 대입하고 if문 실행
//값이 없다면 if문의 조건이 거짓이 되어 if문을 실행하지 않음
}</code></pre>
<hr />
<h2 id="optional-binding">optional binding</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/60578342-a4f7-4fe2-bf1f-6d8c9974bf88/image.png" /></p>
<pre><code class="language-swift">var x : Int?
x = 10
if let xx = x { //옵셔널 변수 x가 값(10)이 있으므로 언래핑해서 일반 상수 xx에 대입하고 if문 실행
print(x,xx)
}
else {
print(&quot;nil&quot;)
}
var x1 : Int?
if let xx = x1 { //옵셔널 변수 x1이 값이 없어서 if문의 조건이 거짓이 되어 if문 실행하지 않고 else로 감
print(xx)
}
else {
print(&quot;nil&quot;)
}</code></pre>
<hr />
<h2 id="여러-옵셔널을-언래핑">여러 옵셔널을 언래핑</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e5019dd1-c240-49be-b4ec-836ba49ab507/image.png" /></p>
<pre><code class="language-swift">var pet1: String?
var pet2: String?
pet1 = &quot;cat&quot;
pet2 = &quot;dog&quot;
if let firstPet = pet1, let secondPet = pet2 {
print(firstPet, secondPet)
} else {
print(&quot;nil&quot;)
}</code></pre>
<h3 id="과제--위-소스를-short-form-of-if-let-to-the-optional-binding으로-변경">과제 : 위 소스를 short form of if-let to the Optional Binding으로 변경</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/46732e64-94ea-4a63-b01f-a3e1756e831d/image.png" /></p>
<pre><code class="language-swift">var pet1: String?
var pet2: String?
pet1 = &quot;cat&quot;
pet2 = &quot;dog&quot;

print(pet1 ?? &quot;nil&quot;, pet2 ?? &quot;nil&quot;)</code></pre>
<hr />
<h2 id="optional-binding여러-옵셔널-값-동시에-언래핑">optional binding(여러 옵셔널 값 동시에 언래핑)</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4aef190c-563d-43ca-a54e-14bf62003a7d/image.png" /></p>
<pre><code class="language-swift">var x : Int?
var y : Int?
x = 10
y = 20
if let xx = x {
print(xx)
}
else {
print(&quot;nil&quot;)
}
if let yy = y {
print(yy)
}
else {
print(&quot;nil&quot;)
}</code></pre>
<hr />
<h2 id="nil-coalescing-operator-nil합병연산자-">Nil-Coalescing Operator (Nil합병연산자) ??</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b220c88b-e868-410c-9f1e-088556f05441/image.png" /></p>
<pre><code class="language-swift">let defaultColor = &quot;black&quot;
var userDefinedColor: String? // defaults to nil
var myColor = userDefinedColor ?? defaultColor
//nil이므로 defaultColor인 black으로 할당됨
print(myColor) //black
userDefinedColor = &quot;red&quot;
myColor = userDefinedColor ?? defaultColor
//nil이 아니므로 원래 값인 red가 할당됨
print(myColor) //red, 주의 optional(red)가 아님</code></pre>
<pre><code class="language-swift">var age : Int?
age = 20
print(age) //과제:값은? Optional(20)
var myAge = age ?? 1
print(myAge) //과제: 값은? 20</code></pre>
<hr />
<h2 id="중요옵셔널을-언래핑하는-여러가지-방법guard-let제외">중요:옵셔널을 언래핑하는 여러가지 방법(guard-let제외)</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0933761f-2c28-4510-a1d4-0e77c89b3765/image.png" /></p>
<pre><code class="language-swift">var x : String? = &quot;Hi&quot;
// = &quot;Hi&quot; 지우고도 실습
print(x, x!)
if let a = x {
print(a)
}
let c = x ?? &quot;&quot;
print(c)
let b = x!.count
print(type(of:b),b)
let b1 = x?.count
print(type(of:b1),b1, b1!)</code></pre>
<hr />
<h2 id="두-가지-optional-형--int-vs-int">두 가지 Optional 형 : Int? vs Int!</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8311b934-829a-4478-8ef3-cb50519347bd/image.png" /></p>
<pre><code class="language-swift">let x : Int? = 1
let y : Int = x!
let z = x
print(x,y,z) //Optional(1) 1 Optional(1)
print(type(of:x),type(of:y),type(of:z))
//Optional&lt;Int&gt; Int Optional&lt;Int&gt;
let a : Int! = 1 //Implicitly Unwrapped Optional
let b : Int = a //Optional로 사용되지 않으면 자동으로 unwrap함
let c : Int = a!
let d = a //Optional로 사용될 수 있으므로 Optional형임
let e = a + 1
print(a,b,c,d,e) //Optional(1) 1 1 Optional(1) 2
print(type(of:a),type(of:b),type(of:c),type(of:d), type(of:e))
//Optional&lt;Int&gt; Int Int Optional&lt;Int&gt; Int</code></pre>
<hr />
<h2 id="int형을-property로-갖는-클래스">Int!형을 property로 갖는 클래스</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9398cbb3-287c-48b2-a8a8-586cdca59d19/image.png" /></p>
<pre><code class="language-swift">class MyAge {
var age : Int!
init(age: Int) {
self.age = age
}
func printAge() {
print(age) //optional(1)
print(age+1) //2, age! + 1 라고 쓰지 않아도 됨
let age1 : Int = age
print(age1) //1
let age2 = age + 2
print(age2) //3
}
}
var han = MyAge(age:1)
han.printAge()</code></pre>
<hr />
<h2 id="옵셔널은-연관-값associated-value을-갖는-enum">옵셔널은 연관 값(associated value)을 갖는 enum</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9e6d8343-a3db-490b-9f69-4c63b711bbb4/image.png" /></p>
<pre><code class="language-swift">var x : Int? = 20 //.some(20)
var y : Int? = Optional.some(10)
var z : Int? = Optional.none
var x1 : Optional&lt;Int&gt; = 30
print(x, y, z, x1) </code></pre>
<hr />
<h2 id="any와-anyobject">Any와 AnyObject</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a0dc1caf-29c2-49e9-ac0a-5c832568b627/image.png" /></p>
<pre><code class="language-swift">var x: Any = &quot;Hi&quot;
print(x, type(of:x))
x = 10
print(x, type(of:x))
x = 3.5
print(x, type(of:x))
//type을 검사해서 사용</code></pre>
<hr />
<h2 id="anyobject-예제">AnyObject 예제</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5b5f9c2a-1045-4b1b-be96-58d74d81b270/image.png" /></p>
<pre><code class="language-swift">class Person {
var name: String = &quot;KIM&quot;
}
let kim: AnyObject = Person()
//모든 클래스가 암시적으로 준수하는 프로토콜
let kim2 = kim as! Person // 부모인스턴스 as! 자식클래스
print(kim2.name)
if let kim1 = kim as? Person {
print(kim1.name)
}</code></pre>
<hr />
<h2 id="대입-연산자">대입 연산자</h2>
<ul>
<li><p>왼쪽에 있는 피연산자는 값이 할당되는 변수 또는 상수이며, 오른쪽에 있는 피연산자는 할당할 값</p>
</li>
<li><p>오른쪽 피연산자는 주로 산술식 또는 논리식을 수행하는 표현식이며, 그결과는 왼쪽 피연산자인 변수나 상수에 할당</p>
<pre><code class="language-swift">var x: Int? // 옵셔널 Int 변수를 선언함
var y = 10 // 일반 Int 변수를 선언하고 초기화함
x = 10 // 값을 x에 할당함, Optional(10)
x = x! + y // x + y의 결과를 x에 할당 Optional(20)
x = y // y의 값을 x에 할당함, Optional(10)</code></pre>
<hr />
<h2 id="산술-연산자">산술 연산자</h2>
</li>
<li><p>보통 두 개의 피연산자를 받는 이항(binary) 연산자</p>
</li>
<li><p>값이 음수임을 가리키는 단항 마이너스 연산자(unary negative
operator)인 ‘ - ’</p>
<ul>
<li>var x = -10 // 변수 x에 -10을 할당하기 위해 사용되는 단항 - 연산자<pre><code class="language-swift">x = x – 5 // x에서 5를 빼는 뺄셈 연산자
- (단항) 변수 또는 표현식의 값을 음수로 만듦
* 곱셈
/ 나눗셈
+ 덧셈
- 뺄셈
% 나머지 연산</code></pre>
</li>
</ul>
</li>
<li><p>하나의 표현식에 여러 개의 연산자를 사용할 수 있음
x = y * 10 + z - 5 / 4</p>
</li>
</ul>
<hr />
<h2 id="복합-대입-연산자">복합 대입 연산자</h2>
<pre><code class="language-swift">x = x + y
x += y
 변수 x값과 변수 y값을 더하고 그 결과를 변수 x에 저장
 x += y x와 y를 더하고 그 결과를 x에 할당
 x -= y x에서 y를 빼고 그 결과를 x에 할당
 x *= y x와 y를 곱하고 그 결과를 x에 할당
 x /= y x를 y로 나누고 그 결과를 x에 할당
 x %= y x를 y로 나눈 나머지를 x에 할당
 x &amp;= y x와 y의 bit AND 연산 결과를 x에 할당
 x |= y x와 y의 bit OR 연산 결과를 x에 할당</code></pre>
<hr />
<h2 id="증가-연산자와-감소-연산자--는-없음">증가 연산자(++)와 감소 연산자(--)는 없음</h2>
<pre><code class="language-swift"> x = x + 1 // x 변수의 값을 1 증가시킴
 x = x - 1 // x 변수의 값을 1 감소시킴
 이러한 방법 대신 ++ 연산자와 --연산자를 사용할 수도
있었음
 x++ // x를 1 증가시킴, Swift 3에서 없어짐, x+=1
 x-- // x를 1 감소시킴, Swift 3에서 없어짐, x-=1</code></pre>
<hr />
<h2 id="비교-연산자">비교 연산자</h2>
<ul>
<li>비교의 결과로 불리언(Boolean) 값을 반환<pre><code class="language-swiftvar">var x = 10
var y = 20
result = x &lt; y //true</code></pre>
<pre><code class="language-swift">x == y x와 y가 같다면 true를 반환
x &gt; y x가 y보다 크면 true를 반환
x &gt;= y x가 y보다 크거나 같다면 true를 반환
x &lt; y x가 y보다 작다면 true를 반환
x &lt;= y x가 y보다 작거나 같다면 true를 반환
x != y x와 y가 같지 않다면 true를 반환
==는 값이 같은가?
===는 동일한 메모리 주소인가?</code></pre>
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/24b22134-b1a7-4c09-8bdd-66e79ca5ebd1/image.png" /></li>
</ul>
<pre><code class="language-swift">class Person {}
let person1 = Person()
let person2 = person1
let person3 = Person()
print(person1 === person2) // true
print(person1 === person3) // false</code></pre>
<hr />
<h2 id="논리-연산자">논리 연산자</h2>
<ul>
<li>NOT(!), AND(&amp;&amp;), OR(||)와 XOR(^)</li>
<li>NOT(!) 연산자는 불리언 값 또는 표현식의 결과를 현재와
반대로 바꿈</li>
<li>var flag = true // 변수는 참</li>
<li>var secondFlag = !flag // secondFlag는 거짓</li>
<li>OR(||) 연산자는 두 개의 피연산자 중에 하나라도 참이면
참(true), 두 개 모두 거짓이면 거짓(false)을 반환</li>
</ul>
<hr />
<h2 id="범위-연산자">범위 연산자</h2>
<ul>
<li>닫힌 범위 연산자(closed range operator)<ul>
<li>x...y<ul>
<li>x에서 시작하여 y로 끝나는 범위에 포함된 숫자</li>
</ul>
</li>
<li>5...8<ul>
<li>5, 6, 7, 8</li>
</ul>
</li>
</ul>
</li>
<li>반 열린 범위 연산자(half-open range operator)<ul>
<li>x..&lt;y<ul>
<li>x부터 시작하여 y가 포함되지 않는 모든 숫자</li>
</ul>
</li>
<li>5..&lt;8<ul>
<li>5, 6, 7</li>
</ul>
</li>
</ul>
</li>
<li>One-Sided Ranges<pre><code class="language-swift">let names = [&quot;A&quot;, &quot;B&quot;, &quot;C&quot;, &quot;D&quot;]
for name in names[2...] { //[...2], [..&lt;2] //과제: 실행 결과
print(name)
} // C
// D</code></pre>
</li>
</ul>
<hr />
<h2 id="삼항-연산자-">삼항 연산자 ?:</h2>
<ul>
<li>비교 연산을 빠르게 하기 위해 삼항 연산자(ternary operator)를 지원</li>
<li>[조건] ? [참 표현식] : [거짓 표현식]</li>
<li>삼항 연산자는 [조건] 부분을 계산하여 참(true) 혹은 거짓(false)을 확인하여
결과가 참이면 [참 표현식] 부분이 실행되며, 거짓이면 [거짓 표현식] 부분을 수행<pre><code class="language-swift">var x = 1
var y = 2
print(&quot;더 큰 값은 \(x &gt; y ? x : y)&quot;)</code></pre>
</li>
</ul>
<hr />
<h2 id="nil-coalescing-operator-nil합병연산자--1">nil-Coalescing Operator (nil합병연산자) ??</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4485b55f-39b2-4374-b6cd-0541e28c416e/image.png" /></p>
<pre><code class="language-swift">let defaultColor = &quot;black&quot;
var userDefinedColor: String? // defaults to nil
var myColor = userDefinedColor ?? defaultColor
//nil이므로 defaultColor인 black으로 할당됨
print(myColor) //black
userDefinedColor = &quot;red&quot;
myColor = userDefinedColor ?? defaultColor
//nil이 아니므로 원래 값인 red가 할당됨
print(myColor) //red, 주의 optional(red)가 아님</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/02a6e106-7ad9-4e43-8165-1bdcd46bf5dd/image.png" /></p>
<pre><code class="language-swift">let defaultAge = 1
var age : Int?
age = 20
print(age) //과제:값은? Optional(20)
var myAge = age ?? defaultAge
//age가 nil이 아니므로 언래핑된 값이 나옴
print(myAge) //과제: 값은? 20
var x : Int? = 1
var y = x ?? 0
print(y) 1</code></pre>
<hr />
<h2 id="타입-검사--is">타입 검사 : is</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bff39138-a653-4f94-8603-e75337bd2508/image.png" /></p>
<ul>
<li>타입 검사(type check)<pre><code class="language-swift">let x = 1
if x is Int {
print(&quot;Int형&quot;)
}</code></pre>
</li>
<li>객체가 MyClass라는 이름의 클래스의 인스턴스인지 검사<ul>
<li>인스턴스가 해당 클래스인가?<ul>
<li>인스턴스 is 클래스<pre><code class="language-swift">if myobject is MyClass {
// myobject는 MyClass의 인스턴스이다
}
class A {}
let a = A()
if a is A{
print(&quot;Yes&quot;)
}</code></pre>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="for-in-반복문">for-in 반복문</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/982c02c9-c59d-4924-b232-557a97cccc96/image.png" /></p>
<pre><code class="language-swift">for index in 1...5 {
print(index)
}</code></pre>
<hr />
<h2 id="_로-참조체i-생략-가능">_로 참조체(i) 생략 가능</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/415df7c7-5dd6-4f9c-9f63-25941b2412e2/image.png" /></p>
<pre><code class="language-swift">for i in 1...5 {
print(&quot;\(i) 안녕&quot;)
}
for _ in 1...5 {
print(&quot;안녕&quot;)
}</code></pre>
<hr />
<h2 id="배열의-항목-접근">배열의 항목 접근</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/239d1d37-6fa1-4c4f-a96b-2aae96683d60/image.png" /></p>
<pre><code class="language-swift">let names = [&quot;A&quot;, &quot;B&quot;, &quot;C&quot;, &quot;D&quot;]
for name in names {
print(name)
}</code></pre>
<hr />
<h2 id="dictionary의-항목-접근">dictionary의 항목 접근</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6b7d4c3e-0d80-40d2-87e2-297d8ce276b4/image.png" /></p>
<pre><code class="language-swift">let numberOfLegs = [&quot;Spider&quot;: 8, &quot;Ant&quot;: 6, &quot;Dog&quot;: 4]
//dictionary는 key:value형식의 배열
for (animalName, legCount) in numberOfLegs {
print(&quot;\(animalName)s have \(legCount) legs&quot;)
}
// Spiders have 8 legs
// Ants have 6 legs
// Dogs have 4 legs</code></pre>
<hr />
<h2 id="while-반복문">while 반복문</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d1f87d28-386b-4969-bb2e-c6cd967f5953/image.png" /></p>
<pre><code class="language-swift">var myCount = 0
while myCount &lt; 1000 {
myCount+=1
}
print(myCount) //결과는?</code></pre>
<hr />
<h2 id="repeatwhile-반복문">repeat~while 반복문</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9112f2a7-a2ae-4e0d-9f32-e53d08698116/image.png" /></p>
<pre><code class="language-swift">
var i = 10
repeat {
i=i-1
print(i) //출력 결과
} while (i &gt; 0)</code></pre>
<hr />
<h2 id="반복문에서-빠져나오기break">반복문에서 빠져나오기(break</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/108c7b3c-f6b7-4bf6-a103-42b3a8d6b30f/image.png" /></p>
<pre><code class="language-swift">for i in 1..&lt;10 {
    if i &gt; 5 {
        break
    }
    print(i)
}
</code></pre>
<hr />
<h2 id="continue문">continue문</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/eb804623-c341-4326-bbaf-ecf428380ee9/image.png" /></p>
<pre><code class="language-swift">for i in 1...10 {
if i % 2 == 0 {
continue
}
print(i)
}</code></pre>
<hr />
<h2 id="if문">if문</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2593661f-f457-4376-ad3b-b577894bc379/image.png" /></p>
<pre><code class="language-swift">var x = 10
if x &gt; 5 {
print(&quot;5보다 큽니다&quot;)
}</code></pre>
<hr />
<h2 id="if문-조건에서-콤마조건나열condition-list">if문 조건에서 콤마:조건나열(condition-list)</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2ca86a07-e697-4ec1-87ad-496588dddeb8/image.png" /></p>
<pre><code class="language-swift">var x = 1
var y = 2
if x == 1 &amp;&amp; y==2 { //논리식이 둘 다 참일 때
print(x,y)
}
if x == 1, y==2 { //조건이 둘 다 참일 때, 두 조건을 콤마로 연결한 condition-list
print(x,y)
}</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f834c009-1d49-4eef-b7b6-dd280724b634/image.png" /></p>
<pre><code class="language-swift">var a: Int? = 1
var b: Int? = 2

print(a, b) // 출력: Optional(1) Optional(2)

if let a1 = a, let b1 = b { // Optional Binding을 콤마(,)로 나열
    print(a1, b1) // 출력: 1 2
}

// ❌ 잘못된 코드: Optional Binding에서는 `&amp;&amp;`를 사용할 수 없음
// if let a1 = a &amp;&amp; let b1 = b {  
//     print(a1, b1)  
// }
</code></pre>
<hr />
<h2 id="ifelse문">if~else문</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3f3fe1cf-2afa-40c8-bca2-e3277c6c09b1/image.png" /></p>
<pre><code class="language-swift">var x = 3
if x % 2 == 0 {
print(&quot;짝수입니다&quot;)
}else{
print(&quot;홀수입니다&quot;)
}</code></pre>
<hr />
<h2 id="다중-if-else문">다중 if-else문</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/865c5653-ccf1-41c1-8116-5d2241010744/image.png" /></p>
<pre><code class="language-swift">var num = 3
if num == 1 || num == 3 {
print(&quot;당신은 남성이군요!\n&quot;)
}else if num == 2 || num == 4 {
print(&quot;당신은 여성이군요!\n&quot;)
}else {
print(&quot;당신은 대한민국 사람이 아니군요!\n&quot;)
}</code></pre>
<hr />
<h2 id="다중-if-else문--bmi-계산-결과-판정">다중 if-else문 : BMI 계산 결과 판정</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2b04fcf2-bc07-4c7d-a283-c5a59207ac02/image.png" /></p>
<pre><code class="language-swift">let weight = 60.0
let height = 170.0
let bmi = weight / (height*height*0.0001) // kg/m*m
var body = &quot;&quot;
if bmi &gt;= 40 {
body = &quot;3단계 비만&quot;
} else if bmi &gt;= 30 &amp;&amp; bmi &lt; 40 {
body = &quot;2단계 비만&quot;
} else if bmi &gt;= 25 &amp;&amp; bmi &lt; 30 {
body = &quot;1단계 비만&quot;
} else if bmi &gt;= 18.5 &amp;&amp; bmi &lt; 25 {
body = &quot;정상&quot;
} else {
body = &quot;저체중&quot;
}
print(&quot;BMI:\(bmi), 판정:\(body)&quot;)</code></pre>
<h3 id="과제--switch-case문으로-변경하기">과제 : switch-case문으로 변경하기</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1ecea862-d575-4b2a-a382-a465b381a375/image.png" /></p>
<pre><code class="language-swift">let weight = 60.0
let height = 170.0
let bmi = weight / (height * height * 0.0001) // kg/m*m
var body = &quot;&quot;

switch bmi {
case 40...:
    body = &quot;3단계 비만&quot;
case 30..&lt;40:
    body = &quot;2단계 비만&quot;
case 25..&lt;30:
    body = &quot;1단계 비만&quot;
case 18.5..&lt;25:
    body = &quot;정상&quot;
default:
    body = &quot;저체중&quot;
}

print(&quot;BMI:\(bmi), 판정:\(body)&quot;)
</code></pre>
<hr />
<h2 id="guard문조건식이-거짓이면-실행">guard문(조건식이 거짓이면 실행)</h2>
<ul>
<li>guard문은 swift 2에 도입된 구문</li>
<li>guard문은 표현식이 거짓(false)으로 판단될 경우에 수행될 else 절을 반드시 포함해야 함<ul>
<li>else 절에 속한 코드는 현재의 코드 흐름을 빠져 나갈 수 있는 구문(return, break, continue, throw 구문)을
반드시 포함해야 함</li>
<li>또는 다른 함수를 else 코드 블록 안에서 호출할 수도 있음<pre><code class="language-swift">guard &lt;불리언 표현식&gt; else {
// 표현식이 거짓일 경우에 실행될 코드
&lt;코드 블록을 빠져 나갈 구문&gt;
}
// 표현식이 참일 경우에 실행되는 코드는 이곳에 위치</code></pre>
</li>
</ul>
</li>
<li>guard문은 기본적으로 특정 조건에 맞지 않을 경우에 현재의 함수나 반복문에서 빠져 나갈 수
있도록 하는 ‘조기 출구(early exit)’ 전략을 제공</li>
</ul>
<hr />
<h2 id="guardlet의-활용">guard~let의 활용</h2>
<ul>
<li>guard는 return, break, continue, throw 등 제어문 전환 키워드를 쓸 수 있는
상황이라면 사용이 가능</li>
<li>그래서 함수 뿐 아니라 반복문 등 특정 블록 내부에 있으면 사용 가능</li>
<li>물론 함수 내부에 있다면 보통 return을 써서 해당 함수를 조기에 빠져나오는 조기
출구 용도로 사용</li>
<li>실제 앱을 만들다 보면 옵셔널 바인딩 때문에 다중 if<del>else를 사용해야 하는데,
guard</del>let을 사용하면 다중 루프 없는 훨씬 가독성이 좋은 코드가 가능해서 그런 경우
많이 사용</li>
<li>다음은 while문 안에 guard와 break문을 사용한 경우<ul>
<li>이렇게 guard문을 활용하지는 않음<pre><code class="language-swift">var x = 1
while true {
guard x &lt; 5 else { break }//조건(x&lt;5)이 거짓일 때 실행(break)
print(x) //1 2 3 4, 조건(x&lt;5)이 참일 때 실행
x = x + 1
}</code></pre>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="iflet-vs-guardlet">if<del>let vs. guard</del>let</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/08aa6a4e-c6da-4f6b-853a-0189d6c82334/image.png" /></p>
<pre><code class="language-swift">func printName(firstName: String, lastName: String?) {
    // Optional Binding (if let)
    if let lName = lastName {
        // lastName이 nil이 아니면 출력
        print(lName, firstName)
    } else {
        // lastName이 nil이면 메시지 출력
        print(&quot;성이 없네요!&quot;)
    }
}

// 사용 예시
printName(firstName: &quot;길동&quot;, lastName: &quot;홍&quot;) // 홍 길동
printName(firstName: &quot;철수&quot;, lastName: nil) // 성이 없네요!
</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b9caea45-688c-4ce9-86e5-758a06695e57/image.png" /></p>
<pre><code class="language-swift">func printName(firstName: String, lastName: String?) {
    // Optional Binding (guard let)
    guard let lName = lastName else {
        // lastName이 nil이면 메시지 출력 후 함수 종료
        print(&quot;성이 없네요!&quot;)
        return
    }
    // lastName이 nil이 아니면 실행
    print(lName, firstName)
}

// 사용 예시
printName(firstName: &quot;길동&quot;, lastName: &quot;홍&quot;) // 홍 길동
printName(firstName: &quot;철수&quot;, lastName: nil) // 성이 없네요!
</code></pre>
<hr />
<h2 id="guard-letelse로-옵셔널-바인딩">guard let~else로 옵셔널 바인딩</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b618eab3-8930-4052-8460-067f6ba9cadd/image.png" /></p>
<pre><code class="language-swift">func multiplyByTen(value: Int?) {
guard let number = value else {//조건식이 거짓(nil)일 때 else 블록 실행
print(&quot;nil&quot;)
return
}
print(number*10) //조건식이 참일 때 실행, 주의 : number를 guard문 밖인 여기서도 사용 가능
}
multiplyByTen(value: 3) //30
multiplyByTen(value: nil)
</code></pre>
<hr />
<h2 id="switch-case문-예제">switch-case문 예제</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ad67cb88-d44f-4edd-8c9a-061833b5a4a8/image.png" /></p>
<pre><code class="language-swift">var value = 0
switch (value)
{
case 0:
print(&quot;영&quot;)
case 1:
print(&quot;일&quot;)
case 2:
print(&quot;이&quot;)
case 3:
print(&quot;삼&quot;)
default:
print(&quot;4이상&quot;)
}
let someCharacter: Character = &quot;z&quot;
switch someCharacter {
case &quot;a&quot;:
print(&quot;The first letter of the alphabet&quot;)
case &quot;z&quot;:
print(&quot;The last letter of the alphabet&quot;)
default:
print(&quot;Some other character&quot;)
}
// Prints &quot;The last letter of the alphabet&quot;</code></pre>
<hr />
<h2 id="switch-case문-주의-사항">switch-case문 주의 사항</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1a32ec89-4a20-49b9-abec-21f141ea0699/image.png" /></p>
<hr />
<h2 id="switch-case문-결합하기--콤마-사용">switch-case문 결합하기 : 콤마 사용</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/61128100-6197-40b0-af62-65972f133e4e/image.png" /></p>
<pre><code class="language-swift">var value = 3
var days : Int = 0
switch(value)
{
case 1,3,5,7,8,10,12:
print(&quot;31 일입니다&quot;)
case 4,6,9,11:
print(&quot;30 일입니다&quot;)
case 2:
print(&quot;28 or 29 일입니다&quot;)
default:
print(&quot;월을 잘못 입력하셨습니다&quot;)
}
let anotherCharacter: Character = &quot;a&quot;
switch anotherCharacter {
case &quot;a&quot;, &quot;A&quot;:
print(&quot;A 글자&quot;)
default:
print(&quot;A글자 아님&quot;)
}
//&quot;The letter A&quot;
</code></pre>
<hr />
<h2 id="switch-case문에서의-범위-지정-매칭">switch-case문에서의 범위 지정 매칭</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/80594d76-6fdf-4a48-9331-36e7eb3657e4/image.png" /></p>
<pre><code class="language-swift">let weight = 60.0
let height = 170.0
let bmi = weight / (height*height*0.0001) // kg/m*m
var body = &quot;&quot;
if bmi &gt;= 40 {
body = &quot;3단계 비만&quot;
} else if bmi &gt;= 30 &amp;&amp; bmi &lt; 40 {
body = &quot;2단계 비만&quot;
} else if bmi &gt;= 25 &amp;&amp; bmi &lt; 30 {
body = &quot;1단계 비만&quot;
} else if bmi &gt;= 18.5 &amp;&amp; bmi &lt; 25 {
body = &quot;정상&quot;
} else {
body = &quot;저체중&quot;
}
print(&quot;BMI:\(bmi), 판정:\(body)&quot;)</code></pre>
<h3 id="과제--switch-case문으로-변경하기-1">과제 : switch-case문으로 변경하기</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9943996f-aeec-424a-8db2-465a48fc53dd/image.png" /></p>
<pre><code class="language-swift">let weight = 60.0
let height = 170.0
let bmi = weight / (height * height * 0.0001) // kg/m*m
var body: String

switch bmi {
case 40...:
    body = &quot;3단계 비만&quot;
case 30..&lt;40:
    body = &quot;2단계 비만&quot;
case 25..&lt;30:
    body = &quot;1단계 비만&quot;
case 18.5..&lt;25:
    body = &quot;정상&quot;
default:
    body = &quot;저체중&quot;
}

print(&quot;BMI:\(bmi), 판정:\(body)&quot;)</code></pre>
<hr />
<h2 id="switch-case에서-where절-사용하기">switch-case에서 where절 사용하기</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5ef5b8c1-0eab-4bdc-9358-637e00a129b2/image.png" /></p>
<pre><code class="language-swift">let number = 27

switch number {
case let x where x % 2 == 0:
    print(&quot;\(x)는 짝수입니다.&quot;)
case let x where x % 2 != 0:
    print(&quot;\(x)는 홀수입니다.&quot;)
default:
    print(&quot;숫자가 아닙니다.&quot;)
}
</code></pre>
<hr />
<h2 id="where--조건을-추가">where : 조건을 추가</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a43b4210-c259-4ee2-b6e3-dfb621806067/image.png" /></p>
<pre><code class="language-swift">var numbers: [Int] = [1, 2, 3, 4, 5]
for num in numbers where num &gt; 3 {
print(num)
}</code></pre>
<hr />
<h2 id="fallthrough">fallthrough</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/89ef0b36-57c6-4a4e-8934-231b73526955/image.png" /></p>
<pre><code class="language-swift">var value = 4
switch (value)
{
case 4:
print(&quot;4&quot;)
fallthrough
case 3:
print(&quot;3&quot;)
fallthrough
case 2:
print(&quot;2&quot;)
fallthrough
default:
print(&quot;1&quot;)
}</code></pre>
<hr />
<h2 id="함수">함수</h2>
<pre><code class="language-c">#include &lt;stdio.h&gt;
void Fun( int param ) // parameter(매개변수, 인자), 형식 매개변수(formal parameter)
{
printf(&quot;%d&quot;,param);
}
int main()
{
Fun( 10 ); // 10은 argument(전달인자), 실 매개변수(actual parameter)
return 0;
}</code></pre>
<hr />
<h2 id="함수를-선언하는-방법">함수를 선언하는 방법</h2>
<pre><code class="language-swfit">func &lt;함수명&gt; (&lt;매개변수 이름&gt;: &lt;매개변수 타입&gt;, &lt;매개변수 이름&gt;: &lt;매개변수 타입&gt;,... ) -&gt; &lt;반환값 타입&gt; {
// 함수 코드
}</code></pre>
<ul>
<li>func ― 함수라는 것을 스위프트 컴파일러에게 알려주는 키워드</li>
<li>&lt;함수명&gt; ― 함수에 할당되는 이름</li>
<li>&lt;매개변수 이름&gt; ― 함수 코드 내에서 참조되는 매개변수의 이름</li>
<li>&lt;매개변수 타입&gt; ― 함수에 전달되는 매개변수의 타입</li>
<li>&lt;반환값 타입&gt; ― 함수가 반환하는 결과에 대한 데이터 타입. 반환하지 않으면 “-&gt;Void”는 생략 가능</li>
<li>매개변수를 받지 않으며 결과를 반환하지도 않고 오직 메시지만 출력</li>
</ul>
<pre><code class="language-swift">func sayHello() { //리턴값 없으면( -&gt; Void ) 지정하지 않아도 됨
print(&quot;Hello&quot;)
}
void sayHello() { //C, C++
printf(&quot;Hello&quot;);
}
</code></pre>
<ul>
<li>하나의 문자열과 하나의 정수를 매개변수로 받아서 문자열을 반환<pre><code class="language-swift">func message(name: String, age: Int) -&gt; String {
return(&quot;\(name) \(age)&quot;)
}</code></pre>
</li>
</ul>
<hr />
<h2 id="swift-함수-정의와-호출하기">Swift 함수 정의와 호출하기</h2>
<pre><code class="language-swift">func sayHello() { //-&gt;Void 생략
print(&quot;Hello&quot;)
} //정의
sayHello() //호출</code></pre>
<hr />
<h2 id="c언어에서-swift-함수-변경-연습">C언어에서 Swift 함수 변경 연습</h2>
<pre><code class="language-c">int add(int x, int y) { //C, C++
return(x+y);
}
add(10,20);
</code></pre>
<pre><code class="language-swift">func add(x: Int, y: Int) -&gt; Int {
return(x+y)
}
add(x:10, y:20)
</code></pre>