def solution(n):
    # 행 별로 계산
    board = []
    for i in range(n):
        board.append([])
    
    # 삽입할 숫자
    num = 1
    for i in range(1, n + 1):
        # 내려감
        if i % 3 == 1:
            for j in range(n - i + 1):
                board[j + 2 * (i // 3)].insert((i // 3), num)
                num += 1

        # 바닥채우기
        if i % 3 == 2:
            for j in range(n - i + 1):
                board[(n - 1) - (i // 3)].insert((i // 3) + 1 + j, num)
                num += 1

        # 올라감
        if i % 3 == 0:
            for j in range(n - i + 1):
                board[(n - 2 - j) - (i // 3 - 1)].insert((len(board[(n - 2 - j) - (i // 3 - 1)])) - (i // 3 - 1), num)
                num += 1
    
    # 정답으로 옮기기
    answer = []
    for k in board:
        answer.extend(k)
        
    return answer
