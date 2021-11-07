import sys
input = sys.stdin.readline

def check(line):
    stack = []
    
    for i in line:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    else:
        return True

# 파싱
t = int(input())

for _ in range(t):
    line = input().rstrip()
    
    if check(line):
        print("YES")
    else:
        print("NO")
