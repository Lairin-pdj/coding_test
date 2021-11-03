from collections import Counter

def solution(a):
    answer = 0
    if len(a) == 1:                                                 # 길이가 1이면 만족하는 스타수열이 없으므로 0반환
        return 0
    
    count = Counter(a)
    
    for x, y in count.items():                                      # 각 숫자 하나씩을 이용하여 만들 수 있는 스타수열의 최대치 계산 
        if answer >= y * 2:
            continue
        
        i = 0
        check = 0
        while i < len(a) - 1:                                       # 주어진 숫자로 만들 수 있는 쌍 갯수 체크
            if (a[i] == x or a[i + 1] == x) and a[i] != a[i + 1]:
                i += 2
                check += 1
            else:
                i += 1
                
        answer = max(check * 2, answer)                             # 최댓값 갱신
    
    return answer
