import sys
sys.stdin = open('sample_input.txt')

def fnd(now, res, cul, num, result):
    if now >= len(num):
        result.append(res)
        return
    if cul[0] > 0:
        cul[0] -= 1
        fnd(now + 1, res + num[now], cul, num, result)
        cul[0] += 1
    if cul[1] > 0:
        cul[1] -= 1
        fnd(now+1, res - num[now], cul, num, result)
        cul[1] += 1
    if cul[2] > 0:
        cul[2] -= 1
        fnd(now+1, res*num[now], cul, num, result)
        cul[2] += 1
    if cul[3] > 0:
        cul[3] -= 1
        if res < 0:
            fnd(now + 1, -(-res // num[now]), cul, num, result)
        else:
            fnd(now + 1, res // num[now], cul, num, result)
        cul[3] += 1

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    cul = list(map(int, input().split()))
    num = list(map(int, input().split()))

    result = []
    fnd(1, num[0], cul, num, result)
    print(f"#{test_case} {max(result)-min(result)}")