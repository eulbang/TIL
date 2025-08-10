import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
# T -= 9
for test_case in range(1, T + 1):
    V, E, node1, node2 = map(int, input().split())
    tree = list(map(int, input().split()))
    # print(tree)

    up_list1, up_list2 = [], []
    while node1 != 1 or node2 != 1:
        for i in range(1, len(tree), 2):
            if tree[i] == node1:
                up_list1 += [tree[i-1]]
                node1 = tree[i-1]
            if tree[i] == node2:
                up_list2 += [tree[i-1]]
                node2 = tree[i-1]

    fore = 0
    for i in up_list1:
        if i in up_list2:
            fore = i
            break

    queue = deque()
    queue.append(fore)
    count = 0

    while queue:
        now = queue.popleft()
        count += 1
        for i in range(0, len(tree)-1, 2):
            if tree[i] == now:
                queue.append(tree[i+1])


    print(f'#{test_case} {fore} {count}')