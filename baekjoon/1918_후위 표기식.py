import sys
input = sys.stdin.readline

# 파싱
infix = input().rstrip()

# 스택을 이용해 위치 변경
stack = []
for i in infix:
    # 영어일 경우 바로 출력
    if i.isalpha():
        print(i, end = "")
    # 우선순위 상 stack 전부 처리
    elif i in ["+", "-"]:
        if stack:
            while stack:
                temp = stack.pop()
                
                if temp == "(":
                    stack.append(temp)
                    break
                
                print(temp, end = "")
                
            stack.append(i)
        else:
            stack.append(i)
    # +, - 를 빼고 전부 처리
    elif i in ["*", "/"]:
        if stack:
            while stack:
                temp = stack.pop()
                
                if temp in ["+", "-", "("]:
                    stack.append(temp)
                    break
                
                print(temp, end = "")
                
            stack.append(i)
        else:
            stack.append(i)
    # 우선순위 최상위 체킹
    elif i == "(":
        stack.append(i)
    # 괄호 전부 처리
    elif i == ")":
        while stack:
            temp = stack.pop()
            
            if temp == "(":
                break
            else:
                print(temp, end = "")

# 남은 스택 정리
while stack:
    temp = stack.pop()
    
    print(temp, end = "")
