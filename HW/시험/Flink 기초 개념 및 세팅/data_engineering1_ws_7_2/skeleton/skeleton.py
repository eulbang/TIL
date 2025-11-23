"""
목표
| 학습목표
-      PyFlink 실행 환경을 구성하는 방법을 학습한다.-      PyFlink의 StreamExecutionEnvironment를 활용하여 데이터 스트림을 생성하는 방법을 익힌다.-      PyFlink 프로그램을 실행하여 데이터를 출력하는 방법을 실습한다.   | 학습 개념  PyFlink는 Apache Flink의 Python API로, Python 환경에서 Flink의 기능을 활용하여 실시간 데이터 스트리밍 및 배치 처리를 수행할 수 있다. 이번 실습에서는 PyFlink 실행 환경을 설정하고, 리스트 데이터를 Flink 스트림으로 변환한 후 출력하는 방법을 학습한다.  
문제
| 학습 방향  데이터 분석 팀 소속 김싸피는 PyFlink를 활용하여 데이터 스트리밍을 테스트하고 있다. 이를 위해 PyFlink 실행 환경을 설정한 후, 간단한 데이터를 스트리밍하여 정상적으로 동작하는지 확인한다. PyFlink의 실행 방식을 익히고, 데이터 스트림을 활용하는 방법을 실습하는 것이 목표이다. 사용된 주요 개념 - StreamExecutionEnvironment: Flink 프로그램의 실행 환경을 설정하는 객체 - from_collection(): 리스트 데이터를 Flink의 데이터 스트림으로 변환하는 메서드 - print(): 데이터 스트림을 출력하는 메서드 - execute(): Flink 프로그램을 실행하는 메서드    
요구사항
1.  실행 환경 생성
2.    PyFlink 실행 환경을 생성하세요.
3.  데이터 스트림 생성
4.    리스트 데이터를 Flink 데이터 스트림으로 변환하세요.
4.  데이터 출력 및 실행
6.    생성된 데이터 스트림을 출력하고, Flink 프로그램을 실행하세요.  
"""

from pyflink.datastream import StreamExecutionEnvironment  # Flink의 실행 환경을 가져오는 모듈 임포트

def main():
    # Flink 실행 환경 생성
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경을 생성하는 코드

    # 데이터 스트림 생성 코드
    data_stream = env.from_collection(["Hello", "Flink", "World"])

    # 스트림 데이터 출력
    data_stream.print()  # 데이터 스트림의 내용을 출력하는 코드

    # Flink 프로그램 실행
    env.execute("Flink Installation Test")  # Flink 프로그램 실행 코드

if __name__ == "__main__":
    main()
