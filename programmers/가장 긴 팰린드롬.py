def solution(s):
    answer = 0
    
    # 모든 부분 문자열에 대해 실시
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            temp = s[i:j]
            # 뒤집은 것과 일치여부 판단
            if temp == temp[::-1]:
                # 같을 경우 최댓값 반영
                answer = max(answer, j - i)

    return answer
