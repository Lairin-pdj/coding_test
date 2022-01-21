import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())

# 2 * 5 = 10 의 갯수 체크
# [n, m, n - m]
# 5의 갯수
count5 = [0, 0, 0]
for i, x in enumerate([n, m, n - m]):
    while x > 0:
        count5[i] += x // 5
        x = x // 5

# 2의 갯수
count2 = [0, 0, 0]
for i, x in enumerate([n, m, n - m]):
    while x > 0:
        count2[i] += x // 2
        x = x // 2

# 결과 출력
print(min(count5[0] - count5[1] - count5[2], count2[0] - count2[1] - count2[2]))
