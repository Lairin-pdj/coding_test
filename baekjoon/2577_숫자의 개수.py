a = int(input())
b = int(input())
c = int(input())

count = [0] * 10

for i in str(a * b * c):
    count[int(i)] += 1
    
for i in count:
    print(i)
