from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    dic = defaultdict(list)
    
    for i, (genre, num) in enumerate(zip(genres, plays)):                   # 주어진 정보를 사전으로 취합
        dic[genre].append([int(num), i])
    
    check = []
    for key in dic.keys():                                                  # 최대 장르 탐색
        temp = 0
        for one in dic[key]:
            temp += one[0]
        check.append([temp, key])
        
    check.sort(reverse=True)
    
    for i in check:                                                         # 최대 장르에서 최대 2개씩 추출
        temp = []
        for j in dic[i[1]]:
            temp.append(j)
        temp = sorted(temp, key=lambda x : (x[0], -x[1]), reverse=True)
        if len(temp) > 1:
            for k in range(2):
                answer.append(temp[k][1])
        else:
            answer.append(temp[0][1])
            
    return answer
