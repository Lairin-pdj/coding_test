from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
rects = [list(map(lambda x : int(float(x) * 10), input().split())) for _ in range(n)]

# x 선분 기준으로 사전 정리
dic = defaultdict(list)
for i in range(n):
    dic[rects[i][0]].append((1, rects[i][1], rects[i][1] + rects[i][3]))
    dic[rects[i][0] + rects[i][2]].append((-1, rects[i][1], rects[i][1] + rects[i][3]))

# 정렬하여 스위핑
answer = 0
length = 0
now = 0
points = []
for i in sorted(dic.keys()):
    
    # 이동에 따른 거리 합산
    answer += length * (i - now)
    
    # x 위치 수정
    now = i
    
    # points 체크
    for k in sorted(dic[i]):
        if k[0] == 1:
            points.append((k[1], 1))
            points.append((k[2], -1))
        elif k[0] == -1:
            points.remove((k[1], 1))
            points.remove((k[2], -1))
    
    # length 계산
    sPoints = sorted(points)

    temp = 0
    count = 1
    for j in range(len(sPoints) - 1):
        if count != 0:
            temp += sPoints[j + 1][0] - sPoints[j][0]
        count += sPoints[j + 1][1]
    
    length = temp

# 결과 출력
if answer % 100 == 0:
    print(answer // 100)
else:
    print(answer / 100)
