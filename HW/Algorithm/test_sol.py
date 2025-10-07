import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

L, R, s, cnt = 0, 0, 0, 0

while True:
    if s >= M:
        if s == M:
            cnt += 1
        s -= A[L]
        L += 1
    else:
        if R == N:
            break
        s += A[R]
        R += 1

print(cnt)
