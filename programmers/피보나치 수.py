def solution(n):
    if n == 1:
        return 1
        
    fibo = [0, 1] + [0 for _ in range(n - 1)] 
    
    for i in range(2, len(fibo)):
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 1234567

    return fibo[-1]
