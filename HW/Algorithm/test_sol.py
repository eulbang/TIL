from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

DY = (-1, 1, 0, 0)
DX = (0, 0, -1, 1)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

empties = []
viruses = []
for y in range(N):
    row = board[y]
    for x in range(M):
        v = row[x]
        if v == 0:
            empties.append((y, x))
        elif v == 2:
            viruses.append((y, x))

E = len(empties)
initial_safe = E
best = 0

for walls in combinations(empties, 3):
    temp = [row[:] for row in board]

    for (wy, wx) in walls:
        temp[wy][wx] = 1

    q = deque(viruses)
    infected = 0

    limit = initial_safe - 3

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + DY[k], x + DX[k]
            if 0 <= ny < N and 0 <= nx < M and temp[ny][nx] == 0:
                temp[ny][nx] = 2
                infected += 1
                if limit - infected <= best:
                    q.clear()
                    break
                q.append((ny, nx))

    safe = limit - infected
    if safe > best:
        best = safe

print(best)
