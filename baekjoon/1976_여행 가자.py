import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

# 파싱
n = int(input())
m = int(input())

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

# 분리집합 적용
parent = [i for i in range(n + 1)]
for i in range(1, n + 1):
    nums = list(map(int, input().split()))
    
    for j in range(i, n):
        if nums[j] == 1:
            union(i, j + 1)

# 경로 체크 및 결과 출력
route = list(map(int, input().split()))
temp = find(route[0])
flag = True
for i in range(1, m):
    if find(route[i]) != temp:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
