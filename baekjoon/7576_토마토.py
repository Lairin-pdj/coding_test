from collections import deque
import sys
input = sys.stdin.readline

# 파싱
m, n = map(int, input().split())
chango = [list(map(int, input().split())) for _ in range(n)]

# 익은 토마토 체크
space = 0
total = 0
queue = deque()
for i in range(n):
    for j in range(m):
        if chango[i][j] == 1:
            queue.append((i, j, 0))
            total += 1
        elif chango[i][j] == -1:
            space += 1

# 익은 토마토 기준 bfs 진행
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
answer = 0
while queue:
    x, y, count = queue.popleft()
    
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        
        if 0 <= ax < n and 0 <= ay < m and chango[ax][ay] == 0:
            chango[ax][ay] = 1
            total += 1
            queue.append((ax, ay, count + 1))

# 결과 출력
if m * n == space + total:
    print(count)
else:
    print(-1)
