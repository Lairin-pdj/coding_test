import sys
input = sys.stdin.readline

# 파싱
na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

temp = list(a - b)
temp.sort()
print(len(temp))
print(*temp)
