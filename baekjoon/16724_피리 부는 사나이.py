import sys
input = sys.stdin.readline
    
# 파싱
n, m = map(int, input().split())
table = [input().rstrip() for _ in range(n)]

# 2차원 분리 집합 함수
def find(x, y):
    if (x, y) != root[x][y]:
        root[x][y] = find(root[x][y][0], root[x][y][1])
    return root[x][y]

def union(x1, y1, x2, y2):
    temp = find(x2, y2)
    root[temp[0]][temp[1]] = find(x1, y1)

# 그룹화 진행
root = [[(i, j) for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if table[i][j] == "U":
            union(i - 1, j, i, j)
        elif table[i][j] == "L":
            union(i, j - 1, i, j)
        elif table[i][j] == "R":
            union(i, j + 1, i, j)
        elif table[i][j] == "D":
            union(i + 1, j, i, j)

# 그룹 체크
check = set()
for i in range(n):
    for j in range(m):
        check.add(find(i, j))

# 결과 출력
print(len(check))
