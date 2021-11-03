def solution(board):
    N = len(board)
    
    # [[[좌측 좌표], [우측 좌표]], 이동 횟수]
    queue = [[[[1, 1], [1, 2]], 0]]
    
    # 같은 위치에서 있었던 기록이 남아 있는 경우 최소조건이 깨지기 때문에 바로 제외
    check = [[[1, 1], [1, 2]]]
    
    # bfs 이용
    while len(queue) > 0:
        ((a, b), (c, d)), count = queue.pop(0)
        
        # bfs이기 때문에 최초발견이 최소값
        if a == N and b == N or c == N and d == N:
            return count
        
        # 동쪽으로 이동
        if b < N and board[a - 1][b] != 1 and d < N and board[c - 1][d] != 1:
            temp = [[a, b + 1], [c, d + 1]]
            temp.sort()
            if temp not in check:
                check.append(temp)
                queue.append([temp, count + 1])
        # 서쪽으로 이동
        if b - 2 >= 0 and board[a - 1][b - 2] != 1 and d - 2 >= 0 and board[c - 1][d - 2] != 1:
            temp = [[a, b - 1], [c, d - 1]]
            temp.sort()
            if temp not in check:
                check.append(temp)
                queue.append([temp, count + 1])
        # 남쪽으로 이동
        if a < N and board[a][b - 1] != 1 and c < N and board[c][d - 1] != 1:
            temp = [[a + 1, b], [c + 1, d]]
            temp.sort()
            if temp not in check:
                check.append(temp)
                queue.append([temp, count + 1])
        # 북쪽으로 이동
        if a - 2 >= 0 and board[a - 2][b - 1] != 1 and c - 2 >= 0 and board[c - 2][d - 1] != 1:
            temp = [[a - 1, b], [c - 1, d]]
            temp.sort()
            if temp not in check:
                check.append(temp)
                queue.append([temp, count + 1])
        # 좌기준 시계방향 회전
        # 가로
        if a == c:
            if a < N and board[a][b - 1] != 1 and board[c][d - 1] != 1:
                temp = [[a, b], [c + 1, d - 1]]
                temp.sort()
                if temp not in check:
                    check.append(temp)
                    queue.append([temp, count + 1])
        # 세로
        else:
            if b - 2 >= 0 and board[a - 1][b - 2] != 1 and board[c - 1][d - 2] != 1:
                temp = [[a, b], [c - 1, d - 1]]
                temp.sort()
                if temp not in check:
                    check.append(temp)
                    queue.append([temp, count + 1])
        # 좌기준 반시계방향 회전
        # 가로
        if a == c:
            if a - 2 >= 0 and board[a - 2][b - 1] != 1 and board[c - 2][d - 1] != 1:
                temp = [[a, b], [c - 1, d - 1]]
                temp.sort()
                if temp not in check:
                    check.append(temp)
                    queue.append([temp, count + 1])
        # 세로
        else:
            if b < N and board[a - 1][b] != 1 and board[c - 1][d] != 1:
                temp = [[a, b], [c - 1, d + 1]]
                temp.sort()
                if temp not in check:
                    check.append(temp)
                    queue.append([temp, count + 1])
        # 우기준 시계방향 회전
        # 가로
        if a == c:
            if a - 2 >= 0 and board[a - 2][b - 1] != 1 and board[c - 2][d - 1] != 1:
                temp = [[a - 1, b + 1], [c, d]]
                temp.sort()
                if temp not in check:
                    check.append(temp)
                    queue.append([temp, count + 1])
        # 세로
        else:
            if b < N and board[a - 1][b] != 1 and board[c - 1][d] != 1:
                temp = [[a + 1, b + 1], [c, d]]
                temp.sort()
                if temp not in check:
                    check.append(temp)
                    queue.append([temp, count + 1])
        # 우기준 반시계방향 회전
        # 가로
        if a == c:
            if a < N and board[a][b - 1] != 1 and board[c][d - 1] != 1:
                temp = [[a + 1, b + 1], [c, d]]
                temp.sort()
                if temp not in check:
                    check.append(temp)
                    queue.append([temp, count + 1])
        # 세로
        else:
            if b - 2 >= 0 and board[a - 1][b - 2] != 1 and board[c - 1][d - 2] != 1:
                temp = [[a + 1, b - 1], [c, d]]
                temp.sort()
                if temp not in check:
                    check.append(temp)
                    queue.append([temp, count + 1])
    
    # 목적지를 찾지 못하는 경우
    return -1
