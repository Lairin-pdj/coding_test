import re
from itertools import permutations

def solution(expression):
    answer = 0
    
    nums = list(map(int, re.split("[-*+]", expression)))            # split을 이용해 숫자만 추출
    
    ops = []
    count = set()
    for i in expression:                                            # 연산자 추출
        if not "0" <= i <= "9":
            ops.append(i)
            count.add(i)
    
    for order in permutations(count, len(count)):                   # 연산자 순서마다 연산 진행
        tempnums = nums[:]                                          # 깊은복사를 위해
        tempops = ops[:]
        
        for doop in order:                                          # 연산순서에 맞게 연산 진행
            i = 0
            while i < len(tempops):
                if tempops[i] == doop:
                    if doop == "*":
                        tempnums[i + 1] = tempnums[i] * tempnums[i + 1]
                    elif doop == "+":
                        tempnums[i + 1] = tempnums[i] + tempnums[i + 1]
                    elif doop == "-":
                        tempnums[i + 1] = tempnums[i] - tempnums[i + 1]
                    tempnums.pop(i)
                    tempops.pop(i)
                else:
                    i += 1
        
        answer = max(answer, abs(tempnums[0]))                      # 연산 최댓값 기록
        
    return answer
