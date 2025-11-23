"""
목표
| 학습목표
-      Flink의 실행 환경을 구성하고 병렬성을 설정하는 방법을 학습한다.-      CSV 형식의 금융 뉴스 데이터를 Flink 데이터 스트림으로 변환하는 과정을 이해한다.-      WordCount 기법을 적용하여 텍스트 데이터를 분석하고 단어 빈도수를 계산하는 방법을 익힌다.   | 학습 개념  Flink는 대용량 데이터를 실시간으로 처리할 수 있는 분산형 데이터 처리 프레임워크입니다.이를 활용하여 금융 뉴스 데이터를 스트리밍 데이터처럼 변환하고 분석할 수 있습니다.본 실습에서는 Flink의 스트림 처리 기능을 사용하여 단어별 등장 횟수를 계산하는 WordCount 연산을 수행합니다.   
문제
| 학습 방향  금융 데이터 분석 팀 소속인 김싸피는 뉴스 기사 데이터를 활용하여 특정 키워드의 빈도수를 분석하고 있습니다. 이 분석을 통해 금융 시장에서 자주 언급되는 핵심 용어를 파악하고, 주식 변동성과의 관계를 연구합니다. 뉴스 기사에서 등장하는 단어를 추출하고, WordCount 분석을 수행하여 가장 많이 언급된 단어를 도출합니다. 이를 통해 금융 뉴스에서 반복적으로 등장하는 키워드를 기반으로 트렌드를 분석하고, 향후 시장 예측을 위한 데이터를 준비합니다. 데이터 설명 - news_text: 뉴스 기사 본문에서 텍스트 데이터만 추출하여 분석에 활용된다.  
요구사항
1.    실행 환경 설정
2.    Flink 실행 환경을 설정하세요.
3.    병렬성 값을 설정하세요.
4.    금융 뉴스 데이터 입력 및 전처리
5.    CSV 파일에서 데이터를 불러오고 원하는 컬럼을 선택하세요.
6.    결측값을 제거하고 리스트 형태로 변환하세요.
7.    데이터 스트림 생성
8.    리스트 형태의 데이터를 Flink 스트림으로 변환하세요.
9.    WordCount 연산 수행
10. 문장을 단어 단위로 나누고 각 단어의 출현 횟수를 1로 설정하세요.
11. 단어별로 데이터를 그룹화한 후, 같은 단어의 출현 횟수를 합산하세요.
12. 결과 출력 및 실행
13. 단어 빈도수 계산 결과를 출력하세요.
14. 프로그램을 실행하여 WordCount 결과를 확인하세요.
"""

import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    # 환경 생성 (Flink의 실행 환경을 설정하세요.)
    env = StreamExecutionEnvironment.get_execution_environment()

    # 병렬성 조정 (병렬성을 2로 설정하세요.)
    env.set_parallelism(2)

    # CSV 파일 읽기
    df = pd.read_csv("../data/data.csv")

    # news_text 컬럼에서 결측값 제거 후 리스트 변환 (news_text 컬럼을 선택하세요.)
    news_texts = df["news_text"].dropna().tolist()

    # 데이터 스트림 생성 (문자열 데이터 타입을 지정하세요.)
    text_stream = env.from_collection(news_texts, type_info=Types.STRING())

    # WordCount 파이프라인 구성
    word_count = (text_stream
                  .map(lambda text: [(word.lower(), 1) for word in text.split()], output_type=Types.LIST(Types.TUPLE([Types.STRING(), Types.INT()])))
                  .flat_map(lambda words: words, output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
                  .key_by(lambda x: x[0])
                  .reduce(lambda a, b: (a[0], a[1] + b[1])))

    # 결과 출력(출력함수를 작성하세요.)
    word_count.print()

    # 실행
    env.execute("Finance News WordCount")

if __name__ == "__main__":
    main()
