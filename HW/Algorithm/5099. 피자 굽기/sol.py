import sys
sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pizza_input = list(map(int, input().split()))

    pizza = deque((i + 1, cheese) for i, cheese in enumerate(pizza_input))  # 피자번호, 치즈양
    oven = deque()

    for _ in range(N):  # 화덕에 피자 투입
        oven.append(pizza.popleft())

    while len(oven) > 1:    # 피자가 한 개 남을 때까지
        num, cheese = oven.popleft()
        cheese //= 2  # 치즈 절반으로

        if cheese == 0:
            if pizza:
                oven.append(pizza.popleft())
        else:
            oven.append((num, cheese))

    print(f"#{test_case} {oven[0][0]}") # 남은 마지막 피자 번호