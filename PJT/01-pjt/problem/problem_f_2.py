import requests
import csv
from collections import Counter

def get_cast_names_with_duplicates(filename='movie_casts.csv'):
    cast_names = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cast_names.append(row['name'])  # 중복 포함 배우 이름 목록
    return cast_names

def save_names_to_csv(names, filename='prolific_actor.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['name'])
        for name in names:
            writer.writerow([name])

names = get_cast_names_with_duplicates()
counter = Counter(names)
prolific_names = [name for name, count in counter.items() if count >= 2]
save_names_to_csv(prolific_names)