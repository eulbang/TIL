# 요구사항 번호: F06

'''
수집된 데이터를 바탕으로 실질적인 분석을 수행하는 도전 
과제입니다. 각 영화의 예산(budget)과 수익(revenue) 정보를 활용하여, 
투자 대비 가장 높은 성과를 낸 영화가 무엇인지 수익률을 계산하고 
해당 영화를 찾아내는 기능을 구현합니다. 
'''

import csv
def calculate_roi(file_name='movie_details.csv'):
    with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # movies = [row for row in reader]
        # roi = (revenue - budget) / budget
        roi_list = []

        for row in reader:
            movie_id = row['movie_id']
            budget = int(row['budget']) if row['budget'] else 0
            revenue = int(row['revenue']) if row['revenue'] else 0
            if budget > 0:  # 예산이 0보다 큰 경우에만
                roi = (revenue - budget) / budget
                roi_list.append((movie_id, roi))
            else:
                roi_list.append((movie_id, None))

    roi_list.sort(key=lambda x: x[1] if x[1] is not None else float('-inf'), reverse=True)
    return roi_list

if __name__ == "__main__":
    roi_list = calculate_roi()
    # 수익률이 가장 높은 영화 찾기
    # max_roi_movie = max(roi_list, key=lambda x: x[1] if x[1] is not None else float('-inf'))
    max_roi_movie = roi_list[0]
    with open('movies.csv', mode ='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == max_roi_movie[0]:
                print(f"가장 높은 수익률 ({max_roi_movie[1]:.2f}) 을 기록한 영화: {row}")
                break
    # print(f"가장 높은 수익률을 기록한 영화 ID: {max_roi_movie[0]}, 수익률: {max_roi_movie[1]:.2f}")
            