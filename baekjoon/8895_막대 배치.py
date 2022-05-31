import sys
input = sys.stdin.readline

# 파싱
t = int(input())

# dp
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
dp[1][1][1] = 1
for i in range(2, 21):
    for j in range(1, i + 1):
        for k in range(1, i + 1):
            dp[i][j][k] = dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] + dp[i - 1][j][k] * (i - 2)

# 케이스별 진행
for _ in range(t):
    n, l, r = map(int, input().split())
    
    # 결과 출력
    print(dp[n][l][r])
