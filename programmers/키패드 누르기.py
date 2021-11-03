def solution(numbers, hand):
    answer = ''
    #1 2 3 4 5 6 7 8 9 * 0  #   (real)
    #0 1 2 3 4 5 6 7 8 9 10 11  (code)
    
    # 초기값 설정
    left = 9
    right = 11
    
    # 주어진 번호를 순서대로 진행
    for temp in numbers:
        # 0일 경우 추가 조정
        if temp == 0:
            temp = 11
            
        # 실제번호를 코드로 변환
        i = temp - 1
        
        # 주어진 조건에 맞게 손가락 선택 및 이동
        if i in [0, 3, 6]:
            answer += 'L'
            left = i
        elif i in [2, 5, 8]:
            answer += 'R'
            right = i
        else:
            # 거리 계산
            leftDis = abs(i % 3 - left % 3) + abs(i // 3 - left // 3)
            rightDis = abs(i % 3 - right % 3) + abs(i // 3 - right // 3)
            
            # 거리에 따라 선택 및 이동
            if leftDis > rightDis:
                answer += 'R'
                right = i
            elif leftDis < rightDis:
                answer += 'L'
                left = i
            else:
                # 거리가 같을 경우 손잡이에 따라 선택 및 이동
                if hand == "left":
                    answer += 'L'
                    left = i
                else:
                    answer += 'R'
                    right = i
            
    return answer
