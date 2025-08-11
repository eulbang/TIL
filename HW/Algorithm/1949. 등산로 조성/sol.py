import sys
sys.stdin = open('sample_input.txt')

dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]    # 상 하 좌 우

# 방문처리 visited 배열 만들어서 처리
# K 만큼 무조건 깎는 것이 아닌 필요한 만큼만 깎을 것

def dfs(x, y, count, K):
    global max_road
    max_road = max(max_road, count)

    for i in range(len(dxy)):
        nx, ny = x + dxy[i][0], y + dxy[i][1]
        if 0 <= nx < N and 0 <= ny < N and mount[nx][ny] < mount[x][y]:
            mount[x][y] += 25
            dfs(nx, ny, count+1, K)
            mount[x][y] -= 25
        elif 0 <= nx < N and 0 <= ny < N and mount[nx][ny] - K < mount[x][y]:
            mount[nx][ny] -= K
            mount[x][y] += 25
            dfs(nx, ny, count+1, 0)
            mount[nx][ny] += K
            mount[x][y] -= 25

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    mount = [list(map(int, input().split())) for _ in range(N)]

    top = []
    top_height = 0
    for y in range(N):
        for x in range(N):
            if top_height < mount[x][y]:
                top.clear()
                top.append([x, y])
                top_height = mount[x][y]
            elif top_height == mount[x][y]:
                top.append([x, y])

    max_road = 0
    for idx in range(len(top)):
        dfs(top[idx][0], top[idx][1], 1, K)

    print(f"#{test_case} {max_road}")