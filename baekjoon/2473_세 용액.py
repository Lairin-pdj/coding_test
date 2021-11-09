from bisect import bisect_left
import sys 
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

# 이분탐색을 이용한 최소값 체크
low = 3000000000
case = []
# 한 값을 고정 시키고 2개 선택
for j in range(n):
    for i, x in enumerate(nums):
        # 0을 만들 수 있는 값의 위치 파악
        idx = bisect_left(nums, -(x + nums[j]))
        if 0 < idx and idx - 1 not in [i, j] and i != j:
            temp = abs(nums[j] + x + nums[idx - 1])
            if low > temp:
                low = temp
                case = [nums[j], x, nums[idx - 1]]
        if idx < n and idx not in [i, j] and i != j:
            temp = abs(nums[j] + x + nums[idx])
            if low > temp:
                low = temp
                case = [nums[j], x, nums[idx]]

# 결과 출력
case.sort()
print(*case)
