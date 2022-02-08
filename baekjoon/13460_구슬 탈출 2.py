from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

# 각 위치 파악
red = []
blue = []
goal = []
for i in range(n):
    for j in range(m):
        if board[i][j] == "B":
            blue = (i, j)
        elif board[i][j] == "R":
            red = (i, j)
        elif board[i][j] == "O":
            goal = (i, j)

# bfs
# (red x, y, blue x, y, count, before)
flag = False
answer = 0
queue = deque([(red[0], red[1], blue[0], blue[1], 0, 0)])
while queue:
    rx, ry, bx, by, count, before = queue.popleft()
    
    # 지정 횟수 초과 시 제외
    if count >= 10:
        continue
    
    # 왼쪽
    if before != 1:
        arx, ary, abx, aby = rx, ry, bx, by
        # 같은 라인에 있는 경우
        if arx == abx:
            rcheck = False
            bcheck = False
            
            # 빨간공 먼저 이동
            if ary < aby:
                # 이동
                while board[arx][ary] != "#":
                    if (arx, ary) == goal:
                        rcheck = True
                        ary = -1
                        break
                    ary -= 1
                while board[abx][aby] != "#" and aby != ary + 1:
                    if (abx, aby) == goal:
                        bcheck = True
                        break
                    aby -= 1
                
                # 성공여부 체크 및 추후 전개
                if not bcheck:
                    if rcheck:
                        flag = True
                        answer = count + 1
                        break
                    else:
                        queue.append((arx, ary + 1, abx, aby + 1, count + 1, 1))
                    
            # 파란공 먼저 이동
            else:
                # 이동
                while board[abx][aby] != "#":
                    if (abx, aby) == goal:
                        bcheck = True
                        break
                    aby -= 1
                while board[arx][ary] != "#" and ary != aby + 1:
                    if (arx, ary) == goal:
                        rcheck = True
                        break
                    ary -= 1
                
                # 성공여부 체크 및 추후 전개
                if not bcheck:
                    if rcheck:
                        flag = True
                        answer = count + 1
                        break
                    else:
                        queue.append((arx, ary + 1, abx, aby + 1, count + 1, 1))
        
        else:
            rcheck = False
            bcheck = False
            
            # 이동
            while board[arx][ary] != "#":
                if (arx, ary) == goal:
                    rcheck = True
                    break
                ary -= 1
            while board[abx][aby] != "#":
                if (abx, aby) == goal:
                    bcheck = True
                    break
                aby -= 1
            
            # 성공여부 체크 및 추후 전개
            if not bcheck:
                if rcheck:
                    flag = True
                    answer = count + 1
                    break
                else:
                    queue.append((arx, ary + 1, abx, aby + 1, count + 1, 1))
    
    # 오른쪽
    if before != 1:
        arx, ary, abx, aby = rx, ry, bx, by
        # 같은 라인에 있는 경우
        if arx == abx:
            rcheck = False
            bcheck = False
            
            # 빨간공 먼저 이동
            if ary > aby:
                # 이동
                while board[arx][ary] != "#":
                    if (arx, ary) == goal:
                        rcheck = True
                        ary = -1
                        break
                    ary += 1
                while board[abx][aby] != "#" and aby != ary - 1:
                    if (abx, aby) == goal:
                        bcheck = True
                        break
                    aby += 1
                
                # 성공여부 체크 및 추후 전개
                if not bcheck:
                    if rcheck:
                        flag = True
                        answer = count + 1
                        break
                    else:
                        queue.append((arx, ary - 1, abx, aby - 1, count + 1, 1))
                    
            # 파란공 먼저 이동
            else:
                # 이동
                while board[abx][aby] != "#":
                    if (abx, aby) == goal:
                        bcheck = True
                        break
                    aby += 1
                while board[arx][ary] != "#" and ary != aby - 1:
                    if (arx, ary) == goal:
                        rcheck = True
                        break
                    ary += 1
                
                # 성공여부 체크 및 추후 전개
                if not bcheck:
                    if rcheck:
                        flag = True
                        answer = count + 1
                        break
                    else:
                        queue.append((arx, ary - 1, abx, aby - 1, count + 1, 1))
        
        else:
            rcheck = False
            bcheck = False
            
            # 이동
            while board[arx][ary] != "#":
                if (arx, ary) == goal:
                    rcheck = True
                    break
                ary += 1
            while board[abx][aby] != "#":
                if (abx, aby) == goal:
                    bcheck = True
                    break
                aby += 1
            
            # 성공여부 체크 및 추후 전개
            if not bcheck:
                if rcheck:
                    flag = True
                    answer = count + 1
                    break
                else:
                    queue.append((arx, ary - 1, abx, aby - 1, count + 1, 1))
    
    # 위쪽
    if before != 2:
        arx, ary, abx, aby = rx, ry, bx, by
        # 같은 라인에 있는 경우
        if ary == aby:
            rcheck = False
            bcheck = False
            
            # 빨간공 먼저 이동
            if arx < abx:
                # 이동
                while board[arx][ary] != "#":
                    if (arx, ary) == goal:
                        rcheck = True
                        arx = -1
                        break
                    arx -= 1
                while board[abx][aby] != "#" and abx != arx + 1:
                    if (abx, aby) == goal:
                        bcheck = True
                        break
                    abx -= 1
                
                # 성공여부 체크 및 추후 전개
                if not bcheck:
                    if rcheck:
                        flag = True
                        answer = count + 1
                        break
                    else:
                        queue.append((arx + 1, ary, abx + 1, aby, count + 1, 2))
                    
            # 파란공 먼저 이동
            else:
                # 이동
                while board[abx][aby] != "#":
                    if (abx, aby) == goal:
                        bcheck = True
                        break
                    abx -= 1
                while board[arx][ary] != "#" and arx != abx + 1:
                    if (arx, ary) == goal:
                        rcheck = True
                        break
                    arx -= 1
                
                # 성공여부 체크 및 추후 전개
                if not bcheck:
                    if rcheck:
                        flag = True
                        answer = count + 1
                        break
                    else:
                        queue.append((arx + 1, ary, abx + 1, aby, count + 1, 2))
        
        else:
            rcheck = False
            bcheck = False
            
            # 이동
            while board[arx][ary] != "#":
                if (arx, ary) == goal:
                    rcheck = True
                    break
                arx -= 1
            while board[abx][aby] != "#":
                if (abx, aby) == goal:
                    bcheck = True
                    break
                abx -= 1
            
            # 성공여부 체크 및 추후 전개
            if not bcheck:
                if rcheck:
                    flag = True
                    answer = count + 1
                    break
                else:
                    queue.append((arx + 1, ary, abx + 1, aby, count + 1, 2))
    
    # 아래쪽
    if before != 2:
        arx, ary, abx, aby = rx, ry, bx, by
        # 같은 라인에 있는 경우
        if ary == aby:
            rcheck = False
            bcheck = False
            
            # 빨간공 먼저 이동
            if arx > abx:
                # 이동
                while board[arx][ary] != "#":
                    if (arx, ary) == goal:
                        rcheck = True
                        arx = -1
                        break
                    arx += 1
                while board[abx][aby] != "#" and abx != arx - 1:
                    if (abx, aby) == goal:
                        bcheck = True
                        break
                    abx += 1
                
                # 성공여부 체크 및 추후 전개
                if not bcheck:
                    if rcheck:
                        flag = True
                        answer = count + 1
                        break
                    else:
                        queue.append((arx - 1, ary, abx - 1, aby, count + 1, 2))
                    
            # 파란공 먼저 이동
            else:
                # 이동
                while board[abx][aby] != "#":
                    if (abx, aby) == goal:
                        bcheck = True
                        break
                    abx += 1
                while board[arx][ary] != "#" and arx != abx - 1:
                    if (arx, ary) == goal:
                        rcheck = True
                        break
                    arx += 1
                
                # 성공여부 체크 및 추후 전개
                if not bcheck:
                    if rcheck:
                        flag = True
                        answer = count + 1
                        break
                    else:
                        queue.append((arx - 1, ary, abx - 1, aby, count + 1, 2))
        
        else:
            rcheck = False
            bcheck = False
            
            # 이동
            while board[arx][ary] != "#":
                if (arx, ary) == goal:
                    rcheck = True
                    break
                arx += 1
            while board[abx][aby] != "#":
                if (abx, aby) == goal:
                    bcheck = True
                    break
                abx += 1
            
            # 성공여부 체크 및 추후 전개
            if not bcheck:
                if rcheck:
                    flag = True
                    answer = count + 1
                    break
                else:
                    queue.append((arx - 1, ary, abx - 1, aby, count + 1, 2))

# 결과출력
if flag:
    print(answer)
else:
    print(-1)
