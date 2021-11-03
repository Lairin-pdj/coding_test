import re

def solution(n, arr1, arr2):
    answer = []
    
    for a, b in zip(arr1, arr2):
        # 비트연산과 2진법을 통해 모양을 생성
        code = str(bin(a | b))[2:].zfill(n)
        
        # re를 이용하여 문자 치환
        code = re.sub("1", "#", code)
        code = re.sub("0", " ", code)
        
        answer.append(code)
    
    return answer
