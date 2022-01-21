from bisect import bisect_left
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))

# 가운데 숫자를 지정하며 양 옆으로 LIS 체크
answer = 0
for i in range(n):
    
    # 왼편 LIS
    left = []
    if i != 0:
        left.append(nums[0])
        for j in range(0, i):
            if nums[j] > left[-1]:
                if nums[i] > nums[j]:
                    left.append(nums[j])
            else:
                idx = bisect_left(left, nums[j])
                left[idx] = nums[j]

    # 오른편 LIS
    right = []
    if i != n - 1:
        right.append(nums[-1])
        for j in range(n - 1, i, -1):
            if nums[j] > right[-1]:
                if nums[i] > nums[j]:
                    right.append(nums[j])
            else:
                idx = bisect_left(right, nums[j])
                right[idx] = nums[j]
    
    # 결과값 계산
    if len(left) == 1 and left[0] == nums[i]:
        left = []
    if len(right) == 1 and right[0] == nums[i]:
        right = []
    answer = max(answer, len(left) + len(right) + 1)

# 결과 출력
print(answer)
