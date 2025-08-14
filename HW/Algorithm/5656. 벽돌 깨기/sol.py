import sys
sys.stdin = open('sample_input.txt')

# 어디에 벽돌을 떨어트릴 것인가?
# DFS 돌린다
    # 벽돌이 떨어졌을 때 하,좌,우 방향으로 해당 벽돌의 값만큼 진행
    # 1을 만나면 0으로 변경
    # 2 이상을 만나면 DFS 출발
# 떨어진 벽돌의 영향을 받은 배열을 아래로 정돈한다
# 다음 벽돌
# 벽돌을 떨어트리는 경우의 수 12P4

def dfs():
    pass

T = int(input())
for test_case in range(1, T + 1):
    # 떨어트릴 벽돌 수 : N, 배열 너비 : W, 배열 높이 : H
    N, W, H = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(H)]

    cnt = N
    while cnt:
        brick = 2000
        for i in range(W):
            dfs()
        # brick = min(brick, )
        cnt -= 1

    # print(f"#{test_case} {}")
