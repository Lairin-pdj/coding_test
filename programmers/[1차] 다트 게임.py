import re

def solution(dartResult):
    # 점수 파싱
    score = re.split("[^0-9]", dartResult)
    score = list(filter(None, score))
    
    # 보너스 파싱
    bonus = re.split("[^SDT]", dartResult)
    bonus = list(filter(None, bonus))
    
    # 보너스 적용 점수 계산
    final = [0] * len(score)
    for i in range(len(score)):
        temp = int(score[i])
        if bonus[i] == "D":
            temp = temp ** 2
        elif bonus[i] == "T":
            temp = temp ** 3
        
        final[i] = temp
    
    # 옵션 파싱
    option = re.split("[^*#]", dartResult)
    option = option[1:][1::2]
    
    # 각 자리 배율 계산
    mag = [1] * len(score)
    for i in range(len(option)):
        if option[i] == "#":
            mag[i] *= -1
        elif option[i] == "*":
            mag[i] *= 2
            if i - 1 >= 0:
                mag[i - 1] *= 2
    
    # 최종 점수 합산
    answer = 0
    for a, b in zip(final, mag):
        answer += a * b
    
    return answer
