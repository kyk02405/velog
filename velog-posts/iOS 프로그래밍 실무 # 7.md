<hr />
<h1 id="enum열거형을-지원하는-프로그래밍-언어">enum(열거형)을 지원하는 프로그래밍 언어</h1>
<h3 id="✅-열거형enum을-명시적으로-지원하는-주요-언어">✅ 열거형(enum)을 명시적으로 지원하는 주요 언어</h3>
<table>
<thead>
<tr>
<th>언어</th>
<th>특징</th>
</tr>
</thead>
<tbody><tr>
<td><strong>C</strong></td>
<td><code>enum</code> 키워드로 기본 타입이 정수형</td>
</tr>
<tr>
<td><strong>C++</strong></td>
<td>C와 동일 + <code>enum class</code>로 타입 안전성 강화</td>
</tr>
<tr>
<td><strong>Java</strong></td>
<td>클래스 수준의 강력한 <code>enum</code> 지원 (메서드, 필드 포함 가능)</td>
</tr>
<tr>
<td><strong>C#</strong></td>
<td><code>enum</code> 지원 + 기본형 지정 가능</td>
</tr>
<tr>
<td><strong>Swift</strong></td>
<td>강력한 <code>enum</code>, 연관값(associated value), 메서드, 패턴 매칭 지원</td>
</tr>
<tr>
<td><strong>Rust</strong></td>
<td><code>enum</code>은 알게브라적 데이터 타입 (ADT) 지원, 매우 유연</td>
</tr>
<tr>
<td><strong>Kotlin</strong></td>
<td><code>enum class</code> 제공, 메서드/필드 정의 가능</td>
</tr>
<tr>
<td><strong>TypeScript</strong></td>
<td><code>enum</code> 키워드 제공 (숫자형, 문자열형)</td>
</tr>
<tr>
<td><strong>Scala</strong></td>
<td><code>sealed trait + case object</code> 패턴으로 구현</td>
</tr>
<tr>
<td><strong>Go</strong></td>
<td>직접적인 <code>enum</code> 없음, <code>const + iota</code>로 유사하게 구현</td>
</tr>
<tr>
<td><strong>Python</strong></td>
<td><code>enum</code> 모듈 (<code>from enum import Enum</code>)</td>
</tr>
<tr>
<td><strong>Dart</strong></td>
<td><code>enum</code> 키워드로 지원 (2.17부터 개선됨)</td>
</tr>
<tr>
<td><strong>F#</strong></td>
<td><code>type</code> 키워드로 열거형 정의 (Discriminated Union으로 표현 가능)</td>
</tr>
<tr>
<td><strong>Objective-C</strong></td>
<td><code>typedef NS_ENUM</code> 또는 <code>typedef enum</code> 사용</td>
</tr>
<tr>
<td><strong>Ruby</strong></td>
<td>내장 <code>enum</code>은 없지만 <code>Symbol</code>, <code>Module</code> 등으로 유사 구현</td>
</tr>
<tr>
<td><strong>PHP</strong></td>
<td>PHP 8.1부터 <code>enum</code> 키워드 지원</td>
</tr>
<tr>
<td><strong>Haskell</strong></td>
<td>데이터 타입 정의로 enum 구현 가능 (<code>data</code>)</td>
</tr>
<tr>
<td><strong>Elixir</strong></td>
<td><code>enum</code> 없음. <code>atom</code> 또는 <code>module</code> + pattern matching 사용</td>
</tr>
</tbody></table>
<hr />
<h3 id="⚠️-enum을-직접-지원하지는-않지만-유사-구현-가능한-언어">⚠️ <code>enum</code>을 직접 지원하지는 않지만 유사 구현 가능한 언어</h3>
<table>
<thead>
<tr>
<th>언어</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>JavaScript</strong></td>
<td><code>Object.freeze({...})</code>, 상수 객체로 흉내냄</td>
</tr>
<tr>
<td><strong>Perl</strong></td>
<td>상수와 해시로 구현</td>
</tr>
<tr>
<td><strong>Shell script (bash)</strong></td>
<td>직접 지원 없음. 문자열 비교나 숫자로 처리</td>
</tr>
</tbody></table>
<hr />
<h3 id="✅-요약">✅ 요약</h3>
<ul>
<li>대부분의 <strong>정적 타입 언어</strong> (Java, C#, Swift, Rust 등)는 enum을 명시적으로 지원합니다.</li>
<li><strong>스크립트 언어</strong>들은 직접적인 enum 지원은 적지만, 유사한 방식으로 구현 가능합니다.</li>
</ul>
<hr />
<h1 id="enum열거형">enum(열거형)</h1>
<h3 id="✅-기본-형식">✅ 기본 형식</h3>
<pre><code class="language-swift">enum 열거형명 {
    열거형 정의
}</code></pre>
<p><code>enum</code> 키워드를 사용해서 열거형을 정의합니다.</p>
<hr />
<h3 id="🪐-예시-1-planet-열거형">🪐 예시 1: <code>Planet</code> 열거형</h3>
<pre><code class="language-swift">enum Planet {
    case Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
}</code></pre>
<ul>
<li>태양계의 행성들을 나열한 열거형입니다.</li>
<li>Swift에서는 <code>case</code> 한 줄에 여러 개의 값을 쉼표로 나열할 수 있습니다.</li>
</ul>
<hr />
<h3 id="🧭-예시-2-compass-열거형">🧭 예시 2: <code>Compass</code> 열거형</h3>
<pre><code class="language-swift">enum Compass {
    case North
    case South
    case East
    case West
}</code></pre>
<ul>
<li>방향을 나타내는 열거형입니다.</li>
<li>각 방향을 멤버(case)로 가집니다.</li>
</ul>
<hr />
<h3 id="💡-사용-예시">💡 사용 예시</h3>
<pre><code class="language-swift">print(Compass.North) // North</code></pre>
<ul>
<li>Compass 열거형의 <code>North</code> 멤버를 출력합니다.</li>
</ul>
<pre><code class="language-swift">var x = Compass.West
print(type(of: x)) // Compass</code></pre>
<ul>
<li>변수 <code>x</code>는 Compass 타입이며, <code>West</code> 값을 가지고 있습니다.</li>
<li><code>type(of: x)</code>는 변수의 타입을 출력합니다.</li>
</ul>
<pre><code class="language-swift">x = .East
print(x) // East</code></pre>
<ul>
<li>Swift에서는 <code>x = .East</code>처럼 타입 추론이 가능한 경우 열거형 이름을 생략할 수 있습니다.</li>
</ul>
<hr />
<h3 id="🔍-참고">🔍 참고</h3>
<ul>
<li><strong>타입 추론이 가능한 시점</strong> (예: 변수가 이미 Compass 타입임이 명확한 경우)에는 <code>Compass.</code>를 생략하고 <code>.East</code>처럼 간단히 작성할 수 있습니다.</li>
</ul>
<h3 id="📌-핵심-요약">📌 핵심 요약</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>enum</code></td>
<td>관련된 값들을 하나의 사용자 정의 타입으로 묶는 기능입니다.</td>
</tr>
<tr>
<td><code>case</code></td>
<td>열거형 내부에서 사용할 수 있는 각각의 값(멤버)을 정의합니다.</td>
</tr>
<tr>
<td>타입 추론</td>
<td>Swift는 <code>var x = Compass.West</code>와 같은 코드에서 자동으로 타입을 추론합니다.</td>
</tr>
<tr>
<td>열거형 이름 생략</td>
<td>변수의 타입이 명확한 경우 <code>.값</code>처럼 열거형 이름 없이도 작성할 수 있습니다.</td>
</tr>
</tbody></table>
<hr />
<h1 id="✅-열거형-멤버별-기능-정의-코드">✅ 열거형 멤버별 기능 정의 코드</h1>
<pre><code class="language-swift">enum Compass {
    case North
    case South
    case East
    case West
}

var direction: Compass
direction = .South

switch direction {
case .North:
    print(&quot;북&quot;)
case .South:
    print(&quot;남&quot;)
case .East:
    print(&quot;동&quot;)
case .West:
    print(&quot;서&quot;)
}</code></pre>
<hr />
<h3 id="📌-설명">📌 설명</h3>
<ul>
<li><p><code>enum Compass { ... }</code><br />→ <code>North</code>, <code>South</code>, <code>East</code>, <code>West</code> 네 가지 방향을 표현하는 열거형입니다.</p>
</li>
<li><p><code>var direction: Compass</code><br />→ <code>Compass</code> 타입의 변수 <code>direction</code>을 선언했습니다.</p>
</li>
<li><p><code>direction = .South</code><br />→ <code>direction</code>에 <code>South</code> 방향을 할당했습니다.<br />   이미 타입이 <code>Compass</code>로 정해졌기 때문에 <code>.South</code>처럼 열거형 이름 생략이 가능합니다.</p>
</li>
<li><p><code>switch direction { ... }</code><br />→ <code>switch</code>문을 사용해서 <code>direction</code>의 값에 따라 분기 처리합니다.</p>
</li>
<li><p><code>case .North</code>, <code>case .South</code>, ...<br />→ 각각의 열거형 멤버에 따라 다른 메시지를 출력합니다.</p>
</li>
<li><p><code>default</code>는 필요 없습니다.<br />→ <code>switch</code>문에서 <strong>모든 열거형 멤버를 case로 나열</strong>하면 <code>default</code> 없이도 문법적으로 완전합니다.</p>
</li>
</ul>
<hr />
<h1 id="✅-코드-예제-열거형-멤버에-메서드-추가">✅ 코드 예제: 열거형 멤버에 메서드 추가</h1>
<pre><code class="language-swift">enum Week {
    case Mon, Tue, Wed, Thur, Fri, Sat, Sun

    func printWeek() { // 열거형 내부 메서드 정의
        switch self { // self는 현재 열거형 값 (예: .Sun)
        case .Mon, .Tue, .Wed, .Thur, .Fri:
            print(&quot;주중&quot;)
        case .Sat, .Sun:
            print(&quot;주말&quot;)
        }
    }
}

// 열거형의 멤버에 직접 메서드를 호출할 수 있습니다.
Week.Sun.printWeek() // 출력: 주말</code></pre>
<hr />
<h3 id="📌-설명-1">📌 설명</h3>
<ul>
<li><code>enum Week</code>는 한 주의 요일들을 나열한 열거형입니다.</li>
<li><code>printWeek()</code>는 열거형 내부에 정의된 <strong>인스턴스 메서드</strong>입니다.</li>
<li><code>switch self</code>는 이 메서드를 호출한 <strong>자기 자신(현재 열거형 값)</strong>을 의미합니다.<ul>
<li>예: <code>Week.Sun.printWeek()</code>라면 <code>self</code>는 <code>.Sun</code>입니다.</li>
</ul>
</li>
<li>따라서 <code>.Sun</code>이 <code>case .Sat, .Sun:</code>에 해당되므로 <strong>&quot;주말&quot;</strong>이 출력됩니다.</li>
</ul>
<hr />
<h3 id="💡-메서드-호출-결과">💡 메서드 호출 결과</h3>
<pre><code class="language-swift">Week.Sun.printWeek()
// 콘솔 출력: 주말</code></pre>
<hr />
<p>Swift에서는 열거형을 클래스나 구조체처럼 <strong>메서드, 계산 프로퍼티, 연관 값, static 멤버</strong> 등으로 확장할 수 있기 때문에 굉장히 유연하고 강력합니다.</p>
<hr />
<h1 id="✅-코드-예제-열거형의-rawvalue-사용">✅ 코드 예제: 열거형의 rawValue 사용</h1>
<pre><code class="language-swift">enum Color: Int { // 열거형 Color는 Int 타입의 원시값(rawValue)을 가짐
    case red           // 자동으로 0이 할당됨
    case green = 2     // 수동으로 2를 지정
    case blue          // 이전 값(2) 기준으로 +1 → 3이 자동 할당됨
}

print(Color.red)           // 출력: red
print(Color.blue)          // 출력: blue
print(Color.red.rawValue)  // 출력: 0
print(Color.blue.rawValue) // 출력: 3</code></pre>
<hr />
<h3 id="📌-설명-2">📌 설명</h3>
<h4 id="🔷-enum-color-int">🔷 <code>enum Color: Int</code></h4>
<ul>
<li><code>Color</code>라는 열거형을 선언하면서 <code>rawValue</code> 타입으로 <code>Int</code>를 지정합니다.</li>
<li>즉, 각 <code>case</code>에 정수 값을 자동 또는 수동으로 할당할 수 있게 됩니다.</li>
</ul>
<h4 id="🔷-원시값-자동-할당-규칙">🔷 원시값 자동 할당 규칙</h4>
<ul>
<li><code>case red</code>는 첫 번째 항목이므로 기본적으로 <code>0</code>이 할당됩니다.</li>
<li><code>case green = 2</code>는 수동으로 <code>2</code>를 지정합니다.</li>
<li><code>case blue</code>는 <code>green</code>의 다음 순번이므로 자동으로 <code>3</code>이 할당됩니다.</li>
</ul>
<h4 id="🔷-printcolorred--printcolorblue">🔷 <code>print(Color.red)</code> / <code>print(Color.blue)</code></h4>
<ul>
<li>열거형 멤버 자체를 출력하면 Swift는 멤버 이름을 문자열로 보여줍니다.<ul>
<li>예: <code>&quot;red&quot;</code>, <code>&quot;blue&quot;</code></li>
</ul>
</li>
</ul>
<h4 id="🔷-printcolorredrawvalue">🔷 <code>print(Color.red.rawValue)</code></h4>
<ul>
<li><code>.rawValue</code>를 사용하면 해당 멤버에 할당된 정수 값을 확인할 수 있습니다.<ul>
<li><code>Color.red.rawValue</code> → <code>0</code></li>
<li><code>Color.blue.rawValue</code> → <code>3</code></li>
</ul>
</li>
</ul>
<hr />
<h3 id="💡-요약">💡 요약</h3>
<table>
<thead>
<tr>
<th>멤버</th>
<th>출력 값</th>
<th>rawValue</th>
</tr>
</thead>
<tbody><tr>
<td><code>Color.red</code></td>
<td>red</td>
<td>0</td>
</tr>
<tr>
<td><code>Color.green</code></td>
<td>green</td>
<td>2</td>
</tr>
<tr>
<td><code>Color.blue</code></td>
<td>blue</td>
<td>3</td>
</tr>
</tbody></table>
<hr />
<h1 id="✅-코드-예제-string형-rawvalue를-갖는-열거형">✅ 코드 예제: String형 rawValue를 갖는 열거형</h1>
<pre><code class="language-swift">enum Week: String {
    case Monday = &quot;월&quot;
    case Tuesday = &quot;화&quot;
    case Wednesday = &quot;수&quot;
    case Thursday = &quot;목&quot;
    case Friday = &quot;금&quot;
    case Saturday           // 값을 지정하지 않으면 case 이름인 &quot;Saturday&quot;가 자동으로 할당됨
    case Sunday             // 마찬가지로 &quot;Sunday&quot;가 할당됨
}

print(Week.Monday)           // 출력: Monday
print(Week.Monday.rawValue)  // 출력: 월
print(Week.Sunday)           // 출력: Sunday
print(Week.Sunday.rawValue)  // 출력: Sunday</code></pre>
<hr />
<h3 id="📌-상세-설명">📌 상세 설명</h3>
<h4 id="🔷-enum-week-string">🔷 <code>enum Week: String</code></h4>
<ul>
<li><code>Week</code>라는 열거형을 선언하고, 각 멤버에 <strong>문자열(rawValue)</strong> 을 할당합니다.</li>
<li><code>String</code>을 <code>rawValue</code> 타입으로 지정하면 각 case에 대응하는 문자열 값을 가질 수 있습니다.</li>
</ul>
<h4 id="🔷-직접-지정한-경우">🔷 직접 지정한 경우</h4>
<ul>
<li><code>case Monday = &quot;월&quot;</code> 등은 한국어로 직접 문자열을 지정한 것입니다.</li>
<li>이런 경우 <code>.rawValue</code>로 해당 문자열을 불러올 수 있습니다.<ul>
<li>예: <code>Week.Monday.rawValue</code> → <code>&quot;월&quot;</code></li>
</ul>
</li>
</ul>
<h4 id="🔷-자동-할당된-경우">🔷 자동 할당된 경우</h4>
<ul>
<li><code>case Saturday</code>, <code>case Sunday</code>처럼 별도로 값을 지정하지 않으면 <strong>case 이름 그 자체가 rawValue로 사용</strong>됩니다.<ul>
<li><code>Week.Saturday.rawValue</code> → <code>&quot;Saturday&quot;</code></li>
<li><code>Week.Sunday.rawValue</code> → <code>&quot;Sunday&quot;</code></li>
</ul>
</li>
</ul>
<h4 id="🔷-출력-예시">🔷 출력 예시</h4>
<table>
<thead>
<tr>
<th>표현식</th>
<th>출력 결과</th>
</tr>
</thead>
<tbody><tr>
<td><code>Week.Monday</code></td>
<td>Monday</td>
</tr>
<tr>
<td><code>Week.Monday.rawValue</code></td>
<td>월</td>
</tr>
<tr>
<td><code>Week.Sunday</code></td>
<td>Sunday</td>
</tr>
<tr>
<td><code>Week.Sunday.rawValue</code></td>
<td>Sunday</td>
</tr>
</tbody></table>
<hr />
<h3 id="💡-정리">💡 정리</h3>
<ul>
<li><code>rawValue</code>는 열거형의 각 멤버에 할당된 <strong>기본 값</strong>입니다.</li>
<li><code>String</code> 타입으로 지정하면, 문자열로 표현할 수 있어 <strong>사용자 친화적인 코드 작성</strong>이 가능합니다.</li>
<li>값을 명시하지 않으면 <strong>case 이름이 자동으로 rawValue가 됩니다</strong>.</li>
</ul>
<hr />
<h1 id="✅-연관-값을-갖는-열거형enum-예제">✅ 연관 값을 갖는 열거형(enum) 예제</h1>
<pre><code class="language-swift">enum Date {
    case intDate(Int, Int, Int) // 정수 3개(연,월,일)를 저장
    case stringDate(String)     // 문자열 하나를 저장
}

var todayDate = Date.intDate(2025, 4, 30)

// 아래 줄이 실행되면 todayDate는 stringDate로 바뀌게 됩니다
todayDate = Date.stringDate(&quot;2025년 5월 20일&quot;) // 이 줄을 주석 처리하면 출력 결과가 달라집니다

switch todayDate {
case .intDate(let year, let month, let day):
    print(&quot;\(year)년 \(month)월 \(day)일&quot;)
case .stringDate(let date):
    print(date)
}</code></pre>
<hr />
<h3 id="📌-설명-3">📌 설명</h3>
<h4 id="🔷-열거형-정의">🔷 열거형 정의</h4>
<pre><code class="language-swift">enum Date {
    case intDate(Int, Int, Int)
    case stringDate(String)
}</code></pre>
<ul>
<li><code>intDate</code>는 <strong>정수형 3개의 연관 값</strong>을 가집니다. → 예: <code>intDate(2025, 4, 30)</code></li>
<li><code>stringDate</code>는 <strong>문자열 1개의 연관 값</strong>을 가집니다. → 예: <code>stringDate(&quot;2025년 5월 20일&quot;)</code></li>
</ul>
<h4 id="🔷-값-할당과-재할당">🔷 값 할당과 재할당</h4>
<pre><code class="language-swift">var todayDate = Date.intDate(2025, 4, 30)
todayDate = Date.stringDate(&quot;2025년 5월 20일&quot;)</code></pre>
<ul>
<li>처음엔 <code>intDate</code>로 값을 넣었다가,</li>
<li>그 다음 줄에서 <code>stringDate</code>로 덮어씌웠기 때문에<br />이후 <code>todayDate</code>는 문자열을 가진 <code>stringDate</code> 상태입니다.</li>
</ul>
<blockquote>
<p>📌 만약 <code>stringDate(...)</code> 줄을 <strong>주석 처리</strong>하면, 그대로 <code>intDate(2025, 4, 30)</code>이 유지되므로<br />출력은: <code>2025년 4월 30일</code>이 됩니다.</p>
</blockquote>
<h4 id="🔷-switch-구문">🔷 switch 구문</h4>
<pre><code class="language-swift">switch todayDate {
case .intDate(let year, let month, let day):
    print(&quot;\(year)년 \(month)월 \(day)일&quot;)
case .stringDate(let date):
    print(date)
}</code></pre>
<ul>
<li><code>todayDate</code>의 열거형 케이스에 따라 적절히 분기하여 출력을 다르게 합니다.</li>
<li><code>let</code>을 사용해 연관된 값을 추출할 수 있습니다.</li>
</ul>
<hr />
<h3 id="🧾-실행-결과">🧾 실행 결과</h3>
<ul>
<li><code>todayDate = Date.stringDate(&quot;2025년 5월 20일&quot;)</code> 이 줄이 있을 경우:</li>
</ul>
<pre><code class="language-text">2025년 5월 20일</code></pre>
<ul>
<li>위 줄을 <strong>주석 처리하면</strong>:</li>
</ul>
<pre><code class="language-text">2025년 4월 30일</code></pre>
<hr />
<h3 id="✅-핵심-요약">✅ 핵심 요약</h3>
<table>
<thead>
<tr>
<th>특징</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>associated value</code></td>
<td>열거형의 각 case에 값을 동적으로 저장 가능</td>
</tr>
<tr>
<td><code>switch</code> 구문</td>
<td>각 case에서 연관 값을 <code>let</code>으로 꺼내서 사용</td>
</tr>
<tr>
<td>유용한 상황</td>
<td>네트워크 응답, 입력 데이터 포맷, 상태 표시 등에 다양하게 활용됨</td>
</tr>
</tbody></table>
<hr />
<h1 id="✅-optional은-연관-값을-갖는-enum이다">✅ Optional은 연관 값을 갖는 enum이다</h1>
<h3 id="📌-전체-코드">📌 전체 코드</h3>
<pre><code class="language-swift">let age: Int? = 30 // Optional(30)

switch age {
case .none: // nil인 경우
    print(&quot;나이 정보가 없습니다.&quot;)
case .some(let a) where a &lt; 20:
    print(&quot;\(a)살 미성년자입니다&quot;)
case .some(let a) where a &lt; 71:
    print(&quot;\(a)살 성인입니다&quot;)
default:
    print(&quot;경로우대입니다&quot;)
}

public enum Optional&lt;Wrapped&gt; {
    case none
    case some(Wrapped)
} // Swift 내부에 이미 정의된 열거형

var x: Int? = 20                  // .some(20)
var y: Int? = Optional.some(10)   // 명시적으로 some 생성
var z: Int? = Optional.none       // 명시적으로 nil 생성
var x1: Optional&lt;Int&gt; = 30        // Optional.some(30)과 동일
print(x, y, z, x1)                // Optional(20) Optional(10) nil Optional(30)</code></pre>
<hr />
<h3 id="🔹-1-optional-값을-switch로-처리">🔹 1. Optional 값을 switch로 처리</h3>
<pre><code class="language-swift">let age: Int? = 30

switch age {
case .none:
    print(&quot;나이 정보가 없습니다.&quot;)
case .some(let a) where a &lt; 20:
    print(&quot;\(a)살 미성년자입니다&quot;)
case .some(let a) where a &lt; 71:
    print(&quot;\(a)살 성인입니다&quot;)
default:
    print(&quot;경로우대입니다&quot;)
}</code></pre>
<ul>
<li><code>Int?</code>는 내부적으로 <code>Optional&lt;Int&gt;</code>로 동작합니다.</li>
<li><code>Optional</code>은 사실상 <code>enum</code>이고, <code>.some(값)</code> 또는 <code>.none</code> 두 가지 상태를 가집니다.</li>
<li><code>30</code>은 <code>.some(30)</code>이므로 <code>case .some(let a) where a &lt; 71</code>에 해당되어 <code>&quot;30살 성인입니다&quot;</code>가 출력됩니다.</li>
</ul>
<hr />
<h3 id="🔹-2-optional은-enum이다">🔹 2. Optional은 enum이다</h3>
<pre><code class="language-swift">public enum Optional&lt;Wrapped&gt; {
    case none
    case some(Wrapped)
}</code></pre>
<ul>
<li>Swift 표준 라이브러리에 정의되어 있는 실제 <code>Optional</code> 열거형입니다.</li>
<li><code>Wrapped</code>는 제네릭 타입이며, <code>some</code>은 값을 가지고, <code>none</code>은 nil을 의미합니다.</li>
<li>직접 정의하지 않아도 iOS 내부에 이미 포함되어 있습니다.</li>
</ul>
<hr />
<h3 id="🔹-3-optional-생성-예시">🔹 3. Optional 생성 예시</h3>
<pre><code class="language-swift">var x: Int? = 20                  // .some(20)
var y: Int? = Optional.some(10)   // 명시적으로 some 생성
var z: Int? = Optional.none       // 명시적으로 nil 생성
var x1: Optional&lt;Int&gt; = 30        // Optional.some(30)과 동일
print(x, y, z, x1)</code></pre>
<ul>
<li><code>x</code>: 일반적인 Optional 대입 방식 (<code>.some(20)</code>과 동일)</li>
<li><code>y</code>: 명시적으로 <code>.some(10)</code>을 사용</li>
<li><code>z</code>: 명시적으로 <code>.none</code>, 즉 nil</li>
<li><code>x1</code>: 제네릭 타입으로 직접 명시 (Optional = 30 → some(30))</li>
</ul>
<p>출력 결과:</p>
<pre><code>Optional(20) Optional(10) nil Optional(30)</code></pre><hr />
<h1 id="✅-uitableviewcellcellstyle-지정-방법">✅ UITableViewCell.CellStyle 지정 방법</h1>
<h3 id="📌-예제-코드">📌 예제 코드</h3>
<pre><code class="language-swift">func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -&gt; UITableViewCell {
    let cell = UITableViewCell(style: .default, reuseIdentifier: &quot;myCell&quot;)
    return cell
}</code></pre>
<hr />
<h3 id="🟩-설명">🟩 설명</h3>
<h4 id="🔸-uitableviewcellstylereuseidentifier-생성자">🔸 <code>UITableViewCell(style:reuseIdentifier:)</code> 생성자</h4>
<ul>
<li>이 생성자를 사용하면 <strong>셀 스타일을 직접 지정</strong>할 수 있습니다.</li>
<li><code>style:</code>에 입력 가능한 값은 <code>UITableViewCell.CellStyle</code>의 열거형 멤버입니다.</li>
</ul>
<h4 id="🔸-default-입력-시">🔸 <code>.default</code> 입력 시</h4>
<ul>
<li><code>.</code>을 입력하면 자동완성 기능이 작동하여 <code>.default</code>, <code>.subtitle</code> 등 사용 가능한 스타일이 제안됩니다.</li>
<li>예: <code>.default</code>, <code>.subtitle</code>, <code>.value1</code>, <code>.value2</code></li>
</ul>
<h4 id="🔸-reuseidentifier-mycell">🔸 <code>reuseIdentifier: &quot;myCell&quot;</code></h4>
<ul>
<li>셀을 재사용하기 위한 식별자입니다.</li>
<li>문자열 <code>&quot;myCell&quot;</code>로 지정하면, 이 식별자를 기준으로 셀을 재사용할 수 있게 됩니다.</li>
</ul>
<hr />
<h3 id="⚠️-주의사항">⚠️ 주의사항</h3>
<ul>
<li><code>UITableViewCell(style:reuseIdentifier:)</code>를 사용하면 셀을 직접 초기화하므로<br /><code>dequeueReusableCell(withIdentifier:)</code>와 병행할 때는 주의해야 합니다.</li>
<li><code>return</code> 문을 생략하면 “Missing return in a function expected to return 'UITableViewCell'” 오류가 발생합니다.</li>
</ul>
<hr />
<h3 id="📌-예시-완성-코드">📌 예시 완성 코드</h3>
<pre><code class="language-swift">func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -&gt; UITableViewCell {
    let cell = UITableViewCell(style: .default, reuseIdentifier: &quot;myCell&quot;)
    cell.textLabel?.text = &quot;셀 텍스트&quot;
    return cell
}</code></pre>
<hr />
<h1 id="✅-구조체-struct">✅ 구조체 (Struct)</h1>
<p>Swift에서 <code>struct</code>는 클래스(<code>class</code>)와 유사하지만, <strong>값 타입</strong>이며 몇 가지 중요한 차이점을 가집니다.</p>
<hr />
<h3 id="🔹-구조체의-주요-특징">🔹 구조체의 주요 특징</h3>
<ul>
<li><code>Memberwise Initializer</code>가 자동 생성됨</li>
<li>Int, Double, String 등 <strong>기본 자료형은 구조체</strong></li>
<li><span style="color: red;">구조체는 <strong>값 타입(value type)</strong>  </span></li>
<li><span style="color: red;">구조체는 <strong>상속 불가</strong></span></li>
<li>구조체는 <strong>확장(extension)</strong> 가능</li>
<li>Swift의 <code>Array</code>, <code>Dictionary</code>, <code>Set</code>도 <strong>Generic 구조체</strong></li>
</ul>
<hr />
<h3 id="🔸-memberwise-initializer">🔸 Memberwise Initializer</h3>
<pre><code class="language-swift">struct Resolution {
    var width: Int
    var height: Int
}

// 자동으로 생성된 이니셜라이저 사용 가능
let hd = Resolution(width: 1920, height: 1080)
print(hd.width)  // 1920</code></pre>
<blockquote>
<p>구조체는 <code>init(width:height:)</code> 생성자를 따로 정의하지 않아도 자동으로 제공됩니다.</p>
</blockquote>
<hr />
<h3 id="🔸-swift의-기본-타입은-모두-구조체">🔸 Swift의 기본 타입은 모두 구조체</h3>
<pre><code class="language-swift">let age: Int = 30       // Int는 구조체
let pi: Double = 3.14   // Double도 구조체
let name: String = &quot;홍길동&quot; // String도 구조체</code></pre>
<blockquote>
<p>Apple 문서에 따르면, <code>Int</code>, <code>Double</code>, <code>String</code>, <code>Array</code> 등은 모두 구조체로 정의되어 있으며 <code>@frozen struct</code> 형태로 구현되어 있습니다.</p>
</blockquote>
<hr />
<h3 id="🔸-frozen-속성">🔸 @frozen 속성</h3>
<ul>
<li>구조체 정의에 붙는 <code>@frozen</code> 속성은, <strong>저장 프로퍼티의 변경이 불가능함</strong>을 의미합니다.</li>
<li>즉, ABI 안정성을 위해 속성을 <strong>추가하거나 제거할 수 없는 구조체</strong>임을 나타냅니다.</li>
</ul>
<pre><code class="language-swift">@frozen
public struct Int {
    // 내부 구현
}</code></pre>
<hr />
<h3 id="🔸-array-dictionary-set도-구조체">🔸 Array, Dictionary, Set도 구조체</h3>
<pre><code class="language-swift">var arr: Array&lt;Int&gt; = [1, 2, 3]
var dict: Dictionary&lt;String, Int&gt; = [&quot;a&quot;: 1]
var set: Set&lt;Int&gt; = [1, 2, 3]</code></pre>
<blockquote>
<p>Swift의 컬렉션 타입들은 모두 구조체이며, 제네릭(Generic) 구조체입니다.<br />예: <code>struct Array&lt;Element&gt;</code>, <code>struct Dictionary&lt;Key, Value&gt;</code></p>
</blockquote>
<hr />
<h3 id="🔸-값-타입-vs-참조-타입">🔸 값 타입 vs. 참조 타입</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>구조체 (struct)</th>
<th>클래스 (class)</th>
</tr>
</thead>
<tbody><tr>
<td>타입</td>
<td>값 타입 (copy)</td>
<td>참조 타입 (reference)</td>
</tr>
<tr>
<td>복사 시</td>
<td><strong>별도 복사본 생성</strong></td>
<td><strong>같은 인스턴스 참조</strong></td>
</tr>
<tr>
<td>상속</td>
<td>❌ 불가능</td>
<td>✅ 가능</td>
</tr>
<tr>
<td>예시</td>
<td>Int, String, Array</td>
<td>UIView, NSObject 등</td>
</tr>
</tbody></table>
<hr />
<h3 id="📘-참고-링크">📘 참고 링크</h3>
<ul>
<li><p>Swift 공식 문서<br /><a href="https://docs.swift.org/swift-book/documentation/the-swift-programming-language/classesandstructures/">https://docs.swift.org/swift-book/documentation/the-swift-programming-language/classesandstructures/</a></p>
</li>
<li><p>Apple API 문서 예시<br /><a href="https://developer.apple.com/documentation/swift/int">https://developer.apple.com/documentation/swift/int</a><br /><a href="https://developer.apple.com/documentation/swift/array">https://developer.apple.com/documentation/swift/array</a></p>
</li>
</ul>
<hr />
<h1 id="✅-구조체-memberwise-initializer-자동-생성">✅ 구조체: Memberwise Initializer 자동 생성</h1>
<hr />
<h3 id="📌-전체-코드-1">📌 전체 코드</h3>
<pre><code class="language-swift">// 기본값이 없는 구조체 정의
struct Resolution {
    var width: Int
    var height: Int
}

// 자동으로 생성된 Memberwise Initializer 사용
let myComputer = Resolution(width: 1920, height: 1080)
print(myComputer.width)  // 출력: 1920</code></pre>
<hr />
<h3 id="🔹-1-구조체-정의-초기값-없음">🔹 1. 구조체 정의 (초기값 없음)</h3>
<pre><code class="language-swift">struct Resolution {
    var width: Int      // 초기값이 없음
    var height: Int
}</code></pre>
<ul>
<li>프로퍼티에 기본값이 없지만,<br />Swift는 자동으로 <code>init(width: Int, height: Int)</code> 형태의 <strong>Memberwise Initializer</strong>를 생성합니다.</li>
<li>즉, 사용자가 별도로 <code>init</code>을 작성하지 않아도 객체를 생성할 수 있습니다.</li>
</ul>
<hr />
<h3 id="🔹-2-인스턴스-생성-및-프로퍼티-접근">🔹 2. 인스턴스 생성 및 프로퍼티 접근</h3>
<pre><code class="language-swift">let myComputer = Resolution(width: 1920, height: 1080)
print(myComputer.width)  // 출력: 1920</code></pre>
<ul>
<li>자동 생성된 생성자를 통해 인스턴스를 생성합니다.</li>
<li>생성된 구조체 인스턴스의 프로퍼티에 접근할 수 있습니다.</li>
</ul>
<hr />
<h3 id="⚠️-참고-직접-init을-작성하면">⚠️ 참고: 직접 init을 작성하면?</h3>
<pre><code class="language-swift">struct Resolution {
    var width: Int
    var height: Int

    // 직접 초기화 메서드를 정의하면,
    // Swift가 자동으로 제공하던 Memberwise Initializer는 사라집니다.
    init(width: Int, height: Int) {
        self.width = width
        self.height = height
    }
}</code></pre>
<ul>
<li>위처럼 <code>init</code>을 직접 작성하면 자동 생성은 <strong>비활성화</strong>됩니다.</li>
<li>사용자가 원하는 커스텀 초기화 방식을 제공하고 싶을 때 유용합니다.</li>
</ul>
<hr />
<h1 id="✅-클래스-내에-구조체-포함하기">✅ 클래스 내에 구조체 포함하기</h1>
<h3 id="📌-전체-코드-2">📌 전체 코드</h3>
<pre><code class="language-swift">struct Resolution {
    var width = 1024
    var height = 768
}

class VideoMode {
    var resolution = Resolution()
    var frameRate = 0.0
}

let myVideo = VideoMode()
print(myVideo.resolution.width)  // 출력: 1024</code></pre>
<hr />
<h3 id="🔹-1-구조체-정의">🔹 1. 구조체 정의</h3>
<pre><code class="language-swift">struct Resolution {
    var width = 1024
    var height = 768
}</code></pre>
<ul>
<li><code>Resolution</code>은 <strong>구조체(struct)</strong>로 정의되어 있으며,</li>
<li><code>width</code>, <code>height</code>라는 두 개의 저장 프로퍼티를 가지고 있습니다.</li>
<li>각각 기본값(1024, 768)을 가지고 있어 별도 초기화 없이 인스턴스 생성 가능.</li>
</ul>
<hr />
<h3 id="🔹-2-클래스-정의">🔹 2. 클래스 정의</h3>
<pre><code class="language-swift">class VideoMode {
    var resolution = Resolution()  // 구조체 인스턴스를 프로퍼티로 가짐
    var frameRate = 0.0            // 클래스 고유의 속성
}</code></pre>
<ul>
<li><code>VideoMode</code>는 <strong>클래스(class)</strong>입니다.</li>
<li>내부에 <code>Resolution</code> 구조체 타입의 프로퍼티를 가지고 있습니다.</li>
<li>즉, 클래스 안에서 구조체를 <strong>속성처럼 포함</strong>하고 있는 구조입니다.</li>
</ul>
<hr />
<h3 id="🔹-3-인스턴스-생성-및-접근">🔹 3. 인스턴스 생성 및 접근</h3>
<pre><code class="language-swift">let myVideo = VideoMode()
print(myVideo.resolution.width)  // 출력: 1024</code></pre>
<ul>
<li><code>myVideo</code>는 <code>VideoMode</code> 클래스의 인스턴스입니다.</li>
<li><code>resolution</code> 프로퍼티는 구조체 타입이므로, 구조체 내부의 <code>width</code>에 접근 가능합니다.</li>
<li><strong>점(.)을 통해 중첩된 구조체의 속성에도 접근 가능</strong>합니다.</li>
</ul>
<hr />
<h3 id="🧭-구조-시각화-설명-이미지-참고">🧭 구조 시각화 설명 (이미지 참고)</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/99983e3a-5b7c-468e-a7e4-bd6dd3440162/image.png" /></p>
<ul>
<li><code>VideoMode</code> 클래스 인스턴스 내부에 <code>resolution</code>이라는 구조체 인스턴스가 포함되어 있고,</li>
<li><code>resolution</code> 안에 다시 <code>width</code>, <code>height</code>가 들어 있습니다.</li>
<li>→ <code>myVideo.resolution.width</code> 로 단계적으로 접근하는 구조입니다.</li>
</ul>
<hr />
<h1 id="✅-swift에서-클래스와-구조체의-선택-기준">✅ Swift에서 클래스와 구조체의 선택 기준</h1>
<table>
<thead>
<tr>
<th>기준</th>
<th>구조체(<code>struct</code>) 사용</th>
<th>클래스(<code>class</code>) 사용</th>
</tr>
</thead>
<tbody><tr>
<td><strong>타입 특성</strong></td>
<td>값 타입 (copy)</td>
<td>참조 타입 (reference)</td>
</tr>
<tr>
<td><strong>복사 시 동작</strong></td>
<td>독립된 복사본 생성</td>
<td>동일한 인스턴스를 공유</td>
</tr>
<tr>
<td><strong>상속</strong></td>
<td>❌ 불가능</td>
<td>✅ 가능</td>
</tr>
<tr>
<td><strong>deinit 사용 여부</strong></td>
<td>❌ 불가</td>
<td>✅ 가능</td>
</tr>
<tr>
<td><strong>필요한 기능</strong></td>
<td>단순한 데이터 저장</td>
<td>객체 간 공유, 상속, 참조 필요</td>
</tr>
<tr>
<td><strong>예시</strong></td>
<td>좌표, 크기, RGB, 모델 데이터</td>
<td>네트워크 매니저, 뷰컨트롤러, 앱 상태 관리 등</td>
</tr>
</tbody></table>
<hr />
<h2 id="🔹-구조체struct를-사용하는-경우">🔹 구조체(struct)를 사용하는 경우</h2>
<blockquote>
<p>✅ 복사되더라도 독립적으로 다뤄야 하는 <strong>단순한 데이터 값</strong>일 때 사용합니다.</p>
</blockquote>
<h3 id="✔-사용-예시">✔ 사용 예시</h3>
<ul>
<li>좌표(Point), 크기(Size), 범위(Rect)</li>
<li>날짜(Date), 색상(Color)</li>
<li>모델 데이터 (User, Product 등)</li>
<li>값이 변경되더라도 <strong>원본에 영향을 주지 않아야 하는 경우</strong></li>
</ul>
<h3 id="✔-예제">✔ 예제</h3>
<pre><code class="language-swift">struct Point {
    var x: Int
    var y: Int
}

var p1 = Point(x: 10, y: 20)
var p2 = p1
p2.x = 100

print(p1.x)  // 10 (원본에 영향 없음)</code></pre>
<hr />
<h2 id="🔹-클래스를-사용하는-경우">🔹 클래스를 사용하는 경우</h2>
<blockquote>
<p>✅ 여러 곳에서 <strong>동일한 인스턴스를 참조</strong>하거나, <strong>상속</strong>이 필요한 경우 사용합니다.</p>
</blockquote>
<h3 id="✔-사용-예시-1">✔ 사용 예시</h3>
<ul>
<li>뷰 컨트롤러, 네트워크 매니저, 싱글톤</li>
<li>상태를 공유해야 하는 객체</li>
<li>부모-자식 관계(상속)가 필요한 경우</li>
</ul>
<h3 id="✔-예제-1">✔ 예제</h3>
<pre><code class="language-swift">class VideoMode {
    var frameRate: Double = 0.0
}

let vm1 = VideoMode()
let vm2 = vm1
vm2.frameRate = 30.0

print(vm1.frameRate)  // 30.0 (같은 인스턴스 참조)</code></pre>
<hr />
<h2 id="🔸-추가-기준-요약">🔸 추가 기준 요약</h2>
<ul>
<li><strong>작고 단순한 데이터 묶음</strong>이면 → <code>struct</code></li>
<li><strong>동작과 상태를 함께 다루는 객체</strong>이면 → <code>class</code></li>
<li><strong>상속이 필요하거나</strong>, <strong>객체 간 참조가 필요</strong>하면 → <code>class</code></li>
<li><strong>thread-safe하게 설계하고 싶다면</strong> → <code>struct</code> (값 타입이 복사되므로 동시성에 유리)</li>
</ul>
<hr />
<h2 id="✅-정리-한-줄-요약">✅ 정리 한 줄 요약</h2>
<blockquote>
<p><strong>값을 복사해도 되는 단순한 데이터</strong> → 구조체<br /><strong>객체 간 공유·상속·참조가 필요한 경우</strong> → 클래스</p>
</blockquote>
<hr />
<h1 id="✅-클래스class와-구조체struct의-공통점">✅ 클래스(class)와 구조체(struct)의 공통점</h1>
<p>Swift에서 <code>class</code>와 <code>struct</code>는 많은 기능을 <strong>공통적으로 제공</strong>하며, 대부분 비슷하게 사용할 수 있습니다.</p>
<hr />
<h3 id="📌-공통적으로-가능한-기능">📌 공통적으로 가능한 기능</h3>
<table>
<thead>
<tr>
<th>기능</th>
<th>설명</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td>프로퍼티 정의</td>
<td>값을 저장하기 위한 변수/상수 정의</td>
<td><code>var name: String</code></td>
</tr>
<tr>
<td>메서드 정의</td>
<td>기능을 구현하는 함수 정의</td>
<td><code>func greet() {}</code></td>
</tr>
<tr>
<td>서브스크립트 정의</td>
<td>배열처럼 <code>[]</code>로 내부 값에 접근</td>
<td><code>subscript(index: Int) -&gt; String</code></td>
</tr>
<tr>
<td>초기화 함수 정의</td>
<td>인스턴스를 생성할 때 초기값 설정</td>
<td><code>init(name: String)</code></td>
</tr>
<tr>
<td>확장 (extension)</td>
<td>기존 타입에 기능 추가</td>
<td><code>extension Double {}</code></td>
</tr>
<tr>
<td>프로토콜 채택</td>
<td>특정 기능을 따르도록 구현</td>
<td><code>struct A: CustomStringConvertible</code></td>
</tr>
</tbody></table>
<hr />
<h3 id="🔹-1-프로퍼티-정의">🔹 1. 프로퍼티 정의</h3>
<pre><code class="language-swift">struct PersonStruct {
    var name: String
}

class PersonClass {
    var name: String = &quot;&quot;
}</code></pre>
<hr />
<h3 id="🔹-2-메서드-정의">🔹 2. 메서드 정의</h3>
<pre><code class="language-swift">struct PersonStruct {
    var name: String
    func sayHello() {
        print(&quot;안녕하세요, \(name)입니다.&quot;)
    }
}

class PersonClass {
    var name: String = &quot;&quot;
    func sayHello() {
        print(&quot;안녕하세요, \(name)입니다.&quot;)
    }
}</code></pre>
<hr />
<h3 id="🔹-3-서브스크립트-정의">🔹 3. 서브스크립트 정의</h3>
<pre><code class="language-swift">struct MyList {
    var data = [1, 2, 3]

    subscript(index: Int) -&gt; Int {
        return data[index]
    }
}

let list = MyList()
print(list[0])  // 1</code></pre>
<blockquote>
<p><code>class</code>도 동일한 방식으로 <code>subscript</code> 정의 가능</p>
</blockquote>
<hr />
<h3 id="🔹-4-초기화-함수-initializer">🔹 4. 초기화 함수 (Initializer)</h3>
<pre><code class="language-swift">struct UserStruct {
    var name: String
    init(name: String) {
        self.name = name
    }
}

class UserClass {
    var name: String
    init(name: String) {
        self.name = name
    }
}</code></pre>
<hr />
<h3 id="🔹-5-extension-기능-확장">🔹 5. extension (기능 확장)</h3>
<pre><code class="language-swift">extension Double {
    var squared: Double {
        return self * self
    }
}

let num: Double = 3.0
print(num.squared)  // 9.0</code></pre>
<hr />
<h3 id="🔹-6-프로토콜-채택">🔹 6. 프로토콜 채택</h3>
<pre><code class="language-swift">protocol Runnable {
    func run()
}

class Man: Runnable {
    func run() {
        print(&quot;뛰는 중입니다.&quot;)
    }
}

struct Woman: Runnable {
    func run() {
        print(&quot;달리는 중입니다.&quot;)
    }
}</code></pre>
<hr />
<h1 id="✅-클래스class가-구조체struct보다-더-갖는-특징">✅ 클래스(class)가 구조체(struct)보다 더 갖는 특징</h1>
<p>구조체와 대부분의 기능을 공유하는 클래스지만, 클래스만이 가지는 기능도 있습니다.</p>
<hr />
<h3 id="span-stylecolorred🔹-1-상속-inheritancespan"><span style="color: red;">🔹 1. 상속 (Inheritance)</span></h3>
<pre><code class="language-swift">class Animal {
    func sound() {
        print(&quot;동물 소리&quot;)
    }
}

class Dog: Animal {
    override func sound() {
        print(&quot;멍멍&quot;)
    }
}

let dog = Dog()
dog.sound()  // 출력: 멍멍</code></pre>
<blockquote>
<p>구조체는 상속이 불가능하지만, 클래스는 다른 클래스를 <strong>상속</strong>할 수 있어 <strong>코드 재사용과 계층화</strong>에 유리합니다.</p>
</blockquote>
<hr />
<h3 id="🔹-2-타입-캐스팅-type-casting">🔹 2. 타입 캐스팅 (Type Casting)</h3>
<pre><code class="language-swift">class Animal {}
class Cat: Animal {}

let pet: Animal = Cat()

if pet is Cat {
    print(&quot;이 객체는 Cat 타입입니다.&quot;)
}

if let myCat = pet as? Cat {
    print(&quot;다운캐스팅 성공&quot;)
}</code></pre>
<blockquote>
<p>클래스는 <strong>런타임에 타입을 확인하고 변환</strong>(is, as, as?, as!)할 수 있습니다.<br />구조체는 상속이 없기 때문에 이런 캐스팅이 필요하지 않거나 불가능합니다.</p>
</blockquote>
<hr />
<h3 id="🔹-3-소멸자-deinitializer">🔹 3. 소멸자 (Deinitializer)</h3>
<pre><code class="language-swift">class FileManager {
    init() {
        print(&quot;파일 열기&quot;)
    }

    deinit {
        print(&quot;파일 닫기&quot;)
    }
}

var file: FileManager? = FileManager()
file = nil  // 출력: 파일 닫기</code></pre>
<blockquote>
<p>클래스는 인스턴스가 메모리에서 해제될 때 실행되는 <strong><code>deinit {}</code></strong> 소멸자를 정의할 수 있습니다.<br />구조체는 값 타입이라 <code>deinit</code>이 없습니다.</p>
</blockquote>
<hr />
<h3 id="🔹-4-참조-카운팅-reference-counting">🔹 4. 참조 카운팅 (Reference Counting)</h3>
<pre><code class="language-swift">class Person {
    var name: String
    init(name: String) { self.name = name }
}

let a = Person(name: &quot;A&quot;)
let b = a
b.name = &quot;B&quot;

print(a.name)  // 출력: B (같은 인스턴스를 참조)</code></pre>
<blockquote>
<p>클래스는 <strong>같은 인스턴스를 여러 변수에서 참조</strong>할 수 있으며,<br />Swift는 <strong>ARC(Automatic Reference Counting)</strong>을 통해 메모리 관리를 합니다.</p>
</blockquote>
<hr />
<h2 id="🧾-클래스만-가능한-기능-요약">🧾 클래스만 가능한 기능 요약</h2>
<table>
<thead>
<tr>
<th>기능</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>상속</td>
<td>다른 클래스를 상속받아 기능 확장 가능</td>
</tr>
<tr>
<td>타입 캐스팅</td>
<td>is, as, as?, as! 등을 통한 타입 확인/변환</td>
</tr>
<tr>
<td>deinit</td>
<td>메모리 해제 직전에 호출되는 소멸자 정의 가능</td>
</tr>
<tr>
<td>참조 카운팅</td>
<td>여러 참조 변수가 같은 인스턴스를 공유</td>
</tr>
</tbody></table>
<hr />
<h1 id="✅-클래스와-구조체-정의하기">✅ 클래스와 구조체 정의하기</h1>
<h3 id="📌-전체-코드-3">📌 전체 코드</h3>
<pre><code class="language-swift">struct Resolution {
    var width = 0
    var height = 0
}

class VideoMode {
    var resolution = Resolution()
    var interlaced = false
    var frameRate = 0.0
    var name: String?
}</code></pre>
<hr />
<h3 id="🔹-1-구조체-정의-1">🔹 1. 구조체 정의</h3>
<pre><code class="language-swift">struct Resolution {
    var width = 0
    var height = 0
}</code></pre>
<ul>
<li><code>struct</code> 키워드를 사용해 구조체를 정의합니다.</li>
<li>프로퍼티 이름은 <code>lowerCamelCase</code> 방식으로 작성합니다.<br />→ 예: <code>width</code>, <code>height</code></li>
<li>타입 이름은 <code>UpperCamelCase</code>로 작성합니다.<br />→ 예: <code>Resolution</code></li>
</ul>
<hr />
<h3 id="🔹-2-클래스-정의-1">🔹 2. 클래스 정의</h3>
<pre><code class="language-swift">class VideoMode {
    var resolution = Resolution()
    var interlaced = false
    var frameRate = 0.0
    var name: String?
}</code></pre>
<ul>
<li><code>class</code> 키워드를 사용해 클래스를 정의합니다.</li>
<li>클래스 내부에 <code>Resolution</code> 구조체를 포함시켜 사용합니다.</li>
<li><code>interlaced</code>, <code>frameRate</code>, <code>name</code> 등 프로퍼티들도 <strong>lowerCamelCase</strong>로 작성합니다.</li>
</ul>
<hr />
<h3 id="📌-swift의-명명-규칙camel-case">📌 Swift의 명명 규칙(Camel Case)</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th>규칙</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td><strong>타입 이름 (클래스, 구조체, 열거형)</strong></td>
<td><code>UpperCamelCase</code></td>
<td><code>VideoMode</code>, <code>Resolution</code>, <code>UserProfile</code></td>
</tr>
<tr>
<td><strong>프로퍼티, 메서드, 변수 이름</strong></td>
<td><code>lowerCamelCase</code></td>
<td><code>frameRate</code>, <code>userName</code>, <code>calculateSize()</code></td>
</tr>
</tbody></table>
<hr />
<h1 id="✅-구조체는-값-타입-클래스는-참조-타입">✅ 구조체는 값 타입, 클래스는 참조 타입</h1>
<h3 id="📌-전체-코드-비교">📌 전체 코드 비교</h3>
<h4 id="🔷-구조체-값-타입">🔷 구조체 (값 타입)</h4>
<pre><code class="language-swift">struct Human {
    var age: Int = 1
}

var kim = Human()
var lee = kim  // 복사됨 (값 타입)
print(kim.age, lee.age)  // 1 1

lee.age = 20
print(kim.age, lee.age)  // 1 20

kim.age = 30
print(kim.age, lee.age)  // 30 20</code></pre>
<h4 id="🔶-클래스-참조-타입">🔶 클래스 (참조 타입)</h4>
<pre><code class="language-swift">class Human {
    var age: Int = 1
}

var kim = Human()
var lee = kim  // 같은 인스턴스를 참조 (참조 타입)
print(kim.age, lee.age)  // 1 1

lee.age = 20
print(kim.age, lee.age)  // 20 20

kim.age = 30
print(kim.age, lee.age)  // 30 30</code></pre>
<hr />
<h2 id="✅-1-구조체-struct는-값-타입">✅ 1. 구조체 (<code>struct</code>)는 값 타입</h2>
<pre><code class="language-swift">struct Human {
    var age: Int = 1
}

var kim = Human()
var lee = kim // 값 복사</code></pre>
<ul>
<li><code>kim</code>과 <code>lee</code>는 <strong>서로 다른 인스턴스</strong>입니다.</li>
<li>구조체는 <strong>값 타입(value type)</strong>이라 복사할 때 <strong>새로운 데이터가 하나 더 생깁니다.</strong></li>
</ul>
<hr />
<pre><code class="language-swift">print(kim.age, lee.age)  // 1 1
lee.age = 20
print(kim.age, lee.age)  // 1 20
kim.age = 30
print(kim.age, lee.age)  // 30 20</code></pre>
<ul>
<li><code>lee.age</code>를 바꿔도 <code>kim.age</code>에는 영향이 없습니다.</li>
<li><code>kim</code>과 <code>lee</code>는 서로 <strong>독립적으로 존재</strong>합니다.</li>
</ul>
<hr />
<pre><code class="language-swift">var x = 1
var y = x
print(x, y)  // 1 1
x = 2
print(x, y)  // 2 1
y = 3
print(x, y)  // 2 3</code></pre>
<ul>
<li><code>Int</code> 타입도 구조체이기 때문에 역시 <strong>값 타입</strong>입니다.</li>
<li>복사한 변수들은 서로 영향을 주지 않습니다.</li>
</ul>
<blockquote>
<p>✅ <strong>값 타입 요약</strong><br />→ 복사 시 새 인스턴스 생성<br />→ 변경해도 원본에 영향 없음</p>
</blockquote>
<hr />
<h2 id="✅-2-클래스-class는-참조-타입">✅ 2. 클래스 (<code>class</code>)는 참조 타입</h2>
<pre><code class="language-swift">class Human {
    var age: Int = 1
}

var kim = Human()
var lee = kim // 같은 객체를 참조</code></pre>
<ul>
<li><code>kim</code>과 <code>lee</code>는 <strong>같은 인스턴스를 공유</strong>합니다.</li>
<li>클래스는 <strong>참조 타입(reference type)</strong>이므로, 복사해도 <strong>주소만 복사</strong>됩니다.</li>
</ul>
<hr />
<pre><code class="language-swift">print(kim.age, lee.age)  // 1 1
lee.age = 20
print(kim.age, lee.age)  // 20 20
kim.age = 30
print(kim.age, lee.age)  // 30 30</code></pre>
<ul>
<li><code>kim</code>과 <code>lee</code>가 <strong>같은 객체를 참조</strong>하기 때문에, 한쪽을 수정하면 다른 쪽도 바뀝니다.</li>
</ul>
<blockquote>
<p>✅ <strong>참조 타입 요약</strong><br />→ 복사 시 주소만 복사됨<br />→ 변경 시 모든 참조에 영향 있음</p>
</blockquote>
<hr />
<h2 id="🔍-핵심-비교-요약">🔍 핵심 비교 요약</h2>
<table>
<thead>
<tr>
<th>항목</th>
<th>구조체 (<code>struct</code>)</th>
<th>클래스 (<code>class</code>)</th>
</tr>
</thead>
<tbody><tr>
<td>타입</td>
<td>값 타입 (Value Type)</td>
<td>참조 타입 (Reference Type)</td>
</tr>
<tr>
<td>복사 시</td>
<td>값이 복사됨</td>
<td>참조(주소)가 복사됨</td>
</tr>
<tr>
<td>독립성</td>
<td>서로 영향 없음</td>
<td>모두 같은 객체 공유</td>
</tr>
<tr>
<td>메모리</td>
<td>스택</td>
<td>힙 (ARC 적용)</td>
</tr>
</tbody></table>
<hr />
<h1 id="✅-구조체는-값-타입-클래스는-참조-타입-2">✅ 구조체는 값 타입, 클래스는 참조 타입 2</h1>
<hr />
<h3 id="📌-전체-코드-4">📌 전체 코드</h3>
<pre><code class="language-swift">struct Resolution {
    var width = 0
    var height = 0
}

class VideoMode {
    var resolution = Resolution()
    var frameRate = 0
    var name: String?
}

var hd = Resolution(width: 1920, height: 1080)
// 자동 Memberwise Initializer 사용

var highDef = hd
// 구조체는 값 타입 → 복사본 생성

print(hd.width, highDef.width)  // 1920 1920

hd.width = 1024
print(hd.width, highDef.width)  // 1024 1920

var xMonitor = VideoMode()
xMonitor.resolution = hd
xMonitor.name = &quot;LG&quot;
xMonitor.frameRate = 30
print(xMonitor.frameRate)       // 30

var yMonitor = xMonitor
// 클래스는 참조 타입 → 같은 인스턴스 공유

yMonitor.frameRate = 25
print(yMonitor.frameRate)       // 25
print(xMonitor.frameRate)       // 25</code></pre>
<hr />
<h3 id="🔹-1-구조체-정의-및-값-타입-확인">🔹 1. 구조체 정의 및 값 타입 확인</h3>
<pre><code class="language-swift">struct Resolution {
    var width = 0
    var height = 0
}

var hd = Resolution(width: 1920, height: 1080)
var highDef = hd</code></pre>
<ul>
<li><code>Resolution</code>은 구조체이므로 <strong>값 타입</strong>입니다.</li>
<li><code>hd</code>를 <code>highDef</code>에 대입하면 <strong>값 자체가 복사</strong>됩니다.</li>
</ul>
<pre><code class="language-swift">hd.width = 1024
print(hd.width, highDef.width)  // 1024 1920</code></pre>
<ul>
<li><code>hd</code>를 변경해도 <code>highDef</code>에는 <strong>영향 없음</strong>  </li>
<li>값 타입은 복사되면 <strong>서로 완전히 다른 인스턴스</strong>가 됨</li>
</ul>
<hr />
<h3 id="🔹-2-클래스-정의-및-참조-타입-확인">🔹 2. 클래스 정의 및 참조 타입 확인</h3>
<pre><code class="language-swift">class VideoMode {
    var resolution = Resolution()
    var frameRate = 0
    var name: String?
}</code></pre>
<ul>
<li><code>VideoMode</code>는 클래스이므로 <strong>참조 타입</strong>입니다.</li>
</ul>
<pre><code class="language-swift">var xMonitor = VideoMode()
xMonitor.resolution = hd
xMonitor.name = &quot;LG&quot;
xMonitor.frameRate = 30</code></pre>
<ul>
<li>클래스 인스턴스를 생성하여 속성값을 설정합니다.</li>
</ul>
<hr />
<h3 id="🔹-3-참조-복사-확인">🔹 3. 참조 복사 확인</h3>
<pre><code class="language-swift">var yMonitor = xMonitor
yMonitor.frameRate = 25
print(yMonitor.frameRate)       // 25
print(xMonitor.frameRate)       // 25</code></pre>
<ul>
<li><code>yMonitor</code>는 <code>xMonitor</code>를 <strong>참조</strong>하므로<br />둘은 <strong>같은 인스턴스를 공유</strong>합니다.</li>
<li>따라서 <code>yMonitor.frameRate</code>를 변경하면<br /><code>xMonitor.frameRate</code>도 함께 변경됩니다.</li>
</ul>
<hr />
<h3 id="✅-요약-정리">✅ 요약 정리</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>구조체 (<code>struct</code>)</th>
<th>클래스 (<code>class</code>)</th>
</tr>
</thead>
<tbody><tr>
<td>타입</td>
<td>값 타입 (value type)</td>
<td>참조 타입 (reference type)</td>
</tr>
<tr>
<td>복사 시</td>
<td>새로운 인스턴스 생성</td>
<td>같은 인스턴스를 가리킴</td>
</tr>
<tr>
<td>예시</td>
<td><code>Resolution</code></td>
<td><code>VideoMode</code></td>
</tr>
<tr>
<td>특징</td>
<td>복사해도 독립적</td>
<td>수정 시 다른 참조에도 영향</td>
</tr>
</tbody></table>
<hr />
<h1 id="✅-언제-클래스를-쓰고-언제-구조체를-쓰나">✅ 언제 클래스를 쓰고, 언제 구조체를 쓰나?</h1>
<h3 id="📌-기본-차이">📌 기본 차이</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th>클래스 (<code>class</code>)</th>
<th>구조체 (<code>struct</code>)</th>
</tr>
</thead>
<tbody><tr>
<td>타입</td>
<td>참조 타입 (reference)</td>
<td>값 타입 (value)</td>
</tr>
<tr>
<td>복사 시</td>
<td>주소 복사 (공유됨)</td>
<td>값 복사 (독립적)</td>
</tr>
<tr>
<td>상속</td>
<td>가능</td>
<td>불가능</td>
</tr>
<tr>
<td><code>deinit</code> 사용</td>
<td>가능</td>
<td>불가능</td>
</tr>
<tr>
<td>쓰레드 안전성</td>
<td>낮음</td>
<td>높음 (복사되므로)</td>
</tr>
</tbody></table>
<hr />
<h3 id="🔹-구조체를-사용하는-경우">🔹 구조체를 사용하는 경우</h3>
<blockquote>
<p>💡 구조체는 값 타입이라 <strong>복사 안전성</strong>, <strong>간결한 데이터 표현</strong>에 적합합니다.</p>
</blockquote>
<h4 id="✅-구조체-사용이-적절한-상황">✅ 구조체 사용이 적절한 상황</h4>
<ul>
<li>간단한 데이터 묶음</li>
<li>크기가 작고, 자주 복사해도 부담이 없는 경우</li>
<li>여러 스레드에서 동시에 사용할 수 있도록 안정성이 필요한 경우</li>
<li>상속이 필요 없는 경우</li>
</ul>
<h4 id="🟨-대표-예시">🟨 대표 예시</h4>
<ul>
<li>기하학적 정보: <code>CGSize</code>, <code>CGRect</code>, <code>CGPoint</code></li>
<li>순열 정보: 시작값, 증분, 길이 등</li>
<li>3차원 좌표: <code>x</code>, <code>y</code>, <code>z</code></li>
<li>사용자 정보, 설정 값, 데이터 모델 등</li>
</ul>
<pre><code class="language-swift">struct Size {
    var width: Int
    var height: Int
}</code></pre>
<hr />
<h3 id="🔹-클래스를-사용하는-경우-1">🔹 클래스를 사용하는 경우</h3>
<blockquote>
<p>💡 클래스는 참조 타입이라 <strong>객체 간 상태 공유</strong>, <strong>상속</strong>이 필요한 경우에 적합합니다.</p>
</blockquote>
<h4 id="✅-클래스-사용이-적절한-상황">✅ 클래스 사용이 적절한 상황</h4>
<ul>
<li>인스턴스를 여러 곳에서 참조해야 함</li>
<li>상속과 다형성이 필요한 경우</li>
<li>한 객체를 여러 객체가 함께 사용해야 하는 경우</li>
<li>메모리 관리를 참조 카운트(ARC)로 하고 싶은 경우</li>
</ul>
<h4 id="🟨-대표-예시-1">🟨 대표 예시</h4>
<ul>
<li>뷰 컨트롤러 (UIViewController)</li>
<li>싱글톤 객체 (예: Logger, UserManager)</li>
<li>네트워크 통신 관리 객체</li>
<li>게임 내 캐릭터 객체 등</li>
</ul>
<pre><code class="language-swift">class VideoPlayer {
    var resolution: Size
    var isPlaying: Bool = false

    init(resolution: Size) {
        self.resolution = resolution
    }
}</code></pre>
<hr />
<h3 id="✅-핵심-정리">✅ 핵심 정리</h3>
<table>
<thead>
<tr>
<th>상황</th>
<th>선택</th>
</tr>
</thead>
<tbody><tr>
<td>상속이 필요하다</td>
<td><code>class</code></td>
</tr>
<tr>
<td>값이 복사되도 독립적으로 유지돼야 한다</td>
<td><code>struct</code></td>
</tr>
<tr>
<td>여러 객체가 동일한 데이터를 공유해야 한다</td>
<td><code>class</code></td>
</tr>
<tr>
<td>데이터 단위가 작고, 단순 저장용일 때</td>
<td><code>struct</code></td>
</tr>
<tr>
<td>멀티스레드 환경에서 안정성이 중요하다</td>
<td><code>struct</code></td>
</tr>
</tbody></table>
<hr />
<h1 id="✅-extension-확장">✅ <code>extension</code> (확장)</h1>
<h3 id="📌-개념-요약">📌 개념 요약</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>정의</td>
<td>기존 타입에 <strong>새로운 기능을 추가</strong>하는 문법</td>
</tr>
<tr>
<td>적용 대상</td>
<td>클래스(class), 구조체(struct), 열거형(enum), 프로토콜(protocol)</td>
</tr>
<tr>
<td>주요 용도</td>
<td>메서드, 계산 프로퍼티, 이니셜라이저, 서브스크립트 등 확장</td>
</tr>
<tr>
<td>장점</td>
<td>원본 타입을 수정하지 않고 기능을 추가할 수 있음</td>
</tr>
<tr>
<td>활용 예</td>
<td>Swift 기본 타입(Int, String 등)이나 iOS 내장 클래스에 기능 추가 시 유용</td>
</tr>
</tbody></table>
<hr />
<h3 id="🔹-기본-문법">🔹 기본 문법</h3>
<pre><code class="language-swift">extension 기존타입이름 {
    // 새로운 기능 추가
}</code></pre>
<hr />
<h3 id="🔸-예제-1-int-타입에-기능-추가">🔸 예제 1: <code>Int</code> 타입에 기능 추가</h3>
<pre><code class="language-swift">extension Int {
    var squared: Int {
        return self * self
    }

    func isEven() -&gt; Bool {
        return self % 2 == 0
    }
}

let number = 4
print(number.squared)  // 출력: 16
print(number.isEven()) // 출력: true</code></pre>
<ul>
<li>기존의 <code>Int</code> 타입에 <code>squared</code> 계산 프로퍼티와 <code>isEven()</code> 메서드를 추가</li>
<li><code>extension</code>을 통해 기본 타입도 자유롭게 확장 가능</li>
</ul>
<hr />
<h3 id="🔸-예제-2-string-타입에-확장">🔸 예제 2: <code>String</code> 타입에 확장</h3>
<pre><code class="language-swift">extension String {
    var isNotEmpty: Bool {
        return !self.isEmpty
    }
}

let text = &quot;Swift&quot;
print(text.isNotEmpty)  // true</code></pre>
<hr />
<h3 id="🔸-예제-3-구조체-확장">🔸 예제 3: 구조체 확장</h3>
<pre><code class="language-swift">struct Point {
    var x: Int
    var y: Int
}

extension Point {
    func distanceFromOrigin() -&gt; Double {
        return sqrt(Double(x * x + y * y))
    }
}

let p = Point(x: 3, y: 4)
print(p.distanceFromOrigin())  // 5.0</code></pre>
<hr />
<h2 id="✅-언제-쓰면-좋은가">✅ 언제 쓰면 좋은가?</h2>
<ul>
<li>외부 라이브러리나 내장 타입을 수정할 수 없을 때</li>
<li>관련 기능을 분리하여 코드 가독성 향상</li>
<li>SwiftUI, UIKit에서 UIKit 컴포넌트 확장 시 자주 사용</li>
</ul>
<hr />
<h2 id="✅-요약-1">✅ 요약</h2>
<table>
<thead>
<tr>
<th>장점</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td>✅ 코드 수정 없이 기능 추가</td>
<td>원본 타입을 그대로 두고 새로운 기능만 추가 가능</td>
</tr>
<tr>
<td>✅ 기본 타입에도 적용 가능</td>
<td>Int, String 등도 확장 가능</td>
</tr>
<tr>
<td>✅ 유지보수 용이</td>
<td>기능별로 코드 분리 가능</td>
</tr>
<tr>
<td>✅ 프레임워크 활용에 유리</td>
<td>UIKit, SwiftUI 확장 시 유용함</td>
</tr>
</tbody></table>
<hr />
<h1 id="✅-extension으로-double에-기능-추가">✅ <code>extension</code>으로 <code>Double</code>에 기능 추가</h1>
<hr />
<h3 id="📌-전체-코드-5">📌 전체 코드</h3>
<pre><code class="language-swift">// Double 타입 확장: 제곱 값을 반환하는 계산 프로퍼티 추가
extension Double {
    var squared: Double {
        return self * self
    }
}

// 사용 예
let myValue: Double = 3.5
print(myValue.squared)    // 출력: 12.25

// Double 리터럴에도 직접 사용 가능
print(3.5.squared)        // 출력: 12.25

// Double의 내장 인스턴스 프로퍼티 확인
print(myValue.isZero)     // 출력: false</code></pre>
<hr />
<h3 id="🔹-1-extension으로-프로퍼티-추가">🔹 1. <code>extension</code>으로 프로퍼티 추가</h3>
<pre><code class="language-swift">extension Double {
    var squared: Double {
        return self * self
    }
}</code></pre>
<ul>
<li><code>Double</code> 구조체에 <code>squared</code>라는 <strong>계산 프로퍼티(computed property)</strong>를 추가합니다.</li>
<li><code>self</code>는 해당 인스턴스를 가리킵니다.</li>
<li><code>self * self</code>는 자기 자신을 제곱한 값입니다.</li>
</ul>
<hr />
<h3 id="🔹-2-인스턴스를-이용한-사용">🔹 2. 인스턴스를 이용한 사용</h3>
<pre><code class="language-swift">let myValue: Double = 3.5
print(myValue.squared)  // 12.25</code></pre>
<ul>
<li>확장한 <code>squared</code> 프로퍼티를 <code>Double</code> 타입 변수에서 사용 가능</li>
</ul>
<hr />
<h3 id="🔹-3-리터럴로도-사용-가능">🔹 3. 리터럴로도 사용 가능</h3>
<pre><code class="language-swift">print(3.5.squared)  // 12.25</code></pre>
<ul>
<li><code>Double</code>은 값 타입이므로 <strong>리터럴.프로퍼티</strong> 형태로도 바로 사용 가능</li>
</ul>
<hr />
<h3 id="🔹-4-내장-인스턴스-프로퍼티-iszero">🔹 4. 내장 인스턴스 프로퍼티: <code>.isZero</code></h3>
<pre><code class="language-swift">print(myValue.isZero)  // false</code></pre>
<ul>
<li><code>Double</code>의 내장 프로퍼티 <code>.isZero</code>는 값이 정확히 <code>0.0</code>일 때 <code>true</code>를 반환</li>
<li>여기서는 <code>3.5</code>이므로 <strong><code>false</code>가 출력</strong></li>
</ul>
<hr />
<h2 id="✅-참고-요약">✅ 참고 요약</h2>
<table>
<thead>
<tr>
<th>코드</th>
<th>결과</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>3.5.squared</code></td>
<td><code>12.25</code></td>
<td>확장한 계산 프로퍼티</td>
</tr>
<tr>
<td><code>myValue.isZero</code></td>
<td><code>false</code></td>
<td>Double의 내장 프로퍼티</td>
</tr>
</tbody></table>
<hr />
<h1 id="✅-swift-주요-키워드-사용-시점-요약">=✅ Swift 주요 키워드 사용 시점 요약</h1>
<table>
<thead>
<tr>
<th>키워드</th>
<th>용도 및 사용 시점</th>
</tr>
</thead>
<tbody><tr>
<td><code>class</code></td>
<td>참조 타입이 필요할 때 / 상속이 필요할 때 / 한 인스턴스를 여러 곳에서 공유해야 할 때</td>
</tr>
<tr>
<td><code>struct</code></td>
<td>값 타입이 적절할 때 / 데이터 복사가 안전하고 명확해야 할 때 / 간단한 데이터 모델</td>
</tr>
<tr>
<td><code>enum</code></td>
<td>정해진 선택지 중 하나를 표현할 때 / 상태, 옵션, 분기 처리가 필요할 때</td>
</tr>
<tr>
<td><code>protocol</code></td>
<td>공통 인터페이스 정의 / 추상화, 다형성 구현 / 클래스와 구조체의 공통 기능 설계</td>
</tr>
<tr>
<td><code>extension</code></td>
<td>기존 타입에 기능 추가 / 외부 라이브러리 타입 확장 / 코드 분리 및 재사용성 향상</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-각-키워드별-자세한-설명과-예시">✅ 각 키워드별 자세한 설명과 예시</h2>
<hr />
<h3 id="🔹-class">🔹 <code>class</code></h3>
<blockquote>
<p><strong>참조 타입</strong>, 상속 가능, ARC 기반 메모리 관리<br /><strong>사용 시점:</strong>  </p>
</blockquote>
<ul>
<li>상속이 필요할 때  </li>
<li>여러 객체가 <strong>같은 인스턴스를 공유</strong>해야 할 때  </li>
<li>UIKit, ViewController 등 대부분 iOS 시스템 객체</li>
</ul>
<pre><code class="language-swift">class Animal {
    var name: String = &quot;&quot;
    func sound() { print(&quot;소리&quot;) }
}</code></pre>
<hr />
<h3 id="🔹-struct">🔹 <code>struct</code></h3>
<blockquote>
<p><strong>값 타입</strong>, 복사 시 독립적<br /><strong>사용 시점:</strong>  </p>
</blockquote>
<ul>
<li>데이터 자체가 중요한 경우 (위치, 크기, 모델)  </li>
<li>상태 공유가 필요 없는 경우  </li>
<li>Swift의 기본 타입(Int, Double, String 등)이 모두 구조체</li>
</ul>
<pre><code class="language-swift">struct Point {
    var x: Int
    var y: Int
}</code></pre>
<hr />
<h3 id="🔹-enum">🔹 <code>enum</code></h3>
<blockquote>
<p><strong>열거형</strong>, 가능한 값의 집합<br /><strong>사용 시점:</strong>  </p>
</blockquote>
<ul>
<li>상태나 옵션이 제한된 경우  </li>
<li><code>switch</code> 문과 함께 분기 처리에 자주 사용  </li>
<li>연관 값(associated value), 원시 값(rawValue) 가능</li>
</ul>
<pre><code class="language-swift">enum Direction {
    case north, south, east, west
}</code></pre>
<hr />
<h3 id="🔹-protocol">🔹 <code>protocol</code></h3>
<blockquote>
<p><strong>공통 기능의 규약</strong>을 정의<br /><strong>사용 시점:</strong>  </p>
</blockquote>
<ul>
<li>여러 타입에 공통 기능을 적용하고 싶을 때  </li>
<li>추상화/다형성을 활용한 설계 필요 시  </li>
<li>delegate 패턴, 의존성 주입 등에 필수</li>
</ul>
<pre><code class="language-swift">protocol Drawable {
    func draw()
}

struct Circle: Drawable {
    func draw() { print(&quot;원 그리기&quot;) }
}</code></pre>
<hr />
<h3 id="🔹-extension">🔹 <code>extension</code></h3>
<blockquote>
<p><strong>기존 타입에 기능 추가</strong><br /><strong>사용 시점:</strong>  </p>
</blockquote>
<ul>
<li>기존 타입의 소스를 수정하지 않고 기능을 확장할 때  </li>
<li>외부 프레임워크, 기본 타입(Int, String 등) 확장  </li>
<li>코드 정리, 기능 분리 목적</li>
</ul>
<pre><code class="language-swift">extension Int {
    var squared: Int {
        return self * self
    }
}

print(4.squared) // 16</code></pre>
<hr />
<h2 id="✅-정리-요약">✅ 정리 요약</h2>
<table>
<thead>
<tr>
<th>키워드</th>
<th>요약</th>
</tr>
</thead>
<tbody><tr>
<td><code>class</code></td>
<td>참조 타입, 상속/공유 필요할 때</td>
</tr>
<tr>
<td><code>struct</code></td>
<td>값 타입, 독립된 데이터 복사</td>
</tr>
<tr>
<td><code>enum</code></td>
<td>상태/선택지 표현, 분기 처리</td>
</tr>
<tr>
<td><code>protocol</code></td>
<td>공통 인터페이스 정의, 추상화</td>
</tr>
<tr>
<td><code>extension</code></td>
<td>기능 확장, 코드 분리 및 유지보수</td>
</tr>
</tbody></table>
<hr />