from collections import deque

def solution(board):
    answer = 999999999
    
    bMin = 0
    bMax = len(board) - 1
    
    remove = [[999999999 for _ in range(bMax + 1)] for _ in range(bMax + 1)]
    remove[0][0] = 0
    
    check = deque()
    check.append([[0, 0], 0, 0, [[0, 0]]]) 
    # [좌표, 방향, 금액, 경로]
    # 방향  1:동,  2:서, 3:남, 4:북
    # 직전방향과 다를 경우 코너 가격을 추가하기 위해서
    
    while len(check) > 0:
        [x, y], to, money, route = check.popleft()
        
        if x == bMax and y == bMax:                                                 # 도착
            answer = min(answer, money)
        else:
            if x + 1 <= bMax and board[y][x + 1] == 0 and not [x + 1, y] in route:  # 동
                temp = route[:]
                temp.append([x + 1, y])
                if to in [0, 1]:
                    if remove[y][x + 1] >= money + 100:
                        check.append([[x + 1, y], 1, money + 100, temp])
                        remove[y][x + 1] = money + 100
                else:
                    if remove[y][x + 1] >= money + 600:
                        check.append([[x + 1, y], 1, money + 600, temp])
                        remove[y][x + 1] = money + 600
            if x - 1 >= bMin and board[y][x - 1] == 0 and not [x - 1, y] in route:  #서
                temp = route[:]
                temp.append([x - 1, y])
                if to == 2:
                    if remove[y][x - 1] >= money + 100:
                        check.append([[x - 1, y], 2, money + 100, temp])
                        remove[y][x - 1] = money + 100
                else:
                    if remove[y][x - 1] >= money + 600:
                        check.append([[x - 1, y], 2, money + 600, temp])
                        remove[y][x - 1] = money + 600
            if y + 1 <= bMax and board[y + 1][x] == 0 and not [x, y + 1] in route:  #남
                temp = route[:]
                temp.append([x, y + 1])
                if to in [0, 3]:
                    if remove[y + 1][x] >= money + 100:
                        check.append([[x, y + 1], 3, money + 100, temp])
                        remove[y + 1][x] = money + 100
                else:
                    if remove[y + 1][x] >= money + 600:
                        check.append([[x, y + 1], 3, money + 600, temp])
                        remove[y + 1][x] = money + 600
            if y - 1 >= bMin and board[y - 1][x] == 0 and not [x, y - 1] in route:  #북
                temp = route[:]
                temp.append([x, y - 1])
                if to == 4:
                    if remove[y - 1][x] >= money + 100:
                        check.append([[x, y - 1], 4, money + 100, temp])
                        remove[y - 1][x] = money + 100
                else:
                    if remove[y - 1][x] >= money + 600:
                        check.append([[x, y - 1], 4, money + 600, temp])
                        remove[y - 1][x] = money + 600
    
    return answer
