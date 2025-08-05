import sys
sys.stdin = open('input.txt')

def reward(num, count, res, visited):
    if count == 0:
        res.append(''.join(num))
        return
    key = (''.join(num), count)
    if key in visited:
        return
    visited.add(key)

    for i in range(len(num)):
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]
            reward(num, count - 1, res, visited)
            num[i], num[j] = num[j], num[i]

T = int(input())
for test_case in range(1, T + 1):
    num_txt, count = input().split()
    count = int(count)
    num = list(num_txt)

    res = []
    visited = set()
    reward(num, count, res, visited)
    print(f"#{test_case} {max(res)}")