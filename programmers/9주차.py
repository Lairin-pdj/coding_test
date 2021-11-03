from collections import defaultdict

# 자식의 수를 구하는 재귀함수
def recur(before, now):
    global dic
    global c_count
    global root
    
    # 부모를 제외한 자기와 연결된 노드 들의 값의 합을 저장
    temp = 0
    for i in dic[now] - {before}:
        root[i] = now
        temp += recur(now, i)
    
    # 자식으로 저장
    c_count[now] += temp 
    
    # 재귀를 위한 값 반환
    return c_count[now]

def solution(n, wires):
    # 각 점마다 연결된 점 해싱
    global dic
    dic = defaultdict(set)
    for a, b in wires:
        dic[a].add(b)
        dic[b].add(a)
    
    # 자신을 포함한 자식 수
    global c_count
    c_count = [1] * (n + 1)
    
    # 루트 체크
    global root
    root = [i for i in range(n + 1)]
    
    # 재귀로 리스트들 완성
    recur(-1, 1)
    
    # 와이어별로 최댓값 체크
    low = n
    for a, b in wires:
        # a의 자식이 무조건 많도록 변경
        if c_count[a] < c_count[b]:
            a, b = b, a
        
        # 자식의 많은 쪽이 트리의 위쪽에 존재하므로
        # 아래쪽의 자식 수와 위쪽의 자식 수를 비교
        top = a
        while root[top] != top:
            top = root[top]
        
        low = min(low, abs((c_count[top] - c_count[b]) - c_count[b]))
    
    return low
