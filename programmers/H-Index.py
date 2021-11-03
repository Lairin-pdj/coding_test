def solution(citations):
    citations.sort()                
    n = len(citations)
    
    for i in range(n):                  # 정렬을 통해 남은 논문 수 보다 값이 커지면 반환
        if n - i <= citations[i]:
            return n - i
    
    return 0
