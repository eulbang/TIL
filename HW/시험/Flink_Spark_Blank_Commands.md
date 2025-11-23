# Flink/Spark 빈칸 명령어 모음
빈칸으로 나왔던 “명령어/호출”만 골라 묶었습니다.

## 기본 기동 (Kafka/Zookeeper, Flink, Spark)
```bash
# Zookeeper 기동 (Kafka 포함 배포본 기준)
bin/zookeeper-server-start.sh config/zookeeper.properties

# Kafka 브로커 기동 (Zookeeper 먼저 기동 후)
bin/kafka-server-start.sh config/server.properties

# Flink 로컬 클러스터 기동
bin/start-cluster.sh   # JobManager + TaskManager 기동

# Spark 로컬/스탠드얼론 기동 예시
sbin/start-master.sh                  # 마스터
sbin/start-worker.sh spark://<host>:7077  # 워커 (마스터 URL에 맞게)
# 혹은 간단 실행: bin/spark-shell / bin/pyspark
```

## Flink
```python
# 실행 환경 생성 및 병렬도 설정
env = StreamExecutionEnvironment.get_execution_environment()  # 실행 환경 가져오기
env.set_parallelism(<값>)  # 병렬 작업 수 지정
env.from_collection(..., type_info=...)  # 파이썬 컬렉션을 스트림 소스로 변환
env.execute("<job name>")  # 플링크 잡 시작
```

```sql
-- Table API 배치 (filesystem 소스/싱크, CSV)
CREATE TABLE finance_source (...) WITH ('connector'='filesystem','path'='<csv>','format'='csv');
CREATE TABLE sector_summary (...) WITH ('connector'='filesystem','path'='<out>','format'='csv');
SELECT sector,
       SUM(price * CAST(volume AS DOUBLE)) AS total_value,
       AVG(price) AS avg_price,
       SUM(volume) AS total_volume,
       COUNT(*) AS trade_count
FROM finance_source
GROUP BY sector;
```

```python
# Kafka ↔ Flink Table
table_env.get_config().get_configuration().set_string("pipeline.jars", "file://<jar>")  # 커넥터 JAR 등록
# 소스: connector=kafka, topic=stock_trades, format=json, scan.startup.mode=earliest-offset
# 싱크: connector=upsert-kafka, topic=stock_stats, key/value=json, PRIMARY KEY(stock_code) NOT ENFORCED
stmt_set = table_env.create_statement_set()  # 여러 INSERT를 묶는 StatementSet
stmt_set.add_insert_sql("""
INSERT INTO kafka_sink
SELECT stock_code, stock_name, SUM(volume), AVG(price), CURRENT_TIMESTAMP
FROM kafka_source
GROUP BY stock_code, stock_name
""")
stmt_set.execute()  # 쿼리 제출
```

## Spark (RDD)
```python
spark = SparkSession.builder.appName("...").getOrCreate()
sc = spark.sparkContext

words.map(lambda w: len(w))  # 단어 길이 계산
words.filter(lambda w: len(w) >= 6)  # 6글자 이상 필터
numbers.filter(lambda x: x % 2 == 0)  # 짝수 필터
numbers.filter(lambda x: x % 2 != 0)  # 홀수 필터
sentences.map(lambda l: l.lower())  # 문장 소문자 변환
sentences.filter(lambda l: "is" in l.lower())  # 특정 단어 포함 필터

line_lengths = text_data.map(lambda line: len(line))  # 각 줄 길이
contains_data = text_data.filter(lambda l: "data" in l.lower())  # data 포함
contains_ai = text_data.filter(lambda l: "ai" in l.lower())  # ai 포함
starts_with_big = text_data.filter(lambda l: l.startswith("Big"))  # Big으로 시작
ends_with_future = text_data.filter(lambda l: l.endswith("future"))  # future로 끝남

default_partitions = numbers.getNumPartitions()  # 기본 파티션 수 확인
repartitioned_data = numbers.repartition(1)  # 파티션 1개로 재분배
numbers.foreach(lambda x: print(x))  # 각 요소 출력
repartitioned_data.foreach(lambda x: print(x))  # 재분배 후 출력

text_data.getNumPartitions()  # 텍스트 RDD 파티션 수
text_data.repartition(4)  # 파티션 4개로 재분배
```

### 샘플링/분할
```python
numbers_rdd.sample(False, 0.2)  # 비복원 20% 샘플
numbers_rdd.sample(True, 0.2)   # 복원 20% 샘플
numbers_rdd.takeSample(False, 5)  # 비복원 5개 추출
numbers_rdd.takeSample(True, 5)   # 복원 5개 추출
numbers_rdd.randomSplit([0.8, 0.2], seed=42)  # 가중치로 랜덤 분할
```

### 최적화 비교
```python
rdd.filter(lambda x: x % 2 == 0).map(lambda x: x * 2)  # 기본 filter+map
rdd.flatMap(lambda x: [x * 2] if x % 2 == 0 else [])   # flatMap으로 동일 처리
rdd.mapPartitions(lambda it: (x * 2 for x in it if x % 2 == 0))  # 파티션 단위 처리
```

## Spark (SQL)
```python
df.createOrReplaceTempView("employee")  # 테이블 뷰 등록
spark.sql("""
    SELECT Department, COUNT(*) AS Employee_Count, AVG(Salary) AS Avg_Salary
    FROM employee
    GROUP BY Department
""")
```

```sql
SELECT e.EmpID, e.Name, e.Department, s.Salary
FROM employee e
INNER | LEFT | RIGHT | FULL OUTER JOIN salary s
ON e.EmpID = s.EmpID;  -- 조인 유형만 바꿔 사용
```

## Spark (Structured Streaming + Kafka)
```python
df = (spark.readStream.format("kafka")
      .option("kafka.bootstrap.servers", "localhost:9092")  # 카프카 주소
      .option("subscribe", "click-events")  # 구독 토픽
      .option("startingOffsets", "latest")  # 최신 오프셋부터
      .load())  # 스트림 로드

value_df = df.selectExpr("CAST(value AS STRING)")  # binary value → 문자열
parsed_df = (value_df.select(from_json(col("value"), schema).alias("data"))
             .select("data.*"))  # JSON 파싱 후 필드 펼치기

result_df = (parsed_df
             .withWatermark("timestamp", "2 minutes")  # 지연 허용
             .groupBy(window("timestamp", "1 minute"), col("event_type"))  # 윈도우 집계
             .agg(count("*").alias("event_count"),
                  countDistinct("user_id").alias("unique_users")))  # 건수/고유 사용자 집계

query = (result_df.writeStream
         .outputMode("complete")  # 전체 결과 출력
         .format("console")  # 콘솔 싱크
         .option("truncate", "false")  # 데이터 자르지 않음
         .start())  # 스트리밍 시작
query.awaitTermination()  # 종료까지 대기
```
