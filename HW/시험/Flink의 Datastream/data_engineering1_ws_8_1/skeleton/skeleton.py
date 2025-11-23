"""
목표
| 학습목표
-      FileSink를 설정하여 스트리밍 결과를 지정된 디렉터리에 파일로 저장하는 방법을 학습한다.   | 학습 개념  PyFlink는 Python 환경에서 Apache Flink의 스트리밍 및 배치 데이터 처리 기능을 사용할 수 있도록 지원하는 API이다. 본 실습에서는 간단한 데이터 소스(예: ["Hello", "Flink", "World"])를 활용하여 스트리밍 환경을 구축하고, FileSink를 통해 실시간으로 처리된 결과를 파일로 저장하는 방법을 다룬다.  
문제
| 학습 방향  김싸피가 수행 중인 실시간 데이터 스트림 처리는 금융 거래와 같이 빠르게 변화하는 데이터를 분석하는 데 필수적이다. 이 실습에서는 CSV나 다른 외부 데이터 소스 대신 간단한 문자열 리스트를 사용하여 PyFlink 실행 환경을 설정하고, 데이터를 스트림으로 변환한 후, FileSink를 이용해 결과를 파일로 저장하는 전체 작업 흐름을 이해한다. 이를 통해 실시간 결과를 모니터링하고 저장하는 기본적인 방법을 익힌다.   
요구사항
1.    실행 환경 생성
2.    Flink 실행 환경을 생성하세요.
3.    데이터 소스 생성 및 스트림 변환
4.    간단한 문자열 리스트["Hello", "Flink", "World"]를 데이터 소스로 사용하세요.
5.    PyFlink의 from_collection() 메서드를 사용하여 데이터를 스트림으로 변환하세요.
6.    Java Encoder 및 Python Encoder 생성
7.    Java의 SimpleStringEncoder를 사용하여 Python Encoder를 생성하세요.
8.    FileSink 설정 및 데이터 저장
9.    FileSink를 설정하여 출력 디렉터리에 스트림 데이터를 저장하세요.
10. 출력 디렉터리는 "./output/result"로 지정하세요.
11. 결과 출력 및 Flink 작업 실행
12. 스트림 데이터를 출력하고, Flink 작업을 실행하여 파일에 결과가 저장되는지 확인하세요.
"""

import os
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FileSink
from pyflink.common.serialization import Encoder
from pyflink.common.typeinfo import Types
from pyflink.java_gateway import get_gateway

def main():
    # 실행 환경 생성
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경을 가져오는 함수 호출

    # 데이터 소스 생성
    data = ["Hello", "Flink", "World"]
    data_stream = env.from_collection(data, type_info=Types.STRING())  # 데이터를 스트림으로 변환하는 메서드 호출

    # Java 인코더 생성
    gateway = get_gateway()
    j_string_encoder = gateway.jvm.org.apache.flink.api.common.serialization.SimpleStringEncoder()  # Java 엔코더 객체 생성

    # Python Encoder 생성
    encoder = Encoder(j_string_encoder)

    # 출력 디렉터리 설정
    output_dir = "./output/result"
    os.makedirs(output_dir, exist_ok=True)  # 디렉터리 없으면 생성

    # FileSink 설정
    file_sink = FileSink.for_row_format(output_dir, encoder).build()  # FileSink 설정(빌드)

    # Sink에 데이터 연결
    data_stream.sink_to(file_sink)  # 데이터 스트림을 Sink에 연결

    # Flink 작업 실행
    env.execute("File Sink Example")  # Flink 실행 시작

if __name__ == "__main__":
    main()
