n = int(input())

count = 0
for _ in range(n):
    line = input()
    
    check = line[0]
    bag = set()
    flag = True
    for i in line:
        if i != check and i in bag:
            flag = False
            break
        else:
            bag.add(i)
            check = i
    
    if flag:
        count += 1

print(count)
