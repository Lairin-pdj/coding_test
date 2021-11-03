from math import ceil 
import sys
input = sys.stdin.readline

# 값 파싱
x, y = map(int, input().split(" "))
target = (y * 100) // x

# 불가능한 경우 제외하고 방정식 대입
if target >= 99:
    print(-1)
else:
    print(ceil((((target + 1) * x)  - (100 * y)) / (99 - target)))

    
    
# 다른 풀이
from math import ceil 
import sys
input = sys.stdin.readline

# 값 파싱
x, y = map(int, input().split(" "))
target = (y * 100) // x

# 불가능한 경우 제외하고 방정식 대입
if target >= 99:
    print(-1)
else:
    # 이분탐색
    start = 0
    end = 1000000000
    while start < end:
        mid = (start + end) // 2
        if (target + 1) < ((y + mid) * 100) / (x + mid):
            end = mid
        else:
            start = mid + 1
    
    # 최소가 아닐 수 있기 때문에
    while True:
        start -= 1
        if (target + 1) > ((y + start) * 100) / (x + start):
            start += 1
            break
    
    # 값 반환
    print(start)
