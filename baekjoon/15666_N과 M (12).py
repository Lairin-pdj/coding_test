import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

def recursion(a, k):
    if len(a) == m:
        answers.add(tuple(a))
    else:
        for i in range(k, n):
            recursion(a + [nums[i]], i)

# 파싱
n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 사전 순을 위한 정렬
nums.sort()

# 재귀 진행
answers = set()
recursion([], 0)

# 결과 정렬 및 출력
answer = list(answers)
answer.sort()
for i in answer:
    print(*i)
