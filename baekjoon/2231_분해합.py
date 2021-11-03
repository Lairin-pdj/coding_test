def disum(num):
    return num + sum(list(map(int, str(num))))

n = int(input())
flag = True

for i in range(1, n):
    if disum(i) == n:
        print(i)
        flag = False
        break
    
if flag:
    print(0)
