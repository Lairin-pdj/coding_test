def solution(enroll, referral, seller, amount):
    # 코드로 계좌를 생성하고 부모가 누구인지 체크하는 명단 생성
    account = [0 for _ in range(len(enroll))]
    root = [i for i in range(len(enroll))]
        
    # 이름 해싱 및 부모 명단 갱신
    dic = {}
    for i, (child, parent) in enumerate(zip(enroll, referral)):
        dic[child] = i
        if parent in dic:
            root[dic[child]] = dic[parent]
            
    # 판매 장부를 기반으로 계좌에 금액 입력
    for sell, many in zip(seller, amount):
        money = many * 100
        code = dic[sell]
        
        # 부모를 타고 올라가며 수익 분배
        while code != root[code]:
            if money == 0:
                break
            
            # 분배
            account[code] += money - (money // 10)
            money = money // 10
            
            # 부모의 코드로 변경
            code = root[code]
        
        # 마지막으로 센터까지 분배
        money = money - (money // 10)
        account[code] += money
    
    return account
