import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())

# 결과출력
print(n // m)
print(n % m)
