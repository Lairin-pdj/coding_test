import sys
input = sys.stdin.readline

# 파싱
n = int(input())

nums = set(map(int, input().split(" ")))

nums = list(nums)
nums.sort()
print(" ".join(map(str, nums)))
