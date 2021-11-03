from collections import defaultdict, deque

def solution(user_id, banned_id):
    answer = set()
    
    dic = defaultdict(list)                                 # 밴아이디에 대입 가능한 유저아이디 사전
    
    for m, i in enumerate(banned_id):                       # 조합을 통해 모든 경우의 수 체크
        for k, j in enumerate(user_id):
            check = True
            if len(i) != len(j):                            # 길이가 다르면 무조건 다름
                check = False
            else:
                for a, b in zip(i, j):                      # 길이가 같으면 비교 
                    if a != "*" and a != b:
                        check = False
                        break
            
            if check:                                       # 같다면 사전에 저장
                dic[i + "-" + str(m)].append(k)             # 중복 방지를 위해 숫자 첨가

    check = deque()
    check.append([-1, []])                                  # [처리수, 처리목록] 
    keys = list(dic.keys())                                 # 처리해야하는 밴아이디 종류
    
    while len(check) > 0:
        a, b = check.popleft()
        a += 1
        if a >= len(keys):
            b.sort()                                        # 집합이기 때문에 동일한 것으로 간주하기 위한 정렬
            answer.add(tuple(b))
        else:
            for i in dic[keys[a]]:                          # 순번에 맞는 것에 가능 목록
                if not i in b:                              # 중복 방지
                    temp = b[:]
                    temp.append(i)
                    check.append([a, temp])
    
    return len(answer)
