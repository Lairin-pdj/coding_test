import sys
input = sys.stdin.readline

# 파싱
a, b, c = map(int, input().split())

# 3개가 같은 경우
if a == b == c:
    print(10000 + a * 1000)
# 2개가 같은 경우
elif a == b or b == c or c == a:
    if a == b:
        print(1000 + a * 100)
    elif b == c:
        print(1000 + b * 100)
    else:
        print(1000 + c * 100)
# 모두 다른 경우
else:
    print(max((a, b, c)) * 100)
