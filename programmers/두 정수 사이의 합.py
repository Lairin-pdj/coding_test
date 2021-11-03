def solution(a, b):
    
    if a * b >= 0:
        return (a + b) * (abs(a - b) + 1) / 2
    else:
        if a > b:
            a, b = b, a
        return ((abs(a) + 1) + b) * (b - abs(a)) / 2
