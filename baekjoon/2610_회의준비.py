from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

# disjoint set
def find(n):
    if n != root[n]:
        root[n] = find(root[n])
        
    return root[n]
    
def union(n1, n2):
    root[find(n2)] = find(n1)

# 파싱
n = int(input())
k = int(input())
link = defaultdict(list)
root = [i for i in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    union(a, b)
    link[a].append(b)
    link[b].append(a)

# 위원회 정리
for i in range(1, n + 1):
    find(i)
    
# 위원회 별 분리
team = defaultdict(list)
for i in range(1, n + 1):
    team[root[i]].append(i)

# 위원회 별 플로이드 워셜
answer = []
for mems in team.values():
    l = len(mems)

    # 치환
    change = defaultdict(int)
    for i in range(l):
        change[mems[i]] = i
    
    # 배열 생성
    dist = [[1000000000] * l for _ in range(l)]
    for i in range(l):
        dist[i][i] = 0
    
    # 경로 생성
    for mem in mems:
        for to in link[mem]:
            dist[change[mem]][change[to]] = 1
    
    # 플로이드 워셜
    for k in range(l):
        for i in range(l):
            for j in range(l):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 최소 찾기
    temp = 0
    low = 1000000000
    for i in range(l):
        now = max(dist[i])
        if now < low:
            low = now
            temp = i
    
    answer.append(mems[temp])

# 결과 출력
print(len(team.keys()))
answer.sort()
for i in answer:
    print(i)
