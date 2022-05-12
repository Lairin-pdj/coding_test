from heapq import heappush, heappop
from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
lecs = defaultdict(list)
day_max = 0
for _ in range(n):
    pay, day = map(int, input().split())
    lecs[day].append(pay)
    day_max = max(day_max, day)

# 날짜 별로 큐에 삽입
queue = []
answer = 0
for now in range(day_max, 0, -1):
    
    # 강의가 있다면 삽입
    if now in lecs:
        for lec in lecs[now]:
            heappush(queue, -lec)
    
    # 진행 할 수 있는 강의가 있다면 한개 진행
    if queue:
        answer -= heappop(queue)

# 결과 출력
print(answer)
