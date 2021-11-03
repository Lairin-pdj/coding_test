def solution(s):
    s = s.lower()
    
    p = 0
    y = 0
    for i in s:
        if i == "p":
            p += 1
        elif i == "y":
            y += 1
    
    if p == y:
        return True
    else:
        return False
