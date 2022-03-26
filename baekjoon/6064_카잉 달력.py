import sys, math
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())

    top = (m * n) // math.gcd(m, n)
    start = x
    
    flag = False
    while start <= top:
        if start % n == y % n:
            flag = True
            break
        start += m
    
    if flag:
        print(start)
    else:
        print(-1)
