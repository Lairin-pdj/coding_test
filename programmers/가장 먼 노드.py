from collections import defaultdict, deque

def solution(n, edge):
    check = [0 for _ in range(n + 1)]           # 시작점에서의 거리를 측정
    
    graph = defaultdict(set)
    
    for a, b in edge:                           # 사전을 통해 연결된 모든 점을 리스트화
        graph[a].add(b)
        graph[b].add(a)
    
    queue = deque()         
    queue.append([1, 0])
    route = set()                               # 집합을 이용해 중복 체크하는 경우 제거
    route.add(1)
    while len(queue) > 0:                       # 큐를 통해 bfs 진행
        now, length = queue.popleft()
        for i in graph[now] - route:            # 차집합으로 남은 노드 진행
            route.add(i)
            queue.append([i, length + 1])
            check[i] = length + 1               # 방문한 노드의 거리 체크
                
    return check.count(max(check))              # 최대치의 노드 갯수 반환
