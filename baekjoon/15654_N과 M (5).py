from itertools import permutations
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 사전 순을 위한 정렬
nums.sort()

# 순열 출력
for i in permutations(nums, m):
    print(*i)
