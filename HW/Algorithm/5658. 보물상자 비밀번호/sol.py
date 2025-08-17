import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num = input()

    pwd = set()
    side = N//4
    for i in range(N):
        if i < N-side:
            pwd.add(int(num[i:i+side], 16))
        else:
            pwd.add(int(num[i:]+num[:side-N+i], 16))

    sorted_pwd = sorted(pwd, reverse=True)

    print(f"#{test_case} {sorted_pwd[K-1]}")
