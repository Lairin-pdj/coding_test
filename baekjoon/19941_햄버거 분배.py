import sys
input = sys.stdin.readline

# 파싱
n, k = map(int, input().split(" "))
table = input().rstrip()

# 좌표 체크
pset = []
hset = []
for i, x in enumerate(table):
    if x == "H":
        hset.append(i)
    else:
        pset.append(i)

# 그리드
p, h = 0, 0
count = 0
while p < len(pset) and h < len(hset):
    if pset[p] - k <= hset[h] <= pset[p] + k:
        count += 1
        p += 1
        h += 1
    else:
        if pset[p] > hset[h]:
            h += 1
        else:
            p += 1

# 결과 출력
print(count)
