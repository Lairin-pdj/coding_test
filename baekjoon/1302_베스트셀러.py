from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    temp = input().rstrip()
    dic[temp] += 1

answer = list(dic.items())
answer.sort(key = lambda x : (-x[1], x[0]))
print(answer[0][0])
