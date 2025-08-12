import sys
sys.stdin = open('input.txt')

import heapq

T = int(input())
for test_case in range(1, T + 1):
    # 입력값 읽기
    N = int(input())
    distance_matrix = [list(map(int, input().split())) for _ in range(N)]

    priority_queue = [(0, 0, 0)]  # distance, current, visited_bitmask

    while priority_queue:
        distance, current, visited = heapq.heappop(priority_queue)
        if current == 0 and visited:  # 다른 곳을 다 방문하고 0으로 돌아왔다는 의미. 집으로 돌아왔네? 배터리 재자.
            result = distance
            break
        elif visited == (1 << N) - 2:  # 0을 제외한 모든 곳을 다 들러봤다는 의미. 이제 집으로 돌아가야지?
            heapq.heappush(priority_queue, (distance + distance_matrix[current][0], 0, visited + 1))
        else:  # 들를 곳이 아직 많이 남아있다는 의미. 더 들러야겠지?
            for i in range(1, N):
                if not (visited & (1 << i)):
                    v = visited
                    v += (1 << i)
                    heapq.heappush(priority_queue, (distance + distance_matrix[current][i], i, v))

    print(f"#{test_case} {result}")