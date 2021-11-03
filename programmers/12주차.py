import sys
sys.setrecursionlimit(100000)

# 재귀를 이용한 dfs
def dfs(count, k, explored):
    global answer
    global duns
    
    # 최대치 체크
    answer = max(answer, count)
    
    # 입장 가능한 던전 체크
    for minimum, consume in duns:
        if [minimum, consume] not in explored:
            if k >= minimum:
                dfs(count + 1, k - consume, explored + [[minimum, consume]])

                
def solution(k, dungeons):
    global answer
    answer = -1
    global duns
    duns = dungeons
    
    # 재귀 실행
    dfs(0, k, [])
    
    # 결과값 반환
    return answer
