import sys
input = sys.stdin.readline

# 파싱
n = int(input())

# dp
dp = [4 for _ in range(n + 1)]
for i in range(1, int(n ** 0.5) + 1):
    dp[i ** 2] = 1
for i in range(2, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - (j ** 2)] + 1)

# 결과 출력
print(dp[n])
