from bisect import bisect_left
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
querys = list(map(int, input().split()))

for i in querys:
    idx = bisect_left(nums, i)
    
    if idx < n and nums[idx] == i:
        print(1)
    else:
        print(0)
