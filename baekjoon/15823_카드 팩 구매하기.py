import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 이분탐색
low, high = 1, n // m
while low <= high:
    mid = (low + high) // 2

    # 가능 여부 체크
    count = 0
    
    # 투 포인터
    i, j = 0, 0
    check = set()
    while j < n:
        # 숫자가 겹치지 않는 경우
        if nums[j] not in check:
            check.add(nums[j])
        # 숫자가 겹치는 경우
        else:
            # 겹치는 숫자가 빠질 때 까지 제외
            while nums[j] in check:
                check.remove(nums[i])
                i += 1
            
            # 그 후 추가
            check.add(nums[j])
        
        # 성공한 경우
        if len(check) == mid:
            check = set()
            count += 1
            # 좌표이동
            i = j + 1
            j += 1
        # 실패한 경우
        else:
            j += 1
    
    # 갯수에 따라 값 수정
    if count < m:
        high = mid - 1
    else:
        low = mid + 1

# 결과 출력
print(high)
