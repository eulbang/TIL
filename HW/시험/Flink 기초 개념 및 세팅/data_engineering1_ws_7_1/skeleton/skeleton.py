"""
목표
| 학습목표
-      WSL 환경에서 Apache Flink 1.19.3을 다운로드하고 설치하는 방법을 학습한다.-      Flink 실행 환경을 구성하고 실행하는 방법을 익힌다.-      Flink 프로그램을 실행하여 정상적으로 작동하는지 확인한다.   | 학습 개념  PyFlink는 Python에서 Apache Flink 기능을 사용할 수 있도록 제공되는 라이브러리로,스트리밍 및 배치 데이터 처리를 지원하는 분산형 데이터 처리 프레임워크이다.WSL 환경에서 PyFlink를 활용하면 Flink의 데이터 스트림 API를 Python으로 실행할 수 있으며,이번 실습에서는 PyFlink를 설치하고 간단한 스트림 처리 프로그램을 실행하는 방법을 실습한다.   
문제
| 학습 방향  데이터 분석 팀 소속 김싸피는 WSL 환경에서 PyFlink를 활용하여 대규모 스트리밍 데이터를 처리할 수 있는 환경을 구축하고 있다. 이를 위해 PyFlink를 설치하고 실행 환경을 설정한 후, 간단한 PyFlink 스트리밍 프로그램을 실행하여 정상적으로 동작하는지 확인한다. 이 과정에서 PyFlink의 실행 방식과 기본적인 데이터 스트림 처리를 테스트하고, Flink의 주요 개념을 이해하는 것이 목표이다. 설치 환경 - 운영 체제: Windows Subsystem for Linux (WSL) - PyFlink 버전: 1.19.3 - Java 버전: OpenJDK 11 이상 필요 (17설치)   
요구사항
1.    WSL 환경에서 Flink 1.19.3 다운로드 및 설치
2.    pip install apache-flink==1.19.3 3.    Flink 실행 환경 설정
4.    PyFlink 실행을 위해 Java 11 이상이 설치되어 있어야 한다. 
5.    Java 버전을 확인한다.(java 17로 통일)
6.    Flink 환경을 설정하기 위해 JAVA_HOME을 설정한다.
7.    PyFlink 간단한 실행 테스트
8.    PyFlink의 실행 환경을 생성한다.
9.    간단한 데이터 스트림을 생성하여 출력한다.
10. PyFlink 프로그램 실행 및 결과 확인
11. PyFlink 프로그램을 실행하여 정상적으로 데이터가 출력되는지 확인한다.
"""

from pyflink.datastream import StreamExecutionEnvironment

def main():
    # Flink 실행 환경을 생성하세요.
    env = StreamExecutionEnvironment.get_execution_environment()

    # 병렬성을 2로 설정하세요.
    env.set_parallelism(2)

    # 간단한 데이터 스트림 생성
    data_stream = env.from_collection(["Hello", "Flink", "World"])

    # 스트림 데이터 출력
    data_stream.print()

    # Flink 프로그램을 실행하세요.
    env.execute("Flink Installation Test")

if __name__ == "__main__":
    main()
