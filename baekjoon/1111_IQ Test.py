from collections import defaultdict
import sys
input = sys.stdin.readline
    
# 파싱
n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print("A")
elif n == 2:
    if nums[0] != nums[1]:
        print("A")
    else:
        print(nums[1])
else:
    # 계산하여 적용
    if nums[1] == nums[0]:
        a = 0
        b = nums[1]
    else:
        a = (nums[2] - nums[1]) // (nums[1] - nums[0])
        b = nums[1] - (nums[0] * a)
    
    # 체크 진행
    flag = False
    for i in range(1, n - 1):
        if nums[i + 1] != nums[i] * a + b:
            flag = True
            break
    
    if flag:
        print("B")
    else:
        print(nums[-1] * a + b)
