from math import dist
import sys
input = sys.stdin.readline

# 파싱
xa, ya, xb, yb, xc, yc = map(int, input().split())

# 가능 여부 계산
flag = True

# 기울기가 같은 경우
if yb != ya:
    if yc != yb:
        if (xb - xa) / (yb - ya) == (xc - xb) / (yc - yb):
            flag = False
else:
    if yc == yb:
        flag = False

# 가능 여부에 따라
if flag:

    # 각 점간 거리 계산
    ab = dist((xa, ya), (xb, yb))
    ac = dist((xa, ya), (xc, yc))
    bc = dist((xb, yb), (xc, yc))
    
    # 최대 최소 계산
    high = 0
    low = 1000000000
    for i, j in [(ab, ac), (ab, bc), (ac, bc)]:
        high = max(high, (i + j) * 2)
        low = min(low, (i + j) * 2)
    
    # 결과 출력
    print(high - low)

# 불가능한 경우
else:
    print(-1.0)
