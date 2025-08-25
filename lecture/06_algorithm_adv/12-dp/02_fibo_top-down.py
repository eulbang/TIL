def fibo(N):
    if N >= 2 and memo[N] == 0:
        # memo[N] = memo[N-1] + memo[N-2]
        memo[N] = fibo(N-1) + fibo(N-2)
    return memo[N]

memo = [0] * 101
memo[1] = 1

res = fibo(100)
print(res)