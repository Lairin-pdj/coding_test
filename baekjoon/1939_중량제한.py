from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# mid 무게로 도착할 수 있는지 체크
def bfs(mid):
    wei[start] = 1

    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
    
        # 도착한 경우
        if now == end:
            return True
    
        # 지나 갈 수 있다면 진행
        for to, can in dic[now]:
            if wei[to] == 0 and mid <= can:
                wei[to] = 1
                queue.append(to)
    
    # 도착할 수 없는 경우
    return False

# 파싱
n, m = map(int, input().split())

# 해싱
dic = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    
    dic[a].append((b, c))
    dic[b].append((a, c))
    
start, end = map(int, input().split())

# 이분 탐색
low, high = 1, 1000000000

while low <= high:
    wei = [0 for _ in range(n + 1)]
    mid = (low + high) // 2
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1

# 결과 출력
print(high)
