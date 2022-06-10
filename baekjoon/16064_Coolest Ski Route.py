from collections import defaultdict, deque
import sys
input = sys.stdin.readline
    
# 파싱
n, m = map(int, input().split())
degree = [0] * n
dic = defaultdict(list)
for _ in range(m):
    s, t, c = map(int, input().split())
    s, t = s - 1, t - 1
    degree[t] += 1
    dic[s].append((t, c))

# 꼭대기 체크
check = deque()
for i in range(n):
    if degree[i] == 0:
        check.append(i)

# 위상 정렬
dist = [0] * n
while check:
    now = check.popleft()
    for to, con in dic[now]:
        degree[to] -= 1
        dist[to] = max(dist[to], dist[now] + con)
        
        if degree[to] == 0:
            check.append(to)

print(max(dist))
