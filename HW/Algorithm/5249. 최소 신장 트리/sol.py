import sys
sys.stdin = open('sample_input.txt')

def find_parents(x):
    if parent[x] != x:
        parent[x] = find_parents(parent[x])
    return parent[x]

def union(x, y):
    ux, uy = find_parents(x), find_parents(y)
    if ux != uy:
        parent[uy] = ux

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]
    edges = [list(map(int, input().split())) for _ in range(E)]

    edges.sort(key=lambda x: x[2])

    mst_cost, cnt = 0, 0

    for u, v, w in edges:
        if find_parents(u) != find_parents(v):
            union(u, v)
            mst_cost += w
            cnt += 1
            if cnt == V:
                break

    print(f"#{test_case} {mst_cost}")