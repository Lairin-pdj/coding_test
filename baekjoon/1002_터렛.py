n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(" "))
    
    
    # 거리 계산
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    # 두 원이 같은 경우
    if dist == 0 and r1 == r2:
        print(-1)
        continue
    
    # 두 원이 만나지 않는 경우 
    # 한 원이 다른 원 안에 들어가 있거나 반지름의 합이 거리보다 작은 경우
    if r1 + r2 < dist:
        print(0)
        continue
    
    if r2 > dist and dist + r1 < r2:
        print(0)
        continue
    
    if r1 > dist and dist + r2 < r1:
        print(0)
        continue
    
    # 두 원이 한 점에서 만나는 경우
    # 반지름의 합이 거리와 같거나 다른 원 안쪽에서 한 점과 붙을 경우
    if r1 + r2 == dist or dist + r1 == r2 or dist + r2 == r1:
        print(1)
        continue
    
    # 두 원이 두 점에서 만나는 경우
    # 위 사항들이 전부 아닌 경우
    print(2)
