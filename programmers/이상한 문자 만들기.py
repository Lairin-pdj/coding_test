def solution(s):
    words = s.split(" ")
    
    answer = ""
    for word in words:
        for i, x in enumerate(word):
            if i % 2 == 0:
                answer += x.upper()
            else:
                answer += x.lower()
        answer += " "
    
    return answer[:-1]
