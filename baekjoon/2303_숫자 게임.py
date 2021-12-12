from itertools import combinations
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
answer = 0
topscore = 0
for i in range(n):
    nums = list(map(int, input().split()))
    score = 0
    for a, b, c in combinations(nums, 3):
        temp = (a + b + c) % 10
        score = max(score, temp)
    
    if topscore <= score:
        topscore = score
        answer = i + 1

print(answer)
