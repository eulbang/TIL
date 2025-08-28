DXY = [(0, -1), (0, 1), (-1, 0), (1, 0)]

REFLECT = {
    1: {0: 1, 1: 3, 2: 0, 3: 2},
    2: {0: 3, 1: 0, 2: 1, 3: 2},
    3: {0: 2, 1: 0, 2: 3, 3: 1},
    4: {0: 1, 1: 2, 2: 3, 3: 0},
    5: {0: 1, 1: 0, 2: 3, 3: 2},
}

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]

    area = [[5]*(N+2)]
    for y in range(N):
        area.append([5] + raw[y][:] + [5])
    area.append([5]*(N+2))

    worm = {}
    for y in range(1, N+1):
        for x in range(1, N+1):
            v = area[y][x]
            if 6 <= v <= 10:
                worm.setdefault(v, []).append((x, y))

    max_cnt = 0

    for sy in range(1, N+1):
        for sx in range(1, N+1):
            if area[sy][sx] != 0:
                continue

            for d in range(4):
                x, y = sx, sy
                score = 0

                while True:
                    nx, ny = x + DXY[d][0], y + DXY[d][1]
                    cell = area[ny][nx]

                    if cell == -1:
                        break

                    if cell == 0:
                        x, y = nx, ny
                        if (x, y) == (sx, sy):
                            break
                        continue

                    if 1 <= cell <= 5:
                        score += 1
                        d = REFLECT[cell][d]
                        x, y = nx, ny
                        if (x, y) == (sx, sy):
                            break
                        continue

                    if 6 <= cell <= 10:
                        a, b = worm[cell]
                        tx, ty = a if (nx, ny) != a else b
                        x, y = tx, ty
                        if (x, y) == (sx, sy):
                            break
                        continue

                if score > max_cnt:
                    max_cnt = score

    print(f"#{test_case} {max_cnt}")
