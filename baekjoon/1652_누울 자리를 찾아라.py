import sys
input = sys.stdin.readline

# 파싱
n = int(input())
table = [input().rstrip() for _ in range(n)]
row, col = 0, 0

# 계산
for i in table:
    for j in i.split("X"):
        if len(j) >= 2:
            row += 1
for i in map(lambda x : "".join(x), zip(*table)):
    for j in i.split("X"):
        if len(j) >= 2:
            col += 1

# 결과 출력
print(row, col)
