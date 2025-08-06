import sys
sys.stdin = open('input1.txt')
sys.setrecursionlimit(10000)

def dfs(x, y, dx, dy):
    if not (0 <= x < N and 0 <= y < M):
        return 0
    if area[x][y] == 0:
        return 0
    return 1 + dfs(x + dx, y + dy, dx, dy)

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    for x in range(N):
        for y in range(M):
            if area[x][y] == 1:
                mx = max(mx, dfs(x, y, 0, 1))
                mx = max(mx, dfs(x, y, 1, 0))

    print(f"#{test_case} {mx}")