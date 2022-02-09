from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
dic = defaultdict(list)
check = [0 for _ in range(n + 1)]
time = [0 for _ in range(n + 1)]
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    dp[i] = info[0]
    for j in range(1, len(info) - 1):
        dic[info[j]].append(i)
        check[i] += 1

# 위상정렬
# 시작 가능 지점 체크 및 큐에 삽입
queue = deque()
for i in range(1, n + 1):
    if check[i] == 0:
        queue.append(i)

# 정점 진행
while queue:
    now = queue.popleft()

    for i in dic[now]:
        if check[i] == 1:
            check[i] = 0
            queue.append(i)
        else:
            check[i] -= 1
        dp[i] = max(dp[i], time[i] + dp[now])

# 결과 출력
for i in range(1, len(time)):
    print(dp[i])
