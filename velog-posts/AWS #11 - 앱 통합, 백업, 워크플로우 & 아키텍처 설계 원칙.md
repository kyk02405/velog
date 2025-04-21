<hr />
<h2 id="amazon-workspaces">Amazon WorkSpaces</h2>
<ul>
<li>윈도우나 리눅스 데스크탑을 프로비저닝 할 수 있는 관리형 DaaS 서비스(가상 데스크탑)<ul>
<li>DaaS(Desktop as a Service) : 인터넷만 연결되면 언제, 어디서나, 어떤 기기로도 기업 내부망에 접속</li>
<li>회사에 입사하면 물리 데스크탑을 받아 업무 수행 → 출장, 재택 근무 시에는 접속 불가</li>
</ul>
</li>
<li>멀티 리전을 사용하며, 사용자과 가까운 곳에 배포<ul>
<li>지연시간을 줄임</li>
</ul>
</li>
<li>속도가 빠르고, 수천명의 사용자로 확장도 쉬움</li>
<li>KMS와 통합되어 안전(보안 우수)</li>
<li>종량제 과금(사용한 만큼 지불)</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5d67ef2d-e14d-4fd0-8d4a-50b98af32a28/image.png" /></p>
<hr />
<h2 id="aws-iot-core">AWS IoT Core</h2>
<ul>
<li>IoT = Internet of Things<ul>
<li>데이터를 전송하고 수집할 수 있는 수많은 장치들의
네트워크</li>
</ul>
</li>
<li>AWS 클라우드에 IoT 기기를 쉽게 연결하기 위한
서비스</li>
<li>Pub/Sub 방식으로 기기간 메시지 교환</li>
<li>Lambda, S3와 같은 다른 AWS 서비스와 통합 가능<ul>
<li>IoT 애플리케이션 구축함으로써 데이터의 수집, 처리,
분석 가능</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/338c57c7-d365-4c40-9207-3794e1d240b2/image.png" /></p>
<hr />
<h2 id="amazon-elastic-transcoder">Amazon Elastic Transcoder</h2>
<ul>
<li>S3에 저장된 미디어 파일을 핸드폰 등에서 재생 가능한 포맷으로 변환<ul>
<li>(예) avi 파일이 S3에 업로드 되면, mp4 파일 혹은 720p, 1080p로 변환되어 웹에서 바로 서비스 가능</li>
</ul>
</li>
<li>사용한 만큼(동영상 길이 만큼) 비용 청구(1분단위)<ul>
<li>(예) 미국 서부(오레곤)에서 10분 분량의 파일은 10 x 0.015 USD = 0.15 USD 소요</li>
</ul>
</li>
<li>장점<ul>
<li>확장성이 뛰어남</li>
<li>사용하기 쉬움</li>
<li>비용 효율적</li>
</ul>
</li>
<li>2025년 11월 13일 중단되며, AWS Elemental MediaConvert 라는 서비스로 대체</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/431f87ee-818e-42cd-98a2-949a6d748080/image.png" /></p>
<hr />
<h2 id="aws-appsync">AWS AppSync</h2>
<ul>
<li>서버리스 형태의 GraphQL 백엔드를 개발할 수 있는 서비스<ul>
<li>모바일 및 웹 애플리케이션의 백엔드를 구축하기 위한 용도로 사용</li>
<li><span style="color: red;">GraphQL </span>: 페이스북의 모바일 기술로서 API를 위한 쿼리 언어
(SQL이 DB로 부터 데이터를 가져오는 언어라면, GraphQL은 서버로부터 데이터를 가져옴)</li>
</ul>
</li>
<li>DynamoDB, Lambda통합할 수 있고, 실시간으로 데이터를 저장, 동기화 할 수 있어 웹/모바일 애플리케이션에 활용</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/31ba0621-a79f-44e5-945d-5344e86abee0/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0d9893d8-b963-4693-9cc2-3897fdfbc7a2/image.png" /></p>
<hr />
<h2 id="aws-amplify">AWS Amplify</h2>
<ul>
<li>풀스택 웹/모바일 애플리케이션을 개발,배포하는 것을 돕는 도구와 서비스의 모음<ul>
<li>Amazon S3, Cognito, AppSync, API Gateway, SageMaker, Lambda, DynmoDB, Lex</li>
<li>인증, 저장, REST API, GraphQL API, CI/CD, pub/sub, 머신러닝, 모니터링 등을 모두 관리</li>
</ul>
</li>
<li>Amplify Studio에서 시각적 인터페이스 제공 및 애플리케이션 설계부터 구축까지 소요시간 단축<ul>
<li>(예) Figma로 만든 UI를 백엔드와 바인딩하고, React로 자동 변환함으로써 웹서비스 개발</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3f43386c-80b2-4c90-8a43-5265bb2a4e52/image.png" /></p>
<hr />
<h2 id="aws-application-composer">AWS Application Composer</h2>
<ul>
<li>서버리스 애플리케이션을 시각적으로 빠르게 설계하고 빌드</li>
<li>AWS 관리 콘솔을 이용해 drag&amp;drop 방식의 시각적 인터페이스 제공</li>
<li>AWS 전문가가 아니더라도 코드형 인프라를 빠르게 생성 가능(IaC)</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/09c25dbd-8989-4a51-a0da-848ff9321571/image.png" /></p>
<hr />
<h2 id="aws-device-farm">AWS Device Farm</h2>
<ul>
<li>웹, 모바일 app을 데스크탑, 모바일, 태블릿 환경에서 테스트할 수 있는 완전 관리형 서비스<ul>
<li>웹, iOS, 안드로이드 개발자 등의 테스트 환경 제공</li>
<li>테스트를 위해 단말기 대여 혹은 준비할 필요 없음</li>
<li>원격지에 있는 실물 단말기로 테스트/디버깅 가능(에뮬레이터 X)</li>
</ul>
</li>
<li>다양한 장치들을 동시에 테스트 함으로써 테스트 실행 속도를 향상<ul>
<li>운용 환경, 화면 크기 등 모두 다른 실제 장치</li>
<li>GPS, Wi-Fi, Bluetooth 등을 마음대로 설정가능</li>
<li>기기간 상호운용 가능</li>
<li>테스트 결과는 보고서, 로그, 스크린샷 등으로 제공</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/89cdccba-5f0d-4637-b3c2-18b9ceb74a91/image.png" /></p>
<hr />
<h2 id="aws-backup">AWS Backup</h2>
<ul>
<li>완전 관리형 서비스</li>
<li>AWS 서비스 전반에 대해서 자동으로 백업 수행<ul>
<li>On-demand 혹은 스케줄에 따라 백업</li>
<li>원본 AWS 자원(EC2, EBS, EFS, DynamoDB, RDS, Aurora 등)을 S3에 보관(백업)</li>
</ul>
</li>
<li>PITR(Point-In-Time-Recovery, 복구시점) 제공</li>
<li>백업 기간, 수명주기관리, 백업 보존 정책 등을 정의할 수 있음</li>
<li>리전 간 백업(Cross-Region Backup), 계정 간 백업(Cross-Account Backup) 지원</li>
</ul>
<hr />
<h2 id="aws-datasync">AWS DataSync</h2>
<ul>
<li>마이그레이션(온프레미스→AWS, AWS→AWS) 과정에서 많은 양의 데이터 이동 가능<ul>
<li>Amazon S3, EFS, FSx로 동기화 가능</li>
<li>주/일/시의 단위로 스케줄링해서 복제</li>
</ul>
</li>
<li>첫 번째 데이터가 로드되면, 이후에는 증분(incremental) 수행<ul>
<li>증분 : 이전 백업 복사본이 만들어지면 이후에는 변경된 부분만 백업하는 방식</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/00ab3538-bbe8-41af-a484-2598c1f6eb95/image.png" /></p>
<hr />
<h2 id="참고-백업-방식">(참고) 백업 방식</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d93e709f-1bd2-4288-b335-3f0798c6f45e/image.png" /></p>
<table>
<thead>
<tr>
<th>항목</th>
<th>풀백업</th>
<th>증분백업</th>
<th>차등백업</th>
</tr>
</thead>
<tbody><tr>
<td>백업방식</td>
<td>전체 데이터를 백업</td>
<td>(풀백업 이후) 변경된 데이터만 백업</td>
<td>(풀백업 이후) 추가된 데이터를 합산하여 백업</td>
</tr>
<tr>
<td>백업속도</td>
<td>가장 느림</td>
<td>가장 빠름</td>
<td>중간</td>
</tr>
<tr>
<td>복원속도</td>
<td>가장 빠름</td>
<td>가장 느림</td>
<td>중간</td>
</tr>
<tr>
<td>저장공간</td>
<td>가장 많음</td>
<td>효율적</td>
<td>중간</td>
</tr>
</tbody></table>
<hr />
<h2 id="aws-stepfunctions">AWS StepFunctions</h2>
<ul>
<li>시각적 워크플로우를 사용해 분산 애플리케이션, 마이크로  서비스의 구성요소를 손쉽게 조정<ul>
<li>상태 머신(State Machine) 형태로 서버리스의 워크플로우를 정의<ul>
<li>Pass 상태, wait 상태, parallel 상태, Choice 상태</li>
</ul>
</li>
</ul>
</li>
<li>Lambda의 한계<ul>
<li>동작시간 최대 15분</li>
<li>동작시간을 늘리기 위해 Lambda를 연속적으로 사용할 수 있지만,<ul>
<li><span style="color: red;">상태 기억을 못함(Stateless) </span>→ Lambda 간의 정보 전달의 위한 매개체 필요(SQS, DynamoDB 등)</li>
<li>다수의 Lambda 함수 관리가 어려움(자동화 필요)</li>
</ul>
</li>
</ul>
</li>
<li>StepFunctions를 이용해 Lambda의 단점 극복 가능!</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ea6c20db-ab88-423d-87f2-8c42fbb9afd0/image.png" /></p>
<hr />
<h2 id="aws-ground-station">AWS Ground Station</h2>
<ul>
<li>완전 관리형 서비스</li>
<li>AWS 리전 근처의 위성 지상국의 글로벌 네트워크 제공<ul>
<li>위성 지상국 인프라를 구축할 필요 없이 위성 데이터를 제어하고 수집</li>
<li>위성의 데이터를 클라우드로 쉽게 가져올 수 있음</li>
</ul>
</li>
<li>사용사례 : 일기예보, 통신, 동영상 방송</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d4fd7564-827a-456f-b972-34c4ce249de9/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f3ae7d75-d0be-483b-b3f8-37d5a3a6ff13/image.png" /></p>
<hr />
<h2 id="well-architected-프레임워크-1">Well-Architected 프레임워크 1</h2>
<ul>
<li>레거시 시스템의 경우, 고객의 문제와 니즈를 해결하기 위해 정보시스템의 용량산정 필수</li>
<li>용량산정<ul>
<li>시스템에 요구되는 성능 요구사항과 성능을 결정하기 위한 계획</li>
<li>동시 접속자 수, TPS, 애플리케이션의 동작 특성, 서버 시스템의 피크율, 여유율 등을 고려</li>
<li>서버(CPU, 메모리, 디스크), 스토리지의 규모 도출</li>
</ul>
</li>
</ul>
<h3 id="webwas-cpu-산정기준">Web/WAS CPU 산정기준</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>산정항목</th>
<th>적용범위</th>
<th>일반값</th>
</tr>
</thead>
<tbody><tr>
<td>S1</td>
<td>동시 사용자 수</td>
<td>-</td>
<td>산정값</td>
</tr>
<tr>
<td>S2</td>
<td>사용자당 오퍼레이션 수</td>
<td>3 ~ 6</td>
<td>5</td>
</tr>
<tr>
<td>S3</td>
<td>기본 OPS 보정</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>S4</td>
<td>업무 OPS 보정</td>
<td>-</td>
<td>WEB: 0.7, WAS: 2</td>
</tr>
<tr>
<td>S5</td>
<td>인터페이스 부하 보정</td>
<td>1.1 ~ 1.2</td>
<td>1.2</td>
</tr>
<tr>
<td>S6</td>
<td>피크타임 부하 보정</td>
<td>-</td>
<td>1.3</td>
</tr>
<tr>
<td>S7</td>
<td>클러스터 보정</td>
<td>2-NODE: 1.4~1.5<br />3-NODE: 1.3</td>
<td>-</td>
</tr>
<tr>
<td>S8</td>
<td>시스템 여유율</td>
<td>-</td>
<td>1.3</td>
</tr>
<tr>
<td>S9</td>
<td>시스템 부하율</td>
<td>-</td>
<td>0.7</td>
</tr>
</tbody></table>
<p><strong>산정식:</strong><br />CPU(OPS 단위) = (동시 사용자 수 × 사용자당 오퍼레이션 수 × 기본 OPS 보정 × 업무 OPS 보정 × 인터페이스 부하 보정 × 피크타임 부하 보정 × 클러스터 보정 × 시스템 여유율) ÷ 시스템 부하율</p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ebd011c1-2a19-46cb-a8ba-f5bacb905372/image.png" /></p>
<hr />
<h2 id="well-architected-프레임워크-2">Well-Architected 프레임워크 2</h2>
<ul>
<li><p>클라우드 환경에서 아키텍처 구축시,</p>
<ul>
<li><p>용량 산정 보다는 오토 스케일링 활용 → 필요한 만큼 사용 &amp; 요금지불</p>
</li>
<li><p>프로덕션 환경 규모로 테스트 → 환경 구성이 쉽다는 장점 활용</p>
<ul>
<li>프로덕션 환경 : 애플리케이션이 실제 사용자에게 제공되는 환경</li>
</ul>
</li>
<li><p>아키텍처 구성을 자동화 → IaC(Infrastructure as Code)를 활용해 다른 계정 &amp; 지역에 쉽게 구성</p>
</li>
<li><p>진화적 아키텍처 고려 → 클라우드 운영 과정에서 더 효율적인 아키텍처가 무엇인지 지속적으로 고민</p>
<ul>
<li><p>(예) 애플리케이션의 마이그레이션 과정에서 더 좋은 아키텍처로 개선 (예) Lambda 활용</p>
</li>
<li><p>※ 카오스 몽키(Chaos Moneky) 전략 : 클라우드 환경에서 시스템의 신뢰성을 확인하기 위해 인위적인 혼돈 (Chaos)를 가해 시스템의 취약 부분을 확인하고 보강하는 방식(넷플릭스에서 개발, 랜덤하게 공격)</p>
<ul>
<li>인위적인 혼돈 : 응답 지연, 네트워크 지연, 예외발생, 애플리케이션 종료, 메모리 누수 등</li>
</ul>
</li>
</ul>
</li>
<li><p><a href="https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html">https://docs.aws.amazon.com/wellarchitected/latest/framework/general-design-principles.html</a></p>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="well-architected-프레임워크--6-원칙pillars">Well-Architected 프레임워크 – 6 원칙(pillars)</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f3722995-d204-4052-a061-5687f5997963/image.png" /></p>
<hr />
<h2 id="첫-번째-원칙pillar---운영-우수성">첫 번째 원칙(Pillar) - 운영 우수성</h2>
<ul>
<li>시스템 실행 및 모니터링을 통해 비즈니스의 가치를 높이고, 프로세스를 개선하기 위한 능력</li>
<li>디자인 원칙<ul>
<li>IaC를 통해 운영<ul>
<li>대표적으로 AWS CloudFormation 서비스를 이용해 리소스 관리 시간을 축소, 애플리케이션 운영 시간 확대</li>
</ul>
</li>
<li>빈번하고(frequent), 작고(small), 되돌릴 수 있는(점진적) 변경 수행<ul>
<li>장애 발생시 파급 효과에 대한 분석을 빠르게 파악하고, 빠르게 복구 가능</li>
</ul>
</li>
<li>빈번하게 운영 절차를 개선하고, 팀원들이 숙지할 수 있도록 함<ul>
<li>정기적으로 검토하고 업데이트, 게임화(Gamify)해서 사용자 참여율을 높여 개선</li>
</ul>
</li>
<li>운영 실패를 예상하고, 실패를 통해 끊임없이 배워야 함 → 실패로 부터 피드백</li>
<li>워크로드 동작, 성능, 안정성, 비용 및 상태에 관한 데이터를 통해서 개선을 위한 인사이트를 획득</li>
</ul>
</li>
</ul>
<hr />
<h2 id="운영-우수성을-위한-aws-서비스">운영 우수성을 위한 AWS 서비스</h2>
<ul>
<li>Prepare(준비)<ul>
<li>AWS를 사용하면 전체 워크로드(애플리케이션, 인프라, 정책, 거버넌스, 운영)를 코드로 확인 가능</li>
<li>AWS CloudFormation을 사용해 일관되고 규격화된 환경에서 운영 제어 수준을 높일 수 있음</li>
</ul>
</li>
<li>Operate(운영)<ul>
<li>수동 작업을 피하고 자동화를 통한 운영</li>
<li>CloudTrail을 통해 의도적으로 수행된 것이나 수동으로 변경된 것이 있는지 추적</li>
<li>CloudWatch를 통해 시간에 따른 성능 모니터링을 실시하고, 어떤 작업을 수행해야 하는지 확인</li>
<li>AWS X-Ray는 HTTP를 추적해 올바르게 동작하는지 확인 또는 오류가 발생한 위치를 확인</li>
</ul>
</li>
<li>Evolve(진화)<ul>
<li>지속적으로 인프라 개선/발전</li>
<li>CI/CD를 통해 운영 우수성에 기여(AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, AWS Code Pipeline)</li>
</ul>
</li>
</ul>
<hr />
<h2 id="두-번째-원칙pillar--성능-효율성">두 번째 원칙(Pillar) : 성능 효율성</h2>
<ul>
<li>시스템 요구사항을 충족하고, 시스템을 유지하는데 컴퓨팅 자원을 효율적으로 사용하는 능력</li>
<li>디자인 원칙<ul>
<li>몇 분안에 다수의 리전에 쉽게 배포할 수 있어야 함 (CloudFormation)</li>
<li>기술의 발전 흐름을 파악해서 고급 기술을 사용</li>
<li>서버리스 아키텍처 사용</li>
<li>많은 테스트를 통해 제대로 동작하는지 확인</li>
<li>(강의, 블로그 등을 통해) AWS 서비스의 변경사항에 대해 지속적으로 학습</li>
</ul>
</li>
</ul>
<hr />
<h2 id="세-번째-원칙pillar--안정성">세 번째 원칙(Pillar) : 안정성</h2>
<ul>
<li>컴퓨팅 자원을 동적으로 구성해서 서비스 중단을 복구하고, 잘못된 구성이나 일시적 네트워크
중단 문제 등을 완화시키는 능력
➔ 어떤 상황에서도 애플리케이션이 실행되도록 하는 능력</li>
<li>디자인 원칙<ul>
<li>일부러 다양한 장애 상황을 일으켜 복구 과정 테스트함</li>
<li>장애 발생을 사전에 예측하고 자동으로 복구 조치</li>
<li>트래픽이 증가하면 수평적 확장(scale out)을 통해 안정성 확보</li>
<li>오토 스케일링을 통해 적정한 사용량 확보(잘못된 용량 산정으로 안정성 ↓)</li>
<li>인프라 변화 등에 대해 자동화</li>
</ul>
</li>
</ul>
<hr />
<h2 id="네-번째-원칙pillar--지속-가능성">네 번째 원칙(Pillar) : 지속 가능성</h2>
<ul>
<li>에너지 소비 등에 초점을 두어 워크로드 동작시 환경에 미치는 영향을 최소화 하는 능력</li>
<li>디자인 원칙<ul>
<li>클라우드 워크로드가 동작할 때, 작업 단위당 필요한 자원과 배출량 등의 영향을 파악</li>
<li>지속 가능성 목표를 설정하고, 목표 달성을 위해 투자</li>
<li>워크로드를 최적화하고 유휴 리소스를 줄여 에너지 효율성을 높임</li>
<li>새로운 하드웨어 및 소프트웨어 기술을 채택</li>
<li>관리형 서비스를 통해 리소스 활용도 극대화</li>
<li>서비스를 사용하는데 필요한 에너지 또는 리소스 양을 줄임</li>
</ul>
</li>
</ul>
<hr />
<h2 id="다섯-번째-원칙pillar--보안">다섯 번째 원칙(Pillar) : 보안</h2>
<ul>
<li>정보, 시스템, 자산을 보호하고, 기밀성, 무결성, 사용자 권한 관리, 보안 이벤트 관리를 위한 제어</li>
<li>디자인 원칙<ul>
<li>강력한 자격증명 기반을 구현(IAM)<ul>
<li>중앙집중형으로 권한을 관리하고, 최소한의 권한 부여</li>
</ul>
</li>
<li>로그, 지표 등을 통해 시스템의 동작을 추적하고, 이상이 있을 때 자동 조치</li>
<li>아키텍처를 구성할 때 VPC, subnet, load balancer, OS, 애플리케이션 등 모두에 보안 설정</li>
<li>보안 문제는 자동화로 실행되어야 함</li>
<li>데이터 전송 및 저장 중 암호화 등을 통해 보호</li>
<li>사전에 보안 이벤트에 대한 대응 조치 준비</li>
</ul>
</li>
</ul>
<hr />
<h2 id="여섯-번째-원칙pillar--비용-최적화">여섯 번째 원칙(Pillar) : 비용 최적화</h2>
<ul>
<li>불필요하게 발생하는 비용을 줄이고, 최저의 가격으로 비즈니스 가치를 만들어 내는 능력</li>
<li>디자인 원칙<ul>
<li>클라우드 사용 예산을 미리 설정하고, 재무관리 및 비용 최적화</li>
<li>필요한 자원에 대해서 사용한 만큼 금액 지불<ul>
<li>EC2와 람다의 비용 비교</li>
</ul>
</li>
<li>CloudWatch를 통해 리소스를 효과적으로 사용하는지 여부를 측정</li>
<li>비용을 분석해서 어디에 어떻게 지출되고 있는지 파악</li>
<li>자체 데이터 센터에서 클라우드로 마이그레이션하면, 데이터 센터 운영에 필요한 경비가 줄어듦</li>
<li>관리형 서비스는 트랜잭션 또는 서비스 당 비용을 줄여줌<ul>
<li>AWS가 관리해주므로 관리자 및 관리 포인트가 줄어듦</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="aws-well-architected-tool">AWS Well-Architected Tool</h2>
<ul>
<li>AWS 모범 사례와 Well-Architected 6 원칙을 기준으로 자신의 아키텍처를 측정할 수 있도록
하는 서비스<ul>
<li>모범 사례를 통해 중요한 설계 고려 사항을 적용</li>
<li>최종적으로 영상, 문서, 보고서 등의 결과물로 조언을 받을 수 있음</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/93dd7bb8-6b63-461e-834b-4e15ef1f7a07/image.png" /></p>
<hr />
<h2 id="aws-customer-탄소발자국-툴">AWS Customer 탄소발자국 툴</h2>
<ul>
<li>AWS 사용으로 인해 발생하는 탄소 배출량을 추적, 측정, 검토, 예측하는 도구<ul>
<li><a href="https://aws.amazon.com/ko/aws-cost-management/aws-customer-carbon-footprint-tool/">https://aws.amazon.com/ko/aws-cost-management/aws-customer-carbon-footprint-tool/</a></li>
</ul>
</li>
<li>Well-Architected 프레임워크의 지속가능성 목표를 달성하는데 도움</li>
<li>탄소발자국: 제품의 원료채취, 생산, 운송, 유통, 소비, 폐기 등의 전 과정에서 발생하는 이산화탄소
배출량을 환산한 수치(kg 또는 나무 그루수)<ul>
<li>(예) 기차로 100Km 이동 : 2.26Kg(1그루), 5만원 어치 전기 사용 : 33.26Kg(122그루) – 동아일보(2015.12.11)</li>
</ul>
</li>
<li>Amazon은 2040년까지 탄소 넷제로(Net-Zero)에 도달하기 위해 노력 중<ul>
<li>넷제로 : 온실가스의 농도를 인간활동으로 증가시키지 않고, 순배출량을 0으로 만드는 것</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ad2fe196-3978-4a9f-91fa-2ee2792a1b9a/image.png" /></p>