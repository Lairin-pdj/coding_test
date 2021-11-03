from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split(" "))
ices = list(map(int, input().split(" ")))

# 해싱
dic = defaultdict(list)
for i, ice in enumerate(ices):
    dic[ice].append(i + 1)

# 정렬
temp = list(dic.keys())
temp.sort(reverse = True)
for key in temp:
    dic[key].sort()

# 아이스크림 먹기
isrev = False
count = 0
for key in temp:
    # 지정된 수량을 다먹은 경우 탈출
    if count >= m:
        break
    
    # 수량 체크
    many = len(dic[key])
    
    # 가능한 양 만큼 섭취
    for _ in range(min(len(dic[key]), m - count)):
        # 역전 상태 체크 후 섭취
        if isrev:
            print(dic[key].pop())
        else:
            print(dic[key].pop(0))
        
        # 민초면 역전 체크
        if key % 7 == 0:
            if isrev:
                isrev = False
            else:
                isrev = True
    
    # 섭취한 양 기록
    count += many
