from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
inf = 1000000000

# 파싱
n, m = map(int, input().split())
dic = defaultdict(set)
for _ in range(m):
    a, b, t = map(int, input().split())
    dic[a].add((b, t))
    dic[b].add((a, t))
    
# 다익스트라
dist = [inf] * (n + 1)
dist[1] = 0
visited = [False] * (n + 1)
update = [0] * (n + 1)

queue = [(0, 1)]
while queue:
    # 방문 안한 최소 찾기
    total, target = heappop(queue)
    
    if not visited[target]:
        # 최소값 갱신
        visited[target] = True
        for i, d in dic[target]:
            cost = dist[target] + d
            if cost < dist[i]:
                update[i] = target
                dist[i] = cost
                heappush(queue, (total + d, i))

# 경로 계산
route = []
now = n
while now:
    route.append(now)
    now = update[now]

# 하나씩 지우며 지연시간 체크
low = dist[n]
answer = 0
for i in range(len(route) - 1):
    # 값 체크
    a, b = route[i], route[i + 1]
    t = 0
    for j, d in dic[a]:
        if j == b:
            t = d
            break
    
    # 거리 지우기 
    dic[a].remove((b, t))
    dic[b].remove((a, t))
    
    # 다익스트라
    dist = [inf] * (n + 1)
    dist[1] = 0
    visited = [False] * (n + 1)
    
    queue = [(0, 1)]
    while queue:
        # 방문 안한 최소 찾기
        total, target = heappop(queue)
        
        if not visited[target]:
            # 최소값 갱신
            visited[target] = True
            for i, d in dic[target]:
                cost = dist[target] + d
                if cost < dist[i]:
                    dist[i] = cost
                    heappush(queue, (total + d, i))
    
    # 아예 초과하는 경우
    if dist[n] == inf:
        answer = -1
        break
    
    # 지연시간 체크
    answer = max(answer, dist[n] - low)
    
    # 거리 복구
    dic[a].add((b, t))
    dic[b].add((a, t))

# 결과 출력
print(answer)
