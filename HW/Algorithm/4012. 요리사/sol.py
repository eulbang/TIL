import sys
sys.stdin = open('sample_input.txt')

def solve_case(area):
    """
    area: N x N 시너지 행렬 (SWEA 4012)
    반환값: 두 팀(A,B)을 N/2명씩 나눴을 때, 팀 내부 시너지 합의 차이의 최솟값
    """
    N = len(area)

    # 1) 대칭합 전처리: pair[i][j] = S[i][j] + S[j][i]
    #    팀 내부의 (i<j) 쌍만 더하면 됨
    pair = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            pair[i][j] = pair[j][i] = area[i][j] + area[j][i]

    ans = float('inf')

    # 2) 백트래킹으로 A팀을 고른다.
    #    대칭 제거를 위해 0번을 A팀에 '고정' → 탐색량 절반으로 감소
    chosen = [0]  # A팀 구성원 리스트(사람 인덱스), 0번을 미리 넣어둠

    def eval_diff():
        """현재 chosen(A팀) 기준으로 A/B 팀 내부 시너지 합을 계산해 차이로 ans 갱신"""
        nonlocal ans
        A = chosen
        # 보완집합 B = 전체 - A
        Aset = set(A)
        B = [i for i in range(N) if i not in Aset]

        # A팀 내부 쌍 합
        sumA = 0
        for ai in range(len(A)):
            i_idx = A[ai]
            for aj in range(ai + 1, len(A)):
                j_idx = A[aj]
                sumA += pair[i_idx][j_idx]

        # B팀 내부 쌍 합
        sumB = 0
        for bi in range(len(B)):
            i_idx = B[bi]
            for bj in range(bi + 1, len(B)):
                j_idx = B[bj]
                sumB += pair[i_idx][j_idx]

        ans = min(ans, abs(sumA - sumB))

    def dfs(start):
        """
        start: 다음으로 선택을 고려할 사람 인덱스 (증가하는 순서로만 선택 → 중복/순서 제거)
        chosen: 현재까지 A팀에 선택된 사람들 (0번 포함)
        목표: len(chosen) == N//2 가 되면 평가
        """
        # A팀이 목표 인원(N//2)에 도달하면 평가
        if len(chosen) == N // 2:
            eval_diff()
            return

        # 다음 후보를 1..N-1 범위에서 오름차순으로 선택 (0은 이미 포함)
        for i in range(start, N):
            # 0 고정 최적화 때문에 start는 최소 1에서 시작
            if i in chosen:
                continue
            chosen.append(i)
            dfs(i + 1)
            chosen.pop()

    # 0을 고정했으므로 다음 후보는 1부터
    dfs(1)
    return ans


T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    area = [list(map(int, input().split())) for _ in range(N)]
    ans = solve_case(area)
    print(f"#{tc} {ans}")
