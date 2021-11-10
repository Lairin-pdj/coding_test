import sys 
input = sys.stdin.readline

# 파싱
n = int(input())

# 에라스토테네스의 체를 이용한 소수 체크
prime = [0]
check = [False, False] + [True for _ in range(n - 1)]
for i in range(2, n + 1):
    if check[i]:
        prime.append(i)
        for j in range(i * 2, n + 1, i):
            check[j] = False

# 누적합을 이용하여 사이 덧셈 이용
for i in range(1, len(prime)):
    prime[i] += prime[i - 1]

# 투 포인터를 이용한 갯수 체크
count = 0
i, j = 0, 1
while j < len(prime):
    temp = prime[j] - prime[i]
    
    if temp == n:
        count += 1
    
    if temp < n:
        j += 1
    else:
        i += 1

# 결과 출력
print(count)
