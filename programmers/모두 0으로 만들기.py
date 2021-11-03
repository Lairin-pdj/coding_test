import sys, copy, math
from collections import defaultdict
sys.setrecursionlimit(300000) 

def dfs(now, before):
    # 전역변수 설정
    global answer, b, dic
    
    # 현재 노드에서 이어진 부분 재귀
    for i in dic[now]:
        # 방금 전 노드는 제외
        if i != before:
            dfs(i, now)
    
    # 값의 이동 
    answer += abs(b[now])
    b[before] += b[now]
    b[now] = 0

def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    # dfs를 위한 전역변수 설정
    global answer, dic, b
    b = a
    answer = 0
    dic = defaultdict(list)
    
    # 사전을 통해 그래프 연결점 파악
    for (x, y) in edges:
        dic[x].append(y)
        dic[y].append(x)
    
    # dfs(현재, 직전)
    dfs(0, 0)
        
    return answer
