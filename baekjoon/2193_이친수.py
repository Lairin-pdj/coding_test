import sys
input = sys.stdin.readline

# 파싱
n = int(input())
dp = [[0 for _ in range(n + 1)] for _ in range(2)]
dp[1][1] = 1

# dp
for i in range(2, n + 1):
    dp[0][i] = dp[0][i - 1] + dp[1][i - 1]
    dp[1][i] = dp[0][i - 1]

# 결과 출력
print(dp[0][n] + dp[1][n])
