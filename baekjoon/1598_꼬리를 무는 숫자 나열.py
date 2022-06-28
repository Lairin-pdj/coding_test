import sys
input = sys.stdin.readline

# 파싱
a, b = map(int, input().split())
a -= 1
b -= 1

# 계산
ax, ay = a // 4, a % 4
bx, by = b // 4, b % 4

# 결과 출력
print(abs(ax - bx) + abs(ay - by))
