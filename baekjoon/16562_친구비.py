from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n, m, k = map(int, input().split())
fcost = [-1] + list(map(int, input().split()))

# disjoint set functions
def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]
    
def union(x1, x2):
    root[find(x2)] = find(x1)

# disjoint 적용
root = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    
    if a < b:
        union(a, b)
    else:
        union(b, a)

# root 간소화
for i in range(1, n + 1):
    find(i)

# 가격 체크
costs = defaultdict(int)
for i in range(1, n + 1):
    if root[i] not in costs:
        costs[root[i]] = fcost[i]
    else:
        costs[root[i]] = min(costs[root[i]], fcost[i])

# 결과 출력
result = sum(costs.values())
if result <= k:
    print(result)
else:
    print("Oh no")
