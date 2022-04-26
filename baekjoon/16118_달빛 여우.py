from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)

# 파싱
n, m = map(int, input().split())
dic = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    dic[a].append((b, d * 2))
    dic[b].append((a, d * 2))

# 달빛 여우
def fox():
    foxdist = [INF for _ in range(n + 1)]
    foxdist[1] = 0
    
    queue = [(0, 1)]
    while queue:
        # 방문 안한 최소 찾기
        total, target = heappop(queue)
        
        # 탈출 조건
        if foxdist[target] < total:
            continue
        
        # 최소값 갱신
        for i, d in dic[target]:
            cost = foxdist[target] + d
            if cost < foxdist[i]:
                foxdist[i] = cost
                heappush(queue, (foxdist[i], i))
    
    return foxdist

# 달빛 늑대
def wolf():
    wolfdist = [[INF] * (n + 1) for _ in range(2)]
    wolfdist[0][1] = 0
    
    queue = [(0, 1, 0)]
    while queue:
        # 방문 안한 최소 찾기
        total, target, status = heappop(queue)
        
        # 탈출 조건
        if wolfdist[status][target] < total:
            continue
        
        # 최소값 갱신
        for i, d in dic[target]:
            if status:
                cost = wolfdist[status][target] + (d * 2)
                if cost < wolfdist[0][i]:
                    wolfdist[0][i] = cost
                    heappush(queue, (wolfdist[0][i], i, 0))
            else:
                cost = wolfdist[status][target] + (d // 2)
                if cost < wolfdist[1][i]:
                    wolfdist[1][i] = cost
                    heappush(queue, (wolfdist[1][i], i, 1))
    
    return wolfdist

fox = fox()
wolf = wolf()

# 결과 출력
answer = 0
for i in range(1, n + 1):
    if fox[i] < min(wolf[0][i], wolf[1][i]):
        answer += 1
print(answer)
