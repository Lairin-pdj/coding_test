from itertools import combinations

def solution(orders, course):
    answer = []
    
    for i in course:
        dic = {}                                    # 사전과 조합을 이용
        for j in orders:                            
            if len(j) >= i:
                for k in combinations(j, i):
                    k = list(k)
                    k.sort()
                    temp = ''.join(k)
                    if temp in dic:                 # 각 개수의 조합의 빈도 수 체크
                        dic[temp] = dic[temp] + 1
                    else:
                        dic[temp] = 1
                        
        if len(dic) != 0:                           # 제일 잘 팔릴 세트 체크 
            temp = max(dic.values())
        else:
            temp = 0
            
        if temp > 1:                                # 배열로 변환
            for i in dic.keys():
                if dic[i] == temp:
                    answer.append(i)
        
    answer.sort()                                   # 정렬 후 반환
    
    return answer
