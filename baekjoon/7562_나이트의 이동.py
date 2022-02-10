from collections import deque
import sys
input = sys.stdin.readline

# 파싱
t = int(input())
dx, dy = [2, 2, 1, 1, -1, -1, -2, -2], [1, -1, 2, -2, 2, -2, 1, -1]
for _ in range(t):
    length = int(input())
    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))
    
    # 계산량 절감을 위한 중복 체크
    check = set([start])
    
    # bfs
    queue = deque([[start, 0]])
    while queue:
        (x, y), count = queue.popleft()
        
        # 탈출조건
        if (x, y) == goal:
            print(count)
            break
        
        # 8방향 이동
        for i in range(8):
            ax = x + dx[i]
            ay = y + dy[i]
            
            if 0 <= ax < length and 0 <= ay < length and (ax, ay) not in check:
                check.add((ax, ay))
                queue.append([(ax, ay), count + 1])
