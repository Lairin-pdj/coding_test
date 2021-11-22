import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())

# 최소값 체크
sets = 1000
each = 1000
for _ in range(m):
    a, b = map(int, input().split())
    sets = min(sets, a)
    each = min(each, b)

# 계산 및 결과출력
sn = n // 6
en = n % 6
if sets > each * 6:
    print(n * each)
elif sets <= each:
    if en == 0:
        print(sn * sets)
    else:
        print((sn + 1) * sets)
else:
    if en == 0:
        print(sn * sets)
    else:
        if en * each > sets:
            print((sn + 1) * sets)
        else:
            print(sn * sets + en * each)
