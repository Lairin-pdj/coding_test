import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))

# 순회
count = 0
i, j = 0, 1
check = set([nums[i]])
while j < n:
    
    if nums[j] not in check:
        check.add(nums[j])
        j += 1
    else:
        check.remove(nums[i])
        count += (j - 1) - i
        i += 1

# 잔여 처리
# i 순회 마무리(1부터 j - i - 1까지의 합)
count += ((j - i) * (j - i - 1)) // 2
# 1개씩 인 경우 추가
count += n

# 결과 출력
print(count)
