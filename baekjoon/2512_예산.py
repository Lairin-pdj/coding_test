import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))
money = int(input())

# 최대치따라 구분
total = sum(nums)
if total <= money:
    # 요구치 만큼 다 줘도 남을 경우
    print(max(nums))
else:
    # 이분 탐색
    low = 0
    high = money
    while low <= high:
        mid = (low + high) // 2
        
        # 현재 mid일 때 최대 값
        count = 0
        for i in range(n):
            count += min(nums[i], mid)
        
        # count에 따른 mid 조정
        if count > money:
            high = mid - 1
        else:
            low = mid + 1
    
    # 결과 출력
    print(high)
