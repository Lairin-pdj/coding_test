from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
nums = list(map(int, input().split()))
m = int(input())
querys = list(map(int, input().split()))

# 해싱
dic = defaultdict(int)
for i in nums:
    dic[i] += 1

# 정답출력
for i in querys:
    print(dic[i], end = " ")
