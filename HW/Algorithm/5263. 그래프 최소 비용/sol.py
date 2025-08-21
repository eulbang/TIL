import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N)]

    INF = 50000

    for k_node in range(N):
        for start in range(N):
            for end in range(N):
                dik = edges[start][k_node] if edges[start][k_node] != 0 or start == k_node else INF
                dkj = edges[k_node][end] if edges[k_node][end] != 0 or k_node == end else INF
                dij = edges[start][end] if edges[start][end] != 0 or start == end else INF

                if dik + dkj < dij:
                    edges[start][end] = dik + dkj

    for i in range(N):
        if edges[i][i] < 0:
            break

    max_cost = 0
    for i in range(N):
        max_cost = max(max_cost, max(edges[i]))

    print(f"#{test_case} {max_cost}")