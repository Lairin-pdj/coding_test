from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n, m, k = map(int, input().split())
table = [list(map(int, list(input().rstrip()))) for _ in range(n)]

# bfs
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
queue = deque([(0, 0, 1)])
visited = [[2000] * m for _ in range(n)]
visited[0][0] = 0
flag = True
while queue:
    x, y, count = queue.popleft()
    
    # 탈출
    if (x, y) == (n - 1, m - 1):
        print(count)
        flag = False
        break
    
    # 4방향 이동
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        
        # 좌표 체크
        if 0 <= ax < n and 0 <= ay < m:
            # 벽 여부
            temp = table[ax][ay] + visited[x][y]
            if temp < visited[ax][ay] and temp <= k:
                queue.append((ax, ay, count + 1))
                visited[ax][ay] = temp

# 실패시
if flag:
    print(-1)
