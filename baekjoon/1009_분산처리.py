import sys
input = sys.stdin.readline

def gob(a, b):
    if b == 1:
        return a % 10
    else:
        if b % 2 == 1:
            return ((gob(a, b // 2) ** 2) * a) % 10
        else:
            return (gob(a, b // 2) ** 2) % 10

# 파싱
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    temp = gob(a, b)
    print(temp if temp != 0 else 10)
