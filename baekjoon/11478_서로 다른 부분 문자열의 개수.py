import sys
input = sys.stdin.readline

# 파싱
s = input().rstrip()

# 갯수 확인
check = set()
for i in range(1, len(s) + 1):
    for j in range(0, len(s) - i + 1):
        check.add(s[j:j + i])

# 결과 출력
print(len(check))
