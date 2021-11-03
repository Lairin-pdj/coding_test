import sys
input = sys.stdin.readline

def gearRotate(i, d, updown):
    # 회전 시키기전에 극이 맞는 주변 바퀴 회전 신호 전달
    if updown != -1 and i + 1 < 5 and int(gear[i - 1][2]) + int(gear[i][6]) == 1:
        if d == -1:
            gearRotate(i + 1, 1, 1)
        elif d == 1:
            gearRotate(i + 1, -1, 1)
    
    if updown != 1 and i - 1 > 0 and int(gear[i - 1][6]) + int(gear[i - 2][2]) == 1:
        if d == -1:
            gearRotate(i - 1, 1, -1)
        elif d == 1:
            gearRotate(i - 1, -1, -1)
    
    
    # 방향에 맞게 회전
    if d == -1:
        gear[i - 1] = gear[i - 1][1:] + gear[i - 1][0]
    elif d == 1:
        gear[i - 1] = gear[i - 1][-1] + gear[i - 1][:-1]
        
        
# 파싱
gear = []
for _ in range(4):
    gear.append(input().rstrip())
    
n = int(input())

# 쿼리 파싱 및 처리
for _ in range(n):
    i, d = map(int, input().split(" "))
    gearRotate(i, d, 0)

# 결과 출력
print(int(gear[0][0]) + int(gear[1][0]) * 2 + int(gear[2][0]) * 4 + int(gear[3][0]) * 8)
