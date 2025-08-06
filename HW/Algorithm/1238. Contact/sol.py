import sys
sys.stdin = open('input.txt')

from collections import deque

# 큐가 비어있을 때까지 반복
# 현재 위치에서 접근 가능한 정점들을 찾고 큐에 넣는다
# 각 요소에 도달하는데 필요한 시간값 저장 필요 -> visited
# 큐에서 현재 위치를 제거한다
# visited 최대값 구한 뒤 해당 정점들의 값의 최대값 출력
# def bfs():
#     while queue:
#         now = queue.popleft()
#
#         for a, b in line:
#             if a == now and visited[b] is None:
#                 visited[b] = visited[a] + 1
#                 queue.append(b)
#
# T = 10
# for test_case in range(1, T + 1):
#     cou, start = map(int, input().split())
#     line = set(zip(*[iter(map(int, input().split()))]*2))
#
#     visited = [None]*101
#     visited[start] = 0
#     queue = deque()
#     queue.append(start)
#
#     bfs()
#     print(line)
#     # print(f'#{test_case} {max((i for i, v in enumerate(visited) if v is not None), key=lambda i: (visited[i], i))}')

T = 10
for test_case in range(1, T + 1):
    cou, start = map(int, input().split())
    nums = list(map(int, input().split()))

    # 입력받은 숫자들을 적절한 인덱스에 입력
    graph = [[] for _ in range(101)]
    for i in range(0, len(nums), 2):
        graph[nums[i]].append(nums[i+1])

    # 방문 확인 + 거리 확인용 빈 배열 선언
    visited = [None]*101

    # 초기값 설정
    visited[start] = 0
    queue = deque([start])

    # BFS
    while queue:
        now = queue.popleft()   # 큐에서 현재 위치 pop
        for nxt in graph[now]:  # 현재 위치에 있는 리스트 순회
            if visited[nxt] is None:    # 비어 있는지 확인
                visited[nxt] = visited[now] + 1 # 현재 경로 +1 다음 위치에 삽입
                queue.append(nxt)   # 다음 방문 위치 큐에 삽입

    # print(graph)
    # print(visited)
    print(f'#{test_case} {max((i for i, v in enumerate(visited) if v is not None), key=lambda i: (visited[i], i))}')
    # visited 의 값이 최대인 항의 인덱스를 모아 그 중 최대값을 출력
    # i, v를 들고 visited 를 순회하는 데 v 가 None이 아닌 i 를 반환한다
    # max 를 비교하는 데 키값을 지정한다. visited[i] = 값 우선, 그 후 i 인덱스 우선