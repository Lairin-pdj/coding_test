def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x : x[2])                 # 길이가 짧은 순으로 정렬
    check = set([costs[0][0]])
    
    while len(check) != n:                          # 붙일 수 있는 섬 중 거리가 가장 짧은 길 선택 반복
        for i, (a, b, c) in enumerate(costs):
            if a in check and b in check:
                continue
            elif a in check or b in check:
                answer += c
                check.update([a, b])
                costs.pop(i)
                break

    return answer
