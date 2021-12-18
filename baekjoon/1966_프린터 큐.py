from collections import deque
import sys
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    prior = list(map(int, input().split()))
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    queue = deque()
    top = 0
    
    # 갯수 체크
    for i, x in enumerate(prior):
        queue.append([i, x])
        count[x] += 1
        top = max(top, x)
    
    # 순서 체크
    printcount = 0
    while len(queue) != 0:
        if queue[0][1] == top:
            printcount += 1
            if queue[0][0] == m:
                print(printcount)
                break
            count[top] -= 1
            while count[top] == 0:
                top -= 1
            queue.popleft()
        else:
            queue.rotate(-1)
