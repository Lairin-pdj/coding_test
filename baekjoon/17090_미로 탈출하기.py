from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000)

# 파싱
n, m = map(int, input().split())
table = [input().rstrip() for _ in range(n)]

# 체크용 변수
check = [[False for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

# 재귀 함수 구현
dic = defaultdict(int)
dic["D"], dic["U"], dic["R"], dic["L"] = 0, 1, 2, 3
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def dfs(x, y):
    # 좌표 계산
    d = dic[table[x][y]]
    ax = x + dx[d]
    ay = y + dy[d]
    
    # 탈출 한 경우
    if not(0 <= ax < n) or not(0 <= ay < m):
        check[x][y] = True
        return True
    
    # 이미 방문한 경우(사이클 형성)
    if visited[ax][ay]:
        return False
    
    # 이미 탈출이 가능한 루트 인 경우
    if check[ax][ay]:
        check[x][y] = True
        return True
    
    # 이동 재귀
    visited[ax][ay] = True
    temp = dfs(ax, ay)
    visited[ax][ay] = False
    
    # 결과에 따라 변화
    if temp:
        check[x][y] = True
        return temp

# 각 칸마다 체크
for i in range(n):
    for j in range(m):
        if not check[i][j]:
            dfs(i, j)

# 결과 출력
answer = 0
for i in range(n):
    for j in range(m):
        if check[i][j]:
            answer += 1
print(answer)
