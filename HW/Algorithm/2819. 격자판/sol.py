import sys
sys.stdin = open('sample_input.txt')

def dfs(x, y, lst):
    if len(lst) == 7:
        count.add(''.join(map(str, lst)))
        return

    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, lst + [grid[nx][ny]])

T = int(input())
for test_case in range(1, T + 1):
    grid = [list(map(int, input().split())) for _ in range(4)]

    count = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, [grid[i][j]])

    print(f"#{test_case} {len(set(count))}")