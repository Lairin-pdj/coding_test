def solution(s):
    stack = []
    
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == "(" and i == ")":
                stack.pop()
            else:
                stack.append(i)
    
    if len(stack) == 0:
        return True
    else:
        return False
