import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

# 결과 출력
print(nums[0] * nums[-1])
