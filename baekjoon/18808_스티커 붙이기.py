import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

# 주어진 2차원 배열을 회전시켜주는 함수
def rotate(n):
    # 열 단위로 따서 뒤집어서 넣어 90도 회전
    # 1 2 3    1 4 7    7 4 1
    # 4 5 6 -> 2 5 8 -> 8 5 2
    # 7 8 9    3 6 9    9 6 3
    return list(map(list, zip(*n[::-1])))

# t 배열에 k 배열을 적용할 수 있는지 체크하는 함수
def check(t, k, m, n):
    for i in range(len(k)):
        for j in range(len(k[0])):
            if t[m + i][n + j] + k[i][j] > 1:
                return False
    return True

# t 배열에 k 배열을 더해주는 함수
def attach(t, k, m, n):
    temp = 0
    
    for i in range(len(k)):
        for j in range(len(k[0])):
            t[m + i][n + j] += k[i][j]
            
            if k[i][j] == 1:
                temp += 1
    
    return temp

# 파싱
n, m, k = map(int, input().split())
table = [[0] * m for _ in range(n)]

# 스티커 별 체크
answer = 0
for _ in range(k):
    r, c = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(r)]
    
    # 회전 체크
    flag = False
    for _ in range(4):
        # 왼쪽 위부터 삽입 가능 체크
        for i in range(n - len(temp) + 1):
            for j in range(m - len(temp[0]) + 1):
                if check(table, temp, i, j):
                    answer += attach(table, temp, i, j)
                    flag = True
                    break
            
            if flag:
                break
        
        if flag:
            break
        
        # 회전
        temp = rotate(temp)

# 결과 출력
print(answer)
