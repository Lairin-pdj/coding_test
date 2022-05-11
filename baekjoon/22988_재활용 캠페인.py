import sys
input = sys.stdin.readline

# 파싱
n, x = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

# 투 포인터
i, j = 0, n - 1
answer = 0
use = 0

# 이미 넘는 경우 체크
while j >= 0 and nums[j] >= x:
    j -= 1
    answer += 1
    use += 1

# 양 옆을 더해 x / 2을 넘는 경우 체크
while i < j:
    if nums[i] + nums[j] >= x / 2:
        answer += 1
        use += 2
        i += 1
        j -= 1
    
    # 아닐 경우 이동
    else:
        i += 1

# 그 외는 3개씩 체크
answer += (n - use) // 3

# 결과 출력
print(answer)
