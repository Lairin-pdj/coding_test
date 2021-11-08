from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
dic = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

# 부모 노드 체크
root = [i for i in range(n + 1)]
queue = deque()
queue.append([1, -1])
while queue:
    now, parent = queue.popleft()
    
    for i in dic[now]:
        if i != parent:
            root[i] = now
            queue.append([i, now])

# 결과 출력
for i in range(2, n + 1):
    print(root[i])
