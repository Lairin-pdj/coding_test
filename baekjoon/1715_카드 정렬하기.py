import sys, heapq
input = sys.stdin.readline

# 파싱
n = int(input())
nums = []
for _ in range(n):
    heapq.heappush(nums, int(input()))

# 덧셈
count = 0
while len(nums) > 1:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    count += a + b
    heapq.heappush(nums, a + b)

# 결과 출력
print(count)
