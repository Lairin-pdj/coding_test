n = int(input())
nums = list(map(int, input().split(" ")))

high = max(nums)

# 에라스토테네스의 체
check = [False, False] + [True] * (high - 1)

for i in range(2, high + 1):
    if check[i]:
        for j in range(2 * i, high + 1, i):
            check[j] = False

# 갯수 체크
count = 0
for num in nums:
    if check[num]:
        count += 1
        
print(count)
