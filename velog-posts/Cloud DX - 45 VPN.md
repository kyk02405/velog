# Cloud DX - 45 VPN

- 📅 Published: Mon, 24 Nov 2025 08:46:54 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-45-VPN)

<hr />
<h1 id="span-style--colorskyblue08-vpnspan"><span style="color: skyblue;">08. VPN</span></h1>
<h2 id="81-일반">8.1 일반</h2>
<h3 id="개요">개요</h3>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0286a6c1-4304-40ae-9766-122b60d19566/image.png" /></p>
<ul>
<li>가상 사설망을 말한다.</li>
<li>회사의 본사와 지사들의 네트워크를 독점적으로 구성하는 <code>기업 전용선</code>의 <code>장점</code>을 그대로 이용하고 <code>단점</code>인 비용이 비싸다는 문제를 해결해주는 서비스를 말한다.</li>
<li>큰 범위에서의 <code>인트라넷(Intranet)</code>과 같은 망 구성을 가지고 있다.</li>
</ul>
<h2 id="82-실습-1">8.2 실습 1.</h2>
<h3 id="시스템-구성">시스템 구성</h3>
<ul>
<li><p><code>VPN Server 1대(SRV100)</code>의 <code>VPN Client 1대(Client100)</code></p>
<blockquote>
<ul>
<li><code>VPN Server(SRV100)</code></li>
</ul>
</blockquote>
<ul>
<li>기본 설정<ul>
<li><code>라우팅 및 원격 액세스</code> -&gt; <code>SRV100</code> 우클릭 후 사용 안 함 -&gt; 구성 및 사용 </li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ada0dfca-6fb5-406a-96e0-919b64e9988b/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/256030fb-4073-452b-a857-ec075d5fd3be/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/04f52269-122b-486a-9d8b-cb0a65a6f4f9/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4aa61747-5931-4358-8a6d-eb8172591a60/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ccc28758-5c26-4a3f-9d9e-edb7f3360daf/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8eaca739-5198-460e-964e-9ff33dfc961b/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/73191a5b-ae05-4ced-ba37-ce01fbd9aecc/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/94076cc9-a509-4cc5-8dc1-ad3af848f8b3/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ed8f3249-4505-4bf5-b20d-2c07f5b672a7/image.png" /></li>
</ul>
</li>
<li><code>VPN Service</code>를 사용할 사용자 생성 <code>(SRV100)</code><ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/28a757ff-329c-45e7-94e7-e28ce243a0c5/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c7b4531b-0a5e-46c0-9b5f-a36e437d648d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/96cfd964-8dbc-4724-bffa-6ad511a3cfee/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/228c9cdb-cffb-4e53-8f2b-7ff69833066a/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p><code>VPN Client(Client 100)</code></p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4de8cd44-12c7-46d8-a2f3-26d0158be8e9/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/104869a7-9976-4df4-99d5-116d80976caf/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b848091b-e613-4168-a6f1-f7c6d727c38d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/acd9f216-357d-496b-9fef-9e10939f6e1e/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ab3e42d7-c070-4931-91bf-91ecd7500ec4/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/348f0553-5a52-4d5d-9ce3-54e3ce047af8/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3c385906-5e99-4701-9e6c-afdae4dd579d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/22482be6-734b-4803-b39e-2495cee47833/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0dde78a7-b0f3-42e1-b22b-9c5163185172/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f8546b23-9b61-4656-9e24-6f57183fd07c/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4d9c411d-70a2-42e2-bdeb-af16e3bd3b8e/image.png" /></li>
<li><code>server</code>에서 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4523be65-a3e2-465f-8547-1c549867ddf5/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0d86c879-e2e9-4343-bf48-375b094b7c6b/image.png" /></li>
</ul>
</li>
</ul>