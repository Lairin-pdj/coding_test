from collections import deque
import sys
input = sys.stdin.readline


# 파싱
w, h = map(int, input().split())
table = [[1000000000] * w for _ in range(h)]
c = []
for i in range(h):
    line = input().rstrip()
    for j in range(w):
        if line[j] == "C":
            c.append((i, j))
        elif line[j] == "*":
            table[i][j] = -1

# bfs
queue = deque([(c[0][0], c[0][1], -1, 0)])
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
while queue:
    x, y, d, count = queue.popleft()
    
    if (x, y) != c[1] and table[x][y] >= count:
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            
            if 0 <= ax < h and 0 <= ay < w and table[ax][ay] != -1:
                if d != -1 and d != i:
                    table[ax][ay] = min(table[ax][ay], count + 1)
                    queue.append((ax, ay, i, count + 1))
                else:
                    table[ax][ay] = min(table[ax][ay], count)
                    queue.append((ax, ay, i, count))

# 결과 출력
print(table[c[1][0]][c[1][1]])
