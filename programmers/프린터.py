from collections import deque

def solution(priorities, location):
    stack = deque()
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]          # 효율성을 올리기 위해 체크
    top = 0

    for i, x in enumerate(priorities):              # 각 각을 좌표와 우선도로 정리
        stack.append([i, x])
        count[x] += 1
        top = max(top, x)
        
    printcount = 0
    while len(stack) != 0:                          # 우선도가 높은 작업부터 진행
        if stack[0][1] == top:
            printcount += 1
            if stack[0][0] == location:
                return printcount
            count[top] -= 1
            while count[top] == 0:
                top -= 1
            stack.popleft()
        else:                                       # 우선도가 높지 않으면 뒤 순번으로 이동
            stack.rotate(-1)
