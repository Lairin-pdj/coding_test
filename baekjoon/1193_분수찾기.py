n = int(input())

count = 1
while (count * (count + 1)) // 2 < n:
    count += 1

total = count + 1
end = (count * (count + 1)) // 2

# 짝수번째 줄 (아래로)
if count % 2 == 0:
    print("{}/{}".format(total - (end - n + 1), end - n + 1))
# 홀수번째 줄 (위로)
else:
    print("{}/{}".format(end - n + 1, total - (end - n + 1)))
