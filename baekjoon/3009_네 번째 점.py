a, b = map(int, input().split(" "))
c, d = map(int, input().split(" "))
e, f = map(int, input().split(" "))

if a == c:
    print(e, end = " ")
else:
    if a == e:
        print(c, end = " ")
    else:
        print(a, end = " ")
        
if b == d:
    print(f)
else:
    if b == f:
        print(d)
    else:
        print(b)
