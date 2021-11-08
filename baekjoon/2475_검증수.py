import sys
input = sys.stdin.readline

# 파싱
nums = list(map(int, input().split()))

# 계산
total = 0
for i in nums:
    total += i ** 2

# 출력
print(total % 10)
