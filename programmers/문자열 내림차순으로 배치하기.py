def solution(s):
    a = list(s)
    a.sort(key = lambda x : -ord(x))
    
    return "".join(a)
