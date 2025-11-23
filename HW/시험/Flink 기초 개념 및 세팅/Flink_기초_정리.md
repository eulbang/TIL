

📌 Flink 기초 개념 및 세팅 실습/과제 정리
---
- [WS 7-1: PyFlink 설치 및 테스트](#ws-7-1-pyflink-설치-및-테스트)
- [WS 7-2: 기본 스트림 생성](#ws-7-2-기본-스트림-생성)
- [WS 7-3: CSV → WordCount](#ws-7-3-csv--wordcount)
- [WS 7-4: 실시간 WordCount](#ws-7-4-실시간-wordcount)
- [WS 7-5: 스트림 결합·FileSink](#ws-7-5-스트림-결합filesink)
- [HW 7-2: 뉴스 WordCount](#hw-7-2-뉴스-wordcount)
- [HW 7-4: 거래 유형별 집계](#hw-7-4-거래-유형별-집계)

## WS 7-1: PyFlink 설치 및 테스트
- 목표: WSL에서 PyFlink 1.19.3 설치 후 간단한 스트림 실행 확인.
- 핵심 단계: 실행 환경 생성 → 병렬성 2 설정 → 컬렉션 스트림 생성/출력 → `env.execute`.
- 정답 코드: `data_engineering1_ws_7_1/skeleton/skeleton.py`
```python
from pyflink.datastream import StreamExecutionEnvironment

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(2)
    data_stream = env.from_collection(["Hello", "Flink", "World"])
    data_stream.print()
    env.execute("Flink Installation Test")

if __name__ == "__main__":
    main()
```

## WS 7-2: 기본 스트림 생성
- 목표: PyFlink 실행 환경 구성 후 리스트 데이터를 스트림으로 변환해 출력.
- 정답 코드: `data_engineering1_ws_7_2/skeleton/skeleton.py`
```python
from pyflink.datastream import StreamExecutionEnvironment

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    data_stream = env.from_collection(["Hello", "Flink", "World"])
    data_stream.print()
    env.execute("Flink Installation Test")

if __name__ == "__main__":
    main()
```

## WS 7-3: CSV → WordCount
- 목표: CSV(news_text) 로드 → 결측 제거 → 스트림 변환 → WordCount.
- 정답 코드: `data_engineering1_ws_7_3/skeleton/skeleton.py`
```python
import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(2)

    df = pd.read_csv("../data/data.csv")
    news_texts = df["news_text"].dropna().tolist()
    text_stream = env.from_collection(news_texts, type_info=Types.STRING())

    word_count = (text_stream
                  .map(lambda text: [(word.lower(), 1) for word in text.split()],
                       output_type=Types.LIST(Types.TUPLE([Types.STRING(), Types.INT()])))
                  .flat_map(lambda words: words,
                            output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
                  .key_by(lambda x: x[0])
                  .reduce(lambda a, b: (a[0], a[1] + b[1])))

    word_count.print()
    env.execute("Finance News WordCount")

if __name__ == "__main__":
    main()
```

## WS 7-4: 실시간 WordCount
- 목표: CSV(news_text) → 스트림 → `flat_map` + `reduce`로 실시간 단어 집계.
- 정답 코드: `data_engineering1_ws_7_4/skeleton/skeleton.py`
```python
import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(2)

    df = pd.read_csv("../data/data.csv")
    news_texts = df["news_text"].dropna().tolist()
    text_stream = env.from_collection(news_texts, type_info=Types.STRING())

    word_count = (text_stream
                  .flat_map(lambda text: [(word.lower(), 1) for word in text.split()],
                            output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
                  .key_by(lambda x: x[0])
                  .reduce(lambda a, b: (a[0], a[1] + b[1])))

    word_count.print()
    env.execute("Streaming Finance News WordCount")

if __name__ == "__main__":
    main()
```

## WS 7-5: 스트림 결합·FileSink
- 목표: 수동 데이터 + CSV(transaction_id, amount) 스트림을 union 후 금액 1.2배 변환, 출력 및 파일 저장.
- 정답 코드: `data_engineering1_ws_7_5/skeleton/skeleton.py`
```python
import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FileSink
from pyflink.common.serialization import Encoder
from pyflink.common.typeinfo import Types

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(2)

    manual_data = [("Manual1", 1000.0), ("Manual2", 2000.0)]
    manual_stream = env.from_collection(manual_data,
                                        type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()]))

    df = pd.read_csv("../data/data.csv")
    file_data = df[["transaction_id", "amount"]].dropna().values.tolist()
    file_stream = env.from_collection(file_data,
                                      type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()]))

    combined_stream = manual_stream.union(file_stream)
    processed_stream = combined_stream.map(lambda x: (x[0], x[1] * 1.2))

    string_stream = processed_stream.map(lambda x: f\"{x[0]},{x[1]}\", output_type=Types.STRING())
    string_stream.print()

    file_sink = FileSink.for_row_format(
        "./output/transactions_result",
        Encoder.simple_string_encoder()
    ).build()

    string_stream.sink_to(file_sink)
    env.execute("Custom Source and Sink Example")

if __name__ == "__main__":
    main()
```

## HW 7-2: 뉴스 WordCount
- 목표: 실행 환경/병렬성 설정 후 news_text 컬럼으로 WordCount 수행.
- 정답 코드: `data_engineering1_hw_7_2/skeleton/skeleton.py`
```python
import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(2)

    df = pd.read_csv("../data/data.csv")
    news_texts = df["news_text"].dropna().tolist()
    text_stream = env.from_collection(news_texts, type_info=Types.STRING())

    word_count = (text_stream
                  .map(lambda text: [(word.lower(), 1) for word in text.split()],
                       output_type=Types.LIST(Types.TUPLE([Types.STRING(), Types.INT()])))
                  .flat_map(lambda words: words,
                            output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
                  .key_by(lambda x: x[0])
                  .reduce(lambda a, b: (a[0], a[1] + b[1])))

    word_count.print()
    env.execute("Finance News WordCount")

if __name__ == "__main__":
    main()
```

## HW 7-4: 거래 유형별 집계
- 목표: 거래 데이터(transaction_type, amount)를 스트림으로 변환해 유형별 금액 합계 계산.
- 정답 코드: `data_engineering1_hw_7_4/skeleton/skeleton.py`
```python
import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(2)

    df = pd.read_csv("../data/data.csv")
    transactions = df[["transaction_type", "amount"]].dropna().values.tolist()
    transaction_stream = env.from_collection(transactions,
                                             type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()]))

    transaction_total = (transaction_stream
                         .key_by(lambda x: x[0])
                         .reduce(lambda a, b: (a[0], a[1] + b[1])))

    transaction_total.print()
    env.execute("Transaction Type Aggregation")

if __name__ == "__main__":
    main()
```
