import sys
sys.stdin = open('sample_input.txt')

import heapq

T = int(input())
for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    distances = [0] + [100000000 for _ in range(N)]

    heap = []
    heapq.heappush(heap, [0, 0])
    visited = set()

    while heap:
        dist, current = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)

        for next, weight in graph[current]:
            next_distance = dist + weight
            if next_distance < distances[next]:
                distances[next] = next_distance
                heapq.heappush(heap, [next_distance, next])

    print(f"#{test_case} {distances[N]}")