from collections import deque
import sys
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    # bfs
    queue = deque([(a, "")])
    check = set([a])
    while queue:
        now, route = queue.popleft()
        
        # 탈출
        if now == b:
            print(route)
            break
        
        # D
        temp = (now * 2) % 10000
        if temp not in check:
            queue.append((temp, route + "D"))
            check.add(temp)
        # S
        temp = (now - 1) % 10000
        if temp not in check:
            queue.append((temp, route + "S"))
            check.add(temp)
        # L
        temp = ((now * 10) + (now // 1000)) % 10000
        if temp not in check:
            queue.append((temp, route + "L"))
            check.add(temp)
        # R
        temp = (now // 10) + ((now % 10) * 1000)
        if temp not in check:
            queue.append((temp, route + "R"))
            check.add(temp)
