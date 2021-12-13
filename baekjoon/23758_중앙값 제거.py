import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

# 2로 잘라 갯수 체크
count = 0
for i in range((n + 1) // 2):
    count += len(bin(nums[i])) - 3

# 결과 출력
print(count + 1)
