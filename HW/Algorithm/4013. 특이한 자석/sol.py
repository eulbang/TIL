import sys
sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    K = int(input())
    magnet = [deque(map(int, input().split())) for _ in range(4)]
    rotate = deque([list(map(int, input().split())) for _ in range(K)])

    for i in range(4):
        magnet[i] = deque(magnet[i])
    rotate = deque(rotate)

    while rotate:
        start, RL = rotate.popleft()
        s = start - 1
        note = [0] * 4
        note[s] = RL

        for i in range(s, 3):
            if magnet[i][2] != magnet[i + 1][6]:
                note[i + 1] = -note[i]
            else:
                break
        for i in range(s, 0, -1):
            if magnet[i][6] != magnet[i - 1][2]:
                note[i - 1] = -note[i]
            else:
                break
        for i in range(4):
            magnet[i].rotate(note[i])

    res = magnet[0][0] + (magnet[1][0] * 2) + (magnet[2][0] * 4) + (magnet[3][0] * 8)
    print(f"#{test_case} {res}")