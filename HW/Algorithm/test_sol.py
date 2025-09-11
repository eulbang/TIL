from collections import deque

gears = [deque(map(int, input().strip())) for _ in range(4)]

K = int(input())
commands = [tuple(map(int, input().split())) for _ in range(K)]

for start, direction in commands:
    s = start - 1
    note = [0] * 4
    note[s] = direction

    for i in range(s, 3):
        if gears[i][2] != gears[i + 1][6]:
            note[i + 1] = -note[i]
        else:
            break

    for i in range(s, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            note[i - 1] = -note[i]
        else:
            break

    for i in range(4):
        if note[i] != 0:
            gears[i].rotate(note[i])

score = 0
weights = [1, 2, 4, 8]
for i in range(4):
    if gears[i][0] == 1:
        score += weights[i]

print(score)
