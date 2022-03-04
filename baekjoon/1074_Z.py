import sys
input = sys.stdin.readline

# 파싱
n, r, c = map(int, input().split())

# 2진수 1의 위치에 따른 숫자의 변화에 초첨
answer = 0

# r의 경우
temp = 1
for i in bin(r)[2:][::-1]:
    if i == "1":
        answer += 2 ** (temp * 2 - 1)
    temp += 1

# c의 경우
temp = 0
for i in bin(c)[2:][::-1]:
    if i == "1":
        answer += 2 ** (temp * 2)
    temp += 1

# 결과 출력
print(answer)
