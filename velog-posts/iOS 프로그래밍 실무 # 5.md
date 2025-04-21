<hr />
<h1 id="protocol">Protocol</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fb883795-df59-43a1-80f0-e9b88f90be7f/image.png" /></p>
<p>정리해주신 내용을 바탕으로 <strong>Swift의 프로토콜 (protocol)</strong> 개념을 핵심만 간단하게 정리해볼게요:</p>
<hr />
<h3 id="✅-프로토콜이란">✅ 프로토콜이란?</h3>
<ul>
<li><strong>역할</strong>: 클래스, 구조체, 열거형이 <strong>특정 기능을 구현하도록 강제</strong>하는 <strong>설계도</strong></li>
<li><strong>구성</strong>: <strong>프로퍼티 및 메서드의 선언만 포함</strong>, 실제 구현은 없음</li>
<li><strong>채택(adopt)</strong>: 클래스/구조체/열거형/익스텐션에서 채택하여 구현</li>
<li><strong>타 언어와 비교</strong>:<ul>
<li>Java, C# → <code>interface</code></li>
<li>C++ → 추상 클래스 (<code>abstract base class</code>)</li>
</ul>
</li>
</ul>
<hr />
<h3 id="✅-swift에서-상속과-프로토콜-채택">✅ Swift에서 상속과 프로토콜 채택</h3>
<pre><code class="language-swift">// 단일 상속 + 다중 프로토콜 채택 가능
class 자식클래스: 부모클래스, 프로토콜1, 프로토콜2 {
    // 구현
}

// 부모 클래스 없이 프로토콜만 채택도 가능
class 어떤클래스: 프로토콜1, 프로토콜2 {
    // 구현
}

// 구조체나 열거형도 채택 가능
struct MyStruct: 프로토콜1 { }
enum MyEnum: 프로토콜2 { }
extension MyClass: 프로토콜1 { }</code></pre>
<ul>
<li><strong>상속은 오직 클래스만 가능</strong> (<code>class 자식: 부모</code>)</li>
<li><strong>프로토콜은 다중 채택 가능</strong></li>
</ul>
<hr />
<h3 id="✅-프로토콜-선언-예시">✅ 프로토콜 선언 예시</h3>
<pre><code class="language-swift">// 단독 프로토콜
protocol Drivable {
    var speed: Int { get set }
    func drive()
}

// 다중 상속(채택) 프로토콜
protocol FlyingDrivable: Drivable, CustomStringConvertible {
    func fly()
}</code></pre>
<hr />
<h3 id="✅-protocol-oriented-programmingpop">✅ Protocol Oriented Programming(POP)</h3>
<ul>
<li>구조체 중심의 Swift 철학</li>
<li><strong>프로토콜 + extension</strong> 조합으로 기본 구현 제공 → <strong>단일 상속 한계 극복</strong></li>
</ul>
<pre><code class="language-swift">protocol Greetable {
    func greet()
}

extension Greetable {
    func greet() {
        print(&quot;Hello!&quot;)
    }
}

struct Person: Greetable {}
let p = Person()
p.greet()  // &quot;Hello!&quot; 출력</code></pre>
<blockquote>
<p>Protocol은 채택한다</p>
</blockquote>
<hr />
<h1 id="uitableviewdatasource">UITableViewDataSource</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7da6ad29-d3b8-4394-9d7c-2043c193694d/image.png" /></p>
<p>이 이미지는 <code>UITableViewDataSource</code> 프로토콜의 핵심 역할과 필수 메서드 두 개를 잘 정리한 슬라이드입니다. 내용을 아래에 정리해드릴게요:</p>
<hr />
<h3 id="✅-uitableviewdatasource란">✅ <code>UITableViewDataSource</code>란?</h3>
<ul>
<li><code>UITableView</code>에 <strong>데이터를 공급하는 역할</strong>을 담당하는 프로토콜</li>
<li>필수 메서드 2개가 있으며, 이를 구현하지 않으면 테이블 뷰가 작동하지 않음</li>
</ul>
<hr />
<h3 id="✅-필수-메서드-2개">✅ 필수 메서드 2개</h3>
<ol>
<li><strong>tableView(_:numberOfRowsInSection:)</strong><pre><code class="language-swift">override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -&gt; Int {
 return items.count
}</code></pre>
</li>
</ol>
<ul>
<li>각 섹션에 표시할 <strong>행(row)</strong>의 개수 리턴</li>
<li>예: <code>items.count</code> 만큼의 셀을 표시</li>
</ul>
<ol start="2">
<li><strong>tableView(_:cellForRowAt:)</strong><pre><code class="language-swift">override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -&gt; UITableViewCell {
 let cell = tableView.dequeueReusableCell(withIdentifier: &quot;cellTypeIdentifier&quot;, for: indexPath)
 cell.textLabel?.text = &quot;Cell text&quot;
 return cell
}</code></pre>
</li>
</ol>
<ul>
<li><strong>각 행(row)</strong>에 표시할 셀(<code>UITableViewCell</code>)을 생성 및 반환</li>
<li><code>dequeueReusableCell()</code>을 통해 재사용 셀을 가져와서 성능 향상</li>
</ul>
<hr />
<h3 id="✅-선택-메서드-필수-아님">✅ 선택 메서드 (필수 아님)</h3>
<ul>
<li><strong>numberOfSections(in:)</strong><pre><code class="language-swift">override func numberOfSections(in tableView: UITableView) -&gt; Int {
  return 1
}</code></pre>
</li>
<li>섹션이 여러 개일 때 사용하며, 구현하지 않으면 기본으로 <strong>1개의 섹션</strong>이 사용됨</li>
</ul>
<hr />
<h3 id="🔗-참고-링크">🔗 참고 링크</h3>
<ul>
<li><a href="https://developer.apple.com/documentation/uikit/uitableviewdatasource">Apple 공식 문서 - UITableViewDataSource</a></li>
</ul>
<hr />
<h1 id="uitableviewdelegate">UITableViewDelegate</h1>
<h3 id="✅-uitableviewdelegate란">✅ <code>UITableViewDelegate</code>란?</h3>
<ul>
<li><code>UITableView</code>의 <strong>행동(이벤트)</strong> 및 <strong>외관</strong>을 조정하는 역할</li>
<li>선택, 편집, 셀/헤더/푸터 높이 조절 등 <strong>UI 및 UX 관련 동작 처리</strong></li>
</ul>
<hr />
<h3 id="✅-자주-사용되는-delegate-메서드-정리">✅ 자주 사용되는 Delegate 메서드 정리</h3>
<table>
<thead>
<tr>
<th>메서드 이름</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>tableView(_:willDisplay:forRowAt:)</code></td>
<td>셀이 화면에 표시되기 <strong>직전</strong> 호출 → 셀 외관 조정</td>
</tr>
<tr>
<td><code>tableView(_:didSelectRowAt:)</code></td>
<td>셀이 <strong>선택되었을 때</strong> 호출 → 클릭 이벤트 처리</td>
</tr>
<tr>
<td><code>tableView(_:heightForRowAt:)</code></td>
<td>각 셀의 <strong>높이 지정</strong> (기본은 44pt)</td>
</tr>
<tr>
<td><code>tableView(_:viewForHeaderInSection:)</code></td>
<td>섹션의 <strong>헤더 커스텀 뷰</strong> 반환</td>
</tr>
<tr>
<td><code>tableView(_:heightForHeaderInSection:)</code></td>
<td>섹션 헤더의 <strong>높이 지정</strong></td>
</tr>
<tr>
<td><code>tableView(_:viewForFooterInSection:)</code></td>
<td>섹션의 <strong>푸터 커스텀 뷰</strong> 반환</td>
</tr>
<tr>
<td><code>tableView(_:heightForFooterInSection:)</code></td>
<td>섹션 푸터의 <strong>높이 지정</strong></td>
</tr>
<tr>
<td><code>tableView(_:willBeginEditingRowAt:)</code></td>
<td>셀이 <strong>편집 모드로 진입</strong>할 때 호출</td>
</tr>
<tr>
<td><code>tableView(_:didEndEditingRowAt:)</code></td>
<td>셀의 <strong>편집이 끝났을 때</strong> 호출</td>
</tr>
</tbody></table>
<hr />
<h3 id="✅-예시-코드-기본적인-선택-처리">✅ 예시 코드 (기본적인 선택 처리)</h3>
<pre><code class="language-swift">func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    print(&quot;사용자가 \(indexPath.row)번째 셀을 선택했습니다.&quot;)
}</code></pre>
<h3 id="✅-커스텀-높이-설정-예시">✅ 커스텀 높이 설정 예시</h3>
<pre><code class="language-swift">func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -&gt; CGFloat {
    return indexPath.row == 0 ? 100 : 60  // 첫 번째 셀만 크게
}</code></pre>
<hr />
<h1 id="uiviewcontroller와-uitableviewcontroller의-상속-관계">UIViewController와 UITableViewController의 상속 관계</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/24ffbd56-e2ff-462d-a5c0-0b89c49721f0/image.png" /></p>
<p>이 이미지는 iOS에서 <strong><code>UIViewController</code>와 <code>UITableViewController</code>의 상속 관계</strong>를 시각적으로 보여주는 클래스 다이어그램입니다. 각각이 어디에 속해 있고 어떤 클래스들과 관계를 가지는지를 비교할 수 있도록 정리되어 있습니다.</p>
<hr />
<h3 id="✅-핵심-비교-요약">✅ 핵심 비교 요약</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th><code>UIViewController</code></th>
<th><code>UITableViewController</code></th>
</tr>
</thead>
<tbody><tr>
<td>상속 구조</td>
<td><code>UIResponder</code> → <code>UIViewController</code></td>
<td><code>UIViewController</code> → <code>UITableViewController</code></td>
</tr>
<tr>
<td>포함 뷰</td>
<td>커스텀 <code>UIView</code>를 사용</td>
<td>내부에 자동으로 <code>UITableView</code> 포함</td>
</tr>
<tr>
<td>용도</td>
<td>다양한 UI 구성에 사용 (범용)</td>
<td><strong>테이블 뷰 중심 화면</strong>에 특화</td>
</tr>
<tr>
<td>tableView 연결</td>
<td>수동으로 연결 필요</td>
<td>자동으로 내장됨</td>
</tr>
<tr>
<td>delegate/dataSource</td>
<td>직접 지정 필요</td>
<td>자동으로 self 지정됨</td>
</tr>
<tr>
<td>장점</td>
<td>자유로운 UI 설계</td>
<td>빠른 테이블 구현, 편리한 관리</td>
</tr>
</tbody></table>
<hr />
<h3 id="✅-이미지에-표시된-주요-클래스">✅ 이미지에 표시된 주요 클래스</h3>
<ul>
<li>🔵 <code>UIViewController</code> – 범용 컨트롤러, 다양한 화면 구성에 사용됨</li>
<li>🟡 <code>UITableViewController</code> – 테이블 뷰 전용 컨트롤러 (<code>UITableView</code>가 자동 포함됨)</li>
<li>🟡 <code>UITableView</code>, <code>UITableViewCell</code> – 테이블 뷰 구성요소</li>
<li>🔴 <code>UIView</code>, <code>UITextField</code>, <code>UIWindow</code> – UI 구성 기본 클래스</li>
</ul>
<hr />
<h3 id="✅-언제-무엇을-쓸까">✅ 언제 무엇을 쓸까?</h3>
<ul>
<li><p><strong>UITableViewController</strong></p>
<ul>
<li>단순 리스트 UI 중심 화면</li>
<li>예: 연락처 목록, 채팅방 목록 등</li>
</ul>
</li>
<li><p><strong>UIViewController</strong></p>
<ul>
<li>복잡한 UI (버튼, 텍스트필드 등 여러 뷰가 섞여 있는 경우)</li>
<li>예: 회원가입 폼, 복합 레이아웃 화면</li>
</ul>
</li>
</ul>
<hr />
<h1 id="constraints-설정">Constraints 설정</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/888a2c44-0ebd-4334-87a5-67778472437d/image.png" /></p>
<p>이 이미지는 <strong>Storyboard에서 Table View에 오토레이아웃 제약(Constraints)</strong>을 설정하는 장면입니다. 현재 Table View의 위치와 크기를 정확하게 제어하려는 의도가 보입니다. 아래에 설명 드릴게요:</p>
<hr />
<h3 id="✅-현재-상황-요약">✅ 현재 상황 요약</h3>
<ul>
<li><strong>Table View</strong>가 화면 중앙쯤에 위치</li>
<li><strong>Add New Constraints</strong> 창을 열어 제약 조건을 설정 중</li>
<li>상하좌우 마진을 모두 <strong>0</strong>으로 설정하려고 함</li>
<li><code>Width</code>, <code>Height</code>는 각각 <strong>240pt / 128pt</strong>로 설정됨</li>
<li>아직 제약 조건을 추가하려면 <strong>&quot;Add 4 Constraints&quot;</strong> 버튼 클릭 필요</li>
</ul>
<hr />
<h3 id="✅-설정되는-제약-조건">✅ 설정되는 제약 조건</h3>
<ol>
<li><p><strong>상단, 하단, 좌우 마진 = 0</strong></p>
<ul>
<li>슈퍼뷰에 TableView가 딱 맞게 붙게 됨 (사방에 고정됨)</li>
<li>하지만 현재처럼 <strong>고정된 Width, Height</strong>와 함께 설정하면 <strong>오류가 발생할 수 있음</strong></li>
</ul>
</li>
<li><p><strong>Width = 240, Height = 128</strong></p>
<ul>
<li>뷰의 크기를 고정하고자 할 때 사용</li>
</ul>
</li>
</ol>
<hr />
<h3 id="⚠️-주의-사항">⚠️ 주의 사항</h3>
<ul>
<li><strong>오류 가능성</strong>: 사방에 <code>0</code> 제약을 주면서 <strong>고정 Width, Height</strong>까지 함께 설정하면 <strong>제약 충돌(Ambiguous Layout)</strong>이 발생할 수 있습니다.<ul>
<li>왜냐하면 <strong>TableView는 크기를 자동 계산하려고 하는데</strong>, 동시에 강제로 크기를 고정하려고 하기 때문입니다.</li>
</ul>
</li>
<li>해결 방법:<ul>
<li><strong>크기 고정</strong>하고 싶다면 사방 <code>0</code> 제약은 피하거나,</li>
<li><strong>사방 0 제약만</strong> 걸고 Width/Height는 체크 해제하세요</li>
</ul>
</li>
</ul>
<hr />
<h3 id="✅-추천-구성-화면-전체에-tableview-채우고-싶을-때">✅ 추천 구성 (화면 전체에 TableView 채우고 싶을 때)</h3>
<ul>
<li>사방 <code>0</code> 제약만 설정 (<code>Width</code>, <code>Height</code> 체크 해제)</li>
<li>이렇게 하면 TableView가 <strong>전체 화면을 꽉 채우는 레이아웃</strong>이 됩니다</li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/28008da8-8ef2-414b-8ae8-04c10375ca87/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/63ae095a-0328-4e7d-9e8a-cd5d93931782/image.png" /></p>
<hr />
<h1 id="uitableviewcell">UITableViewCell</h1>
<p>이 이미지는 <code>UITableViewCell</code>의 <code>textLabel</code> 프로퍼티를 사용하려고 할 때 발생하는 <strong>deprecation(사용 중단 예정)</strong> 경고를 보여주는 Xcode 스크린샷입니다.</p>
<hr />
<h3 id="⚠️-경고-메시지-해석">⚠️ 경고 메시지 해석</h3>
<pre><code>'textLabel' will be deprecated in a future version of iOS.
Use `UIListContentConfiguration` instead.</code></pre><p>👉 즉, <strong>앞으로의 iOS 버전에서는 <code>textLabel</code> 사용이 중단될 예정</strong>이고, 대신에 <code>UIListContentConfiguration</code>을 사용하라는 뜻입니다.</p>
<hr />
<h3 id="✅-기존-방식-이제-곧-deprecated">✅ 기존 방식 (이제 곧 deprecated)</h3>
<pre><code class="language-swift">let cell = UITableViewCell(style: .default, reuseIdentifier: &quot;myCell&quot;)
cell.textLabel?.text = &quot;Hello&quot;</code></pre>
<hr />
<h3 id="✅-권장되는-새로운-방식-uilistcontentconfiguration-사용">✅ 권장되는 새로운 방식 (<code>UIListContentConfiguration</code> 사용)</h3>
<pre><code class="language-swift">var content = cell.defaultContentConfiguration()
content.text = &quot;Hello&quot;
cell.contentConfiguration = content</code></pre>
<blockquote>
<p><code>defaultContentConfiguration()</code>은 <code>.subtitle</code>, <code>.value1</code>, <code>.value2</code> 등 다양한 스타일의 기본 구성을 지원합니다.</p>
</blockquote>
<hr />
<h3 id="📌-정리">📌 정리</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>기존 방식</th>
<th>새로운 권장 방식</th>
</tr>
</thead>
<tbody><tr>
<td>사용성</td>
<td>쉬움</td>
<td>약간 번거롭지만 유연함</td>
</tr>
<tr>
<td>지원 버전</td>
<td>iOS 14 이하까지 익숙함</td>
<td>iOS 14 이상 권장</td>
</tr>
<tr>
<td>이유</td>
<td>Apple의 모던 UI 가이드에 맞춤</td>
<td>다크모드/폰트/아이콘 등 더 쉽게 커스터마이징 가능</td>
</tr>
</tbody></table>
<hr />
<h3 id="💡-tip">💡 Tip</h3>
<ul>
<li>iOS 14 이상만 지원한다면 <strong>가능한 한 <code>UIListContentConfiguration</code> 사용</strong>을 습관화하세요.</li>
<li>커스텀 셀 제작이나 셀 내 여러 요소가 필요할 경우에도 더 유용합니다.</li>
</ul>
<hr />
<h1 id="indexpathdescription">indexPath.description</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/300dd45b-a5e2-4fcb-9df8-a38c03c261e9/image.png" /></p>
<p><code>indexPath.description</code>은 Swift에서 <code>IndexPath</code> 객체를 문자열(String)로 표현해주는 <strong>디버깅용 속성</strong>입니다.</p>
<hr />
<h3 id="✅-기본-개념">✅ 기본 개념</h3>
<p><code>IndexPath</code>는 보통 <strong>섹션과 행(row)</strong>을 나타낼 때 사용합니다.</p>
<pre><code class="language-swift">func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    print(indexPath.description)
}</code></pre>
<hr />
<h3 id="✅-출력-형태-예시">✅ 출력 형태 예시</h3>
<pre><code class="language-swift">[0, 3]</code></pre>
<ul>
<li><strong>첫 번째 숫자</strong>: section 번호 (예: <code>0</code>)</li>
<li><strong>두 번째 숫자</strong>: row 번호 (예: <code>3</code>)</li>
<li>즉, <strong>0번째 섹션의 3번째 행(row)</strong> 이라는 의미입니다.</li>
</ul>
<hr />
<h3 id="✅-description은-언제-쓰이나요">✅ description은 언제 쓰이나요?</h3>
<ul>
<li>주로 <strong>디버깅 시 로그 출력</strong>에 사용됩니다.</li>
<li>실제 값으로 쓰려면 아래처럼 사용하는 게 더 명확합니다:</li>
</ul>
<pre><code class="language-swift">print(&quot;섹션: \(indexPath.section), 행: \(indexPath.row)&quot;)</code></pre>
<hr />
<h3 id="✅-참고">✅ 참고</h3>
<ul>
<li><code>IndexPath</code>는 여러 값을 포함할 수 있으나, 테이블 뷰/컬렉션 뷰에서는 일반적으로 <strong>2개 값</strong> (<code>section</code>, <code>row</code>)만 사용합니다.</li>
<li><code>description</code>은 <code>CustomStringConvertible</code> 프로토콜을 따르는 속성입니다.</li>
</ul>
<hr />
<h1 id="과제">과제</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8d7d0217-946f-40f1-a2b4-bb383ad8b150/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/77bfa20b-9af8-46ee-8cd2-ec7e0da3b35a/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/17468d0d-06ae-4017-b9f9-e58643670fde/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/198b65f1-4d38-420f-9bc6-2206707fe7a9/image.png" /></p>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ffaf4364-f8ee-4802-af3b-6b808ccaded6/image.png" /></p>
<hr />
<h1 id=""></h1>
<p>이 이미지는 <code>tableView.dequeueReusableCell(withIdentifier:for:)</code> 메서드의 공식 문서 설명을 Xcode에서 보여주는 장면입니다. 이 메서드는 <strong>UITableView에서 셀을 재사용하기 위한 핵심 메서드</strong>입니다.</p>
<hr />
<h3 id="✅-메서드-선언">✅ 메서드 선언</h3>
<pre><code class="language-swift">func dequeueReusableCell(withIdentifier identifier: String, for indexPath: IndexPath) -&gt; UITableViewCell</code></pre>
<hr />
<h3 id="✅-주요-설명-요약">✅ 주요 설명 요약</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>용도</strong></td>
<td>재사용 가능한 셀을 큐에서 꺼내거나, 없으면 새로 생성하여 반환</td>
</tr>
<tr>
<td><strong>사용 위치</strong></td>
<td>반드시 <code>tableView(_:cellForRowAt:)</code> 내부에서 사용해야 함</td>
</tr>
<tr>
<td><strong>identifier</strong></td>
<td>스토리보드나 코드에서 등록한 셀의 식별자</td>
</tr>
<tr>
<td><strong>indexPath</strong></td>
<td>현재 셀의 위치 정보 (섹션/행)</td>
</tr>
<tr>
<td><strong>반환값</strong></td>
<td><code>UITableViewCell</code> 객체 (필요 시 캐스팅 가능)</td>
</tr>
</tbody></table>
<hr />
<h3 id="✅-주의할-점">✅ 주의할 점</h3>
<ul>
<li><code>identifier</code>는 스토리보드나 코드에서 등록한 것과 <strong>정확히 일치</strong>해야 함</li>
<li>셀을 사용하기 전, 반드시 아래 중 하나를 먼저 호출해야 함:<ul>
<li><code>tableView.register(_:forCellReuseIdentifier:)</code> (코드로 등록)</li>
<li>스토리보드에서 prototype cell로 등록 후, identifier 지정</li>
</ul>
</li>
</ul>
<hr />
<h3 id="✅-예시">✅ 예시</h3>
<pre><code class="language-swift">// 1. 스토리보드에서 Prototype Cell의 Identifier를 &quot;myCell&quot;로 설정한 경우
let cell = tableView.dequeueReusableCell(withIdentifier: &quot;myCell&quot;, for: indexPath)
cell.textLabel?.text = &quot;Hello, World!&quot;
return cell</code></pre>
<hr />
<h3 id="✅-왜-이-메서드를-써야-할까">✅ 왜 이 메서드를 써야 할까?</h3>
<ul>
<li><strong>성능 최적화</strong>: 셀을 매번 새로 생성하지 않고, 기존 셀을 재사용하여 메모리 절약</li>
<li><strong>scroll 시 끊김 현상 방지</strong>: 셀이 빠르게 재사용되어 부드러운 사용자 경험 제공</li>
</ul>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c4e226ca-3a6c-48e1-abc7-5766ce7d0d89/image.png" /></p>
<pre><code class="language-swift">func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -&gt; UITableViewCell {
//        let cell = UITableViewCell(style: .subtitle, reuseIdentifier: &quot;myCell&quot;)
//        cell.textLabel?.text = foodName[indexPath.row]
//        cell.detailTextLabel?.text = descriptionA[indexPath.row]
//        cell.imageView?.image = UIImage(named: image[indexPath.row])
        let cell = tableView.dequeueReusableCell(withIdentifier: &quot;myCell&quot;, for: indexPath) as! MyTableViewCell
        cell.myLabel.text = &quot;aaa&quot;
        return cell

    }</code></pre>
<blockquote>
<p>*<em>as! *</em>
다운 캐스팅 사용</p>
</blockquote>
<hr />
<h1 id="tableviewdequeuereusablecellwithidentifierfor">tableView.dequeueReusableCell(withIdentifier:for:)</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2921b874-5740-47f5-ba66-c24163dfbc0e/image.png" /></p>
<p>좋아요! 여기서 말하는 함수는 다음과 같습니다:</p>
<pre><code class="language-swift">tableView.dequeueReusableCell(withIdentifier:for:)</code></pre>
<p>Swift에서 이 함수는 <strong>UITableView에서 셀을 효율적으로 재사용하기 위한 핵심 메서드</strong>입니다.</p>
<hr />
<h3 id="✅-함수-선언">✅ 함수 선언</h3>
<pre><code class="language-swift">func dequeueReusableCell(withIdentifier identifier: String, for indexPath: IndexPath) -&gt; UITableViewCell</code></pre>
<hr />
<h3 id="✅-주요-목적">✅ 주요 목적</h3>
<ul>
<li><strong>재사용 가능한 셀을 큐에서 꺼내와서 반환</strong></li>
<li>셀이 없다면 <strong>자동으로 새로 생성</strong></li>
</ul>
<blockquote>
<p>셀을 매번 새로 만들면 메모리 낭비가 크기 때문에, UITableView는 <strong>셀 재사용 메커니즘</strong>을 제공합니다.</p>
</blockquote>
<hr />
<h3 id="✅-사용-예">✅ 사용 예</h3>
<pre><code class="language-swift">let cell = tableView.dequeueReusableCell(withIdentifier: &quot;myCell&quot;, for: indexPath)</code></pre>
<ul>
<li><code>&quot;myCell&quot;</code>: 스토리보드나 코드에서 미리 등록한 셀의 식별자</li>
<li><code>indexPath</code>: 현재 셀의 위치 정보</li>
</ul>
<hr />
<h3 id="✅-왜-필요한가">✅ 왜 필요한가?</h3>
<table>
<thead>
<tr>
<th>이유</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>성능</td>
<td>매번 셀을 새로 생성하지 않고 재사용해서 <strong>스크롤 성능 향상</strong></td>
</tr>
<tr>
<td>메모리 절약</td>
<td>불필요한 셀 객체 생성을 줄임</td>
</tr>
<tr>
<td>깔끔한 코드</td>
<td>재사용 메커니즘에 따라 뷰 컨트롤러 코드가 간결해짐</td>
</tr>
</tbody></table>
<hr />
<h3 id="✅-주의-사항">✅ 주의 사항</h3>
<ul>
<li>반드시 <strong>식별자(identifier)</strong>와 함께 스토리보드나 코드로 셀을 <strong>사전 등록</strong>해야 합니다.</li>
</ul>
<p>예시:</p>
<pre><code class="language-swift">tableView.register(MyTableViewCell.self, forCellReuseIdentifier: &quot;myCell&quot;) // 코드 등록 시 필요</code></pre>
<p>또는 스토리보드에서:</p>
<ul>
<li>셀 선택 → Identifier에 <code>&quot;myCell&quot;</code> 입력</li>
<li>클래스 설정: <code>MyTableViewCell</code></li>
</ul>
<hr />
<h1 id="didselectrowat">didSelectRowAt</h1>
<h3 id="✅-함수-설명">✅ 함수 설명</h3>
<pre><code class="language-swift">func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    print(indexPath.description)
}</code></pre>
<ul>
<li>이 함수는 사용자가 <strong>UITableView의 셀을 클릭했을 때</strong> 호출됩니다.</li>
<li><code>indexPath</code>는 사용자가 <strong>선택한 셀의 위치 정보</strong>를 담고 있는 객체입니다.</li>
<li><code>description</code>은 해당 <code>indexPath</code>를 <strong>문자열 형태로 출력</strong>하는 프로퍼티입니다.</li>
</ul>
<hr />
<h3 id="✅-출력-예시">✅ 출력 예시</h3>
<p>만약 사용자가 <strong>0번 섹션의 2번째 행(row)</strong>을 선택했다면 콘솔에는 다음과 같이 출력됩니다:</p>
<pre><code>[0, 2]</code></pre><blockquote>
<p><code>[섹션번호, 행번호]</code> 형식입니다.</p>
</blockquote>
<hr />
<h3 id="✅-응용-예">✅ 응용 예</h3>
<p>클릭한 셀의 데이터 출력:</p>
<pre><code class="language-swift">func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    print(&quot;섹션: \(indexPath.section), 행: \(indexPath.row)&quot;)
    print(&quot;선택한 음식 이름: \(foodName[indexPath.row])&quot;)
}</code></pre>
<hr />