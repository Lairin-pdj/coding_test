import sys, heapq
input = sys.stdin.readline

# 파싱
n = int(input())

# 힙관리 및 출력
heap = []
for _ in range(n):
    temp = int(input())
    if temp != 0:
        heapq.heappush(heap, (abs(temp), temp))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
