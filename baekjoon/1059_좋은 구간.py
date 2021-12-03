from bisect import bisect_left
import sys
input = sys.stdin.readline

# 파싱
l = int(input())
nums = list(map(int, input().split()))
nums.sort()
n = int(input())

if n > nums[0]:
    idx = bisect_left(nums, n)
    print(max(0, (nums[idx] - n) * (n - nums[idx - 1]) - 1))
else:
    print(max(0, (nums[0] - n) * n - 1))
