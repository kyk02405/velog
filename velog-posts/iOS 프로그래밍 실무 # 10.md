<hr />
<h1 id="codable-구조체">Codable 구조체</h1>
<pre><code class="language-swift">struct MovieData : Codable {
let boxOfficeResult : BoxOfficeResult
}
struct BoxOfficeResult : Codable {
let dailyBoxOfficeList : [DailyBoxOfficeList]
}
struct DailyBoxOfficeList : Codable {
let movieNm : String
let audiCnt : String
let audiAcc : String
let rank : String
}</code></pre>
<h3 id="🔷-struct-moviedata--codable">🔷 <code>struct MovieData : Codable</code></h3>
<ul>
<li><p><strong>역할</strong>: 전체 JSON 응답의 최상위 구조체입니다.</p>
</li>
<li><p><strong>속성</strong></p>
<ul>
<li><code>boxOfficeResult</code>: <code>BoxOfficeResult</code> 타입의 객체. JSON 내 <code>boxOfficeResult</code> 필드에 대응됩니다.</li>
</ul>
</li>
</ul>
<p>예시 JSON:</p>
<pre><code class="language-json">{
  &quot;boxOfficeResult&quot;: {
    ...
  }
}</code></pre>
<hr />
<h3 id="🔷-struct-boxofficeresult--codable">🔷 <code>struct BoxOfficeResult : Codable</code></h3>
<ul>
<li><p><strong>역할</strong>: 박스오피스 결과 전체를 나타냅니다.</p>
</li>
<li><p><strong>속성</strong></p>
<ul>
<li><code>dailyBoxOfficeList</code>: <code>[DailyBoxOfficeList]</code> 배열. 일일 박스오피스 영화 목록을 담고 있습니다.</li>
</ul>
</li>
</ul>
<p>예시 JSON:</p>
<pre><code class="language-json">&quot;boxOfficeResult&quot;: {
  &quot;dailyBoxOfficeList&quot;: [
    {
      &quot;movieNm&quot;: &quot;범죄도시4&quot;,
      &quot;audiCnt&quot;: &quot;150000&quot;,
      &quot;audiAcc&quot;: &quot;5000000&quot;,
      &quot;rank&quot;: &quot;1&quot;
    },
    ...
  ]
}</code></pre>
<hr />
<h3 id="🔷-struct-dailyboxofficelist--codable">🔷 <code>struct DailyBoxOfficeList : Codable</code></h3>
<ul>
<li><p><strong>역할</strong>: 하루 동안 상영된 각 영화의 박스오피스 정보를 담는 구조체입니다.</p>
</li>
<li><p><strong>속성</strong></p>
<ul>
<li><code>movieNm</code>: 영화 이름 (예: <code>&quot;범죄도시4&quot;</code>)</li>
<li><code>audiCnt</code>: 당일 관객 수 (예: <code>&quot;150000&quot;</code>)</li>
<li><code>audiAcc</code>: 누적 관객 수 (예: <code>&quot;5000000&quot;</code>)</li>
<li><code>rank</code>: 박스오피스 순위 (예: <code>&quot;1&quot;</code>)</li>
</ul>
</li>
</ul>
<blockquote>
<p>🔸 모든 값이 <code>String</code>인 이유는 해당 API가 숫자 값도 문자열로 제공하기 때문입니다.</p>
</blockquote>
<hr />
<h3 id="🧠-예시-전체-json-응답-구조">🧠 예시 전체 JSON 응답 구조</h3>
<pre><code class="language-json">{
  &quot;boxOfficeResult&quot;: {
    &quot;dailyBoxOfficeList&quot;: [
      {
        &quot;movieNm&quot;: &quot;범죄도시4&quot;,
        &quot;audiCnt&quot;: &quot;150000&quot;,
        &quot;audiAcc&quot;: &quot;5000000&quot;,
        &quot;rank&quot;: &quot;1&quot;
      },
      {
        &quot;movieNm&quot;: &quot;쿵푸팬더4&quot;,
        &quot;audiCnt&quot;: &quot;80000&quot;,
        &quot;audiAcc&quot;: &quot;3000000&quot;,
        &quot;rank&quot;: &quot;2&quot;
      }
    ]
  }
}</code></pre>
<hr />
<h3 id="✅-정리">✅ 정리</h3>
<p>이 구조체들을 사용하면 다음과 같은 방식으로 JSON 응답을 디코딩할 수 있습니다:</p>
<pre><code class="language-swift">let decoder = JSONDecoder()
let movieData = try decoder.decode(MovieData.self, from: jsonData)</code></pre>
<p>그 후, 다음처럼 사용 가능합니다:</p>
<pre><code class="language-swift">for movie in movieData.boxOfficeResult.dailyBoxOfficeList {
    print(&quot;영화 제목: \(movie.movieNm)&quot;)
    print(&quot;당일 관객 수: \(movie.audiCnt)&quot;)
    print(&quot;누적 관객 수: \(movie.audiAcc)&quot;)
    print(&quot;순위: \(movie.rank)&quot;)
}</code></pre>
<p>필요하다면 <code>audiCnt</code>나 <code>audiAcc</code>를 <code>Int</code>로 바꿔주는 로직을 따로 추가할 수 있어요.</p>
<hr />
<h1 id="func-decodetttype-from-data-throws---t">func decode&lt;T(T.Type, from: Data) throws -&gt; T</h1>
<p><code>func decode&lt;T&gt;(_ type: T.Type, from data: Data) throws -&gt; T</code>는 Swift의 <code>JSONDecoder</code> 클래스에서 제공하는 <strong>제네릭 메서드</strong>입니다.
이 메서드는 JSON 형식의 데이터를 Swift의 타입(<code>struct</code>, <code>class</code>)으로 **변환(디코딩)**하는 데 사용됩니다.</p>
<hr />
<h2 id="📌-전체-선언">📌 전체 선언</h2>
<pre><code class="language-swift">func decode&lt;T&gt;(_ type: T.Type, from data: Data) throws -&gt; T where T : Decodable</code></pre>
<hr />
<h2 id="✅-의미-분석">✅ 의미 분석</h2>
<h3 id="1-func-decodet-">1. <code>func decode&lt;T&gt; ...</code></h3>
<ul>
<li><strong>제네릭 함수</strong>입니다.</li>
<li><code>T</code>는 아무 타입이나 될 수 있는데, 단 <code>Decodable</code> 프로토콜을 채택한 타입이어야 합니다.</li>
<li>즉, <code>T</code>는 <code>struct</code>, <code>class</code>, <code>enum</code> 등인데 <code>Decodable</code>을 준수하는 타입이어야 합니다.</li>
</ul>
<h3 id="2-_-type-ttype-from-data-data">2. <code>(_ type: T.Type, from data: Data)</code></h3>
<ul>
<li><p><code>type: T.Type</code></p>
<ul>
<li>디코딩하려는 대상 타입을 전달합니다.</li>
<li>예: <code>MovieData.self</code> 또는 <code>User.self</code> 등.</li>
</ul>
</li>
<li><p><code>from data: Data</code></p>
<ul>
<li>JSON 데이터를 <code>Data</code> 형식으로 받아옵니다.</li>
<li>보통 <code>URLSession</code> 등을 통해 받은 응답 데이터를 넣습니다.</li>
</ul>
</li>
</ul>
<h3 id="3-throws---t">3. <code>throws -&gt; T</code></h3>
<ul>
<li>이 함수는 <code>throws</code>를 사용하므로 오류를 던질 수 있습니다.</li>
<li>호출 시 <code>try</code>를 붙여야 하며, 실패 시 오류를 처리해야 합니다.</li>
</ul>
<hr />
<h2 id="🧠-예시-코드">🧠 예시 코드</h2>
<h3 id="🎯-구조체-정의">🎯 구조체 정의</h3>
<pre><code class="language-swift">struct User: Codable {
    let name: String
    let age: Int
}</code></pre>
<h3 id="🎯-json-→-data-→-객체로-디코딩">🎯 JSON → Data → 객체로 디코딩</h3>
<pre><code class="language-swift">let json = &quot;&quot;&quot;
{
  &quot;name&quot;: &quot;경윤&quot;,
  &quot;age&quot;: 23
}
&quot;&quot;&quot;.data(using: .utf8)!

do {
    let decoder = JSONDecoder()
    let user = try decoder.decode(User.self, from: json)
    print(user.name)  // 경윤
    print(user.age)   // 23
} catch {
    print(&quot;디코딩 실패: \(error)&quot;)
}</code></pre>
<hr />
<h2 id="🧩-관련-개념-요약">🧩 관련 개념 요약</h2>
<table>
<thead>
<tr>
<th>요소</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>T.Type</code></td>
<td>어떤 타입을 나타내는 메타 타입 (예: <code>User.self</code>)</td>
</tr>
<tr>
<td><code>Data</code></td>
<td>디코딩할 JSON 데이터</td>
</tr>
<tr>
<td><code>Decodable</code></td>
<td>해당 타입이 JSON에서 디코딩 가능하도록 해주는 프로토콜</td>
</tr>
<tr>
<td><code>throws</code></td>
<td>디코딩 실패 시 예외 발생 가능</td>
</tr>
<tr>
<td><code>try</code></td>
<td>예외를 감지하며 함수를 실행</td>
</tr>
</tbody></table>
<hr />
<h2 id="🔚-요약">🔚 요약</h2>
<p><code>decode(_:from:)</code>는 JSON 데이터를 Swift 타입으로 변환하는 핵심 함수이며, 일반적으로 다음처럼 사용합니다:</p>
<pre><code class="language-swift">let object = try JSONDecoder().decode(타입.self, from: jsonData)</code></pre>
<p>이때 타입은 <code>Codable</code> 또는 최소한 <code>Decodable</code>을 준수해야 하며, JSON의 구조와 Swift의 구조체 필드명이 잘 맞아야 합니다.</p>
<hr />
<p>#</p>
<h2 id="시험-나옴">시험 나옴</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b9b1e9a1-c936-4c1c-960c-edb831e3197b/image.png" /></p>
<p>이 에러 메시지는 Swift에서 <strong>클로저 내부에서 인스턴스의 속성(<code>movieData</code>)을 접근할 때 <code>self</code>를 명시적으로 써야 한다</strong>는 의미입니다.</p>
<h3 id="🔴-에러-메시지-요약">🔴 에러 메시지 요약:</h3>
<blockquote>
<p><code>Reference to property 'movieData' in closure requires explicit use of 'self' to make capture semantics explicit</code></p>
</blockquote>
<p>즉, <code>movieData = decodedData</code> 라인에서 <code>movieData</code>는 아마도 클래스나 구조체의 <strong>속성</strong>인데, 이 코드가 <strong>클로저 안에서 실행되고 있어서 <code>self.movieData</code>라고 명시해야 한다</strong>는 것입니다.</p>
<hr />
<h2 id="✅-해결-방법">✅ 해결 방법</h2>
<h3 id="①-selfmoviedata로-명시적으로-작성">① <code>self.movieData</code>로 명시적으로 작성</h3>
<pre><code class="language-swift">self.movieData = decodedData</code></pre>
<p>이 방법이 가장 일반적이며, Swift의 클로저 캡처 규칙을 만족시킵니다.</p>
<hr />
<h2 id="🧠-왜-이런-에러가-나는가">🧠 왜 이런 에러가 나는가?</h2>
<p>Swift는 <strong>클로저 안에서 자기 자신(<code>self</code>)을 캡처할 때</strong> 메모리 관리 문제(특히 강한 참조 순환)를 피하기 위해 <strong>명시적으로 <code>self.</code>를 써야 하는 규칙</strong>이 있습니다.</p>
<p>이 규칙은 다음과 같은 경우에 적용됩니다:</p>
<ul>
<li>클로저 안에서 클래스의 프로퍼티를 접근할 때</li>
<li>클로저가 비동기적으로 실행될 가능성이 있을 때 (예: URLSession 등)</li>
</ul>
<hr />
<h2 id="✍️-예시">✍️ 예시</h2>
<p>클래스 내부에서 다음처럼 정의되어 있을 때:</p>
<pre><code class="language-swift">class MyViewController: UIViewController {
    var movieData: MovieData?

    func loadData() {
        let decoder = JSONDecoder()
        do {
            let decodedData = try decoder.decode(MovieData.self, from: JSONdata)
            self.movieData = decodedData // 🔍 여기에 self 필요
            print(decodedData.boxOfficeResult.dailyBoxOfficeList)
        } catch {
            print(error)
        }
    }
}</code></pre>
<hr />
<h2 id="✅-보너스-캡처-리스트를-쓰는-방법-간단-설명">✅ 보너스: 캡처 리스트를 쓰는 방법 (간단 설명)</h2>
<pre><code class="language-swift">[weak self] in
self?.movieData = decodedData</code></pre>
<ul>
<li>비동기 클로저에서 메모리 누수를 방지하려면 <code>[weak self]</code>를 사용하고 <code>self?</code>로 안전하게 접근합니다.</li>
</ul>
<hr />
<h1 id="main-thread-checker관련-오류-발생">Main Thread Checker관련 오류 발생</h1>
<h2 id="시험--오류-발생시-고치는-법">시험 : 오류 발생시 고치는 법</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4ac358ee-6d4d-4dbd-92af-80e1c91d7714/image.png" /></p>
<p>이 에러는 <strong>메인 스레드가 아닌 백그라운드 스레드에서 UI를 업데이트했기 때문에 발생한 오류</strong>입니다.</p>
<hr />
<h2 id="🔴-에러-메시지-요약-1">🔴 에러 메시지 요약</h2>
<pre><code>Main Thread Checker: UI API called on a background thread: -[UITableView reloadData]</code></pre><h3 id="→-uitableviewreloaddata는-메인-스레드에서만-호출해야-하는데-지금-비동기-클로저-background-thread-안에서-호출하고-있어서-문제가-발생한-것입니다">→ <code>UITableView.reloadData()</code>는 <strong>메인 스레드</strong>에서만 호출해야 하는데, 지금 <strong>비동기 클로저 (background thread)</strong> 안에서 호출하고 있어서 문제가 발생한 것입니다.</h3>
<hr />
<h2 id="✅-해결-방법-1">✅ 해결 방법</h2>
<p><code>self.table.reloadData()</code>를 <strong>메인 스레드</strong>에서 실행되도록 다음처럼 수정하세요:</p>
<pre><code class="language-swift">DispatchQueue.main.async {
    self.table.reloadData()
}</code></pre>
<hr />
<h2 id="🔧-수정-코드-예시">🔧 수정 코드 예시</h2>
<pre><code class="language-swift">do {
    let decodedData = try decoder.decode(MovieData.self, from: JSONdata)
    self.movieData = decodedData
    print(decodedData.boxOfficeResult.dailyBoxOfficeList[0].movieNm)
    print(decodedData.boxOfficeResult.dailyBoxOfficeList[0].audiAcc)

    DispatchQueue.main.async {
        self.table.reloadData()
    }
} catch {
    print(error)
}</code></pre>
<hr />
<h2 id="📌-참고">📌 참고</h2>
<ul>
<li>iOS에서는 모든 <strong>UI 업데이트는 반드시 메인 스레드</strong>에서 해야 합니다.</li>
<li><code>URLSession</code>, <code>DispatchQueue.global</code>, <code>.asyncAfter</code>, 등에서 실행되는 코드는 기본적으로 <strong>백그라운드 스레드</strong>에서 동작합니다.</li>
<li><code>reloadData()</code>는 테이블 뷰를 새로 그리는 작업이기 때문에 반드시 메인 스레드에서 호출되어야 합니다.</li>
</ul>
<hr />
<h1 id="전체-코드-설명">전체 코드 설명</h1>
<p>아래는 요청하신 <strong><code>ViewController.swift</code> 전체 코드에 상세 주석을 추가한 버전</strong>입니다.
코드의 흐름과 기능이 잘 이해되도록 각 줄마다 설명을 달았습니다.</p>
<hr />
<pre><code class="language-swift">//
//  ViewController.swift
//  MovieKYK
//
//  Created by CMAC_43 on 2025/05/07.
//

import UIKit  // iOS 앱 개발을 위한 기본 프레임워크

// 임시로 선언된 영화 이름 배열 (현재 사용하지 않음)
let movie = [&quot;야당&quot;,&quot;야당1&quot;,&quot;야당2&quot;,&quot;야당3&quot;,&quot;야당4&quot;]

// MARK: - JSON 디코딩을 위한 데이터 구조체 정의

// 최상위 JSON 응답 객체
struct MovieData : Codable {
    let boxOfficeResult : BoxOfficeResult  // 박스오피스 결과
}

// 박스오피스 결과 내부 구조
struct BoxOfficeResult : Codable {
    let dailyBoxOfficeList : [DailyBoxOfficeList]  // 일별 박스오피스 영화 목록
}

// 일일 영화 정보 구조
struct DailyBoxOfficeList : Codable {
    let movieNm : String   // 영화 이름
    let audiCnt : String   // 당일 관객 수
    let audiAcc : String   // 누적 관객 수
    let rank : String      // 박스오피스 순위
}

// MARK: - 메인 뷰 컨트롤러 정의

class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {

    @IBOutlet weak var table: UITableView!  // 스토리보드에서 연결된 테이블뷰 아웃렛

    var movieData : MovieData?  // API로부터 디코딩한 영화 데이터를 저장할 변수

    // 영화진흥위원회 API의 기본 주소 (날짜 파라미터는 뒤에서 붙임)
    var movieURL =
    &quot;https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=4b8c2206c2b38d5e037d886bbcca7ebf&amp;targetDt=&quot;

    // 뷰가 로드되었을 때 호출됨
    override func viewDidLoad() {
        super.viewDidLoad()

        // 테이블 뷰 설정
        table.delegate = self
        table.dataSource = self

        // 어제 날짜를 yyyyMMdd 형식으로 구한 뒤 URL에 추가
        movieURL = movieURL + makeYesterdayString()

        // 데이터 요청 시작
        getData()
    }

    // 어제 날짜를 &quot;yyyyMMdd&quot; 형식 문자열로 반환하는 함수
    func makeYesterdayString() -&gt; String {
        let calendar = Calendar.current               // 현재 달력 사용
        let today = Date()                            // 오늘 날짜
        guard let yesterday = calendar.date(byAdding: .day, value: -1, to: today) else {
            return &quot;&quot;
        }

        let formatter = DateFormatter()               // 날짜 포맷터 생성
        formatter.dateFormat = &quot;yyyyMMdd&quot;             // 원하는 출력 형식 지정
        formatter.locale = Locale(identifier: &quot;ko_KR&quot;) // 한국 로케일 지정

        return formatter.string(from: yesterday)      // 어제 날짜를 문자열로 반환
    }

    // API로부터 데이터를 받아와서 디코딩하고 테이블 뷰를 업데이트하는 함수
    func getData() {
        // 문자열을 URL 객체로 변환
        guard let url = URL(string: movieURL) else { return }

        // URL 세션 생성
        let session = URLSession(configuration: .default)

        // 데이터 요청 작업 시작
        let task = session.dataTask(with: url) { data, response, error in
            // 에러 발생 시 콘솔에 출력
            if error != nil {
                print(error!)
                return
            }

            // 데이터가 없으면 종료
            guard let JSONdata = data else { return }

            // (옵션) 데이터 문자열로 변환해보기 (디버깅용)
            let dataString = String(data: JSONdata, encoding: .utf8)
            // print(dataString!)

            let decoder = JSONDecoder()  // JSON 디코더 생성
            do {
                // JSON 데이터를 MovieData 구조체로 디코딩
                let decodedData = try decoder.decode(MovieData.self, from: JSONdata)
                self.movieData = decodedData  // 결과 저장

                // 첫 번째 영화 정보 출력 (디버깅용)
                print(decodedData.boxOfficeResult.dailyBoxOfficeList[0].movieNm)
                print(decodedData.boxOfficeResult.dailyBoxOfficeList[0].audiAcc)

                // UI 업데이트는 반드시 메인 스레드에서 실행
                DispatchQueue.main.async {
                    self.table.reloadData()  // 테이블 뷰 새로고침
                }

            } catch {
                // 디코딩 에러 출력
                print(error)
            }
        }

        task.resume()  // 작업 시작
    }

    // MARK: - 테이블 뷰 데이터소스 및 델리게이트 구현

    // 테이블 뷰 섹션당 셀 개수 설정
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -&gt; Int {
        // movieData가 없으면 0, 있으면 영화 수만큼 반환
        return movieData?.boxOfficeResult.dailyBoxOfficeList.count ?? 0
    }

    // 셀을 생성하고 데이터를 삽입하는 함수
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -&gt; UITableViewCell {
        // 재사용 가능한 셀을 가져옴 (Identifier: &quot;myCell&quot;)
        let cell = tableView.dequeueReusableCell(withIdentifier: &quot;myCell&quot;, for: indexPath) as! MyTableViewCell

        // 해당 인덱스의 영화 데이터를 셀에 표시
        cell.movieName.text = movieData?.boxOfficeResult.dailyBoxOfficeList[indexPath.row].movieNm

        return cell
    }

    // 셀 선택 시 호출되는 함수 (현재는 비어있음)
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        // 선택된 셀의 index 정보 등 활용 가능
        // print(indexPath.description)
    }

    // 섹션 수 설정 (기본적으로 1개)
    func numberOfSections(in tableView: UITableView) -&gt; Int {
        return 1
    }
}</code></pre>
<hr />
<h2 id="✅-요약">✅ 요약</h2>
<ul>
<li><strong>KOBIS API</strong>로부터 어제 날짜의 일별 박스오피스 데이터를 받아와서 테이블 뷰에 표시합니다.</li>
<li><code>makeYesterdayString()</code>을 통해 자동으로 어제 날짜를 계산하고, API URL에 붙입니다.</li>
<li>JSON 응답을 <code>Codable</code> 구조체로 파싱하여 <code>movieData</code>에 저장한 뒤, <code>reloadData()</code>를 통해 테이블 뷰를 업데이트합니다.</li>
</ul>
<hr />
<h1 id="stackview">StackView</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2ac36caa-b69c-4989-842d-e93cc127bad4/image.png" /></p>
<blockquote>
<p>기본적으로 Vertical</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a28e22eb-c157-4590-9b79-cf079d865b62/image.png" /></p>
<blockquote>
<p>Horizontal</p>
</blockquote>