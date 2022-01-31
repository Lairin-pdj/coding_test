import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
rec = [input().rstrip() for _ in range(n)]

# 좌상단의 점 기준으로 정사각형 모두 체크
count = 1
for i in range(n):
    for j in range(m):
        for k in range(min(n - i, m - j)):
            if rec[i][j] == rec[i][j + k] == rec[i + k][j] == rec[i + k][j + k]:
                count = max(count, k + 1)

# 결과 출력
print(count ** 2)
