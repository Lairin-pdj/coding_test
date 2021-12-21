from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())

# 해싱
dic = defaultdict(str)
for _ in range(n):
    link, pw = input().rstrip().split()
    dic[link] = pw

# 결과 출력
for _ in range(m):
    temp = input().rstrip()
    print(dic[temp])
