import sys
input = sys.stdin.readline

temp = []
k = int(input())
for _ in range(k):
    num = int(input())
    
    if num == 0:
        temp.pop()
    else:
        temp.append(num)
        
print(sum(temp))
