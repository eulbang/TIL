import sys
sys.stdin = open('sample_input.txt')

direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def dfs(row, col, dir, cnt, dessert):
    global max_dessert, start_row, start_col
    # print(f'x:{row}, y:{col}, dir:{dir}, cnt:{cnt}, start:{start_row}, {start_col}')
    # 갈 수 있는 방향 인덱스를 벗어나면 return
    if dir > 3:
        return

    # 시작점과 동일한 곳에 도착하면
    if row == start_row and col == start_col:
        # print(f'x:{row}, y:{col}, max:{max_dessert}, cnt:{cnt}')
        if cnt > max_dessert: max_dessert = cnt # max_dessert update
        return

    # 시작점과 동일하지 않고 이미 먹은 디저트라면
    if (row != start_row and col != start_col) and cafe_map[row][col] in dessert:
        # print(f'x:{row}, y:{col}, dir:{dir}, cnt:{cnt}, start:{start_row}, {start_col}, max:{max_dessert}')
        return # 더 이상 탐색하지 않음

    # 이외의 경우는 ...
    next_dessert = dessert + [cafe_map[row][col]]     # 디저트 추가
    nx, ny = row + direction[dir][0], col + direction[dir][1] # 다음 위치 업데이트

    # 인덱스 이내에 존재하는지 확인
    if 0 <= nx < N and 0 <= ny < N:
        dfs(nx, ny, dir, cnt+1, next_dessert)
    if dir < 3:
        nx, ny = row + direction[dir+1][0], col + direction[dir+1][1] # 다음 방향에 대한 nx ,ny 업데이트
        if 0 <= nx < N and 0 <= ny < N:
            dfs(nx, ny, dir+1, cnt+1, next_dessert)
    return


T = int(input())
# T -= 8
for t in range(1, T + 1):
    N = int(input())
    cafe_map = [list(map(int, input().strip().split())) for _ in range(N)]
    max_dessert = -1

    if t == 1: continue

    # 모든 점에서 시작 (가능한 시작점만)
    for i in range(N - 2):  # 사각형을 만들려면 충분한 공간이 필요
        for j in range(1, N - 1):  # 양쪽 끝은 사각형 생성이 어려움
            start_row, start_col = i, j
            dessert = []

            # 시작점의 디저트 추가
            dessert.append(cafe_map[start_row][start_col])

            # 첫 번째 방향(우하(1, 1)으로 DFS 시작
            dfs(start_row+1, start_col+1, 0, 1, dessert)

    print(f"#{t} {max_dessert}")