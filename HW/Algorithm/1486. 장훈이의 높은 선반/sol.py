import sys
sys.stdin = open('input.txt')

def dfs(s_sum, idx):
    global min_sum, B

    if s_sum >= B:
        min_sum = min(s_sum-B, min_sum)
        return
    if idx >= len(S):
        return

    dfs(s_sum + S[idx], idx+1)
    dfs(s_sum, idx+1)
    return

T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    min_sum = sum(S)
    dfs(0, 0)

    print(f'#{test_case} {min_sum}')