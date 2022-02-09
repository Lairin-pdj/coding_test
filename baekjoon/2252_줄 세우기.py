from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
dic = defaultdict(list)
check = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    check[b] += 1

# 위상정렬
# 시작 가능 지점 체크 및 큐에 삽입
queue = deque()
for i in range(1, n + 1):
    if check[i] == 0:
        queue.append(i)

# 정점 진행
answer = []
while queue:
    now = queue.popleft()
    answer.append(now)
    
    for i in dic[now]:
        if check[i] == 1:
            check[i] = 0
            queue.append(i)
        else:
            check[i] -= 1

# 결과 출력
print(*answer)
