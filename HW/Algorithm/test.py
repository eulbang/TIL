from collections import deque
import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if not arr:
        break
    n = arr[0]
    if n == 0:
        break
    heights = arr[1:]

    mx = 0
    stk = deque()  # 각 원소: [height, start_idx]

    # 끝에 0(센티넬) 추가해 남은 막대들 강제 팝
    for i, h in enumerate(heights + [0]):
        start = i
        # 현재 높이 h보다 큰 막대는 여기서 마감
        while stk and stk[-1][0] > h:
            ph, ps = stk.pop()
            mx = max(mx, ph * (i - ps))  # 폭 = 현재 i - 시작 인덱스
            start = ps                   # 더 낮은 막대가 이어질 경우 시작점 당겨오기
        # 스택이 비었거나 엄격히 증가할 때만 푸시(같은 높이는 묶여 확장됨)
        if not stk or stk[-1][0] < h:
            stk.append([h, start])

    print(mx)