def solution(n):
    check = [False, False] + [True] * (n - 1)
    
    count = 0
    for i in range(2, n + 1):
        if check[i]:
            count += 1
            for j in range(2 * i, n + 1, i):
                check[j] = False
                
    return count
