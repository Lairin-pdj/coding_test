from collections import defaultdict, deque
import sys
input = sys.stdin.readline
    
# 파싱
n, start, end, m = map(int, input().split())
dic = defaultdict(lambda : defaultdict(int))
temp = []
for _ in range(m):
    temp.append(tuple(map(int, input().split())))
earn = list(map(int, input().split()))

# 거리 정산
for a, b, cost in temp:
    if b in dic[a]:
        dic[a][b] = max(dic[a][b], earn[b] - cost)
    else:
        dic[a][b] = earn[b] - cost

# bfs를 이용한 도착 여부 체크
check = True
queue = deque([start])
visited = set([start])

while queue:
    now = queue.popleft()
    
    if now == end:
        check = False
        break
    
    if now in dic:
        for j in dic[now]:
            if j not in visited:
                queue.append(j)
                visited.add(j)

# 도착 못할 경우
if check:
    print("gg")
# 도착 가능한 경우
else:

    # 벨만 포드
    dist = [-1000000000] * n
    dist[start] = earn[start]
    for _ in range(n - 1):
        for i in dic:
            for to in dic[i]:
                if dist[to] < dic[i][to] + dist[i]:
                    dist[to] = dic[i][to] + dist[i]
    
    # 양수 사이클 체크
    cycle = False
    for i in dic:
        for to in dic[i]:
            if dist[to] < dic[i][to] + dist[i]:
                
                # bfs를 이용한 도착 여부 체크
                check = False
                queue = deque([start])
                visited = set([start])
                
                while queue:
                    now = queue.popleft()
                    
                    if now == i:
                        check = True
                    
                    if now in dic:
                        for j in dic[now]:
                            if j not in visited:
                                queue.append(j)
                                visited.add(j)
                
                if check:
                    queue = deque([to])
                    visited = set([to])
                    
                    while queue:
                        now = queue.popleft()
                        
                        if now == end:
                            cycle = True
                        
                        if now in dic:
                            for j in dic[now]:
                                if j not in visited:
                                    queue.append(j)
                                    visited.add(j)
    
    # 결과 출력
    if cycle:
        print("Gee")
    else:
        print(dist[end])
