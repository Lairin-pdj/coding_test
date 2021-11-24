import sys
input = sys.stdin.readline

# 파싱
n, a, b = map(int, input().split())

count = 0
while a != b:
    count += 1
    a = (a + 1) // 2
    b = (b + 1) // 2
    
print(count)
