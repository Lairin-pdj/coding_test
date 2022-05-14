from collections import defaultdict
import sys
input = sys.stdin.readline

# 분리집합
def find(n):
    if n != root[n]:
        root[n] = find(root[n])
    
    return root[n]

def union(n1, n2):
    n1 = find(n1)
    n2 = find(n2)
    
    if n1 != n2:
        root[n2] = n1
        size[n1] += size[n2]

# 파싱
n, m, q = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(m)]
removes = [int(input()) for _ in range(q)]
root = [i for i in range(n + 1)]
size = [1 for _ in range(n + 1)]

# 제거된 후의 상태 복원
check = set(removes)
for i in range(m):
    if i + 1 not in check:
        union(lines[i][0], lines[i][1])

# 반대로 간선 설치
cost = 0
for i in range(q - 1, -1, -1):
    a, b = lines[removes[i] - 1][0], lines[removes[i] - 1][1]
    ra, rb = find(a), find(b)
    if ra != rb:
        cost += size[ra] * size[rb]
        union(ra, rb)
    
# 결과 출력
print(cost)
