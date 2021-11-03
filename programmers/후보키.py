from itertools import combinations

def solution(relation):
    canset = []
    
    bar = [i for i in range(len(relation[0]))]
    
    for i in range(len(relation[0])):
        for keys in combinations(bar, i + 1):           # 1 ~ n까지 키 조합 선택
            temp = set()                                # 집합을 이용해 중복 걸러내기
            for j in range(len(relation)):
                tempk = []
                for k in keys:
                    tempk.append(relation[j][k])
                temp.add(tuple(tempk))

            if len(temp) == len(relation):              # 길이가 같다는 건 중복이 없으니 가능한 키
                canset.append(set(keys))

    i = 0
    while i < len(canset) - 1:                          # 가능한 키들의 최소성 체크
        j = i + 1
        while j < len(canset):
            if canset[i] & canset[j] == canset[i]:
                canset.remove(canset[j])
            else:
                j += 1
        i += 1
        
    return len(canset)
