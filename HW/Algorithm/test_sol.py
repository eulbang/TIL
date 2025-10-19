import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def check(line):
    used = [False]*N
    for i in range(N-1):
        if abs(line[i] - line[i+1]) > 1:
            return False
        if line[i] - line[i+1] == 1:
            for j in range(i+1, i+1+L):
                if j >= N or line[j] != line[i+1] or used[j]:
                    return False
                used[j] = True
        elif line[i+1] - line[i] == 1:
            for j in range(i, i-L, -1):
                if j < 0 or line[j] != line[i] or used[j]:
                    return False
                used[j] = True
    return True

cnt = 0
for i in range(N):
    if check(board[i]):
        cnt += 1
    if check([board[j][i] for j in range(N)]):
        cnt += 1

print(cnt)
