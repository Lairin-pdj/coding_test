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
        # 양끝 점이 같은 경우
        if (x1, y1) in ((x3, y3), (x4, y4)) or (x2, y2) in ((x3, y3), (x4, y4)):
            print(1)
        # 평행한 경우 
        else:
            # 겹침 체크
            if min(x1, x2) < min(x3, x4):
                if max(x1, x2) > min(x3, x4):
                    print(1)
                else:
                    print(0)
            else:
                if max(x3, x4) > min(x1, x2):
                    print(1)
                else:
                    print(0)
    else:
        print(1)
else:
    print(0)
