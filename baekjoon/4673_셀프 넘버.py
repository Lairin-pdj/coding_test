# 셀프 넘버 함수
def d(n):
    temp = n
    
    while n > 0:
        temp += n % 10
        n = n // 10
    
    return temp

# 최대 숫자
goal = 10000
# 확인용 체크 숫자표
selfnum = [True] * (goal + 1)

for i in range(1, goal + 1):
    # 셀프 넘버 생성
    temp = d(i)
    
    # 범위 안이면 체크
    if temp <= goal:
        selfnum[temp] = False
    
    # 생성자가 없으면 풀력
    if selfnum[i]:
        print(i)
