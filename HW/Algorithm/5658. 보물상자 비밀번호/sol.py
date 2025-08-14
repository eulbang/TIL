import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num = input()

    print(num)
    print(num[-1:]+num[:2])

    # print(f"#{test_case} {}")
