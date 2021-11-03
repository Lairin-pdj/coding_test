def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    
    for i in s:
        if not (48 <= ord(i) <= 57):
            return False
        
    return True
