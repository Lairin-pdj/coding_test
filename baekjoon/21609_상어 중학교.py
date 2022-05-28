from collections import deque
import sys
input = sys.stdin.readline

# 블록 탐색
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def bfs(nx, ny, color):
    queue = deque([(nx, ny)])
    
    block = [(nx, ny)]
    rainbow = []
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            
            if 0 <= ax < n and 0 <= ay < n and not visited[ax][ay]:
                # 일반 
                if table[ax][ay] == color:
                    visited[ax][ay] = 1
                    queue.append((ax, ay))
                    block.append((ax, ay))
                
                # 무지개
                elif table[ax][ay] == 0:
                    visited[ax][ay] = 1
                    queue.append((ax, ay))
                    rainbow.append((ax, ay))
    
    # 무지개 해제
    for x, y in rainbow:
        visited[x][y] = 0
    
    return [sorted(block) + rainbow, len(rainbow)]

# 반시계 회전
def rotate(t):
    return list(map(list, zip(*t)))[::-1]

# 중력 적용
def gravity(t):
    
    for i in range(n - 2, -1, -1): 
        for j in range(n):
            
            if t[i][j] > -1:
                temp = i
                while True:
                    if 0 <= temp + 1 < n and t[temp + 1][j] == -2:
                        t[temp + 1][j] = t[temp][j]
                        t[temp][j] = -2
                        temp += 1
                    else:
                        break

# 파싱
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

# 플레이
score = 0

while True:
    
    # 블록 찾기
    blocks = [[], 0]
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                temp = bfs(i, j, table[i][j])
                
                # 2개 이상
                if len(temp[0]) >= 2:
                    # 갯수 초과시
                    if len(temp[0]) > len(blocks[0]):
                        blocks = temp
                    # 같을 시
                    elif len(temp[0]) == len(blocks[0]):
                        
                        # 무지개 갯수
                        if temp[1] > blocks[1]:
                            blocks = temp
                        elif temp[1] == blocks[1]:
                            
                            # 기준 블록 위치
                            if temp[0][0][0] > blocks[0][0][0]:
                                blocks = temp
                            elif temp[0][0][0] == blocks[0][0][0]:
                                if temp[0][0][1] > blocks[0][0][1]:
                                    blocks = temp

    # 탈출
    if not blocks[0]:
        break
    
    # 블록 지우기
    for x, y in blocks[0]:
        table[x][y] = -2
    
    # 점수 계산
    score += len(blocks[0]) ** 2
    
    # 중력 적용
    gravity(table)
    
    # 회전 적용
    table = rotate(table)

    # 중력 적용
    gravity(table)

# 결과 출력
print(score)
