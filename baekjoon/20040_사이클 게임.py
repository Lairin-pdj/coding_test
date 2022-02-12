import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

# 파싱
n, m = map(int, input().split())

# 분리집합을 통한 부모 체크
def find(n):
    if n != parent[n]:
        return find(parent[n])
    return n

def union(n1, n2):
    n1 = find(n1)
    n2 = find(n2)
    
    parent[n2] = n1

parent = [i for i in range(n)]
answer = 0
for i in range(1, m + 1):
    a, b = map(int, input().split())
    
    # 부모가 다르면 유니온
    if find(a) != find(b):
        union(a, b)
    # 부모가 같으면 사이클이므로 탈출
    else:
        answer = i
        break

# 결과 출력
print(answer)
