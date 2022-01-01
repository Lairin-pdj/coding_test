from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
s = input().rstrip()
dic = defaultdict(int)
for i in s:
    dic[i] += 1

# 홀수 갯수 체크
count = 0

for i in dic.values():
    if i % 2 == 1:
        count += 1

# 홀수 갯수에 따라 결과 출력
if count > 1:
    print("I'm Sorry Hansoo")
else:
    # 팰린드롭 제작
    temp = list(dic.items())
    temp.sort()
    answer = ""
    mid = ""
    for l, n in temp:
        if n % 2 == 0:
            answer += (l * (n // 2))
        else:
            answer += (l * ((n - 1) // 2))
            mid = l
    print(answer + mid + answer[::-1])
