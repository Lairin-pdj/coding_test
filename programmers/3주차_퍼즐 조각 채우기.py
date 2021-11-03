from collections import deque, defaultdict

def rotate(n):
    # 주어진 2차원 배열을 회전시켜주는 함수
    # 열 단위로 따서 뒤집어서 넣어 90도 회전
    # 1 2 3    1 4 7    7 4 1
    # 4 5 6 -> 2 5 8 -> 8 5 2
    # 7 8 9    3 6 9    9 6 3
    return list(map(list, zip(*n[::-1])))

def checksum(t, k, x, y):                                                     
    # 주어진 두 배열의 합이 전부 1인지 확인하는 함수
    for i in range(x):
        for j in range(y):
            if t[i][j] + k[i][j] != 1:
                return False
    return True

def solution(game_board, table):
    length = len(game_board)
    
    # 빈 공간을 확인하여 작은 단위로 잘라 보관
    spaces = []
    space_boards = []
    # 공간의 중복체크를 막기 위해
    check = set()
    
    # 모든 칸을 시작점으로 고려
    for i in range(length):
        for j in range(length):
            # 비어있으면서 체크가 되지 않는 공간이라면 bfs로 공간 체크
            if game_board[i][j] == 0 and tuple([i, j]) not in check:
                queue = deque()
                # [좌표]
                queue.append([i, j])
                
                temp = []
                while queue:
                    x, y = queue.popleft()
                    
                    # 이미 체크한 좌표라면 제외
                    if [x, y] in temp:
                        continue
                    
                    # 공용 체크 구간에 삽입
                    check.add(tuple([x, y]))
                
                    # 개별 공간에 삽입
                    temp.append([x, y])
                    
                    # 동쪽으로 이동
                    if length > y + 1 and game_board[x][y + 1] == 0:
                        queue.append([x, y + 1])
                        
                    # 서쪽으로 이동
                    if 0 <= y - 1 and game_board[x][y - 1] == 0:
                        queue.append([x, y - 1])
                        
                    # 남쪽으로 이동
                    if length > x + 1 and game_board[x + 1][y] == 0:
                        queue.append([x + 1, y])
                        
                    # 북쪽으로 이동
                    if 0 <= x - 1 and game_board[x - 1][y] == 0:
                        queue.append([x - 1, y])
                
                # 시작점이 포함된 빈공간을 하나의 빈 공간으로 저장
                spaces.append(temp)

    # 좌표 값으로 된 공간을 배열로 치환
    for space in spaces:
        xmin, xmax = length, 0
        ymin, ymax = length, 0
        
        # 각 좌표의 최대, 최소를 계산
        for x, y in space:
            xmin = min(xmin, x)
            xmax = max(xmax, x)
            ymin = min(ymin, y)
            ymax = max(ymax, y)
        
        # 좌표 변환
        for i in range(len(space)):
            space[i][0] -= xmin
            space[i][1] -= ymin
        
        # 공간을 포함한 가장 작은 사각형으로 잘라내는 작업
        # 옮겨담을 배열 생성
        temp = [[1 for _ in range(ymax - ymin + 1)] for _ in range(xmax - xmin + 1)]
        
        # 좌표 적용
        for x, y in space:
            temp[x][y] = 0
        
        # 치환된 빈 공간 배열 저장
        space_boards.append(temp)
    
    
    # 블럭을 확인하여 작은 단위로 잘라 보관
    blocks = []
    block_boards = []
    # 블럭의 중복체크를 막기 위해
    check = set()
    
    # 모든 칸을 시작점으로 고려
    for i in range(length):
        for j in range(length):
            # 블럭이면서 체크가 되지 않는 부분이라면 bfs로 블럭 체크
            if table[i][j] == 1 and tuple([i, j]) not in check:
                queue = deque()
                # [좌표]
                queue.append([i, j])
                
                temp = []
                while queue:
                    x, y = queue.popleft()
                    
                    # 이미 체크한 좌표라면 제외
                    if [x, y] in temp:
                        continue
                    
                    # 공용 체크 구간에 삽입
                    check.add(tuple([x, y]))
                    
                    # 개별 블럭에 삽입
                    temp.append([x, y])
                    
                    # 동쪽으로 이동
                    if length > y + 1 and table[x][y + 1] == 1:
                        queue.append([x, y + 1])
                        
                    # 서쪽으로 이동
                    if 0 <= y - 1 and table[x][y - 1] == 1:
                        queue.append([x, y - 1])
                        
                    # 남쪽으로 이동
                    if length > x + 1 and table[x + 1][y] == 1:
                        queue.append([x + 1, y])
                        
                    # 북쪽으로 이동
                    if 0 <= x - 1 and table[x - 1][y] == 1:
                        queue.append([x - 1, y])
                
                # 시작점이 포함된 블럭을 하나의 블럭으로 저장
                blocks.append(temp)
    
    # 좌표 값으로 된 블럭을 배열로 치환
    for block in blocks:
        xmin, xmax = length, 0
        ymin, ymax = length, 0
        
        # 각 좌표의 최대, 최소를 계산
        for x, y in block:
            xmin = min(xmin, x)
            xmax = max(xmax, x)
            ymin = min(ymin, y)
            ymax = max(ymax, y)
        
        # 좌표 변환
        for i in range(len(block)):
            block[i][0] -= xmin
            block[i][1] -= ymin
        
        # 블럭을 포함한 가장 작은 사각형으로 잘라내는 작업
        # 옮겨담을 배열 생성
        temp = [[0 for _ in range(ymax - ymin + 1)] for _ in range(xmax - xmin + 1)]
        
        # 블록의 갯수를 저장
        count = 0
        for x, y in block:
            count += 1
            # 좌표 적용
            temp[x][y] = 1
        
        # 치환된 블럭 배열 저장
        block_boards.append([temp, count]) 
        
        
    # 사전을 이용해서 대입 가능한 보드와 블록사이 관계 형성
    dic = defaultdict(set)
    
    # 각 공간에 대해서 블록을 회전시켜가며 대입 체크
    for i, space in enumerate(space_boards):
        sx = len(space)
        sy = len(space[0])
        for j, (block, count) in enumerate(block_boards):
            bx = len(block)
            by = len(block[0])
            
            # 회전으로 들어가는 경우 체크
            # 최적화를 위해 회전이 필요없는 경우 구분
            k = 4
            if bx + by == 2:
                k = 1
            elif bx == 1 or by == 1:
                k = 2
                
            for _ in range(k):
                block = rotate(block)
                bx, by = by, bx
                
                # 배열의 크기가 일치하지 않을 경우 제외
                if bx != sx or by != sy:
                    continue
                
                # 모양이 정확한지 확인
                if checksum(space, block, sx, sy):
                    dic[i].add(tuple([j, count]))
    
    
    # 가능한 가짓수 대입하며 최댓값 체크
    answer = 0
    
    # 남은 블록을 가져갈 수 있는 만큼 체크
    remain = [i for i in range(len(block_boards))]
    for i in range(len(space_boards)):
        for (j, n) in dic[i]:
            if j in remain:
                answer += n
                remain.pop(remain.index(j))
                # 중복으로 넣는 경우를 막기 위해 
                break
    
    return answer
