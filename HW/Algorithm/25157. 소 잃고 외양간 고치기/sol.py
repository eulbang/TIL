import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())    # 외양간의 수, 총 기간
    LiDi = [list(map(int, input().split())) for _ in range(N)]  # [손실량, 수리 기간]
    dAd = [list(map(int, input().split())) for _ in range(M)]   # 공격 순서

    # 공격은 매일 온다
    # 수리하는데 시간이 걸린다
    # 수리 기간만큼 공격받는 외양간이 쌓인다
    # 이미 파손된 외양간을 또 공격하면? 안 쌓여야 하는디?
    # 어떤 외양간을 먼저 수리할지 그리디? 재귀?
    # 수리 대기중인 외양간을 리스트로 관리해서 재귀로 보낸다
    # 수리 중인 외양간의 인덱스와 걸린 시간도 보낸다
    # 누적 날짜도 보낸다. 최소 손실 갱신해야 한다.


    # print(f"#{test_case} {}")