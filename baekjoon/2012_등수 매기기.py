import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

# 정렬 및 그리디
nums.sort()
count = 0
for i, x in enumerate(nums):
    count += abs((i + 1) - x)

# 결과 출력
print(count)
