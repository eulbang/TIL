import pandas as pd
import sqlite3
import os

# CSV 파일들이 있는 폴더 경로
folder_path = "."

# DB 파일 생성
conn = sqlite3.connect("movie_data.db")

# 폴더 내 모든 파일 탐색
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        table_name = filename.replace(".csv", "")  # 테이블 이름: 확장자 제거
        file_path = os.path.join(folder_path, filename)

        try:
            df = pd.read_csv(file_path)
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f"✅ {filename} → '{table_name}' 테이블로 삽입 완료")
        except Exception as e:
            print(f"❌ {filename} 처리 중 오류: {e}")

conn.close()
print("📦 모든 CSV → DB로 삽입 완료")