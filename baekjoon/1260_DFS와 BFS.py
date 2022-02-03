from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 파싱
n, m, v = map(int, input().split())
dic = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

# 정렬
for i in dic.keys():
    dic[i].sort()

# dfs
def dfs(node):
    print(node, end = " ")
    
    for i in dic[node]:
        if i not in check:
            check.add(i)
            dfs(i)

# dfs 결과 출력
check = set([v])
dfs(v)
print()

# bfs 및 결과 출력
check = set([v])
queue = deque([v])
while queue:
    temp = queue.popleft()
    print(temp, end = " ")
    
    for i in dic[temp]:
        if i not in check:
            check.add(i)
            queue.append(i)
