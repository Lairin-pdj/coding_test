n = int(input())

count = 0
temp = n
while True:
    # 같아진 경우 탈출 
    if count != 0 and temp == n:
        print(count)
        break
    
    # 새로운 수 만들기
    a = temp // 10
    b = temp % 10
    c = a + b
    
    temp = b * 10 + c % 10
    
    count += 1
