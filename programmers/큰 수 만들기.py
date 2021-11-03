def solution(number, k):
    count = 0
    
    i = 1
    while i < len(number):
        if count >= k:
            break
        if int(number[i - 1]) < int(number[i]):         # 전 숫자 보다 클 경우 앞 숫자 삭제 
            number = number[:i - 1] + number[i:]
            count += 1
            if i > 1:
                i -= 1
        else:
            i += 1
    
    if count != k:                                      # k를 삭제하지 못한 경우 추가 삭제
        number = number[:count - k]
            
    return number
