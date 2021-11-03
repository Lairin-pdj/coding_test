h, m = map(int, input().split(" "))

temp = h * 60 + m - 45

if temp < 0:
    temp += 24 * 60

print(temp // 60, temp % 60)
