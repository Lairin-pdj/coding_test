import sys
input = sys.stdin.readline

# 파싱
n = int(input())
s = [input().rstrip() for _ in range(n)]

# zip check
answer = ""
for line in list(zip(*s)):
    flag = True
    for i in range(1, len(line)):
        if line[0] != line[i]:
            flag = False
            break
    
    if flag:
        answer += line[0]
    else:
        answer += "?"

# 결과 출력
print(answer)
