import sys
sys.stdin = open('sample_input.txt')

import heapq

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    work = [list(input().split()) for _ in range(N)]

    max_heap = []

    print(f'#{test_case}', end=' ')
    for i in range(len(work)):
        if len(work[i]) > 1:
            heapq.heappush(max_heap, -int(work[i][1]))
        else:
            if max_heap:
                print(f'{-heapq.heappop(max_heap)}', end=' ')
            else:
                print(f'-1', end=' ')

    print()