import sys
input = sys.stdin.readline

# 파싱
k, n = map(int, input().split())
nums = []
total = 0
for _ in range(k):
    temp = int(input())
    total += temp
    nums.append(temp)

# 이분탐색
low = 0
high = total // n
while low <= high:
    mid = (low + high) // 2
    
    count = 0
    for i in nums:
        if mid == 0:
            count += n
        else:
            count += (i // mid)
    
    if count >= n:
        low = mid + 1
    else:
        high = mid - 1

# 결과 출력
print(high)
