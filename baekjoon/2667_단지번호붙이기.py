from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
zido = [input().rstrip() for _ in range(n)]

# bfs 기본
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# 모든 점에서 출발
# 그러나 중복점 체크는 확실히
answer = []
check = set()
for i in range(n):
    for j in range(n):
        # 중복되지 않았다면 bfs 체크
        if zido[i][j] == "1" and (i, j) not in check:
            check.add((i, j))
            count = 1
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                
                for k in range(4):
                    ax = x + dx[k]
                    ay = y + dy[k]
                    
                    if 0 <= ax < n and 0 <= ay < n and zido[ax][ay] == "1" and (ax, ay) not in check:
                        count += 1
                        check.add((ax, ay))
                        queue.append((ax, ay))
            
            # 다 체크 된 뒤 count 저장
            answer.append(count)

# 결과 출력
print(len(answer))
answer.sort()
for i in answer:
    print(i)
