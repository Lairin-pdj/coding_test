import re

def solution(lines):
    answer = 0
    tIn = []
    tOut = []
    
    for i in lines:                                         # 트래픽을 시작시간과 완료시간으로 분리
        a, b, c = i.split(" ")
        b = re.sub("[.]", "", b)
        n1, n2, n3 = b.split(":")
        c = re.sub("s", "", c)
        b = int(n1) * 3600000 + int(n2) * 60000 + int(n3)   # 계산의 편의성을 위해 초로 변환 
        c = int(1000 * float(c))
        tIn.append(b - c - 499)                             # 1초간의 트래픽을 체크하기 위해 범위 증가 적용
        tOut.append(b + 499)
    
    tIn.sort()                                              # 시간 순으로 정렬
    tOut.sort()
    iMax = len(tIn)
    i = 0
    j = 0
    count = 0
    while True:                                             # 들어오고 나가는 과정을 통해 겹치는 숫자 확인
        if tIn[i] < tOut[j]:
            i += 1
            count += 1
            answer = max(answer, count)                     # 최대치 기록
        elif tIn[i] > tOut[j]:
            j += 1
            count -= 1
            answer = max(answer, count)
        else:
            i += 1
            j += 1
            count += 1
            answer = max(answer, count)
            count -= 1
        
        if i == iMax:
            break
        
    return answer                                           # 최대치 반환
