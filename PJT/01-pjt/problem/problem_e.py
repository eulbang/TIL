# TMDB API 키 설정

# movie 정보를 로드하는 함수 (problem_a.py의 결과 활용)

# 리뷰 정보를 로드하는 함수 (problem_c.py의 결과 활용)

# API를 사용하여 영화 평점 정보 가져오기

# 영화 평점 데이터 처리 함수

# 데이터 수집 및 CSV 파일로 저장

import csv
import requests

API_KEY = '592fb26f18bc0eefbb816fc25884f862'
BASE_URL = 'https://api.themoviedb.org/3/'

def load_movie_ids(filename='movies.csv'):
    movie_ids = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie_ids.append(row['id'])
    return movie_ids

def load_reviews(filename='movie_reviews.csv'):
    reviews = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                rating = float(row['rating'])
            except (ValueError, TypeError):
                rating = None
            reviews.append({'movie_id': row['movie_id'], 'rating': rating})
    return reviews

def fetch_rating_stats(movie_id, api_key, base_url):
    url = f"{base_url}movie/{movie_id}"
    params = {'api_key': api_key, 'language': 'ko-KR'}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get('vote_average'), data.get('vote_count')
    else:
        print(f"API 요청 실패: {response.status_code} (movie_id: {movie_id})")
        return None, None

def calculate_rating_distribution(reviews, movie_id):
    distribution = {str(i): 0 for i in range(1, 11)}
    for review in reviews:
        if review['movie_id'] == movie_id and review['rating'] is not None:
            rating_int = int(round(review['rating']))
            if 1 <= rating_int <= 10:
                distribution[str(rating_int)] += 1
    # 평점 분포를 "1:2,2:0,3:1,..." 형태의 문자열로 반환
    return ','.join([f"{i}:{distribution[str(i)]}" for i in range(5, 11)])

def save_rating_stats(stats, filename='movie_ratings.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['movie_id', 'average_rating', 'vote_count', 'rating_distribution'])
        for stat in stats:
            writer.writerow([
                stat['movie_id'],
                stat['average_rating'],
                stat['vote_count'],
                stat['rating_distribution']
            ])

if __name__ == "__main__":
    movie_ids = load_movie_ids()
    reviews = load_reviews()
    stats = []
    for movie_id in movie_ids:
        average_rating, vote_count = fetch_rating_stats(movie_id, API_KEY, BASE_URL)
        rating_distribution = calculate_rating_distribution(reviews, movie_id)
        stats.append({
            'movie_id': movie_id,
            'average_rating': average_rating,
            'vote_count': vote_count,
            'rating_distribution': rating_distribution
        })
    save_rating_stats(stats)