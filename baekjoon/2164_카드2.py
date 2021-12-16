from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = deque([i for i in range(1, n + 1)])

# 순환 
while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())

# 결과 출력
print(nums[0])
