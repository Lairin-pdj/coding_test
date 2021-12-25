from collections import deque
import sys
input = sys.stdin.readline

bx = [1, -1, 0, 0]
by = [0, 0, 1, -1]

# 파싱
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    
    # 맵 생성
    space = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        space[y][x] = 1

    # 뭉치로 찾기
    count = 0
    check = set()
    for i in range(n):
        for j in range(m):
            if space[i][j] == 1 and (j, i) not in check:
                count += 1
                check.add((j, i))
                
                # 뭉치 전부 체크
                # bfs
                queue = deque()
                queue.append([j, i])
                while queue:
                    a, b = queue.popleft()
                    
                    for l in range(4):
                        qa = a + bx[l]
                        qb = b + by[l]
                        if 0 <= qa < m and 0 <= qb < n and (qa, qb) not in check and space[qb][qa] == 1:
                            queue.append([qa, qb])
                            check.add((qa, qb))

    # 결과 출력
    print(count)
