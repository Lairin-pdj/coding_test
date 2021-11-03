from math import atan, pi
import sys
input = sys.stdin.readline

# 테스트 
t = int(input())
for _ in range(t):
    n = int(input())
    # 테스트 마다 기댓값 계산 
    score = 0
    # 각 타겟의 기댓값 계산
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split(" "))
        a1, a2 = 0, 0
        
        # a의 각도
        if x1 != 0:
            a1 = atan(y1 / x1) * 180 / pi
            if x1 < 0:
                a1 += 180
        else:
            if y1 > 0:
                a1 = 90
            elif y1 < 0:
                a1 = 270
            else:
                continue
        
        # b의 각도
        if x2 != 0:
            a2 = atan(y2 / x2) * 180 / pi
            if x2 < 0:
                a2 += 180
        else:
            if y2 > 0:
                a2 = 90
            elif y2 < 0:
                a2 = 270
            else:
                continue
                
        # 값 변환 및 적용
        temp = abs(a1 - a2)
        if temp > 180:
            temp = 360 - temp
        elif temp == 180:
            temp = 360
        score += temp
        
    # 출력
    print("{:0.5f}".format(round(score / 360, 5)))
