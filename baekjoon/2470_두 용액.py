from bisect import bisect_left
import sys 
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

# 이분탐색을 이용한 최소값 체크
low = 2000000000
left, right = 0, n - 1
for i, x in enumerate(nums):
    # 0을 만들 수 있는 값의 위치 파악
    idx = bisect_left(nums, -x)
    temp = 2000000000
    if 0 < idx and idx - 1 != i:
        temp = min(temp, abs(x + nums[idx - 1]))
        if low > temp:
            low = temp
            case = [x, nums[idx - 1]]
    if idx < n and idx != i:
        temp = min(temp, abs(x + nums[idx]))
        if low > temp:
            low = temp
            case = [x, nums[idx]]

# 결과 출력
case.sort()
print(*case)
