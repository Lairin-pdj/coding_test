import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
answer = a * b

while b > 0:
    print((b % 10) * a)
    b = b // 10

print(answer)
