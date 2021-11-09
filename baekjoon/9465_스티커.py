import sys 
input = sys.stdin.readline

# 파싱
t = int(input())
for i in range(t):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(2)]
    
    # dp
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = nums[0][0]
    dp[1][0] = nums[1][0]
    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + nums[0][i])
        dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] + nums[1][i])
    
    print(max(dp[0][n - 1], dp[1][n - 1]))
