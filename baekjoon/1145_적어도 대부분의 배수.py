import sys
input = sys.stdin.readline

# 파싱
nums = list(map(int, input().split()))

# 계산
target = min(nums)
while True:
    
    # 체크
    count = 0
    for i in nums:
        if target % i == 0:
            count += 1
    
    # 결과 출력
    if count >= 3:
        print(target)
        break
    
    # 1 상승
    target += 1
