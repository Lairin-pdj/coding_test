def solution(s):
    low = 1000000000
    high = -1000000000
    
    for num in list(map(int, s.split(" "))):
        low = min(low, num)
        high = max(high, num)
        
    return str(low) + " " + str(high)
