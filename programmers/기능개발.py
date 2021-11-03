import math

def solution(progresses, speeds):
    answer = []
    remain = []
    
    #남은 일 수 계산
    for p, s in zip(progresses, speeds):
        remain.append(math.ceil((100 - p) / s))
    
    #배포 수 계산
    temp = 0
    count = 0
    for i in remain:
        if temp == 0:
            temp = i
        elif i > temp:
            answer.append(count)
            count = 0
            temp = i          
        count += 1
        
    answer.append(count)
            
    return answer
