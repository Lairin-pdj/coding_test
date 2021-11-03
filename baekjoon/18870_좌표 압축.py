import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
nums = list(map(int, input().split(" ")))

temp = list(set(nums))
temp.sort()

dic = defaultdict(int)

for i, a in enumerate(temp):
    dic[a] = i

for i in nums:
    print(dic[i], end = " ")
