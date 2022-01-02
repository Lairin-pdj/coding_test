import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))

# 계산
ns = [i ** 2 for i in nums]

# 결과 출력
print((((sum(nums) ** 2) - sum(ns)) // 2) % 1000000007)
