📌 Flink의 Datastream 실습/과제 정리
---
- [WS 8-1: FileSink 기본](#ws-8-1-filesink-기본)
- [WS 8-2: FlatMap+Filter 키워드 집계](#ws-8-2-flatmapfilter-키워드-집계)
- [WS 8-3: 티커별 평균 금액](#ws-8-3-티커별-평균-금액)
- [WS 8-4: 금액 분할·반복 변환](#ws-8-4-금액-분할반복-변환)
- [WS 8-5: Kafka 소스/싱크 SQL](#ws-8-5-kafka-소스싱크-sql)
- [HW 8-2: 거래 유형별 합계](#hw-8-2-거래-유형별-합계)
- [HW 8-4: 섹터별 집계(Table)](#hw-8-4-섹터별-집계table)

## WS 8-1: FileSink 기본
- 목표: 컬렉션 스트림 → FileSink로 저장.
- 정답 코드: `data_engineering1_ws_8_1/skeleton/skeleton.py`
```python
import os
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FileSink
from pyflink.common.serialization import Encoder
from pyflink.common.typeinfo import Types
from pyflink.java_gateway import get_gateway

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    data_stream = env.from_collection(["Hello", "Flink", "World"], type_info=Types.STRING())

    gateway = get_gateway()
    j_string_encoder = gateway.jvm.org.apache.flink.api.common.serialization.SimpleStringEncoder()
    encoder = Encoder(j_string_encoder)

    output_dir = "./output/result"
    os.makedirs(output_dir, exist_ok=True)
    file_sink = FileSink.for_row_format(output_dir, encoder).build()

    data_stream.sink_to(file_sink)
    env.execute("File Sink Example")

if __name__ == "__main__":
    main()
```

## WS 8-2: FlatMap+Filter 키워드 집계
- 목표: 뉴스 텍스트 → 단어 분해 → 금융 키워드 필터 → key_by/sum 집계.
- 정답 코드: `data_engineering1_ws_8_2/skeleton/skeleton.py`
```python
import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(2)

    df = pd.read_csv("../data/data.csv")
    news_texts = df["news_text"].dropna().tolist()
    text_stream = env.from_collection(news_texts, type_info=Types.STRING())

    finance_keywords = {"stock", "market", "investment", "economy"}
    processed_stream = (text_stream
                        .flat_map(lambda text: [(word.lower(), 1) for word in text.split()],
                                  output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
                        .filter(lambda x: x[0] in finance_keywords))

    aggregated_stream = processed_stream.key_by(lambda x: x[0]).sum(1)
    aggregated_stream.print()
    env.execute("FlatMap and Filter Example")

if __name__ == "__main__":
    main()
```

## WS 8-3: 티커별 평균 금액
- 목표: 거래(ticker, amount) → key_by/reduce 누적 → map으로 평균 금액 계산.
- 정답 코드: `data_engineering1_ws_8_3/skeleton/skeleton.py`
```python
import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    df = pd.read_csv("../data/data.csv")
    transactions = df[["stock_ticker", "amount"]].dropna().values.tolist()

    transaction_stream = env.from_collection(
        [(t[0], t[1], 1) for t in transactions],
        type_info=Types.TUPLE([Types.STRING(), Types.FLOAT(), Types.INT()])
    )

    total_amount_stream = (transaction_stream
                           .key_by(lambda x: x[0])
                           .reduce(lambda a, b: (a[0], a[1] + b[1], a[2] + b[2])))

    average_transaction_stream = total_amount_stream.map(
        lambda x: (x[0], x[1], x[1] / x[2] if x[2] > 0 else 0),
        output_type=Types.TUPLE([Types.STRING(), Types.FLOAT(), Types.FLOAT()])
    )

    average_transaction_stream.print()
    env.execute("Stock Ticker Total and Average Transaction Amount")

if __name__ == "__main__":
    main()
```

## WS 8-4: 금액 분할·반복 변환
- 목표: 금액 5000 기준 분할 → 낮은 금액 반복 10% 증액(iteration) → union 병합.
- 정답 코드: `data_engineering1_ws_8_4/skeleton/skeleton.py`
```python
import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def process_transactions(input_stream):
    max_iterations = 10
    iteration = 0
    while iteration < max_iterations:
        updated_stream = (input_stream
                          .map(lambda x: (x[0], x[1] * 1.1),
                               output_type=Types.TUPLE([Types.STRING(), Types.FLOAT()]))
                          .filter(lambda x: x[1] < 5000))
        if updated_stream is None or iteration == max_iterations - 1:
            break
        input_stream = updated_stream
        iteration += 1
    return input_stream

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    df = pd.read_csv("../data/data.csv")
    transactions = df[["stock_ticker", "amount"]].dropna().values.tolist()

    transaction_stream = env.from_collection(transactions,
                                             type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()]))

    high_value_stream = transaction_stream.filter(lambda x: x[1] >= 5000)
    low_value_stream = transaction_stream.filter(lambda x: x[1] < 5000)

    processed_stream = process_transactions(low_value_stream)
    final_stream = processed_stream.union(high_value_stream)

    final_stream.print()
    env.execute("Transaction Processing with Split & Iteration")

if __name__ == "__main__":
    main()
```

## WS 8-5: Kafka 소스/싱크 SQL
- 목표: Kafka 소스/업서트 싱크 테이블 정의 → 주식 코드/이름 기준 집계(SQL) → StatementSet 실행.
- 정답 코드: `data_engineering1_ws_8_5/skeleton/skeleton.py`
```python
import os, logging, time
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Flink 작업 시작...")
    env = StreamExecutionEnvironment.get_execution_environment()
    settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
    table_env = StreamTableEnvironment.create(env, environment_settings=settings)

    kafka_jar = os.path.join(os.path.abspath('.'), 'flink-sql-connector-kafka-3.3.0-1.19.jar')
    table_env.get_config().get_configuration().set_string("pipeline.jars", f"file://{kafka_jar}")

    table_env.execute_sql("""
    CREATE TABLE kafka_source (
        stock_code STRING,
        stock_name STRING,
        trade_type STRING,
        price DECIMAL(10,2),
        volume BIGINT,
        trade_time TIMESTAMP(3),
        proctime AS PROCTIME()
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'stock_trades',
        'properties.bootstrap.servers' = 'localhost:9092',
        'properties.group.id' = 'flink-consumer-group',
        'scan.startup.mode' = 'earliest-offset',
        'format' = 'json',
        'json.fail-on-missing-field' = 'false',
        'json.ignore-parse-errors' = 'true'
    )
    """)

    table_env.execute_sql("""
    CREATE TABLE kafka_sink (
        stock_code STRING,
        stock_name STRING,
        total_volume BIGINT,
        avg_price DECIMAL(10,2),
        update_time TIMESTAMP(3),
        PRIMARY KEY (stock_code) NOT ENFORCED
    ) WITH (
        'connector' = 'upsert-kafka',
        'topic' = 'stock_stats',
        'properties.bootstrap.servers' = 'localhost:9092',
        'key.format' = 'json',
        'value.format' = 'json',
        'properties.group.id' = 'flink-sink-group'
    )
    """)

    stmt_set = table_env.create_statement_set()
    stmt_set.add_insert_sql("""
    INSERT INTO kafka_sink
    SELECT 
        stock_code,
        stock_name,
        SUM(volume) AS total_volume,
        AVG(price) AS avg_price,
        CURRENT_TIMESTAMP as update_time
    FROM kafka_source
    GROUP BY stock_code, stock_name
    """)

    job_client = stmt_set.execute().get_job_client()
    if job_client:
        job_client.get_job_status().result()

if __name__ == '__main__':
    main()
```

## HW 8-2: 거래 유형별 합계
- 목표: 거래 유형별 금액 합산(key_by + sum).
- 정답 코드: `data_engineering1_hw_8_2/skeleton/skeleton.py`
```python
import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    env = StreamExecutionEnvironment.get_execution_environment()

    df = pd.read_csv("../data/data.csv")
    transactions = df[["transaction_type", "amount"]].dropna().values.tolist()

    transaction_stream = env.from_collection(transactions,
                                             type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()]))

    total_amount_per_type = (transaction_stream
                             .key_by(lambda x: x[0])
                             .sum(1))

    total_amount_per_type.print()
    env.execute("Streaming Transaction Processing")

if __name__ == "__main__":
    main()
```

## HW 8-4: 섹터별 집계(Table)
- 목표: TableEnvironment에서 CSV 소스/싱크 등록 → sector 기준 집계 후 출력/저장.
- 정답 코드: `data_engineering1_hw_8_4/skeleton/skeleton.py`
```python
import os, tempfile, logging, pandas as pd, numpy as np
from pyflink.table import EnvironmentSettings, TableEnvironment

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Flink 배치 처리 시작")
    env_settings = EnvironmentSettings.in_batch_mode()
    table_env = TableEnvironment.create(env_settings)
    table_env.get_config().get_configuration().set_string("parallelism.default", "1")

    input_path = create_sample_csv()
    output_dir = tempfile.gettempdir() + '/flink_finance_output'
    if os.path.exists(output_dir):
        import shutil; shutil.rmtree(output_dir)

    source_ddl = f"""
    CREATE TABLE finance_source (
        stock_code STRING,
        sector STRING,
        price DOUBLE,
        volume BIGINT,
        trade_date STRING
    ) WITH (
        'connector' = 'filesystem',
        'path' = '{input_path}',
        'format' = 'csv'
    )"""
    table_env.execute_sql(source_ddl)

    sink_ddl = f"""
    CREATE TABLE sector_summary (
        sector STRING,
        total_value DOUBLE,
        avg_price DOUBLE,
        total_volume BIGINT,
        trade_count BIGINT
    ) WITH (
        'connector' = 'filesystem',
        'path' = '{output_dir}',
        'format' = 'csv'
    )"""
    table_env.execute_sql(sink_ddl)

    result = table_env.execute_sql("""
    SELECT
        sector,
        SUM(price * CAST(volume AS DOUBLE)) AS total_value,
        AVG(price) AS avg_price,
        SUM(volume) AS total_volume,
        COUNT(*) AS trade_count
    FROM finance_source
    GROUP BY sector""")

    with result.collect() as results:
        for row in results:
            print(f"{row[0]}\t{row[1]:,.2f}\t{row[2]:,.2f}\t{row[3]:,}\t{row[4]:,}")

def create_sample_csv():
    temp_file = tempfile.gettempdir() + '/finance_data.csv'
    import numpy as np
    np.random.seed(42)
    stock_codes = ['005930', '000660', '035420', '068270']
    sectors = ['semiconductor', 'biotech', 'internet']
    data = []
    for _ in range(1000):
        stock_code = np.random.choice(stock_codes)
        sector = np.random.choice(sectors)
        price = round(np.random.uniform(50000, 1000000), 2)
        volume = np.random.randint(10, 1000)
        date = f"2025-{np.random.randint(1, 13):02d}-{np.random.randint(1, 29):02d}"
        data.append(f"{stock_code},{sector},{price},{volume},{date}")
    with open(temp_file, 'w') as f:
        f.write('\n'.join(data))
    return temp_file

if __name__ == '__main__':
    main()
```
