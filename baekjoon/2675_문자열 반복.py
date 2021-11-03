n = int(input())

for _ in range(n):
    count, string = input().split(" ")
    temp = ""
    for char in string:
        temp += char * int(count)
    
    print(temp)
