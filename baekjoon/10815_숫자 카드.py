import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = set(map(int, input().split()))
m = int(input())
test = list(map(int, input().split()))

# 체크
for i in test:
    if i in nums:
        print("1", end = " ")
    else:
        print("0", end = " ")
