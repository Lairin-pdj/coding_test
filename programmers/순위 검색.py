from collections import defaultdict

def solution(info, query):
    dic = defaultdict(list)
    
    # dic을 통해 지원자 정보 해싱
    for appli in info:
        # 지원자 정보 파싱
        lan, tp, car, food, score = appli.split(" ")
        score = int(score)
        # 포함 가능한 모든 경우의 수를 사전에 입력
        for a in ["-", lan]:
            for b in ["-", tp]:
                for c in ["-", car]:
                    for d in ["-", food]:
                        dic[a + b + c + d].append(score)
    
    # 점수 이분탐색을 위한 정렬
    for value in dic.values():
        value.sort()
    
    # 쿼리 진행
    answer = []
    for quest in query:
        # 쿼리 파싱
        temp = quest.split(" ")
        # 지원자 명단 
        check = dic[temp[0] + temp[2] + temp[4] + temp[6]]
        target = int(temp[7])
        
        # 이분탐색
        start = 0
        mid = 0
        end = len(check)
        while start < end:
            mid = (start + end) // 2
            if check[mid] < target:
                start = mid + 1
            elif check[mid] >= target:
                end = mid
        
        # 결과 삽입
        answer.append(len(check) - start)
    
    return answer
