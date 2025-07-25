'''
    외부 라이브러리나 모듈 등을 import 해와야 할 때,
    파일 열자마자 import 받지 마시고
    그 import가 반드시 필요한 경우에 받아 주십시오
        코드 외워서 쓰지 말 것
'''

# 요청을 보내야 한다.
import requests
import csv

response = requests.get("https://jsonplaceholder.typicode.com/todos").json()
completed_todos = [] # 최종 결과물을 담을 리스트
fields = ['id', 'title']
for item in response:
    if item.get('completed'):
        temp_item = {}
        for key in fields:
            temp_item[key] = item[key]
        completed_todos.append(temp_item)

with open('completed.todos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fields)
    writer.writeheader()
    writer.writerows(completed_todos)