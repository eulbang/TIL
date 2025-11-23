# Flink & Spark 빈칸 정리 모음
플링크/스파크 실습에서 빈칸으로 나왔던 **명령어** 중심으로, 주석·앞뒤 코드와 함께 코드블록으로 정리했습니다.

## Flink
### 공통 스트리밍 패턴
```python
from pyflink.datastream import StreamExecutionEnvironment
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(<값>)
stream = env.from_collection(data, type_info=...)
stream.연산들()
env.execute("<job name>")
```

### data_engineering1_hw_8_4/skeleton/skeleton.py (Table API 배치)
```sql
-- 소스 테이블
CREATE TABLE finance_source (...) WITH (
    'connector' = 'filesystem',
    'path' = '<샘플 CSV 경로>',
    'format' = 'csv'
);

-- 싱크 테이블
CREATE TABLE sector_summary (...) WITH (
    'connector' = 'filesystem',
    'path' = '<output temp dir>',
    'format' = 'csv'
);

-- 집계 SQL
SELECT
    sector,
    SUM(price * CAST(volume AS DOUBLE)) AS total_value,
    AVG(price) AS avg_price,
    SUM(volume) AS total_volume,
    COUNT(*) AS trade_count
FROM finance_source
GROUP BY sector;
```

### data_engineering1_ws_8_5/skeleton/skeleton.py (Kafka ↔ Flink Table)
```python
# Kafka 커넥터 JAR 등록
table_env.get_config().get_configuration().set_string(
    "pipeline.jars", "file://<jar 경로>"
)

# Kafka 소스 테이블: connector=kafka, topic=stock_trades, format=json, scan.startup.mode=earliest-offset
# Kafka 싱크 테이블: connector=upsert-kafka, topic=stock_stats, key/value json, PRIMARY KEY (stock_code) NOT ENFORCED

# 실행
stmt_set = table_env.create_statement_set()
stmt_set.add_insert_sql("""
INSERT INTO kafka_sink
SELECT stock_code, stock_name, SUM(volume), AVG(price), CURRENT_TIMESTAMP
FROM kafka_source
GROUP BY stock_code, stock_name
""")
stmt_set.execute()
```

## Spark (RDD)
공통: `spark = SparkSession.builder.appName("...").getOrCreate()` → `sc = spark.sparkContext`

### data_engineering1_ws_10_2/skeleton/skeleton.py
```python
word_lengths = words.map(lambda word: len(word))
long_words = words.filter(lambda word: len(word) >= 6)
even = numbers.filter(lambda x: x % 2 == 0)
odd = numbers.filter(lambda x: x % 2 != 0)
lower = sentences.map(lambda line: line.lower())
contains_is = sentences.filter(lambda line: "is" in line.lower())
```

### data_engineering1_ws_10_3/skeleton/skeleton.py
```python
line_lengths = text_data.map(lambda line: len(line))
```

### data_engineering1_ws_10_4/skeleton/skeleton.py
```python
contains_data = text_data.filter(lambda line: "data" in line.lower())
contains_ai = text_data.filter(lambda line: "ai" in line.lower())
starts_with_big = text_data.filter(lambda line: line.startswith("Big"))
ends_with_future = text_data.filter(lambda line: line.endswith("future"))
```

### data_engineering1_ws_10_5/skeleton/skeleton.py
```python
default_partitions = numbers.getNumPartitions()
repartitioned_data = numbers.repartition(1)
numbers.foreach(lambda x: print(x))
repartitioned_data.foreach(lambda x: print(x))
```

### data_engineering1_hw_10_4/skeleton/skeleton.py
```python
contains_data = text_data.filter(lambda line: "data" in line.lower())
upper_case_data = text_data.map(lambda line: line.upper())
lower_case_data = text_data.map(lambda line: line.lower())
text_data.getNumPartitions()
text_data.repartition(4)
```

### data_engineering2_hw_1_2/skeleton/skeleton.py (샘플링)
```python
numbers_rdd.sample(False, 0.2)
numbers_rdd.sample(True, 0.2)
numbers_rdd.takeSample(False, 5)
numbers_rdd.takeSample(True, 5)
numbers_rdd.randomSplit([0.8, 0.2], seed=42)
```

### data_engineering2_hw_1_4/skeleton/skeleton.py (최적화 비교)
```python
rdd.filter(lambda x: x % 2 == 0).map(lambda x: x * 2)
rdd.flatMap(lambda x: [x * 2] if x % 2 == 0 else [])
rdd.mapPartitions(lambda iter: (x * 2 for x in iter if x % 2 == 0))
```

## Spark (SQL)
### data_engineering2_ws_2_4/skeleton/skeleton.py
```python
df.createOrReplaceTempView("employee")
spark.sql("""
    SELECT Department,
           COUNT(*) AS Employee_Count,
           AVG(Salary) AS Avg_Salary
    FROM employee
    GROUP BY Department
""")
```

### data_engineering2_ws_2_5/skeleton/skeleton.py
```sql
SELECT e.EmpID, e.Name, e.Department, s.Salary
FROM employee e
<JOIN TYPE: INNER | LEFT | RIGHT | FULL OUTER> JOIN salary s
ON e.EmpID = s.EmpID;
```

## Spark (Structured Streaming + Kafka)
### data_engineering2_hw_2_4/skeleton/skeleton.py
```python
# 소스
df = (spark.readStream.format("kafka")
      .option("kafka.bootstrap.servers", "localhost:9092")
      .option("subscribe", "click-events")
      .option("startingOffsets", "latest")
      .load())

# value 파싱
value_df = df.selectExpr("CAST(value AS STRING)")
parsed_df = (value_df.select(from_json(col("value"), schema).alias("data"))
             .select("data.*"))

# 집계
result_df = (parsed_df
             .withWatermark("timestamp", "2 minutes")
             .groupBy(window("timestamp", "1 minute"), col("event_type"))
             .agg(
                 count("*").alias("event_count"),
                 countDistinct("user_id").alias("unique_users")
             ))

# 출력
query = (result_df.writeStream
         .outputMode("complete")
         .format("console")
         .option("truncate", "false")
         .start())
query.awaitTermination()
```
