<hr />
<h1 id="table-view-constraints">Table View Constraints</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/eb06a4ef-c4a2-408e-96c3-9a1121c805ce/image.png" /></p>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/45ecda17-e4ab-489f-b380-c7e4c029835e/image.png" /></p>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/628c828f-e221-4edb-822f-ae510c1020cc/image.png" /></p>
<hr />
<h1 id="uitableview">UITableView</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fd731e43-73c1-4427-92df-1bc760b606da/image.png" /></p>
<pre><code class="language-swift">import UIKit</code></pre>
<ul>
<li>iOS UI 구성에 필요한 <code>UIKit</code> 프레임워크를 가져옵니다.</li>
</ul>
<hr />
<pre><code class="language-swift">let movie = [&quot;야당&quot;,&quot;야당1&quot;,&quot;야당2&quot;,&quot;야당3&quot;,&quot;야당4&quot;]</code></pre>
<ul>
<li>영화 제목이 담긴 문자열 배열입니다. 이 배열의 값을 <code>UITableView</code> 셀에 출력할 예정입니다.</li>
</ul>
<hr />
<pre><code class="language-swift">class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {</code></pre>
<ul>
<li>이 클래스는 <strong>뷰 컨트롤러</strong>이며,</li>
<li><code>UITableViewDelegate</code>와 <code>UITableViewDataSource</code> 프로토콜을 채택해 <strong>테이블 뷰와 관련된 이벤트 및 데이터 관리</strong>를 담당합니다.</li>
</ul>
<hr />
<pre><code class="language-swift">@IBOutlet weak var table: UITableView!</code></pre>
<ul>
<li>스토리보드에서 연결된 <code>UITableView</code>입니다.</li>
<li><code>IBOutlet</code>은 Interface Builder와 연결된 변수임을 의미합니다.</li>
</ul>
<hr />
<h3 id="📌-테이블-뷰-관련-필수-메서드">📌 테이블 뷰 관련 필수 메서드</h3>
<pre><code class="language-swift">func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -&gt; Int {
    return 5
}</code></pre>
<ul>
<li>각 섹션마다 몇 개의 셀이 있는지 반환합니다.</li>
<li>여기선 각 섹션에 5개의 셀을 표시합니다.</li>
</ul>
<hr />
<pre><code class="language-swift">func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -&gt; UITableViewCell {
    let cell = tableView.dequeueReusableCell(withIdentifier: &quot;myCell&quot;, for: indexPath) as! MyTableViewCell
    cell.movieName.text = movie[indexPath.row]
    print(indexPath.description)
    return cell
}</code></pre>
<ul>
<li><code>cellForRowAt</code>: 각 셀을 어떻게 표시할지 정의합니다.</li>
<li><code>dequeueReusableCell</code>: 재사용 가능한 셀을 가져옵니다. (식별자는 <code>&quot;myCell&quot;</code>이어야 하고, 커스텀 클래스는 <code>MyTableViewCell</code>로 설정되어 있어야 합니다.)</li>
<li><code>cell.movieName.text</code>: 커스텀 셀 안에 있는 <code>UILabel</code>에 영화 이름을 할당합니다.</li>
<li><code>indexPath.row</code>를 사용하여 배열의 해당 인덱스에 접근합니다.</li>
</ul>
<p>⚠️ 여기서 <code>movie[indexPath.row]</code>는 row 값이 5 이상이면 오류 발생합니다. 아래 섹션 갯수 설정을 보면 더 위험할 수 있습니다.</p>
<hr />
<pre><code class="language-swift">func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    // 셀 선택 시 호출되지만, 현재는 동작 없음.
}</code></pre>
<hr />
<pre><code class="language-swift">func numberOfSections(in tableView: UITableView) -&gt; Int {
    return 5
}</code></pre>
<ul>
<li>테이블 뷰에 섹션을 몇 개 표시할지 정합니다.</li>
<li>여기서는 섹션을 <strong>5개</strong>로 설정했습니다.</li>
</ul>
<p>⚠️ 이 경우, 총 셀 수는 5섹션 x 5행 = 25개가 되고, <code>movie</code> 배열은 5개뿐이라 범위를 벗어난 오류가 발생할 수 있어요.</p>
<hr />
<h3 id="📌-생명-주기-메서드">📌 생명 주기 메서드</h3>
<pre><code class="language-swift">override func viewDidLoad() {
    super.viewDidLoad()
    table.delegate = self
    table.dataSource = self
}</code></pre>
<ul>
<li>뷰가 메모리에 올라온 직후 실행되는 메서드입니다.</li>
<li>테이블 뷰의 <code>delegate</code>, <code>dataSource</code>를 현재 클래스(<code>self</code>)로 지정합니다.</li>
</ul>
<hr />
<h2 id="✅-요약">✅ 요약</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>movie</code></td>
<td>영화 이름 배열</td>
</tr>
<tr>
<td><code>UITableView</code></td>
<td>리스트 형태 UI 구성 요소</td>
</tr>
<tr>
<td><code>numberOfSections</code></td>
<td>섹션 수 설정 (5개로 설정됨)</td>
</tr>
<tr>
<td><code>numberOfRowsInSection</code></td>
<td>각 섹션당 셀 수 (5개로 설정됨)</td>
</tr>
<tr>
<td><code>cellForRowAt</code></td>
<td>각 셀에 데이터 넣는 방법</td>
</tr>
<tr>
<td><code>didSelectRowAt</code></td>
<td>셀 클릭 시 동작 정의 (현재 없음)</td>
</tr>
<tr>
<td><code>viewDidLoad</code></td>
<td>화면이 처음 로드될 때 테이블 뷰 설정</td>
</tr>
</tbody></table>
<hr />
<h1 id="guard-let-else기말">guard let else(기말)</h1>
<blockquote>
<p><strong>&quot;조기 탈출이 필요한 경우&quot;에는 <code>guard let</code>을 사용하는 것이 좋습니다.</strong></p>
</blockquote>
<hr />
<h2 id="📌-guard-let-vs-if-let-비교">📌 <code>guard let</code> vs <code>if let</code> 비교</h2>
<table>
<thead>
<tr>
<th>항목</th>
<th><code>guard let</code></th>
<th><code>if let</code></th>
</tr>
</thead>
<tbody><tr>
<td>위치</td>
<td>함수 초반 (검증용)</td>
<td>조건문 안에서</td>
</tr>
<tr>
<td>목적</td>
<td><strong>조기 탈출</strong> (early exit)</td>
<td><strong>조건부 실행</strong></td>
</tr>
<tr>
<td>가독성</td>
<td>중첩 없이 깔끔</td>
<td>중첩이 생길 수 있음</td>
</tr>
<tr>
<td>실패 시</td>
<td><code>else</code> 블록에서 <code>return</code>, <code>break</code> 등 필요</td>
<td><code>else</code>가 필요 없음</td>
</tr>
<tr>
<td>언래핑된 변수</td>
<td>블록 바깥에서도 사용 가능</td>
<td>블록 내부에서만 사용 가능</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-예시-비교">✅ 예시 비교</h2>
<h3 id="1-guard-let-권장되는-방식">1. <code>guard let</code> (권장되는 방식)</h3>
<pre><code class="language-swift">func fetchUser(id: String?) {
    guard let id = id else {
        print(&quot;ID 없음&quot;)
        return
    }
    print(&quot;ID로 사용자 검색 중: \(id)&quot;)
}</code></pre>
<ul>
<li><code>id</code>가 없으면 함수 종료 → <strong>조기 탈출</strong></li>
<li>이후 로직은 <code>id</code>가 있는 경우만 실행됨 → <strong>안전하고 깔끔</strong></li>
</ul>
<hr />
<h3 id="2-if-let-조건부-로직에-적합">2. <code>if let</code> (조건부 로직에 적합)</h3>
<pre><code class="language-swift">func fetchUser(id: String?) {
    if let id = id {
        print(&quot;ID로 사용자 검색 중: \(id)&quot;)
    } else {
        print(&quot;ID 없음&quot;)
    }
}</code></pre>
<ul>
<li>조건부로 분기할 때는 <code>if let</code>이 자연스럽습니다.</li>
<li>하지만 중첩 로직이 많아질 경우 보기 어렵고 복잡해질 수 있습니다.</li>
</ul>
<hr />
<h2 id="✅-결론-요약">✅ 결론 요약</h2>
<ul>
<li>함수 내에서 <strong>값이 없을 경우 즉시 리턴하거나 오류 처리</strong>를 하고 싶다면 → <code>guard let</code></li>
<li>값이 있을 때만 <strong>특정 블록을 실행</strong>하고 싶다면 → <code>if let</code></li>
</ul>
<hr />
<p>실무에서는 <code>guard let</code>을 많이 사용합니다. 이유는:</p>
<ul>
<li>흐름 제어가 깔끔하고</li>
<li>함수 구조가 덜 중첩되며</li>
<li>코드 가독성이 높기 때문입니다.</li>
</ul>
<hr />
<h1 id="후행-클로저로-바꾸는-방법">후행 클로저로 바꾸는 방법</h1>
<p><img alt="업로드중.." src="blob:https://velog.io/1ec11dd3-9135-4b56-9da0-6a1f7726d41a" /></p>
<h3 id="기존-스타일">기존 스타일:</h3>
<pre><code class="language-swift">session.dataTask(with: url) { data, response, error in
    // code
}</code></pre>
<h3 id="후행-클로저-스타일-괄호-밖으로-꺼냄">후행 클로저 스타일 (괄호 밖으로 꺼냄):</h3>
<pre><code class="language-swift">session.dataTask(with: url) { data, response, error in
    // code
}</code></pre>
<p>→ 사실상 <strong>모양은 동일하지만</strong>, 아래처럼 줄바꿈해서 클린하게 작성할 수도 있습니다.</p>
<pre><code class="language-swift">session.dataTask(with: url) { data, response, error in
    guard let data = data else { return }
    print(&quot;받은 데이터: \(data)&quot;)
}</code></pre>
<hr />
<h2 id="✨-enter로-바뀌는-순간">✨ <code>Enter</code>로 바뀌는 순간?</h2>
<p>Xcode에서 <code>session.dataTask(with: url)</code>를 쓴 다음에 <code>Tab</code> 또는 <code>Enter</code>를 누르면 자동으로 후행 클로저 형태로 전환됩니다.
혹은 클로저 파라미터의 괄호 <code>)</code>를 닫기 전에 바로 <code>{</code> 중괄호를 치면 Xcode가 후행 클로저 스타일로 자동 인식합니다.</p>
<hr />
<h2 id="🧠-요약">🧠 요약</h2>
<ul>
<li>클로저가 <strong>마지막 인자</strong>일 때 후행 클로저 문법 사용 가능</li>
<li><code>Enter</code> 또는 <code>{</code> 입력 시 Xcode가 후행 클로저 스타일 자동 적용</li>
<li>가독성을 높이고 코드가 깔끔해짐</li>
</ul>
<hr />
<h1 id="파싱을-쉽게-하기-위한-moviedata형-구조체를-swift로-만들기">파싱을 쉽게 하기 위한 MovieData형 구조체를 Swift로 만들기</h1>
<h2 id="quicktype">Quicktype</h2>
<pre><code class="language-swift">// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse the JSON, add this file to your project and do:
//
//   let welcome = try? JSONDecoder().decode(Welcome.self, from: jsonData)

import Foundation

// MARK: - Welcome
struct Welcome {
    let boxOfficeResult: BoxOfficeResult
}

// MARK: - BoxOfficeResult
struct BoxOfficeResult {
    let boxofficeType, showRange: String
    let dailyBoxOfficeList: [DailyBoxOfficeList]
}

// MARK: - DailyBoxOfficeList
struct DailyBoxOfficeList {
    let rnum, rank, rankInten: String
    let rankOldAndNew: RankOldAndNew
    let movieCD, movieNm, openDt, salesAmt: String
    let salesShare, salesInten, salesChange, salesAcc: String
    let audiCnt, audiInten, audiChange, audiAcc: String
    let scrnCnt, showCnt: String
}

enum RankOldAndNew: String {
    case old
}</code></pre>
<hr />
<h2 id="chatgpt">ChatGPT</h2>
<pre><code class="language-swift">import Foundation

// MARK: - Root Structure
struct MovieData: Codable {
    let boxOfficeResult: BoxOfficeResult
}

// MARK: - BoxOfficeResult
struct BoxOfficeResult: Codable {
    let boxofficeType: String
    let showRange: String
    let dailyBoxOfficeList: [DailyBoxOffice]
}

// MARK: - DailyBoxOffice
struct DailyBoxOffice: Codable {
    let rnum: String
    let rank: String
    let rankInten: String
    let rankOldAndNew: String
    let movieCd: String
    let movieNm: String
    let openDt: String
    let salesAmt: String
    let salesShare: String
    let salesInten: String
    let salesChange: String
    let salesAcc: String
    let audiCnt: String
    let audiInten: String
    let audiChange: String
    let audiAcc: String
    let scrnCnt: String
    let showCnt: String
}</code></pre>