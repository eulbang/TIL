import sys
sys.stdin = open('sample_input.txt', 'r')
#
# N개의
# 나무가
# 있다.초기의
# 각
# 나무의
# 키가
# 주어진다.
#
# 하루에
# 한
# 나무에
# 물을
# 줄
# 수
# 있다.
#
# 첫
# 날은
# 물을
# 준
# 나무의
# 키가
# 1
# 자라고, 둘째
# 날은
# 물을
# 준
# 나무의
# 키가
# 2
# 자라고,
#
# 셋째
# 날은
# 물을
# 준
# 나무의
# 키가
# 1
# 자라는
# 식으로, 홀수
# 번째
# 날은
# 키가
# 1
# 자라고
# 짝수
# 번째
# 날은
# 키가
# 2
# 자란다.
#
# 모든
# 나무의
# 키가
# 처음에
# 가장
# 키가
# 컸던
# 나무와
# 같아지도록
# 할
# 수
# 있는
# 최소
# 날짜
# 수를
# 계산하라.
#
# 어떤
# 날에는
# 물을
# 주는
# 것을
# 하지
# 않을
# 수도
# 있다.
#
# 예를
# 들어
# 나무가
# 2
# 그루이고
# 각각의
# 높이가
# 4
# 와
# 2
# 라고
# 하자.
#
# 첫째
# 날에
# 물을
# 주게
# 되면, 나무의
# 높이를
# 모두
# 4
# 로
# 만들기
# 위해서는
# 3
# 일째까지
# 물을
# 주어야
# 한다.
#
# 둘째
# 날은
# 아무
# 일도
# 안
# 하게
# 된다.하지만, 첫째
# 날을
# 쉬고
# 둘째
# 날에
# 물을
# 주면
# 2
# 일
# 만에
# 나무의
# 높이가
# 모두
# 4
# 가
# 된다.
#
# [제약사항]
#
# 1.
# 나무의
# 개수
# N은
# 2
# 이상
# 100
# 이하이다.(2 ≤ N ≤ 100)
#
# 2.
# 주어지는
# 나무의
# 초기
# 높이는
# 1
# 이상
# 120
# 이하이다.
#
# [입력]
#
# 가장
# 첫
# 줄에는
# 테스트
# 케이스의
# 총
# 수가
# 주어진다.
#
# 그
# 다음
# 줄부터
# 각
# 테스트
# 케이스가
# 주어지며, 각
# 테스트
# 케이스는
# 2
# 줄로
# 구성된다.
#
# 각
# 테스트
# 케이스의
# 첫째
# 줄에는
# 나무의
# 개수
# N이
# 주어진다.
#
# 다음
# 줄에는
# 나무들의
# 높이가
# N개의
# 자연수로
# 주어진다.
#
# [출력]
#
# 출력의
# 각
# 줄은 ‘  # x’로 시작하고, 공백을 한 칸 둔 다음 가능한 최소 날짜 수를 출력한다.
#
#
# 단, x는
# 테스트
# 케이스의
# 번호이다.
#
# [입력 예]
#
# 5 // 테스트
# 케이스의
# 수
#
# 2 // N = 2, 테스트
# 케이스  # 1
#
# 5
# 5
#
# 2 // N = 2, 테스트
# 케이스  # 2
#
# 4
# 2
#
# 2 // N = 2, 테스트
# 케이스  # 3
#
# 3
# 4
#
# 4 // N = 4, 테스트
# 케이스  # 4
#
# 2
# 3
# 10
# 5
#
# 4 // N = 4, 테스트
# 케이스  # 5
#
# 1
# 2
# 3
# 4
#
# [출력 예]
#
# # 1 0
#
# # 2 2
#
# # 3 1
#
# # 4 14
#
# # 5 4

# def grow(date, now_tree, watered):
#     global min_date, N
#
#     if date > 1000:
#         return
#
#     flg = True
#     for i in range(N-1):
#         if now_tree[i] != now_tree[i+1]:
#             flg = False
#             break
#     if flg:
#         min_date = min(min_date, date)
#         return
#
#     for i in range(N):
#         if watered[i] != 0:
#             watered[i] += 1
#             now_tree[i] += watered[i] % 2 + 1
#
#     for i in range(N):
#         if now_tree[i] == min(now_tree) and watered[i] == 0:
#             if sum(watered) != 0:
#                 grow(date+1, now_tree, watered)
#             now_tree[i] += 1
#             watered[i] = 1
#             grow(date+1, now_tree, watered)
#             now_tree[i] -= 1
#             watered[i] = 0
#
#     return

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    in_tree = list(map(int, input().split()))
    tree = []
    for i in range(N):
        tree.append(in_tree[i])
    print(tree)
    watered = [0]*N

    min_date = 9999

    now_tree = tree

    # grow(0, now_tree, watered)

    # while True:
    #     pass

    print(f'#{test_case} {min_date}')