def solution(n, lost, reserve):
    # 0번째를 체크에서 벗어나게 하기 위해 3으로 초기화
    clothes = [3] + [1] * n
    
    # 읽어버린 사람 체크
    for i in lost:
        clothes[i] -= 1
        
    # 여벌옷 체크
    for i in reserve:
        clothes[i] += 1

    for i, num in enumerate(clothes):
        # 0일 경우 앞 뒤 사람 여벌옷 여부 체크
        if num == 0:
            if i - 1 > 0 and clothes[i - 1] == 2:
                clothes[i - 1] -= 1
                clothes[i] += 1
            elif i + 1 <= n and clothes[i + 1] == 2:
                clothes[i + 1] -= 1
                clothes[i] += 1
                
    return clothes.count(1) + clothes.count(2)
