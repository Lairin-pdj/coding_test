from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n, m, b = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# 최저, 최고 체크 및 높이 체크
top, bottom = 0, 256
dic = defaultdict(int)
for i in range(n):
    for j in range(m):
        top = max(top, maps[i][j])
        bottom = min(bottom, maps[i][j])
        dic[maps[i][j]] += 1

# 결과 값 변수
answer = 256 * 2 * n * m
high = 0

# 각 블럭의 높이에 맞도록 브루트포스
for i in range(bottom, top + 1):
    time = 0
    remain = 0
    # 각 블럭을 같은 높이로 맞출 때 비용 계산
    for j in dic.keys():
        count = dic[j]
        temp = j - i
        if temp > 0:
            time += temp * 2 * count
            remain += temp * count
        else:
            time -= temp * count
            remain += temp * count
    
    # 재고가 모자라면 불가능
    if remain + b >= 0:
        # 최상값 저장
        if time < answer:
            answer = time
            high = i
        elif time == answer:
            high = max(high, i)

# 결과 출력
print(answer, high)

'''
# 비효율적인 코드
import sys
input = sys.stdin.readline

# 파싱
n, m, b = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# 최저, 최고 체크
top, bottom = 0, 256
for i in range(n):
    for j in range(m):
        top = max(top, maps[i][j])
        bottom = min(bottom, maps[i][j])

# 결과 값 변수
answer = 256 * 2 * n * m
high = 0

# 각 블럭의 높이에 맞도록 브루트포스
for i in range(bottom, top + 1):
    time = 0
    remain = 0
    # 각 블럭을 같은 높이로 맞출 때 비용 계산
    for k in range(n):
        for l in range(m):
            temp = maps[k][l] - i
            if temp > 0:
                time += temp * 2
                remain += temp
            else:
                time -= temp
                remain += temp
    
    # 재고가 모자라면 불가능
    if remain + b >= 0:
        # 최상값 저장
        if time < answer:
            answer = time
            high = i
        elif time == answer:
            high = max(high, i)

# 결과 출력
print(answer, high)
'''
