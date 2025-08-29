import sys
sys.stdin = open('sample_input.txt')

def dfs():

T = int(input())
for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    min_put = K - 1

    # print(f"#{test_case} {}")