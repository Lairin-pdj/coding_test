import sys
input = sys.stdin.readline

# 파싱
n, k = map(int, input().split())

temp = 1
for i in range(n, n - k, -1):
    temp *= i
for i in range(1, k + 1):
    temp = temp // i
print(temp)
