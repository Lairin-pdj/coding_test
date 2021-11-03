def solution(s):
    answer = []
    
    for line in s:
        stack = []                                      
        count = 0
        # 스택을 이용하여 "110"을 만들 수 있는 만큼 전부 추출
        for i in line:
            if len(stack) < 2:
                stack.append(i)
            else:
                if stack[-1] == "1" and stack[-2] == "1" and i == "0":
                    stack.pop()
                    stack.pop()
                    count += 1
                else:
                    stack.append(i)
        
        # 연속으로 "111"이 오는 경우가 아니라면 "110"을 앞에 넣는 것이 수가 커짐
        # 그것을 문제없이 반복문 하나로 처리하기 위해 뒤에 허수 "11" 추가
        check = len(stack)   
        stack += ["1", "1"]
        for i, (a, b) in enumerate(zip(stack[:-1], stack[1:])):
            if a == "1" and b == "1":
                stack = stack[:i] + ["1", "1", "0"] * count + stack[i:]
                stack.pop()
                stack.pop()
                break
        
        answer.append("".join(stack))
    
    return answer
