from bisect import bisect_left
from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
s = list(map(int, input().split()))
l = list(map(int, input().split()))

# 순서 변환 
dic = defaultdict(int)
for i in range(n):
    dic[l[i]] = i
for i in range(n):
    s[i] = dic[s[i]]

# lis
on = []
history = [-1 for _ in range(n)]
for i, x in enumerate(s):
    idx = bisect_left(on, x)
    if idx < len(on):
        on[idx] = x
    else:
        on.append(x)
    history[i] = idx

# 역추적
temp = len(on) - 1
answer = []
for i in range(n - 1, -1, -1):
    if history[i] == temp:
        answer.append(l[s[i]])
        temp -= 1

# 정렬
answer.sort()

# 결과 출력
print(len(answer))
print(*answer)
