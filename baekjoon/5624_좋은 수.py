import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))

# x + y + z = i
# x + y = i - z
answer = 0
check = set()
for i in range(n):
    
    # i - z 체크
    for j in range(i):
        if nums[i] - nums[j] in check:
            answer += 1
            break
    
    # x + y 체크
    for j in range(i + 1):
        check.add(nums[i] + nums[j])

# 결과 출력
print(answer)
