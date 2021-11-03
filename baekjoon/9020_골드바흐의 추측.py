n = int(input())

cases = []
for _ in range(n):
    cases.append(int(input()))
high = max(cases)

# 에라스토테네스의 체
check = [False, False] + [True] * (high - 1)

for i in range(2, high + 1):
    if check[i]:
        for j in range(2 * i, high + 1, i):
            check[j] = False

for i in cases:
    for j in range((i // 2), 1, -1):
        if check[j] and check[i - j]:
            print(j, i - j)
            break
