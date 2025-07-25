# TMDB API 키 설정
# API 호출 함수

import requests
import csv

API_KEY = '592fb26f18bc0eefbb816fc25884f862'
BASE_URL = 'https://api.themoviedb.org/3/'

def fetch_movie_details(movie_id, api_key, base_url, language='ko-KR'):
    url = f"{base_url}movie/{movie_id}"
    params = {
        'api_key': api_key,
        'language': language
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'movie_id': movie_id,
            'budget': data.get('budget'),
            'revenue': data.get('revenue'),
            'runtime': data.get('runtime'),
            'genres': ', '.join([genre['name'] for genre in data.get('genres', [])])
        }
    else:
        print(f"API 요청 실패: {response.status_code} (movie_id: {movie_id})")
        return {
            'movie_id': movie_id,
            'budget': None,
            'revenue': None,
            'runtime': None,
            'genres': None
        }

def read_movie_ids_from_csv(filename='movies.csv'):
    movie_ids = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie_ids.append(row['id'])
    return movie_ids

def save_movie_details_to_csv(details_list, filename='movie_details.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['movie_id', 'budget', 'revenue', 'runtime', 'genres'])
        for details in details_list:
            writer.writerow([
                details['movie_id'],
                details['budget'],
                details['revenue'],
                details['runtime'],
                details['genres']
            ])

if __name__ == "__main__":
    movie_ids = read_movie_ids_from_csv()
    details_list = []
    for movie_id in movie_ids:
        details = fetch_movie_details(movie_id, API_KEY, BASE_URL)
        details_list.append(details)
    save_movie_details_to_csv(details_list)
