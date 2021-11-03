from collections import deque

def solution(begin, target, words):
    answer = 1000000
    if not target in words:
        return 0
    
    check = deque()
    check.append([begin, 0, [begin]])               # bfs 기본 큐 설정
    
    while len(check) > 0:
        now, count, route = check.popleft()
        
        if now == target:                           # 정답시 최소값 체크
            answer = min(answer, count)
        
        for i in words:                             
            if not i in route:                      # 루트 안에 없는 단어중 1개만 다른 단어 찾아 큐에 추가
                differ = 0
                for a, b in zip(i, now):
                    if a != b:
                        differ += 1
                if differ == 1:
                    temp = route[:]
                    temp.append(i)
                    check.append([i, count + 1, temp])
    
    return answer
