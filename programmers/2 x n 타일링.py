def solution(n): 
    count = [0, 1, 2] + [0 for _ in range(n - 2)] 
    
    for i in range(3, len(count)):
        count[i] = count[i - 2] + count[i - 1]              # 피보나치 수열
        if count[i] > 1000000007:
            count[i] = count[i] % 1000000007
    
    return count[-1]
