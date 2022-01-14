from collections import deque
import sys
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    # 정렬 및 좌우 배열 나누기
    nums.sort(reverse = True)
    queue = deque()
    temp = True
    for i in nums:
        if temp:
            temp = False
            queue.appendleft(i)
        else:
            temp = True
            queue.append(i)
    
    # 차이 계산
    count = 0
    log = list(queue)
    for i in range(len(log)):
        count = max(count, abs(log[i] - log[(i + 1) % len(log)]))
    
    # 정답 출력
    print(count)
