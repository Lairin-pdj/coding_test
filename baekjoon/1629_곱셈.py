import sys
input = sys.stdin.readline

def power(a, b):
    # 제곱 단위를 분해하여 계산
    if b == 1:
        return a
    elif b % 2 == 0:
        temp = power(a, b // 2)
        return (temp ** 2) % c
    else:
        temp = power(a, b // 2)
        return ((temp ** 2) * a) % c

# 파싱
a, b, c = map(int, input().split())

# 결과 출력
print(power(a, b) % c)
