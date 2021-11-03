from itertools import combinations

def compare(a, b):
    if a[0] > b[0] and a[1] > b[1]:
        return 1
    
    if a[0] < b[0] and a[1] < b[1]:
        return 2
    
    return 0
        

n = int(input())

mans = []

for _ in range(n):
    x, y = map(int, input().split(" "))
    mans.append([x, y, 1])
    
for a, b in combinations(mans, 2):
    temp = compare(a, b)
    
    if temp == 1:
        b[2] += 1
    elif temp == 2:
        a[2] += 1
        
for i in mans:
    print(i[2], end = " ")
