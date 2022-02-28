import sys, bisect
input = sys.stdin.readline

# 파싱
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()

# 이분탐색을 이용한 nlogn LIS
lis = []
index = [-1 for _ in range(n)]
for i, (a, b) in enumerate(lines):
    idx = bisect.bisect_left(lis, b)
    if idx >= len(lis):
        lis.append(b)
    else:
        lis[idx] = b
    index[i] = idx

# 결과 출력
temp = len(lis) - 1
print(n - temp - 1)

answer = set()
for i in range(n - 1, -1, -1):
    if index[i] == temp:
        answer.add(lines[i][0])
        temp -= 1
for a, b in lines:
    if a not in answer:
        print(a)
