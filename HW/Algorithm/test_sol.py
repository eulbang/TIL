N = int(input())

if N == 1:
    print(9)
else:
    prev = [0]*10
    for d in range(1, 10):
        prev[d] = 1

    for _ in range(2, N+1):
        cur = [0]*10
        cur[0] = prev[1] % 1000000000
        cur[9] = prev[8] % 1000000000
        for d in range(1, 9):
            cur[d] = (prev[d-1] + prev[d+1]) % 1000000000
        prev = cur

    print(sum(prev) % 1000000000)