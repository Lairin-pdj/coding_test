n = int(input())

count = 0
while 1 + (3 * count * (count + 1)) < n:
    count += 1

print(count + 1)
