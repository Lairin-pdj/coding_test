import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

# 가능한 모양 체크
techs = set()
for i in [[[1, 1, 1, 1]], [[1, 1], [1, 1]], [[1, 0], [1, 0], [1, 1]], [[1, 1], [1, 0], [1, 0]], [[1, 0], [1, 1], [0, 1]], [[0, 1], [1, 1], [1, 0]], [[0, 1], [1, 1], [0, 1]]]:
    for _ in range(4):
        i = tuple(map(tuple, zip(*i[::-1])))
        techs.add(i)

# 각 모양마다 체크
count = 0
for tech in techs:
    x, y = len(tech), len(tech[0])
    for i in range(n - x + 1):
        for j in range(m - y + 1):
            temp = 0
            for kx in range(x):
                for ky in range(y):
                    if tech[kx][ky] == 1:
                        temp += paper[i + kx][j + ky]
                
            count = max(temp, count)

# 결과 출력
print(count)
