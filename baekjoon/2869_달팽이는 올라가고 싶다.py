import math

a, b, v = map(int, input().split(" "))

day = math.ceil((v - a) / (a - b))

print(day + 1)
