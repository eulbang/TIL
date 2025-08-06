import sys
sys.stdin = open('input.txt')

from collections import deque

def mov(x, y):
    queue = deque()
    queue.append((x, y))
    maze[x][y] = 1

    while queue:
        cx, cy = queue.popleft()
        if maze[cx][cy] == 3:
            print(f'#{test_case} 1')
            return

        maze[cx][cy] = 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < 100 and 0 <= ny < 100:
                if maze[nx][ny] != 1:
                    queue.append((nx, ny))

    print(f'#{test_case} 0')

T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    maze = [list(map(int, input())) for _ in range(100)]

    for x in range(100):
        for y in range(100):
            if maze[x][y] == 2:
                mov(x, y)
                break
    # print(f'#{test_case} {}')