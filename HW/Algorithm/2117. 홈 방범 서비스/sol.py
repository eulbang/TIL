import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    houses = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 1]

    max_houses = 0
    for x in range(N):
        for y in range(N):
            for k in range(1, N+2):
                cnt = 0
                for (hx, hy) in houses:
                    if abs(x-hx) + abs(y-hy) < k:
                        cnt += 1
                if cnt * M >= k * k + (k-1) * (k-1):
                    max_houses = max(cnt, max_houses)

    print(f"#{test_case} {max_houses}")