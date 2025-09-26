N = int(input())
area = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    area[y-1][x-1] = 1

for i in range(N):
    print(area[i])
