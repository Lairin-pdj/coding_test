from collections import defaultdict, deque
from copy import deepcopy

def movement(board, x1, y1, x2, y2):
    count = 0
    if x1 != x2:
        # x와 y가 모두 다를 경우
        if y1 != y2:
            # bfs를 이용하여 목표 지점까지 최소값 체크
            queue = deque()
            # [[현재 좌표], 횟수]
            queue.append([[x1, y1], 0])
            
            # 집합을 이용하여 중복체크 방지
            check = set()
            check.add(tuple([x1, y1]))
            
            while len(queue) > 0:
                [x, y], num = queue.popleft()
                
                # 도착시 최소값 확정으로 바로 반환
                if x == x2 and y == y2:
                    return num
                
                # 서쪽 방향으로 1회 만에 이동 가능한 지점 큐에 삽입
                i = 1
                while x - i >= 0:
                    if x - i >= 0 and tuple([x - i, y]) not in check and movement(board, x, y, x - i, y) == 1:
                        check.add(tuple([x - i, y]))
                        queue.append([[x - i, y], num + 1])
                    i += 1
                    
                # 동쪽 방향으로 1회 만에 이동 가능한 지점 큐에 삽입
                i = 1
                while x + i <= 3:
                    if x + i <= 3 and tuple([x + i, y]) not in check and movement(board, x, y, x + i, y) == 1:
                        check.add(tuple([x + i, y]))
                        queue.append([[x + i, y], num + 1])
                    i += 1
                    
                # 북쪽 방향으로 1회 만에 이동 가능한 지점 큐에 삽입
                i = 1
                while y - i >= 0:
                    if y - i >= 0 and tuple([x, y - i]) not in check and movement(board, x, y, x, y - i) == 1:
                        check.add(tuple([x, y - i]))
                        queue.append([[x, y - i], num + 1])
                    i += 1
                    
                # 남쪽 방향으로 1회 만에 이동 가능한 지점 큐에 삽입
                i = 1
                while y + i <= 3:
                    if y + i <= 3 and tuple([x, y + i]) not in check and movement(board, x, y, x, y + i) == 1:
                        check.add(tuple([x, y + i]))
                        queue.append([[x, y + i], num + 1])
                    i += 1
        # x 값만 다른 경우
        else:
            # 기울기 측정
            xdirect = int((x1 - x2) / abs(x1 - x2))
            # 도착 지점이 카드가 없어 ctrl 이동으로 멈출 수 없는 경우
            if board[x2][y2] == 0 and 3 >= x2 - xdirect >= 0 and x2 != x1 - xdirect:
                count += 1
            # 출발 지점과 도착 지점 사이의 카드 존재 유무 체크
            for i in range(x1 - xdirect, x2, -xdirect):
                if board[i][y1] != 0:
                    count += 1
            # 기본 이동 횟수
            count += 1   
    else:
        # y 값만 다른 경우
        if y1 != y2:
            # 기울기 측정
            ydirect = int((y1 - y2) / abs(y1 - y2))
            # 도착 지점이 카드가 없어 ctrl 이동으로 멈출 수 없는 경우
            if board[x2][y2] == 0 and 3 >= y2 - ydirect >= 0 and y2 != y1 - ydirect:
                count += 1
            # 출발 지점과 도착 지점 사이의 카드 존재 유무 체크
            for i in range(y1 - ydirect, y2, -ydirect):
                if board[x1][i] != 0:
                    count += 1
            # 기본 이동 횟수
            count += 1
    
    # 최소 이동 횟수 반환
    return count

def solution(board, r, c):
    # 사전을 이용해 카드들의 위치 파악
    card = 0
    dic = defaultdict(list)
    for x, a in enumerate(board):
        for y, b in enumerate(a):
            if b != 0:
                card += 1
                dic[b].append([x, y])
    
    move = 1000000
    check = deque()
    # [현재 보드 상태, [현재 좌표], [경로], 이동 횟수]
    copyboard = deepcopy(board)
    check.append([copyboard, [r, c], [], 0])
    
    # bfs로 진행
    while len(check) > 0:
        copyboard, [x, y], route, count = check.popleft()
        # 카드를 전부 뒤집은 경우 최소 비교 후 건너뛰기
        if len(route) == card:
            move = min(move, count)
            continue
        
        # 남은 카드 쌍을 이동하는 방식을 전부 계산
        for i in dic.keys():
            [x1, y1], [x2, y2] = dic[i]
            if [x1, y1] not in route:
                # 왼쪽 좌표 우선 이동
                left = 0
                left += movement(copyboard, x, y, x1, y1)
                left += movement(copyboard, x1, y1, x2, y2)
                
                # 오른쪽 좌표 우선 이동
                right = 0
                right += movement(copyboard, x, y, x2, y2)
                right += movement(copyboard, x2, y2, x1, y1)

                # 카드를 선택하여 지움
                tempboard = deepcopy(copyboard)
                tempboard[x1][y1] = 0
                tempboard[x2][y2] = 0
                
                # 다음 경우의 수를 의미하는 큐 삽입
                check.append([tempboard, [x1, y1], route + dic[i], count + right])
                check.append([tempboard, [x2, y2], route + dic[i], count + left])
    
    # 커서 이동 횟수 + 카드 뒤집은 횟수 반환
    return move + card
