import sys
input = sys.stdin.readline
inf = int(1e9)
empty = None

# 파싱
n = int(input())
now = list(map(int, list(input().rstrip())))
goal = list(map(int, list(input().rstrip())))

# dp
dp = [[inf] * 10 for _ in range(n + 1)]
history = [[empty] * 10 for _ in range(n)]
dp[0][0] = 0

# 회전 수 체크
for i in range(n):
    for j in range(10):
        # 목표 까지 왼쪽으로 돌릴 경우 들어가는 회전 수
        left = (goal[i] + (20 - (now[i] + j))) % 10
        if dp[i + 1][(j + left) % 10] > dp[i][j] + left:
            dp[i + 1][(j + left) % 10] = dp[i][j] + left
            history[i][(j + left) % 10] = (j, left)
        
        # 목표 까지 오른쪽으로 돌릴 경우 들어가는 회전 수
        right = 10 - left
        if dp[i + 1][j] > dp[i][j] + right:
            dp[i + 1][j] = dp[i][j] + right
            history[i][j] = (j, -right)

# 횟수 출력
total = min(dp[n])
print(total)

# 역추적
idx = dp[n].index(total)
route = []
for i in range(n - 1, -1, -1):
    temp = history[i][idx]
    idx = temp[0]
    route.append(temp[1])

# 경로 출력
for i in range(n - 1, -1, -1):
    print(n - i, route[i])
