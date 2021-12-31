import sys
input = sys.stdin.readline

# 파싱
a, b = map(int, input().split())

# 에라스토테네스의 체를 이용한 소수 체크
prime = [0]
check = [False, False] + [True for _ in range(b - 1)]
for i in range(2, b + 1):
    if check[i]:
        prime.append(i)
        for j in range(i * 2, b + 1, i):
            check[j] = False

# dp
dp = [0 for _ in range(b + 1)]
for i in range(1, b + 1):
    if check[i]:
        dp[i] = 1
for i in range(2, b + 1):
    for j in range(2, b + 1):
        if i * j > b:
            break
        elif check[j]:
            dp[i * j] = dp[i] + 1

# 언더 프라임 체크
count = 0
for i in range(a, b + 1):
    if check[dp[i]]:
        count += 1

# 결과 출력
print(count)
