from collections import deque

dxy = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))

T = int(input())
for _ in range(T):
    I = int(input())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())

    field = [[0]*I for _ in range(I)]

    q = deque([(sx, sy)])

    cnt = 0
    while q:
        x, y = q.popleft()
        for cx, cy in dxy:
            nx, ny = x+cx, y+cy
            if 0 <= nx < I and 0 <= ny < I and field[ny][nx] == 0:
                field[ny][nx] = 1
                if (nx, ny) == (gx, gy):
                    break
                q.append((nx, ny))
            cnt += 1

    print(cnt)