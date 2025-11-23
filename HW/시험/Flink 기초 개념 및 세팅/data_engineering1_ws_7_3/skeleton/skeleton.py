"""
목표
| 학습목표
-      PyFlink 실행 환경을 설정하는 방법을 학습한다.-      CSV 데이터를 Pandas를 사용하여 불러오고 전처리하는 과정을 익힌다.-      PyFlink의 from_collection()을 활용하여 데이터를 Flink 데이터 스트림으로 변환하는 방법을 실습한다.   | 학습 개념  PyFlink는 Python에서 Apache Flink의 기능을 사용할 수 있도록 제공되는 API이다. 이를 활용하면 실시간 데이터 스트리밍 및 배치 처리를 Python 코드로 수행할 수 있다. 본 실습에서는 CSV 데이터를 Pandas로 불러오고, 데이터를 전처리한 후 PyFlink를 활용하여 데이터 스트림을 생성하는 과정을 실습한다.  
문제
| 학습 방향  데이터 분석 팀 소속 김싸피는 PyFlink를 활용하여 금융 뉴스 데이터를 스트리밍 데이터로 변환하는 작업을 수행하고 있다. 이를 위해 CSV 파일에서 데이터를 불러오고, 결측값을 처리한 후 PyFlink의 from_collection()을 사용하여 데이터 스트림을 생성한다. 이를 통해 대규모 텍스트 데이터를 실시간으로 처리하는 방법을 익히고, PyFlink를 활용한 데이터 전처리 기법을 학습하는 것이 목표이다. 사용된 주요 개념 - Pandas의 read_csv(): CSV 파일을 로드하는 함수 - Pandas의 dropna(): 결측값을 제거하는 함수 - Pandas의 tolist(): 데이터를 리스트로 변환하는 함수 - PyFlink의 StreamExecutionEnvironment: Flink 프로그램의 실행 환경을 설정하는 객체 - PyFlink의 from_collection(): 리스트 데이터를 Flink의 데이터 스트림으로 변환하는 메서드    
요구사항
1.   실행 환경 생성
2.    PyFlink 실행 환경을 생성하세요.
3.    CSV 데이터 불러오기 및 전처리
4.    Pandas를 사용하여 CSV 파일에서 데이터를 불러오세요.
5.    news_text 컬럼을 선택하고 결측값을 제거한 후 리스트로 변환하세요.
6.   데이터 스트림 생성
7.    PyFlink의 from_collection()을 사용하여 데이터를 Flink 데이터 스트림으로 변환하세요.
8.    wordcount 파이프라인 구성
9.    map, flat_map, key_bym reduce 함수를 사용하여 주어진 텍스트에서 단어의 개수를 세는 프로그램 작성
10.   데이터 출력 및 실행
11. 생성된 데이터 스트림을 출력하고, Flink 프로그램을 실행하세요.
"""

import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    # Flink 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경을 가져오는 함수 호출

    # 병렬성 2로 설정
    env.set_parallelism(2)

    # CSV 데이터 불러오기
    df = pd.read_csv("../data/data.csv")
    news_texts = df["news_text"].dropna().tolist()  # 결측값 제거 후 리스트 변환

    # 데이터 스트림 생성
    text_stream = env.from_collection(news_texts, type_info=Types.STRING())  # 데이터 스트림을 생성하는 메서드

    # WordCount 파이프라인 구성(2일차에 각각의 함수에 대한 내용 다룰 예정)
    word_count = (text_stream
                  .map(lambda text: [(word.lower(), 1) for word in text.split()], 
                       output_type=Types.LIST(Types.TUPLE([Types.STRING(), Types.INT()])))
                  .flat_map(lambda words: words, 
                            output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
                  .key_by(lambda x: x[0])
                  .reduce(lambda a, b: (a[0], a[1] + b[1])))

    # 결과 출력
    word_count.print()  # 스트림을 출력하는 메서드 호출

    # 실행
    env.execute("Finance News WordCount")  # Flink 실행을 시작하는 메서드 호출

if __name__ == "__main__":
    main()