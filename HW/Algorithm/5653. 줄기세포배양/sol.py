import sys
sys.stdin = open('sample_input.txt')

# 입력받은 초기 줄기세포들이 자라날 수 있는 최대 크기의 배열 선언
    # (M+K+50)*(N+K+50)
    # (K, K) 위치부터 입력값 입력
# 세포의 상태(비활성화, 활성화, 사망) 저장할 배열 선언
    # maximum_area 와 동일한 크기, None 으로 초기화
    # 번식 시 상태 배열에 (cnt+생명력 값) 을 넣고 cnt 가 해당 값에 도달하면 활성화
    # 현 시점 활성화 된 세포 중 큰 세포부터 큐에 입력 -> 큰 값부터 돌아야 하니까 필요하긴 함
    # 큐를 기반으로 BFS는 아니고 그냥 상하좌우 입력
        # 다른 값이 있으면 번식X
    # 상태 배열의 값이 (cnt-생명력 값) 이 되면 사망하여 0 으로 변경
# cnt 가 K 가 되면 상태 배열에 0이 아니고 None 이 아닌 값의 수를 출력

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    start_area = [list(map(int, input().split())) for _ in range(N)]

    maximum_area = [[[] for _ in range(M+K+50)] for _ in range(M+K+50)]

    for y in range(N):
        for x in range(M):
            maximum_area[K+y][K+x] = start_area[y][x]

    time = 0

    # print(f"#{test_case} {}")
