from collections import deque

def solution(N, road, K):                                       # 다익스트라 알고리즘
    time = [500001, 0] + [500001 for i in range(N - 1)]
    table = [[-1 for i in range(N + 1)] for j in range(N + 1)]
    
    for a, b, c in road:                                        # 주어진 path를 테이블로 정리
        if table[a][b] != -1:
            table[a][b] = table[b][a] = min(c, table[a][b])
        else:    
            table[a][b] = table[b][a] = c
            
    check = deque()
    check.append([1, 0, [1]])                                   # 경로와 큐를 이용하여 최단거리 계산
    
    while len(check) > 0:
        a, b, c = check.popleft()
        for i, x in enumerate(table[a]):
            if x > -1:
                if time[i] >= time[a] + x:                      # 효율성을 위해 중복 제거
                    time[i] = time[a] + x
                    if b + x <= K and not i in c:
                        d = c[:]
                        d.append(i)
                        check.append([i, b + x, d])
                    
    count = 0
    for i in time:                                              # 경로중 시간안에 이동 가능한 갯수 체크
        if i <= K:
            count += 1
    
    return count
