def solution(lottos, win_nums):
    answer = []
    
    # 0의 갯수와 숫자일치 여부 체크
    check = 0
    zeroCount = 0
    for i in lottos:
        if i == 0:
            zeroCount += 1
        elif i in win_nums:
            check += 1
    
    # 체크된 내용에 따라 결과 
    best = min(7 - check - zeroCount, 6)
    worst = min(7 - check, 6)
    answer = [best, worst]
    
    return answer
