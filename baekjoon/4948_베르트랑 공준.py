cases = []
while True:
    temp = int(input())
    if temp == 0:
        break
    else:
        cases.append(temp)
high = max(cases) * 2

# 에라스토테네스의 체
check = [False, False] + [True] * (high - 1)

for i in range(2, high + 1):
    if check[i]:
        for j in range(2 * i, high + 1, i):
            check[j] = False

for i in cases:
    count = 0
    
    for j in range(i + 1, (2 * i) + 1):
        if check[j]:
            count += 1
            
    print(count)
