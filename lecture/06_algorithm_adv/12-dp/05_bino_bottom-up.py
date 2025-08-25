def bino(n, k):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k) + 1):
            if j == 0 or i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    return dp[n][k]

n = 5 
k = 2
print(bino(n, k))  # 출력: 10
