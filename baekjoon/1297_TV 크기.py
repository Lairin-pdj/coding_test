import sys
input = sys.stdin.readline

# 파싱
d, h, w = map(int, input().split())

# 계산
ratio = d / ((h ** 2 + w ** 2) ** 0.5)

# 출력
print(int(ratio * h), int(ratio * w))
