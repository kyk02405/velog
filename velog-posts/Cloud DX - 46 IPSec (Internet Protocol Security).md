# Cloud DX - 46 IPSec (Internet Protocol Security)

- 📅 Published: Mon, 24 Nov 2025 08:47:38 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-46-IPSec-Internet-Protocol-Security)

<hr />
<h1 id="span-style--colorskyblue09ipsec-internet-protocol-securityspan"><span style="color: skyblue;">09.IPSec (Internet Protocol Security)</span></h1>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9cc9f501-562c-4923-b7a3-50107b48e72c/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c57a6bb0-1288-4c9f-9a78-57e6d49e8804/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/de5e49a0-c805-43a5-8939-a5385e35eac7/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/368025dc-2788-42db-abe4-b1c728b74830/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f6e42fbd-1972-41a0-b2c2-62108e62f980/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4ae05461-f279-4dae-b9db-1747adc7f246/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f681a2f3-8160-4b50-96d6-12e871de7e80/image.png" /></p>
<h2 id="91-일반">9.1 일반</h2>
<h3 id="개요">개요</h3>
<h2 id="92-실습">9.2 실습</h2>
<h3 id="psk">PSK</h3>
<ul>
<li><p>시스템 구성</p>
<ul>
<li><code>SRV 100</code> , <code>Client100</code></li>
</ul>
</li>
<li><p>환경 구성</p>
<ul>
<li><code>HtoH</code>, <code>wf(x)</code> + <code>PSK</code></li>
</ul>
</li>
<li><p>설정 및 테스트</p>
<ul>
<li><p>Step 1.<code>SRV100</code> 또는 <code>Clinet100</code>에서 <code>wireshark</code>를 실행한 상태에서 <code>ping</code> 테스트를 실행한다.</p>
</li>
<li><p>Step 2. <code>wireshark</code>에 올라온 <code>Protocol</code>을 확인<code>(ICMP)</code> <code>SRV100</code>과 <code>Client100</code> 모두 동일한 결과가 나타난다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b2027c42-371e-4aea-8e4b-155507914c18/image.png" /></p>
</li>
<li><p>Step 3. <code>SRV100</code>에서 <code>로컬 보안 정책(secpol.msc)</code>을 </p>
</li>
<li><p>Step 4. <code>보안 설정</code> 하단에 있는 <code>IP 보안 정책</code>의 우측에서 우클릭 후<code>IP 보안 정책 만들기</code>를 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1a699d21-ad66-4769-8360-5d78513e77f2/image.png" /></p>
</li>
<li><p>Step 5. 기본값으로 둔 상태에서 계속 진행한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9a27876c-f7ca-419e-80c9-f2f863397209/image.png" /></p>
</li>
<li><p>Step 6. <code>새 IP 보안 정책 속성</code>창이 출력되면 하단에 있는 <code>추가</code>를 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9aea2cd0-5b76-4577-9fdb-b493fdf632c8/image.png" /></p>
</li>
<li><p>Step 7. <code>IP 필터 목록</code> 탭 하단에 있는 <code>추가</code>를 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a99bfa97-ce09-4e1e-8915-82aedbb1b72a/image.png" /></p>
</li>
<li><p>Step 8. 상단에 있는 <code>추가</code>를 클릭한다. 이 때 하단에 있는 <code>추가 마법사 사용</code>은 반드시 <code>체크 해제</code>해야 한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1aa5514c-55f4-4777-8317-436c03c2ddb1/image.png" /></p>
</li>
<li><p>Step 9. <code>주소</code> 탭에서 다음과 같이 선택, 입력한다.
<code>원본 주소</code> → <code>내 IP 주소</code>를 선택한다. <code>대상 주소</code> → <code>특정 IP 주소 또는 서브네트</code>를 선택한다. <code>(192.168.100.20)</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/17cd5b1b-e453-430d-bd22-b426e1d83081/image.png" /></p>
</li>
<li><p>Step 10. <code>확인</code>을 몇 번 누르면 <code>IP 필터 목록</code> 탭 하단에 추가된 필터가 보인다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/38a690f5-eef6-40ab-9c8f-ac6fca75a26b/image.png" /></p>
</li>
<li><p>Step 11. 이 목록을 체크한 후 <code>필터 동작</code> 탭을 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f2ba813c-a020-435c-b5f0-9959fcc72e4e/image.png" /></p>
</li>
<li><p>Step 12. 하단에 있는 추가를 클릭한다. 이 때 하단에 있는 <code>추가 마법사 사용</code>은 반드시 <code>체크 해제</code>해야 한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1757f639-a078-40bc-b0f5-a3603f097a57/image.png" /></p>
</li>
<li><p>Step 13. <code>보관 방법</code>에서 <code>추가</code>를 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/61e92194-a062-4d08-bd40-2b208e1d7b8e/image.png" /></p>
</li>
<li><p>Step 14. 하단에 있는 <code>사용자 지정</code>에서 <code>설정</code>을 클릭한다.<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7aab2fa2-34a0-4fb2-81ae-dcc3903ea5f8/image.png" /></p>
</li>
<li><p>Step 15.  암호화되지 않은 데이터 및 주소 무결성'만 체크한 후 <code>확인</code>을 클릭한다.<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/06ffe5dd-56fd-4150-a952-2b0e3de386b9/image.png" /></p>
</li>
<li><p>Step 16. <code>확인</code>을 <code>두 번</code> 클릭한 후 <code>필터 동작</code> 탭을 보면 추가된 목록이 보인다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/703ac4eb-4a65-4d46-a14d-ebb3d626a2f2/image.png" /></p>
</li>
<li><p>Step 17. 이 목록을 체크한 후 <code>인증 방법</code> 탭을 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/60ad39c1-af06-47c9-bbb0-f69734b9f278/image.png" /></p>
</li>
<li><p>Step 18. 여기서는 새로 <code>추가</code>하지 말고 목록에 있는 <code>Kerberos</code>를 클릭한 후 <code>편집</code>을 이용해서 변경하도록 한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8655b2a4-97b6-4c46-8ff3-a9bd711ea4aa/image.png" /></p>
</li>
<li><p>Step 19. 하단에 있는 <code>이 문자열 사용(미리 공유한 키)</code>를 체크한 후 하단에 있는 빈 칸에 <code>P@ssw0rd</code>를 입력한 후 <code>확인</code>을 클릭한다.<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0ff5974f-941f-46ae-9266-1607bf01b18c/image.png" /></p>
</li>
<li><p>Step 20.<code>적용</code>을 클릭한 후 <code>확인</code>을 클릭한다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/017d599c-0948-47ec-b949-a6d2af3b64ba/image.png" /></p>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cbcebb03-f711-4726-a339-a94a7308083a/image.png" /></p>
<ul>
<li><p>Step 21. <code>새 IP 보안 정책 속성</code>창의 <code>규칙</code> 탭 하단에 추가된 <code>보안 규칙</code>이 보인다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/09842dc0-6b7f-4bc4-8395-02fcebb9fca9/image.png" /></p>
</li>
<li><p>Step 22. <code>확인</code>을 클릭하면 <code>IP 보안 정책</code>의 우측에서 추가된 목록이 보인다. <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2ea9885d-49e2-4162-adcc-ea16a084a8d1/image.png" /></p>
</li>
</ul>
</li>
<li><p><code>Client100</code>에서의 작업</p>
<ul>
<li><code>SRV100</code>과 동일한 방법으로 설정한다.</li>
<li><code>100.10</code> 으로 바꾸는 것 제외하고 동일 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7a3150c2-6558-4981-824e-35bb5c562a4a/image.png" /></li>
</ul>
</li>
<li><p><code>테스트 2.</code></p>
<ul>
<li><code>SRV100</code> 또는 <code>Clinet100</code>에서 <code>wireshark</code>를 실행한 상태에서 <code>ping</code> 테스트를 실행한다.</li>
<li><code>wireshark</code>에 올라온 <code>Protocol</code>을 확인해보면 <code>테스트 1.</code>과 마찬가지로 <code>ICMP</code>로 나타난다. 즉, 보안 설정이 적용이 되지 않았다는 것을 알 수 있다. <ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/616882fd-1bdf-43a3-b88d-b2d7a54b3fba/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p><code>SRV100</code>과 <code>Client100</code>에서의 <code>보안 적용</code>을 위한 추가 작업</p>
</li>
<li><p><code>테스트 3.</code></p>
<ul>
<li><code>새 IP 보안 정책</code> 우클릭 후 <code>할당</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7082d5d9-5cea-4c12-8da8-fa1bf3edc47b/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4ff1abbb-0968-44a0-9b69-60161ba95f49/image.png" /></li>
<li><code>기밀성</code>이 적용 됨 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9aa1040f-efe7-428a-af46-b538d942ff93/image.png" /></li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/badac33b-4cf1-4b26-b66c-aae7c151e574/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7d7ebb06-988f-4f65-b7be-0ce3daa8b301/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/9a991f8a-8b41-448a-b844-a8da1a649e11/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d770f104-4657-4ad8-9408-8abfed8a52e6/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6e12ac5a-fe20-43c4-bea8-6c9c24c4d7a8/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bb33b0c3-5d37-4eb9-8796-9086fcb7cc4c/image.png" /></p>
<p><code>Client100</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a564aa6e-5eef-4582-bcea-b93d6c784acf/image.png" /></p>
<p><code>SRV100</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e64ce1d7-cce3-453e-80a5-8d707b1cb2e1/image.png" /></p>
<p><code>SRV200</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2b17cbe1-037b-4d7d-aec4-37c21b3a478d/image.png" /></p>
<p><code>Client200</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/45c7ed03-03c2-425a-934e-93e6ee3659b5/image.png" /></p>
<blockquote>
<h3 id="결론">결론</h3>
<p><code>Client100</code> 네트워크(192.168.100.x)와 <code>Client200</code> 네트워크(192.168.200.x)가 서로 <code>ping</code>이 되고,
중간에 있는 <code>SRV100</code> ↔ <code>SRV200</code> 구간은 ESP로 암호화되어 안전하게 통신되고 있음.
이게 전형적인 사이트 간 <code>VPN</code> (Site-to-Site IPsec VPN) 실습 결과. 실무에서도 RRAS나 강력한 장비(Fortigate, Cisco, Palo Alto 등)로 똑같이 구성합니다.</p>
</blockquote>
<hr />
<h3 id="kerberos-생략">Kerberos (생략)</h3>
<hr />
<h3 id="ca-인증서">CA 인증서</h3>
<ul>
<li><p>시스템 구성</p>
<ul>
<li><code>SRV 100</code> , <code>Client100</code>, <code>SRV200</code>, <code>Client200</code></li>
</ul>
</li>
<li><p>환경 구성</p>
<ul>
<li><code>StoS</code>, <code>wf(o)</code> + <code>CA</code></li>
</ul>
</li>
<li><p>설정 및 테스트</p>
<ul>
<li><p>인증기관 설치 및 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/daf9f8de-a49f-4fc6-accb-e469af4329d2/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3e6fc674-5412-4b17-ac4c-2d31e32dbfe6/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/91c98001-76ee-4337-bf85-f41b278de905/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f3a9917f-194d-4632-a0a4-bc40e5ece73d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/90459d82-ed0a-49f4-9320-451d7ae68d56/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fccf14a3-17ad-44b9-9407-8c74c5496113/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/46894afe-7adc-476e-b31f-5655c9483d15/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/6bf85a32-9dfe-4129-a365-9c29b51f7558/image.png" /></li>
</ul>
</li>
<li><p>인증서 설정 1. 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ee92fa4e-9b45-40dd-9088-bafefc88cd51/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1f4836c2-0b63-4527-967a-3adb513dcd29/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b4ef3d5d-bade-4581-98d5-ae639eb8b09e/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d0d74dbe-e560-4f05-a991-11615e5a6da2/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/83aaf665-74f6-421c-a2bd-131c70fc63e5/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5795dc46-0524-4923-9cbb-823cbec022cd/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/41437359-392a-4109-9529-fceedebe8bc2/image.png" /></li>
</ul>
</li>
<li><p>인증서 신청</p>
<ul>
<li><code>internet explorer</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c5099f1b-596b-4249-90a6-f3df50e51d3d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5f482b45-fc70-4140-9e78-35e7b37050e9/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c5123080-73db-4885-9856-43c88470279c/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4f8d7206-7192-4c1e-8a4d-2fa00b1ffaee/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/029ac8e8-c7b0-4865-92c5-bb510e8c6755/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2f0e905f-c0bd-463b-9059-b188113d9cd7/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/17b62ebd-a576-4cc0-a7ab-3ea0fa771b04/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7db502f5-f65a-40fc-9743-010091b2cd47/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8ecdf6bd-ac50-4c7a-abd2-5a4f83a1f3ce/image.png" /></li>
<li>위 설정이 안되어있으면 <code>제출</code>이 <code>활성화</code>가 안됨 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f5c125b9-a67a-4096-89fd-a5a2d2066d43/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fd439cff-010f-467e-b5fe-f9a33c2e48cc/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8b7f1cc5-6c57-4c88-96a8-f38bf042b676/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/53cef412-da19-41ce-abc7-0dfc0ab7761d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e825af16-f6f7-4311-bb53-cd4aae01aa4d/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/213f5a42-8007-4cc0-acba-130b577c8c8a/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5f40bf20-b6d4-4484-ab5f-14e23279f4e5/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4243d283-c4d2-4b2f-9dbd-eb29477bc3b5/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/da9cb248-469d-4a93-a5b0-f5fe7fb26f2b/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f1915eca-af69-4430-8d4d-0abc17136c57/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ebb2fc0d-c8d4-4a54-adb7-b05c6d92d2ec/image.png" /></li>
<li>개인용에서 <code>F5</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5414fd76-fbc9-4626-a9fb-1a1b15b6f829/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/90e0ff92-398b-4ece-83c2-2a9cccf9e000/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/35699c9c-e97e-4e66-b96b-a4205d8916b6/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a873772c-547e-419d-a9c4-d58684488241/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0321d895-d6aa-4327-a932-8127aa8d71a7/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ff380927-0f33-492c-8af6-256b45640879/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2c46d159-6150-458a-a845-611aa592c5c5/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b8e2e863-513b-4599-8ff4-79afe9be3cee/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/84ec3cf9-b63e-4d29-9fdd-fdd16dacd293/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5a5eca92-ec10-4c5e-ae6a-362e649f1b99/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2d834732-7c7e-4aa8-9648-ba61004eca4a/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/51109773-eef6-4152-9450-c524c2da945f/image.png" /></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1d826dc9-f7d3-4f71-9521-9d2801269950/image.png" /></li>
</ul>
</li>
<li><p><code>Client100</code>에서 작업</p>
<ul>
<li><p><code>mmc</code>에서 사용자 , 로컬 컴퓨터 추가 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d205d828-b399-4a69-923e-51718a7f1f64/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f6bb2889-be61-4ba2-a56b-dc05c83aa71a/image.png" /></p>
</li>
<li><p>인터넷 옵션에서 허용 설정</p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/84937f32-e2b8-432a-993f-b47860e29d34/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/94a8a14a-1624-4277-b0ec-987c4212ce34/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/131bdda8-dad5-4d89-85c8-51f92dd0b62e/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/04087a46-2abd-4839-8060-87fcfadf62e1/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/62e7b40d-b146-4b88-8047-0c31ffbc2e94/image.png" /></p>
</li>
<li><p><code>F5</code> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7a16a033-779a-4abf-bc07-72039067dca3/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2d69de53-9903-47b8-a5d4-38c5cbb06497/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3d6976db-8ff6-49d6-9624-a88c737e37ce/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c0f72fbb-7109-4517-89dc-1d5d85e50078/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8ecdf6bd-ac50-4c7a-abd2-5a4f83a1f3ce/image.png" /></p>
</li>
<li><p><code>SRV100</code>에서 확인 <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/80230f23-3323-4eed-85ff-d977a06fb858/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2919fd3c-69f9-4eae-81e7-3344878b7d23/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7254cb4a-be6b-45b8-aec9-db421597a75a/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4e923a56-3de5-48d3-abda-e6a29d46e86b/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/45ff6e6f-ae44-4526-b72d-804ffdf7bced/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/dd5da0e3-012b-4d33-bfe3-fff0480f61d9/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/bb95ccfd-18ea-4887-878e-2f035d1b3844/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/11dc138d-003b-47a1-9b82-a4fe03f5e689/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1887e7ba-d485-4c73-84f7-f271645093e5/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1674df1c-fada-42b4-84df-ce97db1baf3d/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e97f3328-12fd-43c4-a1fe-c135bf432b65/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4f99dbc2-a5a2-46be-94b7-0e47efa33da8/image.png" /></p>
</li>
<li><p><code>H to H</code>만 된상태<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ab701a7e-756b-4f85-bfa0-c232798e6270/image.png" /></p>
</li>
<li><p><code>secpol.msc</code>에서 작업<code>(srv100)도 작업</code></p>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a7911161-9ead-4747-a47d-db3cfc2b44d0/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5bf3e3f4-e53e-4dbe-9b74-077acaff1ad9/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/94129b42-ea8a-4862-b0aa-240ff4fe6d4d/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4006be5a-5103-4931-870f-ff140900deda/image.png" /></p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>