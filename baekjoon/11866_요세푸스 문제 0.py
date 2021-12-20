from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n, k = map(int, input().split())

mans = deque([i for i in range(1, n + 1)])
mans.rotate(-k + 1)

print("<", end = "")
while mans:
    if len(mans) != 1:
        print(mans.popleft(), end = ", ")
    else:
        print(mans.popleft(), end = ">")
    mans.rotate(-k + 1)
