from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

# 분리집합 함수
def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
        return parent[n]
    return n

def union(n1, n2):
    n1 = find(n1)
    n2 = find(n2)
    
    # 인원 수 체크용 추가
    if n1 != n2:
        parent[n2] = n1
        many[n1] += many[n2]
    
# 파싱
t = int(input())
for _ in range(t):
    f = int(input())
    parent = [i for i in range(2 * f)]
    many = [1 for _ in range(2 * f)]
    dic = defaultdict(int)
    order = 0
    for _ in range(f):
        a, b = input().rstrip().split()
        
        # 처음 나온 친구는 자리 배정
        if a not in dic:
            dic[a] = order
            order += 1
        if b not in dic:
            dic[b] = order
            order += 1
        
        # 분리집합 실행
        union(dic[a], dic[b])
        
        # 같은 네트워크 인원 수 출력
        print(many[find(dic[a])])
