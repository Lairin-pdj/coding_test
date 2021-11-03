def solution(s):
    answer = []
    temp = set()
    
    # 숫자 집합으로 만든 뒤 갯수로 정렬
    a = list(map(lambda x : set(map(int, x.split(","))), s[2:-2].split("},{")))
    b = sorted(a, key=lambda x : len(x))
    
    # 차집합을 이용 숫자를 하나씩 추출하여 반환
    for i in range(len(b)):
        num = (b[i] - temp).pop()
        temp.add(num)
        answer.append(num)

    return answer
