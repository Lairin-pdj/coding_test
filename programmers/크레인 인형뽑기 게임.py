def solution(board, moves):
    
    answer = 0
    stack = []
    
    for i in moves:
        for j in range(len(board)):
            # i번째 열의 상태를 위에서 부터 차례대로 체크
            if board[j][i - 1] != 0:
                # 스택의 상태에 따라 별도 체크
                if len(stack) != 0:
                    if stack[-1] != board[j][i - 1]:
                        stack.append(board[j][i - 1])
                    else:
                        stack.pop()
                        answer += 2
                else:
                    stack.append(board[j][i - 1])
                board[j][i - 1] = 0 
                break
    
    return answer
