import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for col in range(N):
        flag = 0
        for row in range(N):
            if table[row][col] == 1:
                flag = 1
            elif table[row][col] == 2:
                if flag == 1:
                    count += 1
                    flag = 0

    print(f"#{test_case} {count}")