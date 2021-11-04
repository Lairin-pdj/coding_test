from math import dist
import sys
input = sys.stdin.readline

def check(x, y, cx, cy, r):
    # (x, y)와 (cx, cy)의 거리가 r 이하면 포함
    if dist((x, y), (cx, cy)) < r:
        return True
    else:
        return False

# 파싱
t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        
        # 시작점과 도착점의 포함여부 체크
        start = check(x1, y1, cx, cy, r)
        end = check(x2, y2, cx, cy, r)
    
        # 여부에 따른 갯수 체크
        if start:
            if not end:
                count += 1
        elif end:
            count += 1

    # 케이스 마다 결과 출력
    print(count)
