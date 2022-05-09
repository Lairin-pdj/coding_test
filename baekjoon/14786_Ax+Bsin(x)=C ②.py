from math import sin
import sys
input = sys.stdin.readline

# 파싱
a, b, c = map(int, input().split())

# (c - b) / a < x < (c + b) / a
# 이분탐색
low = (c - b) / a
high = (c + b) / a
timer = 5000
while low <= high and timer:
    mid = (low + high) / 2
    
    temp = (c - (b * sin(mid))) / a

    if mid > temp:
        high = mid - 0.0000000001
    elif mid < temp:
        low = mid + 0.0000000001
    
    timer -= 1

# 결과 출력
print(mid)
