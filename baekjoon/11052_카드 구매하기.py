import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))

# dp
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + nums[j - 1])

# 결과 출력
print(dp[n])
