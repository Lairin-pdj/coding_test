# 차이에 대해 횟수를 반환해주는 함수
def count(diff):
    # 차이가 1, 1, 2, 2, 3, 3, 4, 4... 인 수열이기 때문에
    # n(n + 1)을 최대치로 계산 후 반절하여 2n or 2n - 1을 반환
    n = 1
    while n * (n + 1) < diff:
        n += 1
    
    if (n * (n + 1)) - n < diff:
        return 2 * n
    else:
        return 2 * n - 1

n = int(input())

for _ in range(n):
    # 각 케이스에 대해 차이값 반환
    a, b = map(int, input().split(" "))
    print(count(b - a))
