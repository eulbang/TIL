from collections import deque
import sys
input = sys.stdin.readline

def dfs(area, cnt):
    global N, M

    if cnt >= 3:
        for i in range(N):
            for j in range(M):
                if area[i][j] == 2:
                    pass
        return

    for y in range(N):
        for x in range(M):
            if area[y][x] == 0:
                n_area = [area[i][:] for i in range(N)]
                n_area[y][x] = 1
                dfs(n_area, cnt+1)


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

dfs(area, 0)