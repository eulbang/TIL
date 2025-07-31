# arr 리스트에서 모든 부분 집합을 생성하는 코드
arr = [1, 2, 3]
n = len(arr) 
subset_cnt = 2 ** n # 생성 가능한 부분 집합의 총 개수
subsets = [] # 모든 부분 집합을 저장할 리스트

for i in range(subset_cnt): # 모든 가능한 부분 집합을 생성하기 위한 반복문
    subset = [] # 현재 부분 집합을 저장할 리스트
    for j in range(n): # 각 요소에 대해 포함 여부를 결정하기 위한 반복문
        if i & (1 << j): # i의 j번째 비트가 1인지 확인
            subset.append(arr[j])
    subsets.append(subset)
    
print(subsets)