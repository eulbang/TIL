from collections import deque
for test_case in range(1, 11):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

# 맨 윗줄 하강시키기

grid_copy = [grid[g][:] for g in range(n)]
for c in range(n):  # n번 옆으로 갈거임
    # 만약 블록 없으면 넘어가
    if grid[0][c] == 0:
        continue
    # 블록 있으면 첫 블록 큐에 담아
    block = deque([(0, c, 1)]) # row, col, 블록무게
    blockcnt = 1
    while block:
        r, c, b = block.popleft()
        # 만약 왔는데 r이 이미 범위를 넘어 섰다면
        if not 0 <= r < n:
            break
        # 하강 가능한지 확인
        nr = r + 1
        if 0 <= nr < n:
            # 만약 다음 칸에 블럭이 없다면?
            if grid[nr][c] == 0:
                block.append((nr, c, b * 1.9))  # 1.9배
            # 만약 다음 칸에 블럭이 있다면?
            else:
                # 블럭 몇개 있는지 확인해야함
                # cnt = 1
                # while True:
                #     nr += 1
                #     # 밑으로 확인해보는데 격자 안이고 계속 1이면
                #     if 0 <= nr < n and grid[nr][c] == 1:
                #         cnt += 1
                #     else:
                #         break
                # blockcnt += cnt
                # # 장애물보다 내 블록이 크면 하강 가능
                # if cnt < b:
                #     block.append((nr, c, b + cnt))
                # # 장애물이 더 크면 하강 불가
                # else:
                #     break
                cnt = 1
                temp = nr
                while temp + 1 < n and grid[temp + 1][c] == 1:
                    temp += 1
                    cnt += 1

                nr = temp + 1

                if cnt < b:
                    blockcnt += cnt
                    block.append((temp, c, b + cnt))
                else:
                    break
    # print(f'컬럼: {c}')
    # print(blockcnt)
    # 벽돌 하강시키기 - 벽 개수: blockcnt
    for num in range(1, nr+1):
        if blockcnt == 0:
            grid_copy[nr - num][c] = 0
        else:
            grid_copy[nr - num][c] = 1
            blockcnt -= 1
# for p in range(n):
#     print(grid_copy[p])

# ========================== 오른쪽 =======================
result = [grid_copy[g][:] for g in range(n)]
for r in range(n):  # n번 밑으로 갈거임
    # 만약 블록 없으면 넘어가
    if grid_copy[r][0] == 0:
        continue
    # 블록 있으면 첫 블록 큐에 담아
    block = deque([(r, 0, 1)]) # row, col, 블록무게
    blockcnt = 1
    while block:
        r, c, b = block.popleft()
        # 만약 왔는데 r이 이미 범위를 넘어 섰다면
        if not 0 <= c < n:
            break
        # 하강 가능한지 확인
        nc = c + 1
        if 0 <= nc < n:
            # 만약 다음 칸에 블럭이 없다면?
            if grid_copy[r][nc] == 0:
                block.append((r, nc, b * 1.9))  # 1.9배
            # 만약 다음 칸에 블럭이 있다면?
            else:
                # 블럭 몇개 있는지 확인해야함
                cnt = 1
                while True:
                    nc += 1
                    # 밑으로 확인해보는데 격자 안이고 계속 1이면
                    if 0 <= nc < n and grid_copy[r][nc] == 1:
                        cnt += 1
                    else:
                        break
                blockcnt += cnt
                # 장애물보다 내 블록이 크면 하강 가능
                if cnt < b:
                    block.append((r, nc, b + cnt))
                # 장애물이 더 크면 하강 불가
                else:
                    break

    for num in range(1, nc+1):
        if blockcnt == 0:
            result[r][nc - num] = 0
        else:
            result[r][nc - num] = 1
            blockcnt -= 1

col_result = 0
for row in range(n):
    if result[row][n-1] == 1:
        col_result += 1
print(f'#{test_case} {sum(result[n-1])} {col_result}')