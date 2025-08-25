import sys
sys.stdin = open('sample_input.txt')

def dp(n, a, b):
    lst = []
    for y in range(n+1):
        lst.append([1])
        for x in range(1, y+1):
            if x == y:
                lst[y].append(1)
            else:
                lst[y].append(lst[y-1][x-1] + lst[y-1][x])
    return lst[n][a]

T = int(input())
for test_case in range(1, T + 1):
    n, a, b = map(int, input().split())

    print(f"#{test_case} {dp(n, a, b)}")