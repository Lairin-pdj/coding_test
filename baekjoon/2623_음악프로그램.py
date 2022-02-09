from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
dic = defaultdict(list)
check = [0 for _ in range(n + 1)]
for _ in range(m):
    order = list(map(int, input().split()))
    for a, b in zip(order[1:-1], order[2:]):
        dic[a].append(b)
        check[b] += 1

# 시작 가능 지점 체크 및 큐에 삽입
queue = deque()
for i in range(1, n + 1):
    if check[i] == 0:
        queue.append(i)

# 위상정렬
answer = []
while queue:
    now = queue.popleft()
    answer.append(now)

    for i in dic[now]:
        if check[i] == 1:
            check[i] = -1
            queue.append(i)
        else:
            check[i] -= 1

# 결과 출력
# 위상정렬이 제대로 이루어 지지 못한 경우 => 사이클이 존재하는 경우
if len(answer) != n:
    print(0)
else:
    for i in answer:
        print(i)
