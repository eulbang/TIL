import sys
sys.stdin = open('input.txt')

T = int(input())
T -= 9
for test_case in range(1, T + 1):
    ipt = list(map(int, input().split()))
    N = ipt[0]
    edges = []
    for i in range(1, len(ipt), N):
        edges += [ipt[i:i+N]]

    n, INF = len(edges), 2000
    for k in range(n):
        for s in range(n):
            for e in range(n):
                dik = edges[s][k] if edges[s][k] != 0 or s == k else INF
                dkj = edges[k][e] if edges[k][e] != 0 or k == e else INF
                dij = edges[s][e] if edges[s][e] != 0 or s == e else INF
                if dik + dkj < dij:
                    edges[s][e] = dik + dkj

    for i in range(n):
        if edges[i][i] < 0:
            print('!!')
            break

    print(edges)
    mn = INF
    for i in range(n):
        mn = min(mn, sum(edges[i]))

    print(f'#{test_case} {mn}')

    edges = {edge: {k:v}}