<hr />
<h1 id="root-view-controller시험">Root View Controller(시험)</h1>
<p><code>Root View Controller</code>는 iOS 앱에서 <strong>UIWindow의 최상단에 위치한 첫 번째 뷰 컨트롤러</strong>입니다. 앱이 실행되면 가장 먼저 사용자에게 보이는 화면을 담당하며, 이 뷰 컨트롤러를 중심으로 전체 화면 구조가 전개됩니다.</p>
<hr />
<h3 id="✅-예시로-이해하기">✅ 예시로 이해하기</h3>
<p>앱을 처음 실행했을 때:</p>
<ul>
<li>로그인 화면이 제일 먼저 나오면 → 로그인 뷰 컨트롤러가 root</li>
<li>내비게이션이 필요한 앱이라면 → Navigation Controller가 root가 되고, 그 안에 첫 번째 화면(예: 홈 화면)이 포함됨</li>
</ul>
<hr />
<h3 id="🧱-구조적-위치">🧱 구조적 위치</h3>
<pre><code class="language-swift">window.rootViewController = SomeViewController()</code></pre>
<ul>
<li>이 코드가 <code>AppDelegate</code>나 <code>SceneDelegate</code>에 들어가서 어떤 뷰 컨트롤러를 <strong>앱의 시작 지점</strong>으로 설정합니다.</li>
<li>보통 <code>NavigationController</code>, <code>TabBarController</code> 같은 <strong>컨테이너 뷰 컨트롤러</strong>가 root로 쓰이는 경우가 많습니다.</li>
</ul>
<hr />
<h3 id="🔁-navigationcontroller와의-관계">🔁 NavigationController와의 관계</h3>
<ul>
<li>Navigation Controller는 여러 화면(ViewController)을 <strong>스택 구조로 관리</strong>합니다.</li>
<li>이 Navigation Controller 자체가 <strong>root view controller</strong>가 되고, 그 안에 <strong>첫 화면</strong>(ex. 홈 화면)이 <strong>rootViewController의 child</strong>가 됩니다.</li>
</ul>
<hr />
<h3 id="📌-정리">📌 정리</h3>
<table>
<thead>
<tr>
<th>용어</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>Root View Controller</code></td>
<td>앱 실행 시 가장 먼저 표시되는 메인 화면 컨트롤러</td>
</tr>
<tr>
<td><code>Navigation Controller</code></td>
<td>여러 화면을 push/pop 방식으로 전환하는 컨테이너 역할</td>
</tr>
<tr>
<td><code>NavigationController</code>가 Root일 경우</td>
<td>Navigation 흐름 전체를 앱의 루트로 사용 가능</td>
</tr>
</tbody></table>
<hr />
<h1 id="✅-액션-세그웨이-vs-매뉴얼-세그웨이-비교표">✅ 액션 세그웨이 vs 매뉴얼 세그웨이 비교표</h1>
<table>
<thead>
<tr>
<th>항목</th>
<th><strong>액션 세그웨이 (Action Segue)</strong></th>
<th><strong>매뉴얼 세그웨이 (Manual Segue)</strong></th>
</tr>
</thead>
<tbody><tr>
<td><strong>정의</strong></td>
<td>버튼 등 UI 요소에 직접 연결된 세그웨이</td>
<td>코드에서 직접 호출하는 세그웨이</td>
</tr>
<tr>
<td><strong>트리거 방식</strong></td>
<td>스토리보드에서 **UI 요소(Control-drag)**로 연결</td>
<td><code>performSegue(withIdentifier:)</code>로 코드에서 호출</td>
</tr>
<tr>
<td><strong>스토리보드 연결 방식</strong></td>
<td>버튼 → ViewController로 직접 연결</td>
<td>ViewController끼리만 연결, identifier 설정 필요</td>
</tr>
<tr>
<td><strong>Segue Identifier 필요 여부</strong></td>
<td>❌ 필요 없음 (스토리보드에서 자동 설정)</td>
<td>✅ 필수 (코드에서 identifier로 호출)</td>
</tr>
<tr>
<td><strong>사용 용도</strong></td>
<td>버튼 클릭 시 자동으로 화면 전환</td>
<td>조건에 따라, 또는 특정 이벤트에서만 전환 시 사용</td>
</tr>
<tr>
<td><strong>예시</strong></td>
<td>로그인 버튼 클릭 시 다음 화면으로 전환</td>
<td>로그인 검증 후 조건 만족 시 다음 화면으로 이동</td>
</tr>
</tbody></table>
<hr />
<h3 id="💡-추가-설명">💡 추가 설명</h3>
<ul>
<li><strong>액션 세그웨이</strong>는 간단한 화면 전환에 유용하며, 조건 없이 항상 전환됩니다.</li>
<li><strong>매뉴얼 세그웨이</strong>는 조건을 검사하거나 로직 실행 후 화면을 전환해야 할 때 사용됩니다.</li>
</ul>
<hr />
<h1 id="navigation-controller를-추가하면-바뀌는-내용">Navigation Controller를 추가하면 바뀌는 내용</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/96566c30-5abe-4a6d-b1ae-8b96a05f40bd/image.png" /></p>
<table>
<thead>
<tr>
<th>번호</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>①</td>
<td><strong>Navigation Controller에 연결된 View Controller에 <code>Navigation Item</code>이 자동으로 추가됨</strong><br />- 상단에 <code>&lt;Back</code> 버튼이 생겨 화면 간 뒤로 이동 가능</td>
</tr>
<tr>
<td>②</td>
<td><strong>Storyboard Entry Point가 Navigation Controller로 변경됨</strong><br />- 앱 실행 시 첫 화면으로 지정되는 뷰가 <strong>Navigation Controller</strong>로 바뀜</td>
</tr>
<tr>
<td>③</td>
<td>**기존 View Controller와 Navigation Controller 사이에 segue(연결선)**가 생김<br />- 이 segue를 통해 Navigation Controller가 해당 View Controller를 관리</td>
</tr>
<tr>
<td>④</td>
<td><strong>Navigation Bar가 상단에 표시됨</strong><br />- Navigation Bar 안에는 <code>Navigation Bar Title</code>이 들어가 제목 표시가 가능<br />- <code>Navigation Item</code>을 통해 뒤로가기 등 버튼 추가 가능</td>
</tr>
</tbody></table>
<hr />
<h3 id="🧱-핵심-개념-요약">🧱 핵심 개념 요약</h3>
<ul>
<li><code>Navigation Controller</code>는 여러 화면을 계층적으로 관리하는 <strong>컨테이너 뷰 컨트롤러</strong></li>
<li>한 번 연결하면, 연결된 각 View Controller에 자동으로 <strong>Navigation Bar + Back Button</strong>이 추가됨</li>
<li>처음 보여줄 화면을 Navigation Controller가 책임지게 되며, segue를 통해 실제 뷰 컨트롤러와 연결</li>
</ul>
<hr />
<h1 id="storyboard-id-설정-방법">Storyboard ID 설정 방법</h1>
<hr />
<h3 id="✅-storyboard-id-설정-방법-detailviewcontroller">✅ Storyboard ID 설정 방법 (<code>DetailViewController</code>)</h3>
<table>
<thead>
<tr>
<th>번호</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>①</td>
<td><strong>Storyboard 상에서 대상 View Controller를 선택</strong><br /> - 왼쪽 Scene 목록 혹은 중앙 뷰에서 클릭 가능</td>
</tr>
<tr>
<td>②</td>
<td><strong>오른쪽 상단의 Identity Inspector 아이콘 클릭</strong><br /> - 정체성 관련 설정을 하는 곳 (작은 ID 카드 모양 아이콘)</td>
</tr>
<tr>
<td>③</td>
<td><strong>Identity 섹션에서 'Storyboard ID'에 이름 입력 후 반드시 <code>Enter</code></strong><br /> - 예시에서는 <code>&quot;DetailViewController&quot;</code> 입력<br /> - 입력 후 엔터를 눌러야 저장됨 (주의사항 강조됨)</td>
</tr>
</tbody></table>
<hr />
<h3 id="💡-왜-필요한가요">💡 왜 필요한가요?</h3>
<p>Storyboard ID는 <strong>코드에서 ViewController를 생성할 때 사용</strong>됩니다. 예를 들어:</p>
<pre><code class="language-swift">let storyboard = UIStoryboard(name: &quot;Main&quot;, bundle: nil)
let vc = storyboard.instantiateViewController(withIdentifier: &quot;DetailViewController&quot;)
self.navigationController?.pushViewController(vc, animated: true)</code></pre>
<p>위 코드에서 <code>&quot;DetailViewController&quot;</code>가 바로 <strong>Storyboard ID</strong>입니다.</p>
<hr />
<h3 id="🔁-요약">🔁 요약</h3>
<ul>
<li>Storyboard ID는 <strong>코드에서 뷰 컨트롤러를 인식하기 위한 키(Key)</strong> 역할</li>
<li>반드시 <strong>입력 후 <code>Enter</code>를 눌러야 적용</strong>됨</li>
<li>설정은 Identity Inspector에서 진행</li>
</ul>
<hr />
<h1 id="prepare">prepare</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c2d6a7de-2450-4eff-a207-bd30cc267579/image.png" /></p>
<ul>
<li><code>UIViewController</code>의 메서드 중 하나</li>
<li>스토리보드에서 <strong>Segue를 사용해 화면 전환</strong>할 때 호출됨</li>
<li>다음 화면(ViewController)으로 <strong>데이터를 전달</strong>하거나 설정할 때 사용</li>
</ul>
<hr />
<h2 id="📌-기본-구조">📌 기본 구조</h2>
<pre><code class="language-swift">override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
    if segue.identifier == &quot;toDetail&quot; {
        let destinationVC = segue.destination as! DetailViewController
        destinationVC.titleText = &quot;전달할 텍스트&quot;
    }
}</code></pre>
<hr />
<h2 id="✅-예제-영화-목록에서-영화-상세로-이동하며-데이터-전달">✅ 예제: 영화 목록에서 영화 상세로 이동하며 데이터 전달</h2>
<h3 id="1-화면-구성">1. 화면 구성</h3>
<ul>
<li><code>MainViewController</code> : 영화 목록</li>
<li><code>DetailViewController</code> : 상세 정보 화면</li>
<li>segue identifier는 <code>&quot;toDetail&quot;</code></li>
</ul>
<hr />
<h3 id="2-detailviewcontrollerswift">2. <code>DetailViewController.swift</code></h3>
<pre><code class="language-swift">class DetailViewController: UIViewController {
    var movieTitle: String?  // 전달받을 변수

    override func viewDidLoad() {
        super.viewDidLoad()
        self.title = movieTitle
    }
}</code></pre>
<hr />
<h3 id="3-mainviewcontrollerswift">3. <code>MainViewController.swift</code></h3>
<pre><code class="language-swift">class MainViewController: UIViewController {
    var selectedMovie = &quot;인셉션&quot;

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == &quot;toDetail&quot; {
            let destination = segue.destination as! DetailViewController
            destination.movieTitle = selectedMovie
        }
    }
}</code></pre>
<hr />
<h2 id="🧠-중요한-포인트">🧠 중요한 포인트</h2>
<table>
<thead>
<tr>
<th>항목</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>segue.identifier</code></td>
<td>어떤 segue인지 구분하기 위한 식별자</td>
</tr>
<tr>
<td><code>segue.destination</code></td>
<td>이동할 대상 ViewController 객체</td>
</tr>
<tr>
<td><code>sender</code></td>
<td>segue를 트리거한 객체 (예: 버튼, 셀 등)</td>
</tr>
<tr>
<td>타입 캐스팅</td>
<td><code>as! DetailViewController</code>처럼 <strong>타입 변환</strong> 필수</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-언제-호출되나요">✅ 언제 호출되나요?</h2>
<ul>
<li>스토리보드에서 segue를 만들고 <strong>버튼, 셀 클릭으로 화면 전환할 때 자동 호출됨</strong></li>
<li><strong>Segue 연결이 있을 때만 작동</strong>
→ 수동 세그웨이(<code>performSegue</code>)도 해당됨</li>
</ul>
<hr />
<h2 id="✅-tip">✅ Tip</h2>
<ul>
<li><code>sender</code>를 활용하면 <strong>누른 버튼, 선택한 셀 정보</strong>를 넘길 수 있음</li>
<li>TableView에서 선택된 셀의 데이터를 넘기고 싶을 때 많이 활용함</li>
</ul>
<hr />
<h1 id="seguedestination">SegueDestination</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5ef4f9c6-9deb-4a49-94fd-00ce77737a00/image.png" /></p>
<hr />
<h3 id="✅-seguedestination이란">✅ <code>segue.destination</code>이란?</h3>
<ul>
<li><code>segue.destination</code>은 <strong>화면 전환 시 목적지 ViewController 객체</strong>를 의미합니다.</li>
<li><code>prepare(for:sender:)</code> 메서드 안에서 주로 사용되며, <strong>데이터 전달의 핵심 역할</strong>을 합니다.</li>
</ul>
<hr />
<h3 id="📌-선언부">📌 선언부</h3>
<pre><code class="language-swift">var destination: UIViewController { get }</code></pre>
<ul>
<li>읽기 전용(read-only) 프로퍼티</li>
<li>반환형은 <code>UIViewController</code>이지만, 실제로는 우리가 만든 커스텀 ViewController (<code>DetailViewController</code> 등)로 <strong>다운캐스팅</strong>하여 사용해야 함</li>
</ul>
<hr />
<h3 id="📘-공식-문서-요약-스크린샷-내용">📘 공식 문서 요약 (스크린샷 내용)</h3>
<table>
<thead>
<tr>
<th>항목</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Summary</strong></td>
<td>해당 segue의 목적지 뷰 컨트롤러</td>
</tr>
<tr>
<td><strong>Discussion</strong></td>
<td>전환이 끝났을 때 보여지게 될 뷰 컨트롤러의 인스턴스를 담고 있음</td>
</tr>
</tbody></table>
<hr />
<h3 id="🧠-사용-예시">🧠 사용 예시</h3>
<pre><code class="language-swift">override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
    if segue.identifier == &quot;toDetail&quot; {
        let dest = segue.destination as! DetailViewController
        dest.movieTitle = &quot;인셉션&quot;
    }
}</code></pre>
<ul>
<li><code>segue.destination</code>은 <code>UIViewController</code> 타입이라서,</li>
<li>우리가 만든 뷰 컨트롤러로 사용하려면 **타입 캐스팅(as!)**을 꼭 해줘야 합니다.</li>
</ul>
<hr />
<h1 id="mvc-디자인-패턴으로-리팩토링하기">MVC 디자인 패턴으로 리팩토링하기</h1>
<h2 id="✅-구조-정리">✅ 구조 정리</h2>
<table>
<thead>
<tr>
<th>구성 요소</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>Model</strong></td>
<td>영화 데이터 구조 정의, 날짜 처리 및 API 요청</td>
</tr>
<tr>
<td><strong>View</strong></td>
<td><code>Storyboard</code>, <code>MyTableViewCell</code>, UI 연결</td>
</tr>
<tr>
<td><strong>Controller</strong></td>
<td><code>ViewController</code>, <code>DetailViewController</code>, <code>MapViewController</code> 등에서 사용자 상호작용 처리</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-리팩토링-전후-핵심-변경사항-요약">✅ 리팩토링 전/후 핵심 변경사항 요약</h2>
<table>
<thead>
<tr>
<th>리팩토링 전</th>
<th>리팩토링 후</th>
</tr>
</thead>
<tbody><tr>
<td><code>ViewController</code>에 모델/로직/뷰 관련 코드가 섞여 있음</td>
<td>Model과 분리하여 로직을 <code>MovieService</code>로 이동</td>
</tr>
<tr>
<td><code>makeYesterdayString()</code>과 <code>getData()</code>가 Controller에 있음</td>
<td>날짜 포맷과 네트워크 로직을 Model 계층으로 이동</td>
</tr>
<tr>
<td>뷰에 표시할 데이터 직접 처리</td>
<td>Model에서 데이터를 가공하여 Controller에 전달</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-1-model-📁-modelmoviemodelswift">✅ 1. Model (📁 <code>Model/MovieModel.swift</code>)</h2>
<pre><code class="language-swift">import Foundation

struct MovieData: Codable {
    let boxOfficeResult: BoxOfficeResult
}

struct BoxOfficeResult: Codable {
    let dailyBoxOfficeList: [DailyBoxOfficeList]
}

struct DailyBoxOfficeList: Codable {
    let movieNm: String
    let audiCnt: String
    let audiAcc: String
    let rank: String
}</code></pre>
<hr />
<h2 id="✅-2-model---서비스-로직-분리-📁-modelmovieserviceswift">✅ 2. Model - 서비스 로직 분리 (📁 <code>Model/MovieService.swift</code>)</h2>
<pre><code class="language-swift">import Foundation

class MovieService {
    static let shared = MovieService()

    private let baseURL = &quot;https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=4b8c2206c2b38d5e037d886bbcca7ebf&amp;targetDt=&quot;

    func getYesterdayString() -&gt; String {
        let calendar = Calendar.current
        let today = Date()
        guard let yesterday = calendar.date(byAdding: .day, value: -1, to: today) else { return &quot;&quot; }

        let formatter = DateFormatter()
        formatter.dateFormat = &quot;yyyyMMdd&quot;
        return formatter.string(from: yesterday)
    }

    func fetchMovies(completion: @escaping (MovieData?) -&gt; Void) {
        let urlStr = baseURL + getYesterdayString()
        guard let url = URL(string: urlStr) else { completion(nil); return }

        URLSession.shared.dataTask(with: url) { data, _, error in
            guard let data = data, error == nil else { completion(nil); return }
            do {
                let decoded = try JSONDecoder().decode(MovieData.self, from: data)
                completion(decoded)
            } catch {
                print(&quot;Decoding error:&quot;, error)
                completion(nil)
            }
        }.resume()
    }
}</code></pre>
<hr />
<h2 id="✅-3-controller-📁-controllerviewcontrollerswift">✅ 3. Controller (📁 <code>Controller/ViewController.swift</code>)</h2>
<pre><code class="language-swift">import UIKit

class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    @IBOutlet weak var table: UITableView!
    var movieData: [DailyBoxOfficeList] = []

    override func viewDidLoad() {
        super.viewDidLoad()
        table.delegate = self
        table.dataSource = self
        fetchData()
    }

    func fetchData() {
        MovieService.shared.fetchMovies { [weak self] data in
            guard let self = self, let result = data?.boxOfficeResult.dailyBoxOfficeList else { return }
            DispatchQueue.main.async {
                self.movieData = result
                self.table.reloadData()
            }
        }
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -&gt; Int {
        return movieData.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -&gt; UITableViewCell {
        let movie = movieData[indexPath.row]
        let cell = tableView.dequeueReusableCell(withIdentifier: &quot;myCell&quot;, for: indexPath) as! MyTableViewCell
        cell.movieName.text = &quot;[\(movie.rank)위] \(movie.movieNm)&quot;
        cell.audiCount.text = &quot;어제: \(formatNumber(movie.audiCnt))명&quot;
        cell.audiAccumulate.text = &quot;누적: \(formatNumber(movie.audiAcc))명&quot;
        return cell
    }

    func formatNumber(_ value: String) -&gt; String {
        let formatter = NumberFormatter()
        formatter.numberStyle = .decimal
        let intVal = Int(value) ?? 0
        return formatter.string(for: intVal) ?? value
    }

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        performSegue(withIdentifier: &quot;toDetail&quot;, sender: indexPath)
    }

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == &quot;toDetail&quot;,
           let indexPath = sender as? IndexPath,
           let dest = segue.destination as? DetailViewController {
            dest.movieName = movieData[indexPath.row].movieNm
        }
    }

    func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -&gt; String? {
        return &quot;박스오피스 (영화진흥위원회 제공: \(MovieService.shared.getYesterdayString()))&quot;
    }

    func tableView(_ tableView: UITableView, titleForFooterInSection section: Int) -&gt; String? {
        return &quot;made by KYK&quot;
    }

    func numberOfSections(in tableView: UITableView) -&gt; Int {
        return 1
    }
}</code></pre>
<hr />
<h2 id="✅-4-view-mytableviewcellswift-detailviewcontrollerswift-mapviewcontrollerswift">✅ 4. View (<code>MyTableViewCell.swift</code>, <code>DetailViewController.swift</code>, <code>MapViewController.swift</code>)</h2>
<p>→ 이미 View만 담당하므로 수정 필요 없음.
필요하다면 View 쪽도 <code>configure(with:)</code> 같은 메서드를 만들어 View 설정만 하도록 할 수 있습니다.</p>
<hr />
<p>필요하시다면, <code>폴더 구조</code>, <code>Storyboard 설정</code>, <code>파일 분리 예시</code>, 또는 전체 zip 패키징 구조 예시도 추가로 안내드릴 수 있어요. 어떤 부분 도와드릴까요?</p>