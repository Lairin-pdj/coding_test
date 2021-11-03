import re

def solution(m, n, board):    
    # 처리의 효율성을 위해 90도 회전
    newboard = []
    for i in list(map(list, zip(*board[::-1]))):
        newboard.append("".join(i))
    
    # 모두 제거할 때까지 반복
    while True:
        # 제거 가능 블럭파악
        temp = []
        for i in range(len(newboard) - 1):
            for j in range(len(newboard[0]) - 1):
                if newboard[i][j] == newboard[i + 1][j] == newboard[i][j + 1] == newboard[i + 1][j + 1]:
                    if newboard[i][j] != " ":
                        temp.append([i, j])
                    
        # 제거할 블럭이 없는 경우 탈출
        if len(temp) == 0:
            break
                    
        # 제거
        for i, j in temp:
            newboard[i] = newboard[i][:j] + "  " + newboard[i][j + 2:]
            newboard[i + 1] = newboard[i + 1][:j] + "  " + newboard[i + 1][j + 2:]
    
        # 공중 블럭 내림
        length = len(newboard[0])
        for i in range(len(newboard)):
            temp = re.sub(" ", "", newboard[i])
            newboard[i] = temp + " " * (length - len(temp))   
    
    # 갯수 파악
    answer = 0
    for line in newboard:
        for i in line:
            if i == " ":
                answer += 1
    
    return answer
