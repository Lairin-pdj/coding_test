import sys
input = sys.stdin.readline

# 파싱 및 출력
print(bin(sum(map(lambda x : int(x, 2), input().split())))[2:])
