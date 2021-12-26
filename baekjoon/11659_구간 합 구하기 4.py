import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 구간합 계산
for i in range(1, n):
    nums[i] += nums[i - 1]

# 쿼리별 정답 출력
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        print(nums[b - 1])
    else:
        print(nums[b - 1] - nums[a - 2])
