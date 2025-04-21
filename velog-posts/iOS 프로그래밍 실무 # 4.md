<hr />
<h1 id="appdelegateswift">AppDelegate.swift</h1>
<pre><code class="language-swift">//
//  AppDelegate.swift
//  ddd
//
//  Created by CMAC_43 on 2025/03/26.
//</code></pre>
<p>👉 이 부분은 파일 헤더 주석입니다.  </p>
<ul>
<li>파일 이름: <code>AppDelegate.swift</code>  </li>
<li>프로젝트 이름: <code>ddd</code>  </li>
<li>작성자: <code>CMAC_43</code>  </li>
<li>작성일: 2025년 3월 26일</li>
</ul>
<pre><code class="language-swift">import UIKit</code></pre>
<p>👉 UIKit 프레임워크를 가져옵니다.<br />iOS 앱 개발 시 필수적으로 사용하는 UI 관련 프레임워크입니다.</p>
<pre><code class="language-swift">@main
class AppDelegate: UIResponder, UIApplicationDelegate {</code></pre>
<p>👉 <code>AppDelegate</code> 클래스 선언입니다.  </p>
<ul>
<li><code>@main</code>: 이 클래스가 앱의 진입점이라는 뜻입니다. 앱이 실행될 때 가장 먼저 실행됩니다.  </li>
<li><code>UIResponder</code>: 이벤트에 반응할 수 있는 기본 클래스입니다.  </li>
<li><code>UIApplicationDelegate</code>: 앱의 생명주기 이벤트(실행, 종료 등)를 처리할 수 있게 해주는 프로토콜입니다.</li>
</ul>
<hr />
<pre><code class="language-swift">    func application(_ application: UIApplication, 
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -&gt; Bool {</code></pre>
<p>👉 앱이 실행된 후 호출되는 메서드입니다.  </p>
<ul>
<li>초기 설정, SDK 초기화, 사용자 설정 불러오기 등을 여기에 작성합니다.</li>
</ul>
<pre><code class="language-swift">        // Override point for customization after application launch.
        return true</code></pre>
<p>👉 앱이 성공적으로 실행되었음을 나타내며, <code>true</code>를 반환합니다.</p>
<hr />
<pre><code class="language-swift">    // MARK: UISceneSession Lifecycle</code></pre>
<p>👉 <code>Xcode</code>에서 코드 구역을 나누기 위한 주석입니다.  </p>
<ul>
<li><code>UISceneSession</code> 관련 메서드들이 아래에 있다는 표시입니다.</li>
</ul>
<pre><code class="language-swift">    func application(_ application: UIApplication, 
                     configurationForConnecting connectingSceneSession: UISceneSession, 
                     options: UIScene.ConnectionOptions) -&gt; UISceneConfiguration {</code></pre>
<p>👉 새로운 씬(화면/윈도우)을 생성할 때 호출되는 메서드입니다.<br />멀티윈도우 또는 멀티씬을 지원하는 앱에서 사용됩니다.</p>
<pre><code class="language-swift">        // Called when a new scene session is being created.
        // Use this method to select a configuration to create the new scene with.
        return UISceneConfiguration(name: &quot;Default Configuration&quot;, sessionRole: connectingSceneSession.role)</code></pre>
<p>👉 &quot;Default Configuration&quot;이라는 이름의 기본 설정을 반환합니다.<br />어떤 씬을 만들지 설정할 수 있습니다.</p>
<hr />
<pre><code class="language-swift">    func application(_ application: UIApplication, 
                     didDiscardSceneSessions sceneSessions: Set&lt;UISceneSession&gt;) {</code></pre>
<p>👉 사용자가 씬 세션을 종료했을 때 호출됩니다.</p>
<pre><code class="language-swift">        // Called when the user discards a scene session.
        // If any sessions were discarded while the application was not running,
        // this will be called shortly after application:didFinishLaunchingWithOptions.
        // Use this method to release any resources that were specific to the discarded scenes, as they will not return.</code></pre>
<p>👉 종료된 씬과 관련된 자원을 해제할 때 사용합니다.<br />예: 특정 뷰 컨트롤러에 종속된 메모리 등을 정리할 수 있습니다.</p>
<hr />
<h1 id="scenedelegateswift">SceneDelegate.swift</h1>
<p>아래는 <code>SceneDelegate.swift</code> 파일의 모든 줄에 대한 상세한 주석 설명입니다.</p>
<pre><code class="language-swift">//
//  SceneDelegate.swift
//  ddd
//
//  Created by CMAC_43 on 2025/03/26.
//</code></pre>
<p>👉 파일 정보 주석입니다.  </p>
<ul>
<li>파일 이름: <code>SceneDelegate.swift</code>  </li>
<li>프로젝트 이름: <code>ddd</code>  </li>
<li>생성자: CMAC_43  </li>
<li>생성일: 2025년 3월 26일</li>
</ul>
<hr />
<pre><code class="language-swift">import UIKit</code></pre>
<p>👉 UIKit 프레임워크를 가져옵니다.<br />iOS의 UI를 구성하기 위한 필수 프레임워크입니다.</p>
<hr />
<pre><code class="language-swift">class SceneDelegate: UIResponder, UIWindowSceneDelegate {</code></pre>
<p>👉 <code>SceneDelegate</code> 클래스 선언입니다.  </p>
<ul>
<li><code>UIResponder</code>: 이벤트에 응답할 수 있는 기본 클래스입니다.  </li>
<li><code>UIWindowSceneDelegate</code>: 씬 생명주기 관련 이벤트를 처리할 수 있게 해주는 프로토콜입니다.  </li>
<li>이 클래스는 iOS 13 이후 도입된 <strong>멀티 씬 지원</strong>을 위해 사용됩니다.</li>
</ul>
<hr />
<pre><code class="language-swift">    var window: UIWindow?</code></pre>
<p>👉 앱에서 UI를 표현하는 창(<code>UIWindow</code>) 객체입니다.<br />스토리보드를 사용할 경우 자동으로 연결됩니다.<br />코드로 UI를 구성할 경우 이 <code>window</code>를 직접 생성해 연결합니다.</p>
<hr />
<pre><code class="language-swift">    func scene(_ scene: UIScene, 
               willConnectTo session: UISceneSession, 
               options connectionOptions: UIScene.ConnectionOptions) {</code></pre>
<p>👉 새로운 씬이 처음 생성될 때 호출됩니다.  </p>
<ul>
<li>앱의 초기 UI를 설정하거나, 특정 상태로 열고 싶을 때 사용합니다.</li>
</ul>
<pre><code class="language-swift">        // Use this method to optionally configure and attach the UIWindow `window` to the provided UIWindowScene `scene`.
        // If using a storyboard, the `window` property will automatically be initialized and attached to the scene.
        // This delegate does not imply the connecting scene or session are new (see `application:configurationForConnectingSceneSession` instead).</code></pre>
<p>👉 스토리보드를 사용할 경우 자동으로 <code>window</code>가 연결되므로, 특별한 설정이 없으면 수정할 필요가 없습니다.</p>
<pre><code class="language-swift">        guard let _ = (scene as? UIWindowScene) else { return }</code></pre>
<p>👉 전달받은 <code>scene</code>이 <code>UIWindowScene</code> 타입이 아닐 경우 아무 작업도 하지 않습니다.<br />안전하게 타입 캐스팅을 수행합니다.</p>
<hr />
<pre><code class="language-swift">    func sceneDidDisconnect(_ scene: UIScene) {</code></pre>
<p>👉 씬이 시스템에 의해 종료될 때 호출됩니다.  </p>
<ul>
<li>백그라운드로 들어가거나, 메모리 절약을 위해 시스템이 씬을 제거할 때 사용됩니다.</li>
</ul>
<pre><code class="language-swift">        // Called as the scene is being released by the system.
        // This occurs shortly after the scene enters the background, or when its session is discarded.
        // Release any resources associated with this scene that can be re-created the next time the scene connects.
        // The scene may re-connect later, as its session was not necessarily discarded (see `application:didDiscardSceneSessions` instead).</code></pre>
<p>👉 씬에 관련된 리소스를 정리할 때 사용됩니다. 예: 타이머 종료, 데이터 저장 등.</p>
<hr />
<pre><code class="language-swift">    func sceneDidBecomeActive(_ scene: UIScene) {</code></pre>
<p>👉 씬이 <strong>활성 상태</strong>가 되었을 때 호출됩니다.<br />(예: 화면이 다시 보일 때)</p>
<pre><code class="language-swift">        // Called when the scene has moved from an inactive state to an active state.
        // Use this method to restart any tasks that were paused (or not yet started) when the scene was inactive.</code></pre>
<p>👉 멈춘 작업을 재시작하거나, UI를 다시 업데이트할 수 있습니다.</p>
<hr />
<pre><code class="language-swift">    func sceneWillResignActive(_ scene: UIScene) {</code></pre>
<p>👉 씬이 <strong>비활성 상태</strong>로 전환되기 직전에 호출됩니다.<br />(예: 전화 수신, 알림 수신 등 일시적인 중단)</p>
<pre><code class="language-swift">        // Called when the scene will move from an active state to an inactive state.
        // This may occur due to temporary interruptions (ex. an incoming phone call).</code></pre>
<p>👉 작업 일시 중지 등을 수행할 수 있습니다.</p>
<hr />
<pre><code class="language-swift">    func sceneWillEnterForeground(_ scene: UIScene) {</code></pre>
<p>👉 씬이 <strong>백그라운드 → 포그라운드</strong>로 전환되기 직전에 호출됩니다.</p>
<pre><code class="language-swift">        // Called as the scene transitions from the background to the foreground.
        // Use this method to undo the changes made on entering the background.</code></pre>
<p>👉 백그라운드에서 바뀐 UI나 상태를 원래대로 되돌릴 수 있습니다.</p>
<hr />
<pre><code class="language-swift">    func sceneDidEnterBackground(_ scene: UIScene) {</code></pre>
<p>👉 씬이 <strong>포그라운드 → 백그라운드</strong>로 전환되었을 때 호출됩니다.</p>
<pre><code class="language-swift">        // Called as the scene transitions from the foreground to the background.
        // Use this method to save data, release shared resources, and store enough scene-specific state information
        // to restore the scene back to its current state.</code></pre>
<p>👉 사용자 데이터를 저장하거나, 리소스를 해제하고, 상태 복구를 위한 정보를 저장하는 곳입니다.<br />(예: 앱을 껐다가 다시 실행했을 때 이어지도록 하기 위함)</p>
<hr />
<h1 id="viewcontrollerswift">ViewController.swift</h1>
<p>아래는 <code>ViewController.swift</code> 파일의 각 줄에 대한 주석 설명입니다.</p>
<pre><code class="language-swift">import UIKit</code></pre>
<p>👉 <code>UIKit</code> 프레임워크를 가져옵니다.<br />iOS 앱에서 UI 구성 요소(버튼, 레이블 등)를 사용하기 위해 필수로 임포트합니다.</p>
<hr />
<pre><code class="language-swift">class ViewController: UIViewController {</code></pre>
<p>👉 <code>ViewController</code> 클래스 선언입니다.  </p>
<ul>
<li><code>UIViewController</code>를 상속받아 뷰 컨트롤러 역할을 합니다.  </li>
<li>하나의 화면(뷰)을 관리하고, 뷰의 생명주기 이벤트를 처리할 수 있습니다.</li>
</ul>
<hr />
<pre><code class="language-swift">    override func viewDidLoad() {
        super.viewDidLoad()</code></pre>
<p>👉 뷰 컨트롤러의 뷰가 메모리에 <strong>로드</strong>된 직후 호출되는 메서드입니다.  </p>
<ul>
<li>앱 실행 후 가장 먼저 실행되는 메서드 중 하나입니다.  </li>
<li>여기서 초기 UI 설정, 데이터 초기화 등을 할 수 있습니다.</li>
</ul>
<pre><code class="language-swift">        // Do any additional setup after loading the view.</code></pre>
<p>👉 뷰가 로드된 후 추가 설정을 할 수 있는 부분입니다.<br />예: 배경색 설정, 버튼 생성, API 호출 등</p>
<hr />
<pre><code class="language-swift">    }

}</code></pre>
<p>👉 <code>viewDidLoad</code>와 <code>ViewController</code> 클래스의 끝을 나타냅니다.</p>
<hr />
<h2 id=""></h2>
<pre><code class="language-swift">func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -&gt; UISceneConfiguration</code></pre>
<h3 id="🔹-이-함수는-언제-호출되나요">🔹 이 함수는 언제 호출되나요?</h3>
<ul>
<li><strong>새로운 씬(Scene)이 생성될 때</strong> 호출됩니다.  </li>
<li>예를 들어 앱을 처음 실행하거나, iPad처럼 <strong>멀티 윈도우 기능</strong>을 지원하는 기기에서 사용자가 새로운 윈도우를 열 때 이 메서드가 실행됩니다.</li>
</ul>
<hr />
<h3 id="🔹-함수의-각-파라미터-설명">🔹 함수의 각 파라미터 설명</h3>
<h4 id="application-uiapplication"><code>application: UIApplication</code></h4>
<ul>
<li>현재 실행 중인 앱 객체입니다.</li>
<li>앱 전체의 상태나 설정을 가져올 때 사용할 수 있습니다.</li>
</ul>
<h4 id="connectingscenesession-uiscenesession"><code>connectingSceneSession: UISceneSession</code></h4>
<ul>
<li><strong>새롭게 연결될 씬 세션</strong>에 대한 정보를 담고 있는 객체입니다.</li>
<li>어떤 역할(예: 일반 UI, 외부 디스플레이 등)을 맡을 씬인지 알 수 있습니다.</li>
</ul>
<h4 id="options-uisceneconnectionoptions"><code>options: UIScene.ConnectionOptions</code></h4>
<ul>
<li>이 씬을 생성하게 된 <strong>상황/옵션</strong>에 대한 정보입니다.</li>
<li>예를 들어 푸시 알림을 눌러 앱이 열렸다면, 어떤 알림이었는지 등의 정보를 여기에 담고 있습니다.</li>
</ul>
<hr />
<h3 id="🔹-반환값-uisceneconfiguration">🔹 반환값: <code>UISceneConfiguration</code></h3>
<ul>
<li>새로 생성될 씬의 <strong>구성 정보</strong>를 담은 객체입니다.</li>
<li>여기서 어떤 스토리보드, 어떤 delegate 클래스를 사용할지 지정합니다.</li>
</ul>
<p>예를 들어 기본적으로는 이렇게 반환합니다:</p>
<pre><code class="language-swift">return UISceneConfiguration(name: &quot;Default Configuration&quot;, sessionRole: connectingSceneSession.role)</code></pre>
<h4 id="구성-요소-설명">구성 요소 설명:</h4>
<ul>
<li><code>name</code>: Info.plist의 <code>Application Scene Manifest</code>에 설정된 이름과 일치해야 합니다. <code>&quot;Default Configuration&quot;</code>이 일반적입니다.</li>
<li><code>sessionRole</code>: 이 씬이 어떤 역할을 할지 나타냅니다.<br />예: <code>.windowApplication</code> (일반적인 앱 UI), <code>.windowExternalDisplay</code> (외부 화면 표시용)</li>
</ul>
<hr />
<h3 id="🔹-요약하면">🔹 요약하면</h3>
<p>이 함수는:</p>
<ul>
<li>&quot;지금 새로운 화면(씬)을 만들려는데, 어떤 설정으로 만들까?&quot;를 결정하는 자리입니다.</li>
<li>대부분의 경우 기본 <code>&quot;Default Configuration&quot;</code>을 사용합니다.</li>
<li>특별한 상황(예: 다른 화면을 다른 UI로 만들고 싶을 때)이 아니면 수정할 일이 적습니다.</li>
</ul>
<hr />
<h3 id="✅-예시-커스텀-설정">✅ 예시: 커스텀 설정</h3>
<p>스토리보드 없이 코드로 UI를 구성하고 싶을 때는 이렇게 작성할 수 있습니다:</p>
<pre><code class="language-swift">let config = UISceneConfiguration(name: &quot;Custom Config&quot;, sessionRole: connectingSceneSession.role)
config.delegateClass = MySceneDelegate.self
return config</code></pre>
<p><code>MySceneDelegate</code>는 우리가 직접 만든 <code>SceneDelegate</code> 대체 클래스입니다.</p>
<hr />
<h1 id="_-사용-이유">_ 사용 이유</h1>
<p>Swift에서 <code>_</code>는 <strong>외부 파라미터 이름 생략자(external parameter name omitter)</strong> 라고 해요.</p>
<hr />
<h3 id="🔹-이-코드에서의-_">🔹 이 코드에서의 <code>_</code>:</h3>
<pre><code class="language-swift">func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -&gt; UISceneConfiguration</code></pre>
<p>여기서 <code>_ application: UIApplication</code> 은<br />함수를 <strong>호출할 때 첫 번째 파라미터 이름을 생략하겠다</strong>는 의미입니다.</p>
<hr />
<h3 id="🔸-외부-파라미터-이름이란">🔸 외부 파라미터 이름이란?</h3>
<p>Swift에서는 함수 호출 시 매개변수 이름을 명시적으로 적는 걸 선호합니다.</p>
<p>예:</p>
<pre><code class="language-swift">func sayHello(to name: String) {
    print(&quot;Hello, \(name)&quot;)
}

sayHello(to: &quot;경윤&quot;) // ✅ 외부 이름(to:)을 사용함</code></pre>
<hr />
<h3 id="🔸-그런데-_-를-쓰면">🔸 그런데 <code>_</code> 를 쓰면?</h3>
<pre><code class="language-swift">func sayHello(_ name: String) {
    print(&quot;Hello, \(name)&quot;)
}

sayHello(&quot;경윤&quot;) // ✅ 외부 이름 없이 호출 가능</code></pre>
<p><code>_</code> 덕분에 <code>sayHello(&quot;경윤&quot;)</code>처럼 간결하게 쓸 수 있어요.</p>
<hr />
<h3 id="🔸-이-함수에선-왜-_를-쓸까">🔸 이 함수에선 왜 <code>_</code>를 쓸까?</h3>
<p><code>UIApplicationDelegate</code> 프로토콜은 Apple이 미리 정의한 형식이기 때문에,
Swift 스타일에 맞게 <strong>첫 번째 인자는 외부 이름 없이 호출되도록 <code>_</code>를 사용</strong>한 거예요.</p>
<blockquote>
<p>즉, 시스템이 내부적으로 이 메서드를 호출할 때<br /><code>application(:configurationForConnecting:options:)</code> 형태로 호출되기 때문에<br /><code>_</code>로 첫 번째 파라미터의 외부 이름을 생략한 것입니다.</p>
</blockquote>
<hr />
<h3 id="✅-정리">✅ 정리</h3>
<table>
<thead>
<tr>
<th>구문</th>
<th>의미</th>
</tr>
</thead>
<tbody><tr>
<td><code>_</code></td>
<td>외부에서 함수 호출할 때 <strong>파라미터 이름을 생략</strong>하겠다는 뜻</td>
</tr>
</tbody></table>
<hr />
<h1 id="🔹-swift-함수-파라미터-이름-구조">🔹 Swift 함수 파라미터 이름 구조</h1>
<p>Swift 함수는 각 매개변수에 두 가지 이름을 가질 수 있어요:</p>
<pre><code class="language-swift">func someFunction(외부이름 내부이름: 타입)</code></pre>
<ul>
<li><strong>외부 이름 (external parameter name)</strong>: 함수 <strong>호출 시</strong> 사용하는 이름  </li>
<li><strong>내부 이름 (internal parameter name)</strong>: 함수 <strong>본문 내에서</strong> 사용하는 이름</li>
</ul>
<hr />
<h2 id="🔸-예시로-이해해보자">🔸 예시로 이해해보자!</h2>
<pre><code class="language-swift">func greet(person name: String) {
    print(&quot;Hello, \(name)!&quot;)
}</code></pre>
<ul>
<li>호출 시: <code>greet(person: &quot;Kyungyoon&quot;)</code>  </li>
<li>내부에서: <code>name</code> 이라는 이름으로 사용</li>
</ul>
<hr />
<h2 id="🔸-그럼-이-코드를-다시-보면">🔸 그럼 이 코드를 다시 보면:</h2>
<pre><code class="language-swift">func application(_ application: UIApplication,
                 configurationForConnecting connectingSceneSession: UISceneSession,
                 options: UIScene.ConnectionOptions) -&gt; UISceneConfiguration</code></pre>
<p>여기서:</p>
<table>
<thead>
<tr>
<th>구문</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>configurationForConnecting</code></td>
<td><strong>외부 이름</strong> – 시스템이 함수 호출할 때 사용하는 이름</td>
</tr>
<tr>
<td><code>connectingSceneSession</code></td>
<td><strong>내부 이름</strong> – 함수 내부에서 사용하는 변수 이름</td>
</tr>
</tbody></table>
<hr />
<h2 id="🔹-왜-이렇게-쓰는-걸까">🔹 왜 이렇게 쓰는 걸까?</h2>
<p>이 함수는 Apple이 정의한 <strong>UIApplicationDelegate 프로토콜</strong>에 포함되어 있는 메서드인데요,<br />시스템이 자동으로 이 메서드를 호출할 때는 <strong>외부 파라미터 이름을 기준으로</strong> 호출합니다.</p>
<p>예를 들어 내부적으로 시스템은 아래와 같은 느낌으로 호출하는 거예요:</p>
<pre><code class="language-swift">appDelegate.application(_:configurationForConnecting:options:)</code></pre>
<hr />
<h2 id="✅-요약하면">✅ 요약하면</h2>
<table>
<thead>
<tr>
<th>이름 구문</th>
<th>용도</th>
</tr>
</thead>
<tbody><tr>
<td><code>configurationForConnecting</code></td>
<td>외부에서 메서드를 호출할 때 사용하는 이름 (system call용)</td>
</tr>
<tr>
<td><code>connectingSceneSession</code></td>
<td>메서드 내부에서 이 값을 참조할 때 쓰는 이름</td>
</tr>
</tbody></table>
<hr />
<p>##</p>
<p>네, 아주 잘 정리하셨어요! 말씀하신 내용을 기반으로 <strong>함수, 매개변수(parameter), 인수(argument)</strong> 개념을 한 번 더 <strong>쉽고 명확하게 정리</strong>해드릴게요.</p>
<hr />
<h2 id="✅-함수란">✅ 함수란?</h2>
<blockquote>
<p><strong>특정 작업을 수행</strong>하기 위해 만들어진 <strong>코드 블록</strong>입니다.</p>
</blockquote>
<ul>
<li>입력값을 받아서(<code>parameter</code>),  </li>
<li>내부에서 어떤 작업을 하고,  </li>
<li>결과를 반환하거나 출력할 수 있습니다.</li>
</ul>
<hr />
<h1 id="✅-매개변수parameter-vs-인수argument">✅ 매개변수(Parameter) vs 인수(Argument)</h1>
<table>
<thead>
<tr>
<th>구분</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>매개변수</strong> (Parameter)</td>
<td>함수 <strong>정의 시</strong> 사용하는 변수 이름 (형식 매개변수 / formal parameter)</td>
</tr>
<tr>
<td><strong>인수</strong> (Argument)</td>
<td>함수 <strong>호출 시</strong> 전달하는 실제 값 (실제 매개변수 / actual parameter)</td>
</tr>
</tbody></table>
<blockquote>
<p>💡 간단히 말해,  </p>
<ul>
<li><strong>parameter = 변수 이름</strong>,  </li>
<li><strong>argument = 실제 값</strong> 이라고 기억하면 됩니다.</li>
</ul>
</blockquote>
<hr />
<h2 id="🔸-예시로-이해하기-c-코드-기반">🔸 예시로 이해하기 (C 코드 기반)</h2>
<pre><code class="language-c">#include &lt;stdio.h&gt;

void Fun(int param)  // param은 매개변수(parameter)
{
    printf(&quot;%d&quot;, param);
}

int main() {
    Fun(10);         // 10은 인수(argument)
    return 0;
}</code></pre>
<ul>
<li>여기서 <code>param</code> → 함수 <code>Fun</code>이 정의될 때 쓰인 <strong>매개변수</strong></li>
<li><code>10</code> → <code>Fun</code>을 호출할 때 전달한 <strong>인수</strong></li>
</ul>
<hr />
<h2 id="🔸-swift에서도-동일">🔸 Swift에서도 동일</h2>
<pre><code class="language-swift">func greet(name: String) {  // name은 매개변수(Parameter)
    print(&quot;Hello, \(name)&quot;)
}

greet(name: &quot;경윤&quot;)         // &quot;경윤&quot;은 인수(Argument)</code></pre>
<hr />
<h2 id="✅-정리-1">✅ 정리</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th>시점</th>
<th>예시 코드</th>
</tr>
</thead>
<tbody><tr>
<td>매개변수(parameter)</td>
<td>함수 정의할 때</td>
<td><code>func greet(name: String)</code>의 <code>name</code></td>
</tr>
<tr>
<td>인수(argument)</td>
<td>함수 호출할 때</td>
<td><code>greet(name: &quot;경윤&quot;)</code>의 <code>&quot;경윤&quot;</code></td>
</tr>
</tbody></table>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8dcb322e-1412-431c-8deb-a83bff32aa43/image.png" /></p>
<h1 id="argument-label--parameter-name">Argument label , Parameter name</h1>
<p>업로드해주신 이미지 정말 잘 만들어졌어요! 아래에 있는 내용을 바탕으로 다시 한 번 <strong>깔끔하게 요약</strong>해드릴게요.</p>
<hr />
<h2 id="✅-핵심-요약-내부-vs-외부-매개변수-이름">✅ 핵심 요약: 내부 vs 외부 매개변수 이름</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th>역할</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td><strong>내부 매개변수</strong> (<code>parameter name</code>)</td>
<td>함수 <strong>내부에서</strong> 사용하는 이름</td>
<td><code>x</code>, <code>y</code></td>
</tr>
<tr>
<td><strong>외부 매개변수</strong> (<code>argument label</code>)</td>
<td>함수 <strong>호출 시</strong> 사용하는 이름</td>
<td><code>first</code>, <code>second</code></td>
</tr>
</tbody></table>
<hr />
<h2 id="📌-함수-정의-예시">📌 함수 정의 예시</h2>
<pre><code class="language-swift">func add(first x: Int, second y: Int) -&gt; Int {
    return x + y
}</code></pre>
<ul>
<li><code>first</code> / <code>second</code>: <strong>외부 이름</strong> → 함수 호출할 때 사용  </li>
<li><code>x</code> / <code>y</code>: <strong>내부 이름</strong> → 함수 내부에서 연산 시 사용</li>
</ul>
<p>📛 <code>return(first + second)</code> → ❌ <strong>오류</strong><br />✅ <code>return(x + y)</code> → 함수 내부에서는 <strong>내부 이름 사용</strong></p>
<hr />
<h2 id="📌-함수-호출-예시">📌 함수 호출 예시</h2>
<pre><code class="language-swift">add(first: 10, second: 20) // ✅ 올바른 호출
add(x: 10, y: 20)          // ❌ 외부 이름이 아님</code></pre>
<hr />
<h2 id="✅-외부-이름-생략한-버전">✅ 외부 이름 생략한 버전</h2>
<pre><code class="language-swift">func add(x: Int, y: Int) -&gt; Int {
    return x + y
}

add(x: 10, y: 20)  // ✅ 여기선 내부/외부 이름 동일</code></pre>
<p>🔸 <strong>외부 이름을 생략하면</strong>, 내부 이름이 외부 이름 역할도 함께 합니다.</p>
<hr />
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0cc8c821-8c17-4697-bed2-35bed05fa659/image.png" /></p>
<h2 id="🧃-자판기-비유-이미지-속-그림">🧃 자판기 비유 (이미지 속 그림)</h2>
<ul>
<li><strong>입력</strong>: 인수 (arguments) → 버튼 누르기  </li>
<li><strong>출력</strong>: 함수 결과  </li>
<li><strong>내부 처리</strong>: 매개변수(parameter)를 이용해 연산 수행</li>
</ul>
<hr />
<h1 id="함수의-이름">함수의 이름</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/495578d4-7810-4d98-896c-fc19f92f05e6/image.png" /></p>
<hr />
<h2 id="✅-1-외부-이름과-내부-이름을-따로-지정한-경우">✅ 1. 외부 이름과 내부 이름을 따로 지정한 경우</h2>
<pre><code class="language-swift">func add(first x: Int, second y: Int) -&gt; Int {
    print(#function)
    return x + y
}
print(add(first: 5, second: 10))</code></pre>
<ul>
<li>호출 시: <code>add(first: 5, second: 10)</code> ✅</li>
<li><code>first</code> / <code>second</code>는 외부 이름, <code>x</code> / <code>y</code>는 내부 이름</li>
<li>출력:<pre><code>add(first:second:)
15</code></pre></li>
</ul>
<hr />
<h2 id="✅-2-외부와-내부-이름이-동일한-경우-생략-안-함">✅ 2. 외부와 내부 이름이 동일한 경우 (생략 안 함)</h2>
<pre><code class="language-swift">func add(x: Int, y: Int) -&gt; Int {
    print(#function)
    return x + y
}
print(add(x: 10, y: 20))</code></pre>
<ul>
<li>호출 시: <code>add(x: 10, y: 20)</code> ✅</li>
<li>외부/내부 모두 <code>x</code>, <code>y</code></li>
<li>출력:<pre><code>add(x:y:)
30</code></pre></li>
</ul>
<hr />
<h2 id="✅-3-외부-이름을-생략한-경우-_-사용">✅ 3. 외부 이름을 생략한 경우 (<code>_</code> 사용)</h2>
<pre><code class="language-swift">func add(_ x: Int, _ y: Int) -&gt; Int {
    print(#function)
    return x + y
}
print(add(1, 2))</code></pre>
<ul>
<li>호출 시: <code>add(1, 2)</code> ✅</li>
<li>외부 이름이 없어서 인자만 넣으면 됨</li>
<li>출력:<pre><code>add(_:_:)
3</code></pre></li>
</ul>
<hr />
<h2 id="✅-4-혼합형--첫-번째는-생략-두-번째는-외부-이름-지정">✅ 4. 혼합형 – 첫 번째는 생략, 두 번째는 외부 이름 지정</h2>
<pre><code class="language-swift">func add(_ x: Int, with y: Int) -&gt; Int {
    print(#function)
    return x + y
}
print(add(5, with: 2))</code></pre>
<ul>
<li>호출 시: <code>add(5, with: 2)</code> ✅</li>
<li>첫 번째는 외부 이름 없음 (<code>_</code>), 두 번째는 <code>with</code></li>
<li>출력:<pre><code>add(_:with:)
7</code></pre></li>
</ul>
<hr />
<h2 id="🎯-function-이란">🎯 <code>#function</code> 이란?</h2>
<p><code>#function</code>은 해당 코드가 실행되고 있는 <strong>함수의 전체 시그니처</strong>를 문자열로 출력해주는 Swift의 디버깅 도구입니다. 함수 이름 + 외부 매개변수명이 나와요.</p>
<hr />
<h2 id="✅-전체-실행-결과-요약">✅ 전체 실행 결과 요약</h2>
<pre><code class="language-plaintext">add(first:second:)
15
add(x:y:)
30
add(_:_:)
3
add(_:with:)
7</code></pre>
<hr />
<h1 id="클래스에-저장-프로퍼티stored-property-추가하기">클래스에 저장 프로퍼티(stored property) 추가하기</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a79e12de-e96d-4fcf-8714-861d1763fd12/image.png" /></p>
<hr />
<h2 id="❗️오류-메시지-해석">❗️오류 메시지 해석</h2>
<pre><code class="language-swift">class Man {
    var age: Int
    var weight: Double
}</code></pre>
<p>이 코드에서 발생한 에러는 다음과 같습니다:</p>
<pre><code>error: class 'Man' has no initializers
stored property 'age' without initial value prevents synthesized initializers
stored property 'weight' without initial value prevents synthesized initializers</code></pre><hr />
<h2 id="✅-이유-설명">✅ 이유 설명</h2>
<p>Swift에서 <strong>클래스의 저장 프로퍼티</strong>는 반드시 다음 셋 중 하나로 초기화가 되어야 합니다:</p>
<ol>
<li><strong>초기값을 직접 줄 것</strong>  </li>
<li><strong><code>init</code> 생성자에서 초기화할 것</strong>  </li>
<li><strong>옵셔널(<code>?</code>)로 선언해서 자동으로 nil로 초기화되게 할 것</strong></li>
</ol>
<p>그런데 현재는:</p>
<ul>
<li><code>var age: Int</code> → 초기값 없음  </li>
<li><code>var weight: Double</code> → 초기값 없음  </li>
<li>생성자(<code>init</code>)도 없음  </li>
<li>옵셔널도 아님  </li>
</ul>
<p>👉 그래서 <strong>컴파일러가 초기화 방법을 알 수 없기 때문에 에러 발생</strong>!</p>
<hr />
<h2 id="✅-해결-방법-3가지">✅ 해결 방법 3가지</h2>
<h3 id="1-초기값을-직접-지정">1. 초기값을 직접 지정</h3>
<pre><code class="language-swift">class Man {
    var age: Int = 0
    var weight: Double = 0.0
}</code></pre>
<hr />
<h3 id="2-초기화-생성자init-사용">2. 초기화 생성자(<code>init</code>) 사용</h3>
<pre><code class="language-swift">class Man {
    var age: Int
    var weight: Double

    init(age: Int, weight: Double) {
        self.age = age
        self.weight = weight
    }
}</code></pre>
<hr />
<h3 id="3-옵셔널로-선언">3. 옵셔널로 선언</h3>
<pre><code class="language-swift">class Man {
    var age: Int?
    var weight: Double?
}</code></pre>
<blockquote>
<p>이 경우 자동으로 <code>nil</code>로 초기화됨</p>
</blockquote>
<hr />
<h2 id="💡-정리">💡 정리</h2>
<table>
<thead>
<tr>
<th>선언 형태</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>var age: Int = 0</code></td>
<td>✅ 기본값을 지정</td>
</tr>
<tr>
<td><code>var age: Int?</code></td>
<td>✅ 옵셔널이므로 초기값 필요 없음</td>
</tr>
<tr>
<td><code>var age: Int</code></td>
<td>❌ 오류 — 생성자(init) 없이 초기화 안 됨</td>
</tr>
</tbody></table>
<hr />
<p>이미지에 있는 질문 <code>&quot;// 오류 나는 이유?&quot;</code>의 답은:</p>
<blockquote>
<p><strong>초기값 없이 저장 프로퍼티를 선언했지만, 생성자(init)도 없어서 컴파일러가 자동 초기화해줄 수 없기 때문입니다.</strong></p>
</blockquote>
<hr />
<h1 id="designated-initializer">Designated initializer</h1>
<p>Swift에서 <strong>initializer(생성자)</strong> 는 객체를 만들 때 초기값을 설정하는 함수인데,<br />그 중에서도 <strong>designated initializer</strong>(지정 이니셜라이저)는 매우 중요한 개념이에요.</p>
<hr />
<h2 id="✅-designated-initializer-지정-이니셜라이저란">✅ designated initializer (지정 이니셜라이저)란?</h2>
<blockquote>
<p>클래스에서 <strong>모든 저장 프로퍼티를 반드시 초기화</strong>하고,<br /><strong>상위 클래스의 이니셜라이저를 호출</strong>하는 <strong>기본 이니셜라이저</strong>를 말합니다.</p>
</blockquote>
<p>한마디로 <strong>&quot;객체를 만들기 위한 핵심 초기화 함수&quot;</strong>예요.</p>
<hr />
<h2 id="🔸-예시">🔸 예시:</h2>
<pre><code class="language-swift">class Person {
    var name: String
    var age: Int

    // ✅ Designated initializer
    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }
}</code></pre>
<ul>
<li>이 <code>init(name:age:)</code>는 <strong>모든 저장 프로퍼티</strong>를 초기화하고 있기 때문에<br /><strong>designated initializer</strong>입니다.</li>
</ul>
<hr />
<h2 id="✅-designated-initializer의-특징">✅ designated initializer의 특징</h2>
<table>
<thead>
<tr>
<th>특징</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>필수 조건</td>
<td>모든 저장 프로퍼티를 초기화해야 함</td>
</tr>
<tr>
<td>상속 관계</td>
<td>상속 시에는 반드시 <strong>super.init()</strong> 호출해야 함</td>
</tr>
<tr>
<td>다른 이니셜라이저가 호출함</td>
<td><code>convenience initializer</code>가 이걸 호출함</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-상속-예시">✅ 상속 예시</h2>
<pre><code class="language-swift">class Person {
    var name: String

    init(name: String) {   // ✅ 지정 이니셜라이저
        self.name = name
    }
}

class Student: Person {
    var grade: Int

    init(name: String, grade: Int) {  // ✅ 서브클래스의 지정 이니셜라이저
        self.grade = grade
        super.init(name: name)        // ✅ 반드시 상위 클래스 지정 init 호출
    }
}</code></pre>
<hr />
<h2 id="✅-convenience-initializer와의-차이">✅ convenience initializer와의 차이</h2>
<table>
<thead>
<tr>
<th>구분</th>
<th>설명</th>
<th>목적</th>
</tr>
</thead>
<tbody><tr>
<td><strong>designated</strong></td>
<td>모든 프로퍼티를 초기화함</td>
<td><strong>기본 구조 초기화</strong></td>
</tr>
<tr>
<td><strong>convenience</strong></td>
<td>일부 설정만 담당, 반드시 다른 init 호출</td>
<td><strong>편의성 제공</strong></td>
</tr>
</tbody></table>
<pre><code class="language-swift">class Person {
    var name: String

    init(name: String) {
        self.name = name
    }

    // ✅ 편의 생성자
    convenience init() {
        self.init(name: &quot;Unknown&quot;)
    }
}</code></pre>
<hr />
<h2 id="📌-정리">📌 정리</h2>
<table>
<thead>
<tr>
<th>용어</th>
<th>의미</th>
</tr>
</thead>
<tbody><tr>
<td>designated initializer</td>
<td>기본 초기화 담당. 저장 프로퍼티 모두 초기화, 상위 클래스 init 호출</td>
</tr>
<tr>
<td>convenience initializer</td>
<td>다른 init을 기반으로 보조 초기화. 반드시 <code>self.init()</code> 호출</td>
</tr>
</tbody></table>
<hr />
<h1 id="코드-설명">코드 설명</h1>
<pre><code class="language-swift">class Man {</code></pre>
<p>👉 <code>Man</code>이라는 이름의 클래스를 정의합니다.<br />(사람 객체를 나타내는 사용자 정의 타입)</p>
<hr />
<pre><code class="language-swift">    var age: Int</code></pre>
<p>👉 <code>age</code>라는 정수형(Int) 저장 프로퍼티를 선언합니다.<br />→ 사람의 나이를 저장할 공간</p>
<hr />
<pre><code class="language-swift">    var weight: Double</code></pre>
<p>👉 <code>weight</code>라는 실수형(Double) 저장 프로퍼티를 선언합니다.<br />→ 사람의 몸무게를 저장할 공간</p>
<hr />
<pre><code class="language-swift">    func display() {
        print(&quot;나이=\(age), 몸무게=\(weight)&quot;)
    }</code></pre>
<p>👉 <code>display()</code>라는 인스턴스 메서드 정의  </p>
<ul>
<li>이 메서드는 <code>age</code>, <code>weight</code> 값을 출력합니다.  </li>
<li><code>self</code> 생략됨 → 클래스 내부에서 프로퍼티 직접 접근 가능</li>
</ul>
<p>📌 출력 예시:</p>
<pre><code>나이=20, 몸무게=35.5</code></pre><hr />
<pre><code class="language-swift">    init(Age: Int, Weight: Double) {</code></pre>
<p>👉 지정 생성자(designated initializer) 정의  </p>
<ul>
<li>외부에서 전달받은 <code>Age</code>, <code>Weight</code> 값을 사용하여<br />내부 프로퍼티를 초기화합니다.</li>
</ul>
<p>⚠️ <strong>여기 주의!</strong></p>
<ul>
<li><code>Age</code>와 <code>age</code>는 <strong>대소문자가 다른 변수이므로 다른 이름</strong>입니다.</li>
</ul>
<hr />
<pre><code class="language-swift">        self.age = age
        self.weight = weight</code></pre>
<p>👉 ❌ <strong>오류 발생하는 부분!</strong></p>
<p>여기서 <code>age</code>와 <code>weight</code>는 <strong>정의된 매개변수 이름이 아님</strong>  </p>
<ul>
<li>위 init의 매개변수는 <code>Age</code>, <code>Weight</code> (대문자 A, W)</li>
</ul>
<p>따라서 올바르게 고치려면 다음과 같아야 해요:</p>
<pre><code class="language-swift">self.age = Age
self.weight = Weight</code></pre>
<hr />
<pre><code class="language-swift">    } // designated initializer 끝
}</code></pre>
<p>👉 클래스 <code>Man</code> 정의 끝</p>
<hr />
<pre><code class="language-swift">var han = Man(Age: 20, Weight: 35.5)</code></pre>
<p>👉 <code>Man</code> 클래스의 인스턴스를 생성합니다.  </p>
<ul>
<li>생성자 <code>init(Age:Weight:)</code>를 호출하며  </li>
<li><code>han</code>이라는 변수에 그 객체를 저장</li>
</ul>
<hr />
<pre><code class="language-swift">han.display()</code></pre>
<p>👉 <code>han</code> 인스턴스의 <code>display()</code> 메서드를 호출하여<br />→ 나이와 몸무게를 출력</p>
<hr />
<h2 id="🔥-전체-수정본-에러-없이-작동하도록">🔥 전체 수정본 (에러 없이 작동하도록)</h2>
<pre><code class="language-swift">class Man {
    var age: Int
    var weight: Double

    func display() {
        print(&quot;나이=\(age), 몸무게=\(weight)&quot;)
    }

    init(Age: Int, Weight: Double) {
        self.age = Age   // ✅ 대소문자 구분 정확히
        self.weight = Weight
    }
}

var han = Man(Age: 20, Weight: 35.5)
han.display()</code></pre>
<hr />
<h2 id="✅-실행-결과">✅ 실행 결과</h2>
<pre><code>나이=20, 몸무게=35.5</code></pre><hr />
<h1 id="상속된-클래스의-초기화-순서">상속된 클래스의 초기화 순서</h1>
<pre><code class="language-swift">init(age: Int, weight: Double, name: String) {
    self.name = name             ✅ 가능
    super.init(age: age, weight: weight)
}</code></pre>
<p>✅ 이렇게 하면 <strong>정상 작동</strong>합니다.</p>
<p>하지만 <strong>순서를 바꾸면 오류</strong>가 발생합니다:</p>
<pre><code class="language-swift">init(age: Int, weight: Double, name: String) {
    super.init(age: age, weight: weight)
    self.name = name             ❌ 에러!
}</code></pre>
<hr />
<h2 id="❗️왜-이럴까">❗️왜 이럴까?</h2>
<p>Swift는 <strong>초기화 순서에 대해 엄격한 규칙</strong>을 가지고 있습니다.</p>
<hr />
<h1 id="✅-swift-초기화-규칙-중요">✅ Swift 초기화 규칙 (중요!)</h1>
<ol>
<li><strong>자식 클래스의 저장 프로퍼티는</strong> <code>super.init()</code> 호출 <strong>이전</strong>에 <strong>모두 초기화되어야 함</strong>  </li>
<li>하지만 <strong><code>self</code>를 완전히 사용할 수 있는 건 <code>super.init()</code> 호출 이후부터</strong>임</li>
</ol>
<hr />
<h2 id="🔍-다시-적용해보면">🔍 다시 적용해보면</h2>
<pre><code class="language-swift">self.name = name  // ✅ OK: 자식 프로퍼티 먼저 초기화
super.init(...)   // ✅ OK: 부모 초기화

super.init(...)   // ❌ self를 완전히 사용하기 전에 호출
self.name = name  // ❌ self 접근 불가 → 컴파일 에러 발생</code></pre>
<p>📛 에러 메시지 예:</p>
<pre><code>'self' used before 'super.init' call</code></pre><hr />
<h2 id="🎯-정리-왜-순서가-중요한가">🎯 정리: 왜 순서가 중요한가?</h2>
<p>Swift는 안전을 위해:</p>
<ul>
<li><code>super.init()</code>이 호출되기 <strong>전에</strong>는 <code>self</code>를 완전히 사용할 수 없다고 판단합니다.</li>
<li><code>self.name = name</code>은 <code>self</code>를 사용하는 것이므로,
반드시 자식 프로퍼티를 <strong>모두 초기화한 다음</strong>에 <code>super.init</code>을 호출해야 합니다.</li>
</ul>
<p>즉, <code>self.name = name</code>은 <code>super.init</code> <strong>이전에 와야만</strong> 합니다.</p>
<hr />
<h2 id="✅-올바른-형태-요약">✅ 올바른 형태 요약</h2>
<pre><code class="language-swift">init(age: Int, weight: Double, name: String) {
    // 1. 자식 프로퍼티 먼저 초기화
    self.name = name
    // 2. 부모 초기화
    super.init(age: age, weight: weight)
}</code></pre>
<hr />
<h2 id="상속-초기화-메서드-오버라이딩">상속, 초기화, 메서드 오버라이딩</h2>
<p>Swift 코드의 <strong>모든 줄에 대한 상세 주석 설명</strong>입니다.<br />상속, 초기화, 메서드 오버라이딩까지 중요한 개념이 잘 들어간 예제예요!</p>
<hr />
<pre><code class="language-swift">class Man {</code></pre>
<p>👉 <code>Man</code>이라는 부모 클래스를 선언합니다.<br />사람이라는 개념을 표현하는 클래스입니다.</p>
<hr />
<pre><code class="language-swift">    var age: Int
    var weight: Double</code></pre>
<p>👉 <code>age</code>: 나이 (정수형),<br />👉 <code>weight</code>: 몸무게 (실수형)<br />→ 저장 프로퍼티(stored property)</p>
<hr />
<pre><code class="language-swift">    func display() {
        print(&quot;나이=\(age), 몸무게=\(weight)&quot;)
    }</code></pre>
<p>👉 <code>display()</code> 메서드는 <code>age</code>와 <code>weight</code> 값을 콘솔에 출력하는 함수입니다.<br />→ 이 함수는 나중에 자식 클래스에서 <strong>override</strong>(재정의) 됩니다.</p>
<hr />
<pre><code class="language-swift">    init(age: Int, weight: Double) {
        self.age = age
        self.weight = weight
    }</code></pre>
<p>👉 <strong>지정 이니셜라이저 (designated initializer)</strong>  </p>
<ul>
<li>매개변수로 전달된 값을 이용해 저장 프로퍼티들을 초기화합니다.  </li>
<li>이 생성자는 나중에 자식 클래스에서 <code>super.init()</code>으로 호출됩니다.</li>
</ul>
<hr />
<pre><code class="language-swift">class Student: Man {</code></pre>
<p>👉 <code>Student</code> 클래스는 <code>Man</code> 클래스를 <strong>상속</strong>받습니다.<br />즉, <code>Student</code>는 <code>Man</code>의 <code>age</code>, <code>weight</code>, <code>display()</code> 메서드 등을 자동으로 갖게 됩니다.</p>
<hr />
<pre><code class="language-swift">    var name: String</code></pre>
<p>👉 <code>Student</code> 클래스에 새롭게 추가된 프로퍼티<br />→ 학생의 이름을 저장하기 위한 문자열</p>
<hr />
<pre><code class="language-swift">    override func display() {
        print(&quot;이름=\(name), 나이=\(age), 몸무게=\(weight)&quot;)
    }</code></pre>
<p>👉 부모 클래스의 <code>display()</code> 메서드를 <strong>override(재정의)</strong> 합니다.  </p>
<ul>
<li>이제 <code>Student</code>의 <code>display()</code>는 이름까지 출력합니다.  </li>
<li><code>override</code> 키워드를 반드시 써야 함</li>
</ul>
<hr />
<pre><code class="language-swift">    init(age: Int, weight: Double, name: String) {
        self.name = name
        super.init(age: age, weight: weight)
    }</code></pre>
<p>👉 <code>Student</code> 클래스의 <strong>지정 이니셜라이저</strong></p>
<ul>
<li><code>self.name = name</code>: 자식 클래스의 프로퍼티를 먼저 초기화  </li>
<li><code>super.init(...)</code>: 부모 클래스의 초기화 함수 호출 → 반드시 필요!!</li>
</ul>
<p>📛 이 줄(<code>super.init(...)</code>)을 <strong>생략하면 에러 발생</strong>:</p>
<pre><code>error: 'super.init' isn't called on all paths before returning from initializer</code></pre><p>✅ 이유: Swift에서는 <strong>부모의 지정 이니셜라이저를 반드시 명시적으로 호출해야</strong> 하고,<br /><strong>호출 전에 자식 프로퍼티가 먼저 초기화되어야 함</strong> (초기화 순서 규칙)</p>
<hr />
<pre><code class="language-swift">} // Student 클래스 끝</code></pre>
<hr />
<pre><code class="language-swift">var lee: Student = Student(age: 20, weight: 65.2, name: &quot;홍길동&quot;)</code></pre>
<p>👉 <code>Student</code> 클래스의 인스턴스를 생성합니다.  </p>
<ul>
<li>이름: &quot;홍길동&quot;, 나이: 20, 몸무게: 65.2  </li>
<li>이때 <code>Student</code>의 init → 내부에서 <code>super.init</code> 호출됨 → 부모 초기화도 함께 진행됨</li>
</ul>
<hr />
<pre><code class="language-swift">lee.display()</code></pre>
<p>👉 <code>Student</code> 인스턴스의 <code>display()</code> 메서드를 호출  </p>
<ul>
<li>부모 메서드를 <strong>override</strong> 했기 때문에 <code>Student</code>의 display가 실행됨  </li>
<li>출력:<pre><code>이름=홍길동, 나이=20, 몸무게=65.2</code></pre></li>
</ul>
<hr />
<h2 id="✅-요약-정리">✅ 요약 정리</h2>
<table>
<thead>
<tr>
<th>요소</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>super.init(...)</code></td>
<td>부모 클래스의 초기화 메서드를 명시적으로 호출해야 함</td>
</tr>
<tr>
<td><code>override</code></td>
<td>부모의 메서드를 재정의할 때 반드시 사용</td>
</tr>
<tr>
<td>초기화 순서</td>
<td>자식 프로퍼티 초기화 → <code>super.init()</code> 호출 순으로 진행해야 함</td>
</tr>
<tr>
<td>호출 결과</td>
<td><code>lee.display()</code>는 <code>Student</code> 클래스에서 재정의한 내용이 실행됨</td>
</tr>
</tbody></table>
<hr />
<h1 id="delegate-design-pattern">Delegate design pattern</h1>
<p>좋은 질문이에요!  
<strong>델리게이트(delegate) 디자인 패턴</strong>은 iOS 개발(특히 Swift, UIKit)에서 정말 자주 쓰이는 <strong>핵심 패턴</strong>이에요.<br />쉽게 말하면, <strong>“대신 처리해줄 사람을 지정해서 일 맡기기”</strong> 개념이에요.</p>
<hr />
<h2 id="✅-델리게이트delegate-디자인-패턴이란">✅ 델리게이트(Delegate) 디자인 패턴이란?</h2>
<blockquote>
<p>어떤 객체가 해야 할 일을 <strong>자기 혼자 하지 않고</strong>,  
<strong>다른 객체에게 위임(delegate)</strong> 하는 디자인 패턴입니다.</p>
</blockquote>
<p>즉, <strong>&quot;내가 직접 처리하지 않고, 대신 처리할 수 있는 사람(delegate)을 지정해서 맡긴다&quot;</strong>는 의미예요.</p>
<hr />
<h2 id="🎯-언제-쓰나">🎯 언제 쓰나?</h2>
<ul>
<li>어떤 객체의 행동이나 이벤트 처리 결과를 <strong>다른 객체에게 전달하고 싶을 때</strong></li>
<li>대표적인 예: <code>UITableView</code>, <code>UITextField</code>, <code>UIScrollView</code>, <code>URLSession</code>, 등에서 자주 사용됨</li>
</ul>
<hr />
<h2 id="✅-예시-비유-자판기--알바생">✅ 예시 비유: 자판기 &amp; 알바생</h2>
<blockquote>
<p><strong>자판기(주체)</strong> 가 버튼이 눌리면 물건을 주는 대신,<br /><strong>알바생(델리게이트)</strong> 에게 &quot;버튼 눌렸으니 처리 좀 해줘&quot;라고 맡기는 구조</p>
</blockquote>
<hr />
<h2 id="✅-기본-구조-swift-기준">✅ 기본 구조 (Swift 기준)</h2>
<pre><code class="language-swift">protocol SomeDelegate {
    func didSomething()
}

class A {
    var delegate: SomeDelegate?

    func trigger() {
        // 어떤 일이 벌어졌을 때
        delegate?.didSomething()
    }
}

class B: SomeDelegate {
    func didSomething() {
        print(&quot;B가 대신 처리함!&quot;)
    }
}

let a = A()
let b = B()

a.delegate = b  // B를 대리인으로 지정
a.trigger()     // 결과: &quot;B가 대신 처리함!&quot;</code></pre>
<hr />
<h2 id="✅-ios에서-진짜-사용-예-uitableview">✅ iOS에서 진짜 사용 예 (UITableView)</h2>
<pre><code class="language-swift">class MyViewController: UIViewController, UITableViewDelegate {
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print(&quot;사용자가 \(indexPath.row)번째 셀을 눌렀어요!&quot;)
    }
}</code></pre>
<ul>
<li><code>UITableView</code>는 <strong>셀을 누른 이벤트</strong>를 스스로 처리하지 않고,</li>
<li><strong>델리게이트(MyViewController)</strong> 에게 위임합니다.</li>
</ul>
<hr />
<h2 id="✅-델리게이트-패턴의-장점">✅ 델리게이트 패턴의 장점</h2>
<table>
<thead>
<tr>
<th>장점</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>역할 분리</strong></td>
<td>객체 간의 책임을 나눌 수 있음</td>
</tr>
<tr>
<td><strong>유연성</strong></td>
<td>위임 대상(delegate)을 바꾸면 동작을 쉽게 바꿀 수 있음</td>
</tr>
<tr>
<td><strong>재사용성</strong></td>
<td>클래스가 범용적으로 재사용될 수 있음 (특정 동작은 delegate가 정의함)</td>
</tr>
</tbody></table>
<hr />
<h2 id="✅-정리-한-줄-요약">✅ 정리 한 줄 요약</h2>
<blockquote>
<p><strong>델리게이트 패턴</strong> = <strong>&quot;대신 처리해줄 사람(객체)을 정해서, 일을 맡기는 구조&quot;</strong></p>
</blockquote>
<hr />
<h1 id="protocol">Protocol</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8ae59aff-1d5f-42ac-baa7-4621fa3a0512/image.png" /></p>
<p>이미지 속 에러 메시지는 <strong>Swift 프로토콜에서 속성(property)을 선언할 때 반드시 <code>get</code> 또는 <code>get set</code>을 명시해야 한다</strong>는 의미입니다.</p>
<hr />
<h2 id="❗️에러-메시지-뜻">❗️에러 메시지 뜻:</h2>
<blockquote>
<p><strong>“Property in protocol must have explicit <code>{ get }</code> or <code>{ get set }</code> specifier”</strong><br />→ <strong>프로토콜의 프로퍼티는 반드시 읽기/쓰기 가능 여부를 명시해야 합니다.</strong></p>
</blockquote>
<hr />
<h2 id="🔎-왜-이런-에러가-나나요">🔎 왜 이런 에러가 나나요?</h2>
<pre><code class="language-swift">protocol Runnable {
    var x: Int    // ❌ 에러 발생
}</code></pre>
<p>위 코드에서 <code>var x: Int</code>라고만 쓰면<br />Swift는 <strong>&quot;x를 읽기만 할 수 있는지, 쓸 수 있는지도 되는지&quot;</strong>를 판단할 수 없기 때문에 에러가 발생합니다.</p>
<hr />
<h2 id="✅-해결-방법-2가지">✅ 해결 방법 2가지</h2>
<h3 id="1-읽기-전용-get만-허용">1. 읽기 전용 (get만 허용)</h3>
<pre><code class="language-swift">protocol Runnable {
    var x: Int { get }
}</code></pre>
<ul>
<li>이 경우, 해당 프로토콜을 따르는 타입은 <code>x</code>를 <strong>읽을 수만 있어야 함</strong></li>
<li>읽기 전용 속성</li>
</ul>
<hr />
<h3 id="2-읽기--쓰기-가능-get-set">2. 읽기 + 쓰기 가능 (get set)</h3>
<pre><code class="language-swift">protocol Runnable {
    var x: Int { get set }
}</code></pre>
<ul>
<li>이 경우, 해당 타입은 <code>x</code>를 <strong>읽고 쓰기 둘 다 가능</strong>해야 함</li>
<li>읽기/쓰기 가능한 속성</li>
</ul>
<hr />
<h2 id="💡-추가-설명">💡 추가 설명</h2>
<p>Swift에서 프로토콜은 &quot;이걸 따르는 타입은 이런 기능을 반드시 가져야 해!&quot;를 정의합니다.<br />그래서 변수도 단순히 <code>var x: Int</code>라고 쓰는 것만으로는 <strong>요구사항이 불명확</strong>해지기 때문에,<br /><strong>접근 제한자 (<code>get</code>, <code>set</code>)를 반드시 써야</strong> 하는 거예요.</p>
<hr />
<h2 id="✅-요약">✅ 요약</h2>
<table>
<thead>
<tr>
<th>선언 형태</th>
<th>의미</th>
</tr>
</thead>
<tbody><tr>
<td><code>var x: Int { get }</code></td>
<td>읽기 전용 속성</td>
</tr>
<tr>
<td><code>var x: Int { get set }</code></td>
<td>읽기 + 쓰기 가능한 속성</td>
</tr>
</tbody></table>
<hr />
<h1 id="fcd">fcd</h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/83e4fc1a-60c4-47a7-af2d-7bad48b210b7/image.png" /></p>
<p>지금 보신 에러는 Swift에서 아주 자주 나오는 프로토콜 관련 에러인데요,<br />이미지 속 메시지:</p>
<hr />
<h3 id="❗️에러-메시지-해석">❗️에러 메시지 해석:</h3>
<pre><code>Type 'Man' does not conform to protocol 'Runnable'</code></pre><p>👉 클래스 <code>Man</code>이 <code>Runnable</code> 프로토콜을 따르겠다고 했지만,<br /><strong>프로토콜의 요구사항을 모두 구현하지 않아서</strong> 발생하는 에러입니다.</p>
<hr />
<h2 id="✅-현재-프로토콜-선언">✅ 현재 프로토콜 선언</h2>
<pre><code class="language-swift">protocol Runnable {
    var x: Int { get set }  // 읽기/쓰기 가능한 변수 요구
    func run()              // run() 함수 요구
}</code></pre>
<hr />
<h2 id="❌-문제-코드">❌ 문제 코드</h2>
<pre><code class="language-swift">class Man: Runnable {
    // 아무 것도 구현 안 함 → 에러 발생!
}</code></pre>
<hr />
<h2 id="✅-해결-방법-요구사항을-전부-구현하기">✅ 해결 방법: 요구사항을 전부 구현하기</h2>
<pre><code class="language-swift">class Man: Runnable {
    var x: Int = 0           // ✅ 읽기/쓰기 가능한 프로퍼티 구현
    func run() {
        print(&quot;달리는 중!&quot;)
    }
}</code></pre>
<ul>
<li><code>var x: Int</code> 구현 → <code>{ get set }</code> 조건 만족</li>
<li><code>func run()</code> 구현 → 프로토콜 함수 구현 완료</li>
</ul>
<hr />
<h2 id="💡-팁-xcode의-fix-버튼-클릭하면">💡 팁: Xcode의 &quot;Fix&quot; 버튼 클릭하면?</h2>
<ul>
<li>자동으로 &quot;프로토콜 스텁(stub)&quot;을 추가해줍니다</li>
<li>아래처럼 자동완성됨:</li>
</ul>
<pre><code class="language-swift">var x: Int {
    get {
        // return some Int
    }
    set {
        // handle newValue
    }
}

func run() {
    // implement run
}</code></pre>
<p>👉 다만 위처럼 구현만 생기고, <strong>내용은 직접 채워야</strong> 해요</p>
<hr />
<h2 id="✅-요약-1">✅ 요약</h2>
<table>
<thead>
<tr>
<th>조건</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>var x: Int { get set }</code></td>
<td>저장 프로퍼티로 구현하거나 <code>get/set</code>을 모두 구현</td>
</tr>
<tr>
<td><code>func run()</code></td>
<td>클래스에서 반드시 함수 구현</td>
</tr>
</tbody></table>
<hr />
<h1 id="protocol-예시">Protocol 예시</h1>
<h2 id="🍽️-상황-설정">🍽️ 상황 설정</h2>
<ul>
<li><code>음식점</code>이라는 <strong>공통 개념</strong>이 있어요.</li>
<li><code>사장님</code>과 <code>아르바이트생</code>은 음식점에서 일하지만, <strong>역할이 다릅니다</strong>.</li>
<li>각각의 역할에 따라 해야 할 일이 정해져 있죠!</li>
</ul>
<hr />
<h2 id="✅-1-프로토콜-protocol-👉-역할-설명서">✅ 1. 프로토콜 (protocol) 👉 “역할 설명서”</h2>
<blockquote>
<p>&quot;음식점에서 일하는 사람은 무조건 <strong>일 시작하기(runWork)</strong> 기능이 있어야 해!&quot;<br />즉, &quot;일하는 사람&quot; 역할을 정한 것!</p>
</blockquote>
<pre><code class="language-swift">protocol Worker {
    var name: String { get set }
    func runWork()
}</code></pre>
<ul>
<li>이건 &quot;음식점에서 일하는 사람은 <strong>이름을 갖고 있고</strong>, <strong>일하는 기능이 있어야 한다</strong>&quot;는 규칙이에요.</li>
<li>이건 역할만 정의한 거고, 실제 내용은 아직 없어요.</li>
</ul>
<hr />
<h2 id="✅-2-상속-inheritance-👉-공통-성질을-물려주기">✅ 2. 상속 (inheritance) 👉 “공통 성질을 물려주기”</h2>
<blockquote>
<p>&quot;사람&quot;이라는 공통적인 성질(이름, 나이 등)을 가진 클래스를 만들고,<br />&quot;사장&quot;과 &quot;알바&quot;는 거기서 기능을 <strong>물려받아</strong> 더 추가해요.</p>
</blockquote>
<pre><code class="language-swift">class Person {
    var name: String
    init(name: String) {
        self.name = name
    }
}</code></pre>
<hr />
<h2 id="✅-3-사장님-클래스-상속--프로토콜-구현">✅ 3. 사장님 클래스 (상속 + 프로토콜 구현)</h2>
<pre><code class="language-swift">class Boss: Person, Worker {
    func runWork() {
        print(&quot;\(name): 오늘 가게 문 열고 재료 확인합니다.&quot;)
    }
}</code></pre>
<hr />
<h2 id="✅-4-아르바이트생-클래스-상속--프로토콜-구현">✅ 4. 아르바이트생 클래스 (상속 + 프로토콜 구현)</h2>
<pre><code class="language-swift">class PartTimer: Person, Worker {
    func runWork() {
        print(&quot;\(name): 손님 응대하고 설거지합니다.&quot;)
    }
}</code></pre>
<hr />
<h2 id="✅-5-실제로-사용해보면">✅ 5. 실제로 사용해보면:</h2>
<pre><code class="language-swift">let boss = Boss(name: &quot;사장님&quot;)
let partTimer = PartTimer(name: &quot;홍길동 알바생&quot;)

boss.runWork()
// 출력: 사장님: 오늘 가게 문 열고 재료 확인합니다.

partTimer.runWork()
// 출력: 홍길동 알바생: 손님 응대하고 설거지합니다.</code></pre>
<hr />
<h2 id="🎯-핵심-요약">🎯 핵심 요약</h2>
<table>
<thead>
<tr>
<th>개념</th>
<th>예시</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>protocol Worker</code></td>
<td>&quot;일하는 사람이라면 무조건 runWork()는 있어야 함!&quot;</td>
<td>공통 역할을 강제함</td>
</tr>
<tr>
<td><code>class Person</code></td>
<td>사람이라는 기본 틀</td>
<td>이름 등 공통 속성 포함</td>
</tr>
<tr>
<td><code>class Boss</code>, <code>class PartTimer</code></td>
<td>사장님, 알바생</td>
<td><code>Person</code>을 상속받고, <code>Worker</code> 프로토콜을 구현</td>
</tr>
</tbody></table>
<hr />
<h2 id="📌-한-줄-정리">📌 한 줄 정리</h2>
<ul>
<li><strong>프로토콜</strong> = <strong>“해야 할 일을 정한 계약서”</strong></li>
<li><strong>상속</strong> = <strong>“공통적인 속성을 물려주는 것”</strong></li>
</ul>
<hr />
<h1 id="protocol-예시-2">Protocol 예시 2</h1>
<h2 id="✅-예제-주제-동물을-모델로-해보자-🐶🐱">✅ 예제 주제: 동물을 모델로 해보자! 🐶🐱</h2>
<ul>
<li><code>Animal</code>: <strong>공통 속성</strong>을 가진 클래스 (상속용)</li>
<li><code>Runnable</code>: <strong>뛸 수 있는 동물</strong>만 사용하는 <strong>프로토콜</strong></li>
<li><code>Dog</code>, <code>Cat</code>: <code>Animal</code>을 <strong>상속받고</strong>, <code>Runnable</code>을 <strong>채택</strong></li>
</ul>
<hr />
<h2 id="🔸-코드-예제">🔸 코드 예제</h2>
<pre><code class="language-swift">// ✅ 프로토콜 정의
protocol Runnable {
    func run()
}

// ✅ Animal이라는 공통 클래스 정의 (이름을 가짐)
class Animal {
    var name: String

    init(name: String) {
        self.name = name
    }

    func speak() {
        print(&quot;\(name)이(가) 소리를 냅니다.&quot;)
    }
}

// ✅ Dog 클래스: Animal 상속 + Runnable 프로토콜 채택
class Dog: Animal, Runnable {
    func run() {
        print(&quot;\(name)이(가) 힘차게 달립니다! 🐕&quot;)
    }
}

// ✅ Cat 클래스: Animal 상속 + Runnable 프로토콜 채택
class Cat: Animal, Runnable {
    func run() {
        print(&quot;\(name)이(가) 조용히 달립니다... 🐈&quot;)
    }
}</code></pre>
<hr />
<h2 id="🔸-사용-예">🔸 사용 예</h2>
<pre><code class="language-swift">let dog = Dog(name: &quot;바둑이&quot;)
let cat = Cat(name: &quot;나비&quot;)

dog.speak()   // 바둑이이(가) 소리를 냅니다.
dog.run()     // 바둑이이(가) 힘차게 달립니다! 🐕

cat.speak()   // 나비이(가) 소리를 냅니다.
cat.run()     // 나비이(가) 조용히 달립니다... 🐈</code></pre>
<hr />
<h2 id="✅-개념-정리">✅ 개념 정리</h2>
<table>
<thead>
<tr>
<th>개념</th>
<th>설명</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td><strong>상속</strong></td>
<td>공통 속성과 기능을 물려받음</td>
<td><code>Dog</code>, <code>Cat</code>이 <code>Animal</code>을 상속</td>
</tr>
<tr>
<td><strong>프로토콜</strong></td>
<td>특정 역할(기능)을 강제함</td>
<td><code>Runnable</code>을 채택 → <code>run()</code> 필수 구현</td>
</tr>
<tr>
<td><strong>동시 사용</strong></td>
<td>클래스는 상속도 받고, 프로토콜도 채택 가능</td>
<td><code>class Dog: Animal, Runnable</code></td>
</tr>
</tbody></table>
<hr />
<h2 id="📌-비유로-이해">📌 비유로 이해</h2>
<table>
<thead>
<tr>
<th>개념</th>
<th>비유</th>
</tr>
</thead>
<tbody><tr>
<td><code>Animal</code> 클래스</td>
<td>“동물이라는 공통적인 틀” (이름, 말하기)</td>
</tr>
<tr>
<td><code>Runnable</code> 프로토콜</td>
<td>“뛸 수 있는 동물만 뛰는 법을 알아야 함”</td>
</tr>
<tr>
<td><code>Dog</code>, <code>Cat</code></td>
<td>동물의 성질을 갖고, 달릴 수 있는 동물로 정의</td>
</tr>
</tbody></table>