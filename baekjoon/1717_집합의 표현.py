import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

# 파싱
n, m = map(int, input().split())

# 분리집합 함수
def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
        return parent[n]
    return n

def union(n1, n2):
    n1 = find(n1)
    n2 = find(n2)
    
    parent[n2] = n1

# 계산 및 결과 출력
parent = [i for i in range(n + 1)]
for _ in range(m):
    order, a, b = map(int, input().split())
    
    # 집합 결합
    if order == 0:
        union(a, b)
    # 출력
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
