from collections import deque, defaultdict
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
lad = defaultdict(int)
for _ in range(n):
    a, b = map(int, input().split())
    lad[a] = b
sna = defaultdict(int)
for _ in range(m):
    a, b = map(int, input().split())
    sna[a] = b

# 모든 경우의 수를 체크하나 중복된 자리에 오는 것은 제외
check = [False] * 101

queue = deque([(1, 0)])
check[1] = True
while queue:
    x, count = queue.popleft()
    
    # 탈출 조건
    if x == 100:
        print(count)
        break
    
    # 주사위 경우의 수 체크
    for i in range(1, 7):
        # 사다리인 경우
        if x + i in lad and not check[lad[x + i]]:
            queue.append((lad[x + i], count + 1))
            check[lad[x + i]] = True
        # 뱀인 경우
        elif x + i in sna and not check[sna[x + i]]:
            queue.append((sna[x + i], count + 1))
            check[sna[x + i]] = True
        elif x + i <= 100 and x + i not in lad and x + i not in sna and not check[x + i]:
            queue.append((x + i, count + 1))
            check[x + i] = True
