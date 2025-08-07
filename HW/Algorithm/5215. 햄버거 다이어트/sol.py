import sys
sys.stdin = open('sample_input.txt')

def dfs(idx, sum_taste, sum_cal):
    global best

    if sum_cal > L:
        return

    if sum_taste > best:
        best = sum_taste

    for i in range(idx, len(ingredients)):  # idx+1 왜안됨?;
        print(f'인덱스:{i} 재료:{ingredients[i]} 맛:{sum_taste} 칼로리:{sum_cal}')
        dfs(i+1, sum_taste + ingredients[i][0], sum_cal + ingredients[i][1])

    return best

T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())

    ingredients = []
    for i in range(N):
        taste, cal = map(int, input().split())
        ingredients.append([taste, cal])

    best = 0
    print(f"#{test_case} {dfs(0, 0, 0)}")
