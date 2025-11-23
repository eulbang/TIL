"""
목표
| 학습목표
-      Flink의 실행 환경을 설정하고 병렬성을 조정하는 방법을 학습한다.-      CSV 데이터를 Flink 데이터 스트림으로 변환하는 과정을 이해한다.-      거래 유형별 총 거래 금액을 계산하는 집계 연산을 수행하는 방법을 익힌다.   | 학습 개념  Flink는 실시간 데이터 처리를 위한 분산형 데이터 처리 프레임워크이다. 이를 활용하면 금융 거래 데이터를 스트리밍 데이터처럼 변환하고, 거래 유형별로 집계 연산을 수행할 수 있다. 본 실습에서는 Flink의 데이터 스트림 기능을 사용하여 각 거래 유형별 총 거래 금액을 계산하는 방법을 실습한다.  
문제
| 학습 방향  금융 데이터 분석 팀 소속인 김싸피는 고객의 거래 데이터를 분석하여 각 거래 유형별 총 거래 금액을 집계하고 있다.이 분석을 통해 거래 유형별 소비 패턴을 파악하고, 금융 서비스 개선을 위한 데이터를 수집한다. 거래 유형을 기준으로 데이터를 그룹화하고, 거래 금액을 합산하여 각 거래 유형의 총 거래 금액을 계산한다. 이를 통해 거래 패턴을 분석하고, 금융 기관이 고객 맞춤형 서비스를 제공할 수 있도록 돕는다. 데이터 설명 - transaction_type: 거래 유형(예: 입금, 출금, 구매 등) - amount: 거래 금액   
요구사항
1.    실행 환경 설정
2.    Flink 실행 환경을 생성하고 스트림 처리를 위한 설정을 수행하세요.
3.    병렬성을 2로 설정하세요.
4.    금융 거래 데이터 입력 및 전처리
5.    CSV 파일에서 데이터를 불러오고 거래 유형과 거래 금액이 포함된 컬럼을 선택하세요.
6.    결측값을 제거하고 데이터를 리스트 형태로 변환하세요.
7.    데이터 스트림 생성
8.    리스트 형태의 데이터를 Flink 데이터 스트림으로 변환하세요.
9.    데이터 타입을 [문자열, 실수형]으로 지정하세요.
10. 거래 유형별 총 거래 금액 계산
11. 거래 유형을 기준으로 데이터를 그룹화하세요.
12. 같은 거래 유형에 대해 거래 금액을 합산하여 총 거래 금액을 계산하세요.
13. 결과 출력 및 실행
14. 거래 유형별 총 거래 금액을 출력하세요.
15. 프로그램을 실행하여 집계 결과를 확인하세요.
"""


import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    # 환경 생성 Flink의 실행 환경을 설정하세요.
    env = StreamExecutionEnvironment.get_execution_environment()

    # 병렬성 조정 병렬성을 2로 설정하세요.
    env.set_parallelism(2)

    # CSV 파일 읽기
    df = pd.read_csv("../data/data.csv")

    # 필요한 컬럼만 선택 후 결측값 제거 (transaction_type과 amount 컬럼을 선택하고, 결측값을 제거하세요.)
    transactions = df[["transaction_type", "amount"]].dropna().values.tolist()

    # 데이터 스트림 생성 (데이터 타입 [문자열, 실수형]으로 지정하세요.)
    transaction_stream = env.from_collection(transactions, type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()]))

    # 거래 유형별 총 거래 금액 계산
    transaction_total = (transaction_stream
                         .key_by(lambda x: x[0])
                         .reduce(lambda a, b: (a[0], a[1] + b[1])))

    # 결과 출력
    transaction_total.print()

    # 실행 (Flink 실행 함수를 작성해주세요.)
    env.execute("Transaction Type Aggregation")

if __name__ == "__main__":
    main()
