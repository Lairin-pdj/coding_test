import sys
input = sys.stdin.readline

def check(line):
    stack = []
    
    for i in line:
        if i in ("[", "("):
            stack.append(i)
        elif i in ("]", ")"):
            if stack:
                if stack[-1] == "[" and i == "]":
                    stack.pop()
                elif stack[-1] == "(" and i == ")":
                    stack.pop()
                else:
                    return False
            else:
                return False
    
    if stack:
        return False
    else:
        return True


while True:
    line = input().rstrip()
    
    if line == ".":
        break
    
    if check(line):
        print("yes")
    else:
        print("no")
