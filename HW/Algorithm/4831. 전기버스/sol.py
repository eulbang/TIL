import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    # 충전 할 때마다 갈수 있는 범위 뒤져보고
    # 범위 내의 가장 먼 충전소로 점프한다

    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    now, count = 0, 0
    while True:
        if now+K >= N:
            break
        for i in range(now+K, now, -1):
            if i in charge:
                now = i
                count += 1
                # print(now)
                break
        else:
            count = 0
            break
        # print(count)

    print(count)