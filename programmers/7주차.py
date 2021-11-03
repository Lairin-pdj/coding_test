from itertools import combinations
from collections import defaultdict

def solution(enter, leave):
    
    # 입출입 시간을 계산하여 사전에 저장
    dic = defaultdict(list)
    
    i, j = 0, 0
    time = 0
    temp = []
    while i < len(enter):
        # 나가는 순서인 사람이 존재하면 나감
        if leave[j] in temp:
            temp.pop(temp.index(leave[j]))
            dic[leave[j]].append(time)
            j += 1
        # 나갈 수 있는 사람이 없으면 입장
        else:  
            temp.append(enter[i])
            dic[enter[i]].append(time)
            i += 1
        
        time += 1
    
    # 나가지 못한 사람이 존재하기에 처리
    while j < len(leave):
        dic[leave[j]].append(time)
        j += 1
        time += 1
    
    # 조합을 통해 2명씩 짝을 지어 체크
    answer = [0 for _ in range(len(enter))]
    for a, b in combinations(enter, 2):
        if not (dic[a][0] >= dic[b][1] or dic[a][1] <= dic[b][0]):
            answer[a - 1] += 1
            answer[b - 1] += 1
        
    return answer
