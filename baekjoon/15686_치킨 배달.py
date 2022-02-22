from itertools import combinations
from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

# 치킨집과 집 위치 파악
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if table[i][j] == 1:
            house.append((i, j))
        elif table[i][j] == 2:
            chicken.append((i, j))

# 사전을 통해 집마다 치킨집 별 위치 저장
dic = defaultdict(list)
for x, y in house:
    for tox, toy in chicken:
        dic[(x, y)].append((abs(x - tox) + abs(y - toy), tox, toy))
    dic[(x, y)].sort()

# 치킨 집 중 m개를 선택하여 최솟값 전부 계산
answer = 1000000000
for selected in combinations(chicken, m):
    temp = 0
    for x, y in house:
        for dist, tox, toy in dic[(x, y)]:
            if (tox, toy) in selected:
                temp += dist
                break
    answer = min(answer, temp)
    
# 결과출력
print(answer)
