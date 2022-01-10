import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())

# 역체크
count = 1
while n < m:
    if str(m)[-1] == "1":
        m = int(str(m)[:-1])
        count += 1
    else:
        if m % 2 == 0:
            m = m // 2
            count += 1
        else:
            break

# 결과 출력
if n == m:
    print(count)
else:
    print(-1)
