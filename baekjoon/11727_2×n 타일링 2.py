import sys
input = sys.stdin.readline

# 파싱
n = int(input())

# dp
dp = [1 for _ in range(n + 1)]
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007

# 결과 출력
print(dp[n])
