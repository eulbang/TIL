import sys
sys.stdin = open('sample_input.txt')

# 충돌하게 될 원자들의 에너지의 총합
# 각 원자는 진행 방향을 가지고 있음
# 1분 뒤 리스트를 만들어서 진행시키기
# 1분 뒤 리스트에 이미 값이 있을 경우 충돌
# 1분 전 리스트에 값이 있고 진행 방향이 반대일 경우 충돌
# 충돌했을 시 충돌지점이라는 표시 또는 상하좌우 탐색 필요
# 충돌 표시로 진행할 경우 순회 마지막에 충돌 표시 제거 필요
# x 또는 y 값 중 하나라도 abs 1001 이상이 되면 제거

dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

T = int(input())
# T -= 1
for test_case in range(1, T + 1):
    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]  # atom[i] = [x, y, dir, energy]

    for i in range(N):
        atom[i] = [[atom[i][0], atom[i][1]], atom[i][2], atom[i][3]]  # atom[i] = [[x, y], dir, energy]

    sum_energy = 0
    while len(atom) > 1:
        future = []
        bang = []
        for now in range(len(atom)):
            in_range = abs(atom[now][0][0]) <= 1000 and abs(atom[now][0][1]) <= 1000 # 영역 안에 있는지 확인 - T/F
            if in_range:
                dx, dy = atom[now][0][0] + dxy[atom[now][1]][0], atom[now][0][1] + dxy[atom[now][1]][1]   # 다음 위치
                # future 안에 해당 x,y 위치에 원자가 있는지 확인 - 있다면 현 원자와 해당 위치 원자의 에너지 저장 후 제거 - 이후 오는 처리 필욧
                flg = 1
                for (x, y), d, e in future:
                    # print(f'atom:{atom} future:{future} bang:{bang} now:{now}')
                    for (bx, by) in bang:   # 이번 회차에 충돌한 기록이 있는지 확인 후 있다면 에너지 저장 후 future 에 저장X
                        if (dx, dy) == (bx, by) and flg == 1:
                            sum_energy += atom[now][2]
                            flg = 0
                            break
                    if (dx, dy) == (x, y) and flg == 1: # 다음 위치에 이미 도착한 원자가 있는지 확인
                        sum_energy += e
                        sum_energy += atom[now][2]
                        # 이놈 이거 안된다 계산량 미쳤다 다른 방법 생각해보자
                        # -> 딕셔너리에 동일한 키에 리스트로 된 값을 append 하면 리스트가 이어진다
                        # -> 값이 1개일 때 길이보다 길면 여러 값이 들어갔다는 뜻이므로 마지막에 atom으로 옮길 때 제외하면서 에너지를 뽑는다
                        future[future.index([[x, y], d, e])] = [[1001, 0], 0, 0]
                        bang.append([x, y])
                        flg = 0
                        continue
                # 현재 시점 중 도착지에 원자가 있고, 진행 방향이 현 원자와 반대인지 확인 - 있다면 추가하지 않고 에너지 저장
                for (x, y), d, e in atom:
                    if (dx, dy) == (x, y) and dxy[atom[now][1]] == (dxy[d][0]*-1, dxy[d][1]*-1):
                        sum_energy += e
                        break
                else:
                    if flg == 1:
                        # print([[dx, dy], atom[now][1], atom[now][2]])
                        future.append([[dx, dy], atom[now][1], atom[now][2]])
        atom = []
        for nxt in range(len(future)):
            if abs(future[nxt][0][0]) <= 1000 and abs(future[nxt][0][1]) <= 1000:
                atom.append(future[nxt])

    print(f"#{test_case} {sum_energy}")