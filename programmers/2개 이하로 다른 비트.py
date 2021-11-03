def solution(numbers):
    answer = []
    
    # 숫자 별로 실행
    for number in numbers:
        # 바로 위의 수가 1개 차이나는 수이기 때문
        if number % 2 == 0:
            answer.append(number + 1)
        # 시작부터 연속되는 1의 갯수를 구하고 맨앞의 1을 2배하여 계산
        else:
            answer.append(number + ((number ^ (number + 1)) + 1) // 4)
                
    return answer
