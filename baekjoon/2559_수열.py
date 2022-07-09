import sys
input = sys.stdin.readline

# 파싱
n, k = map(int, input().split())
nums = [0] + list(map(int, input().split()))

# 누적합
for i in range(2, n + 1):
    nums[i] += nums[i - 1]

# 최댓값 찾기
answer = -1000000000
for i in range(k, n + 1):
    answer = max(answer, nums[i] - nums[i - k])

# 결과 출력
print(answer)
