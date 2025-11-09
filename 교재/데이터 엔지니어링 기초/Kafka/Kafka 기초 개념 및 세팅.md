# Kafka 구조
## 챕터의 포인트
- Kafka 개요
- Kafka의 기본 구조 및 동작 원리
- Kafka 클러스터 구조 및 데이터 분산
- Kafka 설치

# 카프카 개요

## 메세징 시스템이란?
- 어플리케이션 간 데이터를 교환하는 비동기적 방식의 데이터 전송 시스템
  - 메시지를 생산하는 생산자(Producer), 관리하는 브로커(Broker), 소비하는 소비자(Consumer)로 구성
  - 간혹 브로커가 없는 경우도 있음 (Redis Pub/Sub, ZeroMQ 등)

- 메시징 시스템의 특징
  - 안정적인 구조: 비동기적 방식이라 시스템 간 결합이 느슨함  
  - 뛰어난 확장성: 브로커만 추가하면 성능이 선형적으로 증가


## 카프카란?
- 대규모 데이터 처리에 적합한 분산형 메시징 시스템
  - 카프카 브로커(Broker): 카프카의 메시지를 관리하는 서버(브로커)
  - 토픽(Topic): 카프카의 메시지를 관리하는 논리적 단위. 카테고리라고 보면 됨
  - 파티션(Partition): 토픽을 이루는 저장 단위. 파티션 기반으로 병렬 처리가 이루어짐

```
Kafka Cluster
├── Kafka Broker 1
│ ├── Topic A → Partition 0,1
│ └── Topic B → Partition 0
├── Kafka Broker 2
│ └── Topic A → Partition 2
└── Kafka Broker 3
└── Topic B → Partition 1
```

## 카프카의 역할

### 데이터 파이프라인에서 카프카의 역할
- 카프카는 스트리밍형 데이터 수집에 뛰어난 도구
- 스트리밍 데이터 수집: 지속적으로 발생하는 데이터를 즉각 수집 및 처리
- 사용 예시: 금융 데이터, 센서 값, 실시간 로그

## 카프카의 장점
- 카프카를 쓰는 이유
  - 고성능: 초당 수백만 개의 메시지 처리 가능  
  - 확장성: 브로커 추가만으로 성능 선형 확장  
  - 내결함성: 백업본 관리와 모니터링을 통한 장애 복구  
  - 메시지 유지: 메시지를 장기간 저장 가능 → 과거 데이터 재처리 가능  
  - 이벤트 기반 구조: 여러 소비자가 동일한 데이터 읽기 가능  

# Kafka의 기본 구조 및 동작 원리

## Kafka의 핵심 개념
- 주요 개념 요약
  - 생산자(Producer): 메시지를 브로커에 전송  
  - 소비자(Consumer): 브로커에서 메시지를 소비

## Kafka의 핵심 개념
- 주요 개념 요약
  - 토픽(Topic): 메시지를 저장하는 논리적 단위, 택배를 찾을 때 주소 같은 느낌  
  - 파티션(Partition): 메시지를 병렬로 처리하기 위한 단위, 큐와 유사함, 택배 창고 같은 느낌  
  - 브로커(Broker): 메시지를 관리하는 Kafka의 서버  
  - 클러스터(Cluster): 함께 동작하는 Kafka 서버 집단

## Kafka의 핵심 개념
- 주요 개념 요약  
  - Zookeeper: Kafka의 클러스터를 관리해주는 분산 관리 시스템

## Kafka의 기본 구조
- 주요 개념 요약  
  - Zookeeper: Kafka의 클러스터를 관리해주는 분산 관리 시스템

## Kafka의 토픽과 파티션
- 토픽과 파티션
  - 토픽(Topic): 메시지를 저장하는 논리적 단위, 택배를 찾을 때 주소 같은 느낌  
  - 파티션(Partition): 메시지를 병렬로 처리하기 위한 단위, 택배 창고 같은 느낌  
  - 오프셋(Offset): 파티션의 데이터를 가리키는 숫자

## Kafka의 토픽과 파티션
- 토픽과 파티션
  - 토픽(Topic): 메시지를 저장하는 논리적 단위, 택배를 찾을 때 주소 같은 느낌  
  - 파티션(Partition): 메시지를 병렬로 처리하기 위한 단위, 택배 창고 같은 느낌  
  - 오프셋(Offset): 파티션의 데이터를 가리키는 숫자  
  - 순차쓰기 → 임의쓰기

## Kafka의 토픽과 파티션
- 토픽과 파티션
  - 토픽(Topic): 메시지를 저장하는 논리적 단위, 택배를 찾을 때 주소 같은 느낌  
  - 파티션(Partition): 메시지를 병렬로 처리하기 위한 단위, 택배 창고 같은 느낌  
  - 오프셋(Offset): 파티션의 데이터를 가리키는 숫자  
  - 파티션 단위로만 순서 유지 → 순서가 중요한 시스템 X

# Kafka의 데이터 저장방식

## Kafka의 저장방식
- 토픽 / 파티션의 물리적인 위치는?
  - 메모리? 대용량 데이터를 다루려면 많은 데이터가 필요할 것 같은데..
  - 스토리지? 그러면 빠른 입출력이 불가능할텐데…

  빠른 속도  
  작은 용량  
  비싼 가격  
  불안정  

  큰 용량  
  저렴한 가격  
  안정적  
  느린 속도  

## Kafka의 저장방식
- 세그먼트(Segment) 파일  
  - 세그먼트: 파티션이 실제로 저장되는 물리적 단위. 파일 형태.

## Kafka의 저장방식
- 세그먼트(Segment) 파일  
  - 세그먼트: 파티션이 실제로 저장되는 물리적 단위. 파일 형태.  
  1. 오래된 데이터 관리  
    - Segment 1  
    - 마지막 사용 날짜: 7일전  
  2. 파일 수정 속도 최적화  
  3. 메시지 탐색 속도 향상  

## Kafka의 저장방식
- Kafka의 실제 데이터  
  - kafka/config/server.properties 파일에 가면 저장 경로를 확인할 수 있음  

## Kafka의 저장방식
- Kafka의 파일 타입  
  - 모두 [시작 인덱스].[확장자]의 형식  
  - 모두 Binary 파일 → 빠른 읽기 속도  
  - 실제 데이터: 실제로 데이터가 들어있는 파일. XXX.log의 형식  
  - 인덱스 파일: 오프셋을 빠르게 찾기 위한 색인용 파일. XXX.index의 형식  
  - 타임스탬프: 시간 기준 검색을 위한 파일. XXX.timeindex의 형식  

# Kafka의 클러스터 구조 및 데이터 분산

## Kafka 클러스터
- 클러스터를 구성하는 이유  
  - 동시에 더 많은 데이터를 처리할 수 있음 (High Throughput)  

## Kafka 클러스터
- 클러스터를 구성하는 이유  
  - 높은 Throughput: 동시에 더 많은 데이터를 처리할 수 있음  
  - 데이터 안정성: 복제를 통해 데이터 유실률을 낮춤  
  - 고가용성: 하나의 브로커가 문제가 생기더라도 전체 시스템은 멈추지 않음 

## Kafka 클러스터
- 클러스터 관리  
  - 공통 메타데이터 및 자원 관리  
  - 관리의 복잡성 증가: 장애 대처 알고리즘, 파티션 할당 등  
  - 분산 시스템 아키텍처: 네트워크 트래픽, 디스크 용량, 다중 모니터링 시스템 등 고려하여 설계 필요  

## Kafka 클러스터
- Kafka와 Zookeeper  
  - Zookeeper: Kafka의 클러스터를 관리해주는 분산 관리 시스템  
  - 코디네이션 서비스 시스템: Zookeeper 처럼 분산 시스템 관리를 도와주는 시스템

## Kafka 클러스터
- Zookeeper의 역할  
  - 공용 리소스 관리: 브로커들이 공동으로 사용하는 리소스/데이터 관리  
  - 노드 Healthcheck: 브로커(노드/서버)가 정상 동작 중인지 확인
  - 브로커 및 파티션 관리: 메인 파티션의 Leader 선출 및 메인 브로커인 Controller 선출을 도움

## Kafka 클러스터 구조
- Kafka의 컨트롤러
  - 컨트롤러(Controller): 클러스터 관리 및 장애 처리 역할 수행  
  - Broker 1 등록 → /controller znode 등록  
  - Broker 2, 3 등록 실패 (하나의 Controller만 존재)

## Kafka 데이터 분산
- Kafka의 리더와 팔로워
  - 레플리카(Replica): 파티션 데이터를 보존하기 위해 복사본을 두는 것  
  - 리더(Leader): Producer, Consumer와 통신하는 메인 파티션(레플리카)  
  - 팔로워(Follower): 리더의 데이터를 실시간으로 복사해 가지는 파티션(레플리카)

## Kafka의 리더 선출  
- Zookeeper Controller  
- 선호 리더(Prefered Leader): 파티션별로 가장 선호하는 리더, 기본적으로 Round Robin  
- 처음에는 선호 리더에 맞추어 리더가 결정됨

## Kafka의 리더 선출  
- 리더 선출(Leader Election): 기존 리더 브로커가 사망했을 때 다음 리더를 뽑는 것  
- ISR(In-Sync Replica): 리더와 완전히 같은 값을 가진 팔로워

## Kafka의 리더 선출  
- 팔로워 중 ISR에 속한 것이 있는 경우 가장 빠른 순서가 리더가 됨

## Kafka의 리더 선출  
- 팔로워 중 ISR이 없는 경우 ISR이 나타날 때까지 기다림 (혹은 리더가 복구)
- unclean.leader.election.enable = true 옵션 사용 시 그나마 가장 최신 데이터를 가진 팔로워가 리더가 됨

## Kafka의 리더 선출  
- unclean.leader.election.enable = true 옵션 사용 시 원래 브로커가 복구된다해도 팔로워로 참여
- 카프카는 리더의 데이터를 절대적으로 신뢰함

# Kafka 설치

## Kafka 환경 설정  
- 설치 전 필수 요소: 운영체제, Java, Zookeeper  
- Kafka는 여러 개의 브로커(서버)와 토픽-파티션으로 이루어지고 Zookeeper가 이를 관리해줌

## 운영체제 선택  
- Kafka를 실행할 운영체제  
  - JVM 기반이라 다양한 운영체제에서 실행 가능  
  - Linux 환경이 가장 안정적이며 추천됨  
  - Windows는 WSL 환경 추천

## Java 설치 -1 (공식 홈페이지를 통한 설치)  
- Kafka 실행을 위한 Java 환경  
  - Java 8 이상이 필요하며, 과정에서는 통일성을 위해 **Java 17** 사용  
  - JRE(Java Runtime Environment)보다는 **JDK 설치** 추천  
  - 아래 페이지에서 최신 버전 Java 다운로드 가능  
    - https://www.oracle.com/java/technologies/downloads/?er=221886

## Java 설치 -2 (Linux 패키지를 통한 설치)  
- Kafka 실행을 위한 Java 환경  
  - Linux 환경에서 실행 필요  
  - Windows의 경우 WSL을 이용해서 실행 가능  

1. 패키지 업데이트:  
   `sudo apt update`  
2. 자바 JDK 설치 (8 이상):  
   `sudo apt install openjdk-17-jdk`  
   - 중간에 물어보면 **Y 입력 후 엔터**  
3. 아래와 유사하게 출력되면 설치 완료

## Java 설치 확인  
- Kafka 실행을 위한 Java 환경  
- Java 설치 후 `java -version`을 입력하였을 때 정상적으로 출력되면 설치 성공  
- 다음과 같이 출력되면 정상: `java -version`

## Kafka 브로커 설치  
- Kafka 브로커란?  
  - 브로커(Broker): 메시지를 저장하고 제공하는 Kafka 서버  
  - 단일 Kafka 인스턴스를 브로커라고 부름  
  - 다수의 브로커가 모이면 Kafka 클러스터 형성

## Kafka 설치 방법  
- Kafka 다운로드  
  1. 아래 홈페이지에 접속하여 다운로드 후 압축 해제  
     - https://kafka.apache.org/downloads

## Kafka 설치 방법  
- Kafka 다운로드  
  1. 터미널에 아래 명령어를 입력하여 다운로드  
     `wget https://dlcdn.apache.org/kafka/3.9.0/kafka_2.12-3.9.0.tgz`  
  2. 왼쪽과 같은 내용이 출력되면 다운로드 성공  
  3. `ls` 명령어를 실행했을 때 압축이 풀린 폴더가 생성되면 성공

## Kafka 설치 방법  
- Kafka 다운로드  
  2. 관리의 편의를 위해 다운로드한 Kafka 폴더를 `/home/ssafy` 로 이동시키기  
     `sudo mv kafka_2.12-3.9.0 /home/ssafy/kafka`  
  - `/usr/local` 에 kafka 폴더가 생성되면 성공

## Zookeeper 실행하기  
- Zookeeper의 역할  
  - Kafka 클러스터의 메타데이터 관리  
  - 브로커 간 리더 선출 및 상태 유지  
  - 소비자(Consumer) 그룹 정보 저장

## Zookeeper 실행하기  
- Zookeeper 실행하기  
  1. Kafka 폴더로 이동하기  
     `cd /home/ssafy/kafka`  
  2. Zookeeper 실행  
     `./bin/zookeeper-server-start.sh config/zookeeper.properties`  
  - 왼쪽과 같은 내용이 출력되면 성공

## Kafka 실행하기  
- Kafka 브로커 실행하기  
  1. 별도의 터미널 띄우기  
  2. Kafka 폴더로 이동하기  
     `cd /home/ssafy/kafka`  
  3. Kafka 브로커 실행하기  
     `./bin/kafka-server-start.sh config/server.properties`  
  - 왼쪽과 같은 내용이 출력되면 성공

## Kafka 테스트  
### | 토픽 생성 및 메시지 전송  

1. Kafka 폴더로 이동하기  
   `cd /home/ssafy/kafka`  

2. 토픽 생성  
   `./bin/kafka-topics.sh --create --topic lecture-test-topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1`  

3. 메시지 전송  
   `./bin/kafka-console-producer.sh --topic lecture-test-topic --bootstrap-server localhost:9092`  
   `ssafy@6PC120:~/kafka$ ./bin/kafka-console-producer.sh --topic lecture-test-topic --bootstrap-server localhost:9092`  

4. 메시지 수신  
   `./bin/kafka-console-consumer.sh --topic lecture-test-topic --from-beginning --bootstrap-server localhost:9092`
