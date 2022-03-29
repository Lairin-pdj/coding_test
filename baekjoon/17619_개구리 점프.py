import sys
input = sys.stdin.readline

# 분리집합
def find(x):
    if x != root[x]:
        return find(root[x]) 
    return x

def union(n1, n2):
    root[find(n2)] = find(n1) 

# 파싱
n, q = map(int, input().split())
logs = []
for i in range(n):
    x1, x2, y = map(int, input().split())
    logs.append((x1, x2, i + 1))

# 정렬 및 집합 관계 형성
logs.sort()
root = [i for i in range(n + 1)]
high = logs[0][1]
for i in range(1, n):
    if high >= logs[i][0]:
        union(logs[i - 1][2], logs[i][2])
    high = max(high, logs[i][1])

# 쿼리 진행
for _ in range(q):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(1)
    else:
        print(0)
