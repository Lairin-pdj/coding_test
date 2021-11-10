from itertools import combinations
import sys 
input = sys.stdin.readline

# 파싱
n, s = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

# 2등분하여 합을 처리
left = nums[:len(nums) // 2]
right = nums[len(nums) // 2:]
leftsum = []
for i in range(len(left) + 1):
    for j in combinations(left, i):
        leftsum.append(sum(j))
leftsum.sort()
rightsum = []
for i in range(len(right) + 1):
    for j in combinations(right, i):
        rightsum.append(sum(j))
rightsum.sort()

# 투포인터로 값 처리
count = 0
i, j = 0, len(rightsum) - 1
while i < len(leftsum) and j >= 0:
    temp = leftsum[i] + rightsum[j]
    
    if temp > s:
        j -= 1
    elif temp < s:
        i += 1
    else:
        # 같은 것 한 번에 처리
        bi, bj = i, j
        isame, jsame = 0, 0
        while i < len(leftsum) and leftsum[bi] == leftsum[i]:
            isame += 1
            i += 1
        while j >= 0 and rightsum[bj] == rightsum[j]:
            jsame += 1
            j -= 1
        
        count += isame * jsame

# 결과 출력 
print(count - 1 if s == 0 else count)
