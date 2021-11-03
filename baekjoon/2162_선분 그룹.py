# pypy로만 효율성 통과
# python3로 통과하게 하기 위해 추가적인 알고리즘 변경이 요구됨

import sys
from collections import Counter

def ccw(x1, y1, x2, y2, x3, y3):                                    # 벡터를 통한 방향성 측정
    s = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    
    if s > 0:
        return 1
    elif s < 0:
        return -1
    else:
        return 0
        
def find(x):                                                        # 집합체크를 위한 find와 union 정의
    if lineroot[x] == x:
        return x
    else:
        return find(lineroot[x])
        
def union(x, y):
    x = find(x)
    y = find(y)

    lineroot[y] = x
        
lines = []

N = int(sys.stdin.readline())                                       # 선분정보 입력
for i in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split(" "))
    lines.append([a, b, c, d, i])

lineroot = [i for i in range(N)]

for i in range(N - 1):
    for j in range(i + 1, N):
        (x1, y1, x2, y2, i1), (x3, y3, x4, y4, i2) = lines[i], lines[j]
        a = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
        b = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    
        if a == 0 and b == 0:
            # 한 점이 맞닿아 있는 경우
            if (x1 == x3 and y1 == y3) or (x1 == x4 and y1 == y4) or (x2 == x3 and y2 == y3) or (x2 == x4 and y2 == y4):
                union(i1, i2)
            # 선분이 다른 선분에 포함되는 경우
            else:
                if (x1 <= x3 <= x2 or x3 <= x1 <= x4 or x4 <= x1 <= x3 or x2 <= x3 <= x1) and (y1 <= y3 <= y2 or y3 <= y1 <= y4 or y4 <= y1 <= y3 or y2 <= y3 <= y1):
                    union(i1, i2)
        # 각 점의 방향성이 달라 선분이 교차하는 경우
        elif a + b < 0 :                                
            union(i1, i2)
        
for i in range(N):                                                  # 그룹의 구성원 수를 확인하기 위해 
    lineroot[i] = find(i)

result = Counter(lineroot)                                          # counter를 이용하여 그룹의 수와 구성원 수 출력
print(len(result))
print(result.most_common()[0][1])
