import sys
input = sys.stdin.readline

# 파싱
r, c = map(int, input().split())
maps = [input().rstrip() for _ in range(r)]

# bfs
answer = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
queue = set([(0, 0, maps[0][0])])
while queue:
    x, y, route = queue.pop()
    answer = max(answer, len(route))
    
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        if 0 <= ax < r and 0 <= ay < c and maps[ax][ay] not in route:
            queue.add((ax, ay, route + maps[ax][ay]))

# 결과 출력
print(answer)
