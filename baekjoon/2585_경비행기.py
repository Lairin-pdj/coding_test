from collections import defaultdict, deque
from math import dist, ceil
import sys
input = sys.stdin.readline
    
# 파싱
n, k = map(int, input().split())
point = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)] + [(10000, 10000)]

# 비행장간 거리 체킹
dic = defaultdict(list)
for i in range(n + 2):
    for j in range(n + 2):
        if i != j:
            dic[i].append((ceil(dist(point[i], point[j]) / 10), j))

# 이분탐색
low = 0
high = ceil(dist((0, 0), (10000, 10000)) / 10)

while low <= high:
    mid = (low + high) // 2
    
    # 도달 가능 여부 bfs 판정
    check = False
    queue = deque([(0, 0)])
    visited = set([0])
    
    while queue:
        now, count = queue.popleft()
        
        # 도달 실패
        if count > k + 1:
            break
        
        # 도달 성공
        if now == n + 1:
            check = True
            break
        
        for d, to in dic[now]:
            if d <= mid:
                if to not in visited:
                    queue.append((to, count + 1))
                    visited.add(to)
    
    if check:
        high = mid - 1
    else:
        low = mid + 1

# 결과 출력
print(low)
