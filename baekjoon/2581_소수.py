m = int(input())
n = int(input())

# 에라스토테네스의 체
check = [False, False] + [True] * (n - 1)

for i in range(2, n + 1):
    if check[i]:
        for j in range(2 * i, n + 1, i):
            check[j] = False

# 소수 체크
primes = []
for i in range(m, n + 1):
    if check[i]:
        primes.append(i)


if len(primes):
    print(sum(primes))
    print(primes[0])
else:
    print(-1)
