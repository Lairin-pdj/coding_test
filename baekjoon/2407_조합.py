import sys
input = sys.stdin.readline

def com(n, r):
    if r < 0 or n < r:
        return 0
    temp = 1
    for i in range(n, n - r, -1):
        temp *= i
    for i in range(1, r + 1):
        temp = temp // i
    return temp
    
# 파싱
n, m = map(int, input().split())

if n // 2 < m:
    m = n - m
    
print(com(n, m))
