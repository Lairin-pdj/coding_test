import sys
input = sys.stdin.readline

# 파싱
s, a, b, c = map(int, input().split())

# nCr
def comb(n, r):
    if r < 0 or n < r:
        return 0
        
    temp = 1
    for i in range(n, n - r, -1):
        temp *= i
    for i in range(1, r + 1):
        # float 오버플로를 막기 위해 
        temp = temp // i
    return temp

# 불가능한 경우
if s > a + b + c:
    print(0)
# 가능한 경우
else:

    # 자유롭게 선택하는 경우의 수
    answer = (comb(s, a) * comb(s, b) * comb(s, c)) % 1000000007
    
    # 선택되지 않은 곡이 있는 경우의 수
    for i in range(1, s - max(a, b, c) + 1):
        temp = (comb((s - i), a) * comb((s - i), b) * comb((s - i), c) * comb(s, i)) % 1000000007
        answer += ((-1) ** i) * temp
        answer = answer % 1000000007

    # 결과 출력
    print(answer)
