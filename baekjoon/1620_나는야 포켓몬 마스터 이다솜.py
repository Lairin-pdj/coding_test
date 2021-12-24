from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())

# 해싱
name = defaultdict(str)
num = defaultdict(int)
for i in range(1, n + 1):
    temp = input().rstrip()
    name[i] = temp
    num[temp] = i

# 결과 출력
for _ in range(m):
    temp = input().rstrip()
    if temp.isdigit():
        print(name[int(temp)])
    else:
        print(num[temp])
