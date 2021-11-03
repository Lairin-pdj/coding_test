# 10진수 num을 n진수로 변환하여 반환하는 함수
def jin(num, n):
    temp = ''
    
    if num == 0:
        return '0'
    
    while num > 0:
        now = num % n
        if now > 9:
            if now == 10:
                temp += 'A'
            elif now == 11:
                temp += 'B'
            elif now == 12:
                temp += 'C'
            elif now == 13:
                temp += 'D'
            elif now == 14:
                temp += 'E'
            elif now == 15:
                temp += 'F'
        else:
            temp += str(now)
        num = num // n
    
    return temp[::-1]
    

def solution(n, t, m, p):
    # 정답라인 생성
    line = ''
    i = 0
    while len(line) < m * (t - 1) + p:
        line += jin(i, n)
        i += 1
        
    # 튜브용 단어 추출
    answer = ''
    for i in range(p - 1, p + m * (t - 1), m):
        answer += line[i]
    
    return answer
