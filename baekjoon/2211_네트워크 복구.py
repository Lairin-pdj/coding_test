from collections import defaultdict, deque
import sys
input = sys.stdin.readline
    
# 파싱
n, m = map(int, input().split())
dic = defaultdict(lambda : defaultdict(int))
for _ in range(m):
    a, b, d = map(int, input().split())
    dic[a][b] = d
    dic[b][a] = d

# 거리 저장 배열
dist = [1000000000] * (n + 1)
visited = [False] * (n + 1)

# 갱신내역 저장 배열
update = [-1] * (n + 1)

# 다익스트라
dist[1] = 0

for _ in range(n):
    # 가장 짧은 값 체크
    path = -1
    low = 1000000000
    for i in range(1, n + 1):
        if not visited[i] and dist[i] < low:
            path = i
            low = dist[i]
    
    visited[path] = True
    for i in dic[path]:
        cost = dist[path] + dic[path][i]
        if cost < dist[i]:
            update[i] = path
            dist[i] = cost

# 결과 계산
answer = []
for i in range(1, n + 1):
    if update[i] != -1:
        answer.append((i, update[i]))

# 결과 출력
print(len(answer))
for i in answer:
    print(*i)
