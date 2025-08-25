import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    goods = [list(map(int, input().split())) for _ in range(M)]

    K = [[0 for _ in range(N+1)] for _ in range(M+1)]

    for i in range(1, M+1):
        for w in range(1, N+1):
            if goods[i-1][0] > w:
                K[i][w] = K[i-1][w]
            else:
                K[i][w] = max(goods[i-1][1] + K[i-1][w-goods[i-1][0]], K[i-1][w])

    print(f"#{test_case} {K[M][N]}")