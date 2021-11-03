from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split(" ")))

# 연산자들 파싱
openum = list(map(int, input().split(" ")))
opes = []
for i, ope in zip(openum, ["+", "-", "*", "%"]):
    for _ in range(i):
        opes.append(ope)
        
# 최대 최소 변수
high = -1000000000
low = 1000000000

# 모든 경우의 수 계산
for order in permutations(opes, n - 1):
    # 주어진 순서에 맞게 연산 진행
    temp = nums[0]
    for i, ope in enumerate(order):
        if ope == "+":
            temp += nums[i + 1]
        elif ope == "-":
            temp -= nums[i + 1]
        elif ope == "*":
            temp *= nums[i + 1]
        elif ope == "%":
            temp = int(temp / nums[i + 1])
            
    # 최대 최소 비교
    high = max(high, temp)
    low = min(low, temp)

# 결과값 출력
print(high)
print(low)
