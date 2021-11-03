import sys
input = sys.stdin.readline

# 파싱
n = int(input())

for _ in range(n):
    i, string = input().rstrip().split(" ")
    i = int(i)
    print(string[:i - 1] + string[i:])
