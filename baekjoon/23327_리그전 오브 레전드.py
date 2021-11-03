import sys
input = sys.stdin.readline

# 파싱
n, q = map(int, input().split(" "))
teams = list(map(int, input().split(" ")))

# (a + b + c + ...)
sumA = [0]
# (a^2 + b^2 + c^2 + ...)
sumA2 = [0]

for funny in teams:
    sumA.append(sumA[-1] + funny)
    sumA2.append(sumA2[-1] + funny ** 2)

# funny = ab + bc + ca = ((a + b + c)^2 - (a^2 + b^2 + c^2)) / 2
for _ in range(q):
    l, r = map(int, input().split(" "))
    
    a1 = (sumA[r] - sumA[l - 1])
    a2 = (sumA2[r] - sumA2[l - 1])
    print((a1 ** 2 - a2) // 2 )
