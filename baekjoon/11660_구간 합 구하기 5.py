import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]

# 누적합
sums = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sums[i][j] = sums[i][j - 1] + nums[i - 1][j - 1]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sums[j][i] += sums[j - 1][i]

# 쿼리 진행
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sums[x2][y2] - sums[x2][y1 - 1] - sums[x1 - 1][y2] + sums[x1 - 1][y1 - 1])
