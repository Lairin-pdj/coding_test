a, b, c = map(int, input().split(" "))

# 만들수록 손해일 경우
if c - b <= 0:
    print(-1)
else:
    print((a // (c - b)) + 1)
