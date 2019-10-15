def CMM(p, n):
    dp = [[0] * n for _ in range(n)]
    for L in range(1, n-1):
        for i in range(1, n-L):
            j = i+L
            dp[i][j] = float('inf')
            for k in range(i, j):
                print(i, j, k)
                q = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
                if q < dp[i][j]:
                    dp[i][j] = q
    for i in dp:
        print(i)
    return dp[1][-1]

p = [40, 20, 30, 10, 30]
print(CMM(p, len(p)))