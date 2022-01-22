from math import gcd
import sys
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    print((a * b) // gcd(a, b))
