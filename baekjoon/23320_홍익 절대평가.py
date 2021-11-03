import sys
input = sys.stdin.readline

# 파싱
n = int(input())

scores = list(map(int, input().split(" ")))

x, y = map(int, input().split(" "))

count = 0
for i in scores:
    if i >= y:
        count += 1

print(int(n * x / 100), end = " ")
print(count)
