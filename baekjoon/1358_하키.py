from math import dist
import sys
input = sys.stdin.readline

# 파싱
w, h, x, y, p = map(int, input().split())

# 체크
count = 0
for _ in range(p):
    px, py = map(int, input().split())
    
    # 네모 체크
    if x <= px <= x + w and y <= py <= y + h:
        count += 1
        continue
    
    # 원 체크
    if dist((x, y + (h / 2)), (px, py)) <= (h / 2) or dist((x + w, y + (h / 2)), (px, py)) <= (h / 2):
        count += 1

# 결과 출력
print(count)
