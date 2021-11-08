import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

def recursion(a, k):
    if len(a) == m:
        print(*a)
    else:
        for i in range(k, n):
            recursion(a + [nums[i]], i)

# 파싱
n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 사전 순을 위한 정렬
nums.sort()

# 재귀 진행
recursion([], 0)
