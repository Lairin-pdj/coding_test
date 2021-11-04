from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 파싱
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    dic = defaultdict(list)
    
    # 역추적
    for _ in range(k):
        a, b = map(int, input().split())
        # 단방향 
        dic[b].append(a)
    
    win = int(input())
    
    # bfs로 경로 체크 
    check = [0 for _ in range(n + 1)]
    count = 0
    queue = deque()
    queue.append([win, times[win]])
    while queue:
        now, time = queue.popleft()
        
        # 선행 조건이 더이상 없는 경우
        if not dic[now]:
            # 최대치 체크
            count = max(count, time)
            continue
        
        for i in dic[now]:
            if check[i] < time + times[i]:
                check[i] = time + times[i]
                queue.append([i, time + times[i]])

    # 값 체크 출력
    print(count)
