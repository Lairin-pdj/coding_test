import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 0, 1000000000
while low <= high:
    mid = (low + high) // 2
    total = 0
    for i in trees:
        total += max(0, i - mid)
    
    if total < m:
        high = mid - 1
    else:
        low = mid + 1

# 결과 출력
print(high)
