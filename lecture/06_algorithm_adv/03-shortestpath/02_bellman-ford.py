def bellman_ford(graph, start):
    n = len(graph)
    distances = {v: float('inf') for v in graph}
    distances[start] = 0

    for _ in range(n-1):
        updated = False

        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    updated = True

        if not updated:
            break

    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                print('음수 사이클')
                return False

    return distances

# 예시 그래프
graph = {
    'a': {'b': 4, 'c': 2},
    'b': {'c': 3, 'd': 2, 'e': 3},
    'c': {'b': 1, 'd': 4, 'e': 5},
    'd': {'e': -3},
    'e': {'f': 2},
    'f': {}
}

# 음수 사이클 예시 그래프
# graph = {
#     'a': {'b': 4, 'c': 2},
#     'b': {'c': -3, 'd': 2, 'e': 3},
#     'c': {'b': 1, 'd': 4, 'e': 5},
#     'd': {'e': -3},
#     'e': {'f': 2},
#     'f': {}
# }

# 시작 정점 설정
start_vertex = 'a'

# 벨만-포드 알고리즘 실행
result = bellman_ford(graph, start_vertex)

print(f"'{start_vertex}': {result}")
