from itertools import combinations
import sys, bisect
input = sys.stdin.readline

# 파싱
n, c = map(int, input().split())
weis = list(map(int, input().split()))

# 0 ~ n / 2
case1 = [0]
weis1 = weis[:n // 2]
for i in range(1, len(weis1) + 1):
    for j in combinations(weis1, i):
        case1.append(sum(j))
case1.sort()

# n / 2 + 1 ~ n - 1
case2 = [0]
weis2 = weis[n // 2:]
for i in range(1, len(weis2) + 1):
    for j in combinations(weis2, i):
        case2.append(sum(j))
case2.sort()

# case1, case2 결합
answer = 0
for i in case2:
    answer += bisect.bisect_right(case1, c - i)
    
# 결과 출력
print(answer)
