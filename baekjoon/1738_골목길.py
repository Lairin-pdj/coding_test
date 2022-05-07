from collections import defaultdict, deque
import sys
input = sys.stdin.readline
inf = float("inf")
none = 0

# 파싱
n, m = map(int, input().split())
dic = defaultdict(lambda : defaultdict(int))
for _ in range(m):
    u, v, w = map(int, input().split())
    dic[u][v] = w
    
# bfs를 이용한 도착 여부 체크
check = True
queue = deque([1])
visited = set([1])
while queue:
    now = queue.popleft()
    
    if now == n:
        check = False
        break
    
    if now in dic:
        for j in dic[now]:
            if j not in visited:
                queue.append(j)
                visited.add(j)

# 도착 못할 경우
if check:
    print(-1)
else:
    
    # 벨만 포드
    dist = [-inf] * (n + 1)
    history = [none] * (n + 1)
    dist[1] = 0
    for _ in range(n - 1):
        for i in dic:
            for to in dic[i]:
                if dic[i][to] + dist[i] > dist[to]:
                    dist[to] = dic[i][to] + dist[i]
                    history[to] = i
    
    # 사이클 체크
    cycle = False
    for i in dic:
        for to in dic[i]:
            if dic[i][to] + dist[i] > dist[to]:
                
                # bfs를 이용한 도착 여부 체크
                queue = deque([to])
                visited = set([to])
                
                while queue:
                    now = queue.popleft()
                    
                    if now == n:
                        cycle = True
                        break
                    
                    if now in dic:
                        for j in dic[now]:
                            if j not in visited:
                                queue.append(j)
                                visited.add(j)
            
            # 사이클일 경우 체크하지 말고 탈출 
            if cycle:
                break
        
        # 사이클일 경우 체크하지 말고 탈출
        if cycle:
            break
    
    # 결과출력
    if cycle:
        print(-1)
    else:
        temp = n
        answer = []
        while temp != 0:
            answer.append(temp)
            temp = history[temp]
        
        print(*answer[::-1])
