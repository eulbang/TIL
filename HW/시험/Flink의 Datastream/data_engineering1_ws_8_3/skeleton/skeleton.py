"""
목표
| 학습목표
-      key_by()와 reduce() 연산을 통해 각 금융 상품(주식 티커)별 거래 금액 및 거래 횟수를 누적 집계하는 방법을 학습한다.-      map() 연산을 통해 누적 결과로부터 평균 거래 금액을 계산하는 방법을 실습한다.   | 학습 개념  PyFlink는 Python 환경에서 Apache Flink의 스트리밍 데이터 처리 기능을 활용할 수 있는 API이다. 본 실습에서는 금융 거래 CSV 데이터를 Pandas로 불러와 결측값을 제거한 후, 리스트로 변환하여 PyFlink의 from_collection()메서드로 데이터 스트림을 생성한다. 이후, key_by 연산으로 데이터를 상품별(주식 티커)로 그룹화하고, reduce 연산으로 거래 금액과 거래 횟수를 누적 집계한 후, map 연산을 통해 평균 거래 금액을 계산하는 전체 변환 과정을 다룬다.   
문제
| 학습 방향  김싸피가 수행 중인 실시간 금융 거래 데이터 분석은 고객의 거래 패턴 및 금융 서비스 개선을 위한 중요한 인사이트를 제공한다. 본 실습에서는 CSV 파일에서 거래 데이터를 불러와 Pandas를 통해 전처리한 후, PyFlink를 사용하여 데이터를 스트림으로 전환한다. 이어서, key_by와 reduce 연산을 통해 각 상품별 거래 금액과 거래 횟수를 누적하고, map 연산을 통해 평균 거래 금액을 계산하는 파이프라인을 구성한다. 이를 통해, 실시간으로 집계 및 평균 계산 결과를 출력하는 기본적인 데이터 변환 및 집계 흐름을 이해한다.  사용된 주요 개념 - PyFlink의 key_by(): 데이터를 특정 키(상품 ID) 기준으로 그룹화하는 연산 - PyFlink의 reduce(): 그룹화된 데이터의 값을 누적 집계하는 연산 - PyFlink의 map(): 누적 결과를 원하는 형식(평균 계산)으로 가공하는 연산    
요구사항
1.   실행 환경 생성
2.   실행 환경을 생성하세요.
3.   CSV 데이터 불러오기 및 전처리
4.    Pandas를 사용하여 금융 거래 CSV 파일에서 데이터를 불러오고, "stock_ticker"와 "amount" 컬럼을 선택한 후 결측값을 제거하여 리스트로 변환하세요.
5.    각 거래마다 초기 거래 횟수 1을 추가하여 튜플 형태로 재구성하세요.
6.   데이터 스트림 생성
7.    PyFlink의 from_collection() 메서드를 사용하여 전처리된 리스트 데이터를 데이터 스트림으로 변환하세요.
8.    데이터 타입은 (문자열, 실수형, 정수형) 튜플로 지정하세요.
9.    거래 집계 파이프라인 구성
10.    key_by()를 사용하여 상품(주식 티커) 기준으로 데이터를 그룹화하세요.
12. reduce() 연산을 적용하여 동일한 상품별로 거래 금액과 거래 횟수를 누적 집계하세요.
13.   평균 거래 금액 계산
14. map() 연산을 사용하여 누적 결과로부터 평균 거래 금액(총 거래 금액 ÷ 거래 횟수)을 계산하세요.
15.   프로그램 실행
16. 최종 변환 결과(상품별 총 거래 금액 및 평균 거래 금액)를 실시간으로 출력하고, Flink 작업을 실행하세요.
"""

import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    # Flink 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경 가져오기
    
    # 병렬성 1로 설정
    env.set_parallelism(1)  

    # CSV 파일 로드
    df = pd.read_csv("../data/data.csv")  
    transactions = df[['stock_ticker', 'amount']].dropna().values.tolist()  # 주식 티커(상품)와 거래 금액 선택

    # 데이터 스트림 생성 (상품 ID, 거래 금액, 초기 거래 횟수(1) 추가)
    transaction_stream = env.from_collection(
        [(t[0], t[1], 1) for t in transactions],  # 거래 횟수(1) 추가
        type_info=Types.TUPLE([Types.STRING(), Types.FLOAT(), Types.INT()])
    )

    # Keyby Reduce 연산: 상품별 총 거래 금액 및 거래 횟수 누적
    total_amount_stream = (transaction_stream
                           .key_by(lambda x: x[0])  # 특정 키 기준 그룹화 함수
                           .reduce(lambda a, b: (a[0], a[1] + b[1], a[2] + b[2])))  # 거래 금액 및 횟수 누적 함수

    # 평균 거래 금액 계산 (map 연산)
    average_transaction_stream = total_amount_stream.map(
        lambda x: (x[0], x[1], x[1] / x[2] if x[2] > 0 else 0),  # 평균 계산을 위한 map 연산 적용
        output_type=Types.TUPLE([Types.STRING(), Types.FLOAT(), Types.FLOAT()])
    )

    # 결과 출력 (상품별 총 거래 금액 및 평균 거래 금액)
    average_transaction_stream.print()  # 데이터 출력

    # Flink 실행
    env.execute("Stock Ticker Total and Average Transaction Amount")  # Flink 실행

if __name__ == "__main__":
    main()
