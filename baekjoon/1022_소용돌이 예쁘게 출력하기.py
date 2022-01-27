import sys
input = sys.stdin.readline

# 파싱
r1, c1, r2, c2 = map(int, input().split())
d = max(max(abs(r1), abs(r2)), max(abs(c1), abs(c2)))

# 배열 생성 
paper = [[1 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]

# 배열 숫자 적용
t = 1
n = 0
row = -r1 
col = -c1
cnt = 2
trans = 1
while t <= (2 * d) + 1:
    for _ in range(t):
        col += trans
        if 0 <= row <= (r2 - r1) and 0 <= col <= (c2 - c1):
            paper[row][col] = cnt
            n = max(n, cnt)
        cnt += 1
    for _ in range(t):
        row -= trans
        if 0 <= row <= (r2 - r1) and 0 <= col <= (c2 - c1):
            paper[row][col] = cnt
            n = max(n, cnt)
        cnt += 1
    t += 1
    trans *= -1

# 배열 부분 출력
for i in paper:
    for j in i:
        print(str(j).rjust(len(str(n))), end = " ")
    print()
