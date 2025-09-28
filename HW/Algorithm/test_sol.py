from collections import deque

DR = [0, 1, 0, -1]
DC = [1, 0, -1, 0]

N = int(input())
area = [[False]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    area[r-1][c-1] = True

L = int(input())
turns = {}
for _ in range(L):
    t, d = input().split()
    turns[int(t)] = d

snake = deque([(0, 0)])
occupied = {(0, 0)}
dir = 0
time = 0
r, c = 0, 0

while True:
    time += 1
    nr, nc = r + DR[dir], c + DC[dir]

    if not (0 <= nr < N and 0 <= nc < N) or (nr, nc) in occupied:
        print(time)
        break

    snake.appendleft((nr, nc))
    occupied.add((nr, nc))

    if area[nr][nc]:
        area[nr][nc] = False
    else:
        tr, tc = snake.pop()
        occupied.remove((tr, tc))

    if time in turns:
        if turns[time] == 'L':
            dir = (dir + 3) % 4
        else:
            dir = (dir + 1) % 4

    r, c = nr, nc