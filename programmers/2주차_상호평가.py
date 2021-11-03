def solution(scores):
    answer = ""
    
    # 인별 점수로 변경
    score = list(zip(*scores))
    # 각자의 점수에 대해서
    for i, x in enumerate(score):
        high = max(x)
        low = min(x)
        avg = 0
        
        # 평균계산
        if (x[i] == high or x[i] == low) and x.count(x[i]) == 1:
            avg = sum(x[:i] + x[i + 1:]) / (len(x) - 1)
        else:
            avg = sum(x) / len(x)
        
        # 점수 부여
        if avg >= 90:
            answer += "A"
        elif avg >= 80:
            answer += "B"
        elif avg >= 70:
            answer += "C"    
        elif avg >= 50:
            answer += "D"
        else:
            answer += "F"
            
    return answer
