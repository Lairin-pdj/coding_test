from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n, k = map(int, input().split())

# 누나가 뒤에 있는 경우
if n > k:
    print(n - k)
    print(1)
else:
    # 재방문 방지
    check = [100000 for _ in range(100001)]
    
    # bfs
    queue = deque()
    queue.append([n, 0])
    check[n] = False
    count = 0
    limit = 100000
    
    while queue:
        now, times = queue.popleft()
        
        # 최대치 설정
        if times > limit:
            break
        
        # 도착 체크
        if now == k:
            count += 1
            limit = times
            continue
        
        # 가능한 이동 체크
        if now - 1 >= 0 and check[now - 1] >= times + 1:
            queue.append([now - 1, times + 1])
            check[now - 1] = times + 1
        if now + 1 <= 100000 and check[now + 1] >= times + 1:
            queue.append([now + 1, times + 1])
            check[now + 1] = times + 1
        if now * 2 <= 100000 and check[now * 2] >= times + 1:    
            queue.append([now * 2, times + 1])
            check[now * 2] = times + 1

    # 결과 출력
    print(limit)
    print(count)
