# Spark DataFrame과 Spark SQL

## 챕터의 포인트
- DataFrame과 Spark SQL
- DSL과 SQL을 활용한 데이터 처리
- Sqprk Streaming

# DataFrame과 Spark SQL

# RDD와 Spark SQL · DataFrame

## RDD란?
- Resilient Distributed Dataset
  - 데이터를 병렬 처리하는 핵심적인 역할을 수행하여 빠르고 안정적으로 동작하는 프로그램을 작성 가능
- but  
  - 데이터 값 자체는 표현이 가능하지만,  
  - 데이터에 대한 메타 데이터, ‘스키마’에 대해 명시적 표현 방법이 없음

# SparkSQL, DataFrame, Dataset

## RDD API의 문제점
- 스파크가 RDD API 기반의 연산, 표현식을 검사하지 못해 최적화할 방법이 없음
  - RDD API 기반 코드에서 어떤 일이 일어나는지 스파크는 알 수 없음
  - Join, filter, group by 등 여러 연산을 하더라도 스파크에서는 람다 표현식으로만 보임
  - 특히 PySpark의 경우, 연산 함수 Iterator 데이터 타입을 제대로 인식하지 못함  
    - 스파크에서는 단지 파이썬 기본 객체로만 인식

- 스파크는 어떠한 데이터 압축 테크닉도 적용하지 못함
  - 객체 안에서 어떤 타입의 컬럼에 접근하더라도 스파크는 알 수 없음
  - 결국 바이트 뭉치로 직렬화해 사용할 수밖에 없음

- → 스파크가 연산 순서를 재정렬하여 효율적인 질의 계획으로 바꿀 수 없음

# Spark SQL과 DataFrame 소개

## DataFrame
- 스키마(schema)를 가진 분산 데이터 컬렉션
- 데이터를 행(row)과 열(column)로 구성된 표 형태로 관리
- 각 열은 명확한 데이터 타입과 메타 데이터(schema)를 가지고 있음
- Spark SQL이 제공하는 구조화된 데이터 모델로서 RDD의 한계를 보완

# DataFrame API

## DataFrame API - 개요
- 구조, 포맷 등 몇몇 특정 연산 등에 있어 Pandas의 DataFrame에 영향을 많이 받음
- 이름 있는 컬럼과 스키마를 가진 분산 인메모리 테이블처럼 동작
- Spark DataFrame은 하나의 표 형태로 보임

## DataFrame API - 데이터 타입
- 기본 타입
  - Byte, Short, Integer, Long, Float, Double, String, Boolean, Decimal

- 정형화 타입
  - Binary, Timestamp, Date, Array, Map, Struct, StructField

- 실제 데이터를 위한 스키마를 정의할 때 이런 타입이 어떻게 연계되는지 이해하는 것이 중요함

- 예시 코드(원문 그대로):
  ```
  from pyspark.sql.types import StructType, StructField, StringType, ArrayType, IntegerType
  
  schema = StructType([
      StructField("name", StringType(), True),
      StructField("scores", ArrayType(IntegerType()), True)
  ])
  ```

## DataFrame API - 스키마(Schema)
- 스파크에서의 스키마는 Dataframe을 위해 컬럼 이름과 연관된 데이터 타입을 정의한 것
- 외부 데이터 소스에서 구조화된 데이터를 읽어 들일 때 사용

- 읽을 때 스키마를 가져오는 방식과 달리, 미리 스키마를 정의하는 것은 여러 장점 존재
  - 스파크가 데이터 타입을 추측해야 되는 책임을 덜어줌
  - 스파크가 스키마를 확정하기 위해 파일의 많은 부분을 읽어 들이려 별도의 Job을 만드는 것을 방지
  - 데이터가 스키마와 맞지 않는 경우, 조기에 문제 발견 가능

# Spark SQL과 DataFrame 구조

## DataFrame의 구성
- DataFrame = RDD + schema + DSL
- Named columns with types
- Domain-Specific Language(DSL)

## DataFrame 쿼리 방식
- DataFrame은 DSL 방식과 SQL 방식 모두 지원

### DSL 수행 예시 (코드블록)
```python
# 필터링
sciDocs = data.filter(col("label") == 1)

# 결과 출력
sciDocs.show()
```

### SQL 수행 예시 (코드블록)
```python
# SQL 필터링
data_scaled = spark.sql("SELECT * FROM data WHERE label = 1")

# 결과 출력
data_scaled.show()
```

## RDD와 DataFrame의 차이점은 무엇인가?

| 구분 | RDD | DataFrame |
|------|------|------------|
| 데이터 표현 방식 | 값만 표현 가능, 스키마 표현 불가능 | 명확한 스키마(컬럼, 데이터 타입)를 가진 구조적 데이터 |
| 최적화 및 성능 | 최적화 어려움, 직접적 연산 필요 | Catalyst Optimizer 통한 자동 최적화 및 빠른 처리 |
| 사용 편의성 | 낮음(저수준 API) | 높음(고수준 API, SQL 활용 가능) |

- 결론  
  - DataFrame을 사용하면 데이터를 더 효율적이고 편리하게 처리 가능  
  - 메타 정보를 활용하여 더 빠르고 최적화된 분석 수행 가능

## RDD를 사용하는 경우
1. 저수준의 Transformation과 Action을 직접 제어해야 할 때  
2. 스트림 데이터(미디어나 텍스트 스트림)가 구조화되지 않은 경우  
3. 특정 도메인 표현을 위해 함수형 프로그래밍이 필요할 때  
4. 스키마 변환이 필요 없을 때  
   - 예: 열 기반 저장소를 사용하지 않는 경우  
5. DataFrame이나 Dataset에서 처리할 수 없는 성능 최적화가 필요할 때

## DataFrame를 사용하는 경우
1. 고수준의 추상화와 도메인 기반 API가 필요할 때  
2. 고수준의 표현(filter, map, agg, avg, sum SQL, columnar access) 등 복잡한 연산이 필요하거나  
   반구조적 데이터에 대한 lambda 식이 필요할 때  
3. 타입 안정성과 최적화를 위해 컴파일 시 타입 안전성을 보장하고,  
4. Catalyst 최적화 및 Tungsten의 효율적인 코드 제너레이션이 필요할 때  
5. Spark API의 일관성과 간결함을 원할 때  

## SparkSQL이란?
- Spark SQL은 구조화된 데이터를 SQL처럼 처리할 수 있도록 해주는 스파크 모듈  
- 내부적으로는 DataFrame/Dataset API와 동일한 엔진(Catalyst)을 사용하여 처리  
- DataFrame과 Dataset을 SQL처럼 다룰 수 있게 해주는 분산 SQL 쿼리 엔진  
- Spark SQL은 RDD보다 더 높은 수준의 추상화와 자동 최적화를 제공  

→ DataFrame이 중심이고, Spark SQL은 그것을 SQL 방식으로 접근하게 해주는 방법 중 하나

## SparkSQL의 역할
- SQL 같은 질의 수행  
- 스파크 컴포넌트들을 통합하고, Dataframe, Dataset가 java, scala, python, R 등 여러 프로그래밍 언어로  
  정형화 데이터 관련 작업을 단순화할 수 있도록 추상화  
- 정형화된 파일 포맷(JSON, CSV, txt, avro, parquet, orc 등)에서 스키마와 정형화 데이터를 읽고 쓰며,  
  데이터를 임시 테이블로 변환  
- 빠른 데이터 탐색을 할 수 있도록 대화형 스파크 SQL 셀을 제공  
- 표준 데이터베이스 JDBC/ODBC 커넥터를 통해, 외부의 도구들과 연결할 수 있는 중간 역할 제공  
- 최종 실행을 위해 최적화된 질의 계획과 JVM을 위한 최적화된 코드를 생성 

## Spark SQL

| UserID   | Name            | Age | Location   | Pet       |
|----------|-----------------|-----|------------|-----------|
| 28492942 | John Galt       | 32  | New York   | Sea Horse |
| 95829324 | Winston Smith   | 41  | Oceania    | Ant       |
| 92871761 | Tom Sawyer      | 17  | Mississippi| Raccoon   |
| 37584932 | Carlos Hinojosa | 33  | Orlando    | Cat       |
| 73648274 | Luis Rodriguez  | 34  | Orlando    | Dogs      |

## SparkSQL의 역할
- JDBC  
- Console  
- User Programs (Java, Scala, Python)  
  ↓  
- Spark SQL / DataFrame API  
  ↓  
- Catalyst Optimizer  
  ↓  
- Spark  
  ↓  
- Resilient Distributed Datasets  

## Spark SQL의 내부 동작
- SQL 쿼리를 실행하는 역할  
  +  
  사용자가 입력한 쿼리나 DataFrame의 명령을 가장 빠르고 효율적인 방식으로 처리
- Spark SQL이 내부에서 데이터를 효율적으로 처리하는 핵심적인 엔진이 Catalyst Optimizer

## Spark SQL의 내부는 어떻게 작동할까?
### Catalyst Optimizer의 최적화 과정
1. SQL Parser & DataFrame API 해석 단계  
2. Logical Plan (논리적 계획) 생성  
3. Optimized Logical Plan (최적화된 논리 계획) 생성  
4. Physical Plan (물리적 실행 계획) 생성  

-> Catalyst Optimizer가 내부적으로 복잡한 최적화 과정을 자동으로 처리

## Spark SQL과 DataFrame API의 관계
- Spark SQL과 DataFrame API는 서로 완전히 독립된 별개의 것이 아님  
- 동일한 최적화 엔진(Catalyst Optimizer)을 공유하고, 내부적으로 통합된 구조를 가짐  

=> Spark에서는 DataFrame API를 이용해 작성된 데이터 처리 명령을 내부적으로 Spark SQL의 엔진으로 최적화해 실행

# Dataset API

## Dataset API
- 스파크 2.0에서, 개발자들이 한 종류의 API만 알면 되도록, Dataframe, Dataset API를 하나로 합침.  
- Dataset은 정적 타입(typed) API와 동적 타입(untyped) API의 두 특성을 모두 가짐.  
- Java, Scala(타입 안전을 보장하는 언어)에서만 사용이 가능하고,  
  Python, R(타입 안전을 보장하지 않는 언어)에서는 사용이 불가능, DataFrame API만 사용 가능.

# SparkSQL, Dataframe, Dataset 이란?

## DataFrame vs Dataset
- 가장 큰 차이점은 오류가 발견되는 시점

| 구분 | SQL | DataFrames | Datasets |
|------|------|-------------|-----------|
| Syntax Errors | Runtime | Compile Time | Compile Time |
| Analysis Errors | Runtime | Runtime | Compile Time |

# DataFrame과 Spark SQL

## View 등록 및 SQL 실행

```python
# DataFrame을 뷰로 등록하기
df.createTempView("viewName")
df.createGlobalTempView("viewName")
df.createOrReplaceTempView("viewName")

# 뷰에 SQL 쿼리 실행하기
spark.sql("SELECT * FROM viewName ").show()
spark.sql("SELECT * FROM global_temp.viewName").show()
```

## DataFrame 구조 변환

```python
# DataFrame → RDD (분산 처리용 RDD로 변환)
rdd1 = df.rdd

# DataFrame → JSON 문자열 → 첫 번째 항목 확인
df.toJSON().first()

# DataFrame → Pandas DataFrame
pandas_df = df.toPandas()
print(pandas_df)
```

# DSL과 SQL을 활용한 데이터 처리

## SQL쿼리 기본 문법
- 데이터 조회 : SELECT, WHERE  
- 정렬 : ORDER BY  
- 중복 제거 : DISTINCT  
- 데이터 집계 : GROUP BY, HAVING, 집계 함수(COUNT, AVG, SUM)  
- 데이터 결합 : JOIN  

## Creating DataFrames(DSL 코드)

```python
# SparkSession 생성
spark = SparkSession.builder.appName("ExampleApp").getOrCreate()

# 스키마 정의
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# 데이터 전처리 및 DataFrame 생성
parts = spark.sparkContext.parallelize([("Mine", "28"), ("Filip", "29"), ("Jonathan", "30")])
people = parts.map(lambda p: Row(name=p[0], age=int(p[1].strip())))
df = spark.createDataFrame(people, schema)

# 결과 출력
df.show()
```

## Creating DataFrames(SQL 코드)

```python
# DataFrame을 SQL에서 사용할 수 있도록 TempView 등록
df.createOrReplaceTempView("people")

# Spark SQL을 이용한 동일 조회
result = spark.sql("""
    SELECT name, age
    FROM people
""")

result.show()
```

## Creating DataFrames From File(DSL 코드)

```python
# DataFrame을 직접 생성
people_df = spark.read.option("header", "false") \
    .option("inferSchema", "true") \
    .csv("people.txt") \
    .toDF("name", "age")

# 결과 출력
peopledf.show()
```

## Creating DataFrames From File(SQL 코드)

```python
# DataFrame을 직접 생성
people_df = spark.read.option("header", "false") \
    .option("inferSchema", "true") \
    .csv("people.txt") \
    .toDF("name", "age")

# TempView 등록
people_df.createOrReplaceTempView("people")

# SQL 쿼리로 조회
result = spark.sql("""SELECT name, age FROM people""")

# 출력 확인
result.show()
```

## From Spark Data Sources

```python
# JSON
df = spark.read.json(filename.json)
df = spark.read.load("filename.json", format="json")

# Parquet files
df = spark.read.load("filename.parquet")

# TXT files
df = spark.read.txt("filename.txt")
```

## From Spark Data Sources

```python
# 열 이름과 데이터 유형 반환
df.dtypes

# 내용 표시
df.show()

# 처음 n개의 행 반환
df.head()

# 첫 번째 행 반환
df.first()
```

## Inspect Data

```python
# 처음 n개의 행 반환
df.take(n)

# DataFrame의 스키마 반환
df.schema

# 요약 통계 계산
df.describe().show()

# 열 이름 반환
df.columns
```

## Inspect Data

```python
# 행 개수 계산
df.count()

# 고유 행 개수 계산
df.distinct().count()

# 스키마 출력
df.printSchema()

# (논리 및 물리적) 실행 계획 출력
df.explain()
```

## Duplicate Values

```python
# 중복 행 제거
df = df.dropDuplicates()
```






38~



