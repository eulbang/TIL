import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# 이동 방향: 0(정지), 1(상), 2(우), 3(하), 4(좌)
# 문제 정의에 맞춰 (x, y)에서 y가 위로 감소하도록 설정
dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

for test_case in range(1, T + 1):
    M, A = map(int, input().split())
    A_route = list(map(int, input().split()))   # 길이 M
    B_route = list(map(int, input().split()))   # 길이 M
    # charger[i] = [x, y, c, p] (1-indexed 좌표, 맨해튼 거리 c, 성능 p)
    charger = [list(map(int, input().split())) for _ in range(A)]

    # -------------------------------------------------------
    # 1) 사전 계산: 10x10 모든 칸에 대해, 접근 가능한 BC 인덱스 리스트
    #    area[y][x] = [bc_idx, ...]  (x,y 모두 1~10 편의, 내부 배열은 0~9 사용)
    # -------------------------------------------------------
    area = [[[] for _ in range(11)] for _ in range(11)]  # 1~10 인덱싱 쉽게

    for idx, (cx, cy, c, p) in enumerate(charger):
        # 모든 격자 칸을 훑어보며 맨해튼 거리로 커버되는 칸에 이 BC를 추가
        for y in range(1, 11):
            for x in range(1, 11):
                if abs(cx - x) + abs(cy - y) <= c:
                    area[y][x].append(idx)  # 이 칸에서 사용할 수 있는 BC

    # 각 BC의 성능 배열 (인덱스로 바로 접근)
    power = [p for (_, _, _, p) in charger]

    # -------------------------------------------------------
    # 2) 시뮬레이션: t=0(시작 위치) 포함하여 총 M+1번 충전
    #    A 시작 (1,1), B 시작 (10,10) — 문제 정의
    # -------------------------------------------------------
    ax, ay = 1, 1
    bx, by = 10, 10

    total = 0

    # t = 0 ~ M
    for t in range(M + 1):
        # 현재 위치에서 가능한 BC 후보
        a_list = area[ay][ax]
        b_list = area[by][bx]

        # 두 사람이 선택할 수 있는 조합 중 최대 합을 고른다.
        # 동일 BC를 선택하면 성능을 나눠 갖지만 총합은 p(그 BC의 성능)로 본다.
        best = 0
        if not a_list and not b_list:
            best = 0
        else:
            # "선택 안 함"도 고려(-1)
            a_choices = a_list if a_list else [-1]
            b_choices = b_list if b_list else [-1]

            for ai in a_choices:
                for bi in b_choices:
                    if ai == -1 and bi == -1:
                        cand = 0
                    elif ai == -1:
                        cand = power[bi]
                    elif bi == -1:
                        cand = power[ai]
                    else:
                        if ai == bi:
                            # 같은 BC를 고르면 둘이 나눠 갖지만 총합은 p
                            cand = power[ai]
                        else:
                            cand = power[ai] + power[bi]
                    if cand > best:
                        best = cand

        total += best

        # 다음 시점으로 이동 (t == M 이면 이동 없음)
        if t < M:
            da = A_route[t]
            db = B_route[t]
            ax += dx[da]
            ay += dy[da]
            bx += dx[db]
            by += dy[db]

    print(f"#{test_case} {total}")
