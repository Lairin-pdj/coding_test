import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# 상어 체크
sharks = set()
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            sharks.add((i, j))

# 거리 체크
answer = 0
for i in range(n):
    for j in range(m):
        temp = 50
        for a, b in sharks:
            temp = min(temp, max(abs(i - a), abs(j - b)))
        answer = max(temp, answer)

# 결과 출력
print(answer)
