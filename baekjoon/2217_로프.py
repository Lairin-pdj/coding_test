import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

# 정렬 및 최대 계산
high = 0
nums.sort()
for i in range(n):
    high = max(high, (n - i) * nums[i])

# 결과 출력
print(high)
