import sys, heapq
input = sys.stdin.readline

# 파싱
n = int(input())
nums = []

for _ in range(n):
    x = int(input())
    
    if x == 0:
        if nums:
            print(-heapq.heappop(nums))
        else:
            print(0)
    else:
        heapq.heappush(nums, -x)
