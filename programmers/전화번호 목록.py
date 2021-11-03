def solution(phone_book):
    phone_book.sort()                                       # 정렬을 이용하여 풀이
    
    for i in range(len(phone_book) - 1):                    # 정렬이 됬으므로 바로 다음에 같은 부분이 보이지 않으면 패스
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
        
    return True
