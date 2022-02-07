from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
field = [input().rstrip() for _ in range(n)]

# bfs
flag = True
dx, dy= [1, -1, 0, 0], [0, 0, 1, -1]
check = set([(0, 0, True)])
queue = deque([(0, 0, 1, True)])
while queue:
    x, y, count, can = queue.popleft()
    
    # 탈출 조건 체크 및 결과 출력
    if x == n - 1 and y == m - 1:
        print(count)
        flag = False
        break

    # 4방향 진행
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]

        if 0 <= ax < n and 0 <= ay < m and (ax, ay, can) not in check:
            # 돌파 여부에 따라
            if field[ax][ay] == "0":
                check.add((ax, ay, can))
                queue.append((ax, ay, count + 1, can))
            else:
                if can:
                    check.add((ax, ay, can))
                    queue.append((ax, ay, count + 1, False))

# 도달 불가시
if flag:
    print(-1)
