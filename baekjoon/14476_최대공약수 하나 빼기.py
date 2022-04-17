from math import gcd
import sys
input = sys.stdin.readline
    
# 파싱
n = int(input())
nums = list(map(int, input().split()))

# 공약수 누적
left, right = [nums[0]], [nums[-1]]
for i in range(1, n - 1):
    left.append(gcd(left[-1], nums[i]))
    right.append(gcd(right[-1], nums[n - i - 1]))
left.append(gcd(left[-1], nums[n - 1]))
right.append(gcd(right[-1], nums[0]))
right = right[::-1]

# 최대 체크
answer, target = 0, 0
for i in range(n):
    if i == 0:  
        temp = right[i + 1]
    elif i == n - 1:
        temp = left[i - 1]
    else:
        temp = gcd(left[i - 1], right[i + 1])
    
    if temp > answer:
        target = nums[i]
        if target % temp != 0:
            answer = temp

# 결과 출력
if answer == 0:
    print(-1)
else:
    print(answer, target)
