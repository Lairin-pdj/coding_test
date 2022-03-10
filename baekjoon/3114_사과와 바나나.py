import sys
input = sys.stdin.readline

# 파싱
r, c = map(int, input().split())
apple = [[0] * c for _ in range(r)]
banana = [[0] * c for _ in range(r)]
for i in range(r):
    line = input().split()
    for j in range(c):
        if line[j][0] == "A":
            apple[i][j] = int(line[j][1:])
        else:
            banana[i][j] = int(line[j][1:])

# 누적합
# 바나나는 위에서 아래로
for i in range(c):
    for j in range(1, r):
        banana[j][i] += banana[j - 1][i]
# 사과는 왼쪽에서 오른쪽으로
for i in range(r):
    for j in range(1, c):
        apple[i][j] += apple[i][j - 1]

# dp
dp = [[0] * c for _ in range(r)]
# 왼쪽, 위쪽, 왼쪽 위 중 최대 값이 되는 경우를 체크
for i in range(1, r):
    for j in range(1, c):
        left = dp[i][j - 1] + banana[i - 1][j]
        up = dp[i - 1][j] + apple[i][j - 1]
        mix = dp[i - 1][j - 1] + apple[i][j - 1] + banana[i - 1][j]
        dp[i][j] = max(left, up, mix)

# 결과 출력
print(dp[r - 1][c - 1])
