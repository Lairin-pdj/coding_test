from bisect import bisect_left
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))

# LIS
list = [nums[0]]
for i in range(1, n):
    if nums[i] > list[-1]:
        list.append(nums[i])
    else:
        idx = bisect_left(list, nums[i])
        list[idx] = nums[i]

# 결과 출력
print(len(list))
