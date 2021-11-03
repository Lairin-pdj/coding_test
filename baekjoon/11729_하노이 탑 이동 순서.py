def hanoi(start, temp, end, n):
    if n == 1:
        print(start, end)
    else:
        hanoi(start, end, temp, n - 1)
        print(start, end)
        hanoi(temp, start, end, n - 1)

n = int(input())
print((2 ** n) - 1)
hanoi(1, 2, 3, n)
