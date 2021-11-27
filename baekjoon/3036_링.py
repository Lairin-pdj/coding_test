import sys, math
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))

for i in range(1, n):
    temp = math.gcd(nums[0], nums[i])
    print(nums[0] // temp, end = "/")
    print(nums[i] // temp)
