# TMDB API 키 설정

# 영화 ID 리스트를 movies.csv 파일에서 읽어옴

# API 호출 함수

# 리뷰 데이터 처리 함수

# 데이터 수집 및 CSV 파일로 저장

import requests
import csv

API_KEY = '592fb26f18bc0eefbb816fc25884f862'
BASE_URL = 'https://api.themoviedb.org/3/'

def read_movie_ids_from_csv(filename='movies.csv'):
    movie_ids = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie_ids.append(row['id'])
    return movie_ids

def fetch_reviews(movie_id, api_key, base_url, language='ko-KR', page=1):
    url = f"{base_url}movie/{movie_id}/reviews"
    params = {
        'api_key': api_key,
        'language': language,
        'page': page
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print(f"API 요청 실패: {response.status_code} (movie_id: {movie_id})")
        return []

def process_reviews(reviews, movie_id):
    filtered = []
    for review in reviews:
        rating = review.get('author_details', {}).get('rating')
        if rating is not None and rating >= 5:
            content = review.get('content')
            if not content or content.strip() == "":
                content = '내용 없음'
            filtered.append({
                'review_id': review.get('id'),
                'movie_id': movie_id,
                'author': review.get('author'),
                'content': content,
                'rating': rating
            })
    return filtered

def save_reviews_to_csv(reviews, filename='movie_reviews.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['review_id', 'movie_id', 'author', 'content', 'rating'])
        for review in reviews:
            writer.writerow([
                review['review_id'],
                review['movie_id'],
                review['author'],
                review['content'],
                review['rating']
            ])

if __name__ == "__main__":
    movie_ids = read_movie_ids_from_csv()
    all_reviews = []
    for movie_id in movie_ids:
        reviews = fetch_reviews(movie_id, API_KEY, BASE_URL)
        filtered = process_reviews(reviews, movie_id)
        all_reviews.extend(filtered)
    save_reviews_to_csv(all_reviews)