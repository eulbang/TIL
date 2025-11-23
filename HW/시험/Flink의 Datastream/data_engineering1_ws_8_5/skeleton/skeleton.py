"""
목표
| 학습목표
-      PyFlink에서 Kafka 소스 및 싱크 테이블을 SQL로 정의할 수 있다.-      주식 코드와 이름을 기준으로 거래량과 가격을 집계하는 SQL 쿼리를 작성할 수 있다.-      StatementSet을 사용하여 SQL 쿼리를 실행할 수 있다.-      Kafka 커넥터를 통한 PyFlink 스트리밍 처리 전체 흐름을 이해하고 구현할 수 있다. | 학습 개념  PyFlink는 Apache Flink의 스트리밍/배치 처리 기능을 Python에서 사용할 수 있도록 해주는 인터페이스이다.Kafka 커넥터를 활용하여 실시간 데이터를 수신하고, 집계 후 Kafka 토픽으로 결과를 다시 전송할 수 있다.StatementSet은 여러 SQL 문을 하나의 실행 단위로 구성하여 효율적으로 실행하는 기능이다.  
문제
| 학습 방향  데이터 엔지니어링 팀 소속인 김싸피는 실시간 주식 거래 데이터를 수집하여 집계 통계를 Kafka 토픽으로 전송하는 분석 시스템을 PyFlink로 구축하고자 한다. 본 실습에서는 Kafka 소스/싱크 테이블을 정의하고, 주식 코드 및 이름을 기준으로 거래량과 평균 가격을 집계한 뒤, 해당 결과를 Kafka 싱크 테이블로 전송하는 전 과정을 구현한다. 학습자는 실시간 데이터 파이프라인의 전체 흐름을 익히고, PyFlink SQL을 실무에 적용할 수 있는 능력을 기르게 된다. 사용된 주요 개념	- StreamExecutionEnvironment: Flink 스트리밍 실행 환경 구성	- EnvironmentSettings.in_streaming_mode(): SQL 실행을 위한 스트리밍 모드 설정	- StreamTableEnvironment.create(): PyFlink SQL 테이블 환경 생성	- CREATE TABLE: Kafka와 연결된 소스 및 싱크 테이블 정의	- StatementSet: 다중 SQL 쿼리 실행 객체   
요구사항
1. StreamExecutionEnvironment 객체 생성○ PyFlink의 StreamExecutionEnvironment.get_execution_environment() 메서드를 사용하여 스트리밍 실행 환경을 생성하세요. 2. 스트리밍 모드 환경 설정 구성○ EnvironmentSettings.new_instance().in_streaming_mode().build()를 사용하여 Flink SQL의 스트리밍 실행 모드를 설정하세요. 3. StreamTableEnvironment 생성○ StreamTableEnvironment.create()를 사용하여 Flink SQL 실행 환경 객체를 생성하세요. 4. Kafka 소스 테이블 정의○ table_env.execute_sql()을 사용하여 Kafka 소스 테이블을 정의하세요.○ 'connector' = 'kafka', 'format' = 'json'과 같은 속성을 포함해야 합니다. 5. Kafka 싱크 테이블 정의○ table_env.execute_sql()을 사용하여 Kafka 싱크 테이블을 정의하세요.○ 'connector' = 'upsert-kafka', 'key.format' = 'json', 'value.format' = 'json'을 포함하세요. 6. StatementSet 객체 생성 및 SQL 쿼리 추가○ table_env.create_statement_set()을 사용하여 StatementSet 객체를 생성하세요.○ stmt_set.add_insert_sql()을 통해 집계 쿼리를 추가하세요.○ SQL 쿼리에는 SUM(volume)과 AVG(price)를 포함하여 주식 코드와 이름으로 그룹화해야 합니다.
"""

from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings
import os
import logging
import time
# TODO: 해당 코드를 실행하기 전에 kafka_producer.py를 먼저 실행해주세요.

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Flink 작업 시작...")
    
    # [1] 실행 환경 구성
    env = StreamExecutionEnvironment.get_execution_environment()
    settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
    table_env = StreamTableEnvironment.create(env, environment_settings=settings)

    # [2] Kafka 커넥터 JAR 경로 설정
    kafka_jar = os.path.join(os.path.abspath('.'), 'flink-sql-connector-kafka-3.3.0-1.19.jar')
    logger.info(f"사용하는 JAR 파일 경로: {kafka_jar}")
    if not os.path.exists(kafka_jar):
        logger.error(f"JAR 파일이 존재하지 않습니다: {kafka_jar}")
        return
        
    table_env.get_config().get_configuration().set_string("pipeline.jars", f"file://{kafka_jar}")

    # [3] Kafka 소스 테이블 생성
    try:
        logger.info("Kafka 소스 테이블 생성 시도...")
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
        logger.info("Kafka 소스 테이블 생성 성공")
    except Exception as e:
        logger.error(f"소스 테이블 생성 중 오류 발생: {e}")
        return

    # [4] Kafka 싱크 테이블 생성
    try:
        logger.info("Kafka 싱크 테이블 생성 시도...")
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
        logger.info("Kafka 싱크 테이블 생성 성공")
    except Exception as e:
        logger.error(f"싱크 테이블 생성 중 오류 발생: {e}")
        return

    # [5] SQL 쿼리 작성 및 실행
    try:
        logger.info("SQL 쿼리 실행 시도...")
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
            job_id = job_client.get_job_id()
            logger.info(f"작업이 성공적으로 제출되었습니다. 작업 ID: {job_id}")
            monitor_job(job_client)
        else:
            logger.error("작업 클라이언트를 가져올 수 없습니다.")
    except Exception as e:
        logger.error(f"작업 실행 중 오류 발생: {e}")

def monitor_job(job_client):
    """작업 상태를 모니터링하고 로그를 출력합니다."""
    try:
        job_status = job_client.get_job_status().result()
        logger.info(f"현재 작업 상태: {job_status}")
        
        logger.info("Kafka 토픽에 샘플 데이터가 있는지 확인해주세요.")
        logger.info("샘플 데이터가 없다면 kafka_producer.py를 실행하여 테스트 데이터를 생성하세요.")
        
        print("\n작업 모니터링 시작 (10초마다 상태 확인, Ctrl+C로 종료)")
        for i in range(6):
            time.sleep(10)
            try:
                current_status = job_client.get_job_status().result()
                print(f"[{i+1}/6] 현재 작업 상태: {current_status}")
            except Exception as e:
                print(f"상태 확인 중 오류 발생: {e}")
        
        print("\n모니터링 완료. 작업은 계속 실행 중입니다.")
        print("결과를 확인하려면 다음 명령어를 실행하세요:")
        print("/home/ssafy/kafka/bin/kafka-console-consumer.sh --topic stock_stats --bootstrap-server localhost:9092 --from-beginning")
        
    except Exception as e:
        logger.error(f"작업 모니터링 중 오류 발생: {e}")

if __name__ == '__main__':
    main()