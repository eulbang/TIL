import sys
sys.stdin = open('sample_input.txt')

def calories_calculator(start, taste_subset, calory_sum):
    # print(sum(taste_subset))
    print(score)
    if calory_sum > L:
        return

    if 0 < calory_sum < L:
        score.append(sum(taste_subset))

    if calory_sum == L:
        score.append(sum(taste_subset))
        # return

    for idx in range(start, len(calories)):
        taste = tastes[idx]
        # calory = calories[idx]
        # calory_sum += calory
        taste_subset.append(taste)
        # print(f'맛 점수: {sum(taste_subset)}, 칼로리: {calory_sum}')
        calories_calculator(idx + 1, taste_subset, calory_sum + calories[idx])
        # calories_calculator(idx + 1, taste_subset, calory_sum)
        taste_subset.pop()
        # calory_sum -= calory

T = int(input())  # T : 테스트 케이스 수

for cnt in range(T):
    N, L = map(int, input().split())  # N : 재료의 수, L : 제한 칼로리
    tastes = []
    calories = []
    for _ in range(N):
        T, K = map(int, input().split())  # T : 맛에 대한 점수 , K : 칼로리
        tastes.append(T)
        calories.append(K)

score = []

calories_calculator(0, [], 0)
print(f'#{cnt + 1} {max(score)}')
