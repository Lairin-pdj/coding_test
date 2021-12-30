import sys
input = sys.stdin.readline

# 파싱
n, m = input().split()

# 자리 비교
count = 0
if len(n) == len(m):
    if n[0] == m[0]:
        for a, b in zip(n, m):
            if a == b:
                if a == "8":
                    count += 1
            else:
                break

# 결과 출력
print(count)
