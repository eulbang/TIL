import sys
sys.stdin = open('sample_input.txt')

def honey(y, x, count, sum_honey):
    global M, C

    if count == M:
        honey_cost = sum(i * i for i in sum_honey)
        return honey_cost

    if sum(sum_honey) > C:
        return 0

    best = 0

    if x < N:
        if sum(sum_honey) + beehive[y][x] <= C:
            sum_honey.append(beehive[y][x])
            best = max(best, honey(y, x + 1, count + 1, sum_honey))
            sum_honey.pop()
        best = max(best, honey(y, x + 1, count + 1, sum_honey))

    return best


T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    beehive = [list(map(int, input().split())) for _ in range(N)]

    res_honey = 0
    y1 = x1 = 0

    while y1 < N:
        if x1 <= N - M:
            x2, y2 = x1 + M, y1
        else:
            x2, y2 = 0, y1 + 1
            if y2 >= N:
                break
        while y2 < N:
            while x2 <= N - M:
                h1 = honey(y1, x1, 0, [])
                h2 = honey(y2, x2, 0, [])
                if y1 == y2 and not (x2 >= x1 + M or x1 >= x2 + M):
                    x2 += 1
                    continue
                res_honey = max(res_honey, h1 + h2)
                x2 += 1
            x2 = 0
            y2 += 1
        if x1 < N - M:
            x1 += 1
        else:
            x1 = 0
            y1 += 1

    print(f"#{test_case} {res_honey}")