def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    # 도착하지 못한 선수는 1명인 점에서 착안
    # 각각을 정렬 후 비교하여 다르게 되는 부분에서 체크 
    for i in range(len(participant) - 1):
        if(participant[i] != completion[i]):
            answer = participant[i]
            return answer
        
    # 정렬 순으로 맨 마지막 선수가 도착하지 못하였을 경우 체크
    answer = participant[len(participant) - 1]
    return answer
