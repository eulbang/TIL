import sys
sys.stdin = open('input.txt')

def inorder(node, ans):
    if len(tree[node]) > 2 and tree[node][2].isdigit():
        inorder(int(tree[node][2]), ans)
    ans.append(tree[node][1])
    if len(tree[node]) > 3 and tree[node][3].isdigit():
        inorder(int(tree[node][3]), ans)

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    tree = [None] * (N + 1)

    for _ in range(N):
        info = input().split()
        idx = int(info[0])
        tree[idx] = info

    ans = []
    inorder(1, ans)
    print(f"#{test_case} {''.join(ans)}")