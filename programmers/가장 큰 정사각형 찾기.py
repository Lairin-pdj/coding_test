def solution(board):
    # dp를 이용
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i][j - 1], board[i - 1][j], board[i - 1][j - 1]) + 1
    
    # 각 줄의 최댓값 -> 전체 최댓값
    return max(list(map(max, board))) ** 2
