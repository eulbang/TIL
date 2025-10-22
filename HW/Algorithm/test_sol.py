import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

edges = [tuple(map(int, input().split())) for _ in range(M)]
res = {1}

changed = True
while changed:
    changed = False
    for a, b in edges:
        if a in res and b not in res:
            res.add(b); changed = True
        if b in res and a not in res:
            res.add(a); changed = True

print(len(res) - 1)
