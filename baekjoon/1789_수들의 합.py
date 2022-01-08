import sys
input = sys.stdin.readline

# 파싱
n = int(input())

t = int((2 * n) ** 0.5) - 1
while (t * (t + 1)) // 2 <= n:
    t += 1

# 결과 출력
print(t - 1)
