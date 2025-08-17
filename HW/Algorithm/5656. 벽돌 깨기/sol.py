import sys
sys.stdin = open('sample_input.txt')

# 어디에 벽돌을 떨어트릴 것인가?
# DFS 돌린다
    # 벽돌이 떨어졌을 때 하,좌,우 방향으로 해당 벽돌의 값만큼 진행
    # 1을 만나면 0으로 변경
    # 2 이상을 만나면 BFS 출발
# 떨어진 벽돌의 영향을 받은 배열을 아래로 정돈한다
# 다음 벽돌
# 벽돌을 떨어트리는 경우의 수 12P4

def crash(x, y, board):  # 벽돌 깨기 (BFS)
    if board[y][x] == 0:     # 빈칸이면 바로 종료
        return
    q = [(x, y, board[y][x])]  # 시작 벽돌 (위치, 범위)
    board[y][x] = 0            # 맞춘 위치 제거
    while q:                   # 큐가 빌 때까지
        cx, cy, p = q.pop(0)   # 벽돌 하나 꺼냄
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:  # 4방향 탐색
            nx, ny = cx, cy
            for _ in range(p-1):                    # (숫자-1)칸만큼 확장
                nx += dx
                ny += dy
                if 0 <= nx < W and 0 <= ny < H and board[ny][nx] != 0:
                    if board[ny][nx] > 1:           # 또 터질 수 있는 벽돌이면 큐에 추가
                        q.append((nx, ny, board[ny][nx]))
                    board[ny][nx] = 0               # 제거 처리

def dfs(cnt, board):  # 구슬 쏘기 횟수, 현재 보드 상태
    global brick

    remain = 0
    for r in board:         # 남은 벽돌 개수 세기
        for v in r:
            if v != 0:
                remain += 1

    if remain == 0:        # 모든 벽돌 제거됨
        brick = 0
        return

    if cnt == 0:           # 최소값 갱신
        brick = min(brick, remain)
        return

    for col in range(W):   # 모든 열에 대해 시도
        row = 0
        while row < H and board[row][col] == 0:  # 해당 열에서 첫 벽돌 찾기
            row += 1
        if row == H:       # 벽돌이 없으면 넘어감
            continue

        new_board = [r[:] for r in board]  # 현재 보드 복사
        crash(col, row, new_board)         # 벽돌 깨기

        for x in range(W):                 # 중력 처리
            temp = []                      # 남아있는 벽돌 임시 저장
            for y in range(H-1, -1, -1):   # 아래에서 위로
                if new_board[y][x] != 0:
                    temp.append(new_board[y][x])
            for y in range(H-1, -1, -1):   # 아래부터 채우기
                new_board[y][x] = temp.pop(0) if temp else 0

        dfs(cnt-1, new_board)  # 다음 구슬 쏘기

T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())  # 구슬 수, 너비, 높이
    area = [list(map(int, input().split())) for _ in range(H)]
    brick = 2000                         # 최소 벽돌 개수 초기화 (충분히 큰 값)
    dfs(N, area)                         # DFS 시작
    print(f"#{test_case} {brick}")       # 결과 출력
