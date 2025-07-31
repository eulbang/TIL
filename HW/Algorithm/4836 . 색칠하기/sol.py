import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    area = [[0] * 30 for _ in range(30)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if area[r][c] == 0:
                    area[r][c] = color
                elif area[r][c] != color and area[r][c] != 3:
                    area[r][c] = 3

    cnt = sum(row.count(3) for row in area)
    print(f"#{test_case} {cnt}")