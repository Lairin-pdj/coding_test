def solution(weights, head2head):
    answer = []
    
    for i, (weight, scores) in enumerate(zip(weights, head2head)):
        total = 0
        win = 0
        count = 0
        # i번째 선수 마다 기록표를 보며 체크
        for j, score in enumerate(scores):
            # 경기가 진행된 경우
            if score != "N":
                total += 1
                # 이긴 경우
                if score == "W":
                    win += 1
                    # 무게까지 많은 상대일 경우
                    if weights[j] > weights[i]:
                        count += 1
        
        # 승률 계산
        rate = 0
        if total != 0:
            rate = win / total
        
        # 리스트에 저장
        answer.append([i + 1, rate, count, weight])
    
    # 키를 이용해 문제 요구에 맡게 정렬
    answer.sort(key = lambda x : (-x[1], -x[2], -x[3], x[0]))
    
    # 순번만 반환
    return list(zip(*answer))[0]
