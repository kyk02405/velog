# Cloud DX - 19 Quota(할당량)

- 📅 Published: Thu, 23 Oct 2025 00:55:07 GMT
- 🔗 [Read on Velog](https://velog.io/@kyk02405/Cloud-DX-19-Quota%ED%95%A0%EB%8B%B9%EB%9F%89)

<hr />
<h1 id="12-quota할당량">12. Quota(할당량)</h1>
<h2 id="개요">개요</h2>
<ul>
<li><p>시스템에 있는 HDD를 사용자들에게 <code>(핵심)일정한 비율로 할당</code>함으로써 보다 효율적인 관리를 할 수가 있다.</p>
</li>
<li><p><a href="https://www.cafe24.com">cafe24</a>에서 서비스하고 있는 <code>웹호스팅</code>서비스가 대표적이다.</p>
</li>
</ul>
<h2 id="주의사항">주의사항</h2>
<ul>
<li><code>시스템 파티션</code> 즉, <code>swap 파티션</code>과 <code>/파티션</code>에는 절대 설정해서는 안된다.</li>
<li><span style="color: red;">(권장)</span><code>시스템 HDD</code>가 아닌, <code>별도의 HDD</code>를 추가한 후 설정해야 한다.</li>
<li>참고로 <code>swap 파티션</code>은 <code>가상 메모리</code> 공간을 말하는데 HDD의 일정 부분을 메모리처럼 사용하는 파티션을 말한다. 
권장 용량은, <code>시스템 메로리(RAM) x 2</code>만큼 지정한다.</li>
</ul>
<hr />
<h2 id="실습-1-기본">실습 1. 기본</h2>
<h3 id="작업환경-구성">작업환경 구성</h3>
<ul>
<li><code>2GB HDD</code>를 추가한 후 통으로 잡고 자동 마운트를 설정한다.<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/aa6d3755-ffa8-472c-9588-d0d30a1b37e4/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="단계별-설정">단계별 설정</h3>
<ul>
<li>Step 1. 쿼터 설정 가능 여부 확인<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/259a8294-eafc-4bdc-b64a-cea91aa33b52/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 2. 쿼터 적용을 위한 파티션 자동마운트 정보 수정<ul>
<li>자동 마운트 수정<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b275e630-c276-4865-9493-36f0182dab62/image.png" /></li>
</ul>
</li>
<li><code>reboot</code> 후 적용 상태 확인<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/397bb883-8455-487f-9718-2c3ad8c41ff6/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 3. 쿼터 설정 후 파티션 정보가 저장될 데이터베이스(/aquota.user) 파일 생성<ul>
<li>이 파일은 관리자 이외에는 접근을 허용해서는 안되기 때문에 생성 후 <code>허가권을 변경(600)</code>해야한다</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ea29ed41-70de-4bb1-adde-2b5d4986ad67/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 4. 대상이 되는 파티션에 쿼터 설정을 적용<ul>
<li>오류 (정상적인 오류)</li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/03d0c0d4-84af-4b30-91c7-d41ce0ac3a79/image.png" /></li>
<li><code>a</code>(ll partition), </li>
<li><code>v</code>(erbose),</li>
<li><code>u</code>(UID, 특정 UID가 사용하는 파일과 디렉토리 체크), </li>
<li><code>g</code>(GID, 특정 GID가 사용하는 파일과 디렉토리 체크)</li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 5. 쿼터가 적용할 파티션에 쿼터 설정 데이터베이스 파일이 생성되었는지 확인<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d89ace5b-a766-4a1b-91d5-4f195b78eb0a/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 6. 쿼터 설정 활성화 및 비활성화<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/313d6e5c-8550-4832-8894-2ed2ab5d1241/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<ul>
<li>Step 7. 지금까지 설정한 내용이 정상적으로 동작하는지 확인<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f5d259f6-5fd9-4f92-963a-c99adfd8d402/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cc9dfd51-0594-4800-a2ca-5a0fb2c33101/image.png" /></li>
</ul>
<hr />
<h2 id="실습-2-응용">실습 2. 응용</h2>
<h3 id="예제-1-사용자별-출력되는-쿼터-형태">예제 1. 사용자별 출력되는 쿼터 형태</h3>
<ul>
<li><p>쿼터가 적용되지 않는 파티션에 존재하는 사용자의 경우 </p>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2d28eb65-9a5e-47aa-b964-0d1fa1124497/image.png" /></p>
</li>
<li><p>현재 적용된 것이 없기 때문에 아무것도 안 나온다.</p>
</li>
</ul>
</li>
</ul>
<ul>
<li>쿼터가 적용된 파티션에 존재하는 사용자의 경우<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/e58e446b-a65e-4d7a-bf7f-5cfdc3789cdd/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="예제-2-사용자별-쿼터-설정">예제 2. 사용자별 쿼터 설정</h3>
<ul>
<li><p>사용자 정보 변경</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/12c2ba31-5640-4168-97fd-7ab7f3d38dda/image.png" /></li>
</ul>
</li>
<li><p>사용자 쿼터 설정</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/db43867e-94fa-47c1-8cda-3c929beae47b/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="예제-3-쿼터-용량-변화-확인-테스트">예제 3. 쿼터 용량 변화 확인 테스트</h3>
<ul>
<li><p>Test 1. 리눅스의 터미널 창(Putty)에서 파일을 직접 복사한 경우</p>
<ul>
<li><p>개요</p>
<ul>
<li>용량과 무관하게 아무런 변화가 없다.</li>
</ul>
</li>
<li><p>복사 전 쿼터 상태 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ef39f9c2-7fc3-49b9-9a00-2477d925f9b0/image.png" /></li>
</ul>
</li>
<li><p>파일 복사를 위한 <code>ISO</code>파일 마운트 한 후 파일 복사 </p>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/31809d0e-953d-4280-8082-35652f56dea6/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/65a25e5b-6375-4529-86a6-77a7800d8bd3/image.png" /></p>
</li>
</ul>
</li>
<li><p>복사 후 쿼터 상태 확인    </p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5332431a-c9fc-435c-a3de-5d6399f8b89d/image.png" /></li>
</ul>
</li>
</ul>
</li>
<li><p>Test 2. 윈도우에서의 <code>알FTP</code>를 이용한 <code>파일 업로드</code></p>
<ul>
<li><p>개요</p>
<ul>
<li>리눅스 시스템 내에서 복사하는 경우는 쿼터와</li>
<li>쿼터 용량 단위는 <code>KB</code>이다.</li>
</ul>
</li>
<li><p><code>Test 1.</code> 에서 다운로드 받았던 <code>파일들(mariadb-server-*)</code>을 윈도우에서 다운로드 받은 후 <code>/cloud/samadal/</code> 디렉토리 안에 있는 내용들을 모두 삭제한다.</p>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2a284b8d-5a96-4027-adf9-1157d2afba2e/image.png" /></p>
</li>
<li><p><code>알FTP</code>를 이용해서 다운로드 받은 파일들을 업로드 한다.
쿼터 설정을 통해 용량을 제한했기 때문에 오류가 발생한다.</p>
</li>
<li><p>현재 쿼터 상태를 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b859ddf7-f55f-4bdf-99ee-44c5301b3e2c/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="예제-4-사용자samadal의-쿼터-정보를-또-다른-사용자에게-자동으로-적용">예제 4. 사용자(samadal)의 쿼터 정보를 또 다른 사용자에게 자동으로 적용</h3>
<ul>
<li>사용자에게 soft(400M), hard(440M)로 쿼터를 설정한다.<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b4286d01-0eb9-46c9-abae-f309ef56c259/image.png" /></li>
</ul>
</li>
</ul>
<ul>
<li><p>다른 사용자에게 자동으로 적용</p>
<ul>
<li><p>사용자 생성</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/370694f2-81b6-4193-944f-a893362b8283/image.png" /></li>
</ul>
</li>
<li><p>자동 적용</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/76aba4ba-185f-4453-bc0d-f0a41d4fd154/image.png" /></li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="예제-5-유예기간-변경">예제 5. 유예기간 변경</h3>
<ul>
<li><p>현재 설정되어 있는 유예기간 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/186f96dd-2125-43c0-bd6c-141f6f7842bf/image.png" /></li>
</ul>
</li>
<li><p>유예기간 변경</p>
<ul>
<li><p><code>edquota -t</code></p>
<ul>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/90650a13-7314-4c3c-b2e2-30a571f6740b/image.png" /></p>
</li>
<li><p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/693c33a3-446a-4437-b9fc-428fdb93caa3/image.png" /></p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h3 id="예제-6-사용자별-쿼터-확인">예제 6. 사용자별 쿼터 확인</h3>
<ul>
<li><code>quota -v</code></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/486677cf-5724-4ef9-b76b-5f04345583c1/image.png" /></li>
</ul>
<hr />
<h3 id="예제-7-특정-파티션에-적용된-쿼터-해제">예제 7. 특정 파티션에 적용된 쿼터 해제</h3>
<ul>
<li><p>쿼터 비활성화 및 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d57ed581-c050-45ad-978d-c87adc9fc17c/image.png" /></li>
</ul>
</li>
<li><p>테스트</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/130d3948-a299-44c5-bf8f-76bbdc66bf28/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h3 id="예제-8-사용자가-없는데도-쿼터-정보가-계속-남아-있는-경우">예제 8. 사용자가 없는데도 쿼터 정보가 계속 남아 있는 경우</h3>
<ul>
<li><p>사전 작업</p>
<ul>
<li><code>홈 디렉토리 변경</code></li>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a534f7df-9194-41c8-9135-b13aa67046fb/image.png" /></li>
</ul>
</li>
<li><p>비정상적인 결과를 <code>새로 고침</code>을 통해서 확인</p>
<ul>
<li><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b7b8d230-cd76-49d0-9402-761059477925/image.png" /></li>
</ul>
</li>
</ul>
<hr />
<h2 id="실습-3-응용">실습 3. 응용</h2>
<h3 id="초기-작업">초기 작업</h3>
<ul>
<li><code>samadal</code>을 제외한 모든 계정 삭제</li>
<li><code>samadal</code>은 원래 경로로 이동 </li>
<li>HDD 제거 </li>
</ul>
<h3 id="작업-개요">작업 개요</h3>
<ul>
<li>다음과 같이 두 개의 웹 호스팅 상품을 제공한다고 할 때의 쿼터를 설정한다. </li>
<li>HDD(4GB)를 추가하고 eco(500MB), gen(700MB)로 구성한 후 자동마운트, 쿼터 설정</li>
<li>각 영역에 다음과 같은 사용자를 각각 한 개씩 생성하고 용량을 할당한다.</li>
<li>user1(100MB), user2(400MB)</li>
<li>모든 작업은 Shell Scripting으로 설정한 후 자동 적용되도록 한다.</li>
</ul>
<pre><code class="language-bash"> 1 #!/bin/bash
  2
  3
  4 clear
  5
  6 echo &quot;===========================================&quot;
  7 echo &quot;1. 파티션 설정&quot;
  8 echo &quot;===========================================&quot;
  9
 10 printf &quot;fdisk -l /dev/&quot;
 11 read PART
 12 echo &quot;&quot;
 13 fdisk -l /dev/$PART
 14
 15 echo &quot;&quot;
 16 printf &quot;Press any key to reboot...&quot;
 17 read AA
 18
 19 fdisk /dev/$PART
 20
 21 echo &quot;&quot;
 22 echo &quot;===========================================&quot;
 23 echo &quot;2. 파티션 포맷&quot;
 24 echo &quot;===========================================&quot;
 25
 26 read PART1
 27 mkfs.ext4 /dev/sda1
 28 echo &quot;========================&quot;
 29 mkfs.ext4 /dev/sda2
 30
 31 echo &quot;파티션 포맷을 완료했습니다.&quot;
 32
 33 echo &quot;&quot;
 34 echo &quot;==============================================================&quot;
 35 echo &quot;첫번째 마운트 포인트 이름로 사용할 디렉토리를  입력해주세요 : &quot;
 36 echo &quot;==============================================================&quot;
 37 echo &quot;&quot;
 38 read HDD
 39
 40 mkdir -p /$PART
 41 mkdir -p /sda/$HDD
 42 ls -l /$PART/
 43
 44 echo &quot;==============================================================&quot;
  45 echo &quot;두번째 마운트 포인트 이름로 사용할 디렉토리를  입력해주세요 : &quot;
 46 echo &quot;==============================================================&quot;
 47 read HDD1
 48
 49 mkdir -p /sda/$HDD1
 50 ls -l /$PART/
 51
 52 echo &quot;====================================================================&quot;
 53 echo &quot;자동 마운트 설정을 하려면 \&quot;y\&quot;, 취소하려면 \&quot;n\&quot;  버튼을 눌러주세요&quot;
 54 echo &quot;====================================================================&quot;
 55 read BB
 56
 57 case $BB in
 58
 59         y)
 60                 vi /etc/fstab
 61                 cat /etc/fstab
 62                 ;;
 63         n)
 64                 echo &quot;마운트 설정을 취소합니다&quot;
 65                 ;;
 66 esac
 67
 68 echo &quot;=======================================================&quot;
 69 echo &quot;재부팅 하려면 \&quot;y\&quot; 취소하려면  \&quot;n\&quot; 버튼을 눌러주세요&quot;
 70 echo &quot;=======================================================&quot;
 71
 72 read RE
 73
 74 case $RE in
 75         y)
 76                 echo &quot; 시스템을 재부팅 합니다&quot;
 77                 reboot
 78                 ;;
 79         n)
 80                 echo &quot; 재부팅을 취소합니다 &quot;
 81                 ;;
 82 esac
 83
 84</code></pre>
<pre><code class="language-bash">#!/bin/bash


echo &quot;쿼터 설정 파일 생성&quot;
read CR
echo &quot;&quot;
quotacheck -cum /eco
quotacheck -cum /gen


echo &quot;사용자 생성&quot;
read US
echo &quot;&quot;
useradd -d sda/eco/user1 -m user1
useradd -d sda/gen/user2 -m user2

echo &quot;user1 쿼터 설정&quot;
read SET1
echo &quot;&quot;
edquota -u user1

echo &quot;user2 쿼터 설정&quot;
read SET2
echo &quot;&quot;
edquota -u user2

repquota -a</code></pre>