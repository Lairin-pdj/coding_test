from collections import Counter

def solution(s):
    
    total = 0
    count = 0
    
    while True:
        # 0과 1의 갯수 확인
        temp = Counter(s)
        zero = temp["0"]
        one = temp["1"]
        
        # 다음 문자 생성
        new = str(bin(one))[2:]
        
        # 1인지 확인 후 결과 값 저장 혹은 반복
        if new == "1":
            return [count + 1, total + zero]
        else:
            count += 1
            total += zero
            s = new
