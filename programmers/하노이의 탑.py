def hanoi(n, start, temp, end):
    global answer
    
    # 1개 일경우 바로 옮김
    if n == 1:
        answer.append([start, end])
    # 그렇지 않을 경우 3단계로 나누어 옮김
    else:
        # 나머지를 임시 저장소로 옮김
        hanoi(n - 1, start, end, temp)
        # 제일 큰 기둥을 목적지로 옮김
        hanoi(1, start, temp, end)
        # 임시 저장소에 있는 기둥을 목적지로 옮김 
        hanoi(n - 1, temp, start, end)
    

def solution(n):
    global answer
    answer = []
    
    hanoi(n, 1, 2, 3)
    
    return answer
