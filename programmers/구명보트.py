from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort()                               # 최대 2명인 점에서 착안
    people = deque(people)                      # 가벼운 사람과 무거운 사람을 같이 태움
    
    while len(people) > 1:
        if people[-1] + people[0] <= limit:     # 제한을 넘지 않으면 태움
            people.popleft()
            people.pop()
        else:                                   # 그렇지 않으면 무거운 사람을 혼자 보냄 
            people.pop()
        answer += 1
    
    if len(people) == 1:                        # 혼자 남은 경우 한 번 추가
        answer += 1
        
    return answer
