import sys
input = sys.stdin.readline

# 방향 체크 함수
def ccw(x1, y1, x2, y2, x3, y3):
    s = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    
    if s > 0:
        return 1
    elif s < 0:
        return -1
    else:
        return 0

# 파싱
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# 결과 출력
a = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
b = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
if a <= 0 and b <= 0:
    if a == 0 and b == 0:
        # 평행한 경우 
        if (x2 == x1 and x4 == x3) or (x2 != x1 and x4 != x3 and ((y2 - y1) / (x2 - x1)) == ((y4 - y3) / (x4 - x3))):
            # 겹침 체크
            if x1 == x2:
                if min(y1, y2) < min(y3, y4):
                    if max(y1, y2) > min(y3, y4):
                        print(1)
                    elif max(y1, y2) == min(y3, y4):
                        print(1)
                        if (x1, y1) in ((x3, y3), (x4, y4)):
                            print(x1, y1)
                        else:
                            print(x2, y2)
                    else:
                        print(0)
                else:
                    if max(y3, y4) > min(y1, y2):
                        print(1)
                    elif max(y3, y4) == min(y1, y2):
                        print(1)
                        if (x1, y1) in ((x3, y3), (x4, y4)):
                            print(x1, y1)
                        else:
                            print(x2, y2)
                    else:
                        print(0)
            else:
                if min(x1, x2) < min(x3, x4):
                    if max(x1, x2) > min(x3, x4):
                        print(1)
                    elif max(x1, x2) == min(x3, x4):
                        print(1)
                        if (x1, y1) in ((x3, y3), (x4, y4)):
                            print(x1, y1)
                        else:
                            print(x2, y2)
                    else:
                        print(0)
                else:
                    if max(x3, x4) > min(x1, x2):
                        print(1)
                    elif max(x3, x4) == min(x1, x2):
                        print(1)
                        if (x1, y1) in ((x3, y3), (x4, y4)):
                            print(x1, y1)
                        else:
                            print(x2, y2)
                    else:
                        print(0)
        # 양끝 점이 같은 경우
        else:
            print(1)
            if (x1, y1) in ((x3, y3), (x4, y4)):
                print(x1, y1)
            else:
                print(x2, y2)
    else:
        print(1)
        px = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
        py = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) *(x3 * y4 - y3 * x4)
        d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        print(px / d, py / d)
else:
    print(0)
