def solution(n, s):
    # n이 s보다 클 경우 자연수로 불가능하므로 -1 반환
    if s // n == 0:
        return [-1]
    
    answer = []
    
    # 최대한 골고루 나누어 곱하는 것이 제일 큰 것을 활용
    # s // n과 (s // n) + 1로 적절하게 합이 s가 되도록 분배
    for i in range(n - (s % n)):
        answer.append(s // n)
        
    for i in range(s % n):
        answer.append((s // n) + 1)
    
    return answer
