import sys
input = sys.stdin.readline

# 파싱
h, m = map(int, input().split())
time = int(input())

total = 60 * h + m + time
print((total // 60) % 24, total % 60)
