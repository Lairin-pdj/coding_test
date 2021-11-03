def solution(absolutes, signs):
    answer = 0
    
    # zip을 활용하여 분배
    for num, sign in zip(absolutes, signs):
        if sign:
            answer += num
        else:
            answer -= num
        
    return answer
