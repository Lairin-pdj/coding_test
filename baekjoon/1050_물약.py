from collections import defaultdict, deque
import sys, re
input = sys.stdin.readline

# 파싱
n, m = map(int, input().split())
price = defaultdict(int)
for _ in range(n):
    name, cost = input().split()
    cost = int(cost)
    price[name] = cost
    
# 수식 체크 
express = defaultdict(list)
sort = defaultdict(list)
count = defaultdict(int)
for _ in range(m):
    temp = input().rstrip()
    names = re.split("[^A-Z]", temp)
    names = [i for i in names if i]
    nums = re.split("[^0-9]", temp)
    nums = [i for i in nums if i]
    
    # 같은 물질에 여러 제작방법이 있는 경우를 체크하기 위해
    temp = []
    flag = True
    for i in range(len(nums)):
        if names[0] == names[i + 1]:
            flag = False
            break
        temp.append((names[i + 1], int(nums[i])))
    
    # 자기 자신을 재료로 하는 경우 제거
    if flag:
        express[names[0]].append(temp)
        
        # 위상정렬을 위한 정보 저장
        for i in range(len(nums)):
            sort[names[i + 1]].append(names[0])
            count[names[0]] += 1
            if names[i + 1] not in count:
                count[names[i + 1]] = 0

# 위상정렬
# 시작 가능 지점 체크 및 큐에 삽입
queue = deque()
for name in count.keys():
    if count[name] == 0:
        queue.append(name)

# 정점 진행
order = []
while queue:
    now = queue.popleft()
    order.append(now)
    
    # 가격 반영
    if now in express:
        can = False
        
        # 수식 별 체킹
        for ex in express[now]:
            temp = 0
            flag = True
            
            for mate, ea in ex:
                # 가격이 있는 경우
                if mate in price:
                    temp += price[mate] * ea
                # 가격이 없는 경우
                else:
                    flag = False
                    break
            
            # 최소값 갱신
            if flag:
                if now in price:
                    price[now] = min(price[now], temp)
                else:
                    price[now] = temp

    # 노드 체크
    for i in sort[now]:
        if count[i] == 1:
            queue.append(i)
        count[i] -= 1

# 사이클로 체크되지 않은 수식 추가
for _ in range(m):
    for name in express.keys():
        if name not in order:
            
            # 수식 별 확인
            for ex in express[name]:
                flag = True
                temp = 0
                
                for mate, ea in ex:
                    # 모든 재료에 가격이 존재하면 계산
                    if mate not in price:
                        flag = False
                        break
                    else:
                        temp += price[mate] * ea
                
                if flag:
                    if name in price:
                        price[name] = min(price[name], temp)
                    else:
                        price[name] = temp

# 결과 출력
if "LOVE" not in price:
    print(-1)
else:
    print(min(price["LOVE"], 1000000001))
