import sys
input = sys.stdin.readline

# 파싱
n = input().rstrip()

temp = n[0]
count = 0
for i in n[1:]:
    if temp != i:
        count += 1
        temp = i

print((count + 1) // 2)
