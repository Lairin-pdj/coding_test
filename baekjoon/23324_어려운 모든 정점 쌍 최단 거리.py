from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

# union find
def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return
    else:
        parent[b] = a
    
# 파싱
n, m, k = map(int, input().split(" "))

parent = [i for i in range(n + 1)]

# k 번째 간선 만 제외하고 union
for i in range(m):
    a, b = map(int, input().split(" "))
    
    if i != k - 1:
        union(a, b)

# 그룹 체크
dic = defaultdict(int)
for i in range(1, len(parent)):
    dic[find(i)] += 1

answer = list(dic.values())
# 1그룹일 경우
if len(answer) == 1:
    print(0)
# 2그룹일 경우
else:
    print(answer[0] * answer[1])
