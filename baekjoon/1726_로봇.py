from collections import deque
import sys
input = sys.stdin.readline
    
# 파싱
m, n = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(m)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())

# 초기값 처리
sx -= 1
sy -= 1
ex -= 1
ey -= 1

# bfs
direct = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
queue = deque([(sx, sy, sd, 0)])
check = set([(sx, sy, sd)])
while queue:
    x, y, d, count = queue.popleft()
    
    # 탈출
    if (x, y, d) == (ex, ey, ed):
        print(count)
        break
    
    # 회전 명령
    if d == 1 or d == 2:
        if (x, y, 3) not in check:
            queue.append((x, y, 3, count + 1))
            check.add((x, y, 3))
        if (x, y, 4) not in check:
            queue.append((x, y, 4, count + 1))
            check.add((x, y, 4))
    else:
        if (x, y, 1) not in check:
            queue.append((x, y, 1, count + 1))
            check.add((x, y, 1))
        if (x, y, 2) not in check:
            queue.append((x, y, 2, count + 1))
            check.add((x, y, 1))
    
    # 이동 명령
    move = direct[d]
    for i in range(1, 4):
        ax = x + move[0] * i
        ay = y + move[1] * i
        
        # 도달 가능한 경우
        if 0 <= ax < m and 0 <= ay < n and table[ax][ay] == 0:
            if (ax, ay, d) not in check:
                queue.append((ax, ay, d, count + 1))
                check.add((ax, ay, d))
        # 도달 불가능한 경우
        else:
            break
