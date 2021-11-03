from collections import defaultdict
import heapq

def solution(n, s, a, b, fares):
    answer = 0
    
    # 거리 환산표 생성
    dist = [[100000000 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][i] = 0
    
    # 연결점 해싱
    dic = defaultdict(list)
    for x, y, fare in fares:
        dic[x].append([y, fare])
        dic[y].append([x, fare])
    
    # 다익스트라 활용하여 a -> b 의 모든 최단 거리 계산
    for i in range(1, n + 1):
        # 우선순위 큐 활용
        queue = []
        heapq.heappush(queue, [i, 0])
        
        while queue:
            now, cost = heapq.heappop(queue)
            
            # 이미 빠른 도착 방법이 존재하는 경우 
            if cost > dist[i][now]:
                continue
            
            for j, fare in dic[now]:
                # 더 짧은 길일 경우 
                if cost + fare < dist[i][j]:
                    dist[i][j] = cost + fare
                    heapq.heappush(queue, [j, dist[i][j]])
                    
                    
    # 출발지점 -> 헤어지는 지점 -> 각자 집
    #        비용      +     비용      => 최솟값 계산 
    answer = 1000000000
    for i in range(1, n + 1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
        
    return answer
