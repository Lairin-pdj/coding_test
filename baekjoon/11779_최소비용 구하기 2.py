import sys, heapq
input = sys.stdin.readline
    
# 파싱
n = int(input())
m = int(input())
dic = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    dic[a].append((b, d))

start, end = map(int, input().split())

# 다익스트라
dist = [1000000000] * (n + 1)
dist[start] = 0
visited = [False] * (n + 1)
update = [0] * (n + 1)

queue = [(0, start)]
while queue:
    # 방문 안한 최소 찾기
    total, target = heapq.heappop(queue)
    
    if not visited[target]:
        # 최소값 갱신
        visited[target] = True
        for i, d in dic[target]:
            cost = dist[target] + d
            if cost < dist[i]:
                update[i] = target
                dist[i] = cost
                heapq.heappush(queue, (total + d, i))

# 결과 계산
path = []
temp = end
while temp:
    path.append(temp)
    temp = update[temp]

# 결과 출력
print(dist[end])
print(len(path))
print(*path[::-1])
