import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    txt = list(map(int, input().split('+')))
    sm = sum(txt)

    print(f"#{test_case} {sm}")