from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

# 각 먹이 위치 및 상어 위치 체킹
for i in range(n):
    for j in range(n):
        if table[i][j] == 9:
            shark = (i, j)
            table[i][j] = 0

# 먹이 섭취 진행
time, size, eat = 0, 2, 0
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
while True:
    queue = deque([(shark, 0)])
    check = set([shark])
    food = []
    target = 41
    
    # 한마리 먹을 때마다 체크
    while queue:
        (x, y), dist = queue.popleft()
        
        # 대상자 선정이 끝난 경우
        if food and target < dist:
            break
        
        # 조건에 맞을 경우 대상자에 포함
        if 0 < table[x][y] < size:
            food.append((x, y))
            target = dist
            continue
        
        # bfs
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            
            # set을 이용하여 연산 간소화
            if 0 <= ax < n and 0 <= ay < n and table[ax][ay] <= size and (ax, ay) not in check:
                check.add((ax, ay))
                queue.append([(ax, ay), dist + 1])
    
    # 대상자가 있는 경우
    if food:
        # 정렬하여 우선순위 적용
        food.sort()
        shark = (food[0][0], food[0][1])
        table[food[0][0]][food[0][1]] = 0
        eat += 1
        time += target
        if eat == size:
            size += 1
            eat = 0
    # 대상자가 없는 경우 바로 호출
    else:
        break

# 결과 출력
print(time)
