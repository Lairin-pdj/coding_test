def solution(clothes):
    dic = {}
    
    for i in clothes:                   # 사전을 이용하여 종류별로 옷 갯수를 파악
        if not i[1] in dic:
            dic[i[1]] = 1
        else:
            dic[i[1]] = dic[i[1]] + 1
    
    temp = 1
    for i in dic.values():              # 종류별 옷 갯수만큼 선택 조합으로 결과 도출
        temp *= (i + 1)
    
    return temp - 1                     # 하나도 안 입는 경우 제외 후 반환
