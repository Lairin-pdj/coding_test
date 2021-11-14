import sys
input = sys.stdin.readline

# 파싱
n = int(input())
s = set()
for _ in range(n):
    query = input().rstrip().split()
    
    if query[0] == "add":
        s.add(query[1])
    elif query[0] == "remove":
        if query[1] in s:
            s.remove(query[1])
    elif query[0] == "check":
        if query[1] in s:
            print(1)
        else:
            print(0)
    elif query[0] == "toggle":
        if query[1] in s:
            s.remove(query[1])
        else:
            s.add(query[1])
    elif query[0] == "all":
        s = set([str(i) for i in range(1, 21)])
    else:
        s = set()
