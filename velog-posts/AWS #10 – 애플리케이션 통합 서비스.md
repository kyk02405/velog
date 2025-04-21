<hr />
<h2 id="애플리케이션-통합">애플리케이션 통합</h2>
<ul>
<li>애플리케이션을 구성하는 서비스들의 통합<ul>
<li>AWS에서 독립적으로 구축된 소프트웨어/서비스를 시스템이 자동으로 함께 동작하도록 구현</li>
<li>(예) 서로 다른 서버에서 동작하는 마이크로서비스를 긴밀하게 연결(통합)</li>
</ul>
</li>
<li>특징<ul>
<li>생산성 향상 : 비즈니스 프로세스 전반에 걸쳐 자동화 제공</li>
<li>데이터 통합 지원 : 데이터 사일로 현상 억제, 구성 요소 간의 데이터 통합 제공</li>
<li>고객 호소력 강화 : 고객은 서비스가 상호운용되기를 기대 (예)이메일 계정으로 다른 APP 로그인
로 직접 코딩할 필요 없음</li>
</ul>
</li>
<li>이벤트 기반(Event-driven), 느슨한 결합(Loose coupling), 디커플링(De-coupling)와 같은 설계 기술 필요</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/710c0e7b-b2b4-4126-a97c-25812644adab/image.png" /></p>
<hr />
<h2 id="이벤트-기반event-driven-아키텍처">이벤트 기반(Event-driven) 아키텍처</h2>
<ul>
<li>시스템에서 발생하는 상태 변경 혹은 업데이트 등 <span style="color: red;">액션의 기록</span><ul>
<li>사용자 회원 가입, S3 버킷에 파일 업로드, DynamoDB의 데이터 변경, API Gateway를 통한 API 호출 등</li>
</ul>
</li>
<li>이벤트 기반 아키텍처는 현대적인 클라우드 아키텍처에서 핵심적인 역할 수행</li>
<li>느슨한 결합, 확장성, 유연성, 비용 효율성</li>
<li>동작 구조<ul>
<li>이벤트 생산자<ul>
<li>시스템에서 이벤트를 발생시키는 주체</li>
<li>사용자 애플리케이션, AWS 서비스</li>
</ul>
</li>
<li>이벤트 버스(EventBridge)<ul>
<li>이벤트를 수집하고 적절한 대상으로 라우팅</li>
</ul>
</li>
<li>이벤트 소비자<ul>
<li>Lambda, SQS, SNS</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/746db4f6-ba58-4825-9f4f-cd532c154c07/image.png" /></p>
<hr />
<h2 id="느슨한-결합">느슨한 결합</h2>
<ul>
<li>느슨한 결합(Loose Coupling)<ul>
<li>시스템의 구성 요소들이 서로 독립적으로 작동할 수 있도록 설계</li>
<li>각 구성요소를 독립적으로 변경 가능 → 쉽게 교체 및 추가 가능</li>
<li>유지보수 및 배포 용이</li>
<li>AWS Gateway, EventBridge</li>
</ul>
</li>
<li>긴밀한 결합(Tight Coupling)<ul>
<li>구성 요소 간에 의존하고 있어 변경 어려움</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a1dff973-9db5-476b-b9b9-657fa24c1cfd/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/40ca38a8-dee2-4734-821f-62cdf5a1790e/image.png" /></p>
<hr />
<h2 id="시스템-결합도-비교">시스템 결합도 비교</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7887c021-185b-4738-b667-c0c783e032e5/image.png" /></p>
<hr />
<h2 id="디커플링de-coupling">디커플링(De-Coupling)</h2>
<ul>
<li>시스템의 구성요소 간의 의존성을 줄여 서로의 변경이 다른 구성 요소에 영향을 미치지 않도록 함</li>
<li>특징<ul>
<li>일관성 관리 : 데이터 정합성 보장, 이벤트 순서 보장</li>
<li>장애 격리 : 하나의 서비스에서 발생한 장애가 다른 서비스에 영향을 미치지 않도록 함</li>
<li>유연한 아키텍처 : 시스템 간 의존성을 줄여 아키텍처를 유연하게 설계</li>
<li>확장성 : 각 서비스가 독립적으로 확장 → 트래픽 증가에 유연하게 대응</li>
</ul>
</li>
<li>구현 방법<ul>
<li>메시지 큐 사용 – Amazon SQS</li>
<li>이벤트 기반 아키텍처 – EventBridge, SNS</li>
<li>API Gateway – 서비스 간 인터페이스 추상화</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/402c71fc-61c8-4c02-8ad9-dcdc8ce234a2/image.png" /></p>
<hr />
<h2 id="비교">비교</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/008ced12-c5bc-4269-be89-dbeb6bda53b6/image.png" /></p>
<hr />
<h2 id="애플리케이션-통합-메커니즘">애플리케이션 통합 메커니즘</h2>
<ul>
<li>API<ul>
<li>정의 및 프로토콜 세트를 사용해 두 소프트웨어 구성요소 간의 통신을 제공</li>
<li>gRPC, RESTful API
※ gRPC는 Cloud Native Computing Foundation(CNCF)에서 관리하는 오픈 소스 API 아키텍처
※ RESTful API : HTTP 기반으로 POST, GET, PUT, DELETE와 같은 작업 수행</li>
</ul>
</li>
<li>이벤트 버스<ul>
<li>이벤트를 수신하고 이벤트를 기반으로 애플리케이션 구 성 요소를 서로 연결하는 파이프라인</li>
<li>익명성, 비동기, 이벤트 통신을 하기 때문에 서비스 간 분리 가능</li>
<li>Pub/Sub (게시/구독)</li>
</ul>
</li>
<li>메시징 프로토콜 및 표준<ul>
<li>다양한 메시징 프로토콜 및 표준으로 애플리케이션 간 통신</li>
<li>트리거, 알림, 웹훅</li>
</ul>
</li>
</ul>
<hr />
<h2 id="amazon-sqs">Amazon SQS</h2>
<ul>
<li>Amazon Simple Queue Service</li>
<li><span style="color: red;">완전 관리형 서비스, 서비리스 서비스</span></li>
<li>애플리케이션을 분리하는 <span style="color: red;">디커플링</span> 수행<ul>
<li>웹서버와 애플리케이션 서버를 분리</li>
<li>수강신청시 한꺼번에 수십만건 요청발생,
SQS로 데이터베이스가 감당할 수 있는 속도로 처리</li>
</ul>
</li>
<li>기본 메시지 보유기한은 4일, 최대 14일</li>
<li>큐 안의 메시지 수는 제한없음, 메시지 크기는 최대 256KB</li>
<li>FIFO Queue<ul>
<li>First In First Out : 큐에 들어오는 메시지 순서대로 처리(정확한 순서 보장)</li>
</ul>
</li>
<li>가장 오래된 서비스(AWS 클라우드 처음 생길 때 나온 서비스)</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ba95c483-bd5d-431e-96b2-d03723666702/image.png" /></p>
<hr />
<h2 id="amazon-sns">Amazon SNS</h2>
<ul>
<li>Amazon Simple Notification Service</li>
<li>생산자(publisher)의 메시지를 다수의 구독자(subscriber)에게 전달<ul>
<li>SNS 주제(topic)를 생성 → 이 주제를 구독 신청하면 구독자에게 알림 → 메시지 전달</li>
<li>SQS와 달리 구독한 주제(topic)에만 메시지 획득할 수 있음</li>
<li>유튜브 구독, 알림과 유사</li>
</ul>
</li>
<li>A2A(Application-to-Application) : 분산 애플리케이션의 통합, 분리</li>
<li>A2P(Application-to-Person) : 고객에게 SMS, 푸시 알람, 이메일</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a9057cca-adf3-42e8-925e-e52e9aa01010/image.png" /></p>
<hr />
<h2 id="sqs-vs-sns">SQS vs SNS</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2cf3a93d-8d15-477e-a458-afaa1828db40/image.png" /></p>
<hr />
<h2 id="ses">SES</h2>
<ul>
<li>Amazon Simple Email Service</li>
<li>개발자가 모든 애플리케이션 안에서 이메일을 보낼 수 있는 서비스<ul>
<li>Email을 보내고 받을 수 있는 서비스</li>
</ul>
</li>
<li>대량의 이메일을 보내기 위해서는 AWS Support 센터를 통해 가능(SES 샌드박스 해제)<ul>
<li>스팸 메일이 아닌 것을 확인하는 과정임</li>
<li><span style="color: red;">SES 샌드박스 :</span> 도용 및 침해를 방지하기 위해 맨 처음 구성이 제약되어 있는 환경<ul>
<li>인증된 메일만 발송할 수 있음</li>
<li>하루에 200건 발송 가능</li>
<li>1초에 1건 가능</li>
</ul>
</li>
</ul>
</li>
<li>수신한 메일은 다른 AWS 서비스와 통합가능</li>
<li>S3, Lambda, SNS, Work mail</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5e2dc9de-c390-4804-bebe-6fac52d3fa26/image.png" /></p>
<hr />
<h2 id="amazon-kinesis">Amazon Kinesis</h2>
<p>-<span style="color: red;"> 실시간 빅데이터 스트리밍</span>(Real-time big data streaming)</p>
<ul>
<li>대량의 실시간 스트리밍 데이터를 수집, 처리, 분석하는 관리형 서비스</li>
<li>Kinesis Data Stream<ul>
<li>수 백개 이상의 소스로부터 데이터를 실시간으로 수집, 처리, 분석,하는 서버리스 스트리밍 데이터 서비스</li>
<li>(예) IoT 장치로부터 수집되는 데이터 실시간 처리</li>
</ul>
</li>
<li>Kinesis Data Firehose<ul>
<li>스트리밍을 우리가 원하는 곳(S3, Redshift 등)에 적재 &amp; 데이터 배치 처리</li>
</ul>
</li>
<li>Kinesis Data Analytics<ul>
<li>SQL을 이용해 스트리밍에 대한 실시간 분석</li>
<li>(예) 실시간 대시보드, 복잡한 스트림 처리</li>
</ul>
</li>
<li>Kinesis Video Streams<ul>
<li>ML 등으로 실시간 영상 스트리밍을 모니터링</li>
<li>(예) 보안 카메라 영상 처리, 미디어 스트리밍</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/353a6580-3944-410a-9a62-1dd8bb748ddf/image.png" /></p>
<hr />
<h2 id="api-gateway">API Gateway</h2>
<ul>
<li>완전관리형 서버리스 서비스</li>
<li>서비스 <span style="color: red;">경계</span>에서 클라이언트를 연결(관문 역할)<ul>
<li>IoT 등에서 다양한 클라이언트가 AWS 서비스에 접근할 때 단일 진입점 제공</li>
</ul>
</li>
<li><span style="color: red;">RESTful API,</span> WebSocket API를 생성, 게시, 유지, 모니터링, 보호 하기 위한 서비스</li>
<li>RESTful API<ul>
<li>HTTP 기반 상태 <span style="color: red;">비저장</span> 클라이언트-서버 통신 활성화</li>
<li>표준 HTTP 메서드(GET, POST, PUT, PATCH, DELETE)구현</li>
</ul>
</li>
<li>WebSocket API<ul>
<li>클라이언트-서버 간 상태를 <span style="color: red;">저장</span>하는 전이중 통신</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c89a6f30-c8f1-47ee-84ef-f937b961a754/image.png" /></p>
<hr />
<h2 id="서버리스-컴퓨팅serverless-computing">서버리스 컴퓨팅(Serverless Computing)</h2>
<ul>
<li><p>Server + Less : 서버가 없다는 뜻이 아니라 CSP가 서버를 관리, 실행, 애플리케이션 동작 제공</p>
</li>
<li><p>개발자가 서버를 관리할 필요없이 애플리케이션과 서비스를 구축할 수 있게 해주는 클라우드
컴퓨팅 모델</p>
<ul>
<li>개발자가 비즈니스 로직에만 집중할 수 있게 하는 클라우드 네이티브 방식</li>
</ul>
</li>
<li><p>서버리스 등장 배경 → <span style="color: red;">효율적인 서버 운용</span></p>
<ul>
<li>데이터 센터 운영<ul>
<li>높은 초기 비용, 리소스 활용 비효율</li>
</ul>
</li>
<li>가상화 활용<ul>
<li>리소스 가상화, 유연한 자원 할당</li>
</ul>
</li>
<li>IaaS/PaaS<ul>
<li>탄력적 운영, 관리 부담 감소</li>
</ul>
</li>
<li>서버리스<ul>
<li>서버 관리 불필요, 자동 확장/축소</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/ab505480-15a8-40ba-a30d-676f75b0c218/image.png" /></p>
</li>
</ul>
<hr />
<h2 id="aws-서버리스-서비스">AWS 서버리스 서비스</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/56b8ef8d-fbc0-44e1-bdd5-970ff4ddfc52/image.png" /></p>
<hr />
<h2 id="aws-lambda">AWS Lambda</h2>
<ul>
<li>서버를 프로비저닝 하거나 관리할 필요 없이 <span style="color: red;">코드 실행 가능한</span> 서버리스 컴퓨팅 서비스<ul>
<li>개발자가 서버의 존재를 신경 쓰지 않고, 오직 코드에만 집중</li>
<li>서버가 잘 돌아가도 있는지, 개수와 사양은 적당한지 등 판단할 필요 없음</li>
</ul>
</li>
<li>사용한 컴퓨팅 시간에 대해서만 요금 지불, 코드가 실행되지 않으면 요금 부과 X</li>
<li>지원언어 : Python, C#, Node.js, Ruby, PowerShell, Go 등</li>
<li>제한된 리소스 사용(메모리, 디스크 등 최대 10GB)</li>
<li>최대 실행시간 : 900초(15분)</li>
<li>사용 사례<ul>
<li>서버를 띄우지 않고 간단한 코드를 실행할 경우</li>
<li>특정한 주기로 코드를 실행할 경우(Cron Job)</li>
<li>트리거가 발생할 때만 코드를 실행할 경우</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/4241c147-9c23-4747-a383-359691aa794e/image.png" /></p>
<hr />
<h2 id="참고-람다-트리거">(참고) 람다 트리거</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/cb03378e-fcd4-496a-a085-a33425d89887/image.png" /></p>
<hr />
<h2 id="span-style-color--redaws-lambda-장단점span"><span style="color: red;">AWS Lambda 장/단점</span></h2>
<ul>
<li>낮은 비용<ul>
<li>실제 사용한 만큼 비용 청구</li>
</ul>
</li>
<li>애플리케이션 품질에 집중, 빠른 개발/배포(생산성 향상)<ul>
<li>개발자는 서버 관리에 신경 쓸 필요 없음(FaaS/BaaS 활용)</li>
</ul>
</li>
<li>높은 가용성 및 유연한 확장<ul>
<li>동적으로 자원을 할당, 단기 이벤트에 효과적</li>
</ul>
</li>
<li>콜드 스타트(Cold Start)<ul>
<li>하나의 요청이 끝난 후 함수 실행 시 큰 지연 발생
→ 실시간 서비스 부적합(요청 즉시 실행X)</li>
</ul>
</li>
<li>서버에서 긴 시간동안 요구되는 작업(큰 프로젝트)은 아직 부적절<ul>
<li>1회 호출 시 사용할 수 있는 메모리, 시간 등에 제한</li>
<li>동영상 업로드, 백업 등은 비효율적</li>
</ul>
</li>
<li>무상태(Stateless)<ul>
<li>요청 마다 새로 호출되므로 전후 상태를 공유할 수 없음</li>
</ul>
</li>
<li>CSP에 종속적<ul>
<li>다른 플랫폼((예) AWS → GCP) 으로 이전하기 어려움</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/d169a575-8eb8-44fa-ae4d-258b503d7d42/image.png" /></p>
<ul>
<li><span style="color: red;">콜드 스타트(Cold Start) : 시스템이 처음 시작되거나
장시간 미사용 후 다시 시작될 때의 상태(메모리 초기화)</span></li>
<li><span style="color: red;">웜 스타트(Warm Start) : POST(Power On Self Test)절차를
생략한 소프트웨어적인 부팅, 다시 시작(메모리 유지)</span></li>
</ul>
<hr />
<h2 id="참고-faas--baas">(참고) FaaS / BaaS</h2>
<ul>
<li>FaaS(Function as a Service)<ul>
<li>사용자가 쓸 기능을 함수 단위로 나누어 구현</li>
<li>이벤트가 발생했을 때 해당 함수가 실행되고, 알아서 종료됨</li>
<li>서버가 항상 대기하는 것이 아닌, 이벤트 발생시 실행
※ FaaS는 서버리스 컴퓨팅의 하위 집합</li>
</ul>
</li>
<li>BaaS(Backend as a Service)<ul>
<li>백엔드를 개발자가 개발하지 않고 CSP가 제공, 안정적인 서비스 운용</li>
<li>대표적인 BaaS로는 Firebase!(아래 기능을 제공함)<ul>
<li>실시간 데이터 베이스</li>
<li>사용자 인증</li>
<li>호스팅</li>
<li>클라우드 스토리지</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>  <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/3ca48d2f-6290-4285-9864-5883f5751ff0/image.png" /></p>
<hr />
<h2 id="참고-전통적인-3티어-아키텍처의-변화">(참고) 전통적인 3티어 아키텍처의 변화</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2ee50d51-f912-4cdd-bebe-4a02e13e2ed6/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/0fbce3bc-149f-420a-b90c-dae7738a0d4b/image.png" /></p>
<ul>
<li>서버리스 아키텍처에서는 클라이언트에서 발생한 이벤트를 <span style="color: red;">API Gatewa</span>y를 통해 Lambda로 전달</li>
<li>API Gateway는 <span style="color: red;">REST API</span>로 구현(GET/POST method) → 트리거</li>
<li><span style="color: red;">Lambda 핸들러</span> 실행 후 API Gateway로 응답</li>
<li>API Gateway는 클라이언트에 전달</li>
</ul>
<hr />
<h2 id="lambda를-사용한-모바일-백엔드">Lambda를 사용한 모바일 백엔드</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a74eaf0f-c9e5-49d9-a450-20d853101762/image.png" /></p>
<hr />
<h2 id="aws-batch">AWS Batch</h2>
<ul>
<li>대규모 계산 작업(Batch Job)을 쉽게 처리할 수 있는 관리형 서비스<ul>
<li>Batch Job : 시작과 끝을 가진 대규모 작업(Job), continuous와 대비</li>
<li>보통, Batch Job을 ECS에서 동작하는 Docker 이미지로 정의</li>
</ul>
</li>
<li>사용 사례<ul>
<li>데이터 처리 : 이미지, 비디오, 로그파일 등과 같은 대량의 데이터 처리
(예) 금융회사의 대규모 거래 데이터 분석으로 사기 거래 탐지, 고객 행동 패턴 예측 실시</li>
<li>머신 러닝 : 머신 러닝 모델을 학습하고 배포</li>
<li>과학 시뮬레이션</li>
</ul>
</li>
<li>Jobs : AWS Batch를 실행하는 작업 단위</li>
<li>Job Definition : 배치 작업을 설정/정의<ul>
<li>도커 이미지, 실행 명령어, 환경 변수 등 정의</li>
</ul>
</li>
<li>Job Queue : 실행을 기다리른 Job의 대기열</li>
<li>Compute Environment : Job을 실행하는 인프라<ul>
<li>관리형(Managed) 환경 : On-demand 인스턴스, spot 인스턴스 등 선택 가능</li>
<li>사용자 관리형 : 사용자가 프로비저닝한 EC2 인스턴스 </li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/80c4bee0-de7a-478e-b5c0-d0cd5b5a72e8/image.png" /></p>
<hr />
<h2 id="docker-ecs-ecr">Docker, ECS, ECR</h2>
<ul>
<li>Docker<ul>
<li>앱 배포를 위한 소프트웨어 개발 플랫폼</li>
<li><span style="color: red;">컨테이너</span>  : 애플리케이션, 라이브러리 등을 패키징</li>
<li><span style="color: red;">어디서 실행하든 관계없이 매번 똑같이 실행할 수 있음</span> <ul>
<li>호환성 문제 없이 쉽게 유지보수 및 배포 가능</li>
</ul>
</li>
<li>Docker Repository에 도커 이미지로 저장<ul>
<li>Public : Docker Hub</li>
<li>Private : <span style="color: red;">Amazon ECR</span> (Elastic Container Registry)</li>
</ul>
</li>
</ul>
</li>
<li>ECS(Elastic Container Service)<ul>
<li>도커 컨테이너의 손쉬운 <span style="color: red;">배포, 실행, 관리</span> 하는 완전관리형 컨테이너 오케스트레이션 서비스</li>
<li>EC2 인스턴스를 사전에 만들고, ECS를 통해 컨테이너 실행/정지</li>
<li>다른 AWS 서비스와 연동 – ECR, ALB 등</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/60929055-c2b9-46ae-b9e6-68196a4df738/image.png" /></p>
<hr />
<h2 id="span-style-color--redfargatespan"><span style="color: red;">Fargate</span></h2>
<ul>
<li>ECS와 동일하게 <span style="color: red;">AWS에서 컨테이너 실행</span> </li>
<li>But, EC2 인스턴스를 프로비저닝 할 필요 없음!!</li>
<li><span style="color: red;">서버리스</span> <ul>
<li>AWS가 각 컨테이너의 CPU, 메모리 등을 파악하고 컨테이너 실행</li>
</ul>
</li>
<li>Fargate는 단독으로 사용하지 않고, ECS 혹은 EKS와 함께 사용<ul>
<li>ECS + Fargate : ECS가 AWS에 종속적이며, 비교적 단순환 컨테이너 애플리케이션에 활용</li>
<li>EKS + Fargate : 서버관리를 최소화하며 K8S의 유연성, 확장성을 활용(대규모 복잡한 애플리케이션)</li>
<li><span style="color: red;">EKS</span> (Elastic Kubernetes Service) :<ul>
<li>AWS에서 K8S를 쉽게 사용할 수 있도록 제공 – 배포, 스케일링, 관리</li>
<li>대규모 컨테이너 애플리케이션을 다룰때 사용 </li>
</ul>
</li>
</ul>
</li>
</ul>
<p> <img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c62f2e07-fd4f-42f8-ba27-31e86e4c135c/image.png" /></p>
<hr />
<h2 id="참고-amazon-ecs-vs-amazon-eks">(참고) Amazon ECS vs Amazon EKS</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/c27520e8-cdb2-4c01-bced-a598a693ae73/image.png" /></p>
<hr />
<h2 id="lightsail">Lightsail</h2>
<ul>
<li>가상 프라이빗 서버(Virtual Private Server, VPS)<ul>
<li>가상 머신(VM)의 한 종류로써 웹 호스팅 용도로
최적화</li>
<li>애플리케이션 또는 웹사이트 실행에 필요한 모든
소프트웨어를 호스팅하는 머신</li>
</ul>
</li>
<li>(클라우드를 모르는 사람일지라도) 웹 서비스를
빠르고 쉽게 구축</li>
<li>가상 서버(EC2), 데이터베이스(RDS) 등을 따로
구축하지 않고 Lightsail 하나로 웹서버 운용<ul>
<li>매우 저렴하고 쉽게 구축 가능</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/2de95f7c-e0aa-4bf2-9645-f64d0d4d5334/image.png" /></p>
<hr />
<h2 id="클라우드에-최적화된-현대적인-애플리케이션-설계">클라우드에 최적화된 현대적인 애플리케이션 설계</h2>
<ul>
<li>아키텍처 : 마이크로 서비스 아키텍처(MSA)<ul>
<li>애플리케이션을 더 쉽게 확장하고, 개발 속도를 단축해 출시 시간 단축</li>
</ul>
</li>
<li>S/W 배포 : 자동화 및 표준화(CI/CD), IaC(Infra as Code)<ul>
<li>자동화된 릴리즈 파이프라인으로 오류를 최소화, 신속화 테스트를 통한 릴리즈</li>
</ul>
</li>
<li>데이터 : 디커플링 및 용도에 최적화<ul>
<li>데이터베이스와 마이크로서비스를 디커플링함으로써
요구사항에 적합한 데이터베이스를 선택
(예) DynamoDB(확장성), Aurora(효율성)</li>
</ul>
</li>
<li>운영 : 애플리케이션 스택별 서버리스 서비스 활용<ul>
<li>애플리케이션 운영 환경을 관리할 필요 없음</li>
</ul>
</li>
<li>보안 : 개발 수명 주기의 전체 단계에 긴밀히 통합</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/1f8eba17-5da1-407e-872b-20ebfba4a382/image.png" /></p>