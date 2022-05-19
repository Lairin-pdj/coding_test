from heapq import heappush, heappop
import sys
input = sys.stdin.readline
inf = 1e9

# 높이 변환 함수
def high(n):
    if n == n.lower():
        return ord(n) - 71
    else:
        return ord(n) - 65

# 파싱
n, m, t, d = map(int, input().split())
table = [list(map(lambda x : high(x), input().rstrip())) for _ in range(n)]

# 다익스트라
dist = [[inf] * m for _ in range(n)]
dist[0][0] = 0
visited = [[False] * m for _ in range(n)]

queue = [(0, 0, 0)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
while queue:
    # 방문 안한 최소 찾기
    total, x, y = heappop(queue)
    
    if not visited[x][y]:
        # 최소값 갱신
        visited[x][y] = True
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            
            if 0 <= ax < n and 0 <= ay < m:
                temp = table[ax][ay] - table[x][y]
                if abs(temp) <= t:
                    if temp > 0:
                        cost = dist[x][y] + temp ** 2
                        if cost < dist[ax][ay]:
                            dist[ax][ay] = cost
                            heappush(queue, (total + temp ** 2, ax, ay))
                    else:
                        cost = dist[x][y] + 1
                        if cost < dist[ax][ay]:
                            dist[ax][ay] = cost
                            heappush(queue, (total + 1, ax, ay))

# 다시 돌아올 수 있는지 체크
answer = 0
for i in range(n):
    for j in range(m):
        queue = [(0, i, j)]
        visited = [[False] * m for _ in range(n)]
        
        while queue:
            total, x, y = heappop(queue)
            
            # 도착 한 경우
            if (x, y) == (0, 0):
                if total + dist[i][j] <= d:
                    answer = max(answer, table[i][j])
                break
            
            if not visited[x][y]:
                # 최소값 갱신
                visited[x][y] = True
                for k in range(4):
                    ax = x + dx[k]
                    ay = y + dy[k]
                    
                    if 0 <= ax < n and 0 <= ay < m:
                        temp = table[ax][ay] - table[x][y]
                        if abs(temp) <= t:
                            if temp > 0:
                                heappush(queue, (total + temp ** 2, ax, ay))
                            else:
                                heappush(queue, (total + 1, ax, ay))

# 결과 출력
print(answer)
