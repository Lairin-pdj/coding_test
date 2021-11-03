m, n = map(int, input().split(" "))
high = n

# 에라스토테네스의 체
check = [False, False] + [True] * (high - 1)

for i in range(2, high + 1):
    if check[i]:
        for j in range(2 * i, high + 1, i):
            check[j] = False

for i in range(m, n + 1):
    if check[i]:
        print(i)
