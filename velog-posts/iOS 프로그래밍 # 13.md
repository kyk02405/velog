<hr />
<h2 id="클로저">클로저</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/46b769f2-12ef-4edc-93a9-f340f148c42c/image.png" /></p>
<p>클로저(closure)를 지원하는 프로그래밍 언어들은 함수형 프로그래밍 패러다임을 채택했거나 현대 프로그래밍 언어의 주요 기능으로 클로저를 포함한 경우가 많습니다. 아래는 클로저를 지원하는 대표적인 프로그래밍 언어들입니다:</p>
<h3 id="1-자바스크립트-javascript">1. <strong>자바스크립트 (JavaScript)</strong></h3>
<ul>
<li><p><strong>특징:</strong> 함수 내에서 선언된 변수가 함수 외부에서 참조될 수 있도록 캡처하는 클로저를 기본적으로 지원합니다.  </p>
</li>
<li><p><strong>예제:</strong> </p>
<pre><code class="language-javascript">function outer() {
  let count = 0;
  return function inner() {
    count++;
    console.log(count);
  };
}

const counter = outer();
counter(); // 1
counter(); // 2</code></pre>
</li>
</ul>
<h3 id="2-파이썬-python">2. <strong>파이썬 (Python)</strong></h3>
<ul>
<li><p><strong>특징:</strong> 함수가 반환된 후에도 내부 함수가 외부 함수의 변수에 접근할 수 있는 클로저를 제공합니다.  </p>
</li>
<li><p><strong>예제:</strong></p>
<pre><code class="language-python">def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(count)
    return inner

counter = outer()
counter()  # 1
counter()  # 2</code></pre>
</li>
</ul>
<h3 id="3-루비-ruby">3. <strong>루비 (Ruby)</strong></h3>
<ul>
<li><p><strong>특징:</strong> 블록, 프로시저, 람다(lambda) 등을 통해 클로저를 구현합니다.  </p>
</li>
<li><p><strong>예제:</strong> </p>
<pre><code class="language-ruby">def outer
  count = 0
  return Proc.new {
    count += 1
    puts count
  }
end

counter = outer
counter.call  # 1
counter.call  # 2</code></pre>
</li>
</ul>
<h3 id="4-스칼라-scala">4. <strong>스칼라 (Scala)</strong></h3>
<ul>
<li><p><strong>특징:</strong> 함수형 프로그래밍을 지원하며 클로저를 사용해 외부 변수에 접근 가능합니다.  </p>
</li>
<li><p><strong>예제:</strong></p>
<pre><code class="language-scala">def outer(): () =&gt; Unit = {
  var count = 0
  () =&gt; {
    count += 1
    println(count)
  }
}

val counter = outer()
counter() // 1
counter() // 2</code></pre>
</li>
</ul>
<h3 id="5-고-go">5. <strong>고 (Go)</strong></h3>
<ul>
<li><p><strong>특징:</strong> 클로저를 지원하며 익명 함수로 구현 가능합니다.  </p>
</li>
<li><p><strong>예제:</strong></p>
<pre><code class="language-go">package main

import &quot;fmt&quot;

func outer() func() {
    count := 0
    return func() {
        count++
        fmt.Println(count)
    }
}

func main() {
    counter := outer()
    counter() // 1
    counter() // 2
}</code></pre>
</li>
</ul>
<h3 id="6-하스켈-haskell">6. <strong>하스켈 (Haskell)</strong></h3>
<ul>
<li><strong>특징:</strong> 함수형 언어로 클로저는 기본적으로 모든 함수에서 사용됩니다.  </li>
<li><strong>예제:</strong> <pre><code class="language-haskell">outer = 
    let count = 0
    in \_ -&gt; do
        let count = count + 1
        print count</code></pre>
</li>
</ul>
<h3 id="7-c">7. <strong>C#</strong></h3>
<ul>
<li><p><strong>특징:</strong> 익명 메서드와 람다 식으로 클로저를 구현합니다.  </p>
</li>
<li><p><strong>예제:</strong> </p>
<pre><code class="language-csharp">using System;

class Program {
    static Func&lt;int&gt; Outer() {
        int count = 0;
        return () =&gt; {
            count++;
            Console.WriteLine(count);
            return count;
        };
    }

    static void Main() {
        var counter = Outer();
        counter(); // 1
        counter(); // 2
    }
}</code></pre>
</li>
</ul>
<h3 id="8-자바-java">8. <strong>자바 (Java)</strong></h3>
<ul>
<li><p><strong>특징:</strong> 자바 8부터 람다 표현식을 통해 클로저를 지원합니다.  </p>
</li>
<li><p><strong>예제:</strong></p>
<pre><code class="language-java">import java.util.function.Supplier;

public class Main {
    public static void main(String[] args) {
        Supplier&lt;Runnable&gt; outer = () -&gt; {
            int[] count = {0}; // effectively final
            return () -&gt; {
                count[0]++;
                System.out.println(count[0]);
            };
        };

        Runnable counter = outer.get();
        counter.run(); // 1
        counter.run(); // 2
    }
}</code></pre>
</li>
</ul>
<h3 id="9-러스트-rust">9. <strong>러스트 (Rust)</strong></h3>
<ul>
<li><p><strong>특징:</strong> 클로저를 함수형 프로그래밍 스타일로 기본 지원합니다.  </p>
</li>
<li><p><strong>예제:</strong></p>
<pre><code class="language-rust">fn outer() -&gt; impl FnMut() {
    let mut count = 0;
    move || {
        count += 1;
        println!(&quot;{}&quot;, count);
    }
}

fn main() {
    let mut counter = outer();
    counter(); // 1
    counter(); // 2
}</code></pre>
</li>
</ul>
<h3 id="10-php">10. <strong>PHP</strong></h3>
<ul>
<li><p><strong>특징:</strong> 익명 함수와 <code>use</code> 키워드를 통해 클로저를 지원합니다.  </p>
</li>
<li><p><strong>예제:</strong></p>
<pre><code class="language-php">&lt;?php
function outer() {
    $count = 0;
    return function() use (&amp;$count) {
        $count++;
        echo $count . &quot;\n&quot;;
    };
}

$counter = outer();
$counter(); // 1
$counter(); // 2</code></pre>
</li>
</ul>
<h3 id="결론">결론</h3>
<p>많은 현대 프로그래밍 언어는 클로저를 지원하며, 함수형 프로그래밍의 핵심 요소로 클로저를 활용합니다. 클로저를 통해 상태를 캡처하고 재사용할 수 있어 개발 과정에서 매우 유용합니다.</p>
<p>더 자세한 프로그래밍 지식은 <a href="https://gptonline.ai/ko/">GPTOnline</a>에서 확인하세요!</p>
<hr />
<h2 id="span-style-colorred-add1의-자료형-span"><span style="color: red;"> add1의 자료형 </span></h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/093a3bf8-1122-48f6-8116-3daa4c7f03cf/image.png" /></p>
<p>시험에 나옴</p>
<hr />
<h2 id="후행-클로저">후행 클로저</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ed2a7fc7-a6b5-483d-a7dd-664b234f2030/image.png" /></p>
<hr />
<h2 id=""></h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4601f1a7-241c-4d14-86e3-85fc8a372ce2/image.png" /></p>
<p>이 코드는 Swift에서 함수, 클로저, 그리고 고차 함수의 사용을 보여주는 예제입니다. 각각의 구성 요소를 하나씩 살펴보겠습니다.</p>
<hr />
<h3 id="1-add-함수">1. <strong><code>add</code> 함수</strong></h3>
<pre><code class="language-swift">func add(x: Int, y: Int) -&gt; Int {
    return x + y
}
print(add(x: 3, y: 5)) // 출력: 8
print(type(of: add))   // 출력: (Int, Int) -&gt; Int</code></pre>
<ul>
<li><strong><code>add</code> 함수</strong>는 두 개의 정수를 더해서 반환합니다.</li>
<li><strong><code>type(of:)</code></strong> 함수는 특정 객체의 타입을 반환합니다. 여기서는 <code>add</code> 함수의 타입이 <code>(Int, Int) -&gt; Int</code>임을 보여줍니다.<br />이는 두 개의 <code>Int</code>를 입력으로 받아 하나의 <code>Int</code>를 반환하는 함수 타입입니다.</li>
</ul>
<hr />
<h3 id="2-클로저-add1">2. <strong>클로저 <code>add1</code></strong></h3>
<pre><code class="language-swift">let add1 = { (x: Int, y: Int) -&gt; Int in
    return x + y
}
print(add1(2, 3)) // 출력: 5</code></pre>
<ul>
<li><strong><code>add1</code></strong>은 함수 대신 사용할 수 있는 클로저입니다.  <ul>
<li><code>(x: Int, y: Int) -&gt; Int</code>는 두 정수를 입력받아 <code>Int</code>를 반환하는 클로저의 타입입니다.</li>
<li>클로저 내부에서는 <code>in</code> 키워드로 클로저의 매개변수와 본문을 구분합니다.</li>
</ul>
</li>
<li><strong><code>add1(2, 3)</code></strong>은 클로저를 호출하여 두 정수를 더한 결과를 반환합니다.</li>
</ul>
<hr />
<h3 id="3-math-함수">3. <strong><code>math</code> 함수</strong></h3>
<pre><code class="language-swift">func math(x: Int, y: Int, cal: (Int, Int) -&gt; Int) -&gt; Int {
    return cal(x, y) // add(1, 2)
}
print(math(x: 1, y: 2, cal: add1)) // 출력: 3</code></pre>
<ul>
<li><strong><code>math</code> 함수</strong>는 <strong>고차 함수</strong>입니다. 고차 함수란 다른 함수를 매개변수로 받거나, 반환하는 함수를 말합니다.</li>
<li><code>math</code> 함수는 두 정수 <code>x</code>와 <code>y</code>를 입력으로 받고, 세 번째 매개변수 <code>cal</code>로 전달받은 함수를 호출하여 결과를 반환합니다.<ul>
<li><strong><code>cal(x, y)</code></strong>는 <code>cal</code>에 전달된 함수나 클로저를 호출한 결과를 반환합니다.</li>
</ul>
</li>
<li>여기서는 <code>cal</code>로 <code>add1</code> 클로저를 전달했기 때문에, <code>1 + 2</code>의 결과가 출력됩니다.</li>
</ul>
<hr />
<h3 id="4-익명-클로저-사용">4. <strong>익명 클로저 사용</strong></h3>
<pre><code class="language-swift">var a = math(x: 10, y: 20, cal: { (x: Int, y: Int) -&gt; Int in
    return x + y
})
print(a) // 출력: 30</code></pre>
<ul>
<li>클로저를 직접 전달할 때 <strong>익명 클로저</strong>를 사용할 수 있습니다. </li>
<li>위 코드는 <code>math</code> 함수의 <code>cal</code> 매개변수로 <code>(x, y) -&gt; Int</code> 형태의 익명 클로저를 전달하여 <code>10 + 20</code>의 결과를 반환합니다.</li>
</ul>
<hr />
<h3 id="5-후행-클로저-사용">5. <strong>후행 클로저 사용</strong></h3>
<pre><code class="language-swift">a = math(x: 100, y: 200) { (x: Int, y: Int) -&gt; Int in
    return x + y
}
print(a) // 출력: 300</code></pre>
<ul>
<li><strong>후행 클로저</strong>는 함수의 마지막 매개변수로 전달된 클로저를 함수 호출 괄호 바깥에 작성하는 방식입니다.</li>
<li><code>math</code> 함수의 <code>cal</code> 매개변수로 전달된 클로저가 후행 클로저로 작성되어 있습니다.</li>
<li>결과적으로 <code>100 + 200</code>의 결과를 반환합니다.</li>
</ul>
<hr />
<h3 id="요약">요약</h3>
<ol>
<li><strong><code>add</code> 함수와 <code>add1</code> 클로저</strong>:<ul>
<li>동일한 역할을 수행하지만, <code>add1</code>은 함수가 아닌 클로저로 정의됨.</li>
</ul>
</li>
<li><strong><code>math</code> 함수</strong>:<ul>
<li>두 정수와 클로저를 받아 계산 결과를 반환하는 고차 함수.</li>
</ul>
</li>
<li><strong>익명 클로저</strong>:<ul>
<li>클로저를 이름 없이 <code>math</code> 함수에 전달.</li>
</ul>
</li>
<li><strong>후행 클로저</strong>:<ul>
<li>클로저를 더 간결하게 전달할 수 있는 방식.</li>
</ul>
</li>
</ol>
<p>이 코드는 클로저를 정의하고 사용하는 다양한 방법을 보여줌과 동시에, Swift의 함수형 프로그래밍 개념을 학습하는 데 유용한 예제입니다.</p>
<hr />
<p>더 많은 Swift 관련 자료는 <a href="https://gptonline.ai/ko/">GPTOnline</a>에서 확인하세요!</p>