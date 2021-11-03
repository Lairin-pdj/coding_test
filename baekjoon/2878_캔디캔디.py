from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
m, n = map(int, input().split(" "))

# 해싱 및 총갯수 체크
dic = defaultdict(int)
total = 0
for _ in range(n):
    candy = int(input())
    dic[candy] += 1
    total += candy

temp = list(dic.keys())
temp.sort()

# 작은 순서부터 체크
dist = total - m
remain_human = n
remain_void = dist
count = []
# 제곱은 모든 수가 전체적으로 작게해야함
# 모든 사람에게 모자란 사탕공간을 분배하는 방식
for i in temp:
    if remain_void // remain_human >= i:
        if i in dic:
            count.append([i, dic[i]])
            remain_human -= dic[i]
            remain_void -= dic[i] * i
    else:
        k = remain_void // remain_human
        count.append([k + 1, remain_void % remain_human])
        count.append([k, remain_human - (remain_void % remain_human)])
        break

# 제곱의 합 계산
answer = 0
for i, nums in count:
    answer += i * i * nums
    
# 출력
print(answer & ( (1 << 64) - 1))
