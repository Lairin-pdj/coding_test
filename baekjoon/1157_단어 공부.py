from collections import defaultdict

line = input()
line = line.upper()

dic = defaultdict(int)
for char in line:
    dic[char] += 1
    
high = max(dic.values())
temp = []
for key in dic.keys():
    if dic[key] == high:
        temp.append(key)
        
if len(temp) == 1:
    print(temp[0])
else:
    print("?")
