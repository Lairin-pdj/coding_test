import sys
input = sys.stdin.readline

# 파싱
n = input().rstrip()
check = [0 for _ in range(10)]

# 숫자체크
for i in n:
    temp = int(i)
    check[temp] += 1

check[6] += check[9]
check[6] = (check[6] + 1) // 2

# 정답 출력
print(max(check[:-1]))
