"""
목표
| 학습목표
-      TableEnvironment를 설정하고 CSV 파일을 Flink 테이블로 연결할 수 있다.-      SQL을 사용하여 sector별 집계를 수행하고, 결과를 다른 파일로 출력할 수 있다.-      Flink SQL 쿼리 실행 결과를 Python 코드에서 수집하고 출력할 수 있다.   | 학습 개념  Flink의 TableEnvironment는 SQL 기반 데이터 처리를 가능하게 하는 핵심 객체이다.CSV 파일을 파일 시스템 커넥터와 함께 사용해 테이블로 등록하고, SQL 쿼리를 통해 집계 및 분석이 가능하다.execute_sql 결과를 collect()하여 결과를 순회하면서 처리할 수 있다.  
문제
| 학습 방향  김싸피는 금융 거래 데이터를 부문별로 집계하는 PyFlink 배치 처리 흐름을 구성하며, 테이블 생성부터 SQL 쿼리 작성 및 결과 출력까지의 과정을 직접 구현합니다. 이를 통해 TableEnvironment, 파일 시스템 커넥터(filesystem), SQL 집계 함수(SUM, AVG, COUNT), result.collect() 등의 핵심 개념을 실습하며 Flink 배치 처리의 주요 흐름을 학습합니다.이 실습은 금융 거래 데이터를 부문(sector)별로 집계하는 간단한 PyFlink 배치 처리 흐름을 구성하는 것을 목표로 한다.사용자는 테이블 생성, SQL 쿼리 작성 및 결과 출력 과정을 직접 구성하며, Flink 배치 처리의 핵심 흐름을 학습하게 된다.
사용된 주요 개념- TableEnvironment- 파일 시스템 커넥터 (filesystem)- SQL 집계 함수 (SUM, AVG, COUNT)- result.collect()    
요구사항
1. 소스 테이블 DDL을 작성하세요.	○ finance 테이블을 생성하고, 샘플 CSV 파일 경로(input_path)를 경로로 지정하세요.	○ stock_code, sector, price, volume, transaction_date 필드를 정의하고, 파일 형식은 csv로 설정하세요.	 2. 싱크 테이블 DDL을 작성하세요.	○ finance_summary 테이블을 생성하고, 출력 경로(output_dir)로 결과를 저장하도록 설정하세요.	○ sector, total_value, avg_price, total_volume, transaction_count 필드를 포함하세요. 3. sector별 집계 쿼리를 작성하세요.	○ finance 테이블에서 sector를 기준으로 총 거래액, 평균 가격, 총 거래량, 거래 건수를 집계하여 SELECT 하세요.
"""
from pyflink.table import EnvironmentSettings, TableEnvironment
import tempfile
import os
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Flink 배치 처리 시작")

    env_settings = EnvironmentSettings.in_batch_mode()
    table_env = TableEnvironment.create(env_settings)

    config = table_env.get_config().get_configuration()
    config.set_string("parallelism.default", "1")

    input_path = create_sample_csv()
    output_dir = tempfile.gettempdir() + '/flink_finance_output'

    if os.path.exists(output_dir):
        import shutil
        shutil.rmtree(output_dir)

    # 빈칸: 소스 테이블 정의
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

    # 빈칸: 싱크 테이블 정의
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

    # 빈칸: SQL 쿼리 작성 및 실행
    result = table_env.execute_sql("""
    SELECT
        sector,
        SUM(price * CAST(volume AS DOUBLE)) AS total_value,
        AVG(price) AS avg_price,
        SUM(volume) AS total_volume,
        COUNT(*) AS trade_count
    FROM finance_source
    GROUP BY sector""")

    print("\n=== 섹터별 금융 데이터 요약 ===")
    print("섹터\t총 거래액\t평균 가격\t총 거래량\t거래 건수")
    print("-" * 80)

    with result.collect() as results:
        for row in results:
            print(f"{row[0]}\t{row[1]:,.2f}\t{row[2]:,.2f}\t{row[3]:,}\t{row[4]:,}")

def create_sample_csv():
    temp_file = tempfile.gettempdir() + '/finance_data.csv'
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
