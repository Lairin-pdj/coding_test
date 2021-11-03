import sys
input = sys.stdin.readline

stack = []
n = int(input())

for _ in range(n):
    ope = input().rstrip().split(" ")
    
    if ope[0] == "push":
        stack.append(ope[1])
        
    elif ope[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
            
    elif ope[0] == "size":
        print(len(stack))
        
    elif ope[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
            
    elif ope[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
