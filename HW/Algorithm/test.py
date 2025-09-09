from collections import deque

while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1 and arr[0] == 0:
        break
    N = len(arr)
    mx = 0
    # 스택에 높이와 인덱스를 저장해두고 top 보다 낮아지면 사각형이 마감
    stk = deque()
    stk.append([arr[0], 0])

    for i in range(1, N):
        if arr[i]

    # for i in range(N):
    #     height, length = True, 0
    #     while height:
    #         if height and i-length > 0 and arr[i-length] >= arr[i]:
    #             length += 1
    #         else:
    #             height = False
    #     mx = max(mx, arr[i]*length)
    #     height, length = True, 0
    #     while height:
    #         if height and i+length < N and arr[i+length] >= arr[i]:
    #             length += 1
    #         else:
    #             height = False
    #     mx = max(mx, arr[i]*length)

    print(mx)