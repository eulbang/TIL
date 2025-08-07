import sys
sys.stdin = open('sample_input.txt')

dxy = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def dfs(x, y, dir, count, dessert, start):
    global max_count
    # print(f'dir:{dir}, (x,y):{(x,y)}, dessert:{dessert}, count:{count}')

    if dir > 3:
        return

    if (x, y) == start:
        max_count = max(max_count, count)
        return

    if (x, y) != start and cafe[x][y] in dessert:
        return

    next_dessert = dessert + [cafe[x][y]]

    nx, ny = x + dxy[dir][0], y + dxy[dir][1]
    if 0 <= nx <= N-1 and 0 <= ny <= N-1:
        # print(f'현재 위치:{x}, {y} 다음 위치:{nx}, {ny}')
        dfs(nx, ny, dir, count + 1, next_dessert, start)
    if dir < 3:
        nx, ny = x + dxy[dir + 1][0], y + dxy[dir + 1][1]
        if 0 <= nx < N and 0 <= ny < N:
            # print(f'현재 위치:{x}, {y} 다음 위치:{nx}, {ny}')
            dfs(nx, ny, dir + 1, count + 1, next_dessert, start)

    return


T = int(input())
# T -= 9
for test_case in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    max_count = -1

    for x in range(N):
        for y in range(N):
            if x < N-2 and 0 < y < N-1:
                start = (x, y)
                dessert = []
                dessert.append(cafe[x][y])
                dfs(x+1, y+1, 0, 1, dessert, start)

    print(f"#{test_case} {max_count}")