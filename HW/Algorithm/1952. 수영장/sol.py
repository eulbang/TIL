import sys
sys.stdin = open('sample_input.txt')

def dfs(idx, sum_cost):
    global min_pay, day_cost, month_cost, month3_cost

    if idx > 12:
        min_pay = min(min_pay, sum_cost)
        return

    dfs(idx+3, sum_cost+month3_cost)
    if calender[idx] == 0:
        dfs(idx+1, sum_cost)
    elif calender[idx]*day_cost < month_cost:
        dfs(idx+1, sum_cost+calender[idx]*day_cost)
    else:
        dfs(idx+1, sum_cost+month_cost)

T = int(input())
for test_case in range(1, T + 1):
    day_cost, month_cost, month3_cost, year_cost = map(int, input().split())
    calender = list(map(int, input().split()))
    # calender = [0, 0] + calender + [0, 0]
    calender = calender

    min_pay = year_cost

    dfs(0, 0)

    print(f"#{test_case} {min_pay}")