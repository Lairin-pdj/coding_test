import sys
input = sys.stdin.readline

# 파싱
n, k = map(int, input().split())

# 이진수
answer = 0
while bin(n).count('1') > k:
    temp = 2 ** (bin(n)[::-1].index('1'))
    answer += temp
    n += temp
    
# 결과 출력
print(answer)
