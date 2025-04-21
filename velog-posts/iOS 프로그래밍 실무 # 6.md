<hr />
<h1 id="옵셔널-체이닝을-지원하는-프로그래밍-언어">옵셔널 체이닝을 지원하는 프로그래밍 언어</h1>
<p>옵셔널 체이닝(optional chaining)은 <strong>객체나 값이 <code>null</code> 또는 <code>undefined</code>일 수 있을 때, 오류 없이 안전하게 접근</strong>할 수 있도록 도와주는 문법입니다. 이 기능을 지원하는 대표적인 프로그래밍 언어들과 예시는 다음과 같습니다:</p>
<hr />
<h3 id="✅-1-swift">✅ <strong>1. Swift</strong></h3>
<p>Swift에서는 <code>?</code> 연산자를 사용해서 옵셔널 체이닝을 합니다.</p>
<pre><code class="language-swift">class Person {
    var name: String?
}

var person: Person? = Person()
person?.name = &quot;경윤&quot;

// 옵셔널 체이닝 예시
if let name = person?.name {
    print(&quot;이름은 \(name)입니다&quot;)
} else {
    print(&quot;이름이 없습니다&quot;)
}</code></pre>
<ul>
<li><code>person</code>이 <code>nil</code>이면, <code>person?.name</code> 도 자동으로 <code>nil</code>을 반환하고 crash 나지 않음.</li>
</ul>
<hr />
<h3 id="✅-2-javascript-es2020-이후">✅ <strong>2. JavaScript (ES2020 이후)</strong></h3>
<p>JavaScript에서도 <code>?.</code> 연산자로 옵셔널 체이닝을 지원합니다.</p>
<pre><code class="language-javascript">let user = {
  profile: {
    name: &quot;경윤&quot;
  }
};

console.log(user.profile?.name); // &quot;경윤&quot;
console.log(user.account?.email); // undefined (오류 발생하지 않음)</code></pre>
<ul>
<li><code>user.account?.email</code>에서 <code>account</code>가 존재하지 않아도 undefined만 반환되고 에러는 발생하지 않음.</li>
</ul>
<hr />
<h3 id="✅-3-kotlin">✅ <strong>3. Kotlin</strong></h3>
<p>Kotlin에서는 <code>?.</code> 연산자를 사용하여 널 세이프 코딩이 가능합니다.</p>
<pre><code class="language-kotlin">data class User(val name: String?)

val user: User? = User(&quot;경윤&quot;)

val username = user?.name ?: &quot;이름 없음&quot;
println(username)</code></pre>
<ul>
<li><code>user?.name</code>에서 <code>user</code>가 null이어도 오류 없이 null 반환됨.</li>
</ul>
<hr />
<h3 id="✅-4-c">✅ <strong>4. C#</strong></h3>
<p>C# 6.0 이후부터 <code>?.</code> 문법으로 옵셔널 체이닝을 지원합니다.</p>
<pre><code class="language-csharp">class Person {
    public string Name { get; set; }
}

Person person = null;

// 옵셔널 체이닝 사용
string name = person?.Name;
Console.WriteLine(name);  // null 출력, 에러 아님</code></pre>
<hr />
<h1 id="옵셔널을-언래핑-하는-방법">옵셔널을 언래핑 하는 방법</h1>
<h2 id="시험에-나옴">시험에 나옴</h2>
<hr />
<pre><code class="language-swift">var x : String? = &quot;Hi&quot; // 옵셔널 문자열 x 선언
print(x, x!)</code></pre>
<p>✅ 출력 (x = &quot;Hi&quot;일 때):</p>
<pre><code>Optional(&quot;Hi&quot;) Hi</code></pre><ul>
<li><code>x</code>는 옵셔널이므로 <code>Optional(&quot;Hi&quot;)</code>로 출력됨  </li>
<li><code>x!</code>는 강제 언래핑 — <code>x</code>가 <code>nil</code>이면 <strong>런타임 에러 발생</strong></li>
<li>❗️&quot;Hi&quot;를 지우면(<code>x = nil</code>) → <code>x!</code>에서 <strong>crash 발생</strong></li>
</ul>
<hr />
<pre><code class="language-swift">if let a = x {
    print(a)
}</code></pre>
<p>✅ 옵셔널 바인딩 (안전하게 꺼냄)</p>
<ul>
<li><code>x</code>가 <code>nil</code>이 아니면 <code>a</code>에 값이 들어가고 출력됨</li>
<li>&quot;Hi&quot;일 때: <code>Hi</code> 출력  </li>
<li><code>nil</code>일 때: 아무 것도 출력되지 않음 (안전함)</li>
</ul>
<hr />
<pre><code class="language-swift">let b = x!.count
print(type(of:b), b)</code></pre>
<p>✅ 옵셔널 강제 언래핑 후 count 사용</p>
<ul>
<li><code>x!</code> → <code>&quot;Hi&quot;</code>가 되면 <code>&quot;Hi&quot;.count</code> → 2  </li>
<li><code>type(of:b)</code>는 <code>Int</code></li>
</ul>
<p>결과:</p>
<pre><code>Int 2</code></pre><p>❗️하지만 <code>x = nil</code>일 경우, <code>x!</code>에서 <strong>강제 언래핑 crash 발생</strong></p>
<hr />
<pre><code class="language-swift">let b1 = x?.count
print(type(of:b1), b1, b1!)</code></pre>
<p>✅ 옵셔널 체이닝 사용</p>
<ul>
<li><code>x</code>가 <code>nil</code>이 아니면 <code>.count</code> 실행 → <code>Optional(2)</code></li>
<li><code>x</code>가 <code>nil</code>이면 <code>b1 = nil</code></li>
</ul>
<p>출력:</p>
<pre><code>Optional&lt;Int&gt; Optional(2) 2</code></pre><p>❗️하지만 <code>b1!</code>은 <code>b1 == nil</code>일 경우 <strong>강제 언래핑 crash 발생</strong></p>
<hr />
<pre><code class="language-swift">let c = x ?? &quot;&quot;
print(c)</code></pre>
<p>✅ nil 병합 연산자 (<code>??</code>)</p>
<ul>
<li><code>x</code>가 nil이면 <code>&quot;&quot;</code> (빈 문자열) 사용</li>
<li><code>x = &quot;Hi&quot;</code>면 <code>&quot;Hi&quot;</code> 출력  </li>
<li><code>x = nil</code>이면 <code>&quot;&quot;</code> 출력됨 → crash 없음</li>
</ul>
<hr />
<h3 id="🔁-정리-hi-제거-시-결과">🔁 정리 (Hi 제거 시 결과)</h3>
<table>
<thead>
<tr>
<th>코드</th>
<th>Hi 있을 때</th>
<th>Hi 없을 때 (<code>x = nil</code>)</th>
</tr>
</thead>
<tbody><tr>
<td><code>print(x, x!)</code></td>
<td>Optional(&quot;Hi&quot;) Hi</td>
<td>❌ <code>x!</code> → crash</td>
</tr>
<tr>
<td><code>if let a = x { print(a) }</code></td>
<td>Hi</td>
<td>아무 출력 없음 (안전함)</td>
</tr>
<tr>
<td><code>let b = x!.count</code></td>
<td>Int 2</td>
<td>❌ <code>x!</code> → crash</td>
</tr>
<tr>
<td><code>let b1 = x?.count</code></td>
<td>Optional(2)</td>
<td>Optional(nil), ❌ <code>b1!</code> crash</td>
</tr>
<tr>
<td><code>let c = x ?? &quot;&quot;</code></td>
<td>Hi</td>
<td>빈 문자열 출력 (안전함)</td>
</tr>
</tbody></table>
<hr />
<h1 id="swift에서--와--가-선언문일때와-실행문일떄-어떻게-다른지-표로-정리해줘">swift에서 ! 와 ? 가 선언문일때와 실행문일떄 어떻게 다른지 표로 정리해줘</h1>
<p>Swift에서 <code>!</code>(강제 언래핑)과 <code>?</code>(옵셔널) 연산자는 <strong>선언문</strong>과 <strong>실행문</strong>에서 사용될 때 의미가 다릅니다. 아래 표는 이 둘의 사용을 <strong>선언문</strong>과 <strong>실행문</strong>으로 나누어 간단하고 명확하게 정리한 것입니다:</p>
<hr />
<h3 id="✅-와-의-선언문-vs-실행문-비교표">✅ <code>!</code>와 <code>?</code>의 선언문 vs 실행문 비교표</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th><code>?</code> (옵셔널)</th>
<th><code>!</code> (암시적 언래핑 또는 강제 언래핑)</th>
</tr>
</thead>
<tbody><tr>
<td><strong>선언문</strong></td>
<td>변수나 상수가 <code>nil</code>을 가질 수 있도록 함</td>
<td>변수는 <code>nil</code> 가능하지만 사용할 때 자동으로 언래핑됨</td>
</tr>
<tr>
<td></td>
<td><code>var name: String?</code> → Optional String</td>
<td><code>var name: String!</code> → Implicitly Unwrapped Optional</td>
</tr>
<tr>
<td><strong>실행문</strong></td>
<td>옵셔널 체이닝 또는 안전한 접근 (<code>x?.count</code>)</td>
<td>강제 언래핑 → 값이 반드시 있다고 가정하고 사용 (<code>x!</code>)</td>
</tr>
<tr>
<td></td>
<td>값이 <code>nil</code>이면 무시되거나 <code>nil</code> 반환</td>
<td>값이 <code>nil</code>이면 런타임 crash 발생</td>
</tr>
</tbody></table>
<hr />
<h3 id="🔎-예시로-비교">🔎 예시로 비교</h3>
<pre><code class="language-swift">// 선언문
var a: String? = &quot;Hi&quot;   // a는 Optional(String)
var b: String! = &quot;Hi&quot;   // b는 암시적 언래핑 Optional(String)

// 실행문
let len1 = a?.count     // 옵셔널 체이닝: len1은 Int? (a가 nil이면 nil)
let len2 = b.count      // 자동 언래핑: b가 nil이면 crash

let force = a!          // 강제 언래핑: a가 nil이면 crash</code></pre>
<hr />
<h3 id="✅-요약">✅ 요약</h3>
<table>
<thead>
<tr>
<th>사용 위치</th>
<th><code>?</code> 의미</th>
<th><code>!</code> 의미</th>
</tr>
</thead>
<tbody><tr>
<td>선언문</td>
<td>Optional 타입</td>
<td>Implicitly Unwrapped Optional 타입</td>
</tr>
<tr>
<td>실행문</td>
<td>옵셔널 체이닝, nil 가능성 고려한 접근</td>
<td>강제 언래핑, nil이면 crash 발생</td>
</tr>
</tbody></table>
<hr />
<h1 id="var-x--int--var-x--int-차이점">var x : Int! , var x : Int? 차이점</h1>
<p>좋아요! Swift에서 아래 두 선언은 <strong>비슷해 보이지만 분명한 차이</strong>가 있어요. 하나씩 분석해보면서 <strong>공통점과 차이점</strong>을 명확히 알려드릴게요.</p>
<hr />
<h3 id="🔹-선언문-비교">🔹 선언문 비교</h3>
<pre><code class="language-swift">var x: Int!   // 암시적 언래핑 옵셔널 (Implicitly Unwrapped Optional)
var x: Int?   // 일반 옵셔널 (Optional)</code></pre>
<hr />
<h3 id="✅-공통점">✅ 공통점</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>타입</td>
<td>둘 다 <code>Optional</code> 타입 (즉, <code>nil</code>을 저장할 수 있음)</td>
</tr>
<tr>
<td>저장 가능한 값</td>
<td><code>Int</code> 값 또는 <code>nil</code></td>
</tr>
<tr>
<td>사용 목적</td>
<td>값이 나중에 할당될 수 있고, 현재는 <code>nil</code>일 수 있음을 나타냄</td>
</tr>
</tbody></table>
<hr />
<h3 id="❗️차이점">❗️차이점</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th><code>Int?</code> (Optional)</th>
<th><code>Int!</code> (Implicitly Unwrapped Optional)</th>
</tr>
</thead>
<tbody><tr>
<td>선언 의미</td>
<td>옵셔널 타입 → 값이 있을 수도, 없을 수도 있음</td>
<td>옵셔널인데 사용할 때는 <strong>자동으로 언래핑됨</strong></td>
</tr>
<tr>
<td>사용 시 접근</td>
<td><code>x</code> → Optional(Int), <code>x!</code>로 강제 언래핑 필요</td>
<td><code>x</code> → 자동으로 언래핑되어 Int처럼 사용 가능</td>
</tr>
<tr>
<td>안전성</td>
<td>안전함 (명시적으로 언래핑해야 함)</td>
<td>위험함 (<code>nil</code>일 때 접근하면 런타임 crash 발생)</td>
</tr>
<tr>
<td>사용 목적</td>
<td>옵셔널 바인딩 등으로 <strong>nil 확인 후 사용</strong></td>
<td><strong>초기화는 나중에 하지만, nil 아님을 확신할 때</strong> 사용</td>
</tr>
</tbody></table>
<hr />
<h3 id="🔎-예제-비교">🔎 예제 비교</h3>
<pre><code class="language-swift">var a: Int? = 5
var b: Int! = 5

print(a)       // Optional(5)
print(a!)      // 5

print(b)       // 5 ← 자동으로 언래핑됨
print(b + 1)   // 6 ← b가 Int처럼 바로 사용됨

a = nil
b = nil
print(a ?? 0)  // 0
print(b)       // ❌ 런타임 crash 발생!</code></pre>
<hr />
<h3 id="✅-요약-표">✅ 요약 표</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th><code>Int?</code></th>
<th><code>Int!</code></th>
</tr>
</thead>
<tbody><tr>
<td>타입 이름</td>
<td>Optional</td>
<td>Implicitly Unwrapped Optional</td>
</tr>
<tr>
<td>nil 저장 가능</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>사용 시 언래핑</td>
<td>필요 (<code>x!</code> 또는 옵셔널 바인딩 등)</td>
<td>자동 언래핑됨 (<code>x</code>만으로도 접근)</td>
</tr>
<tr>
<td>nil 접근 시</td>
<td>안전 (옵셔널로 유지됨)</td>
<td>❌ 런타임 crash 위험 있음</td>
</tr>
<tr>
<td>주 사용 상황</td>
<td>값이 없어도 됨, 안전성 우선</td>
<td>값이 나중에 설정되나 절대 nil 아님을 확신할 때 사용</td>
</tr>
</tbody></table>
<hr />
<h1 id="실행문에서-차이점">실행문에서 차이점</h1>
<p>  좋아요! Swift에서 실행문에서 <code>!</code>와 <code>?</code>는 <strong>옵셔널 값에 접근하는 방식</strong>에서 매우 중요한 차이를 가지고 있어요. 아래 예제를 통해 <code>!</code>와 <code>?</code>의 차이를 <strong>쉽게 비교</strong>해볼게요.</p>
<hr />
<h2 id="✅-실행문에서--와--차이-예제">✅ 실행문에서 <code>?</code> 와 <code>!</code> 차이 예제</h2>
<pre><code class="language-swift">var name: String? = &quot;경윤&quot;</code></pre>
<h3 id="1--강제-언래핑">1. <code>!</code> (강제 언래핑)</h3>
<pre><code class="language-swift">print(name!)  // 출력: &quot;경윤&quot;</code></pre>
<ul>
<li><code>name</code>이 <strong>절대 nil이 아님을 확신</strong>할 때 사용</li>
<li>❗️만약 <code>name = nil</code>이면 <strong>런타임 에러(Crash)</strong> 발생</li>
</ul>
<pre><code class="language-swift">name = nil
print(name!)  // ❌ Fatal error: Unexpectedly found nil while unwrapping an Optional value</code></pre>
<hr />
<h3 id="2--옵셔널-체이닝">2. <code>?</code> (옵셔널 체이닝)</h3>
<pre><code class="language-swift">print(name?.count)  // 출력: Optional(2)</code></pre>
<ul>
<li><code>name</code>이 <code>nil</code>이면 <code>nil</code>을 반환하고 에러 없이 넘어감</li>
<li>안전하게 옵셔널 값을 접근하는 방법</li>
<li>반환 타입은 <code>Optional&lt;Int&gt;</code> (즉, <code>Int?</code>)</li>
</ul>
<pre><code class="language-swift">name = nil
print(name?.count)  // 출력: nil (Crash 안남!)</code></pre>
<hr />
<h2 id="✅-차이-요약-표">✅ 차이 요약 표</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th><code>?</code> (옵셔널 체이닝)</th>
<th><code>!</code> (강제 언래핑)</th>
</tr>
</thead>
<tbody><tr>
<td>동작 방식</td>
<td>값이 있으면 접근, 없으면 <code>nil</code> 반환</td>
<td>값이 있다고 가정하고 바로 접근</td>
</tr>
<tr>
<td>안전성</td>
<td>매우 안전함 (<code>nil</code>이어도 crash 안남)</td>
<td>❗️ <code>nil</code>이면 런타임 에러 발생</td>
</tr>
<tr>
<td>반환 타입</td>
<td>옵셔널 타입 (<code>Int?</code>, <code>String?</code>, ...)</td>
<td>언래핑된 일반 타입 (<code>Int</code>, <code>String</code>, ...)</td>
</tr>
<tr>
<td>대표 예제</td>
<td><code>name?.count</code>, <code>user?.email</code></td>
<td><code>name!.count</code>, <code>user!.email</code></td>
</tr>
<tr>
<td>사용 시점</td>
<td>값이 있을 수도 없을 수도 있을 때</td>
<td>값이 반드시 있다고 확신할 때만!</td>
</tr>
</tbody></table>
<hr />
<h2 id="✨-보너스-if-let과-함께-쓰면-더-안전해요">✨ 보너스: if let과 함께 쓰면 더 안전해요</h2>
<pre><code class="language-swift">if let realName = name {
    print(realName.count) // 안전하게 강제 언래핑 없이 사용 가능
}</code></pre>
<hr />
<h2 id="옵셔널-체이닝">옵셔널 체이닝</h2>
<p>  물론이죠! 아래는 질문해주신 Swift 코드에 <strong>한 줄씩 상세한 주석</strong>을 달아 해설한 버전입니다.</p>
<hr />
<pre><code class="language-swift">// Person 클래스 선언
class Person {
    var name: String         // 이름 속성 (String 타입, 옵셔널 아님)
    var age: Int            // 나이 속성 (Int 타입, 옵셔널 아님)

    // 이니셜라이저(생성자) 정의
    init(name: String, age: Int) {
        self.name = name    // 매개변수 name을 클래스의 name에 할당
        self.age = age      // 매개변수 age를 클래스의 age에 할당
    }
}

// Person 인스턴스 'kim' 생성, name = &quot;Kim&quot;, age = 20
let kim: Person = Person(name: &quot;Kim&quot;, age: 20)

// kim.age는 일반 Int 타입이므로 그대로 출력됨
print(kim.age)              // 출력: 20

// 옵셔널 타입의 Person 인스턴스 'han' 생성
let han: Person? = Person(name: &quot;Han&quot;, age: 25)

// 옵셔널 체이닝으로 han의 age 속성에 접근
// han이 nil이 아니면 age를 반환하고, nil이면 nil 반환
print(han?.age)             // 출력: Optional(25)

// 아래 코드는 오류 아님, 주석 때문에 오해할 수 있음
// 강제 언래핑: han이 nil이 아님을 확신할 때만 사용해야 함
//print(han!.age)            // 출력: 25 (단, han이 nil이면 crash)

// 옵셔널 체이닝 후 강제 언래핑
// han?.age는 Optional(25)이므로, 그걸 다시 강제 언래핑함
print((han?.age)!)          // 출력: 25 (단, han이 nil이면 crash)

// 안전한 옵셔널 바인딩: han이 nil이 아니고 age가 있으면 출력
if let hanAge = han?.age {
    print(hanAge)           // 출력: 25
} else {
    print(&quot;nil&quot;)            // han 또는 age가 nil일 때 실행
}</code></pre>
<hr />
<h3 id="✅-핵심-요약">✅ 핵심 요약</h3>
<table>
<thead>
<tr>
<th>표현식</th>
<th>의미</th>
<th>안전성</th>
</tr>
</thead>
<tbody><tr>
<td><code>han?.age</code></td>
<td>옵셔널 체이닝 (nil일 경우 nil 반환)</td>
<td>✅ 안전</td>
</tr>
<tr>
<td><code>han!.age</code></td>
<td>강제 언래핑 (nil일 경우 crash 발생)</td>
<td>❗️ 위험</td>
</tr>
<tr>
<td><code>(han?.age)!</code></td>
<td>체이닝 후 강제 언래핑 (값이 없으면 crash)</td>
<td>❗️ 위험</td>
</tr>
<tr>
<td><code>if let ...</code></td>
<td>옵셔널 바인딩 (안전하게 값이 있을 때만 사용)</td>
<td>✅ 안전</td>
</tr>
</tbody></table>
<hr />
<h1 id="swift-오류-제어">Swift 오류 제어</h1>
<h2 id="✅-swift-오류-제어-요약표">✅ Swift 오류 제어 요약표</h2>
<table>
<thead>
<tr>
<th>방식</th>
<th>키워드</th>
<th>특징 및 사용 상황</th>
<th>예제 코드</th>
</tr>
</thead>
<tbody><tr>
<td><strong>1. do-catch</strong></td>
<td><code>do { try ... } catch {}</code></td>
<td>명시적으로 오류를 처리하고, 다양한 오류 유형을 분기하여 다룰 수 있음</td>
<td>✅ 안정적</td>
</tr>
<tr>
<td><strong>2. 옵셔널 변환</strong></td>
<td><code>try?</code></td>
<td>실패해도 오류를 발생시키지 않고 <code>nil</code> 반환</td>
<td>⚠️ 단순 실패 확인</td>
</tr>
<tr>
<td><strong>3. 에러 전파</strong></td>
<td><code>throws</code></td>
<td>함수에서 에러를 던지고 호출자가 처리하도록 위임</td>
<td>🚀 네트워크, 복잡한 처리에 적합</td>
</tr>
<tr>
<td><strong>4. 단정적 처리</strong></td>
<td><code>try!</code></td>
<td>에러가 절대 없다고 확신할 때 사용. 실패 시 crash</td>
<td>❗️위험, 최소 사용</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-각-방식별-예제">✅ 각 방식별 예제</h2>
<h3 id="1-do-catch--일반적인-에러-처리">1. <code>do-catch</code> – 일반적인 에러 처리</h3>
<pre><code class="language-swift">enum FileError: Error {
    case notFound
}

func readFile(name: String) throws {
    throw FileError.notFound
}

do {
    try readFile(name: &quot;data.txt&quot;)
} catch FileError.notFound {
    print(&quot;파일을 찾을 수 없습니다.&quot;)
} catch {
    print(&quot;알 수 없는 오류 발생: \(error)&quot;)
}</code></pre>
<hr />
<h3 id="2-try--옵셔널로-에러-처리">2. <code>try?</code> – 옵셔널로 에러 처리</h3>
<pre><code class="language-swift">func loadData() throws -&gt; String {
    throw NSError(domain: &quot;&quot;, code: 1)
}

let result = try? loadData()  // 실패 시 nil 반환
print(result)  // Optional(nil)</code></pre>
<hr />
<h3 id="3-throws--에러-전파">3. <code>throws</code> – 에러 전파</h3>
<pre><code class="language-swift">func fetchData() throws -&gt; String {
    throw NSError(domain: &quot;Server&quot;, code: 500)
}

func handleRequest() {
    do {
        let data = try fetchData()
        print(data)
    } catch {
        print(&quot;데이터를 불러오는 중 오류 발생&quot;)
    }
}</code></pre>
<hr />
<h3 id="4-try--단정적-처리">4. <code>try!</code> – 단정적 처리</h3>
<pre><code class="language-swift">func alwaysSuccess() throws -&gt; String {
    return &quot;성공&quot;
}

let data = try! alwaysSuccess()  // 반드시 성공한다고 확신할 때
print(data)  // &quot;성공&quot;</code></pre>
<p>❗️주의: <code>try!</code>는 실제 에러가 나면 앱이 crash 됩니다.</p>
<hr />
<h2 id="dotrycatch">do<del>try</del>catch</h2>
<h2 id="✅-기본-구조">✅ 기본 구조</h2>
<pre><code class="language-swift">do {
    try 오류를_던질_수_있는_함수()
    // 성공했을 때 실행할 코드
} catch 오류_종류1 {
    // 오류 종류1일 때 처리할 코드
} catch 오류_종류2 {
    // 오류 종류2일 때 처리할 코드
} catch {
    // 그 외 모든 오류
}</code></pre>
<hr />
<h2 id="✅-예제와-함께-보기">✅ 예제와 함께 보기</h2>
<pre><code class="language-swift">enum FileError: Error {
    case fileNotFound
    case unreadable
}

func readFile(name: String) throws -&gt; String {
    if name == &quot;none.txt&quot; {
        throw FileError.fileNotFound
    }
    return &quot;파일 내용입니다&quot;
}

// 오류 처리
do {
    let content = try readFile(name: &quot;none.txt&quot;)
    print(content)
} catch FileError.fileNotFound {
    print(&quot;❌ 파일이 없습니다.&quot;)
} catch {
    print(&quot;❗️기타 오류 발생: \(error)&quot;)
}</code></pre>
<h3 id="🔍-결과">🔍 결과:</h3>
<pre><code>❌ 파일이 없습니다.</code></pre><hr />
<h2 id="✅-핵심-키워드-설명">✅ 핵심 키워드 설명</h2>
<table>
<thead>
<tr>
<th>키워드</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>do</code></td>
<td>오류 발생 가능 코드 블록을 시작함</td>
</tr>
<tr>
<td><code>try</code></td>
<td>오류 발생 가능 함수 앞에 붙여야 함</td>
</tr>
<tr>
<td><code>catch</code></td>
<td>오류를 잡아 처리하는 블록</td>
</tr>
<tr>
<td><code>catch let error</code></td>
<td>발생한 오류를 변수로 받아서 출력하거나 분석 가능</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-왜-써야-할까">✅ 왜 써야 할까?</h2>
<ul>
<li>오류 발생 시 앱이 <strong>바로 죽지 않게</strong> 하려고 (안정성 ↑)</li>
<li>실패했을 때 <strong>대체 로직 제공</strong> 가능</li>
<li><code>do-try-catch</code>는 <strong>가장 명시적</strong>이고, 복잡한 에러 처리 시 좋음</li>
</ul>
<hr />
<h2 id="✅-간단-버전도-있어요">✅ 간단 버전도 있어요</h2>
<table>
<thead>
<tr>
<th>구문</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>try?</code></td>
<td>실패 시 <code>nil</code> 반환</td>
</tr>
<tr>
<td><code>try!</code></td>
<td>실패 시 앱 크래시</td>
</tr>
</tbody></table>
<p>예시:</p>
<pre><code class="language-swift">let result = try? readFile(name: &quot;none.txt&quot;)  // Optional(nil)
let result = try! readFile(name: &quot;file.txt&quot;)  // 파일이 있으면 OK, 없으면 crash</code></pre>
<hr />
<h1 id="generic">Generic</h1>
<p>  물론이죠! 아래는 제시해주신 Swift 코드에 <strong>한 줄씩 상세한 주석을 추가한 설명</strong>입니다. 특히 <strong>제네릭(Generic)</strong> 사용과 비교를 쉽게 이해할 수 있도록 구성했어요.</p>
<hr />
<pre><code class="language-swift">// 제네릭(Generic)을 사용하는 함수 선언
// &lt;T&gt;는 타입 파라미터로, 어떤 타입이든 받아들일 수 있음
func myPrint &lt;T&gt; (a: T, b: T) {
    print(b, a)  // 두 값을 순서 바꿔 출력 (b 먼저, a 나중)
}</code></pre>
<blockquote>
<p>🔍 <code>T</code>는 임의의 타입을 나타내며, 호출 시 전달되는 값의 타입에 따라 자동으로 결정됩니다.<br />같은 타입이어야만 함 (<code>a</code>와 <code>b</code>는 둘 다 <code>T</code>이어야 함).</p>
</blockquote>
<hr />
<pre><code class="language-swift">// 아래는 제네릭이 아닌 오버로딩을 위한 함수 예시 (현재는 주석 처리됨)
//func myPrint(a: Double, b: Double) {
//    print(b, a)
//}</code></pre>
<blockquote>
<p>이 함수는 <strong>Double 전용</strong>이기 때문에 다른 타입(String, Int 등)에는 사용할 수 없음.<br />제네릭을 쓰면 굳이 이런 식으로 타입마다 함수를 따로 만들 필요 없음.</p>
</blockquote>
<hr />
<pre><code class="language-swift">// 제네릭 함수 호출 - Int 타입
myPrint(a: 1, b: 2)           // 출력: 2 1</code></pre>
<ul>
<li><code>T == Int</code>로 추론됨</li>
</ul>
<hr />
<pre><code class="language-swift">// 제네릭 함수 호출 - Double 타입
myPrint(a: 2.5, b: 3.5)       // 출력: 3.5 2.5</code></pre>
<ul>
<li><code>T == Double</code>로 추론됨</li>
</ul>
<hr />
<pre><code class="language-swift">// 제네릭 함수 호출 - String 타입
myPrint(a: &quot;Hi&quot;, b: &quot;Hello&quot;)  // 출력: Hello Hi</code></pre>
<ul>
<li><code>T == String</code>으로 추론됨</li>
</ul>
<hr />
<h2 id="✅-요약-정리">✅ 요약 정리</h2>
<table>
<thead>
<tr>
<th>항목</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>func myPrint&lt;T&gt;(a: T, b: T)</code></td>
<td>어떤 타입이든 받을 수 있는 <strong>제네릭 함수</strong></td>
</tr>
<tr>
<td><code>T</code></td>
<td>타입 파라미터, 호출 시 전달된 값의 타입으로 자동 결정</td>
</tr>
<tr>
<td>코드 활용도</td>
<td>Int, Double, String 등 다양한 타입에서 재사용 가능</td>
</tr>
<tr>
<td>장점</td>
<td>코드 <strong>재사용성</strong>, <strong>유연성</strong> 증가</td>
</tr>
<tr>
<td>단점</td>
<td>타입이 달라지면 따로 처리해줘야 함 (예: <code>a: Int</code>, <code>b: Double</code>은 불가)</td>
</tr>
</tbody></table>
<hr />
<h1 id="array">Array</h1>
<p>  좋아요! 아래는 주신 코드에 대해 <strong>한 줄씩 설명을 덧붙인 버전</strong>입니다. Swift에서 배열을 선언하는 여러 방법을 잘 보여주는 예제예요.</p>
<hr />
<pre><code class="language-swift">// 1. 정수형 배열 number를 빈 배열로 선언 (대괄호 사용)
var number : [Int] = []</code></pre>
<ul>
<li><code>number</code>는 <code>Int</code> 타입의 배열</li>
<li>현재 아무 값도 없기 때문에 <code>[]</code> (빈 배열)</li>
</ul>
<hr />
<pre><code class="language-swift">// 2. odd 배열 선언, 타입 추론을 사용하여 빈 정수 배열 생성
var odd = [Int]()</code></pre>
<ul>
<li>타입 명시 없이 <code>Int</code> 배열로 초기화</li>
<li>Swift가 <code>odd</code>가 <code>[Int]</code> 타입임을 자동으로 추론</li>
</ul>
<hr />
<pre><code class="language-swift">// 3. even 배열 선언, `Array&lt;Int&gt;` 형태로 생성자 사용
var even : Array&lt;Int&gt; = Array()</code></pre>
<ul>
<li><code>Array&lt;Int&gt;</code>는 <code>[Int]</code>와 동일한 타입</li>
<li>생성자 방식으로 빈 배열 생성</li>
</ul>
<hr />
<pre><code class="language-swift">print(number) // 출력: []</code></pre>
<ul>
<li>빈 배열이므로 출력 결과는 <code>[]</code></li>
</ul>
<hr />
<h3 id="✅-요약-배열-선언-방법-3가지">✅ 요약: 배열 선언 방법 3가지</h3>
<table>
<thead>
<tr>
<th>선언 방식</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>var arr: [Int] = []</code></td>
<td>가장 일반적인 형태</td>
</tr>
<tr>
<td><code>var arr = [Int]()</code></td>
<td>타입 추론 사용, 간결함</td>
</tr>
<tr>
<td><code>var arr: Array&lt;Int&gt; = Array()</code></td>
<td>명시적으로 Array 타입 선언</td>
</tr>
</tbody></table>
<hr />
<h1 id="swift의-배열은-genric-구조체">Swift의 배열은 Genric 구조체</h1>
<p>  네, 정확합니다! Swift의 배열은 사실상 <strong>제네릭(Generic) 구조체</strong>인 <code>Array&lt;Element&gt;</code>로 정의되어 있으며, 이 구조와 관련된 개념들을 아래와 같이 설명드릴게요.</p>
<hr />
<h2 id="✅-swift-배열은-제네릭-구조체이다">✅ Swift 배열은 제네릭 구조체이다</h2>
<h3 id="📌-배열-선언-예시">📌 배열 선언 예시</h3>
<pre><code class="language-swift">var x: [Int] = []                     // 방법 1: 대괄호 문법
var y = [Int]()                       // 방법 2: 타입 추론
var z: Array&lt;Int&gt; = []               // 방법 3: 제네릭 타입 명시
var a: [Int] = [1,2,3,4]             // 초기값 포함 배열
var b: Array&lt;Int&gt; = [1,2,3,4]        // 위와 동일한 의미
var c: Array&lt;Double&gt; = [1.2, 2.3, 3.5, 4.1]  // Double 배열</code></pre>
<ul>
<li><code>Array&lt;Element&gt;</code>는 <code>[Element]</code>와 동일한 타입입니다.</li>
<li><code>Element</code>는 배열에 저장되는 <strong>요소 타입(Generic Type)</strong>입니다.</li>
</ul>
<hr />
<h2 id="✅-구조체-정의-방식">✅ 구조체 정의 방식</h2>
<pre><code class="language-swift">@frozen struct Array&lt;Element&gt; : ...</code></pre>
<h3 id="🔹-frozen-이란">🔹 <code>@frozen</code> 이란?</h3>
<ul>
<li>Swift 5 이후 등장한 <strong>속성 어노테이션</strong></li>
<li>이 구조체는 <strong>추가적인 저장 프로퍼티가 생기지 않을 것</strong>이라는 약속</li>
<li>이유: 컴파일러와 ABI 안정성 확보를 위해 미리 메모리 구조를 고정시키는 역할</li>
</ul>
<blockquote>
<p>✅ 쉽게 말하면:<br />컴파일러에게 “이 구조는 <strong>앞으로 변경되지 않을 거야</strong>”라고 말해주는 것<br />→ 성능 최적화 + ABI 안정성 유지 가능</p>
</blockquote>
<hr />
<h2 id="✅-제네릭-구조체란">✅ 제네릭 구조체란?</h2>
<pre><code class="language-swift">struct Box&lt;T&gt; {
    var value: T
}</code></pre>
<ul>
<li>위와 같이 타입 파라미터 <code>T</code>를 사용하는 구조체를 <strong>제네릭 구조체</strong>라고 하며, <code>Array&lt;Element&gt;</code>도 이런 방식으로 구현되어 있습니다.</li>
<li>Swift의 표준 라이브러리에는 <code>Array</code>, <code>Dictionary</code>, <code>Set</code> 등 많은 제네릭 타입이 존재합니다.</li>
</ul>
<hr />
<h2 id="✅-요약-정리-1">✅ 요약 정리</h2>
<table>
<thead>
<tr>
<th>내용</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>배열 타입</td>
<td><code>Array&lt;Element&gt;</code> 또는 <code>[Element]</code></td>
</tr>
<tr>
<td>저장 요소 타입</td>
<td><code>Element</code> (예: Int, String 등)</td>
</tr>
<tr>
<td><code>@frozen</code> 의미</td>
<td>구조체의 내부 구조가 고정됨 (성능 및 ABI 안정성 확보)</td>
</tr>
<tr>
<td>제네릭 구조체</td>
<td>타입에 유연하게 대응 가능 (<code>Array&lt;T&gt;</code>, <code>Box&lt;T&gt;</code> 등)</td>
</tr>
</tbody></table>
<hr />
<h1 id="프로그래밍-언어에서-콜렉션-타입">프로그래밍 언어에서 콜렉션 타입</h1>
<p>  물론이죠!  
프로그래밍 언어에서 <strong>콜렉션 타입(Collection Type)</strong>은 <strong>여러 개의 값을 하나의 그룹으로 저장하고 관리할 수 있게 해주는 데이터 타입</strong>입니다.<br />Swift를 포함한 대부분의 언어에서 제공되며, 대표적으로 <strong>배열(Array)</strong>, <strong>집합(Set)</strong>, <strong>사전(Dictionary/Map)</strong> 등이 있어요.</p>
<hr />
<h2 id="✅-콜렉션-타입이란">✅ 콜렉션 타입이란?</h2>
<blockquote>
<p>여러 값을 하나의 변수나 상수에 담아 <strong>반복</strong>, <strong>검색</strong>, <strong>정렬</strong> 등의 작업을 효율적으로 수행할 수 있도록 만든 데이터 구조</p>
</blockquote>
<hr />
<h2 id="✅-swift의-주요-콜렉션-타입-3가지">✅ Swift의 주요 콜렉션 타입 3가지</h2>
<table>
<thead>
<tr>
<th>타입</th>
<th>설명</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Array</strong></td>
<td>순서가 있는 데이터 모음, 인덱스로 접근 가능</td>
<td><code>[1, 2, 3]</code></td>
</tr>
<tr>
<td><strong>Set</strong></td>
<td>순서가 없고 중복이 없는 데이터 모음</td>
<td><code>Set([1, 2, 3])</code></td>
</tr>
<tr>
<td><strong>Dictionary</strong></td>
<td>키-값(key-value) 쌍으로 구성된 데이터</td>
<td><code>[&quot;name&quot;: &quot;경윤&quot;, &quot;age&quot;: 24]</code></td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-각-타입의-특징">✅ 각 타입의 특징</h2>
<h3 id="1-📦-array-배열">1. 📦 <strong>Array (배열)</strong></h3>
<ul>
<li>순서 있음 (인덱스로 접근 가능)</li>
<li>중복 허용</li>
<li>선언 예시:<pre><code class="language-swift">var numbers: [Int] = [1, 2, 3, 4]
print(numbers[0]) // 1</code></pre>
</li>
</ul>
<h3 id="2-🧮-set-집합">2. 🧮 <strong>Set (집합)</strong></h3>
<ul>
<li>순서 없음</li>
<li>중복 불가</li>
<li>빠른 검색에 유리</li>
<li>선언 예시:<pre><code class="language-swift">var fruits: Set&lt;String&gt; = [&quot;apple&quot;, &quot;banana&quot;, &quot;apple&quot;]
print(fruits) // [&quot;banana&quot;, &quot;apple&quot;]</code></pre>
</li>
</ul>
<h3 id="3-🔑-dictionary-사전">3. 🔑 <strong>Dictionary (사전)</strong></h3>
<ul>
<li>key-value 구조</li>
<li>key는 유일, value는 중복 가능</li>
<li>선언 예시:<pre><code class="language-swift">var student: [String: String] = [&quot;name&quot;: &quot;경윤&quot;, &quot;major&quot;: &quot;컴퓨터공학&quot;]
print(student[&quot;name&quot;]!) // &quot;경윤&quot;</code></pre>
</li>
</ul>
<hr />
<h2 id="✅-언제-콜렉션-타입을-써야-할까">✅ 언제 콜렉션 타입을 써야 할까?</h2>
<table>
<thead>
<tr>
<th>상황</th>
<th>적합한 타입</th>
</tr>
</thead>
<tbody><tr>
<td>순서가 중요할 때</td>
<td>Array</td>
</tr>
<tr>
<td>중복 없는 목록이 필요할 때</td>
<td>Set</td>
</tr>
<tr>
<td>키로 값을 저장하고 싶을 때</td>
<td>Dictionary</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-다른-언어와의-비교">✅ 다른 언어와의 비교</h2>
<table>
<thead>
<tr>
<th>언어</th>
<th>배열</th>
<th>집합(Set)</th>
<th>사전/딕셔너리</th>
</tr>
</thead>
<tbody><tr>
<td>Swift</td>
<td><code>Array</code></td>
<td><code>Set</code></td>
<td><code>Dictionary</code></td>
</tr>
<tr>
<td>Python</td>
<td><code>list</code></td>
<td><code>set</code></td>
<td><code>dict</code></td>
</tr>
<tr>
<td>Java</td>
<td><code>ArrayList</code></td>
<td><code>HashSet</code></td>
<td><code>HashMap</code></td>
</tr>
<tr>
<td>JavaScript</td>
<td><code>Array</code></td>
<td><code>Set</code></td>
<td><code>Object</code>, <code>Map</code></td>
</tr>
</tbody></table>
<hr />
<h1 id="swift-array-에서-많이-사용하는-프로퍼티와-메서드">swift Array 에서 많이 사용하는 프로퍼티와 메서드</h1>
<p>  좋은 질문이에요!  
Swift의 <code>Array</code>는 매우 자주 쓰이는 <strong>콜렉션 타입</strong>이며, 다양한 <strong>프로퍼티와 메서드</strong>를 제공합니다.<br />아래에 <strong>실무에서 자주 사용하는 프로퍼티와 메서드</strong>들을 설명과 함께 예제와 함께 정리해드릴게요.</p>
<hr />
<h2 id="✅-자주-사용하는-array-프로퍼티">✅ 자주 사용하는 <strong>Array 프로퍼티</strong></h2>
<table>
<thead>
<tr>
<th>프로퍼티</th>
<th>설명</th>
<th>예제 결과</th>
</tr>
</thead>
<tbody><tr>
<td><code>count</code></td>
<td>배열의 요소 개수 반환</td>
<td><code>[1, 2, 3].count → 3</code></td>
</tr>
<tr>
<td><code>isEmpty</code></td>
<td>배열이 비어 있는지 확인 (Bool)</td>
<td><code>[1, 2].isEmpty → false</code></td>
</tr>
<tr>
<td><code>first</code></td>
<td>첫 번째 요소 반환 (옵셔널)</td>
<td><code>[10, 20].first → Optional(10)</code></td>
</tr>
<tr>
<td><code>last</code></td>
<td>마지막 요소 반환 (옵셔널)</td>
<td><code>[10, 20].last → Optional(20)</code></td>
</tr>
<tr>
<td><code>min()</code></td>
<td>가장 작은 값 반환 (옵셔널)</td>
<td><code>[5, 1, 7].min() → Optional(1)</code></td>
</tr>
<tr>
<td><code>max()</code></td>
<td>가장 큰 값 반환 (옵셔널)</td>
<td><code>[5, 1, 7].max() → Optional(7)</code></td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-자주-사용하는-array-메서드">✅ 자주 사용하는 <strong>Array 메서드</strong></h2>
<table>
<thead>
<tr>
<th>메서드</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>append(_:)</code></td>
<td>배열 끝에 요소 추가</td>
</tr>
<tr>
<td><code>insert(_:at:)</code></td>
<td>특정 위치에 요소 삽입</td>
</tr>
<tr>
<td><code>remove(at:)</code></td>
<td>특정 인덱스 요소 제거</td>
</tr>
<tr>
<td><code>removeAll()</code></td>
<td>모든 요소 제거</td>
</tr>
<tr>
<td><code>contains(_:)</code></td>
<td>특정 요소 포함 여부 확인</td>
</tr>
<tr>
<td><code>sort()</code></td>
<td>배열 자체를 정렬 (in-place)</td>
</tr>
<tr>
<td><code>sorted()</code></td>
<td>정렬된 새로운 배열 반환</td>
</tr>
<tr>
<td><code>reverse()</code></td>
<td>배열 순서를 반전</td>
</tr>
<tr>
<td><code>map {}</code></td>
<td>각 요소를 변형하여 새 배열 생성</td>
</tr>
<tr>
<td><code>filter {}</code></td>
<td>조건에 맞는 요소만 추출</td>
</tr>
<tr>
<td><code>forEach {}</code></td>
<td>각 요소에 대해 작업 수행</td>
</tr>
<tr>
<td><code>reduce(_:_:){}</code></td>
<td>모든 요소를 하나의 값으로 축약</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-예시-코드">✅ 예시 코드</h2>
<pre><code class="language-swift">var nums = [1, 2, 3]

// append
nums.append(4)               // [1, 2, 3, 4]

// insert
nums.insert(0, at: 0)        // [0, 1, 2, 3, 4]

// remove
nums.remove(at: 2)           // [0, 1, 3, 4]

// contains
print(nums.contains(3))      // true

// sort (in-place)
nums.sort()                  // [0, 1, 3, 4]

// sorted (new array)
let sortedNums = nums.sorted(by: &gt;)  // [4, 3, 1, 0]

// map
let doubled = nums.map { $0 * 2 }    // [0, 2, 6, 8]

// filter
let even = nums.filter { $0 % 2 == 0 } // [0, 4]

// reduce
let total = nums.reduce(0) { $0 + $1 } // 8

// forEach
nums.forEach { print($0) }</code></pre>
<hr />
<h2 id="✅-요약-정리표">✅ 요약 정리표</h2>
<table>
<thead>
<tr>
<th>종류</th>
<th>이름 예시</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>프로퍼티</td>
<td><code>count</code>, <code>isEmpty</code>, <code>first</code>, <code>last</code></td>
<td>배열 정보 확인</td>
</tr>
<tr>
<td>변경 메서드</td>
<td><code>append</code>, <code>insert</code>, <code>remove</code></td>
<td>배열 내용 수정</td>
</tr>
<tr>
<td>반복/변형</td>
<td><code>map</code>, <code>filter</code>, <code>forEach</code></td>
<td>요소 반복/추출/변환</td>
</tr>
<tr>
<td>기타</td>
<td><code>sort</code>, <code>sorted</code>, <code>reduce</code></td>
<td>정렬, 합산 등 처리</td>
</tr>
</tbody></table>
<hr />
<h1 id="array-의-자료형">Array 의 자료형</h1>
<p>  아주 좋은 예제예요!  
아래는 작성하신 Swift 코드에 대해 <strong>한 줄씩 주석을 추가하고 설명한 버전</strong>입니다.<br /><strong>타입 추론</strong>, <strong>배열 타입 명시</strong>, 그리고 <code>type(of:)</code> 사용을 함께 익힐 수 있는 구조입니다.</p>
<hr />
<pre><code class="language-swift">// 타입 추론을 통해 number는 [Int]로 자동 결정됨
let number = [1, 2, 3, 4]  // [Int]

// 타입 명시 방식으로 홀수 배열 선언
let odd: [Int] = [1, 3, 5]

// Array 제네릭 문법을 사용한 짝수 배열 선언
let even: Array&lt;Int&gt; = [2, 4, 6]

// number의 타입을 출력
print(type(of: number))  // 출력: Array&lt;Int&gt;
print(number)            // 출력: [1, 2, 3, 4]

// odd의 타입을 출력
print(type(of: odd))     // 출력: Array&lt;Int&gt;
print(odd)               // 출력: [1, 3, 5]

// even의 타입을 출력
print(type(of: even))    // 출력: Array&lt;Int&gt;
print(even)              // 출력: [2, 4, 6]</code></pre>
<hr />
<pre><code class="language-swift">// 문자열 배열 animal 선언 (타입 생략 → 자동 추론: [String])
let animal = [&quot;dog&quot;, &quot;cat&quot;, &quot;cow&quot;]

// 타입 확인
print(type(of: animal))  // 출력: Array&lt;String&gt;
print(animal)            // 출력: [&quot;dog&quot;, &quot;cat&quot;, &quot;cow&quot;]</code></pre>
<hr />
<h2 id="✅-핵심-요약-1">✅ 핵심 요약</h2>
<table>
<thead>
<tr>
<th>선언 형태</th>
<th>의미</th>
</tr>
</thead>
<tbody><tr>
<td><code>let a = [1, 2]</code></td>
<td>타입 추론으로 <code>[Int]</code></td>
</tr>
<tr>
<td><code>let a: [Int] = [1, 2]</code></td>
<td>대괄호 문법으로 명시</td>
</tr>
<tr>
<td><code>let a: Array&lt;Int&gt; = [...]</code></td>
<td>제네릭 문법으로 명시</td>
</tr>
<tr>
<td><code>type(of: a)</code></td>
<td>a의 정확한 타입 확인</td>
</tr>
</tbody></table>
<hr />
<h1 id="빈-배열empty-array-개념과-주의사항">빈 배열(empty array) 개념과 주의사항</h1>
<p>아래는 주신 내용을 바탕으로 <strong>&quot;빈 배열(empty array)&quot; 개념과 주의사항</strong>을 보기 쉽게 <strong>설명 + 정리 + 예제 코드 주석</strong> 형태로 재구성한 자료입니다. 실습/강의자료로 사용하기에도 좋아요!</p>
<hr />
<h2 id="✅-빈-배열-empty-array">✅ 빈 배열 (Empty Array)</h2>
<pre><code class="language-swift">// 가변형(Mutable) 빈 배열 선언
var number: [Int] = []              // 방법 1: 타입 명시
var odd = [Int]()                   // 방법 2: 타입 추론
var even: Array&lt;Int&gt; = Array()      // 방법 3: 제네릭 타입 사용

print(number) // 출력: []</code></pre>
<hr />
<h2 id="⚠️-빈-배열-주의사항">⚠️ 빈 배열 주의사항</h2>
<pre><code class="language-swift">// 불변형(Immutable) 빈 배열 선언
let number: [Int] = []

print(number)        // 출력: []

// ❗️빈 배열에 인덱스로 접근하면 런타임 에러
print(number[0])     // ❌ 오류: Index out of range

// ❗️let으로 선언된 배열은 값 추가 불가
number.append(100)   // ❌ 오류: Cannot use mutating member on immutable value

// ❗️아래 코드들은 실행되지 않음 (모두 오류)
print(number[0])
number.append(200)
print(number[0], number[1], number)</code></pre>
<hr />
<h2 id="✅-가변형mutable-vs-불변형immutable">✅ 가변형(Mutable) vs 불변형(Immutable)</h2>
<table>
<thead>
<tr>
<th>선언 형태</th>
<th>설명</th>
<th>가능 작업</th>
</tr>
</thead>
<tbody><tr>
<td><code>var animal = [&quot;dog&quot;, &quot;cat&quot;]</code></td>
<td>가변 배열 – 나중에 수정 가능</td>
<td>✅ 추가/삭제/수정 가능</td>
</tr>
<tr>
<td><code>let animal1 = [&quot;dog&quot;, &quot;cat&quot;]</code></td>
<td>불변 배열 – 내용 수정 불가능</td>
<td>❌ append 등 불가</td>
</tr>
</tbody></table>
<hr />
<h2 id="🔑-핵심-요약">🔑 핵심 요약</h2>
<ul>
<li><code>var</code> → 가변 배열 (값 추가/삭제 가능)</li>
<li><code>let</code> → 불변 배열 (초기값 이후 변경 불가)</li>
<li>빈 배열 선언 후 값을 넣지 않고 인덱스로 접근하면 <strong>런타임 에러 발생</strong></li>
<li>배열은 <strong>항상 값이 있는지 확인하고 접근</strong>하는 습관 필요<br />(예: <code>isEmpty</code>, <code>count</code>, <code>optional binding</code>)</li>
</ul>
<hr />
<h2 id="✅-안전한-배열-접근-예시">✅ 안전한 배열 접근 예시</h2>
<pre><code class="language-swift">if !number.isEmpty {
    print(number[0])
} else {
    print(&quot;배열이 비어있습니다.&quot;)
}</code></pre>
<p>또는</p>
<pre><code class="language-swift">if let first = number.first {
    print(first)
} else {
    print(&quot;배열이 비어있습니다.&quot;)
}</code></pre>
<hr />
<h1 id="forin으로-배열-항목-접근">for~in으로 배열 항목 접근</h1>
<pre><code class="language-swift">// 문자열 요소를 가진 배열 선언
let colors = [&quot;red&quot;, &quot;green&quot;, &quot;blue&quot;]

// 배열 전체 출력
print(colors)  
// 출력: [&quot;red&quot;, &quot;green&quot;, &quot;blue&quot;]

// for-in 반복문을 사용하여 배열의 각 요소에 접근
for color in colors {
    print(color)
}
// 출력 결과:
// red
// green
// blue</code></pre>
<hr />
<h2 id="✅-핵심-설명">✅ 핵심 설명</h2>
<table>
<thead>
<tr>
<th>문법 요소</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>for color in colors</code></td>
<td><code>colors</code> 배열의 각 요소를 하나씩 꺼내어 <code>color</code>에 저장하면서 반복</td>
</tr>
<tr>
<td><code>print(color)</code></td>
<td>현재 반복 중인 요소 출력</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-인덱스와-함께-접근하고-싶다면">✅ 인덱스와 함께 접근하고 싶다면?</h2>
<pre><code class="language-swift">for (index, color) in colors.enumerated() {
    print(&quot;\(index): \(color)&quot;)
}
// 출력:
// 0: red
// 1: green
// 2: blue</code></pre>
<hr />
<h2 id="✅-배열이-비었을-경우-처리">✅ 배열이 비었을 경우 처리</h2>
<pre><code class="language-swift">if colors.isEmpty {
    print(&quot;배열이 비어있습니다.&quot;)
} else {
    for color in colors {
        print(color)
    }
}</code></pre>
<hr />
<h1 id="첨자subscript로-항목-접근">첨자(subscript)로 항목 접근</h1>
<h2 id="시험">시험</h2>
<hr />
<pre><code class="language-swift">// 정수형 배열 num을 선언하고 초기화
var num = [1, 2, 3, 4]</code></pre>
<hr />
<pre><code class="language-swift">// 배열의 첫 번째 요소(num[0])와 마지막 요소(num[3]) 출력
print(num[0], num[3])  // 출력: 1 4</code></pre>
<hr />
<pre><code class="language-swift">// 배열의 첫 요소에 안전하게 접근 (옵셔널 언래핑)
print(num.first!)      // 출력: 1
// num.first는 Optional이므로 !를 붙여 언래핑</code></pre>
<hr />
<pre><code class="language-swift">// for-in + 범위 연산자(...)를 사용하여 인덱스 기반 반복
for i in 0...num.count-1 {
    print(num[i])      // 출력: 1 2 3 4
}</code></pre>
<hr />
<pre><code class="language-swift">// 배열의 일부 구간(슬라이스) 출력 → 인덱스 1부터 2까지
print(num[1...2])      // 출력: [2, 3]
// 결과는 ArraySlice&lt;Int&gt;</code></pre>
<hr />
<pre><code class="language-swift">// 배열의 0~2번째 인덱스까지 부분을 새 값으로 변경
num[0...2] = [10, 20, 30]
// 기존 num: [1, 2, 3, 4]
// 바뀐 num: [10, 20, 30, 4]</code></pre>
<hr />
<pre><code class="language-swift">// 변경된 배열 전체 출력
print(num)             // 출력: [10, 20, 30, 4]</code></pre>
<hr />
<h2 id="✅-핵심-정리">✅ 핵심 정리</h2>
<table>
<thead>
<tr>
<th>표현</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>num[0]</code>, <code>num[3]</code></td>
<td>인덱스를 통한 직접 접근</td>
</tr>
<tr>
<td><code>num.first!</code></td>
<td>첫 요소 언래핑</td>
</tr>
<tr>
<td><code>for i in 0...num.count-1</code></td>
<td>전체 인덱스 순회</td>
</tr>
<tr>
<td><code>num[1...2]</code></td>
<td>배열 슬라이스 (ArraySlice)</td>
</tr>
<tr>
<td><code>num[0...2] = [...]</code></td>
<td>배열 부분 치환</td>
</tr>
</tbody></table>
<hr />
<h1 id="array는-구조체이므로-값-타입">Array는 구조체이므로 값 타입</h1>
<p>  맞습니다!  
Swift의 <code>Array</code>는 <strong>구조체(struct)</strong>로 구현되어 있기 때문에 <strong>값 타입(value type)</strong>입니다.<br />즉, 복사 시 <strong>값이 복제</strong>되고 <strong>별개의 독립된 배열</strong>이 됩니다.<br />아래는 주신 코드에 대한 <strong>주석 설명</strong>입니다.</p>
<hr />
<pre><code class="language-swift">// 정수형 배열 num 선언 및 초기화
var num = [1, 2, 3]

// num 배열을 x에 복사 → x는 num과는 별개의 복사본 (값 타입 복사)
var x = num

// num 배열의 첫 번째 요소만 변경
num[0] = 100</code></pre>
<hr />
<pre><code class="language-swift">// num은 [100, 2, 3] 으로 변경됨
print(num)   // 출력: [100, 2, 3]

// x는 변경되지 않고 원래 값 유지
print(x)     // 출력: [1, 2, 3]</code></pre>
<hr />
<h2 id="✅-핵심-개념-swift-배열은-값-타입">✅ 핵심 개념: Swift 배열은 <strong>값 타입</strong></h2>
<table>
<thead>
<tr>
<th>개념</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>Array</code>는 <code>struct</code> 기반</td>
<td>클래스와 달리 <strong>참조 X, 복사됨</strong></td>
</tr>
<tr>
<td><code>var x = num</code></td>
<td>x는 num의 <strong>복사본</strong></td>
</tr>
<tr>
<td><code>num[0] = 100</code></td>
<td>num만 변경, x는 영향 없음</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-시각적으로-보면">✅ 시각적으로 보면</h2>
<pre><code>num = [1, 2, 3]
x   = num     → [1, 2, 3] (복사됨)

num[0] = 100

결과:
num = [100, 2, 3]
x   = [1, 2, 3]</code></pre><hr />
<h1 id="array-요소의-최댓값-최솟값-max-min">Array 요소의 최댓값 최솟값 :max(), min()</h1>
<p>  좋아요! 아래는 <code>Array</code>에서 <strong>최댓값과 최솟값</strong>을 구하는 <code>min()</code>과 <code>max()</code> 메서드를 사용한 예제에 대한 <strong>주석 설명</strong>입니다. Swift에서는 이 두 메서드는 <strong>Optional 값을 반환</strong>하기 때문에 안전하게 처리하는 것도 중요합니다.</p>
<hr />
<pre><code class="language-swift">// 정수형 배열 선언
var num = [1, 2, 3, 10, 20]

// 배열 전체 출력
print(num)         // 출력: [1, 2, 3, 10, 20]</code></pre>
<hr />
<pre><code class="language-swift">// 배열에서 최솟값을 구함 → Optional(Int)
print(num.min())   // 출력: Optional(1)

// 배열에서 최댓값을 구함 → Optional(Int)
print(num.max())   // 출력: Optional(20)</code></pre>
<ul>
<li><code>min()</code>과 <code>max()</code>는 <strong>배열이 비어있을 경우 nil을 반환</strong>할 수 있으므로, 반환 타입이 <code>Int?</code> (옵셔널 Int)입니다.</li>
</ul>
<hr />
<pre><code class="language-swift">// 옵셔널을 강제 언래핑 → 배열이 비어 있지 않기 때문에 안전
print(num.min()!)  // 출력: 1
print(num.max()!)  // 출력: 20</code></pre>
<ul>
<li><code>!</code>를 붙이면 옵셔널이 아닌 일반 값으로 변환되지만,</li>
<li>배열이 비어 있으면 ❗️런타임 에러 발생 (Fatal error: unexpectedly found nil)</li>
</ul>
<hr />
<h2 id="✅-핵심-정리-1">✅ 핵심 정리</h2>
<table>
<thead>
<tr>
<th>메서드</th>
<th>반환 타입</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>min()</code></td>
<td><code>Int?</code></td>
<td>최솟값, 비어 있으면 nil</td>
</tr>
<tr>
<td><code>max()</code></td>
<td><code>Int?</code></td>
<td>최댓값, 비어 있으면 nil</td>
</tr>
<tr>
<td><code>min()!</code></td>
<td><code>Int</code></td>
<td>최솟값, 단 <strong>비어 있으면 crash 발생</strong></td>
</tr>
<tr>
<td><code>max()!</code></td>
<td><code>Int</code></td>
<td>최댓값, crash 가능성 있음</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-안전한-방법-옵셔널-바인딩">✅ 안전한 방법 (옵셔널 바인딩)</h2>
<pre><code class="language-swift">if let minValue = num.min(), let maxValue = num.max() {
    print(&quot;최솟값: \(minValue), 최댓값: \(maxValue)&quot;)
} else {
    print(&quot;배열이 비어 있습니다.&quot;)
}</code></pre>
<hr />
<h1 id="array-요소의-정렬">Array 요소의 정렬</h1>
<h2 id="시험-1">시험</h2>
<p>  아주 잘 정리하셨습니다!  
아래는 주신 코드를 기반으로 <strong>Swift에서 배열 요소를 정렬하는 다양한 방법</strong>에 대해 <strong>주석과 함께 설명</strong>해드린 버전입니다.<br /><code>sort()</code>, <code>sorted()</code>, <code>reverse()</code>의 차이점을 이해하는 데 특히 도움이 됩니다.</p>
<hr />
<pre><code class="language-swift">// 정렬 대상이 될 배열 선언
var num = [1, 5, 3, 2, 4]

// 오름차순 정렬 (원본 배열이 변경됨)
num.sort()                
print(num)               // 출력: [1, 2, 3, 4, 5]</code></pre>
<hr />
<pre><code class="language-swift">// 배열 요소를 다시 변경
num[0...4] = [2, 3, 4, 5, 1]

// 내림차순 정렬 (원본 배열 변경)
num.sort(by: &gt;)          
print(num)               // 출력: [5, 4, 3, 2, 1]</code></pre>
<hr />
<pre><code class="language-swift">// 다시 배열 값을 변경
num[0...4] = [2, 3, 4, 5, 1]

// 배열의 순서를 반대로 뒤집음 (원본 변경)
num.reverse()            
print(num)               // 출력: [1, 5, 4, 3, 2]</code></pre>
<hr />
<pre><code class="language-swift">// sorted(): 오름차순 정렬 결과를 반환하지만, 원본은 변경하지 않음
print(num.sorted())      // 출력: [1, 2, 3, 4, 5]

// 원본 배열은 그대로 유지됨
print(num)               // 출력: [1, 5, 4, 3, 2]</code></pre>
<hr />
<pre><code class="language-swift">// 내림차순 정렬 결과를 반환 (원본은 그대로)
print(num.sorted(by: &gt;)) // 출력: [5, 4, 3, 2, 1]

// 원본 배열 확인
print(num)               // 출력: [1, 5, 4, 3, 2]</code></pre>
<hr />
<h2 id="✅-핵심-요약-2">✅ 핵심 요약</h2>
<table>
<thead>
<tr>
<th>메서드</th>
<th>원본 변경 여부</th>
<th>정렬 방식</th>
<th>반환값 타입</th>
</tr>
</thead>
<tbody><tr>
<td><code>sort()</code></td>
<td>✅ 변경함</td>
<td>오름차순</td>
<td><code>Void</code> (반환 없음)</td>
</tr>
<tr>
<td><code>sort(by: &gt;)</code></td>
<td>✅ 변경함</td>
<td>내림차순</td>
<td><code>Void</code> (반환 없음)</td>
</tr>
<tr>
<td><code>reverse()</code></td>
<td>✅ 변경함</td>
<td>순서 반전</td>
<td><code>Void</code></td>
</tr>
<tr>
<td><code>sorted()</code></td>
<td>❌ 변경 안 함</td>
<td>오름차순 정렬 복사</td>
<td><code>[Element]</code> (새 배열 반환)</td>
</tr>
<tr>
<td><code>sorted(by: &gt;)</code></td>
<td>❌ 변경 안 함</td>
<td>내림차순 정렬 복사</td>
<td><code>[Element]</code> (새 배열 반환)</td>
</tr>
</tbody></table>
<hr />
<h1 id="swift의-접근제어">Swift의 접근제어</h1>
<p>(2025년 4월 9일 기준, Swift 5.9 및 6.0 포함)</p>
<h3 id="swift-접근-제어-수준">Swift 접근 제어 수준</h3>
<table>
<thead>
<tr>
<th>접근 수준</th>
<th>설명</th>
<th>범위</th>
</tr>
</thead>
<tbody><tr>
<td><code>open</code></td>
<td>모듈 외부(다른 패키지 포함)에서 상속 및 오버라이드 가능.</td>
<td>전체 모듈 및 모듈 외부 (패키지 간 접근 가능).</td>
</tr>
<tr>
<td><code>public</code></td>
<td>모듈 외부(다른 패키지 포함)에서 사용 가능하지만 상속/오버라이드 불가.</td>
<td>전체 모듈 및 모듈 외부 (패키지 간 호출 가능).</td>
</tr>
<tr>
<td><code>package</code></td>
<td>동일 패키지 내 모든 모듈에서 접근 가능, 패키지 외부에서는 접근 불가.</td>
<td>동일 패키지 내 모든 모듈 (패키지 외부 접근 불가).</td>
</tr>
<tr>
<td><code>internal</code></td>
<td>동일 모듈 내에서만 접근 가능.</td>
<td>동일 모듈 내 (패키지 내 다른 모듈 및 패키지 외부 접근 불가).</td>
</tr>
<tr>
<td><code>fileprivate</code></td>
<td>동일 파일 내에서만 접근 가능.</td>
<td>동일 파일 내 (파일 외부 및 패키지 외부 접근 불가).</td>
</tr>
<tr>
<td><code>private</code></td>
<td>동일 선언 블록 내에서만 접근 가능.</td>
<td>동일 선언 블록 내 (선언 블록 외부 및 패키지 외부 접근 불가).</td>
</tr>
</tbody></table>
<h3 id="추가-정보">추가 정보</h3>
<ul>
<li><strong>&quot;package&quot; 도입</strong>: Swift 5.9에서 추가, Swift 6.0에서 강화. 동일 패키지 내 모듈 간 공유용.</li>
<li><strong>사용 조건</strong>: Swift 5.9 이상, <code>swift-tools-version</code> 5.9 이상 설정 필요.</li>
<li><strong>예시</strong>:<pre><code class="language-swift">package class Example {
    func method() {}
}</code></pre>
</li>
</ul>
<hr />
<h1 id="swift의-접근제어-중에서-인터널">swift의 접근제어 중에서 인터널</h1>
<p>  Swift의 접근 제어 중 <code>internal</code>은 다음과 같습니다:</p>
<h3 id="internal"><code>internal</code></h3>
<ul>
<li><strong>설명</strong>: 동일 모듈(module) 내에서만 접근 가능합니다. Swift에서 기본 접근 수준으로, 명시적으로 다른 접근 제어를 지정하지 않으면 자동으로 <code>internal</code>이 적용됩니다.</li>
<li><strong>범위</strong>: 동일 모듈 내에서만 유효하며, 모듈 외부(다른 패키지나 모듈)에서는 접근할 수 없습니다. 패키지 내 다른 모듈에서도 접근 불가입니다.</li>
<li><strong>사용 예시</strong>: 패키지나 앱 내부에서만 사용되며, 외부로 노출할 필요가 없는 코드에 적합합니다. 예를 들어, 프레임워크의 내부 유틸리티 함수나 클래스.</li>
</ul>
<h3 id="추가-세부사항">추가 세부사항</h3>
<ul>
<li><strong>모듈(Module)</strong>: Swift에서 모듈은 독립적인 코드 단위로, 일반적으로 프레임워크, 라이브러리, 또는 애플리케이션 타겟을 의미합니다. 예를 들어, 한 패키지 안에 여러 모듈이 있을 수 있으며, <code>internal</code>은 그 모듈의 경계를 넘지 않습니다.</li>
<li><strong>비교</strong>: <ul>
<li><code>public</code>이나 <code>open</code>은 모듈 외부에서도 접근 가능하지만, <code>internal</code>은 모듈 내부에만 한정됩니다.</li>
<li><code>package</code> 접근 제어(Swift 5.9 이상)와의 차이: <code>package</code>는 동일 패키지 내 모든 모듈에서 접근 가능하지만, <code>internal</code>은 오직 동일 모듈 내에서만 작동합니다.</li>
</ul>
</li>
</ul>
<h3 id="예시-코드">예시 코드</h3>
<pre><code class="language-swift">internal class InternalClass {
    internal func internalMethod() {
        print(&quot;이 메서드는 동일 모듈 내에서만 호출 가능합니다.&quot;)
    }
}

// 동일 모듈 내에서는 접근 가능
let obj = InternalClass()
obj.internalMethod()

// 다른 모듈이나 패키지에서는 접근 불가
// import OtherModule
// let obj = InternalClass() // 오류 발생</code></pre>
<h3 id="요약">요약</h3>
<p><code>internal</code>은 Swift의 기본 접근 수준으로, 코드 캡슐화를 유지하면서 동일 모듈 내에서만 사용되도록 제한합니다. 외부 노출을 최소화하려는 경우 유용합니다.</p>