def solution(answers):
    answer = []
    
    # 배열의 좌표를 문제 번호의 mod계산으로 활용
    score = [0, 0, 0]
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 점수 계산
    for i in range(len(answers)):
        if p1[i % len(p1)] == answers[i]:
            score[0] += 1
        if p2[i % len(p2)] == answers[i]:
            score[1] += 1
        if p3[i % len(p3)] == answers[i]:
            score[2] += 1
    
    # 최대인 점수를 차례대로 입력
    for i in range(3):
        if score[i] == max(score):
            answer.append(i + 1)
    
    return answer
