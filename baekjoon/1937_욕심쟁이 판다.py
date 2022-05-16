import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

# 파싱
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
count = [[0] * n for _ in range(n)]

# dfs
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def dfs(x, y):
    
    # 이미 방문하여 계산한 경우
    if count[x][y] != 0:
        return count[x][y]
    
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        
        if 0 <= ax < n and 0 <= ay < n:
            if table[x][y] < table[ax][ay]:
                count[x][y] = max(count[x][y], dfs(ax, ay) + 1)
    
    return count[x][y]

# dfs 실행
answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

# 결과 출력
print(answer + 1)
