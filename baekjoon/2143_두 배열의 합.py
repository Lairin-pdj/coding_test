from collections import defaultdict
import sys 
input = sys.stdin.readline

# 파싱
t = int(input())
n = int(input())
an = [0] + list(map(int, input().split()))
m = int(input())
bm = [0] + list(map(int, input().split()))

# 누적합
for i in range(1, n + 1):
    an[i] += an[i - 1]
for i in range(1, m + 1):
    bm[i] += bm[i - 1]

# bm의 가능한 값 체크
dic = defaultdict(int)
for i in range(m):
    for j in range(i + 1, m + 1):
        dic[bm[j] - bm[i]] += 1

# 가능한 숫자 체킹
# an의 가능한 값
count = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        temp = an[j] - an[i]
        remain = t - temp
        
        # 해싱 값 반영
        count += dic[remain]

# 결과 출력
print(count)
