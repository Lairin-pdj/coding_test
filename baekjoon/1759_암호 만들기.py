from itertools import combinations
import sys
input = sys.stdin.readline

# 파싱
l, c = map(int, input().split())
alpha = input().rstrip().split()
alpha.sort()

for temp in combinations(alpha, l):
    a, b = 0, 0
    for i in temp:
        if i in ("a", "e", "i", "o", "u"):
            a += 1
        else:
            b += 1
    
    if a >= 1 and b >= 2:
        print("".join(temp))
