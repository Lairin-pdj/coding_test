def solution(N, stages):
    nCount = []
    temp = len(stages)
    
    # 각 층별 도달 유저 체크 
    for i in range(1, N + 1):
        count = stages.count(i)
        if count == 0:
            nCount.append([0, i])
        else:
            nCount.append([count / temp, i])
            
        # 다음 스테이지의 도전자는 그 전 층까지의 성공자를 제외해야하기 때문에 제외
        temp -= count
    
    # 실패율 기준으로 정렬
    rank = sorted(nCount, key=lambda x : (-x[0], x[1]))
    
    answer = []
    
    for x, i in rank:
        answer.append(i)
        
    return answer
