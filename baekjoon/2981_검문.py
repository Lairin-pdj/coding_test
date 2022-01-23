from math import gcd
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = [int(input()) for _ in range(n)]

# 최대 공약수
temp = abs(nums[0] - nums[1])
for i in range(1, n - 1):
    temp = gcd(temp, abs(nums[i] - nums[i + 1]))

# 약수 출력
answer = set([temp])
for i in range(2, int(temp ** 0.5) + 1):
    if temp % i == 0:
        answer.add(i)
        answer.add(temp // i)
answer = list(answer)
answer.sort()
print(*answer)
