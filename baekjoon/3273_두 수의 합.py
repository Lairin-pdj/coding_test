from bisect import bisect_left
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
x = int(input())

# 케이스 체크
count = 0
for i in range(n):
    temp = x - nums[i]
    idx = bisect_left(nums, temp)
    
    if i < idx < n and nums[idx] + nums[i] == x:
        count += 1

# 정답 출력
print(count)
