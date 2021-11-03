def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        # 최소갯수의 합보다 커질경우 반복 중지
        if i * (i + 1) / 2 > n:
            break
        
        # 짝수개로 구성 할 경우
        if i % 2 == 0:
            if (n / i) % 1 == 0.5:
                answer += 1
        
        # 홀수개로 구성 할 경우
        else:
            if n % i == 0:
                answer += 1
    
    return answer
