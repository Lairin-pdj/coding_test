from collections import deque

def solution(n, computers):
    answer = 0
    remain = [i for i in range(len(computers))]             # 남은 컴퓨터의들의 번호
    
    while len(remain) > 0:
        temp = set()                                        # 집합을 통해 중복 제거
        temp.add(remain[0])                                 # 하나를 루트로 지정
        
        check = deque()
        check.append(remain[0])                             
        
        while len(check) > 0:                               # 그것을 큐를 통해 연결된 모든 노드 체크
            a = check.popleft()
            for i, x in enumerate(computers[a]):
                if x == 1 and not i in temp:
                    temp.add(i)
                    check.append(i)
                    
        for i in temp:                                      # 연결된 네크워크는 목록에서 제외
            remain.pop(remain.index(i))
            
        answer += 1

    return answer
