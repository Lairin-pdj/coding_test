from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 파싱
n, m, r = map(int, input().split())
dic = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())

    # 간선 설정
    dic[u].append(v)
    dic[v].append(u)

# bfs
queue = deque([r])
check = set([r])
count = 1
record = [0] * n
while queue:
    now = queue.popleft()
    record[now - 1] = count
    count += 1

    for i in sorted(dic[now], key=lambda x : -x):
        if i not in check:
            check.add(i)
            queue.append(i)

# 출력
for i in record:
    print(i)
