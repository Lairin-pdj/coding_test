import sys
input = sys.stdin.readline

# 파싱
while True:
    string = input().rstrip()
    
    if string == "0":
        break
    
    flag = True
    for a, b in zip(string[:len(string) // 2], string[::-1][:len(string) // 2]):
        if a != b:
            flag = False
            break
    
    if flag:
        print("yes")
    else:
        print("no")
