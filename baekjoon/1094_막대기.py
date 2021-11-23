import sys
input = sys.stdin.readline

# 파싱
n = int(input())

print(sum(map(int, bin(n)[2:])))
