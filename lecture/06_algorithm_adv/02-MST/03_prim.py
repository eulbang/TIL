import heapq

def prim(vertices, edges):
    mst = []
    visited = set()
    start_vertex = vertices[0]  # 아무 정점이나 상관없음

    # adj_list[start_vertex]

    min_heap = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]

    heapq.heapify(min_heap)
    visited.add(start_vertex)

    while min_heap:
        weight, start, end = heapq.heappop(min_heap)
        if end in visited: continue

        visited.add(end)
        mst.append((start, end, weight))

        for next, weight in adj_list[end]:
            if next in visited: continue
            heapq.heappush(min_heap, (weight, end, next))

    return mst


'''
    가중치 그래프 형상
         1
      ¹ / \ ²
       2---3
         ³
'''
vertices = [1, 2, 3]
edges = [[1, 2, 1], [2, 3, 3], [1, 3, 2]]

adj_list = {v: [] for v in vertices}
for s, e, w in edges:
    adj_list[s].append((e, w))
    adj_list[e].append((s, w))

'''
    MST 구성 결과
         1
      ¹ / \ ²
       2   3
'''
mst = prim(vertices, edges)  # [(1, 2, 1), (1, 3, 2)]
print(mst)


# # 교재 간선 정보
# edges = [
#     (0, 1, 32),
#     (0, 2, 31),
#     (0, 5, 60),
#     (0, 6, 51),
#     (1, 2, 21),
#     (2, 4, 46),
#     (2, 6, 25),
#     (3, 4, 34),
#     (3, 5, 18),
#     (4, 5, 40),
#     (4, 6, 51),
# ]
# vertices = list(range(7))  # 정점 집합

# result = prim(vertices, edges)
# print(result) # [(0, 2, 31), (2, 1, 21), (2, 6, 25), (2, 4, 46), (4, 3, 34), (3, 5, 18)]