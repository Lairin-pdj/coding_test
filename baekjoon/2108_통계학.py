from collections import Counter
import sys

n = int(sys.stdin.readline())

nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

# 산술 평균
print(round(sum(nums) / len(nums)))

# 중앙값
nums.sort()
print(nums[len(nums) // 2])

# 최빈값
temp = Counter(nums).most_common()
if len(temp) > 1:
    if temp[0][1] == temp[1][1]:
        print(temp[1][0])
    else:
        print(temp[0][0])
else:
    print(temp[0][0])

# 범위
print(max(nums) - min(nums))
