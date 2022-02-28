import sys, bisect
input = sys.stdin.readline

# 파싱
n = int(input())
lines = list(map(int, input().split()))

# 이분탐색을 이용한 nlogn LIS
lis = []
index = [-1 for _ in range(n)]
for i, x in enumerate(lines):
    idx = bisect.bisect_left(lis, x)
    if idx >= len(lis):
        lis.append(x)
    else:
        lis[idx] = x
    index[i] = idx

# 결과 출력
temp = len(lis) - 1
answer = []
for i in range(n - 1, -1, -1):
    if index[i] == temp:
        answer.append(lines[i])
        temp -= 1
print(len(answer))
print(*answer[::-1])
