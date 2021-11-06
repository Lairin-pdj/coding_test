import sys
input = sys.stdin.readline

# 파싱
n = int(input())
k = int(input())

# 이분탐색으로 특정 k번째 값 확인
# n * logn
low = 0
high = n ** 2
answer = 0
while low <= high:
    mid = (low + high) // 2
    
    count = 0
    for i in range(1, n + 1):
        count += min(mid // i, n)
    
    if count >= k:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1
    
# 결과 출력
print(answer)
