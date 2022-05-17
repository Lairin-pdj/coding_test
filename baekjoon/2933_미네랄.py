from collections import deque
import sys
input = sys.stdin.readline

# 파싱
r, c = map(int, input().split())
table = [list(input().rstrip()) for _ in range(r)]
n = int(input())
stick = list(map(int, input().split()))

# 막대기 던지기
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
direct = 1
for i in stick:
    # 좌측
    target = [-1, -1]
    if direct == 1:
        for j in range(c):
            if table[r - i][j] == "x":
                table[r - i][j] = "."
                target = [r - i, j]
                break
    # 우측
    else:
        for j in range(c - 1, -1, -1):
            if table[r - i][j] == "x":
                table[r - i][j] = "."
                target = [r - i, j]
                break
    
    direct = -direct
    
    # 조각 분리 체크
    if target != [-1, -1]:
        
        # 블럭 저장 및 최저 위치 체크
        line = [[set(), set(), set(), set()] for _ in range(c)]
        low = [[-1] * 4 for _ in range(c)]
        count = [-1, -1, -1, -1]
        
        # 제거된 미네랄의 주변 체크
        check = set()
        for j in range(4):
            ax = target[0] + dx[j]
            ay = target[1] + dy[j]
            
            # 체크된 적 없다면 진행
            if 0 <= ax < r and 0 <= ay < c and table[ax][ay] == "x" and (ax, ay) not in check:
                count[j] = 1
                queue = deque([(ax, ay)])
                check.add((ax, ay))
                line[ay][j].add(ax)
                low[ay][j] = ax
                
                # bfs로 클러스터 체크
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        tx = x + dx[k]
                        ty = y + dy[k]
                        
                        if 0 <= tx < r and 0 <= ty < c and table[tx][ty] == "x" and tx not in line[ty][j]:
                            queue.append((tx, ty))
                            check.add((tx, ty))
                            line[ty][j].add(tx)
                            low[ty][j] = max(low[ty][j], tx)
        
        # 체크된 블럭 가능한 만큼 수직이동
        for j in range(4):
            if count[j] == 1:
                # 이동 가능한 depth 체크
                depth = 1000
                for k in range(c):
                    if low[k][j] != -1:
                        temp = 0
                        for l in range(low[k][j] + 1, r):
                            if table[l][k] != "x":
                                temp += 1
                            else:
                                break
                        depth = min(depth, temp)
                
                # 이동 가능하면 이동 후 탈출
                if depth >= 1:
                    # 기존 값 제거
                    for k in range(c):
                        for l in line[k][j]:
                            table[l][k] = "."
                    
                    # 이동 된 값 삽입
                    for k in range(c):
                        for l in line[k][j]:
                            table[l + depth][k] = "x"
                    
                    # 탈출
                    break

# 결과 출력
for i in table:
    print("".join(i))
