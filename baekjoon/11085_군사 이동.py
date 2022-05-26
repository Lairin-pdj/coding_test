from heapq import heappush, heappop
from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
p, w = map(int, input().split())
c, v = map(int, input().split())
dic = defaultdict(list)
for _ in range(w):
    s, e, width = map(int, input().split())
    dic[s].append([e, width])
    dic[e].append([s, width])

# bfs 체크
queue = [(-1000, c)]
visited = [0] * p
answer = 1000
while queue:
    total, now = heappop(queue)
    
    # 방문 체크
    if visited[now]:
        continue
    visited[now] = 1
    
    # 최대 체크
    answer = min(answer, -total)
    
    # 탈출 조건
    if now == v:
        break
    
    # 이동
    for to, cost in dic[now]:
        heappush(queue, (-cost, to))

# 결과 출력
print(answer)
