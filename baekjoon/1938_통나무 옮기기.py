from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
table = [input().rstrip() for _ in range(n)]

# 위치 파악
b = []
e = []
for i in range(n):
    for j in range(n):
        if table[i][j] == "B":
            b.append((i, j))
        elif table[i][j] == "E":
            e.append((i, j))

# -1 : 0B0 1 : 000 2 : B00 -2 : 00B
#      0B0     BBB     0B0      0B0
#      0B0     000     00B      B00

# b의 형태 파악
# 1의 경우
if b[0][0] == b[1][0]:
    start = (b[1], 1)
# -1의 경우
elif b[0][1] == b[1][1]:
    start = (b[1], -1)
# -2의 경우
elif b[0][1] - b[1][1] == 1:
    start = (b[1], -2)
# 2의 경우
else:
    start = (b[1], 2)

# e의 형태 파악
# 1의 경우
if e[0][0] == e[1][0]:
    end = (e[1], 1)
# -1의 경우
elif e[0][1] == e[1][1]:
    end = (e[1], -1)
# -2의 경우
elif e[0][1] - e[1][1] == 1:
    end = (e[1], -2)
# 2의 경우
else:
    end = (e[1], 2)

# 겹치지 못하는 경우 처리
if abs(start[1]) != abs(end[1]):
    print(0)
    
# 가능한 경우
else:

    # bfs
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    answer = 0
    queue = deque([(start, 0)])
    check = set([start])
    
    while queue:
        ((x, y), shape), count = queue.popleft()
        
        # 도착
        if ((x, y), shape) == end:
            answer = count
            break
        
        # 5가지 행동처리
        # 4가지 이동처리
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            
            if 0 <= ax < n and 0 <= ay < n and table[ax][ay] != "1":
                # 끝 처리
                if (ax == 0 or ax == n - 1) and shape != 1:
                    continue
                if (ay == 0 or ay == n - 1) and shape != -1:
                    continue
                
                # 충돌처리
                flag = True
                if shape == 1 and (table[ax][ay - 1] == "1" or table[ax][ay + 1] == "1"):
                    flag = False
                elif shape == -1 and (table[ax - 1][ay] == "1" or table[ax + 1][ay] == "1"):
                    flag = False
                elif shape == 2 and (table[ax - 1][ay - 1] == "1" or table[ax + 1][ay + 1] == "1"):
                    flag = False
                elif shape == -2 and (table[ax - 1][ay + 1] == "1" or table[ax + 1][ay - 1] == "1"):
                    flag = False
                
                if flag and ((ax, ay), shape) not in check:
                    check.add(((ax, ay), shape))
                    queue.append((((ax, ay), shape), count + 1))
        
        # 1가지 회전처리
        if 0 < x < n - 1 and 0 < y < n - 1:
            # 충돌처리
            flag = True
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if table[i][j] == "1":
                        flag = False
            
            if flag and ((x, y), -shape) not in check:
                check.add(((x, y), -shape))
                queue.append((((x, y), -shape), count + 1))
    
    # 결과 출력
    print(answer)
