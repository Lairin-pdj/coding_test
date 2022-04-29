import sys
input = sys.stdin.readline

# 파싱
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

# 선분 생성 및 분리
ver, hor = [], []
for i in range(n):
    # x좌표가 같은 수직선
    if points[i - 1][0] == points[i][0]:
        ver.append((points[i - 1][1], points[i][1]))
    # y좌표가 같은 수평선
    else:
        hor.append((points[i - 1][0], points[i][0]))

# 주어진 선분들에 대해 최대 체크 함수
def check(lines):
    # in, out 체크
    high = 0
    enter, out = [], []
    for a, b in lines:
        if a > b:
            a, b = b, a
        
        enter.append(a)
        out.append(b)
    enter.sort()
    out.sort()
    
    # 최댓값 체크
    now = 0
    i, j = 0, 0
    while i < len(lines) and j < len(lines):
        if enter[i] < out[j]:
            i += 1
            now += 1
            high = max(high, now)
        elif enter[i] > out[j]:
            j += 1
            now -= 1
        else:
            i += 1
            j += 1
    
    # 최댓값 반환
    return high

# 결과 출력
print(max(check(ver), check(hor)))
