import sys
input = sys.stdin.readline

# 파싱
a = int(input().rstrip())
n = int(input().rstrip())

# 가장자리 체크
if a in (1, 5):
    n *= 2

# 결과 출력
# 짝수, 홀수를 통한 위치 체크
print(n * 4 + (a - 1) if n % 2 == 0 else n * 4 + (5 - a))
