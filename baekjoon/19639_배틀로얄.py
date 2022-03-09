import sys
input = sys.stdin.readline

# 파싱
x, y, m = map(int, input().split())
mans = []
for _ in range(x):
    mans.append(int(input()))
potion = []
for _ in range(y):
    potion.append(int(input()))
    

# 불가능한 경우
if sum(potion) + m <= sum(mans):
    print(0)
# 가능한 경우
else:
    kill = 0
    drink = 0
    
    while kill < x:
        # 죽일 수 있는 경우
        if m > mans[kill]:
            m -= mans[kill]
            kill += 1
            print(-kill)
        # 죽일 수 없는 경우
        else:
            m += potion[drink]
            drink += 1
            print(drink)
    
    # 남은 물약먹기
    while drink < y:
        drink += 1
        print(drink)
