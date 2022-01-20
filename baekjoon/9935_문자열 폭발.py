import sys
input = sys.stdin.readline

# 파싱
s = list(input().rstrip())
n = list(input().rstrip())
answer = []

# 순서대로 체크
for c in s:
    answer.append(c)
    if c == n[-1] and answer[-len(n):] == n:
        del answer[-len(n):]

# 결과 출력
if answer:
    print("".join(answer))
else:
    print("FRULA")
