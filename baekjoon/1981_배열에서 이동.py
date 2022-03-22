from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

# 최대 최소 체크
low = 200
for i in range(n):
    for j in range(n):
        low = min(low, table[i][j])
high = low
    
# 범위 줄이기
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
answer = 200
while low <= table[0][0] and high <= 200:
    
    # 초기값 체크
    flag = False
    if low <= table[0][0] <= high:
        # bfs
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        while queue:
            x, y = queue.popleft()
            
            # 도착 가능 체크
            if (x, y) == (n - 1, n - 1):
                flag = True
                break
            
            for i in range(4):
                ax = x + dx[i]
                ay = y + dy[i]
                
                if 0 <= ax < n and 0 <= ay < n and (ax, ay) not in visited:
                    if low <= table[ax][ay] <= high:
                        queue.append((ax, ay))
                        visited.add((ax, ay))
    
    # 도달 여부에 따라 low, high 조절
    if flag:
        answer = min(answer, high - low)
        low += 1
    else:
        high += 1

# 결과 출력
print(answer)
