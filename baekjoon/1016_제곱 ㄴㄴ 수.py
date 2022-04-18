import sys
input = sys.stdin.readline
    
# 파싱
최소, 최대 = map(int, input().split())
제곱수 = []
for 가 in range(2, int(최대 ** 0.5) + 1):
    제곱수.append(가 ** 2)

# 가능성 판별
가능성 = [True] * (최대 - 최소 + 1)
for 가 in 제곱수:
    모드 = 최소 % 가
    
    if 모드 != 0:
        for 나 in range(가 - 모드, 최대 - 최소 + 1, 가):
            가능성[나] = False
    else:
        for 나 in range(0, 최대 - 최소 + 1, 가):
            가능성[나] = False

# 결과 계산
갯수 = 0
for 가 in 가능성:
    if 가:
        갯수 += 1

# 결과 출력
print(갯수)
