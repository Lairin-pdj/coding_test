import sys
input = sys.stdin.readline

# 파싱
line = input().rstrip()

# 체크
flag = True
for i in range(len(line) // 2, len(line)):
    
    # 짝수
    temp = len(line) - i
    if line[i - temp:i] == line[i:][::-1]:
        print(i * 2)
        flag = False
        break
    
    # 홀수
    temp = len(line) - i - 1
    if line[i - temp:i] == line[i + 1:][::-1]:
        print(i * 2 + 1)
        flag = False
        break

# 최악의 경우
if flag:
    print(len(line) * 2 - 1)
