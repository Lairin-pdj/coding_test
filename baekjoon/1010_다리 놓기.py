import sys
input = sys.stdin.readline

# nCr 조합의 수를 반환하는 함수
def com(n, r):
    # 범위 밖 숫자일 경우 0 반환
    if r < 0 or n < r:
        return 0
        
    temp = 1
    for i in range(n, n - r, -1):
        temp *= i
    for i in range(1, r + 1):
        # float 오버플로를 막기 위해 
        temp = temp // i
    return temp

# 파싱
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    print(com(m, n))
