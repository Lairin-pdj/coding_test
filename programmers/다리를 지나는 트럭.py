def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks = truck_weights[::-1]
    
    temp = []
    wei = 0
    while len(trucks) > 0:
        # 탈출 조건 체크 및 탈출
        for a, b in temp:
            if b + bridge_length - 1 <= time:
                wei -= a
                temp.pop(temp.index([a, b]))
                
        # 태울 수 있다면 태우면서 1초 증가
        if wei + trucks[-1] <= weight:
            wei += trucks[-1]
            time += 1
            temp.append([trucks.pop(), time])
        # 태울 수 있는 상태가 되도록 시간 스킵
        else:
            time = temp[0][1] + bridge_length - 1
        
    # 남은 트럭 건너기
    time = temp[-1][1] + bridge_length
        
    return time
