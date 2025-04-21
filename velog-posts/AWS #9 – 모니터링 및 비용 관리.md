<hr />
<h2 id="aws-모니터링-서비스">AWS 모니터링 서비스</h2>
<ul>
<li>AWS는 200개가 넘는 다양한 서비스와 리소스가 존재<ul>
<li>다수의 계정(IAM 사용자 포함)으로 접근</li>
<li>관리콘솔, CLI, SDK, API 등 다양한 방식으로 접근</li>
</ul>
</li>
<li>AWS 관리자는 모든 상황을 관찰 &amp; 통제해야 함<ul>
<li>시스템 전반에 대한 운영 상황 관찰</li>
<li>애플리케이션의 성능</li>
<li>리소스 사용에 대한 관찰 및 통제</li>
<li>비용 효율화/최적화 설계</li>
<li>보안</li>
<li>유지보수</li>
</ul>
</li>
<li>일정 시간이 지나도 특정 시점에 무슨 일이 있었는지 파악할 수 있어야 함<ul>
<li>누가, 언제, 어떤 리소스에, 어떤 방식으로 접근했는지 등</li>
</ul>
</li>
</ul>
<hr />
<h2 id="대표적인-aws-모니터링-서비스">대표적인 AWS 모니터링 서비스</h2>
<ul>
<li><p><span style="color: red;"> Amazon CloudWatch </p>
</span>
</li>
<li><p><span style="color: red;">AWS CloudTrail</span></p>
</li>
<li><p>AWS X-Ray</p>
</li>
<li><p>Amazon Managed Grafana</p>
</li>
<li><p>Amazon Managed Service for Prometheus</p>
</li>
<li><p>Amazon GuardDuty</p>
</li>
<li><p>VPC Traffic Mirroring</p>
</li>
</ul>
<hr />
<h2 id="cloudwatch-대시보드">CloudWatch 대시보드</h2>
<ul>
<li>사용 중인 리소스 목록, 개별 리소스 사용량 추이, 비용 관련 정보 등 제공</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/36fb0168-62ee-4da1-9bc5-66acae3d80b8/image.png" /></p>
<hr />
<h2 id="cloudwatch">CloudWatch</h2>
<ul>
<li><p>AWS 리소스 및 애플리케이션 모니터링 서비스</p>
</li>
<li><p>로그, 지표, 이벤트 등의 운영 데이터를 수집화해서 시각화</p>
</li>
<li><p><strong>CloudWatch Logs</strong></p>
<ul>
<li>EC2 인스턴스 로그, CloudTrail 이벤트 로그, Route 53 DNS 쿼리 등 다양한 서비스 생성 로그 저장 및 액세스</li>
</ul>
</li>
<li><p><strong>CloudWatch Alarm</strong></p>
<ul>
<li>일정 기간 동안 지정 임계값과 지표값 비교, SNS 알림 전송, Auto Scaling 작업 수행 등 작업 수행</li>
</ul>
</li>
<li><p><strong>Event Bridge(=CloudWatch Event)</strong></p>
<ul>
<li>서비스, 앱, 마이크로서비스 등에서 유입된 이벤트를 수집, 분류해 SNS 알림 전송, Lambda 실행 등 작업 수행</li>
</ul>
</li>
</ul>
<hr />
<h2 id="cloudwatch-구조">CloudWatch 구조</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b0b56217-80cc-43d2-a5a1-c0f3af209878/image.png" /></p>
<ul>
<li><strong>Instance ID Type Auto Scaling Group CPU Utilization</strong><ul>
<li>지표(metric): 시간 순서로 정리된 데이터의 집합<ul>
<li>EC2 인스턴스: CPU 사용량, 상태 체크, 네트워크</li>
<li>EBS 볼륨: 디스크의 읽기(read)/쓰기(write)</li>
<li>S3 버킷: 버킷 사이즈, 객체 수</li>
<li>Billing: 하나의 리전에서 추정하는 비용</li>
<li>Service Limits: Service API를 얼마나 사용했는지 여부</li>
<li>Custom metrics: 메모리 관련 확인 가능</li>
</ul>
</li>
<li>네임스페이스(namespace): 지표를 논리적으로 묶은 단위 (AWS/{서비스명})</li>
<li>차원(dimension): 지표를 식별하기 위한 키-값으로 구성</li>
<li>통계값(statistics): 최소, 최대, 합계, 평균 등 지표값 분석</li>
</ul>
</li>
</ul>
<hr />
<h2 id="지표metric">지표(metric)</h2>
<ul>
<li>시간 순서로 정리된 데이터의 집합<ul>
<li>EC2 인스턴스 : CPU 사용량, 상태 체크, 네트워크(RAM은 해당 안됨)</li>
<li>EBS 볼륨 : 디스크의 읽기(read)/쓰기(write)</li>
<li>S3 버킷 : 버킷 사이즈, 객체수</li>
<li>Billing : 하나의 리전에서 추정하는 비용</li>
<li>Service Limits : service API를 얼마나 사용했는지 여부</li>
<li>Custom metrics</li>
</ul>
</li>
<li>기본적으로 AWS의 모든 서비스(EC2, RDS, ASG, ELB, Rout53 등)에서 지표(metric) 제공</li>
<li>커스텀 지표 생성 가능<ul>
<li>CloudWatch agent를 사용해 지표, 로그, 추적 수집</li>
<li>특히, 메모리 관련 내용(사용량 등) 확인에 사용</li>
</ul>
</li>
<li>지표는 Timestamps를 가지며, 이것을 기반으로 대시보드에 나타냄</li>
</ul>
<hr />
<h2 id="참고-cloudwatch의-동작">(참고) CloudWatch의 동작</h2>
<ul>
<li>CloudWatch로 Amazon Aurora 지표 모니터링</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/7c56a7fa-afa9-4910-9f50-027e2b9e2e7e/image.png" /></p>
<hr />
<h2 id="참고-cloudwatch-agent로-인스턴스-메트릭-수집">(참고) CloudWatch Agent로 인스턴스 메트릭 수집</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/13bf33fb-66f7-4a7d-ac6a-8cf9b62e2fd2/image.png" /></p>
<hr />
<h2 id="네임스페이스namespaes">네임스페이스(Namespaes)</h2>
<ul>
<li>네임스페이스(Namespace)<ul>
<li>지표(metric)을 논리적으로 묶은 단위</li>
<li><span style="color: skyblue;">AWS/{서비스명}</span>과 같은 형태로 네임스페이스 표시<ul>
<li>AWS/EC2, AWS/RDS</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5154b5c4-18d8-485f-a1e8-d99a617b3da6/image.png" /></p>
<h2 id="참고-cloudwatch-logs">(참고) CloudWatch Logs</h2>
<ul>
<li>AWS 내외의 로그를 모아 보관하고 사용자에게 전달<ul>
<li>각종 서비스에서 생성된 로그를 수집, 모니터링</li>
<li>로그 보존 기간 설정 가능 (7일, 30일, 1년, 혹은 영원히)</li>
<li>로그를 S3, Lambda, Elastic Search 등으로 전송 가능</li>
</ul>
</li>
</ul>
<hr />
<h2 id="차원dimension">차원(Dimension)</h2>
<ul>
<li>지표(Metric)을 식별하기 위해 키-값으로 구성</li>
<li>(예) AWS/EC2 네임스페이스를 구성하는 각각의 EC2(instanceId로 구분)<ul>
<li>키 : EC2의 instanceId, 값: 실제 instanceId 값</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/554ab5b4-3c91-493f-b557-8f1168b3e47b/image.png" /></p>
<hr />
<h2 id="통계값statistics">통계값(Statistics)</h2>
<ul>
<li>각 지표에 따라 적절한 통계값 설정 및 확인 가능</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/20f3ab1b-ffd0-4c3e-92f5-9f4f4335b63a/image.png" /></p>
<hr />
<h2 id="정리-cloudwatch-구조">(정리) CloudWatch 구조</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/be8a2c36-fe42-4a1e-902a-bc5c9edac3c7/image.png" /></p>
<hr />
<h2 id="사례-cloudwatch를-통한-프로세스-모니터링">(사례) CloudWatch를 통한 프로세스 모니터링</h2>
<ul>
<li>CloudWatch 알람을 통해 EC2 인스턴스 재시작은 가능하나, 인스턴스 안의 프로세스 재시작은 불가능</li>
<li>EC2 인스턴스 내에 CloudWatch Agent를 설치하고, SSM Agent를 이용해 원격으로 프로세스 재시작이
가능하도록 구성
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b408d718-ea8b-4f02-86cf-ef6653c7907e/image.png" /></li>
</ul>
<hr />
<h2 id="cloudwatch-logs">CloudWatch Logs</h2>
<ul>
<li>AWS 내외의 로그를 모아 보관하고 사용자에게 전달</li>
<li>각 종 서비스가 실행되면서 생성한 로그 파일 수집 &amp; 모니터링<ul>
<li>EC2 인스턴스 로그 모니터링</li>
<li>Elastic Beanstalk</li>
<li>컨테이너로부터 수집된 로그(ECS)</li>
<li>AWS Lambda가 실행한 함수 로그</li>
<li>CloudTrail 이벤트 모니터링</li>
<li>Route 53 DNS 쿼리 로그</li>
<li>CloudWatch log agents(EC2 / on-premise 서버)</li>
</ul>
</li>
<li>로그에 대한 실시간 모니터링 가능 → 실시간 대응</li>
<li>로그는 7일, 30일, 1년, 혹은 영원히 보존 설정 가능</li>
<li>수집된 로그는 S3, Lambda, Elastic Search 등으로 전송됨</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/fd552964-9173-468a-980c-5ea43c22ba07/image.png" /></p>
<hr />
<h2 id="참고-cloudwatch-alarms">(참고) CloudWatch Alarms</h2>
<ul>
<li>임계값(Threshold) 설정에 따른 알람 생성</li>
<li>다양한 시나리오로 대응<ul>
<li>EC2 인스턴스의 Auto Scaling에 따라 알람</li>
<li>EC2 인스턴스의 상태(stop, terminate, reboot 등) 알람</li>
<li>웹서버 장애에 대한 알람(Slack, telegram 활용)</li>
<li>Billing metric에 따른 Billing 알람</li>
</ul>
</li>
<li><span style="color: red;"> 3가지 상태 </span><ul>
<li>OK : 정상</li>
<li>Alarm : 임계값 초과</li>
<li>INSUFFICIENT_DATA : 데이터 부족</li>
</ul>
</li>
<li>Sampling, % 표시, 최대값, 최소값 등</li>
<li>알람 평가 주기 설정(5분, 10분, 1시간 등)</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/92de84e4-f1d8-49a1-8d10-5b94ec6af21b/image.png" /></p>
<hr />
<h2 id="amazon-eventbridge-cloudwatch-events">Amazon EventBridge (CloudWatch Events)</h2>
<ul>
<li><span style="color: red;">서버리스 Event Bus 서비스</span>(대량의 이벤트 전송 및 처리)<ul>
<li>Event Bus : Event 소스에서 이벤트를 수집해 목적지(target)까지 전달하는 시스템</li>
<li>Event Bus 종류<ul>
<li><span style="color: red;">기본 이벤트(AWS 서비스), 커스텀 이벤트(사용자 정의 APP), 파트너 이벤트(SaaS APP과 통합) </span></li>
</ul>
</li>
</ul>
</li>
<li>운영 오버헤드 감소, 대규모 이벤트 기반 아키텍처 구축<ul>
<li>이벤트에 따라 효율적인 AWS 리소스 사용(Auto scaling 등)</li>
<li>복잡한 이벤트 패턴도 마우스 클릭으로 구성 가능</li>
</ul>
</li>
<li>EventBridge의 동작<ul>
<li>스케줄 된 이벤트 : Cron Jobs<ul>
<li>사전에 정의된 시간 또는 시간 간격으로 작업 수행</li>
<li>(예) 매 시간 Lambda function 수행</li>
</ul>
</li>
<li>이벤트 패턴 : 임의의 서비스를 수행하면 이벤트 룰에 따라 미리 정한 event rule 수행<ul>
<li>(예) IAM 사용자가 로그인하면 관리자에게 Email 전송</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a017ca85-2c80-4062-8195-90c2d9f1c7b7/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/a8a417f2-b1ea-4bec-818b-8c64c3882c4d/image.png" /></p>
<hr />
<h2 id="cloudtrail">CloudTrail</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/f899766b-1aec-4950-8ddc-b9dca6c808a2/image.png" /></p>
<ul>
<li>AWS 계정의 거버넌스, 규정 준수, 운영 감사, 위험 감사를 지원하는 서비스</li>
<li>계정을 사용할 때 기본적(default)으로 활성화됨</li>
<li>AWS 계정에서 일어난 모든 이벤트 및 API 호출을 로그로 제공하여 추적함<ul>
<li>관리콘솔, AWS CLI, SDK, AWS 서비스, API 호출 등 모든 이벤트 대상</li>
<li>“누가, 언제, 어디서, 어떻게” 서비스를 이용했는지 확인</li>
</ul>
</li>
<li>(데이터를 장기 보존하려면) CloudWatch Logs 또는 Amazon S3로 전송</li>
<li>모든 리전(default) 또는 단일 리전 추적 선택 가능</li>
<li><span style="color: red;">(시험) 만약 AWS에서 어떤 자원이 삭제되었다면, 누가, 무엇을, 언제 삭제했는지 확인할 수 있는가? </span></li>
</ul>
<hr />
<h2 id="cloudwatch와-cloudtrail-비교">CloudWatch와 CloudTrail 비교</h2>
<ul>
<li>CloudWatch : <span style="color: red;">성능 모니터링</span>과 운영에 중점</li>
<li>CloudTrail : 보안, <span style="color: red;">감사</span>, 규정 준수에 중점</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b93b7914-ad16-409c-b656-b002347f820b/image.png" /></p>
<hr />
<h2 id="cloudwatch의-ec2-resource-health">CloudWatch의 EC2 Resource Health</h2>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/78c4f0fa-5f5e-4a2e-90be-dbfda27e68d7/image.png" /></p>
<ul>
<li>Amazon EC2의 <span style="color: red;">현재 상태 정보를 시각적으로 표현</span>해주는 실시간 서비스</li>
<li>임계값과 색 구성표를 정의해서
CPU, 메모리 사용률 등을 색으로 상태 표시<ul>
<li>0<del>10 : 흰색, 10</del>50 : 주황색, 50~100 : 빨간색</li>
<li>임계값 별 색상 조정 가능</li>
</ul>
</li>
<li>주요 커스터마이징 기능<ul>
<li>Metric : CPU 사용률, 메모리 사용률, 상태 검사</li>
<li>Group by capability<ul>
<li>노드를 그룹으로 분할</li>
<li>AZ, 태그, VPC, 인스턴스 유형, 인스턴스 상태 등 기준</li>
</ul>
</li>
<li>Filter by capability<ul>
<li>하나 이상의 필터를 선택하여 보기를 좁힘</li>
<li>인스턴스 상태, 가용영역, EBS 볼륨, 보안그룹 등 속성 기준</li>
</ul>
</li>
<li>Sort by capability<ul>
<li>상태체크, 인스턴스 상태, 메모리, CPU 알람 기준</li>
<li>오름차순/내림차순 정렬</li>
</ul>
</li>
</ul>
</li>
</ul>
<hr />
<h2 id="aws-x-ray">AWS X-Ray</h2>
<ul>
<li>마이크로 서비스 아키텍처(MSA)를 포함한 <span style="color: red;">분산 애플리케이션을 분석</span>하는 서비스<ul>
<li>모놀리스(monolith) 구조의 애플리케이션은 분석 &amp; 디버깅 하기 쉽지만,</li>
<li>마이크로 서비스 아키텍처(MSA)과 같은 분산된 서비스와 같은 복잡한 구조는 어려움</li>
</ul>
</li>
<li>애플리케이션과 기본 서비스가 어떻게 동작하는지 이해하고, 장애에 대한 근본 원인 해결<ul>
<li>애플리케이션을 <span style="color: red;">추적하고 시각적 분석</span> 가능</li>
<li>병목 현상 등을 확인해 성능 개선 가능</li>
<li>(예) End-to-End 추적, 서비스 맵 시각화, 지연시간, 오류, 병목현상 식별, 실시간 문제 해결 등</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/00f2520d-9990-4acb-b656-eb17c8e9b4cb/image.png" /></p>
<hr />
<h2 id="aws-결제-및-비용-관리">AWS 결제 및 비용 관리</h2>
<ul>
<li>클라우드 사업자는 청구서 제공시, 사용자가 이해하기 쉽고 정확한 근거 자료 제시해야 함<ul>
<li>사용자가 AWS리소스를 사용할 때, 어떤 것을, 얼만큼 사용했는지 정확히 파악 필요</li>
</ul>
</li>
<li>AWS에서는 결제 및 비용 관리(Billing &amp; Cost Management)에서 제공</li>
<li>(사례) 1755만원 요금 폭탄!!</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/8d2dbfac-c11c-4732-bc16-995f1668271d/image.png" /></p>
<hr />
<h2 id="비용-및-사용-보고서cost--usage-report-cur">비용 및 사용 보고서(Cost &amp; Usage Report, CUR)</h2>
<ul>
<li>AWS 사용 내역을 자세히 확인<ul>
<li>AWS 리소스 사용량, 비용, 예상 비용 등</li>
<li>CSV 파일 형태로 보고서 생성</li>
<li>사용 내역 추적을 통해 비용 절감 및 AWS 운영 상태 파악 가능</li>
</ul>
</li>
<li>현재 지원 중단 보류 중이며, “과금 정보 및 비용 관리 &gt; 데이터 내보내기”로 변경(CUR 2.0)</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/b2588d5f-221d-4b72-ae35-ba3a6eb9af81/image.png" /></p>
<hr />
<h2 id="비용-할당-태그cost-allocation-tags">비용 할당 태그(Cost Allocation Tags)</h2>
<ul>
<li>더 상세하게 비용을 추적하고 분류할 수 있게 함</li>
<li>AWS에서 생성되는 비용할당 태그<ul>
<li>AWS 리소스를 사용하면서 자동으로 적용</li>
<li>(예) <span style="color: red;">aws:</span>createdBy</li>
</ul>
</li>
<li>사용자 정의 비용할당 태그<ul>
<li>사용자가 정의</li>
<li>(예) <span style="color: red;">user:</span> Name</li>
</ul>
</li>
<li>보통 태그에 이름, 환경, 팀 등에 관한 사항을 기재<ul>
<li>같은 태그로 그룹/필터링해서 작업 수행</li>
<li>보고서 생성시 태그 정보를 통해 효율적인 관리</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/906e1cc8-1b6b-47a4-bea2-f075b867ee74/image.png" /></p>
<hr />
<h2 id="프리티어">프리티어</h2>
<ul>
<li>AWS 서비스를 특정 사용량 한도 내에서 무료로 사용(<a href="https://aws.amazon.com/ko/free">https://aws.amazon.com/ko/free</a>)<ul>
<li>상시 무료 : AWS 고객은 만료 없이 사용 가능</li>
<li>12개월 무료 : 최초 가입일로부터 12개월 간</li>
<li>단기 평가판 : 12개월 미만의 기간 동안 일정 한도 사용</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/96fe3931-68b8-4c15-908a-1705387e63c6/image.png" /></p>
<hr />
<h2 id="비용-탐색기cost-explorer">비용 탐색기(Cost Explorer)</h2>
<ul>
<li>일정 기간 동안의 비용과 그 원인 리소스 사용의 상세 정보 제공<ul>
<li>AWS 리소스의 사용량과 비용을 그래프로 시각화, 데이터 분석 제공</li>
<li>최근 몇 달 동안의 비용 흐름을 파악해 예상 외의 비용 발생 부분이 무엇인지 추적</li>
</ul>
</li>
<li>클라우드에서 하나의 서비스를 사용했지만,<ul>
<li>실제로는 연계된 다른 서비스가 함께 사용되면서 비용 발생</li>
<li>특정 서비스를 종료 했지만 연계된 서비스는 종료되지 않아 비용이 계속 발생</li>
<li>(예) EC2 인스턴스를 종료했지만, ASG 활성화 되어 있을 경우 EC2 인스턴스 재생성</li>
</ul>
</li>
<li>사용자 맞춤형 보고서 생성<ul>
<li>보고서 매개변수를 선택하여 보고서 생성 → 라이브러리에 저장</li>
<li>일별 비용, 연결된 계정별 월별 비용, 서비스별 월별 비용 등</li>
</ul>
</li>
<li>절감형 플랜(Saving Plan)을 추천</li>
<li><span style="color: red;"> (시험) 이전 사용량을 분석해서 +1, +3, +12개월의 추정 비용(Forecast Usage) 제공</span> </li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/887639da-8168-425d-a0bd-8c8f62be25f3/image.png" /></p>
<hr />
<h2 id="aws-budgets">AWS Budgets</h2>
<ul>
<li>AWS에서 발생한 비용 및 사용량 추적하는 서비스<ul>
<li>시간별 비용/사용량을 지속적으로 파악해 비용/사용량이 임계값을 초과하면 알람(이메일)</li>
</ul>
</li>
<li>사용자가<span style="color: red;"> 지정한 비용 </span> 이상이 발생하면 대응<ul>
<li>(예) SNS와 Lambda를 이용한 대응(slack 알람 등)</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/kyk02405/post/5bbd6a71-fafd-48aa-beef-632bf7a91e1c/image.png" />
<img alt="" src="https://velog.velcdn.com/images/kyk02405/post/adc5621a-b6b8-455f-b175-4f637e6b7806/image.png" /></p>