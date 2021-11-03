def solution(n):
    answer = ''
    temp = n
    
    # 3으로 나누며 나머지를 answer에 입력
    while temp > 0:
        answer += str(temp % 3)
        temp = temp // 3
    
    # int함수를 이용하여 변환하여 출력
    return int(answer, 3)
