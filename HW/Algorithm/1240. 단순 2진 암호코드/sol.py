import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    code = [[0, 0, 0, 1, 1, 0, 1],
              [0, 0, 1, 1, 0, 0, 1],
              [0, 0, 1, 0, 0, 1, 1],
              [0, 1, 1, 1, 1, 0, 1],
              [0, 1, 0, 0, 0, 1, 1],
              [0, 1, 1, 0, 0, 0, 1],
              [0, 1, 0, 1, 1, 1, 1],
              [0, 1, 1, 1, 0, 1, 1],
              [0, 1, 1, 0, 1, 1, 1],
              [0, 0, 0, 1, 0, 1, 1]]

    N, M = map(int, input().split())
    password = [[int(ch) for ch in input()] for _ in range(N)]

    for i in range(N):
        if sum(password[i])!=0:
            pwd_line = password[i]

    for i in range(len(pwd_line)-1, 0, -1):
        if pwd_line[i] != 0:
            if i - 55 >= 0:
                real_pwd = pwd_line[i - 55: i + 1]
                break

    num_pwd = []
    for i in range(0, len(real_pwd), 7):
        for j in range(len(code)):
            # print(f"{code[j]}, {real_pwd[i:i+7]}")
            if code[j] == real_pwd[i:i+7]:
                num_pwd.append(j)
    # print(num_pwd)

    pwd_sum = 0
    for i in range(len(num_pwd)):
        if i % 2 == 0:
            pwd_sum += num_pwd[i]*3
        else:
            pwd_sum += num_pwd[i]
    # print(pwd_sum)

    if pwd_sum % 10 == 0:
        print(f"#{test_case} {sum(num_pwd)}")
    else:
        print(f"#{test_case} 0")
