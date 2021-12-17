import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]

# 이분탐색
low = 0
high = ((m // n) + 1) * 1000000000
while low <= high:
    mid = (low + high) // 2
    
    check = 0
    for i in times:
        check += mid // i
    
    if check >= m:
        high = mid - 1
    else:
        low = mid + 1

# 결과 출력
print(low)
