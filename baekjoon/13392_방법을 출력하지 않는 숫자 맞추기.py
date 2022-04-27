import sys
input = sys.stdin.readline
inf = int(1e9)

# 파싱
n = int(input())
now = list(map(int, list(input().rstrip())))
goal = list(map(int, list(input().rstrip())))

# 회전수 체크
dp = [[inf] * 10 for _ in range(n + 1)]
for i in range(10):
    dp[0][i] = i
    
for i in range(n):
    for j in range(10):
        left = (goal[i] + (20 - (now[i] + j))) % 10
        right = 10 - left
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + right)
        dp[i + 1][(j + left) % 10] = min(dp[i + 1][(j + left) % 10], dp[i][j] + left)

# 결과 출력
print(min(dp[n]))
