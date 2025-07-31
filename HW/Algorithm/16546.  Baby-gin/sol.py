# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
#
# def baby_gin(lst_num):
#     if not lst_num:
#         return True
#
#     n = len(lst_num)
#     for i in range(n - 2):
#         a, b, c = lst_num[i], lst_num[i+1], lst_num[i+2]
#
#         if a == b == c:
#             next_lst = lst_num[:i] + lst_num[i+3:]
#             if baby_gin(next_lst):
#                 return True
#
#         elif a + 1 == b and b + 1 == c:
#             next_lst = lst_num[:i] + lst_num[i+3:]
#             if baby_gin(next_lst):
#                 return True
#
#     return False
#
# for test_case in range(1, T + 1):
#     num = input()
#     lst_num = sorted(list(map(int, num)))
#
#     result = 'true' if baby_gin(lst_num) else 'false'
#     print(f"#{test_case} {result}")

T = int(input())

for test_case in range(1, T + 1):
    cards = input().strip()
    counts = [0]*10

    for ch in cards:
        counts[int(ch)] += 1

    for i in range(10):
        while counts[i] >= 3:
            counts[i] -= 3

    i = 0
    while i <= 7:
        while counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
        i += 1

    ans = "true" if sum(counts) == 0 else "false"
    print(f"#{test_case} {ans}")
