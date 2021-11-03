def check(num):
    temp = str(num)
    # 2자리 수 이하는 무조건 한수
    if len(temp) < 3:
        return True
    
    # 처음 차이를 기록
    diff = int(temp[0]) - int(temp[1])
    
    # 차이와 다른지 체크 
    for a, b in zip(temp[1:-1], temp[2:]):
        if int(a) - int(b) != diff:
            return False
    
    # 모두 같으면 True 반환
    return True
    

n = int(input())

# 1 부터 n까지 체크
count = 0
for i in range(1, n + 1):
    if check(i):
        count += 1
    
print(count)
