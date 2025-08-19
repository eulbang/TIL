import sys
sys.stdin = open('sample_input.txt')

def find_parents(x):
    if x != parents[x]:
        parents[x] = find_parents(parents[x])
    return parents[x]

def union(x, y):
    ux, uy = find_parents(x), find_parents(y)
    if ux != uy:
        parents[ux] = uy


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    parents = [i for i in range(N+1)]

    res = []
    for i in range(M):
        cal, x, y = map(int, input().split())
        if cal == 0:
            union(x, y)
        else:
            res.append('1' if find_parents(x) == find_parents(y) else '0')

    print(f"#{test_case} {''.join(res)}")