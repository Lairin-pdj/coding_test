import sys
input = sys.stdin.readline

# 파싱
n = int(input())
s = [0 for _ in range(21)]
for _ in range(n):
    query = input().rstrip().split()
    
    if query[0] == "add":
        s[int(query[1])] = 1
    elif query[0] == "remove":
        s[int(query[1])] = 0
    elif query[0] == "check":
        print(s[int(query[1])])
    elif query[0] == "toggle":
        if s[int(query[1])] == 1:
            s[int(query[1])] = 0
        else:
            s[int(query[1])] = 1
    elif query[0] == "all":
        s = [1 for _ in range(21)]
    else:
        s = [0 for _ in range(21)]
