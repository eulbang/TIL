import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    crops = 0
    for x in range(N):
        for y in range(N):
            if (x + y >= N // 2) and (N-1-x + y >= N // 2) and (x + N-1-y >= N//2) and (N-1-x + N-1-y >= N // 2):
                crops += farm[x][y]

    print(f'#{test_case} {crops}')