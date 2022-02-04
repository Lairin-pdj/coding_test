from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
miro = [input().rstrip() for _ in range(n)]

# bfs
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
check = set([(0, 0)])
queue = deque([(0, 0, 1)])
while queue:
    x, y, count = queue.popleft()
    
    # 결과 출력
    if x == n - 1 and y == m - 1:
        print(count)
        break
    
    # 4방향 이동
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        
        if (ax, ay) not in check and 0 <= ax < n and 0 <= ay < m and miro[ax][ay] == "1":
            check.add((ax, ay))
            queue.append((ax, ay, count + 1))
