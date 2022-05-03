import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)
    
# 분리 집합
def find(n):
    if root[n] != n:
        # 루트를 찾아 올라가며 경로 압축 진행 및 거리 합산
        temp = find(root[n])
        dist[n] += dist[root[n]]
        root[n] = temp
        return root[n]
        
    return n

def union(i, j):
    # 센터를 무조건 하위로 붙이며 거리 설정
    root[i] = j
    dist[i] = abs(i - j) % 1000

# 파싱
t = int(input())
for _ in range(t):
    n = int(input())
    root = [i for i in range(n + 1)]
    dist = [0 for _ in range(n + 1)]
    while True:
        line = input().rstrip().split()
        
        # 명령어 종료
        if line[0] == "O":
            break
        # 찾으며 거리 갱신 후 값 출력
        elif line[0] == "E":
            find(int(line[1]))
            print(dist[int(line[1])])
        # union 진행
        elif line[0] == "I":
            union(int(line[1]), int(line[2]))
