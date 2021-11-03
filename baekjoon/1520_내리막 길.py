import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

def dfs(x, y):
    ver = [-1, 0, 0, 1]
    hor = [0, 1, -1, 0]
    
    if x == m - 1 and y == n - 1:
        return 1
        
    if d[x][y] != -1:
        return d[x][y]
    d[x][y] = 0
    
    for i in range(4):
        ax = x + ver[i]
        ay = y + hor[i]
        if 0 <= ax < m and 0 <= ay < n:
            if h[x][y] > h[ax][ay]:
                d[x][y] += dfs(ax, ay)
                
    return d[x][y]

# 파싱
m, n = map(int, input().split(" "))
h = [list(map(int, input().split(" "))) for _ in range(m)]

# 가지수 체크 리스트
d = [[-1 for _ in range(n)] for _ in range(m)]

# dfs 및 결과 출력
print(dfs(0, 0))
