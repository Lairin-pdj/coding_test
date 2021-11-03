def solution(s, n):
    answer = ''
    
    for i in s:
        # 공백
        if i == " ":
            answer += " "
        # 대문자
        elif ord(i) < 91:
            answer += chr((ord(i) - 65 + n) % 26 + 65)
        # 소문자
        else:
            answer += chr((ord(i) - 97 + n) % 26 + 97)
    
    return answer
