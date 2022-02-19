from collections import deque
import sys
input = sys.stdin.readline

# 파싱
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# 선분 교차 체크
def ccw(x1, y1, x2, y2, x3, y3):
    s = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    
    if s > 0:
        return 1
    elif s < 0:
        return -1
    else:
        return 0

# 결과 출력
print(ccw(x1, y1, x2, y2, x3, y3))
