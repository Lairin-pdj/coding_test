import sys
input = sys.stdin.readline

# 파싱
n, c = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

# 이분 탐색
low = 0
high = (nums[-1] - nums[0]) // (c - 1)
while low <= high:
    mid = (low + high) // 2
    
    # 가능한지 여부 체크
    # O(n)
    count = 1
    temp = nums[0]
    for i in range(1, n):
        if nums[i] - temp >= mid:
            temp = nums[i]
            count += 1
    
    # 가능한 경우 low 상승
    # 불가능한 경우 high 하락
    if count >= c:
        low = mid + 1
    else:
        high = mid - 1

# 결과 출력
print(high)
