import sys
input = sys.stdin.readline

# 파싱
n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]

# dp
dp = [0 for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    if i + work[i][0] <= n:
        dp[i] = max(dp[i + 1], dp[i + work[i][0]] + work[i][1])
    else:
        dp[i] = dp[i + 1]

# 결과 출력
print(dp[0])
