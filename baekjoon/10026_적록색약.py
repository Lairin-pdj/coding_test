from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
table = [[*input().rstrip()] for _ in range(n)]

# bfs
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# 적록 색약이 아닌 경우
check = set()
countRGB = 0
for i in range(n):
    for j in range(n):
        if (i, j) not in check:
            queue = deque([(i, j)])
            check.add((i, j))
            color = table[i][j]
            while queue:
                x, y = queue.popleft()
                
                for k in range(4):
                    ax = x + dx[k]
                    ay = y + dy[k]
                    
                    if 0 <= ax < n and 0 <= ay < n and (ax, ay) not in check and table[ax][ay] == color:
                        queue.append((ax, ay))
                        check.add((ax, ay))
            
            # 영역 하나 체크
            countRGB += 1

# 적록색맹 변환
for i in range(n):
    for j in range(n):
        if table[i][j] == "G":
            table[i][j] = "R"

# 적록 색약인 경우
check = set()
countTB = 0
for i in range(n):
    for j in range(n):
        if (i, j) not in check:
            queue = deque([(i, j)])
            check.add((i, j))
            color = table[i][j]
            while queue:
                x, y = queue.popleft()
                
                for k in range(4):
                    ax = x + dx[k]
                    ay = y + dy[k]
                    
                    if 0 <= ax < n and 0 <= ay < n and (ax, ay) not in check and table[ax][ay] == color:
                        queue.append((ax, ay))
                        check.add((ax, ay))
            
            # 영역 하나 체크
            countTB += 1

# 결과 출력
print(countRGB, countTB)
