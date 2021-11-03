def solution(n):
    answer = ''
    
    while n > 0:                    # 3진법과 비슷하게 표현
        a = str(n % 3)
        if a == '0':                # 0일 경우에만 4로 표기하며 자리수를 줄이기위해 추가감소
            answer += '4'
            n -= 1
        else:
            answer += a
        
        n = n // 3
        
    return answer[::-1]             # 뒤집어서 출력
