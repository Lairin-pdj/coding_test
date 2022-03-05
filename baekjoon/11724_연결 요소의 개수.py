from collections import deque, defaultdict
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
dic = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

# 체크
check = [False] * (n + 1)
count = 0
for i in range(1, n + 1):
    if not check[i]:
        
        # bfs로 순회
        queue = deque([i])
        check[i] = True
        
        while queue:
            x = queue.popleft()
            
            for j in dic[x]:
                if not check[j]:
                    queue.append(j)
                    check[j] = True
        
        count += 1

# 결과 출력
print(count)
