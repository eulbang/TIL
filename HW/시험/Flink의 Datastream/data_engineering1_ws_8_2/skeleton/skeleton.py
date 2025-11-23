"""
목표
| 학습목표
-      PyFlink의 from_collection()을 사용해 데이터를 스트림으로 생성하는 방법을 익힌다.-      flat_map() 및 filter() 연산을 통해 텍스트 데이터를 단어 단위로 분해하여 금융 관련 키워드를 감지하는 방법을 학습한다.-      처리된 결과를 실시간으로 출력하고 Flink 작업을 실행하는 방법을 실습한다.   | 학습 개념  본 실습에서는 금융 뉴스 데이터의 "news_text" 컬럼을 Pandas로 불러와 전처리한 후, 이를 PyFlink 스트림으로 변환하여 텍스트 데이터를 단어 단위로 분해하는 FlatMap 연산과, 미리 정의한 금융 관련 키워드 집합에 포함되는 단어만 선별하는 Filter 연산을 통해 실시간 데이터 처리를 구현하는 방법을 다룬다.   
문제
| 학습 방향  실시간 금융 데이터 분석은 시장 동향을 파악하고 금융 서비스를 개선하는 데 중요한 역할을 한다. 본 실습에서는 CSV 파일로부터 금융 뉴스 데이터를 불러와 Pandas로 전처리한 후, PyFlink를 사용하여 데이터 스트림을 생성한다. 이어서, FlatMap 연산으로 텍스트를 단어별로 분해하고, Filter 연산을 통해 "stock", "market", "investment", "economy"와 같은 금융 키워드에 해당하는 단어만 선별한다. 마지막으로, 실시간으로 처리된 결과를 출력하고 Flink 작업을 실행하는 전체 흐름을 이해한다. 사용된 주요 개념 - PyFlink의 flat_map(): 텍스트 데이터를 단어 단위로 분해하는 연산 - PyFlink의 filter(): 데이터를 조건에 따라 선별하는 연산 - PyFlink의 key_by(): 데이터를 그룹화하는 연산   
요구사항
1.    실행 환경 생성
2.    PyFlink 실행 환경을 생성하세요.
3.    CSV 데이터 불러오기 및 전처리
4.    Pandas를 사용하여 금융 뉴스 CSV 파일(data.csv)에서 데이터를 불러오세요.
5.    "news_text" 컬럼을 선택하고, 결측값을 제거한 후 리스트로 변환하세요.
6.    데이터 스트림 생성
7.    PyFlink의 from_collection() 메서드를 사용하여 전처리된 데이터를 데이터 스트림으로 변환하세요.
8.    데이터 타입은 문자열로 지정하세요.
9.    텍스트 처리 및 금융 키워드 필터링
10. flat_map()을 사용하여 각 뉴스 텍스트를 단어 단위로 분해하고, 각 단어의 출현 횟수를 1로 설정하는 튜플로 변환하세요.
11. 미리 정의한 금융 키워드 집합(예: {"stock", "market", "investment", "economy"})에 포함된 단어만 필터링하세요.
12. 결과 출력 및 작업 실행  13.  필터링된 결과를 실시간으로 출력하고, Flink 작업을 실행하세요.
"""

import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    # Flink 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()  # 실행 환경 가져오기
    # 병렬성 2로 설정
    env.set_parallelism(2)  

    # CSV 데이터 불러오기
    df = pd.read_csv("../data/data.csv")
    news_texts = df["news_text"].dropna().tolist()  # 결측값 제거 후 리스트 변환

    # 데이터 스트림 생성
    text_stream = env.from_collection(news_texts, type_info=Types.STRING())  # 데이터 스트림 생성

    # FlatMap 및 Filter 연산 적용
    finance_keywords = {"stock", "market", "investment", "economy"}
    processed_stream = (text_stream
                        .flat_map(lambda text: [(word.lower(), 1) for word in text.split()], 
                              output_type=Types.TUPLE([Types.STRING(), Types.INT()]))  # FlatMap 연산 적용
                        .filter(lambda x: x[0] in finance_keywords))  # 특정 금융 키워드만 필터링하는 함수

    # 키워드 별로 갯수 집계
    aggregated_stream = processed_stream.key_by(lambda x: x[0]).sum(1)
    # 결과 출력
    aggregated_stream.print()

    # 실행
    env.execute("FlatMap and Filter Example")  # Flink 실행

if __name__ == "__main__":
    main()
