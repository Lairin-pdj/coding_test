def solution(numbers):
    strNums = []
    for num in numbers:                         # 각 숫자들을 정렬순으로 비교할 수 있게 변환
        temp = []
        for i in str(num):
            temp.append(int(i))
        while len(temp) < 4:
            temp.append(int(str(num)[0]))
        temp.append(len(str(num)))
        if len(str(num)) != 4 and temp[0] > temp[1]:
            temp[3] += temp[4]
        strNums.append(temp)
        
    sortNums = sorted(strNums, key = lambda x : (-x[0], -x[1], -x[2], -x[3], x[4]))
    
    answer = ""
    for i in sortNums:                          # 정렬된 숫자들을 자릿수 만큼 붙여넣기
        for j in range(i[4]):
            answer += str(i[j])
            
    if int(answer) == 0:
        return "0"
    return answer
