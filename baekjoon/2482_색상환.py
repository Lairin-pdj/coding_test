import sys

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

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

# 부동소수점 오차를 막기 위해 최종 int 연산
# 선택할 K개를 제외한 N - K개를 기본 배치
# 그 사이 거리인 N - K + 1개의 공간에 K를 순서없이 나열
# 양 끝이 전부 선택된다면 원형에서 이웃하게되는 결과를 초래
# 여사건으로 활용하여 양 끝이 선택되고 남은 N - K - 1개의 공간에서 K - 2개 뽑는 수를 제외
print(int(com(N - K + 1, K) - com(N - K - 1, K - 2)) % 1000000003)
