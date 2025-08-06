import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input())) for _ in range(N)]
    srt = [[None]*N for _ in range(N)]

    queue = deque()
    queue.append((0, 0))
    srt[0][0] = 0

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = dx + cx, dy + cy

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if srt[nx][ny] is None or srt[cx][cy] + area[nx][ny] < srt[nx][ny]:
                srt[nx][ny] = srt[cx][cy] + area[nx][ny]
                queue.append((nx, ny))

    print(f'#{test_case} {srt[N-1][N-1]}')