from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
nums = deque([i for i in range(1, n + 1)])
query = list(map(int, input().split()))

# 횟수 체크
count = 0
for num in query:
    count += min(nums.index(num), len(nums) - nums.index(num))
    nums.rotate(-nums.index(num))
    nums.popleft()

# 결과 출력
print(count)
