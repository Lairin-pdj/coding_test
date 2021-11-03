n, x = map(int, input().split(" "))

nums = map(int, input().split(" "))

for num in nums:
    if num < x:
        print(num, end = " ")
