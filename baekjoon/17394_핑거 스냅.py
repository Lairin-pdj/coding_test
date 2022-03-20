from collections import deque
import sys
input = sys.stdin.readline

# 에라스토테네스의 체
check = [False, False] + [True] * 99999

for i in range(2, 100001):
    if check[i]:
        for j in range(2 * i, 100001, i):
            check[j] = False

# 파싱
t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    
    # 소수가 있는지 체크
    flag = True
    for i in range(a, b + 1):
        if check[i]:
            flag = False
            break
    
    if flag:
        print(-1)
        continue
    
    # 현재 수가 목표치보다 적어 늘리기만 해야할 경우
    if n < a:
        for i in range(a, b + 1):
            if check[i]:
                print(i - n)
                break
    
    else:
        # bfs
        visited = set([n])
        queue = deque([(n, 0)])
        
        while queue:
            now, count = queue.popleft()
            
            # 탈출 조건
            if now <= 100000 and check[now] and a <= now <= b:
                print(count)
                break
            
            # 3으로 나누기
            if (now // 3) not in visited:
                visited.add(now // 3)
                queue.append((now // 3, count + 1))
            # 2로 나누기
            if (now // 2) not in visited:
                visited.add(now // 2)
                queue.append((now // 2, count + 1))
            # 하나 늘리기
            if now < 100000 and (now + 1) not in visited:
                visited.add(now + 1)
                queue.append((now + 1, count + 1))
            # 하나 줄이기
            if now > 0 and (now - 1) not in visited:
                visited.add(now - 1)
                queue.append((now - 1, count + 1))
