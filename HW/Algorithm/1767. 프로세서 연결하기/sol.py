import sys
sys.stdin = open('sample_input.txt')

def wire(idx, dir):
    x, y = core[idx]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    path = []
    nx, ny = x + dx[dir], y + dy[dir]

    while 0 <= nx < N and 0 <= ny < N:
        if area[nx][ny] != 0:
            return []  # 전선이나 코어가 있으면 막힘
        path.append((nx, ny))
        nx += dx[dir]
        ny += dy[dir]

    return path

def dfs(idx, plug, length):
    global max_connected, min_length

    # 모든 코어 다 처리했을 때 결과 갱신
    if idx == len(core):
        if plug > max_connected:
            max_connected = plug
            min_length = length
        elif plug == max_connected and length < min_length:
            min_length = length
        return

    # 가지치기: 남은 코어 전부 연결해도 최대치 못 넘으면 종료
    if plug + (len(core) - idx) < max_connected:
        return

    x, y = core[idx]
    # 가장자리 코어는 이미 연결된 것으로 간주
    if x == 0 or x == N - 1 or y == 0 or y == N - 1:
        dfs(idx + 1, plug + 1, length)
        return

    connected = False
    for dir in range(4):
        path = wire(idx, dir)
        if path:
            for px, py in path:
                area[px][py] = 2  # 전선 설치
            dfs(idx + 1, plug + 1, length + len(path))
            for px, py in path:
                area[px][py] = 0  # 전선 제거 (백트래킹)
            connected = True

    # 전선 연결하지 않고 스킵
    dfs(idx + 1, plug, length)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    core = []
    for x in range(N):
        for y in range(N):
            if area[x][y] == 1:
                core.append((x, y))

    max_connected = 0
    min_length = 10**9

    dfs(0, 0, 0)

    print(f"#{test_case} {min_length}")
