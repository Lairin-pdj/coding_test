import sys
input = sys.stdin.readline

# 파싱
t = int(input())

for _ in range(t):
    n, m = map(int, input().split(" "))
    temp = n
    count = 0
    while temp > 0:
        count += 1
        temp = temp // 2
    print(count + m)
