from itertools import permutations
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 집합을 이용한 순열 중복 제거
answers = set()
for i in permutations(nums, m):
    answers.add(i)

# 정렬
answer = list(answers)
answer.sort()
    
# 결과 출력
for i in answer:
    print(*i)
