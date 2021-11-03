from collections import defaultdict

def solution(tickets):
    # 사전으로 정리할 때 알파벳 순의 역순으로 정리하기 위함
    tickets.sort(reverse=True)
    
    dic = defaultdict(list)
    # 사전으로 정리
    for (a, b) in tickets:
        dic[a].append(b)
    
    # 시작점 설정
    stack = ["ICN"]
    answer = []
    while stack:
        # 스택의 맨 뒤인 현재 위치에서 갈 수 있는 지점 확인
        top = stack[-1]
        # 현재 위치에서 출발하는 표가 없거나 표를 다 사용한 경우
        # 모든 표를 사용해야한다는 조건에 의해 더 이상 갈 곳이 없는 위치는 도착지로 확정
        if top not in dic or len(dic[top])==0:
            answer.append(stack.pop())
        else:
            stack.append(dic[top].pop())
    
    # 도착지부터 삽입하였기에 뒤집은 후 반환
    answer.reverse()
    return answer
