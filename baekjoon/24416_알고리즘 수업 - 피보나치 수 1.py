import sys
input = sys.stdin.readline

# 파싱
n = int(input())

# dp
reccount = [0 for _ in range(n + 1)]
reccount[1] = 1
reccount[2] = 1
for i in range(3, n + 1):
    reccount[i] = reccount[i - 1] + reccount[i - 2]

# 결과 출력
print(reccount[n], n - 2)
