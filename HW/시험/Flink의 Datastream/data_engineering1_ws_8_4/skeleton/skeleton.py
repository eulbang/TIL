"""
목표
| 학습목표
-      filter() 연산을 통해 거래 금액 기준으로 스트림을 분할하는 방법을 학습한다.-      반복(Iteration) 함수를 적용하여 낮은 거래 금액 데이터에 대해 일정 횟수 동안 거래 금액을 10%씩 증가시키는 변환 연산 과정을 이해한다.-      union() 연산을 사용하여 분할된 스트림을 병합하고, 최종 결과를 실시간으로 출력하는 방법을 학습한다.   | 학습 개념  PyFlink의 변환 연산은 실시간 데이터 스트림에서 데이터를 선별, 변환 및 집계하는 데 중요한 역할을 한다. 본 실습에서는 금융 거래 데이터의 "stock_ticker"와 "amount" 정보를 Pandas로 전처리한 후, PyFlink의 from_collection()을 이용해 스트림을 생성한다. 그 후, Filter 연산을 통해 거래 금액에 따라 스트림을 두 개로 분할하고, 낮은 거래 금액 스트림에는 반복 연산을 적용하여 거래 금액을 10%씩 증가시키는 작업을 수행한 후, 두 스트림을 union 연산으로 병합하는 과정을 다룬다.  
문제
| 학습 방향  김싸피가 수행 중인 실시간 금융 거래 데이터 처리에서는 거래 금액이 일정 기준 이상인 데이터와 그렇지 않은 데이터를 분리하여 다르게 처리할 필요가 있다. 본 실습에서는 CSV 파일로부터 금융 거래 데이터를 불러와 Pandas로 전처리한 후, PyFlink를 사용하여 데이터를 스트림으로 변환한다. 이후, Filter 연산을 통해 거래 금액이 5000 이상인 데이터와 5000 미만인 데이터를 분리하고, 낮은 거래 금액 데이터에 대해서는 반복 연산을 적용해 거래 금액을 10%씩 증가시키는 과정을 수행한다. 마지막으로, 두 개의 처리된 스트림을 union 연산으로 병합하여 최종 결과를 실시간으로 출력하는 전체 변환 과정을 학습한다. 사용된 주요 개념 - PyFlink의 filter(): 데이터를 조건에 따라 선별하는 연산 - PyFlink의 reduce(): 그룹 내 데이터를 누적 집계하는 연산 - PyFlink의 map(): 집계 결과를 가공하는 연산 - PyFlink의 union(): 여러 스트림을 병합하는 연산    
요구사항
1.    실행 환경 생성
2.    Filnk 실행 환경을 생성합니다.
3.    CSV 데이터 불러오기 및 전처리
4.    Pandas를 사용하여 금융 거래 CSV 파일에서 "stock_ticker"와 "amount" 컬럼의 데이터를 불러오세요.
5.    결측값을 제거한 후, 각 거래에 대해 초기 거래 횟수 1을 추가하여 리스트 형태의 튜플로 변환하세요.
6.    데이터 스트림 생성
7.    PyFlink의 from_collection()을 사용하여 전처리된 데이터를 데이터 스트림으로 변환하세요.
8.    데이터 타입은 (문자열, 실수형, 정수형) 튜플로 지정하세요.
9.    데이터 분할
10. filter() 연산을 사용하여 거래 금액이 5000 이상인 데이터와 5000 미만인 데이터를 각각 분리하세요.
11. 반복 처리
12. 반복 함수를 적용하여, 5000 미만의 거래 데이터에 대해 거래 금액을 10%씩 증가시키는 연산을 최대 10회 반복하세요.
13. 스트림 병합
14. union() 연산을 사용하여 반복 처리가 완료된 데이터 스트림과 5000 이상 거래 데이터 스트림을 병합하세요.
15. 프로그램 실행
16. 최종 결과를 print() 함수를 통해 출력합니다.
17. 전체 파이프라인을 실행합니다.   
"""

import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def process_transactions(input_stream):
    """
    거래 데이터를 반복 처리하는 함수
    - 최대 10회 반복 후 종료
    - 거래 금액을 10% 증가시키면서 5000 미만 데이터만 유지
    """
    max_iterations = 10  # 최대 반복 횟수
    iteration = 0

    while iteration < max_iterations:
        updated_stream = (input_stream
                          .map(lambda x: (x[0], x[1] * 1.1), output_type=Types.TUPLE([Types.STRING(), Types.FLOAT()]))  
                          .filter(lambda x: x[1] < 5000))  # 5000 미만 값만 유지

        if updated_stream is None or iteration == max_iterations - 1:  
            break  

        input_stream = updated_stream  # 업데이트된 데이터를 사용
        iteration += 1  

    return input_stream  # 최종 처리된 스트림 반환

def main():
    # Flink 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # CSV 데이터 불러오기
    df = pd.read_csv("../data/data.csv")
    transactions = df[['stock_ticker', 'amount']].dropna().values.tolist()  

    # 데이터 스트림 생성
    transaction_stream = env.from_collection(
        transactions, 
        type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()])
    )

    # 거래 금액 기준 데이터 분할
    high_value_stream = transaction_stream.filter(lambda x: x[1] >= 5000)  # 5000 이상인 거래만 선택하는 람다 함수
    low_value_stream = transaction_stream.filter(lambda x: x[1] < 5000 )  # 5000 미만 거래만 선택하는 람다 함수 작성

    # 반복 연산 적용
    processed_stream = process_transactions(low_value_stream)  # 반복 적용할 데이터 스트림 지정

    # 최종 결과 스트림 병합
    final_stream = processed_stream.union(high_value_stream)  # 두 개의 데이터 스트림을 병합

    # 결과 출력
    final_stream.print()

    # 실행
    env.execute("Transaction Processing with Split & Iteration")

if __name__ == "__main__":
    main()
