import sys
sys.stdin = open('Sample_input.txt')

T = int(input())
for t in range(1, T+1):
    # N : 문제 수, M : 맟추는 문제 수, K : 점수 2배 되는 카운트
    N, M, K = map(int, input().split())
    problems = [True]*N
    cnt = 0
    for idx in range(N-K, -1, -K):
        if cnt == N-M:
            break
        else:
            problems[idx] = False
            cnt += 1

    while cnt < N-M:
        temp_index = problems.index(True)
        problems[temp_index] = False
        cnt += 1

    total = 0
    k_cnt = 0

    for pb in problems:
        if pb == True:
            k_cnt += 1
            if k_cnt == K:
                total = (total+1)*2
                k_cnt = 0
            else:
                total += 1
        else:
            k_cnt = 0

    print(f"#{t} {total}")