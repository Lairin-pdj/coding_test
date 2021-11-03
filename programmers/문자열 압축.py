def solution(s):
    answer = 1000
    
    for i in range(1, (len(s) // 2) + 2):                       # 자르는 갯수 늘려가며 반복
        stack = []
        for j in range((len(s) // i)):                          # 스택을 이용하여 자르것들 비교
            if len(stack) == 0 or s[i * j:i * (j + 1)] != stack[-1][0]:
                stack.append([s[i * j:i * (j + 1)], 1])
            else:
                count = stack[-1][1]
                stack.pop()
                stack.append([s[i * j:i * (j + 1)], count + 1])
        
        temp = ''
        total = 0
        for n, c in stack:                                      # 실제 압축표현으로 치환
            temp += n
            if c >= 2:
                total += len(str(c))
        
        answer = min(answer, (len(temp) + len(s) % i + total))  # 길이가 짧은 것 채택
                
    return answer
