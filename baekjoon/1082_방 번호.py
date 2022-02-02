import sys
input = sys.stdin.readline

# 파싱
n = int(input())
p = list(map(int, input().split()))
m = int(input())

# 길이 체크
if n != 1:
    low09 = p.index(min(p))
    low19 = p.index(min(p[1:]))
    
    # 최장길이 긴 번호 제작
    answer = [low19]
    cost = p[low19]
    
    # 숫자하나만 살 수 있는 경우 중 특수 케이스 처리
    if cost > m:
        answer[0] = low09
        cost = p[low09]
    
    # 제일 싼 숫자 돈이 되는 대로 붙이기
    while cost + p[low09] <= m:
        answer += [low09]
        cost += p[low09]
    
    # 최대 수치로 변화
    for i in range(len(answer)):
        targetcost = p[answer[i]]
        for j in range(n - 1, 0, -1):
            changecost = p[j] - targetcost
            if cost + changecost <= m:
                answer[i] = j
                cost += changecost
                break
        
    # 결과 출력
    if max(answer) == 0:
        print(0)
    else:
        print("".join(map(str, answer)))
else:
    print(0)
