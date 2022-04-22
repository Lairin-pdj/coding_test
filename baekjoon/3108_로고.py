import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

# 파싱
n = int(input())
recs = [list(map(int, input().split())) for _ in range(n)] + [[0, 0, 0, 0]]

# 분리 집합
def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x1, x2):
    x1 = find(x1)
    x2 = find(x2)
    
    root[x2] = x1
    
# 출동처리
# 0 = left, 1 = bottom, 2 = right, 3 = top
def check(a, b):
    
    # 사각형이 겹치는 경우
    if a[0] <= b[2] and a[2] >= b[0] and a[1] <= b[3] and a[3] >= b[1]:
        
        # 아예 포함 되는 경우
        if (a[0] < b[0] and a[2] > b[2] and a[1] < b[1] and a[3] > b[3]) or (a[0] > b[0] and a[2] < b[2] and a[1] > b[1] and a[3] < b[3]):
            
            return False
        
        return True
    
    return False

# 집합 처리
root = [i for i in range(n + 1)]
for i in range(n):
    for j in range(i + 1, n + 1):
        if check(recs[i], recs[j]):
            union(i, j)

# 결과 처리
for i in range(n + 1):
    find(i)
answer = set(root)

# 결과 출력
print(len(answer) - 1)
