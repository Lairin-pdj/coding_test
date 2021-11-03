def solution(s):
    stack = []
    
    for i in s:                         # 스택을 활용하여 중복체크
        if len(stack) != 0:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    
    if len(stack) == 0:                 # 전부 지워질시 1 반환
        return 1
    else:
        return 0
