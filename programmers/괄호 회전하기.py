def solution(s):
    answer = 0

    for i in range(len(s)):                     # 1칸씩 회전
        s = s[1:] + s[0]
        
        stack = []
        
        for i in s:                             # 스택을 이용하여 괄호 체크
            if i in ["[", "]"]:
                if len(stack) > 0 and stack[-1] == "[" and i == "]":
                    stack.pop()
                else:
                    stack.append(i)
            elif i in ["{", "}"]:
                if len(stack) > 0 and stack[-1] == "{" and i == "}":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                if len(stack) > 0 and stack[-1] == "(" and i == ")":
                    stack.pop()
                else:
                    stack.append(i)
        
        if len(stack) == 0:                     # 괄호가 올바르면 체크
            answer += 1
        
    return answer
