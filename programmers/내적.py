def solution(a, b):
    answer = 0
    
    # 내적 수식 대입
    for i in range(len(a)):
        answer += (a[i] * b[i])
       
    return answer
