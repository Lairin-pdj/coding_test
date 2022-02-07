from collections import deque
import sys
input = sys.stdin.readline

# 파싱
m, n, h = map(int, input().split())
chango = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 익은 토마토 체크
space = 0
total = 0
queue = deque()
for i in range(n):
    for j in range(m):
        for k in range(h):
            if chango[k][i][j] == 1:
                queue.append((i, j, k, 0))
                total += 1
            elif chango[k][i][j] == -1:
                space += 1

# 익은 토마토 기준 bfs 진행
dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
answer = 0
while queue:
    x, y, z, count = queue.popleft()

    for i in range(6):
        ax = x + dx[i]
        ay = y + dy[i]
        az = z + dz[i]

        if 0 <= ax < n and 0 <= ay < m and 0 <= az < h and chango[az][ax][ay] == 0:
            chango[az][ax][ay] = 1
            total += 1
            queue.append((ax, ay, az, count + 1))

# 결과 출력
if m * n * h == space + total:
    print(count)
else:
    print(-1)
