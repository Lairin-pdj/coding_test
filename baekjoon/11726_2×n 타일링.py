import sys
input = sys.stdin.readline

# 파싱
n = int(input())
count = [1 for _ in range(n + 1)]

# dp
for i in range(2, n + 1):
    count[i] = (count[i - 1] + count[i - 2]) % 10007

# 결과 출력
print(count[n])
