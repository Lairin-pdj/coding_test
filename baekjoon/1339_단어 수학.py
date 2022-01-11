from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    s = input().rstrip()[::-1]
    for i in range(len(s)):
        dic[s[i]] += 10 ** i

# 숫자 배당 및 결과 계산
answer = 0
temp = 9
order = list(dic.items())
order.sort(key = lambda x : (-x[1]))
for a, b in order:
    answer += temp * b
    temp -= 1

# 정답 출력
print(answer)
