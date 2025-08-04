import sys
sys.stdin = open('sample_input.txt')

def cul(lst, pos):
    if pos > N:
        return 0
    if lst[pos] is None:
        lst[pos] = cul(lst, pos*2) + cul(lst, pos*2+1)
    return lst[pos]

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    lst = [None]*(N+1)

    for i in range(M):
        pos, num = map(int, input().split())
        lst[pos] = num

    cul(lst, 1)

    print(f"#{test_case} {lst[L]}")