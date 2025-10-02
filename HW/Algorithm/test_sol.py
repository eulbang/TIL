from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def is_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False


def solve(data):
    q = deque([(0, 0, 0)])
    visit = set()
    visit.add((0, 0))
    distances[0][0] = 0

    while q:
        cx, cy, dist = q.popleft()
        if (cx, cy) == (n - 1, m - 1):
            return distances[cx][cy]

        for dr in range(4):
            nx, ny = cx + dx[dr], cy + dy[dr]
            if is_range(nx, ny) and data[nx][ny] and (nx, ny) not in visit:
                visit.add((nx, ny))
                if dist > distances[nx][ny]:
                    distances[nx][ny] = dist + 1
                    q.append((nx, ny, dist + 1))

    return -1

    # if not ans:
    #     return -1
    # return ans


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
distances = [[0] * m for _ in range(n)]
result = solve(a)
print(result)