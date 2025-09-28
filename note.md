data_analysis_ws_2_1
``` py
import pandas as pd

# ===================== 1. 데이터 로드 =====================
# CSV 파일을 읽어와 데이터프레임 생성
file_path = '../data/customer_data.csv'  # 파일 경로 지정
customer_data = pd.read_csv(file_path)  # CSV 파일 로드
# ===================== 3. 결측치 처리 =====================
# dropna(): 결측치(NaN)가 있는 행을 제거하여 데이터 정제
customer_data = customer_data.dropna()

# 결측치 제거 후 데이터 크기 출력
print(f"결측치 제거 후 데이터셋 크기: {customer_data.shape}")  
# shape: (행, 열) 형태의 데이터 크기 출력

# ===================== 4. 이상치 탐지 및 처리 =====================
# 이상치를 탐지하기 위해 IQR(Interquartile Range, 사분위 범위) 방법 사용
for column in ['Age', 'AnnualIncome']:  # 이상치를 탐지할 컬럼 선택
    Q1 = customer_data[column].quantile(0.25)  # 1사분위(Q1, 25% 지점)
    Q3 = customer_data[column].quantile(0.75)  # 3사분위(Q3, 75% 지점)
    IQR = Q3 - Q1  # 사분위 범위 (IQR = Q3 - Q1)

    # 이상치 경계값 설정
    lower_bound = Q1 - 1.5 * IQR  # 하한값: Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR  # 상한값: Q3 + 1.5 * IQR

    # 기존 데이터 크기 저장
    initial_shape = customer_data.shape  

    # 이상치를 제거한 데이터프레임 생성 (lower_bound보다 크거나 upper_bound보다 작은 데이터만 남김)
    customer_data = customer_data[(customer_data[column] >= lower_bound) & (customer_data[column] <= upper_bound)]

    # 이상치 처리 전후 데이터 크기 출력
    print(f"{column} 이상치 처리 전후 데이터셋 크기: {initial_shape} -> {customer_data.shape}")
```

data_analysis_ws_2_2
``` py
# 필요한 라이브러리 불러오기
import pandas as pd

# ===================== 1. 데이터 로드 =====================
# 캠페인 데이터 파일 경로 설정
campaign_file_path = "../data/campaign_data.csv"

# CSV 파일을 데이터프레임으로 로드
df_campaign = pd.read_csv(campaign_file_path)
# ===================== 2. 데이터 확인 =====================
# 데이터프레임 기본 정보 출력
print("=== 캠페인 데이터 정보 ===")
print(df_campaign.info())  # 데이터프레임의 구조 및 컬럼 정보 확인

# 데이터의 상위 5개 행 출력
print("\n=== 캠페인 데이터 샘플 ===")
print(df_campaign.head())  # 데이터의 상위 5개 행을 출력하여 확인

# ===================== 3. 결측치 처리 =====================
# 각 컬럼별 결측치 개수 확인
print("\n=== 결측치 개수 확인 ===")
print(df_campaign.isna().sum())  # 모든 컬럼의 결측치 개수 출력

# 결측치가 있는 경우 제거 (현재 데이터에는 결측치 없음)
df_campaign = df_campaign.dropna()

# ===================== 4. 캠페인 참여율 분석 =====================
# 전체 캠페인 고객 수 계산
total_customers = df_campaign.shape[0]  # 전체 고객 수

# 캠페인 참여 고객 수 계산
participating_customers = df_campaign[df_campaign["Participation"]==1].shape[0]  # 캠페인 참여 고객 수

# 캠페인 참여율 계산
participation_rate = (participating_customers / total_customers) * 100  # 백분율 변환

# 캠페인 참여율 출력
print("\n=== 캠페인 참여율 분석 ===")
print(f"전체 고객 수: {total_customers}명")
print(f"캠페인 참여 고객 수: {participating_customers}명")
print(f"캠페인 참여율: {participation_rate:.2f}%")

# ===================== 5. 캠페인 참여 여부에 따른 매출 비교 =====================
# 캠페인 참여 고객과 비참여 고객의 평균 매출 계산
avg_revenue_participation = df_campaign[df_campaign["Participation"] == 1]["Revenue"].mean()  # 참여 고객 평균 매출
avg_revenue_non_participation = df_campaign[df_campaign["Participation"] == 0]["Revenue"].mean()  # 비참여 고객 평균 매출

# 평균 매출 비교 출력
print("\n=== 캠페인 참여 여부에 따른 평균 매출 비교 ===")
print(f"캠페인 참여 고객 평균 매출: {avg_revenue_participation:.2f}")
print(f"캠페인 비참여 고객 평균 매출: {avg_revenue_non_participation:.2f}")

# ===================== 6. 캠페인별 평균 매출 분석 =====================
# 각 캠페인별 평균 매출 계산
df_campaign_revenue = df_campaign.groupby("CampaignID")["Revenue"].mean().reset_index()

# 컬럼명 변경 (캠페인별 평균 매출)
df_campaign_revenue.rename(columns={"Revenue": "AvgRevenue"}, inplace=True)

# 캠페인별 평균 매출 출력
print("\n=== 캠페인별 평균 매출 분석 ===")
df_campaign_revenue

# ===================== 7. 캠페인별 클릭 수 및 매출 비교 =====================
# 각 캠페인별 평균 클릭 수 및 평균 매출 계산
df_campaign_clicks_revenue = df_campaign.groupby("CampaignID")[["Clicks", "Revenue"]].mean().reset_index()

# 컬럼명 변경 (캠페인별 평균 클릭 수 및 매출)
df_campaign_clicks_revenue.rename(columns={"Clicks": "AvgClicks", "Revenue": "AvgRevenue"}, inplace=True)

# 캠페인별 평균 클릭 수 및 매출 출력
print("\n=== 캠페인별 평균 클릭 수 및 매출 분석 ===")
df_campaign_clicks_revenue
```

data_analysis_ws_2_3
``` py
# 필요한 라이브러리 불러오기
import pandas as pd

# ===================== 1. 데이터 로드 =====================
# 판매 데이터 파일 경로 설정
sales_file_path = "../data/sales_data.csv"

# CSV 파일을 데이터프레임으로 로드
df_sales = pd.read_csv(sales_file_path)

# ===================== 2. 데이터 확인 =====================
# 데이터프레임 기본 정보 출력
print("=== 판매 데이터 정보 ===")
df_sales.info()  # 컬럼 정보 및 데이터 타입 확인

# 데이터의 상위 5개 행 출력
print("\n=== 판매 데이터 샘플 ===")
df_sales.head()

# ===================== 3. 결측치 처리 =====================
# 각 컬럼별 결측치 개수 확인
print("\n=== 결측치 개수 확인 ===")
print(df_sales.isna().sum())  # 각 컬럼의 결측치 개수 확인

# 결측치가 있는 경우 제거 (현재 데이터에는 결측치 없음)
df_sales = df_sales.dropna()

# ===================== 4. 총 매출(Total Sales) 컬럼 생성 =====================
# 총 매출(TotalSales) = 가격(Price) * 판매량(Quantity)
df_sales["TotalSales"] = df_sales["Price"] * df_sales["Quantity"]

# 총 매출 컬럼이 추가된 데이터 확인
print("\n=== 총 매출(TotalSales) 컬럼 추가 후 데이터 확인 ===")
print(df_sales.head())

# ===================== 5. 제품별 가격과 판매량 분석 =====================
# 제품별 평균 가격 계산
df_avg_price = df_sales.groupby("Product")["Price"].mean().reset_index()

# 제품별 평균 판매량 계산
df_avg_quantity = df_sales.groupby("Product")["Quantity"].mean().reset_index()

# 제품별 평균 가격과 평균 판매량 데이터 병합
df_product_analysis = pd.merge(df_avg_price, df_avg_quantity, on="Product")

# 제품별 평균 가격과 평균 판매량 출력
print("\n=== 제품별 평균 가격과 평균 판매량 분석 ===")
print(df_product_analysis)

# ===================== 6. 가격과 판매량 간의 상관관계 계산 =====================
# --------------------------------------------------------------
# [상관관계란?]
# - 두 변수 간의 관계가 얼마나 밀접한지를 나타내는 통계적 지표
# - 상관계수(correlation coefficient)는 -1 ~ 1 사이의 값을 가짐
# 
# 
# 상관계수 해석:
#   -  1.0  : 완전한 양의 상관관계 (가격이 오르면 판매량도 반드시 오름)
#   -  0.0  : 상관관계 없음 (가격과 판매량은 무관함)
#   - -1.0 : 완전한 음의 상관관계 (가격이 오르면 판매량은 반드시 떨어짐)
# 
# 
# 예시:
#   - 상관계수 -0.85: 가격이 오를수록 판매량이 확실히 줄어드는 패턴
#   - 상관계수 +0.60: 가격이 오르면 판매량도 어느 정도 함께 오르는 경향

# 주의할 점:
#   - 이 상관계수는 선형 관계(linear relationship)만 측정합니다.
#   - 만약 두 변수 사이가 곡선(비선형) 관계라면, 상관계수가 0 근처라도 실제로는 관련이 있을 수 있습니다.
#   - 따라서 상관계수만 보고 관계 유무를 단정하면 안 되고, 시각화(산점도) 등을 함께 보는 것이 좋습니다.
# --------------------------------------------------------------


# 전체 데이터에서 가격과 판매량 간의 상관계수 계산
correlation = df_sales[["Price", "Quantity"]].corr()

# 상관계수 출력
print("\n=== 가격과 판매량 간의 상관관계 분석 ===")
print(correlation)

# ===================== 7. 제품별 상관관계 분석 =====================
# 제품별 가격과 판매량의 상관계수 계산
df_product_corr = df_sales.groupby("Product")[["Price", "Quantity"]].corr()

# 데이터 변환 과정 설명:
# 1. groupby("Product")로 제품별 데이터를 그룹화한 후 Price와 Quantity 간의 상관관계를 계산함
# 2. corr() 함수는 기본적으로 두 변수 간의 상관계수를 포함하는 **멀티 인덱스(multi-index) 형태**의 DataFrame을 반환함
# 3. unstack()을 사용하면 멀티 인덱스 형태에서 **행을 확장(flatten)하여 단순한 형태의 데이터프레임으로 변환** 가능
# 4. unstack() 후, 필요한 상관계수 값을 가져오기 위해 `iloc[:, 1]`을 사용하여 Price와 Quantity 간의 상관계수를 추출

df_product_corr = df_product_corr.unstack().iloc[:, 1]  # Price와 Quantity 간의 상관계수만 추출

# 제품별 가격과 판매량의 상관계수 출력
print("\n=== 제품별 가격과 판매량 간의 상관관계 분석 ===")
print(df_product_corr)
```

data_analysis_ws_2_4
``` py
# 필요한 라이브러리 불러오기
import pandas as pd

# ===================== 1. 데이터 로드 =====================
# 각 데이터 파일 경로 설정
purchase_file_path = "../data/purchase_history.csv"
survey_file_path = "../data/satisfaction_survey.csv"

# CSV 파일을 데이터프레임으로 로드
df_purchase = pd.read_csv(purchase_file_path)
df_survey = pd.read_csv(survey_file_path)

# ===================== 2. 데이터 확인 =====================
# 데이터프레임 기본 정보 출력
print("=== 구매 이력 데이터 정보 ===")
print(df_purchase.dtypes)  # 컬럼 정보 및 데이터 타입 확인

print("\n=== 고객 만족도 설문 데이터 정보 ===")
print(df_survey.dtypes)  # 컬럼 정보 및 데이터 타입 확인

# 데이터의 상위 5개 행 출력
print("\n=== 구매 이력 데이터 샘플 ===")
print(df_purchase.head())

print("\n=== 고객 만족도 설문 데이터 샘플 ===")
print(df_survey.head())

# ===================== 3. 데이터 병합 =====================
# 두 데이터셋을 CustomerID를 기준으로 병합
df_merged = pd.merge(df_purchase, df_survey, on="CustomerID")

# 병합된 데이터 확인
print("\n=== 병합된 데이터 확인 ===")
print(df_merged.info())

# ===================== 4. 결측치 처리 =====================
# 각 컬럼별 결측치 개수 확인
print("\n=== 결측치 개수 확인 ===")
print(df_merged.isna().sum())  # 결측치 개수 출력

# 결측치가 없는 경우 그대로 사용, 결측치가 있다면 제거 또는 적절한 값으로 대체
df_merged = df_merged.fillna(df_merged.median(numeric_only=True))

# 결측치 처리 후 데이터 확인
print("\n=== 결측치 처리 후 데이터 크기 ===")
print(df_merged.shape)  # 데이터 크기 확인

# ===================== 5. 고객 세분화 (구매 이력 기반) =====================
# 구매 횟수(PurchaseHistory)를 기준으로 고객을 세 그룹으로 나누기
# 구매 횟수가 10 이하: 'Low'
# 구매 횟수가 11~30: 'Medium'
# 구매 횟수가 31 이상: 'High'
def categorize_purchase_history(purchase_count):
    if purchase_count <= 10:
        return 'Low'
    elif purchase_count <= 30:
        return 'Medium'
    else:
        return 'High'

df_merged["PurchaseCategory"] = df_merged["PurchaseHistory"].apply(categorize_purchase_history)

# 고객 세분화 결과 확인
print("\n=== 구매 횟수 기반 고객 세분화 결과 ===")
print(df_merged["PurchaseCategory"].value_counts())  # 각 그룹별 고객 수 확인

# ===================== 6. 고객 만족도 기반 세분화 =====================
# 만족도 점수(Satisfaction)를 기준으로 고객을 세 그룹으로 나누기
# 만족도 1~3: 'Low'
# 만족도 4~7: 'Medium'
# 만족도 8~10: 'High'
def categorize_satisfaction(satisfaction_score):
    if satisfaction_score <= 3:
        return 'Low'
    elif satisfaction_score <= 7:
        return 'Medium'
    else:
        return 'High'

df_merged["SatisfactionCategory"] = df_merged["Satisfaction"].apply(categorize_satisfaction)

# 고객 만족도 세분화 결과 확인
print("\n=== 고객 만족도 기반 세분화 결과 ===")
print(df_merged["SatisfactionCategory"].value_counts())  # 각 그룹별 고객 수 확인

# ===================== 7. 각 그룹별 평균 구매 금액 분석 =====================
# 구매 카테고리별 평균 총 지출 금액 분석
df_purchase_analysis = df_merged.groupby("PurchaseCategory")["TotalSpent"].mean().reset_index()
df_purchase_analysis.rename(columns={"TotalSpent": "AvgSpent"}, inplace=True)

# 구매 카테고리별 평균 지출 금액 출력
print("\n=== 구매 카테고리별 평균 지출 금액 분석 ===")
print(df_purchase_analysis)

# 만족도 카테고리별 평균 총 지출 금액 분석
df_satisfaction_analysis = df_merged.groupby("SatisfactionCategory")["TotalSpent"].mean().reset_index()
df_satisfaction_analysis.rename(columns={"TotalSpent": "AvgSpent"}, inplace=True)

# 만족도 카테고리별 평균 지출 금액 출력
print("\n=== 만족도 카테고리별 평균 지출 금액 분석 ===")
print(df_satisfaction_analysis)

# ===================== 8. 구매 카테고리와 만족도 카테고리 간의 관계 분석 =====================
# 구매 카테고리별 고객 만족도 분포 확인
df_category_relation = df_merged.groupby(["PurchaseCategory", "SatisfactionCategory"])["CustomerID"].count().reset_index()
df_category_relation.rename(columns={"CustomerID": "CustomerCount"}, inplace=True)

# 관계 분석 결과 출력
print("\n=== 구매 카테고리와 만족도 카테고리 간의 관계 분석 ===")
print(df_category_relation)

# ===================== 9. 데이터 저장 =====================
# 분석된 데이터를 CSV 파일로 저장
df_merged.to_csv("../data/segmented_customer_data.csv", index=False)
df_purchase_analysis.to_csv("../data/purchase_category_analysis.csv", index=False)
df_satisfaction_analysis.to_csv("../data/satisfaction_category_analysis.csv", index=False)
df_category_relation.to_csv("../data/category_relation_analysis.csv", index=False)

print("\n=== 분석된 데이터 저장 완료 ===")
```

data_analysis_ws_2_5
``` py
# 필요한 라이브러리 불러오기
import pandas as pd

# ===================== 1. 데이터 로드 =====================
# 각 데이터 파일 경로 설정
purchase_file_path = "../data/purchase_history.csv"
survey_file_path = "../data/satisfaction_survey.csv"

# CSV 파일을 데이터프레임으로 로드
df_purchase = pd.read_csv(purchase_file_path)
df_survey = pd.read_csv(survey_file_path)

# ===================== 2. 데이터 확인 =====================
# 데이터프레임 기본 정보 출력
print("=== 구매 이력 데이터 정보 ===")
print(df_purchase.dtypes)  # 컬럼 정보 및 데이터 타입 확인

print("\n=== 고객 만족도 설문 데이터 정보 ===")
print(df_survey.dtypes)  # 컬럼 정보 및 데이터 타입 확인

# 데이터의 상위 5개 행 출력
print("\n=== 구매 이력 데이터 샘플 ===")
print(df_purchase.head())

print("\n=== 고객 만족도 설문 데이터 샘플 ===")
print(df_survey.head())

# ===================== 3. 데이터 병합 =====================
# 두 데이터셋을 CustomerID를 기준으로 병합
df_merged = pd.merge(df_purchase, df_survey, on="CustomerID")

# 병합된 데이터 확인
print("\n=== 병합된 데이터 확인 ===")
print(df_merged.info())

# ===================== 4. 결측치 처리 =====================
# 각 컬럼별 결측치 개수 확인
print("\n=== 결측치 개수 확인 ===")
print(df_merged.isna().sum())  # 결측치 개수 출력

# 결측치가 없는 경우 그대로 사용, 결측치가 있다면 제거 또는 적절한 값으로 대체
df_merged = df_merged.fillna(df_merged.median(numeric_only=True))

# 결측치 처리 후 데이터 확인
print("\n=== 결측치 처리 후 데이터 크기 ===")
print(df_merged.shape)  # 데이터 크기 확인

# ===================== 5. 고객 세분화 (구매 이력 기반) =====================
# 구매 횟수(PurchaseHistory)를 기준으로 고객을 세 그룹으로 나누기
# 구매 횟수가 10 이하: 'Low'
# 구매 횟수가 11~30: 'Medium'
# 구매 횟수가 31 이상: 'High'
def categorize_purchase_history(purchase_count):
    if purchase_count <= 10:
        return 'Low'
    elif purchase_count <= 30:
        return 'Medium'
    else:
        return 'High'

df_merged["PurchaseCategory"] = df_merged["PurchaseHistory"].apply(categorize_purchase_history)

# 고객 세분화 결과 확인
print("\n=== 구매 횟수 기반 고객 세분화 결과 ===")
print(df_merged["PurchaseCategory"].value_counts())  # 각 그룹별 고객 수 확인

# ===================== 6. 고객 만족도 기반 세분화 =====================
# 만족도 점수(Satisfaction)를 기준으로 고객을 세 그룹으로 나누기
# 만족도 1~3: 'Low'
# 만족도 4~7: 'Medium'
# 만족도 8~10: 'High'
def categorize_satisfaction(satisfaction_score):
    if satisfaction_score <= 3:
        return 'Low'
    elif satisfaction_score <= 7:
        return 'Medium'
    else:
        return 'High'

df_merged["SatisfactionCategory"] = df_merged["Satisfaction"].apply(categorize_satisfaction)

# 고객 만족도 세분화 결과 확인
print("\n=== 고객 만족도 기반 세분화 결과 ===")
print(df_merged["SatisfactionCategory"].value_counts())  # 각 그룹별 고객 수 확인

# ===================== 7. 각 그룹별 평균 구매 금액 분석 =====================
# 구매 카테고리별 평균 총 지출 금액 분석
df_purchase_analysis = df_merged.groupby("PurchaseCategory")["TotalSpent"].mean().reset_index()
df_purchase_analysis.rename(columns={"TotalSpent": "AvgSpent"}, inplace=True)

# 구매 카테고리별 평균 지출 금액 출력
print("\n=== 구매 카테고리별 평균 지출 금액 분석 ===")
print(df_purchase_analysis)

# 만족도 카테고리별 평균 총 지출 금액 분석
df_satisfaction_analysis = df_merged.groupby("SatisfactionCategory")["TotalSpent"].mean().reset_index()
df_satisfaction_analysis.rename(columns={"TotalSpent": "AvgSpent"}, inplace=True)

# 만족도 카테고리별 평균 지출 금액 출력
print("\n=== 만족도 카테고리별 평균 지출 금액 분석 ===")
print(df_satisfaction_analysis)

# ===================== 8. 구매 카테고리와 만족도 카테고리 간의 관계 분석 =====================
# 구매 카테고리별 고객 만족도 분포 확인
df_category_relation = df_merged.groupby(["PurchaseCategory", "SatisfactionCategory"])["CustomerID"].count().reset_index()
df_category_relation.rename(columns={"CustomerID": "CustomerCount"}, inplace=True)

# 관계 분석 결과 출력
print("\n=== 구매 카테고리와 만족도 카테고리 간의 관계 분석 ===")
print(df_category_relation)

# ===================== 9. 데이터 저장 =====================
# 분석된 데이터를 CSV 파일로 저장
df_merged.to_csv("../data/segmented_customer_data.csv", index=False)
df_purchase_analysis.to_csv("../data/purchase_category_analysis.csv", index=False)
df_satisfaction_analysis.to_csv("../data/satisfaction_category_analysis.csv", index=False)
df_category_relation.to_csv("../data/category_relation_analysis.csv", index=False)

print("\n=== 분석된 데이터 저장 완료 ===")
```

data_science1_ws_4_1
``` py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.family'] = 'Malgun Gothic'

# 1. 데이터 불러오기 및 기본 탐색
# 주어진 영화 데이터 파일을 불러온다.
file_path = "../data/movie_data.csv"  # 실제 데이터 파일 경로
df = pd.read_csv(file_path)  # 데이터를 불러오는 코드 작성

# 데이터의 첫 5행 출력 (EDA의 첫 단계)
print("데이터 미리보기")
df.head()  # 데이터의 처음 몇 개의 행을 출력하는 코드 작성

# 데이터의 기본 정보 확인 (컬럼명, 데이터 타입, 결측값 확인)
print("\n데이터 정보")
df.info()  # 데이터프레임의 정보를 출력하는 코드 작성

# 2. 필요한 컬럼 선택 및 데이터 변환
# 'Director' (감독) 컬럼과 'Rating' (평점) 컬럼이 존재한다고 가정하고, 필요한 컬럼만 선택
df = df[['Director', 'Rating']].dropna()  # 감독과 평점 데이터가 없는 경우 제거

# 3. 특정 감독의 영화 데이터 필터링
# 특정 감독의 이름을 설정 (예: 크리스토퍼 놀란)
target_director = "Christopher Nolan"

# 감독명이 target_director인 영화만 필터링
director_movies = df[df['Director'] == target_director]

# 4. 데이터 시각화: 특정 감독의 영화 평점 분포
plt.figure(figsize=(10, 6))  # 그래프 크기 설정

# 특정 감독의 영화 평점 데이터를 히스토그램으로 표현하는 코드 작성
sns.histplot(df["Rating"], bins=10, kde=True, color='blue', alpha=0.7)

# 그래프 제목 및 라벨 설정
plt.title(f'{target_director} 영화의 평점 분포')
plt.xlabel('평점')
plt.ylabel('영화 개수')
plt.grid(True)  # 격자 추가

# 그래프 출력
plt.show()

# 5. 결과 해석
# 특정 감독(예: 크리스토퍼 놀란)의 영화 평점 분포를 분석한다.
# 그래프를 통해 해당 감독의 영화가 높은 평점을 많이 받았는지, 평점이 고르게 분포하는지 확인할 수 있다.
# KDE(Kernel Density Estimate) 곡선을 통해 평점 분포의 밀도를 확인할 수 있다.
# 특정 평점대(예: 8.0 이상)에 집중되어 있다면, 해당 감독이 대체로 좋은 평가를 받는다고 해석할 수 있다.
# 반대로 평점이 다양하게 분포되어 있다면, 감독의 영화 스타일이 작품마다 평가가 다를 가능성이 있다.
```

data_science1_ws_4_2
``` py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.family'] = 'Malgun Gothic'

# 1. 데이터 불러오기 및 기본 탐색
# 주어진 지하철 데이터 파일을 불러온다.
file_path = "../data/subway_data.csv"  # 실제 데이터 파일 경로
df = pd.read_csv(file_path)

# 데이터의 첫 5행 출력 (EDA의 첫 단계)
print("데이터 미리보기")
df.head()

# 데이터의 기본 정보 확인 (컬럼명, 데이터 타입, 결측값 확인)
print("\n데이터 정보")
df.info()

# 2. 필요한 컬럼 선택 및 데이터 변환
# 'Date' (날짜), 'Station' (지하철역), 'Passengers' (승객 수) 컬럼이 존재한다고 가정하고, 필요한 컬럼만 선택
df = df[["Date", "Station", "Passengers"]].dropna()  # 날짜, 역, 승객 수 데이터가 없는 경우 제거

# 'Date' 컬럼을 날짜 형식으로 변환하여 요일 정보 추출
df['Date'] = pd.to_datetime(df["Date"])  # 날짜 데이터를 datetime 형식으로 변환
df['Weekday'] = df['Date'].dt.day_name()  # 요일(월요일~일요일) 정보 추가

# 3. 요일별 평균 승객 수 분석
# 요일별 평균 승객 수를 계산하여 새로운 데이터프레임 생성
# 'Weekday'를 기준으로 'Passengers'의 평균을 계산하는 코드 작성
weekday_avg_passengers = df.groupby("Weekday")['Passengers'].mean().reset_index()

# 요일별 데이터를 정렬 (월요일~일요일 순서)
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_avg_passengers['Weekday'] = pd.Categorical(weekday_avg_passengers['Weekday'], categories=weekday_order, ordered=True)
weekday_avg_passengers = weekday_avg_passengers.sort_values('Weekday') # 요일 기준으로 정렬하는 코드 작성

# 4. 가장 승객 수가 많은 요일 찾기
# 가장 평균 승객 수가 많은 요일을 찾는 코드 작성
busiest_day = weekday_avg_passengers.loc[weekday_avg_passengers["Passengers"].idxmax()]

print("\n가장 평균 승객 수가 많은 요일:")
busiest_day

# 5. 데이터 시각화 (요일별 평균 승객 수 비교)
plt.figure(figsize=(10, 6))
sns.barplot(data=weekday_avg_passengers, x='Weekday', y='Passengers', palette='viridis')
# Seaborn의 barplot을 사용하여 요일별 평균 승객 수를 시각화하는 코드 작성

# 그래프 제목 및 라벨 설정
plt.title('요일별 평균 승객 수')
plt.xlabel('요일')
plt.ylabel('평균 승객 수')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 그래프 출력
plt.show()

# 6. 결과 해석
## 1. 특정 요일별로 평균 승객 수를 분석하여 가장 붐비는 요일을 찾았다.
## 2. 전체적으로 주중(월요일~금요일)이 주말보다 승객 수가 많을 가능성이 높음.
## 3. 가장 승객 수가 많은 요일이 금요일이라면, 이는 출퇴근 및 여가 활동이 겹치는 영향을 받을 가능성이 있음.
## 4. 주말의 경우(토요일, 일요일)는 상대적으로 승객 수가 감소할 수 있으며, 특정 관광지가 포함된 역은 예외일 수 있음.
## 5. 가장 붐비는 요일의 역별 승객 수를 추가적으로 분석하여, 특정 역이 평균을 끌어올리는지 확인할 필요가 있음.
```

data_science1_ws_4_3
``` py
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

# 1. 데이터 불러오기 및 기본 탐색
# 주어진 주식 데이터 파일을 불러온다.
file_path = "../data/stock_data.csv"  # 실제 데이터 파일 경로
df = pd.read_csv(file_path)

# 데이터의 첫 5행 출력 (EDA의 첫 단계)
print("데이터 미리보기")
df.head()

# 데이터의 기본 정보 확인 (컬럼명, 데이터 타입, 결측값 확인)
print("\n데이터 정보")
df.info()

# 2. 필요한 컬럼 선택 및 데이터 변환
# 'Date' (날짜), 'Close' (종가) 컬럼을 선택
df = df[["Date", "Close"]].dropna()  # 날짜 및 종가 데이터가 없는 경우 제거

# 'Date' 컬럼을 날짜 형식으로 변환
df['Date'] = pd.to_datetime(df["Date"])  # 날짜 데이터를 datetime 형식으로 변환

# 날짜 기준으로 정렬
df = df.sort_values(by='Date')

# 3. 이동 평균선 계산 (새로운 컬럼 만들기)
# 단기 이동 평균선 (5일)
df['MA5'] = df['Close'].rolling(window=5).mean()  # 5일 이동 평균선 계산

# 중기 이동 평균선 (20일)
df['MA20'] = df['Close'].rolling(window=20).mean()  #20일 이동 평균선 계산

# 장기 이동 평균선 (60일)
df['MA60'] = df['Close'].rolling(window=60).mean()  # 60일 이동 평균선 계산

# 4. 특정 구간 강조 (이동 평균선이 교차하는 구간)
# 이동 평균선이 교차하는 특정 구간을 찾기 위해, MA5와 MA20의 차이를 계산
df['Crossover'] = df['MA5'] - df['MA20'] # 이동 평균선 차이를 계산하는 코드 작성

# 교차점: MA5가 MA20을 상향 돌파하는 경우 (골든크로스)
golden_cross = df[(df['Crossover'] > 0) & (df['Crossover'].shift(1) < 0)]

# 교차점: MA5가 MA20을 하향 돌파하는 경우 (데드크로스)
death_cross = df[(df['Crossover'] < 0) & (df['Crossover'].shift(1) > 0)]

# 5. 데이터 시각화 (이동 평균선 및 특정 구간 강조)
plt.figure(figsize=(12, 6))

# 종가 그래프
plt.plot(df['Date'], df['Close'], label='종가', color='black', linewidth=1, alpha=0.7)

# 이동 평균선 그래프
plt.plot(df['Date'], df['MA5'], label='5일 이동 평균선', color='blue', linewidth=1)
plt.plot(df['Date'], df['MA20'], label='20일 이동 평균선', color='orange', linewidth=1)
plt.plot(df['Date'], df['MA60'], label='60일 이동 평균선', color='green', linewidth=1)

# 골든크로스 지점 강조
plt.scatter(golden_cross['Date'], golden_cross['Close'], color='red', label='골든크로스', marker='^', s=100)

# 데드크로스 지점 강조
plt.scatter(death_cross['Date'], death_cross['Close'], color='purple', label='데드크로스', marker='v', s=100)

# 그래프 제목 및 라벨 설정
plt.title('주식 데이터의 이동 평균선 분석 및 특정 구간 강조')
plt.xlabel('날짜')
plt.ylabel('주가')
plt.legend()
plt.grid(True)

# 그래프 출력
plt.show()

# 6. 결과 해석
# 1. 이동 평균선을 통해 주가의 흐름을 파악할 수 있다.
# 2. 5일 이동 평균선이 20일 이동 평균선을 상향 돌파하는 경우(골든크로스)는 상승 신호로 해석된다.
# 3. 반대로, 5일 이동 평균선이 20일 이동 평균선을 하향 돌파하는 경우(데드크로스)는 하락 신호로 해석된다.
# 4. 장기 이동 평균선(60일)을 함께 분석하면 주가의 장기적인 방향성을 이해하는 데 도움을 줄 수 있다.
# 5. 특정 구간에서의 교차점(골든크로스, 데드크로스)을 강조하여 투자 의사 결정을 지원할 수 있다.
```

data_science1_ws_4_4
``` py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.family'] = 'Malgun Gothic'

# 1. 데이터 불러오기 및 기본 탐색
# 주어진 매장 매출 데이터 파일을 불러온다.
file_path = "../data/store_sales.csv"  # 실제 데이터 파일 경로
df = pd.read_csv(file_path)

# 데이터의 첫 5행 출력 (EDA의 첫 단계)
print("데이터 미리보기")
df.head()

# 데이터의 기본 정보 확인 (컬럼명, 데이터 타입, 결측값 확인)
print("\n데이터 정보")
df.info()

# 2. 날짜 변환 및 연-월 데이터 생성
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m")  # 'Date' 컬럼을 datetime 형식으로 변환
df["YearMonth"] = df["Date"].dt.to_period("M")  # 연-월(YYYY-MM) 형식으로 변환하여 새로운 컬럼 생성

# 3. 월별 매출 집계
monthly_sales = df.groupby("YearMonth")["Revenue"].sum().reset_index()  # 'YearMonth' 기준으로 매출 합산
monthly_sales["YearMonth"] = monthly_sales["YearMonth"].astype(str)  # 문자열로 변환하여 시각화에서 오류 방지

# 4. 제품별 총 판매량 분석
product_sales = df.groupby("Product")["Quantity"].sum().reset_index()  # 'Product'별로 총 판매량 합산

# 5. 가장 많이 팔린 제품 상위 10개 선정
top_products = product_sales.sort_values(by="Quantity", ascending=False).head(10)  # 판매량 기준으로 내림차순 정렬 후 상위 10개 선택

# 6. 시각화 - 월별 매출 변화
plt.figure(figsize=(12, 6))  # 그래프 크기 설정
sns.lineplot(data=monthly_sales, x="YearMonth", y="Revenue", marker="o")  # 선 그래프(lineplot) 생성
plt.xticks(rotation=45)  # x축 라벨 45도 회전
plt.title("월별 매출 변화")  # 그래프 제목 설정
plt.xlabel("연-월")  # x축 레이블 설정
plt.ylabel("매출")  # y축 레이블 설정
plt.grid(True)  # 격자 추가
plt.show()  # 그래프 출력

# 7. 시각화 - 가장 많이 팔린 제품
plt.figure(figsize=(12, 6))  # 그래프 크기 설정
sns.barplot(data=top_products, x="Product", y="Quantity")  # 바 그래프(barplot) 생성
plt.xticks(rotation=45)  # x축 라벨 45도 회전
plt.title("가장 많이 팔린 제품 상위 10개")  # 그래프 제목 설정
plt.xlabel("제품")  # x축 레이블 설정
plt.ylabel("판매량")  # y축 레이블 설정
plt.show()  # 그래프 출력
```

data_science1_ws_4_5
``` py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.family'] = 'Malgun Gothic'

# 1. 데이터 불러오기 및 기본 탐색
# 주어진 영화 리뷰 데이터 파일을 불러온다.
file_path = "../data/movie_reviews.csv"  # 실제 데이터 파일 경로
df = pd.read_csv(file_path)

# 데이터의 첫 5행 출력 (EDA의 첫 단계)
print("데이터 미리보기")
df.head()

# 데이터의 기본 정보 확인 (컬럼명, 데이터 타입, 결측값 확인)
print("\n데이터 정보")
df.info()

# 2. 리뷰 길이 계산 및 새로운 컬럼 추가
# - 각 리뷰의 문자 길이를 계산하여 새로운 컬럼 'Review Length'를 생성합니다.
df["Review Length"] = df["Review"].apply(len)

# 3. 평점과 리뷰 길이의 관계 시각화
# - 박스 플롯을 사용하여 평점별 리뷰 길이의 분포를 시각화합니다.
# - 이를 통해 특정 평점에서 리뷰 길이가 더 긴 경향이 있는지 확인할 수 있습니다.
plt.figure(figsize=(10, 6))
sns.boxplot(x=df["Rating"], y=df["Review Length"])
plt.xlabel("Rating (평점)")
plt.ylabel("Review Length (리뷰 길이)")
plt.title("평점과 리뷰 길이의 관계")
plt.show()

# 4. 리뷰 길이의 분포 확인
# - 히스토그램과 KDE(커널 밀도 추정)를 사용하여 리뷰 길이의 분포를 확인합니다.
# - 리뷰 길이의 평균과 편차를 시각적으로 파악할 수 있습니다.
plt.figure(figsize=(10, 6))
sns.histplot(df["Review Length"], bins=30, kde=True)
plt.xlabel("Review Length (리뷰 길이)")
plt.ylabel("Count (개수)")
plt.title("리뷰 길이 분포")
plt.show()

# 5. 장문 리뷰 필터링 (상위 25% 이상의 길이를 가진 리뷰)
# - 전체 리뷰 길이 데이터에서 75번째 백분위수(Q3)를 계산합니다.
# - Q3 이상인 리뷰를 '장문 리뷰'로 간주하여 필터링합니다.
long_review_threshold = df["Review Length"].quantile(0.75)  # 75% 백분위수
long_reviews = df[df["Review Length"] >= long_review_threshold]

# 6. 필터링된 장문 리뷰 개수 및 샘플 출력
# - 장문 리뷰의 개수를 출력하여 얼마나 많은 리뷰가 해당하는지 확인합니다.
print(f"장문 리뷰 개수: {long_reviews.shape[0]}")

# - 일부 장문 리뷰 샘플을 출력하여 필터링이 잘 되었는지 확인합니다.
print("\n장문 리뷰 샘플:")
long_reviews.head()
```