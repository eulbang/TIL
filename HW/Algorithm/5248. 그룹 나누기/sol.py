import sys
sys.stdin = open('sample_input.txt')

def find_parent(idx):
    if idx != parent[idx]:
        parent[idx] = find_parent(parent[idx])
    return parent[idx]

# def union(a, b):
#     pa, pb = find_parent(a), find_parent(b)
#     if pa != pb:
#         parent[pb] = pa

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    chosen = list(map(int, input().split()))

    parent = [i for i in range(N + 1)]

    # for i in range(0, len(chosen), 2):
    #     union(chosen[i], chosen[i + 1])

    for i in range(0, len(chosen), 2):
        pa, pb = find_parent(chosen[i]), find_parent(chosen[i + 1])
        if pa != pb:
            parent[pb] = pa

    for i in range(1, N + 1):
        find_parent(i)

    print(f"#{test_case} {len(set(parent)) - 1}")
