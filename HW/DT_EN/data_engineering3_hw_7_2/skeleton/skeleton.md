# 내장 WordCount 실행 실습

## 1. 입력 파일 업로드
```bash
hadoop fs -put shopping_transactions.csv /user/hadoop/input/
hadoop fs -ls /user/hadoop/input/
hadoop fs -cat /user/hadoop/input/shopping_transactions.csv | head -10
```

## 2. 내장 WordCount 실행
```bash
hadoop jar /home/ssafy/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar \
  wordcount /user/hadoop/input/shopping_transactions.csv /user/hadoop/output/wordcount_builtin
```

## 3. 결과 확인
```bash
hadoop fs -cat /user/hadoop/output/wordcount_builtin/part-* | sort -k2 -nr | head -10
```
