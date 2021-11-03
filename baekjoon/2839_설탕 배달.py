n = int(input())

dp = [-1] * (n + 3)
dp[3] = 1
dp[5] = 1

for i in range(n - 2):
    if dp[i] != -1:
        if dp[i + 3] != -1:
            dp[i + 3] = min(dp[i + 3], dp[i] + 1)
        else:
            dp[i + 3] = dp[i] + 1
        
        if dp[i + 5] != -1:
            dp[i + 5] = min(dp[i + 5], dp[i] + 1)
        else:
            dp[i + 5] = dp[i] + 1

print(dp[n])
