import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    M, A = map(int, input().split())
    A_route = list(map(int, input().split()))
    B_route = list(map(int, input().split()))
    charger = [list(map(int, input().split())) for _ in range(A)]

    # 이제 충전소 입력 받는데 2차원 리스트에 인자로 리스트를 넣고
    # 닿는 충전소들의 출력을 넣어둔다? 어느 충전소인지도 알아야 하네
    # 그럼 area[10][10][[출력][충전소]] ? 미친건가

    area = [[[] for _ in range(10)] for _ in range(10)]
    print(area)

    # print(f"{test_case} {}")