from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
t = int(input())
dic = defaultdict(list)
for _ in range(t):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

# 갯수 체크
count = set()
queue = deque()
queue.append(1)
while queue:
    now = queue.popleft()
    
    for i in dic[now]:
        if i not in count:
            count.add(i)
            queue.append(i)

# 결과출력
print(len(count) - 1)
