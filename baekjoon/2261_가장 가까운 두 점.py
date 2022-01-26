import sys
input = sys.stdin.readline

# 파싱
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
points.sort()

# 거리 계산
def get(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

# 분할 정복
def div(low, high):
    # 점이 1개인 경우
    if low == high:
        return float('inf')
    
    # 점이 2개인 경우
    if high - low == 1:
        return get(points[high], points[low])
    
    # 점이 3개 이상인 경우
    mid = (low + high) // 2
    # x축의 거리 계산
    dist = min(div(low, mid), div(mid, high))
    
    # 거리 기준으로 후보 탐색
    candi = []
    for i in range(low, high + 1):
        if (points[mid][0] - points[i][0]) ** 2 < dist:
            candi.append(points[i])
    
    # 후보군 들을 y축으로 재정렬
    candi.sort(key = lambda x : x[1])
    
    # y축을 포함하여 거리 체킹
    mindist = dist
    for i in range(len(candi) - 1):
        for j in range(i + 1, len(candi)):
            # 작을 경우 체크
            if (candi[i][1] - candi[j][1]) ** 2 < mindist:
                mindist = min(mindist, get(candi[i], candi[j]))
            # 기준보다 멀어지고 나면 그 뒤는 더이상 불가능 하기에 탈출
            else:
                break
    
    # 최소거리 반환
    return mindist

# 결과 출력
print(div(0, n - 1))
