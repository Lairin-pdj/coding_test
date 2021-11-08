from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n = int(input())

# bfs
check = [True for _ in range(n + 1)]
check[n] = False
queue = deque()
queue.append([n, [n]])
while queue:
    now, route = queue.popleft()
    
    if now == 1:
        print(len(route) - 1)
        print(*route)
        break
    
    if now % 3 == 0 and check[now // 3]:
        queue.append([now // 3, route + [now // 3]])
        check[now // 3] = False
    if now % 2 == 0 and check[now // 2]:
        queue.append([now // 2, route + [now // 2]])
        check[now // 2] = False
    if check[now - 1]:
        queue.append([now - 1, route + [now - 1]])
        check[now - 1] = False
