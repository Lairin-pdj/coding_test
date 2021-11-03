import re

def solution(str1, str2):  
    str1 = str1.upper()                                 # 문자열 처리
    str2 = str2.upper()
    str1 = re.sub(r"[^A-Z]", " ", str1)
    str2 = re.sub(r"[^A-Z]", " ", str2)
    
    set1 = []                                           # 각 문자열을 다중집합으로 변환
    for i in range(len(str1) - 1):
        if str1[i] != ' ' and str1[i + 1] != ' ':
            set1.append(str1[i] + str1[i + 1])
    set2 = []
    for i in range(len(str2) - 1):
        if str2[i] != ' ' and str2[i + 1] != ' ':
            set2.append(str2[i] + str2[i + 1])

    inter = []                                          # 교집합
    temp1 = set1[:]
    temp2 = set2[:]
    for i in temp1:
        if i in temp2:
            inter.append(i)
            temp2.pop(temp2.index(i))
    
    union = []                                          # 합집합
    for i in set1:
        union.append(i)
    for i in set2:
        union.append(i)
    for i in inter:
        union.pop(union.index(i))    
        
    if len(union) == 0:                                 # 예외처리
        return 65536
    
    return int((len(inter) / len(union)) * 65536)       # 결과출력
