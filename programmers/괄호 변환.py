def checkright(w):                              # 올바른 문자열인지 확인하는 함수
    stack = []
    
    for i in w:                                 # 스택을 이용하여 짝이 맞는지 체크
        if len(stack) != 0:
            if stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
            
    if len(stack) == 0:                         # 체크 결과를 반환
        return True
    else:
        return False
    

def modify(w):                                  # 주어진 문자열 변환 함수
    
    if checkright(w):                           # 주어진 문자열이 올바르면 바로 반환
        return w
    
    u = ''
    v = ''
    left = 0
    right = 0
    
    for i in w:                                 # u와 v로 분리하는 과정
        if len(u) != 0 and left == right:
            break
        else:
            if i == '(':
                left += 1
            else:
                right += 1    
            u += i
    v = w[len(u):]
    
    if checkright(u):                           # u가 올바르면 v를 변환 후 붙임
        u += modify(v)                          
    else:                                       # 아닐 경우 주어진 알고리즘 적용
        temp = '('
        temp += modify(v)
        temp += ')'
        u = u[1:-1]
        uReverse = ''
        for i in u:
            if i == '(':
                uReverse += ')'
            else:
                uReverse += '('
        temp += uReverse
        u = temp
    
    return u
    
    
def solution(p):                    
    answer = ''
    
    if p == '' or checkright(p):                # 주어진 문자열이 공백인 경우
        return p                                # 혹은 이미 올바른경우 바로 반환
    
    answer = modify(p)                          # 변환 후 반환
    
    return answer
