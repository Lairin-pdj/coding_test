from collections import defaultdict, deque
import sys
input = sys.stdin.readline
    
# 파싱
m, n = map(int, input().split())
table = [input().rstrip() for _ in range(m)]

# 위치기록
dic = defaultdict(list)
for i in range(m):
    for j in range(n):
        if table[i][j] not in (".", "#"):
            dic[table[i][j]].append((i, j))

# dfs
flag = True
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
queue = deque([(dic["0"][0][0], dic["0"][0][1], [], 0)])
visited = set([(dic["0"][0][0], dic["0"][0][1], ())])
while queue:
    x, y, keys, count = queue.popleft()
    
    # 출구 발견 
    if table[x][y] == "1":
        print(count)
        flag = False
        break
    
    # 이동
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i]
        
        # 정상적인 좌표 체크
        if 0 <= ax < m and 0 <= ay < n:
            # 벽이 아닌 경우
            if table[ax][ay] != "#":
                # 문의 경우
                if table[ax][ay].isupper():
                    # 해당 열쇠가 있는 경우
                    temp = keys[:]
                    if table[ax][ay].lower() in temp:
                        if (ax, ay, tuple(temp)) not in visited:
                            queue.append((ax, ay, temp, count + 1))
                            visited.add((ax, ay, tuple(temp)))

                # 열쇠의 경우
                elif table[ax][ay].islower():
                    temp = keys[:]
                    if table[ax][ay] not in temp:
                        temp.append(table[ax][ay])
                        temp.sort()
                    if (ax, ay, tuple(temp)) not in visited:
                        queue.append((ax, ay, temp, count + 1))
                        visited.add((ax, ay, tuple(temp)))
                
                # 기본 케이스
                else:
                    temp = keys[:]
                    if (ax, ay, tuple(temp)) not in visited:
                        queue.append((ax, ay, temp, count + 1))
                        visited.add((ax, ay, tuple(temp)))

# 탈출 실패
if flag:
    print(-1)
