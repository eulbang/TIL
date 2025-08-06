import sys
sys.stdin = open('input.txt')

def mov(x, y):
    if maze[x][y] == 3:
        return True

    maze[x][y] = 1

    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 16 and 0 <= ny < 16:
            if maze[nx][ny] != 1:
                if mov(nx, ny):
                    return True

    return False


T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    for x in range(16):
        for y in range(16):
            if maze[x][y] == 2:
                result = mov(x, y)

    if result:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')