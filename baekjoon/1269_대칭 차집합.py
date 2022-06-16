import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

# 결과 출력
print(len(a) + len(b) - 2 * len(a & b))
