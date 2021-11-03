def solution(prices):
    answer = []
    
    # 얼마뒤에 떨어지는지 숫자마다 체크
    for i in range(len(prices) - 1):
        temp = 1
        for j in range(i + 1, len(prices) - 1):
            # 떨어질 경우 멈춤
            if prices[i] > prices[j]:
                break
            # 그렇지 않을 경우 이어나감
            else:
                temp += 1
        # 기록을 저장
        answer.append(temp)
    
    # 맨 마지막은 무조건 0이므로 삽입
    answer.append(0)
    
    return answer
