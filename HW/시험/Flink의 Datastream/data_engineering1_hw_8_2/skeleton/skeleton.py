"""
목표
| 학습목표
-      PyFlink의 from_collection() 메서드를 사용해 전처리된 데이터를 데이터 스트림으로 변환하는 방법을 실습한다.-      key_by()와 sum() 연산을 활용하여 거래 유형별 금액 집계 파이프라인을 구성하는 방법을 학습한다.   | 학습 개념  본 실습에서는 Pandas로 금융 거래 CSV 데이터를 불러와 전처리한 후, PyFlink의 from_collection() 메서드를 이용해 데이터 스트림을 생성하고, 거래 유형별로 데이터를 그룹화하여 금액을 합산하는 집계 파이프라인을 구현하는 과정을 다룬다.   
문제
| 학습 방향  금융 거래 데이터 분석팀의 김싸피는 고객의 거래 패턴을 파악하고 금융 서비스를 개선하는 데 중요한 역할을 한다. 본 실습에서는 CSV 파일에서 금융 거래 데이터를 불러와 Pandas를 통해 전처리한 후, PyFlink를 사용하여 데이터를 스트림으로 변환하고, key_by()와 sum()연산을 통해 거래 유형별 금액을 집계하는 파이프라인을 구성한다. 이를 통해 실시간으로 금융 데이터를 처리하는 기본적인 방법을 익힌다. 사용된 주요 개념 - PyFlink의 key_b():: 데이터를 그룹화하는 연산 - PyFlink의 sum(): 데이터를 집계하는 연산   
요구사항
1.    실행 환경 생성
2.    PyFlink 실행 환경을 생성하세요.
3.    CSV 데이터 불러오기 및 전처리
4.    Pandas를 사용하여 금융 거래 CSV 파일(financial_transactions.csv)에서 데이터를 불러오세요.
5.    transaction_type과 amount 컬럼을 선택하고, 결측값을 제거한 후 리스트로 변환하세요.
6.    데이터 스트림 생성
7.    PyFlink의 from_collection() 메서드를 사용하여 전처리된 데이터를 데이터 스트림으로 변환하세요.
8.    데이터 타입은 [문자열, 실수형] 튜플로 지정하세요.
9.    거래 유형별 금액 집계 파이프라인 구성
10. key_by()를 사용하여 거래 유형(예: x[0])을 기준으로 데이터를 그룹화하세요.
11. sum(1) 연산을 적용하여 각 거래 유형별 금액을 합산하세요.
12. 결과 출력 및 실행  13.   구성된 거래 유형별 금액 집계 결과를 출력하고, Flink 프로그램을 실행하세요
"""

import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    # Flink 스트리밍 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경을 가져오는 함수 호출

    # CSV 데이터 불러오기
    df = pd.read_csv("../data/data.csv")
    transactions = df[["transaction_type", "amount"]].dropna().values.tolist()  

    # 스트리밍 데이터 스트림 생성
    transaction_stream = env.from_collection(transactions, type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()]))  # 데이터 스트림을 생성하는 메서드(문자열, 실수로 이루어진 튜플 정의)

    # 거래 유형별 금액 합산 파이프라인 구성
    total_amount_per_type = (transaction_stream
                             .key_by(lambda x: x[0])  # 거래 유형(transaction_type, x[0]) 기준 그룹화
                             .sum(1))  # 합산할 컬럼 인덱스 입력

    # 결과 실시간 출력
    total_amount_per_type.print()

    # 실행
    env.execute("Streaming Transaction Processing")  # Flink 실행을 시작하는 메서드 호출

if __name__ == "__main__":
    main()
