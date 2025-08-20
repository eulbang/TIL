import sys
sys.stdin = open('re_sample_input.txt')

import heapq

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))

    pos_island = []
    for i in range(N):
        pos_island += [[island_x[i], island_y[i]]]

    E = float(input())

    visited = [False]*N
    visited[0] = True
    min_heap = []
    for i in range(1, N):
        tunnel = ((pos_island[0][0] - pos_island[i][0]) ** 2) + ((pos_island[0][1] - pos_island[i][1]) ** 2)
        heapq.heappush(min_heap, (tunnel, i))

    min_cost = 0
    while min_heap:
        c, e = heapq.heappop(min_heap)

        if visited[e]: continue

        visited[e] = True
        min_cost += c

        for n in range(N):
            if not visited[n]:
                next_cost = ((pos_island[e][0] - pos_island[n][0]) ** 2) + ((pos_island[e][1] - pos_island[n][1]) ** 2)
                heapq.heappush(min_heap, (next_cost, n))

    print(f"#{test_case} {round(min_cost*E)}")