import sys, re
input = sys.stdin.readline

# 파싱
line = input().rstrip()
nums = list(map(int, re.split("[-+]", line)))
opes = list(filter(None, re.split("[^-+]", line)))

# + 우선 계산
i = 0
while i < len(opes):
    if opes[i] == "+":
        nums[i] = nums[i] + nums[i + 1]
        nums.pop(i + 1)
        opes.pop(i)
    else:
        i += 1

# 결과 출력
print(nums[0] - sum(nums[1:]))
