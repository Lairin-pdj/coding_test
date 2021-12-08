import sys
input = sys.stdin.readline

# 파싱
n = int(input())
high = 0
nums = []
for _ in range(n):
    temp = int(input())
    high = max(high, temp)
    nums.append(temp)

# dp
dp = [1 for _ in range(high + 1)]
if high > 1:
    dp[2] = 2
for i in range(3, high + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

# 결과 출력
for i in nums:
    print(dp[i])
