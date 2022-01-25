import sys
input = sys.stdin.readline

# 파싱
n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

# dp
dp = [0 for _ in range(k + 1)]
dp[0] = 1
for coin in nums:
    for i in range(1, k + 1):
        if i - coin >= 0:
            dp[i] += dp[i - coin]

# 결과 출력
print(dp[-1])
