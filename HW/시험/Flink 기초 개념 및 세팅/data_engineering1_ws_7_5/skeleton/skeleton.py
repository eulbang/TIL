"""
목표
| 학습목표
-      Pandas를 사용하여 금융 거래 CSV 데이터를 불러오고 전처리하는 방법을 익혀, 파일 데이터를 스트림으로 변환할 준비를 한다.-      PyFlink의 from_collection()을 이용해 직접 만든 데이터와 파일에서 불러온 데이터를 스트림으로 변환하는 방법을 실습한다.-      두 개의 데이터 스트림을 union() 연산을 통해 결합하고, map 연산을 통해 거래 금액을 변환하는 방법을 이해한다.-      FileSink를 설정하여 변환된 결과를 지정된 디렉터리에 파일로 저장하고, 결과를 실시간으로 출력하는 방법을 학습한다.   | 학습 개념  PyFlink는 Python 환경에서 Apache Flink의 스트리밍 처리 기능을 활용할 수 있도록 지원하는 API이다. 본 실습에서는 Pandas로 금융 거래 CSV 데이터를 불러와 결측값을 제거한 후 리스트로 변환한 데이터를 PyFlink 스트림으로 전환한다. 또한, 직접 만든 데이터 스트림과 파일에서 불러온 데이터 스트림을 union() 연산으로 결합한 후, map 연산을 통해 거래 금액을 1.2배 증가시키는 변환을 적용하고, 결과를 PrintSink와 FileSink를 사용하여 실시간 출력 및 파일 저장하는 전체 흐름을 다룬다.  
문제
| 학습 방향
김싸피가 진행 중인 실시간 금융 거래 데이터 처리는 다양한 소스에서 발생하는 데이터를 결합하여 처리하는 데 중요한 역할을 한다. 본 실습에서는 CSV 파일과 수동 데이터 두 가지 소스를 결합하여 스트림을 생성한 후, map 연산을 통해 거래 금액을 변환하는 과정을 학습한다. 이어서, 변환된 결과를 실시간으로 출력하고, FileSink를 통해 지정된 디렉터리에 파일로 저장하는 방법을 실습하여, 데이터 변환 및 저장 작업의 전체 파이프라인을 이해한다. 사용된 주요 개념 - PyFlink의 union(): 여러 데이터 스트림을 결합하는 연산 - PyFlink의 map(): 데이터를 원하는 형식으로 변환하는 연산 - FileSink와 Encoder: 스트림 데이터를 파일로 저장하는 구성 요소    
요구사항
1.    실행 환경 생성
2.    PyFlink 실행 환경을 생성하세요.
3.    CSV 데이터 불러오기 및 전처리
4.    Pandas를 사용하여 금융 거래 CSV 파일(예: data.csv)에서 "transaction_id"와 "amount" 컬럼의 데이터를 불러오고, 결측값을 제거한 후 리스트로 변환하세요.
5.    데이터 스트림 생성
6.    PyFlink의 from_collection() 메서드를 사용하여, 수동 데이터[("Manual1", 1000.0), ("Manual2", 2000.0)]와 파일 데이터를 스트림으로 각각 생성하세요.
7.    데이터 스트림 결합 및 변환
8.    union() 연산을 사용하여 두 개의 데이터 스트림을 결합하세요.
9.    map() 연산을 적용하여 각 데이터의 거래 금액을 1.2배 증가시키는 변환을 수행하세요.
10. 결과 출력 및 파일 저장
11. print() 메서드를 사용하여 변환 결과를 실시간으로 출력하세요.
12. FileSink를 설정하여 변환된 결과를 "./output/result" 디렉터리에 파일로 저장하세요.
13. 프로그램 실행
14. env.execute()를 통해 전체 파이프라인이 정상 실행되는지 확인합니다.
"""
import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FileSink
from pyflink.common.serialization import Encoder
from pyflink.common.typeinfo import Types

def main():
    # Flink 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경을 가져오는 메서드 호출
    
    # 병렬성 2로 설정
    env.set_parallelism(2)

    # 직접 만든 데이터 스트림
    manual_data = [("Manual1", 1000.0), ("Manual2", 2000.0)]
    manual_stream = env.from_collection(manual_data, type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()]))

    # 파일에서 읽어온 데이터 스트림
    df = pd.read_csv("../data/data.csv")
    file_data = df[['transaction_id', 'amount']].dropna().values.tolist()
    file_stream = env.from_collection(file_data, type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()]))

    # 두 개의 데이터 스트림 결합
    combined_stream = manual_stream.union(file_stream)  # 두 개의 스트림을 결합하는 연산

    # 데이터 변환 (금액을 1.2배 증가)
    processed_stream = combined_stream.map(lambda x: (x[0], x[1] * 1.2))

    # 튜플을 문자열로 변환 → "Manual1,1200.0"
    string_stream = processed_stream.map(
        lambda x: f"{x[0]},{x[1]}",
        output_type=Types.STRING()
    )

    # PrintSink를 활용한 출력
    string_stream.print()

    # FileSink 설정 (문자열 저장용)
    file_sink = FileSink.for_row_format(
        "./output/transactions_result",
        Encoder.simple_string_encoder()
    ).build()

    # FileSink 연결
    string_stream.sink_to(file_sink)

    # Flink 실행
    env.execute("Custom Source and Sink Example")


if __name__ == "__main__":
    main()
