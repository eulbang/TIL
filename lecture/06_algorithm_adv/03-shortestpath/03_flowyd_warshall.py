
def floyd_warshall(graph):
    n = len(graph)
    for k_node in range(n):
        for start in range(n):
            for end in range(n):
                Dik = graph[start][k_node]
                Dkj = graph[k_node][end]
                Dij = graph[start][end]
                if Dik + Dkj < Dij:
                    graph[start][end] = Dik + Dkj

    for i in range(n):
        if graph[i][i] < 0:
            print('음수 사이클')
            break

    return graph

INF = float('inf')  # 무한대

# 예시 그래프의 인접 행렬
adj_matrix = [
    [0, 4, 2, 5, INF],
    [INF, 0, 1, INF, 4],
    [1, 3, 0, 1, 2],
    [-2, INF, INF, 0, 2],
    [INF, -3, 3, 1, 0]
]

# 음수 사이클 확인
# adj_matrix = [
#     [0, -4, 2, 5, INF],
#     [INF, 0, 1, INF, 4],
#     [1, 3, 0, 1, 2],
#     [-2, INF, INF, 0, 2],
#     [INF, -3, 3, 1, 0]
# ]

result = floyd_warshall(adj_matrix)

# 최단 거리 행렬 출력 
for row in result:
    print(row)
