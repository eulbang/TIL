import sys
sys.stdin = open('s_input.txt')

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    rx, ry = find_set(x), find_set(y)

    if rx != ry:
        parent[ry] = rx

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    parent = [i for i in range(N+1)]

    for i in range(M):
        u, v = map(int, input().split())

        union(u, v)

    for i in range(1, N + 1):
        find_set(i)

    print(f"#{test_case} {len(set(parent))-1}")
