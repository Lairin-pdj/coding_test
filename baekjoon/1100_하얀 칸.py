import sys
input = sys.stdin.readline

# 파싱
table = [list(input().rstrip()) for _ in range(8)]

# 계산
count = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if table[i][j] == "F":
                count += 1

# 결과 출력
print(count)
