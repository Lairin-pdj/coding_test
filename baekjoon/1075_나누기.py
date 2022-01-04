import sys
input = sys.stdin.readline

# 파싱
n = int(input())
f = int(input())

# 00부터 체크
n = (n // 100) * 100
for i in range(100):
    if (n + i) % f == 0:
        # 결과 출력
        print(str(i).zfill(2))
        break
