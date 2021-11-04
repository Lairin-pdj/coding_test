import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

# 냅색 공간
bag = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# 냅색 dp
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j < items[i - 1][0]:
            bag[i][j] = bag[i - 1][j]
        else:
            bag[i][j] = max(bag[i - 1][j], bag[i - 1][j - items[i - 1][0]] + items[i - 1][1])

# 결과 출력
print(bag[n][m])
