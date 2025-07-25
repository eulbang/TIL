# TMDB API 키 설정

# API 호출 함수

# 영화 데이터 처리 함수

# 데이터 수집 및 CSV 파일로 저장
API_KEY = '592fb26f18bc0eefbb816fc25884f862'
BASE_URL = 'https://api.themoviedb.org/3/'

import requests
import csv

def fetch_popular_movies(api_key, base_url, language='ko-KR', page=1):
    url = f"{base_url}movie/popular"
    params = {
        'api_key': api_key,
        'language': language,
        'page': page
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print(f"API 요청 실패: {response.status_code}")
        return []

def save_movies_to_csv(movies, filename='movies.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'title', 'release_date', 'popularity'])
        for movie in movies:
            writer.writerow([
                movie.get('id'),
                movie.get('title'),
                movie.get('release_date'),
                movie.get('popularity')
            ])

if __name__ == "__main__":
    all_movies = []
    for page in range(1, 11):  # 1~5페이지까지 조회 (필요에 따라 숫자 조정)
        movies = fetch_popular_movies(API_KEY, BASE_URL, page=page)
        all_movies.extend(movies)
    save_movies_to_csv(all_movies)

