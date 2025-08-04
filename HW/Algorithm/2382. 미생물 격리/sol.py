import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    area = [[None] * N for _ in range(N)]

    for _ in range(K):
        r, c, count, direct = map(int, input().split())
        area[r][c] = [count, direct]

    for _ in range(M):
        future = [[None] * N for _ in range(N)]

        for x in range(N):
            for y in range(N):
                if area[x][y] is None:
                    continue
                count, direction = area[x][y]
                if direction == 1:
                    nx, ny = x - 1, y
                elif direction == 2:
                    nx, ny = x + 1, y
                elif direction == 3:
                    nx, ny = x, y - 1
                else:
                    nx, ny = x, y + 1
                if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
                    count //= 2
                    if count == 0:
                        continue
                    if direction == 1:
                        ndir = 2
                    elif direction == 2:
                        ndir = 1
                    elif direction == 3:
                        ndir = 4
                    else:
                        ndir = 3
                else:
                    ndir = direction
                if future[nx][ny] is not None:
                    if future[nx][ny][2] < count:
                        future[nx][ny][1] = ndir
                        future[nx][ny][2] = count
                    future[nx][ny][0] += count
                else:
                    future[nx][ny] = [count, ndir, count]
        for x in range(N):
            for y in range(N):
                if future[x][y] is not None:
                    future[x][y] = [future[x][y][0], future[x][y][1]]
        area = future

    total = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] is not None:
                total += area[i][j][0]

    print(f"#{test_case} {total}")

'''
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    area = [[None] * N for _ in range(N)]

    for _ in range(K):
        r, c, count, direct = map(int, input().split())
        area[r][c] = [count, direct]

    for _ in range(M):
        future = [[None] * N for _ in range(N)]

        for x in range(N):
            for y in range(N):
                if area[x][y] is None:
                    continue
                direction = area[x][y][1]

                if direction == 1:  # 위: (x-1, y)
                    nx, ny = x - 1, y
                elif direction == 2:  # 아래: (x+1, y)
                    nx, ny = x + 1, y
                elif direction == 3:  # 좌: (x, y-1)
                    nx, ny = x, y - 1
                else:  # direction == 4, 우: (x, y+1)
                    nx, ny = x, y + 1

                if future[nx][ny] is not None:
                    if area[x][y][0] > future[nx][ny][0]:
                        future[nx][ny][1] = area[x][y][1]
                        future[nx][ny][0] += area[x][y][0]
                    else:
                        future[nx][ny][0] += area[x][y][0]
                else:
                    future[nx][ny] = area[x][y]

                # 레드존(경계) 처리
                if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
                    future[nx][ny][0] //= 2
                    if future[nx][ny][1] == 1:
                        future[nx][ny][1] = 2
                    elif future[nx][ny][1] == 2:
                        future[nx][ny][1] = 1
                    elif future[nx][ny][1] == 3:
                        future[nx][ny][1] = 4
                    elif future[nx][ny][1] == 4:
                        future[nx][ny][1] = 3

        area = future

    total = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] is not None:
                total += area[i][j][0]

    print(f"#{test_case} {total}")
'''