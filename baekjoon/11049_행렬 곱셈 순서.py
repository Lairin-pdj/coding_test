import sys, math
input = sys.stdin.readline

# 파싱
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

# 2차원 dp
dp = [[0 for _ in range(n)] for _ in range(n)]

# 대각선으로 채워 나가기
for i in range(1, n):
    for j in range(n - i):
        if i == 1:
            dp[j][j + i] = m[j][0] * m[j + 1][0] * m[j + 1][1]
        else:
            # 최소 찾기
            dp[j][j + i] = math.inf
            for k in range(j, j + i):
                dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + (m[j][0] * m[k][1] * m[j + i][1]))

# 결과 출력
print(dp[0][-1])
