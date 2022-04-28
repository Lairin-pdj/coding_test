import sys
input = sys.stdin.readline

# 파싱
n, k, d = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(k)]

# 이분탐색
low = 1
high = n
while low <= high:
    mid = (low + high) // 2
    
    # 현재 선물 상자 가능 위치 체크
    temp = 0
    for a, b, c in table:
        if mid >= a:
            temp += ((min(mid, b) - a) // c) + 1
    
    # 수가 적은 경우
    if temp < d:
        low = mid + 1
    
    # 같거나 많은 경우
    else:
        high = mid - 1

# 결과 출력
print(low)
