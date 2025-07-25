# TMDB API 키 설정
API_KEY = '592fb26f18bc0eefbb816fc25884f862'
BASE_URL = 'https://api.themoviedb.org/3/'
import requests
import csv

# API 호출 함수
def fetch_movie_details(movie_id, api_key, base_url, language='ko-KR'):
    url = f"{base_url}movie/{movie_id}/credits"
    params = {
        'api_key': api_key,
        'language': language
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        cast_list = data.get('cast', [])
        details = []
        for cast in cast_list:
            order = cast.get('order')
            if order < 10:
                details.append({
                    'cast_id': cast.get('cast_id'),
                    'movie_id': movie_id,
                    'name': cast.get('name'),
                    'character': cast.get('character'),
                    'order': order
                })
        return details
    else:
        print(f"API 요청 실패: {response.status_code} (movie_id: {movie_id})")
        return []


# 데이터 수집 및 CSV 파일로 저장
def save_movie_details_to_csv(details_list, filename='movie_casts.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['cast_id', 'movie_id', 'name', 'character', 'order'])
        for details in details_list:
            writer.writerow([
                details['cast_id'],
                details['movie_id'],
                details['name'],
                details['character'],
                details['order']
            ])


if __name__ == "__main__":
    # 문제 a에서 생성된 movies.csv 파일을 기반으로 영화 ID 목록 가져오기
    with open('movies.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        movie_ids = [row['id'] for row in reader]
    details_list = []

    for movie_id in movie_ids:
        cast_details = fetch_movie_details(movie_id, API_KEY, BASE_URL)
        details_list.extend(cast_details)  # 여러 배우 정보 추가
    save_movie_details_to_csv(details_list)