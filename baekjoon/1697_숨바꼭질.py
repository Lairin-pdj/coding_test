from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n, k = map(int, input().split())

# 누나가 뒤에 있는 경우
if n > k:
    print(n - k)
else:
    # 재방문 방지
    check = [True for _ in range(100001)]
    
    # bfs
    queue = deque()
    queue.append([n, [n]])
    check[n] = False
    
    while queue:
        now, route = queue.popleft()
        
        # 도착시 결과 출력 및 bfs 종료
        if now == k:
            print(len(route) - 1)
            break
        
        # 가능한 이동 체크
        if now - 1 >= 0 and check[now - 1]:
            queue.append([now - 1, route + [now - 1]])
            check[now - 1] = False
        if now + 1 <= 100000 and check[now + 1]:
            queue.append([now + 1, route + [now + 1]])
            check[now + 1] = False
        if now * 2 <= 100000 and check[now * 2]:    
            queue.append([now * 2, route + [now * 2]])
            check[now * 2] = False
